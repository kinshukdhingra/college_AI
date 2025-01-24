// Function to send a message and receive a response from the backend
async function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (!userInput) return;  // Prevent sending empty messages

    // Display user's message at the bottom
    displayMessage(userInput, 'user');

    // Send message to backend
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    });

    const data = await response.json();
    const botResponse = data.response;

    // Display bot's response at the bottom
    displayMessage(botResponse, 'bot');

    // Clear input field
    document.getElementById('userInput').value = '';
}

// Function to display messages in the chat
function displayMessage(message, sender) {
    const chatMessages = document.querySelector('.chat-messages');

    // Create new message div
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('chat-message', sender);
    messageDiv.textContent = message;

    // Append message to the chat (at the bottom)
    chatMessages.appendChild(messageDiv);

    // Scroll to the bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Optional: Enable sending messages when pressing Enter
document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});


