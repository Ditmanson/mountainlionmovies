from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Conversation, User
from django.db.models import Q


@login_required
def all_conversations(request):
    # Preprocess conversations
    conversations = []
    for conversation in request.user.conversations.all():
        other_participant = conversation.participants.exclude(id=request.user.id).first()
        conversations.append({
            'id': conversation.id,
            'other_participant': other_participant.username if other_participant else "Unknown",
        })

    return render(request, 'filmproject/instant_messenger_all_conversations.html', {
        'conversations': conversations,
    })

@login_required
def one_conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    return render(request, 'filmproject/instant_messenger_one_conversation.html', {'conversation': conversation})

@login_required
def start_conversation(request, friend_id):
    # Ensure the friend exists
    friend = get_object_or_404(User, id=friend_id)

    # Compare against Viewer objects
    friend_viewer = friend.viewer  # Get the Viewer object for the friend

    print(f"Logged-in user: {request.user.viewer}")
    print(f"Target friend: {friend}")
    print(f"Logged-in user's friends: {list(request.user.viewer.friends.all())}")

    if friend_viewer not in request.user.viewer.friends.all():
        print("Users are not friends.")
        return redirect('profile_viewer', viewer_id=friend_id)

    # Check if a conversation already exists
    conversation = Conversation.objects.filter(
        Q(participants=request.user) & Q(participants=friend)
    ).first()
    if not conversation:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, friend)
        print(f"New conversation created with ID: {conversation.id}")
    else:
        print(f"Existing conversation found with ID: {conversation.id}")

    return redirect('chat_one_conversation', conversation_id=conversation.id)

