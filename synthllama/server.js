const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();
const PORT = 3000;

app.use(express.json());

app.post('/ask', async (req, res) => {
  try {
    const ollamaRes = await axios.post('http://localhost:11434/api/chat', {
      model: 'llama3',
      messages: [{ role: 'user', content: req.body.message }]
    });
    res.json({ reply: ollamaRes.data.message.content });
  } catch (error) {
    res.status(500).json({ error: String(error) });
  }
});

app.use(express.static(path.join(__dirname)));

app.listen(PORT, () => {
  console.log(`Sunucu http://localhost:${PORT} adresinde çalışıyor!`);
});
