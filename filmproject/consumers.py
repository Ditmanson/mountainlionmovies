import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Conversation, Message
from .serializers import MessageSerializer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connection attempt...")  # Debug: Connection attempt
    
        # Ensure the user is authenticated
        if not self.scope['user'].is_authenticated:
            print("WebSocket connection rejected: User not authenticated")
            await self.close()
            return

        self.user = self.scope['user']
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.room_group_name = f'chat_{self.conversation_id}'

        print(f"User: {self.user}, Conversation ID: {self.conversation_id}, Room Group: {self.room_group_name}")

        # Verify the conversation exists and the user is a participant
        self.conversation = await sync_to_async(self.get_conversation)()
        if not self.conversation:
            print(f"Conversation {self.conversation_id} does not exist or user is not a participant")
            await self.close()
            return

        # Join the WebSocket group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print(f"WebSocket connection accepted. User {self.user} joined room {self.room_group_name}")
        await self.accept()

    async def disconnect(self, close_code):
        print(f"WebSocket disconnect: User {self.user}, Room {self.room_group_name}, Close Code: {close_code}")
        # Leave the WebSocket group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print(f"Message received: {text_data}")  # Debug: Message received

        # Parse incoming message
        try:
            data = json.loads(text_data)
            message_content = data['message']
            print(f"Parsed message content: {message_content}")  # Debug: Message parsed
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return

        # Save the message in the database
        try:
            saved_message = await sync_to_async(self.save_message)(message_content)
            print(f"Message saved to database: {saved_message}")
        except Exception as e:
            print(f"Error saving message: {e}")
            return

        # Serialize and broadcast the message to the group
        serialized_message = MessageSerializer(saved_message).data
        print(f"Broadcasting message: {serialized_message}")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': serialized_message,
            }
        )

    async def chat_message(self, event):
        # Send the serialized message to the WebSocket
        print(f"Sending message to WebSocket: {event['message']}")
        await self.send(text_data=json.dumps(event['message']))

    # Helper methods
    def get_conversation(self):
        """
        Verify that the conversation exists and the user is a participant.
        """
        print(f"Fetching conversation {self.conversation_id} for user {self.user}")
        try:
            conversation = Conversation.objects.get(id=self.conversation_id)
            if self.user in conversation.participants.all():
                print(f"Conversation found: {conversation}")
                return conversation
            print("User is not a participant in the conversation")
            return None
        except Conversation.DoesNotExist:
            print("Conversation does not exist")
            return None

    def save_message(self, content):
        """
        Save a new message in the conversation.
        """
        print(f"Saving message to conversation {self.conversation_id}: {content}")
        return Message.objects.create(
            conversation=self.conversation,
            sender=self.user,
            content=content
        )
