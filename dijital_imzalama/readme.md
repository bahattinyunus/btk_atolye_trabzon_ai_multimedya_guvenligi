
# **Dijital İmzalama – README**

*Eğitim + Teknik Konu Anlatımı*

## 📌 **1. Dijital İmza Nedir?**

Dijital imza, bir dijital belgenin veya verinin **kim tarafından üretildiğini**, **değiştirilmediğini** ve **inkâr edilemeyeceğini** garanti eden kriptografik bir doğrulama yöntemidir.

Gerçekte yaptığı şey:

> Verinin **özetini (hash)** özel anahtarla **şifrelemek** ve bu imzayı veriye eklemek.

Bu imza daha sonra herkes tarafından doğrulanabilir.

---

## 🎯 **2. Dijital İmzanın Çözdüğü Problemler**

Dijital imza üç temel güvenlik ilkesini sağlar:

### 🔹 **1. Kimlik Doğrulama (Authentication)**

İmzanın, özel anahtarı elinde tutan kişi tarafından atıldığını kanıtlar.

### 🔹 **2. Bütünlük (Integrity)**

Belgenin **bir bitinin bile değişmediğini** garanti eder.
(Değişirse hash tutmaz → imza bozulur.)

### 🔹 **3. İnkar Edilemezlik (Non-Repudiation)**

"Ben imzalamadım" deme şansını ortadan kaldırır.
Özel anahtar sadece sende → imza sadece senden çıkabilir.

Bu yüzden mahkemelerde bile geçerli.

---

## 🧩 **3. Dijital İmza Nasıl Çalışır? (Step-by-step)**

### **İmza Oluşturma Süreci**

1. **Verinin özeti alınır**

   ```
   H = Hash(data)
   ```
2. **Özel anahtar ile özet şifrelenir**

   ```
   Signature = Encrypt_with_PrivateKey(H)
   ```
3. **İmza veriye eklenir**
   Belge + imza birlikte saklanır/iletilir.

---

### **İmza Doğrulama Süreci**

1. Veri tekrar hash'lenir

   ```
   H2 = Hash(data)
   ```

2. Gönderilen imza, **gönderenin açık anahtarı** ile çözülür

   ```
   H1 = Decrypt_with_PublicKey(Signature)
   ```

3. H1 == H2 ise:
   ✔ Bütünlük sağlandı
   ✔ İmza doğru
   ✔ Kaynak doğru

---

## 🔐 **4. Dijital İmzada Kullanılan Kriptografi Türleri**

### ### **1. Asimetrik Kriptografi (Public-Key) – Çekirdek Teknoloji**

Dijital imzaların %99’u şu algoritmalarla yapılır:

* **RSA** (2048/4096 bit)
* **ECDSA** (Elliptic Curve Digital Signature Algorithm)
* **EdDSA (Ed25519 / Ed448)** → modern ve çok hızlı
* **DSA** → eski, terk ediliyor

Modern dünyada “best practice”:
➡️ **Ed25519 dijital imza için en temiz ve en hızlı çözümdür.**

---

## 🧱 **5. Hash Fonksiyonlarının Rolü**

Hash fonksiyonları imzanın temelidir.

Dijital imzada **SHA-256** veya **SHA-3** gibi güvenli fonksiyonlar kullanılır.

Hash fonksiyonu neden zorunlu?

* Veriyi direkt 10 MB şifrelemek çok maliyetli → özetini imzalamak çok daha hızlıdır.
* Hash = benzersiz kimlik
* Tek yönlü, geri döndürülemez
* Bir bit değişse bile hash tamamen değişir (avalanche effect)

---

## 🪪 **6. Dijital Sertifikalar (X.509)**

Bir imzanın **gerçekten sana ait olup olmadığını** nasıl anlıyoruz?

Bunun için **dijital sertifikalar (certificate)** kullanılır.

Bir sertifika şunları içerir:

* Kullanıcının açık anahtarı
* Kimlik bilgileri
* Sertifika sağlayıcısının (CA) imzası
* Geçerlilik tarihleri
* Seri numarası
* Anahtar kullanımı

---

## 🏛️ **7. PKI (Public Key Infrastructure) – Dijital İmzanın Devleti**

Dijital imza aslında koca bir ekosistemdir.
Bu ekosistemin adı: **PKI**.

PKI bileşenleri:

* **CA (Certificate Authority)** → Ana otorite
* **RA (Registration Authority)** → Kullanıcı doğrulama
* **CRL/OCSP** → Sertifika iptal kontrolleri
* **Anahtar Yönetimi**
* **Zaman damgası**

---

## ⏳ **8. Zaman Damgası (Timestamping)**

Dijital imza için kritik bir parça daha var:

> “Bu belge *ne zaman* imzalandı?” sorusunun ispatı.

Hash, **TSA (Time Stamping Authority)** tarafından imzalanır.

Belgenin sonradan değiştirilmediğini + o tarihte var olduğunu kanıtlar.

---

## 📦 **9. Dijital İmza Türleri**

### **Basit Dijital İmza**

→ Temel imzalama, yasal geçerlilik düşük.

### **Gelişmiş Dijital İmza (Advanced Electronic Signature – AES)**

→ Kimlik doğrulaması güçlü
→ İzleme ve doğrulama gelişmiş

### **Nitelikli Elektronik İmza (QES – Qualified e-Signature)**

Türkiye’de **e-İmza** dediğimiz şey.
EAL4+ sertifikalı akıllı kart + kimlik doğrulama.

EU eIDAS yasasına göre:
➡️ QES = el ile atılan ıslak imza ile aynı yasal güçte.

---

## 🧪 **10. Dijital İmza Kullanım Alanları**

* E-devlet ve resmi süreçler
* Bankacılık
* E-sözleşme, e-fatura
* Yazılım paket imzalama (APK, exe, npm paketleri)
* Kod imzalama (Code Signing)
* Blockchain / kripto cüzdan imzaları
* IoT cihaz kimlik doğrulaması
* VPN / TLS sertifikaları
* Email imzalama (S/MIME)

---

## 🏗️ **11. Dijital İmza ve Kod İmzalama**

Yazılım geliştiriciler için kritik konu:

### Kod imzalama ne sağlar?

* Yazılımın değişmediğini
* Gerçek geliştirici tarafından üretildiğini
* Dağıtım sırasında manipüle edilmediğini

Örnek:
Windows `.exe` → Authenticode
Android `.apk` → APK Signature v3
Linux → GPG-based signing
Git Commits → GPG/SSH signing

---

## 🛡️ **12. Dijital İmzanın Tehditleri ve Zafiyetler**

### **1. Özel anahtarın çalınması**

→ Tam facia. Saldırgan gerçek imza atabilir.

### **2. Zayıf hash algoritmaları**

MD5, SHA-1 artık güvensizdir.

### **3. Sahte sertifikalar / CA saldırıları**

CA hacklenirse tüm sistem çöker.

### **4. Replay saldırıları**

Eski imzanın tekrar kullanılması.

### **5. Yan kanal saldırıları**

Özel anahtarı RAM, CPU, cache gibi yerlerden sızdırabilirler.

---

## 🚀 **13. Özet: Dijital İmza Mantığı**

* Hash al 🤝
* Özel anahtarla imzala 🤝
* Açık anahtarla doğrula 🤝
* Sertifika zinciri ile güveni kanıtla 🤝
* Zaman damgasıyla sabitle 🤝

Modern güvenliğin bel kemiği budur.


---

## ▶️ Nasıl Çalıştırılır? (Kod Demosu)

Bu klasörde, dijital imza kavramını somutlaştıran bir Python demo dosyası vardır:

- `signature_demo.py` → `multimedya-guvenligi-ai/src/crypto/digital_signature_demo.py` modülünü kullanarak **RSA ile dijital imza oluşturma ve doğrulama** örneği çalıştırır.

Örnek kullanım (bu klasörden):

```bash
cd dijital_imzalama
python signature_demo.py
```

> Not: Kodun çalışması için aynı repoda `multimedya-guvenligi-ai/` projesi
> bulunmalı ve oradaki `requirements.txt` dosyasındaki bağımlılıklar
> kurulmuş olmalıdır.

