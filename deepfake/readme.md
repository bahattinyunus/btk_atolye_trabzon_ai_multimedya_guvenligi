# Deepfake Teknolojisi: Konu Anlatımı

Bu doküman, deepfake teknolojisini temel kavramlardan uygulamalara kadar kapsamlı bir şekilde anlatmayı amaçlamaktadır. Eğitim amaçlı hazırlanmıştır.

---

## 1. Deepfake Nedir?

Deepfake, "deep learning" (derin öğrenme) ve "fake" (sahte) kelimelerinin birleşiminden oluşan bir terimdir. Yapay zeka algoritmaları kullanılarak, bir kişinin görüntü veya sesini başka bir içerikte gerçeğe çok yakın şekilde değiştirme veya taklit etme sürecine verilen isimdir.

Özellikleri:

* Yüksek gerçekçilik
* Video, ses ve görüntüde manipülasyon
* Makine öğrenimi ve yapay sinir ağları kullanımı

---

## 2. Deepfake Nasıl Çalışır?

Deepfake, çoğunlukla Generative Adversarial Networks (GANs) ve Autoencoder tabanlı modeller kullanılarak oluşturulur.

### 2.1 Autoencoder Yöntemi

* **Encoder:** Girdi görüntüsünü sıkıştırır ve düşük boyutlu bir latent space’e dönüştürür.
* **Decoder:** Latent representation’dan yeni bir görüntü üretir.
* Kaynak ve hedef görüntülerden eğitim yapılarak yüz transferi gerçekleştirilir.

### 2.2 GAN Yöntemi

* **Generator:** Gerçekçi sahte görüntü üretir.
* **Discriminator:** Üretilen görüntünün sahte mi gerçek mi olduğunu tahmin eder.
* İki ağ birbirine karşı yarışır, zamanla üretilen içerik gerçek görüntüye çok yakın hale gelir.

---

## 3. Deepfake Kullanım Alanları

### 3.1 Olumlu Kullanım Alanları

* Film ve animasyon endüstrisinde görsel efektler
* Eğitim ve simülasyon içerikleri
* Sanat projeleri ve yaratıcı medya
* Ses ve video restorasyonu

### 3.2 Olumsuz Kullanım Alanları

* Kişisel itibar ve mahremiyetin ihlali
* Sahte haber (fake news) ve dezenformasyon
* Sosyal mühendislik ve dolandırıcılık
* Kimlik ve finansal dolandırıcılık

---

## 4. Deepfake Tespit Yöntemleri

Deepfake içeriklerini tespit etmek için yapay zekâ ve analiz yöntemleri kullanılır:

* **CNN tabanlı modeller:** Görüntü ve video üzerinde manipülasyon izlerini tespit eder.
* **Vision Transformers (ViT):** Daha karmaşık ve büyük veri setlerinde etkili tespit.
* **Göz ve yüz hareketi analizi:** İnsan doğal davranışlarını modelleyerek sahte içerikleri bulur.
* **Texture artifact analizi:** Derin öğrenme modellerinin oluşturduğu küçük hataları fark eder.

---

## 5. Etik ve Hukuki Boyut

* Deepfake kullanımı kişisel hak ve özgürlüklere zarar verebilir.
* Birçok ülkede deepfake ile sahte içerik üretimi ve dağıtımı yasal yaptırımlara tabidir.
* Eğitim ve araştırma amaçlı kullanım etik çerçeveye uygun olmalıdır.

---

## 6. Sonuç

Deepfake, hem yaratıcı hem de tehlikeli potansiyele sahip bir teknolojidir. Eğitim ve farkındalık yoluyla, hem olumsuz etkiler azaltılabilir hem de olumlu kullanım alanları geliştirilebilir.

---
# Deepfake Teknolojisi: Örnek Proje Yapısı

Bu proje yapısı, deepfake içeriklerinin tespitine yönelik bir eğitim ve uygulama platformu oluşturmak için hazırlanmıştır.

```
deepfake-detection-project/
│
├── README.md                     # Proje açıklaması ve konu anlatımı
├── requirements.txt              # Gerekli Python paketleri ve bağımlılıklar
├── data/                         # Eğitim ve test verileri
│   ├── videos/                   # Video dosyaları (gerçek ve sahte)
│   ├── frames/                   # Videolardan çıkarılan kareler (frames)
│   └── labels.csv                # Video/Frame etiketleri (real/fake)
│
├── src/                          # Kaynak kodlar
│   ├── preprocessing/            # Veri ön işleme ve frame çıkarma
│   │   ├── extract_frames.py
│   │   └── normalize_data.py
│   ├── models/                   # Yapay zekâ modelleri
│   │   ├── cnn_model.py          # CNN tabanlı tespit modeli
│   │   ├── vit_model.py          # Vision Transformer tabanlı model
│   │   └── ensemble.py           # Model kombinasyonları
│   ├── training/                 # Model eğitim scriptleri
│   │   ├── train_cnn.py
│   │   └── train_vit.py
│   └── inference/                # Tahmin scriptleri
│       ├── predict_video.py
│       └── predict_frame.py
│
├── notebooks/                    # Jupyter Notebook ile eğitim ve analiz
│   ├── data_exploration.ipynb
│   └── model_evaluation.ipynb
│
├── utils/                        # Yardımcı fonksiyonlar
│   ├── file_utils.py             # Dosya okuma/yazma
│   └── metrics.py                # Başarı ve doğruluk metrikleri
│
├── results/                      # Model çıktıları, raporlar ve görselleştirmeler
│   ├── figures/
│   └── logs/
│
└── scripts/                      # Komut satırından çalıştırma
    ├── run_training.sh
    └── run_inference.sh
```

## Açıklamalar

* **data/**: Deepfake ve gerçek video/frame verilerini içerir. Eğitim ve test verileri ayrı tutulur.
* **src/**: Yapay zekâ modelleri, veri ön işleme, eğitim ve tahmin scriptlerini içerir.
* **notebooks/**: Veri keşfi, model performans değerlendirmeleri ve analizler için interaktif ortam.
* **utils/**: Tekrarlayan işlemler ve metrik hesaplamaları için fonksiyonlar.
* **results/**: Eğitim ve test sonuçları, grafikler ve loglar.
* **scripts/**: Projeyi kolay çalıştırmak için hazır bash scriptleri.


---

## Uygulama İçin Bu Repodaki Örnek Proje

Bu depoda, deepfake tespitine yönelik basit bir YZ iskeleti örneği **`multimedya-guvenligi-ai/`** klasöründe yer almaktadır. Özellikle:

- `src/models/deepfake_detector.py`: Basit bir CNN tabanlı tespit modeli iskeleti
- `src/training/train_deepfake.py`: Örnek eğitim döngüsü (dummy veri ile)
- `src/inference/predict_deepfake.py`: Örnek tahmin akışı

Bu dokümandaki kavramları uygulamaya dökmek için bu kod iskeletini başlangıç noktası olarak kullanabilirsin.

---

## ▶️ Nasıl Çalıştırılır? (Kod Demoları)

Bu klasörde, deepfake konu anlatımını destekleyen iki küçük Python demo dosyası vardır:

- `train_demo.py` → `multimedya-guvenligi-ai/src/training/train_deepfake.py` içindeki `train()` fonksiyonunu çağırarak **dummy veri ile kısa bir eğitim demosu** çalıştırır.
- `predict_demo.py` → `multimedya-guvenligi-ai/src/inference/predict_deepfake.py` içindeki `predict_video()` fonksiyonunu çağırarak **rastgele bir görüntü tensörü üzerinde dummy skor üretir**.

Örnek kullanım (bu klasörden):

```bash
cd deepfake
python train_demo.py

python predict_demo.py
```

> Not: Kodların çalışması için aynı repoda `multimedya-guvenligi-ai/` projesi
> bulunmalı ve oradaki `requirements.txt` dosyasındaki bağımlılıklar
> kurulmuş olmalıdır.
