# SynthLLaMA
Bu klasör, SynthLLaMA ile ilgili tüm proje ve dokümantasyonları içerir.

## İçindekiler
- `index.html` : Ana sohbet arayüzü (Ollama ile sohbet)
- `style.css` : Chat uygulaması için tasarım
- `app.js` : Sohbetin dinamiği ve arayüz işlevleri
- `server.js` : Node.js/Express backend & Ollama entegrasyonu
- `changelog.md` : Değişiklik geçmişi

## Kurulum ve Kullanım

1. Bu klasörü bilgisayarına klonla veya indir.

2. Proje klasörünü başlat:
   ```
   npm init -y
   ```

3. Gerekli Node.js paketlerini yükle:
   ```
   npm install express axios
   ```

4. Ollama'nın arka plandaki API sunucusunun çalıştığından emin ol.

5. Node.js backend uygulamasını başlat:
   ```
   node server.js
   ```

6. Tarayıcıdan `http://localhost:3000` adresine gir ve chat ekranını kullan!

## Notlar
- Kodlar temel örnek olup, özelleştirmeye ve geliştirmeye açıktır.
- Destek veya katkı eklemek için changelog dosyasına veya bu dokümana güncelleme girebilirsin.
