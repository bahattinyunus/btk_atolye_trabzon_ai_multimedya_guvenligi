<div align="center">

![Project Concept](../assets/project-concept.png)

# 🧠 Multimedya Güvenliğinde Yapay Zeka · Örnek Proje

_Deepfake tespiti · LSB steganografi · Watermarking GAN · Anomali tespiti_

[![Status](https://img.shields.io/badge/Durum-İskelet-blue?style=for-the-badge&logo=github)]()
[![Python](https://img.shields.io/badge/Python-3.8%2B-orange?style=for-the-badge&logo=python&logoColor=white)]()
[![Model](https://img.shields.io/badge/Model-CNN%20%2B%20GAN-purple?style=for-the-badge)]()

</div>

---

## 🔍 TL;DR

Bu klasör, kökteki `ornek_proje.md` dosyasında tarif edilen
**multimedya güvenliği + yapay zeka** proje yapısının basit bir
implementasyonudur.

- Deepfake tespitine yönelik **basit bir CNN modeli**
- Anomali tespiti için **Isolation Forest** örneği
- Steganografi için **LSB demo modülü**
- Watermarking için **örnek GAN mimarisi**
- Şifreleme ve dijital imza için **AES/RSA/digital signature** demoları

barındırır.

---

## 📂 Klasör Yapısı

- `data/` : Eğitim ve test verileri (video, görüntü, etiketler)
- `src/` : Kaynak kodlar (ön işleme, modeller, eğitim, çıkarım)
  - `models/` : `SimpleDeepfakeCNN`, `AnomalyDetector`, `WatermarkGenerator`, `WatermarkDiscriminator`
  - `training/` : Anomali ve deepfake eğitimi için scriptler
  - `inference/` : Tahmin/demolar için scriptler
  - `steganography/` : LSB stenografi demo kodu (`lsb_stego.py`)
- `utils/` : Yardımcı fonksiyonlar ve metrikler
- `results/` : Eğitim sonuçları, loglar ve görseller
- `scripts/` : Eğitim ve çıkarım komutlarını çalıştırmak için scriptler

---

## ⚙️ Kurulum

Projeyi çalıştırmadan önce Python bağımlılıklarını kur:

```bash
pip install -r requirements.txt
```

---

## 🚀 Hızlı Başlangıç (Quickstart)

### 1) Dummy Deepfake Eğitimi

```bash
python -m src.training.train_deepfake
```

Bu komut, `SimpleDeepfakeCNN` modeli ile örnek bir eğitim döngüsü
çalıştırır ve epoch bazında loss çıktısı üretir.

### 2) Dummy Deepfake Tahmini

```bash
python -m src.inference.predict_deepfake
```

Bu komut, rastgele bir görüntü tensörü oluşturur ve modelden alınan
"dummy" real/fake skorunu ekrana basar.

### 3) LSB Steganografi Demosu

`data/images/example_input.png` altında küçük bir görüntü bulunduğundan
emin olduktan sonra:

```bash
python -m src.steganography.lsb_stego
```

Bu komut, görüntüye kısa bir metin mesajı gizler ve daha sonra aynı
mesajı çözerek ekrana yazar.

> Not: Gerçek bir veri seti ile çalışmak için `DummyFramesDataset`
> yerine frame klasörlerinden okuma yapan bir dataset ve `predict_video`
> fonksiyonuna gerçek video/frame işleme adımlarının eklenmesi gerekir.

---

## 🎯 Amaç

Bu proje eğitim amaçlıdır; multimedya güvenliği konusundaki teorik
dokümanları (örn. `readme.md`, `deepfake/readme.md`, `stegonografi.md`)
destekleyen basit bir uygulama iskeleti sunar. Gerçek zamanlı sistemler
ve ölçekli üretim senaryoları için ek optimizasyon ve altyapı gereklidir.
