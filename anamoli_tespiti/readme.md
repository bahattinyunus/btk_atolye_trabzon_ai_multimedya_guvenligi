

# 🔍 **Anomali Tespiti (Anomaly Detection) – README**

## 📌 **Giriş**

Anomali tespiti; sistemde, ağda veya veride **normal davranış dışındaki** hareketleri saptama işidir. Siber güvenlikte “garip olan her şey potansiyel tehdittir” mottosu üzerine kurulur.
Bu yöntem sayesinde:

* Saldırı girişimleri
* Yetkisiz erişimler
* Botnet davranışları
* DDoS belirtileri
* İç tehdit aktiviteleri

çok daha erken fark edilir.

---

# 🧠 **1. Anomali Nedir?**

“Normal” sistem davranışının dışına çıkan **her türlü sıra dışı aktivite**.

Mesela:

* Bir kullanıcının saat 03.00’te sunucuya bağlanması
* Normalde 10 MB veri çeken bir uygulamanın bir anda 2 GB istemesi
* Log’larda aniden artan hata sayısı
* CPU’nun boşta %5’ten %90’a fırlaması

Anomali = Şüpheli hareket.

---

# ⚡ **2. Anomali Tespitinin Siber Güvenlikte Önemi**

Saldırganlar artık klasik signature’lara takılmıyor. Bu yüzden **davranış tabanlı tespit** şart oldu.
Anomali tespiti şu alanlarda kritik:

* IDS / IPS sistemleri
* SIEM analizleri
* Kullanıcı davranışı izlemesi (UEBA)
* Ağ trafik analizi
* Sistem kaynak tüketimi izlemesi

“Zero-day saldırıları” bile çoğu zaman anomali olarak kendini belli eder.

---

# 🧩 **3. Anomali Türleri**

### **1️⃣ Nokta Anomalileri (Point Anomalies)**

Bir veri diğerlerinden çok farklıdır.
Örn: CPU aniden %100.

### **2️⃣ Bağlamsal Anomaliler (Contextual Anomalies)**

Duruma göre anormaldir.
Örn: Gece 4’te admin login → anormal
Öğlen 14.00’te admin login → normal

### **3️⃣ Kolektif Anomaliler (Collective Anomalies)**

Bir grup veri topluca anormallik gösterir.
Örn: 10000 tane SYN paketi arka arkaya → DDoS belirtisi.

---

# 🛠️ **4. Kullanılan Anomali Tespit Yöntemleri**

## 🔹 **Statik (İstatistiksel) Yöntemler**

* Ortalama, standart sapma
* Z-score
* IQR
* Threshold tespiti
* Yoğunluk analizleri

Basit ama etkili. Ağ trafiğinde sık kullanılır.

---

## 🔹 **Makine Öğrenimi Yöntemleri**

Siber güvenlikte günümüz yıldızı ✨

### **📌 Denetimsiz Öğrenme Modelleri**

En çok kullanılanlar çünkü çoğu veride “etiket” yok.

* **K-Means Clustering**
* **DBSCAN**
* **Isolation Forest** (efsane)
* **LOF – Local Outlier Factor**
* **Autoencoder** (derin öğrenme)

### **📌 Denetimli Öğrenme**

Saldırı verisi *etiketli* olduğunda işe yarar.

* Random Forest
* SVM
* Logistic Regression
* XGBoost

---

## 🔹 **Zaman Serisi Tabanlı Tespit**

Özellikle sistem logları, ağ trafiği, CPU/RAM kullanımında:

* ARIMA
* LSTM (deep learning)
* Prophet

---

# 🛰️ **5. Siber Güvenlikte Anomali Örnekleri**

### 🔥 **1. Ağ Trafiği**

* Normalde 2 Mbps olan trafik bir anda 80 Mbps → DDoS ihtimali
* Aynı IP’den 1000 failed login → Brute force girişimi

### 🧑‍💻 **2. Kullanıcı Davranışı**

* Yeni çalışan, 1 günde 3000 dosyayı indiriyor → Şüpheli
* Kişi ilk kez PowerShell’i yönetici olarak çalıştırıyor

### 🧷 **3. Log Analizi**

* Belirli periyotlarla tekrar eden komutlar
* Olağan dışı hatalar
* Şüpheli servis restart’ları

---

# 📡 **6. IDS/IPS Sistemlerinde Anomali Tespiti**

Klasik iki tespit mekanizması:

### **A) Signature-Based Detection (İmza Tabanlı)**

Virüs imzası gibi → bilinen saldırıları tanır.

### **B) Anomaly-Based Detection (Anomali Tabanlı)**

Bilinmeyeni yakalar.
Zero-day’e karşı en güçlü yöntem.

**Snort, Suricata, Zeek** gibi sistemlerde yaygın.

---

# 🔐 **7. Anomali Tespitinde Zorluklar**

* 🔸 False positive çok olur (normal davranış anormal gibi görünebilir)
* 🔸 Normal davranışın tanımı her şirkette farklıdır
* 🔸 Büyük veri işleme zordur
* 🔸 Saldırganlar da artık *“normalmiş gibi davranmayı”* öğreniyor

Ama iyi model + doğru loglama = şahane sonuç.

---

# 🧿 **8. Önleme ve İyileştirme Önerileri**

* SIEM ile sürekli log takibi
* Kullanıcı davranış analizi (UEBA)
* Ağ segmentasyonu
* Anormallik durumunda otomatik aksiyon (SOAR)
* Zaman serisi modelleri kurma
* Threshold değerlerinin düzenli güncellenmesi

---

# 📊 **9. Örnek Basit Anomali Algoritması (Mantıksal)**

```
if (trafik_miktari > ortalama * 3) and (gece_saati == true):
    alarm("Olası saldırı")
```

Gerçek sistemler çok daha karmaşık ama prensip aynı:
**Normal → Bilinir.
Anormal → Yakalanır.**

---

# 🚀 **10. Sonuç**

Anomali tespiti, siber güvenlikte artık opsiyon değil **zorunluluk**.
İmzalar sadece eski saldırıları tanır; anomali tespiti ise *davranışı* analiz ederek **bilinmeyeni yakalar**. Özellikle SOC, SIEM, IDS/IPS, UEBA gibi modern güvenlik mimarilerinin temel yapı taşlarından biridir.

