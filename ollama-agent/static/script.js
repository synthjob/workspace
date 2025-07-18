function sendPrompt() {
    const prompt = document.getElementById("prompt").value;
    fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({prompt})
    })
    .then(res => res.json())
    .then(data => document.getElementById("response").innerText = data.response || "Yanıt yok")
    .catch(err => document.getElementById("response").innerText = "Hata: " + err);
}
