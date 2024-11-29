const chatSocket = new WebSocket(
    `ws://${window.location.host}/ws/chat/${conversationId}/`
);

chatSocket.onmessage = function (event) {
    try {
        const data = JSON.parse(event.data);

        // Log the received data for debugging
        console.log("Received WebSocket data:", data);

        // Extract and validate fields from the data
        const username = data.sender || "Unknown"; // Use a default value if sender is missing
        const content = data.content || "";

        // Append the message to the chat log
        const chatLog = document.getElementById("chat-log");
        chatLog.innerHTML += `<p><strong>${username}:</strong> ${content}</p>`;
    } catch (error) {
        console.error("Error processing WebSocket message:", error);
    }
};

chatSocket.onopen = function () {
    console.log("WebSocket connection established.");
};

chatSocket.onclose = function (e) {
    console.error("WebSocket closed unexpectedly. Code:", e.code, "Reason:", e.reason);
};

chatSocket.onerror = function (e) {
    console.error("WebSocket encountered an error:", e);
};



document.querySelector("#chat-message-submit").onclick = function (e) {
    const messageInput = document.querySelector("#chat-message-input");
    const message = messageInput.value;

    if (message.trim()) {
        chatSocket.send(JSON.stringify({ message }));
        messageInput.value = ""; // Clear the input field
    }
};
