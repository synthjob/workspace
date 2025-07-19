const messages = document.getElementById('messages');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const fileInput = document.getElementById('fileInput');
const attachBtn = document.getElementById('attachBtn');
let attachedImage = null;

attachBtn.addEventListener('click', () => fileInput.click());
fileInput.addEventListener('change', () => {
  if (fileInput.files[0]) {
    attachedImage = fileInput.files[0];
    attachBtn.textContent = "🖼️";
  }
});

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', e => {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(e);}
});
document.getElementById('input-bar').addEventListener('submit', e => {e.preventDefault(); sendMessage(e);});

function appendMessage(owner, content, isImage = false) {
  const msg = document.createElement('div');
  msg.className = `message ${owner}`;
  if (isImage && content) {
    const img = document.createElement('img');
    img.src = content; img.style.maxWidth = '100%'; img.style.borderRadius = '7px'; img.style.marginTop='6px';
    msg.innerHTML = owner === 'user' ? "Sen<br>" : "Bot<br>";
    msg.appendChild(img);
  } else {
    msg.innerText = (owner === 'user' ? "Sen: " : "Bot: ") + content;
  }
  messages.appendChild(msg);
  messages.scrollTop = messages.scrollHeight;
}

async function sendMessage(e) {
  let text = userInput.value.trim();
  if (!text && !attachedImage) return;
  if (text) appendMessage('user', text);
  if (attachedImage) {
    let imgURL = URL.createObjectURL(attachedImage);
    appendMessage('user', imgURL, true);
  }
  userInput.value = "";
  attachBtn.textContent = "📎";

  // Multimodal API (GEMMA3n:e4b veya backend'in neyi gerektiriyorsa ayarlanmalı)
  let formData = new FormData();
  formData.append('text', text);
  if (attachedImage) formData.append('image', attachedImage);

  let res;
  try {
      res = await fetch('http://localhost:11434/api/chat', {
      method: 'POST',
      body: formData
    });
    let data = await res.json();
    if (data.imageUrl) appendMessage('ai', data.imageUrl, true);
    if (data.response) appendMessage('ai', data.response);
  } catch {
    appendMessage('ai', '[Bağlantı başarısız]', false);
  }
  attachedImage = null;
}
