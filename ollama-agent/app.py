from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
    ollama_url = "http://localhost:11434/api/generate"
    payload = {"model": "llama3", "prompt": prompt, "stream": False}
    response = requests.post(ollama_url, json=payload)
    if response.status_code == 200:
        cevap = response.json().get("response", "")
    else:
        cevap = "Ollama API hatası!"
    return jsonify({"response": cevap})

if __name__ == "__main__":
    app.run(debug=True)
