# 🤖 Teknik Destek Botu

Bu proje, **mezuniyet projem** olarak yaptığım bir **Discord teknik destek botudur.**  
Bot, **"Alabileceğin Her Şey"** mağazasındaki kullanıcıların sıkça sorduğu sorulara otomatik cevap verir.  
Ayrıca özel soruları da yaklaşık olarak eşleştirip uygun cevabı bulmaya çalışır.

---

## 📦 Gerekli Kütüphaneler

Bu projeyi çalıştırmak için sadece **discord.py** kütüphanesi yeterlidir.

```bash
pip install discord
```

> Python 3.9 veya üzeri sürüm önerilir.

---

## 💾 Projeyi İndirme ve Çalıştırma

1. Sağ üstteki **Code** (yeşil buton) kısmına tıklayıp bağlantıyı kopyalayın.  
2. Terminal veya VSCode’da şu komutu yazın:
   ```bash
   git clone "kopyaladığınız_link"
   ```
3. Proje klasörüne girin:
   ```bash
   cd teknik-destek-botu
   ```
4. Gerekli kütüphaneyi yükleyin:
   ```bash
   pip install discord
   ```
5. `config.py` dosyasına kendi bot tokeninizi yazın:
   ```python
   TOKEN = "BURAYA_TOKENİNİ_YAZ"
   ```
6. Son olarak botu çalıştırın:
   ```bash
   python main.py
   ```

---

## 🧠 Bot Ne Yapar?

- `/start` komutuyla kendini tanıtır.  
- `/sor` komutuyla kullanıcıların yazdığı sorulara cevap verir.  
- `/sorular` komutuyla hazır soru listesini görsel olarak gönderir.  

---

## 📁 Dosya Yapısı

```
📂 Proje Klasörü
│
├── main.py           # Botun ana dosyası
├── logic.py          # Sorular ve cevaplar burada
├── config.py         # Token burada tutulur
├── hazir_sorular.png # Hazır sorular görseli
└── README.md         # Bu dosya
```

---

👨‍💻 **Geliştirici:** Mete  
🎓 **Proje Türü:** Mezuniyet Projesi  
