# Synthllama - Electron Tabanlı Node.js Masaüstü Chatbot Template

Electron ve Node.js kullanarak geliştirilmiş bir masaüstü chatbot uygulaması template'i. Ollama entegrasyonu ile yerel AI modelleri kullanarak sohbet edebilmenizi sağlar.

## Dosya Yapısı

```
synthllama/
├── main.js          # Ana Electron process dosyası
├── renderer.js      # Renderer process (UI) mantığı
├── preload.js       # Güvenli API köprüsü
├── index.html       # Ana HTML arayüzü
├── package.json     # Proje bağımlılıkları ve yapılandırması
└── README.md        # Bu dosya
```

## Kurulum

### Ön Gereksinimler
- Node.js (v14 veya üzeri)
- npm veya yarn paket yöneticisi
- Ollama (yerel AI modeli için)

### Kurulum Adımları

1. Proje klasörüne gidin:
   ```bash
   cd synthllama
   ```

2. Bağımlılıkları yükleyin:
   ```bash
   npm install
   ```

3. Ollama'yı kurun ve bir model indirin:
   ```bash
   # Ollama kurulumu (https://ollama.ai)
   ollama pull llama2  # veya istediğiniz model
   ```

## Başlatma

Uygulamayı başlatmak için:

```bash
npm start
```

veya

```bash
electron .
```

## Temel Özellikler

- ✅ **Masaüstü Uygulaması**: Electron ile cross-platform masaüstü desteği
- ✅ **Yerel AI Entegrasyonu**: Ollama ile yerel AI modelleri kullanımı
- ✅ **Modern Arayüz**: HTML5, CSS3 ve JavaScript ile responsive tasarım
- ✅ **Güvenli Mimari**: Preload script ile güvenli API erişimi
- ✅ **Hızlı Başlangıç**: Template yapısı ile kolay geliştirme

## Kullanım Adımları

1. **Uygulamayı Başlatın**: `npm start` komutu ile uygulamayı çalıştırın
2. **Model Seçimi**: Ollama'da yüklü olan modellerden birini seçin
3. **Sohbet Başlatın**: Metin kutusuna mesajınızı yazıp Enter'a basın
4. **AI Yanıtı**: Model yanıtını bekleyin ve sohbete devam edin

## Geliştirme

- `main.js`: Electron ana process konfigürasyonu
- `renderer.js`: UI etkileşimleri ve API çağrıları
- `preload.js`: Ana process ile renderer arasında güvenli köprü
- `index.html`: Kullanıcı arayüzü tasarımı

## Lisans

Bu proje MIT lisansı altında sunulmaktadır.
