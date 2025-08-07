document.addEventListener('DOMContentLoaded', initChatbot);

function initChatbot() {
    createChatbotUI();
    registerEventHandlers();
}

function createChatbotUI() {
    const chatbotHTML = `
    <div class="chatbot-icon" id="chatbotIcon">
        <i class="bi bi-chat-dots-fill"></i>
    </div>

    <div class="chatbot-window" id="chatbotWindow">
        <div class="chatbot-header">
            <span>Chatbot</span>
            <button id="closeChatbot">X</button>
        </div>
        <div class="chatbot-body">
            <div class="chatbot-messages" id="chatbotMessages">
                <!-- 메시지 뜨는 곳 -->
            </div>
            <div class="chatbot-input-container">
                <input type="text" id="chatbotInput" placeholder="메시지를 입력하세요">
                <button id="sendMessage">Send</button>
            </div>
        </div>
    </div>`
    document.body.insertAdjacentHTML('beforeend', chatbotHTML)
}

function registerEventHandlers() {
    const chatbotIcon = document.getElementById('chatbotIcon')
    const chatbotWindow = document.getElementById('chatbotWindow')
    const closeChatbot = document.getElementById('closeChatbot')
    const chatbotInput = document.getElementById('chatbotInput')
    const sendMessage = document.getElementById('sendMessage')

    chatbotIcon.addEventListener('click', () => {
        console.log('열기')
        chatbotIcon.style.display = 'none';
        chatbotWindow.style.display = 'flex';
    })
    
    closeChatbot.addEventListener('click', () => {
        console.log('닫기')
        chatbotIcon.style.display = 'flex';
        chatbotWindow.style.display = 'none';
    })

    sendMessage.addEventListener('click', handleUserMessage);
    chatbotInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleUserMessage();
    })

}

async function handleUserMessage() {
    const input = document.getElementById('chatbotInput');
    const message = input.value.trim();
    if (!message) return;

    addMessage(message, 'user');
    // const botResponse = '[BOT]' + input.value;
    input.value = ''
    // addMessage(botResponse, 'bot')
    const chatbot = await sendMessageToServer(message)
    addMessage(chatbot, 'chatbot')

}

function addMessage(message, sender) {
    const container = document.getElementById('chatbotMessages')

    const messageElement = document.createElement('div');
    messageElement.innerHTML = sender === 'user'
        ?`<i class="bi bi-person"></i> ${message}`
        :`<i class="bi bi-robot"></i> ${message}`
    messageElement.classList.add(sender, 'message', 'message-bubble');

    container.appendChild(messageElement);
    container.scrollTop = container.scrollHeight;
}


const ECHO_MODE = false;

async function sendMessageToServer(userInput) {
    if (ECHO_MODE) {
        return `Echo: ${userInput}`
    }
    console.log('서버로 보낼 메시지 : ', userInput)
    const response = await fetch('/api/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({userInput})
    });

    const data = await response.json();
    console.log('서버응답:', data)
    get_todolist()
    return data; // 나중에 서버의 응답 변수로 변경해야함.
}