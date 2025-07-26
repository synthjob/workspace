const chatBox = document.getElementById('chat-box');
const form = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

function addMessage(sender, text) {
  const div = document.createElement('div');
  div.className = 'message ' + sender;
  div.innerHTML = `<span class="${sender}">${sender === 'user' ? 'Sen' : 'Ollama'}:</span> ${text}`;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const input = userInput.value;
  addMessage('user', input);
  userInput.value = '';
  // Backend'e mesaj gönder
  const res = await fetch('/ask', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message: input})
  });
  const data = await res.json();
  addMessage('ollama', data.reply);
});
