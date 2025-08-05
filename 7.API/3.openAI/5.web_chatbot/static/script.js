console.log('로딩')

document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-container')
    const userInputForm = document.getElementById('user-input-form')
    const userInputField = document.getElementById('user-input')
    const loadingIndicator = document.getElementById('loading-indicator')

    userInputForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const userInput = userInputField.value;
        userInputField.value = '';
        appendMessage('user', userInput)
        scrollToBottom()
        showLoadingIndicator();
         
        const chatGPTResponse = await getChatGPTResponse(userInput)
        console.log(chatGPTResponse)
        hideLoadingIndicator();
        appendMessage('chatbot', chatGPTResponse)
        scrollToBottom()
    })
})


    function showLoadingIndicator() {
        loadingIndicator.style.display = 'flex';
    }

    function hideLoadingIndicator() {
        loadingIndicator.style.display = 'none';
    }

    function scrollToBottom() {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }


    function appendMessage(role, content) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', role)
        messageDiv.innerText = `${role}: ${content}`
        chatContainer.appendChild(messageDiv)
    }

    async function getChatGPTResponse(userinput) {
        const response = await fetch('/api/chat/', {
            method: "post",
            headers: {'content-type': 'application/json; charset=UTF-8'},
            body: JSON.stringify(userinput)
        })

        const data = await response.json()
        console.log(data)
        return data.response
    }