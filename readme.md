<div align="center">

# 🛡️ Multimedya Veri Güvenliğinde Yapay Zeka

_BTK Atölye • Multimedya Güvenliği • Eğitim ve Örnek Proje Repo_

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Eğitim-orange?style=for-the-badge)

</div>

---

> **EN (short summary)**: This repository combines lecture notes and
> example Python code about using AI for multimedia security
> (deepfake detection, steganography, watermarking, anomaly detection
> and basic crypto / access control). It is designed as a teaching
> resource, not a production-ready system.

---

## 🔍 TL;DR

Bu repo;

- Multimedya veri güvenliğinde yapay zekanın rolünü anlatan **ders notlarını**,
- Deepfake, steganografi, ransomware, USOM gibi konuların **özetlerini**,
- Ve bunları destekleyen **örnek bir Python proje iskeletini** (`multimedya-guvenligi-ai/`)

bir araya getirir.

Hem teori hem de pratik (kod) içeren bir eğitim seti olarak düşünülebilir.

---

## 📚 İçindekiler

- [📂 Proje Yapısı](#-proje-yapısı)
- [🛠️ Kurulum ve Kullanım](#️-kurulum-ve-kullanım)
- [🎯 1. Yapay Zeka ve Veri Güvenliğinin Kesişimi](#-1-yapay-zeka-ve-veri-güvenliğinin-kesişimi)
- [🔐 2. YZ'nin Kullanıldığı Temel Alanlar](#-2-yznin-kullanıldığı-temel-alanlar)
- [🧠 3. Kullanılan Yapay Zeka Modelleri](#-3-kullanılan-yapay-zeka-modelleri)
- [🛡️ 4. Multimedya Güvenliğinde YZ'nin Sağladığı Avantajlar](#️-4-multimedya-güvenliğinde-yznin-sağladığı-avantajlar)
- [⚠️ 5. Zorluklar ve Sınırlamalar](#️-5-zorluklar-ve-sınırlamalar)
- [🧪 6. Uygulama Senaryosu: Güvenli Video Yayınlama Sistemi](#-6-uygulama-senaryosu-güvenli-video-yayınlama-sistemi)
- [🚀 7. Sonuç](#-7-sonuç)

---

## 📂 Proje Yapısı

```
btk_atolye_multimedya_guvenligi/
├── 📂 eğitim_kodları/          # Makine öğrenmesi ve CNN örnekleri
│   ├── 📂 01_Temel_ML/         # Regresyon, Sınıflandırma, Kümeleme
│   │   ├── 📄 1_dogrusalRegresyon.py
│   │   └── ...
│   ├── 📂 02_Derin_Ogrenme/    # CNN, Transfer Learning
│   │   ├── 📄 10_cnnDenemesi.py
│   │   └── ...
│   ├── 📂 03_Generative_AI/    # GAN, Diffusion, Style Transfer
│   │   ├── 📄 13_ganOrnek.py
│   │   ├── 📄 14_ganSahteYuz.py
│   │   ├── 📄 15_difuzyonSahteYuz.py
│   │   ├── 📄 16_siftOrnek.py      # SIFT ile Özellik Çıkarımı
│   │   └── 📄 17_exifOrnek.py      # EXIF Analizi ile Sahtecilik İpuçları
│   └── 📂 veriler/             # Ortak veri klasörü
├── 📂 multimedya-guvenligi-ai/ # Örnek proje iskeleti
├── 📂 deepfake/                # Deepfake notları ve örnekleri
├── 📂 stegonografi/            # Steganografi notları
├── 📄 colab_turuba_rehberi.md  # Colab ve Turuba kullanım rehberi
├── 📄 requirements.txt         # Gerekli kütüphaneler
└── 📄 readme.md                # Ana dokümantasyon (Bu dosya)
```

---

## 🛠️ Kurulum ve Kullanım

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

### 1. Repoyu Klonlayın
```bash
git clone https://github.com/bahattinyunus/btk_atolye_multimedya_guvenligi.git
cd btk_atolye_multimedya_guvenligi
```

### 2. Sanal Ortam Oluşturun (Önerilen)
```bash
python -m venv venv
# Windows için:
venv\Scripts\activate
# Mac/Linux için:
source venv/bin/activate
```

### 3. Gerekli Kütüphaneleri Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Örnek Kodları Çalıştırın
Örneğin, CNN modelini eğitmek ve test etmek için:
```bash
cd eğitim_kodları
python 10_cnnDenemesi.py
```
*Not: Bu kod CIFAR-10 veri setini otomatik olarak indirecektir.*

---

## 🎯 1. Yapay Zeka ve Veri Güvenliğinin Kesişimi

Yapay zeka, özellikle makine öğrenimi (ML) ve derin öğrenme (DL) algoritmalarıyla multimedya içeriklerini analiz edip tehditleri tespit etmede geleneksel yöntemlere göre daha hızlı ve etkili çözümler sunar.

Multimedya veri güvenliğinde YZ'nin hedefleri:

* Saldırıları daha erken tespit etmek
* İçerik manipülasyonunu fark etmek
* Yetkisiz erişimi önlemek
* Telif hakkını korumak
* Veri bütünlüğünü otomatik izlemek

---

## 🔐 **2. YZ'nin Kullanıldığı Temel Alanlar**

### **2.1. Anomali Tespiti (Anomaly Detection)**

Multimedya sunucularındaki olağan dışı dosya hareketlerini YZ otomatik olarak algılayabilir.

Örnek:

* Normalde saniyede 5 video isteği gelirken bir anda 500 istek gelmesi → DDoS tespiti
* Yetkisiz kullanıcı davranışları

Kullanılan YZ yöntemleri:

* Isolation Forest
* Autoencoder tabanlı anomali modelleri
* LSTM tabanlı davranış analizi

---

### **2.2. Derin Sahtekârlık (Deepfake) Tespiti**

Günümüzde görüntü ve video manipülasyonları (deepfake) ciddi bir multimedya güvenlik tehdidi oluşturuyor.

YZ bu manipülasyonları tespit etmek için kullanılır:

* Yüz hareketi tutarsızlıklarını analiz eder
* Göz kırpma frekansı ölçer
* Yapay görüntülerdeki "texture artifact" hatalarını yakalar

Kullanılan modeller:

* CNN (Convolutional Neural Networks)
* Vision Transformer (ViT)
* Deepfake Detection Networks (XceptionNet)

---

### **2.3. Telif Hakkı Koruma ve Dijital Filigran (Watermarking)**

YZ, videolara ve görsellere görünmez filigran ekleyip izinsiz kullanım tespitini kolaylaştırır.

YZ tabanlı sistemler:

* Filigranın kaldırılma girişimlerini otomatik tespit eder
* Filigranı sıkıştırma / kırpma gibi dönüşümlere dayanıklı hale getirir

---

### **2.4. İçerik Sınıflandırma ve Erişim Kontrolü**

Multimedya içerikleri otomatik olarak sınıflandırılabilir:

* Hassas veri içeren dosyaları belirleme
* İçerik türüne göre erişim seviyesini ayarlama

Örnek:

* YZ bir görüntünün kimlik kartı fotoğrafı olduğunu algılar → "Gizli" etiketi koyar

---

### **2.5. Zararlı İçerik Analizi**

Yapay zeka, multimedya dosyalarının içine gizlenmiş zararlı yazılımları bile tespit edebilir.

Örnek:

* Bir JPEG içine embedding ile gizlenmiş malware kodları
* YZ, dosyanın binary pattern'larında anormallikleri keşfeder

Kullanılan teknikler:

* Binary classification neural networks
* Random Forest tabanlı malware detection

---

## 🧠 **3. Kullanılan Yapay Zeka Modelleri**

| Kullanım Alanı         | YZ Modeli          | Açıklama                             |
| ---------------------- | ------------------ | ------------------------------------ |
| Deepfake tespiti       | CNN, ViT           | Manipülasyon izlerini yakalar        |
| Anomali tespiti        | Autoencoder, LSTM  | Normal davranıştan sapmaları algılar |
| Zararlı içerik analizi | Random Forest, DNN | Dosya bazlı tehdit analizi           |
| Filigranlama           | GAN                | Dayanıklı filigran oluşturma         |
| İçerik sınıflandırma   | CNN, ResNet        | Görsel içerik analizi                |

---

## 🛡️ **4. Multimedya Güvenliğinde YZ'nin Sağladığı Avantajlar**

* ✔ Gerçek zamanlı tehdit tespiti
* ✔ Hata oranının ciddi şekilde azalması
* ✔ Manuel güvenlik yükünün azalması
* ✔ Geniş veri setlerini hızlı analiz etme
* ✔ Yeni saldırı türlerini otomatik öğrenme

---

## ⚠️ **5. Zorluklar ve Sınırlamalar**

* Yanlış pozitif sonuçlar
* Çok büyük GPU maliyetleri
* Veri gizliliği ve etik sorunlar
* Adversarial attack (YZ kandırma saldırıları)

Örnek:

* Bir görüntüye görünmez birkaç piksel eklenerek YZ’nin kandırılması

---

## 🧪 **6. Uygulama Senaryosu: Güvenli Video Yayınlama Sistemi**

YZ ile güvenliği artırılmış bir video platformunda:

1. Kullanıcı davranışı LSTM modeliyle takip edilir.
2. Video dosyası CNN ile analiz edilerek manipülasyon kontrolü yapılır.
3. İçeriğe görünmez watermark eklenir.
4. Sunucuya gelen aşırı istekler Autoencoder ile anomali olarak işaretlenir.
5. Zararlı içerik analizi yapılır.

---

## 🚀 **7. Sonuç**

Yapay zeka, multimedya veri güvenliğinde artık opsiyonel bir teknoloji değil—mecburi hale gelmiş güçlü bir koruma katmanıdır. Hem tehditleri tespit etme hem de içerik güvenliğini sağlama konusunda geleceğin omurgasını oluşturur.

Hazırlanan bu README, eğitim amacıyla derli toplu ve uygulamaya dönük bir çerçeve sunar.

