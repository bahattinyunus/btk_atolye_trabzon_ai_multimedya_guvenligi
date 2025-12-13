<div align="center">

![BTK Akademi Workshop Banner](assets/header-banner.png)

# 🛡️ Multimedya Veri Güvenliğinde Yapay Zeka
### _BTK Akademi • Trabzon Atölyesi_

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![BTK Akademi](https://img.shields.io/badge/BTK-Akademi-red?style=for-the-badge)](https://www.btkakademi.gov.tr/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 🚀 Atölye Hakkında

Bu proje, **BTK Akademi** iş birliğiyle **Trabzon'da** gerçekleştirilen **"Multimedya Veri Güvenliğinde Yapay Zekâ Kullanımı"** atölye çalışmasının resmi kaynak kodlarını ve eğitim materyallerini içerir.

Atölye süresince katılımcılarla birlikte; yapay zekanın siber güvenlikteki çift yönlü rolü (saldırı ve savunma) incelenmiş, **Deepfake tespiti**, **dijital filigranlama (watermarking)** ve **adversarial örnekler** konuları uygulamalı olarak işlenmiştir.

> **Amaç:** Katılımcıların, multimedya verileri üzerindeki manipülasyonları tespit edebilen ve kendi güvenli yapay zeka modellerini eğitebilen yetkinliğe ulaşmasıdır.

---

## 🎓 Eğitim İçeriği ve Modüller

Proje, atölye müfredatına uygun olarak aşağıdaki temel modüllere ayrılmıştır:

| Modül | İçerik | Uygulamalar |
| :--- | :--- | :--- |
| **🧠 1. Temel ML & AI** | Yapay Zekaya Giriş | Regresyon, Sınıflandırma, Python ile ML |
| **👁️ 2. Deep Learning** | CNN ve Görsel Analiz | Görüntü Sınıflandırma, Transfer Learning |
| **🕵️ 3. Deepfake Analizi** | Sahte İçerik Tespiti | Yüz Manipülasyonu Tespiti, MesoNet Mimarisi |
| **🎨 4. Generative AI** | Üretken Modeller | GANs, Diffusion Models, Style Transfer |
| **🔐 5. Veri Güvenliği** | Koruma Yöntemleri | Steganografi, Filigran (Watermark) Ekleme |

---

## 🏗️ Proje Mimarisi

Aşağıdaki şema, atölye kapsamında geliştirilen genel güvenlik mimarisini özetlemektedir:

```mermaid
graph TD
    A[🎥 Multimedya Girdisi] -->|Görüntü/Ses/Video| B(⚙️ Ön İşleme)
    B --> C{🔍 Analiz Katmanı}
    
    subgraph "Yapay Zeka Modelleri"
    C -->|Sahtecilik Tespiti| D[Deepfake Dedektörü (CNN/ViT)]
    C -->|Anomali Tespiti| E[Autoencoder Ağları]
    end
    
    D --> F{Sonuç?}
    E --> F
    
    F -->|⚠️ Tehdit Var| G[Blokla ve Raporla]
    F -->|✅ Temiz| H[Güvenli İçerik]
    
    H --> I[🛡️ Filigran Ekle (Watermark)]
    I --> J[💾 Güvenli Depolama]
    
    style A fill:#f9f,stroke:#333
    style G fill:#f00,color:white,stroke:#333
    style J fill:#0f0,stroke:#333
```

---

<div align="center">

![Analysis Concept](assets/mid-banner.png)

</div>

---

## 📂 Dosya Yapısı

```
btk_atolye_multimedya_guvenligi/
├── 📂 eğitim_kodları/          # Atölye sırasında yazılan kodlar
│   ├── 01_Temel_ML/            # Makine Öğrenmesi temelleri
│   ├── 02_Derin_Ogrenme/       # CNN ve DL uygulamaları
│   └── 03_Generative_AI/       # GAN ve Diffusion örnekleri
├── 📂 deepfake/                # Deepfake tespit dökümanları
├── 📂 stegonografi/            # Gizli veri saklama teknikleri
├── 📂 docs/                    # Ek okumalar (Ransomware, USOM vb.)
├── 📂 assets/                  # Görsel materyaller
└── 📄 requirements.txt         # Proje bağımlılıkları
```

---

## 🛠️ Kurulum ve Çalıştırma

Atölye materyallerini bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

### 1. Repoyu Klonlayın
```bash
git clone https://github.com/bahattinyunus/btk_atolye_multimedya_guvenligi.git
cd btk_atolye_multimedya_guvenligi
```

### 2. Sanal Ortam (Önerilen)
```bash
python -m venv venv
# Windows için:
venv\Scripts\activate
# Mac/Linux için:
source venv/bin/activate
```

### 3. Kütüphaneleri Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Örnek Bir Kod Çalıştırın
Örneğin, CNN modelini eğitmek veya test etmek için:
```bash
cd eğitim_kodları/02_Derin_Ogrenme
python 10_cnnDenemesi.py
```

---

## 🤝 Katkıda Bulunma

Bu proje eğitim amaçlıdır ve geliştirime açıktır. Hata bildirimleri veya yeni özellik eklemeleri için **Pull Request** gönderebilirsiniz.

Lütfen katkıda bulunmadan önce [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyiniz.

---

<div align="center">

_Copyright © 2024 - BTK Akademi & Bahattin Yunus_
_Tüm Hakları Saklıdır._

</div>
