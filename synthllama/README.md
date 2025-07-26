# SynthLLaMA
Bu klasör, SynthLLaMA ile ilgili tüm proje ve dokümantasyonları içerir.

## İçindekiler
- `index.html` : Ana sohbet arayüzü (Ollama ile sohbet)
- `style.css` : Chat uygulaması için tasarım
- `app.js` : Sohbetin dinamiği ve arayüz işlevleri
- `backend.py` : FastAPI backend & Ollama entegrasyonu
- `changelog.md` : Değişiklik geçmişi

## Kullanım
1. Bu klasörü bilgisayarına klonla veya indir.
2. Gerekli Python kütüphanelerini yükle:
   ```
   pip install fastapi uvicorn requests
   ```
3. Ollama'nın arka plandaki API sunucusunun çalıştığından emin ol.
4. FastAPI backend uygulamasını başlat:
   ```
   uvicorn backend:app --reload
   ```
5. Tarayıcıdan `http://localhost:8000` adresine gir ve chat ekranını kullan!

## Notlar
- Kodlar temel örnek olup, özelleştirmeye ve geliştirmeye açıktır.
- Destek veya katkı eklemek için changelog dosyasına veya bu dokümana güncelleme girebilirsin.
