// renderer.js - Modern fonksiyonel chat UI ve bağlantı/model kontrolü

const chatArea = document.getElementById('chatArea');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', function(e) {
  if (e.key === 'Enter') {
    sendMessage();
  }
});

function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;
  appendMessage('Sen', message);
  userInput.value = '';

  // Burada Ollama API'ye istek atabilirsin (örn. axios ile)
  // Özelleştirilebilir alan:
  /*
  axios.post('http://localhost:11434/api/chat', {
    message: message
  }).then(res => {
    appendMessage('Bot', res.data.response);
  });
  */
}

function appendMessage(owner, text) {
  chatArea.value += `${owner}: ${text}\n`;
  chatArea.scrollTop = chatArea.scrollHeight;
}
