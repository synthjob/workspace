# Ollama Agent

Bu klasör, Ollama Agent projesinin ana dizinidir. HTML, CSS, JavaScript ve Python/Flask kullanılarak geliştirilmiştir. Proje; web arayüzünden komut/prompt yazarak Ollama sunucusunda konuşan bir yapay zeka ile etkileşime geçmenizi sağlar.

## Kurulum

1. Gerekli Python paketlerini yükle:
```
pip install -r requirements.txt
```

2. Ollama'nın kurulu ve çalışıyor olduğundan emin olun (ör: `ollama serve` ile başlatın; model olarak `llama3`, `mistral`, vs. yükleyebilirsiniz).

3. Uygulamayı başlatın:
```
python app.py
```

4. Tarayıcıdan [http://localhost:5000](http://localhost:5000) adresine gidin.

## Klasör Yapısı

```
ollama-agent/
├── app.py
├── requirements.txt
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
└── README.md
```

## Açıklama
- Python/Flask backend ile web arayüzü üzerinden prompt gönderebilir, arka planda Ollama API yanıtlarını alabilirsin.
- static/ içerisinde projenin stilleri (CSS) ve JavaScript dosyaları yer alır.
- templates/ içerisinde index.html ana arayüzdür.
- Tüm modern Python ortamlarında çalışır.
