// instant_messenger_one_conversation.js

const chatSocket = new WebSocket(
    `ws://${window.location.host}/ws/chat/${conversationId}/`
);


chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const chatLog = document.querySelector('#chat-log');
    const newMessage = document.createElement('p');
    newMessage.textContent = `${data.sender}: ${data.message}`;
    chatLog.appendChild(newMessage);
    chatLog.scrollTop = chatLog.scrollHeight;  // Auto-scroll to the bottom
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    const input = document.querySelector('#chat-message-input');
    const message = input.value;
    chatSocket.send(JSON.stringify({ 'message': message }));
    input.value = '';
};
