from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests

Ollama_API_URL = "http://localhost:11434/api/chat"  # Kendi sunucu adresinle gerekirse değiştir

app = FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
def root():
    return FileResponse('index.html')

@app.post("/ask")
async def ask_ollama(msg: Message):
    payload = {
        "model": "llama3",  # Ollama'da yüklü model ismini kullan
        "messages": [{"role": "user", "content": msg.message}]
    }
    response = requests.post(Ollama_API_URL, json=payload)
    reply = response.json()["message"]["content"]
    return JSONResponse(content={"reply": reply})

# Çalıştırmak için: uvicorn backend:app --reload
