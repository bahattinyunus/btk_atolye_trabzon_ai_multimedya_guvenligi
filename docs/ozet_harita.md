# Multimedya Güvenliği Eğitimi – Özet & İçindekiler Haritası

Bu dosya, repodaki tüm konu anlatımlarını ve Python demolarını **tek yerden** görmen için bir harita olarak hazırlanmıştır.

---

## 1. Ana README ve Örnek Proje

- **`readme.md`**
  - Multimedya veri güvenliğinde yapay zekanın rolü
  - Anomali tespiti, deepfake, watermarking, zararlı içerik analizi vb.
  - İngilizce kısa özet + içindekiler + diğer klasörlere bağlantılar

- **`multimedya-guvenligi-ai/`**
  - Örnek Python proje iskeleti (src/, data/, utils/, results/, scripts/)
  - TL;DR, klasör yapısı, kurulum ve quickstart komutları

**Önemli komutlar (proje kökünde):**

```bash
cd multimedya-guvenligi-ai
pip install -r requirements.txt
```

---

## 2. Deepfake

- **Konu:** `deepfake/readme.md`
  - Deepfake nedir, nasıl çalışır, kullanım alanları
  - Tespit yöntemleri (CNN, ViT, yüz/göz analizi, texture artifact)
  - Örnek deepfake proje yapısı ve bu repodaki proje ile bağlantı

- **Demolar:**
  - Proje tarafı:
    - `multimedya-guvenligi-ai/src/models/deepfake_detector.py`
    - `multimedya-guvenligi-ai/src/training/train_deepfake.py`
    - `multimedya-guvenligi-ai/src/inference/predict_deepfake.py`
  - Klasör içi scriptler:
    - `deepfake/train_demo.py`
    - `deepfake/predict_demo.py`

**Çalıştırma (deepfake klasöründen):**

```bash
cd deepfake
python train_demo.py
python predict_demo.py
```

---

## 3. Steganografi (LSB vb.)

- **Konu:** `stegonografi.md`
  - LSB, transform domain, ses/video stenografisi vb.

- **Demo kod:**
  - `multimedya-guvenligi-ai/src/steganography/lsb_stego.py`
    - Bir görüntüye mesaj gizleme ve geri çıkarma

**Çalıştırma (proje içinden):**

```bash
cd multimedya-guvenligi-ai
ython -m src.steganography.lsb_stego
```

`data/images/example_input.png` altında küçük bir PNG/JPEG olmalı.

---

## 4. Şifreleme (Encryption)

- **Konu:** `sifreleme/readme.md`
  - Simetrik/asimetrik şifreleme, hibrit şifreleme, blok modları, dijital imza, PQC vb.

- **Demolar (proje):**
  - `multimedya-guvenligi-ai/src/crypto/symmetric_aes_demo.py`
  - `multimedya-guvenligi-ai/src/crypto/rsa_demo.py`

- **Klasör içi scriptler:**
  - `sifreleme/aes_demo.py`
  - `sifreleme/rsa_demo.py`

**Çalıştırma (sifreleme klasöründen):**

```bash
cd sifreleme
python aes_demo.py
python rsa_demo.py
```

---

## 5. Erişim Kontrolü (Access Control)

- **Konu:** `erisim_control/readme.md`
  - DAC, MAC, RBAC, ABAC, PBAC, ReBAC, Zero Trust, PEP/PDP/PIP vb.

- **Demolar (proje):**
  - `multimedya-guvenligi-ai/src/access_control/rbac_demo.py`
  - `multimedya-guvenligi-ai/src/access_control/abac_demo.py`

- **Klasör içi scriptler:**
  - `erisim_control/rbac_demo.py`
  - `erisim_control/abac_demo.py`

**Çalıştırma (erisim_control klasöründen):**

```bash
cd erisim_control
python rbac_demo.py
python abac_demo.py
```

---

## 6. Dijital İmza (Digital Signature)

- **Konu:** `dijital_imzalama/readme.md`
  - Dijital imza kavramı, hash rolü, sertifikalar, PKI, kod imzalama, tehditler.

- **Demo (proje):**
  - `multimedya-guvenligi-ai/src/crypto/digital_signature_demo.py`

- **Klasör içi script:**
  - `dijital_imzalama/signature_demo.py`

**Çalıştırma (dijital_imzalama klasöründen):**

```bash
cd dijital_imzalama
python signature_demo.py
```

---

## 7. Güvenlik Duvarları (Firewalls)

- **Konu:** `güvenlik_duvarları/readme.md`
  - Temel firewall kavramları, NGFW, WAF, DPI, log analizi, Zero Trust, SIEM entegrasyonu vb.

- **Demo (proje):**
  - `multimedya-guvenligi-ai/src/firewall/firewall_log_demo.py`

- **Klasör içi script:**
  - `güvenlik_duvarları/firewall_demo.py`

**Çalıştırma (güvenlik_duvarları klasöründen):**

```bash
cd güvenlik_duvarları
python firewall_demo.py
```

---

## 8. Yedekleme ve Felaket Kurtarma (Backup & DR)

- **Konu:** `yedekleme_felaket_kurtarma/readme.md`
  - Backup türleri, 3-2-1 kuralı, RPO/RTO, DR stratejileri, ransomware senaryoları, ileri seviye DR.

- **Demo (proje):**
  - `multimedya-guvenligi-ai/src/backup/backup_dr_demo.py`

- **Klasör içi script:**
  - `yedekleme_felaket_kurtarma/backup_demo.py`

**Çalıştırma (yedekleme_felaket_kurtarma klasöründen):**

```bash
cd yedekleme_felaket_kurtarma
python backup_demo.py
```

---

## 9. Diğer Konu Notları

- **`ransomware.md`**
  - Fidye yazılımları, çalışma mantığı, korunma yöntemleri.

- **`usom.md`**
  - USOM tanımı, görevleri, siber olay müdahale süreci.

- **`tehditler.md`**
  - Farklı tehdit türleri (ransomware, phishing, malware, DDoS vb.) için genel özet.

- **`kümeler/` altı:**
  - `bilgi_güvenliği.md`
  - `veri_güvenliği.md`
  - `siber_güvenlik.md`

Bu dosyalar, genel güvenlik kavramlarını destekleyici teorik içerikler sağlar.

---

## 10. Hızlı Başlangıç Özeti

1. **Kurulum:**
   ```bash
   cd multimedya-guvenligi-ai
   pip install -r requirements.txt
   ```

2. **Her konu için:**
   - İlgili klasöre gir (`deepfake/`, `sifreleme/`, `erisim_control/`, `dijital_imzalama/`, `güvenlik_duvarları/`, `yedekleme_felaket_kurtarma/`)
   - README’yi oku
   - Sonundaki "Nasıl Çalıştırılır" komutlarını çalıştır.

Bu harita, sunum/ödev hazırlarken veya dersi anlatırken "nerede ne var" sorusuna hızlı cevap vermek için tasarlanmıştır.
