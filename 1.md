# 🚀 Colab ve Turuba Model Eğitimi Rehberi

Bu dokümantasyon, **Google Colab** ve **Turuba** platformlarında makine öğrenmesi model eğitimi hakkında kapsamlı bilgi sağlar.

## 📋 İçindekiler

- [Google Colab Nedir?](#google-colab-nedir)
- [Turuba Nedir?](#turuba-nedir)
- [Platform Karşılaştırması](#platform-karşılaştırması)
- [Colab Kullanım Rehberi](#colab-kullanım-rehberi)
- [Turuba Kullanım Rehberi](#turuba-kullanım-rehberi)
- [Model Eğitimi Best Practices](#model-eğitimi-best-practices)
- [Maliyet Analizi](#maliyet-analizi)
- [Troubleshooting](#troubleshooting)

## 🌟 Google Colab Nedir?

### Genel Bakış
**Google Colaboratory (Colab)**, Google'ın sunduğu **ücretsiz bulut tabanlı Jupyter notebook** ortamıdır. Makine öğrenmesi ve veri bilimi projeleri için optimize edilmiştir.

### Temel Özellikler
- ✅ **Ücretsiz GPU/TPU** erişimi (sınırlı süre)
- ✅ **Python 3.x** desteği
- ✅ **Önceden yüklenmiş ML kütüphaneleri**
- ✅ **Google Drive entegrasyonu**
- ✅ **Jupyter Notebook** arayüzü
- ✅ **Gerçek zamanlı işbirliği**

### Avantajları
| Avantaj | Açıklama |
|---------|----------|
| **Ücretsiz** | Temel kullanım tamamen bedava |
| **Kurulum gereksiz** | Tarayıcıda çalışır |
| **Güçlü donanım** | GPU/TPU desteği |
| **Entegrasyon** | Google ekosistemi uyumu |
| **Paylaşım** | Kolay kod paylaşımı |

### Dezavantajları
| Dezavantaj | Açıklama |
|------------|----------|
| **Oturum sınırı** | 12 saatlik çalışma limiti |
| **Kaynak sınırı** | Ücretsiz GPU/TPU kısıtlı |
| **İnternet bağımlılığı** | Offline çalışmaz |
| **Veri transferi** | Büyük veri setlerinde yavaş |

## 🔧 Turuba Nedir?

### Genel Bakış
**Turuba**, Türkiye merkezli bir **yapay zeka ve makine öğrenmesi platformu**dur. Yerel veri güvenliği ve Türkçe dil desteği ile öne çıkar.

### Temel Özellikler
- ✅ **Yerel veri güvenliği** (Türkiye'de barındırma)
- ✅ **Türkçe arayüz** ve destek
- ✅ **Kurumsal çözümler**
- ✅ **Özelleştirilebilir altyapı**
- ✅ **KVKK uyumluluğu**
- ✅ **Yerel teknik destek**

### Avantajları
| Avantaj | Açıklama |
|---------|----------|
| **Veri güvenliği** | Türkiye'de veri saklama |
| **KVKK uyumu** | Yasal gereksinimlere uygun |
| **Yerel destek** | Türkçe teknik destek |
| **Özelleştirme** | Kurumsal ihtiyaçlara göre |
| **Performans** | Yerel ağ avantajı |

### Dezavantajları
| Dezavantaj | Açıklama |
|------------|----------|
| **Maliyet** | Genellikle ücretli |
| **Topluluk** | Küçük kullanıcı topluluğu |
| **Kaynaklar** | Sınırlı dokümantasyon |
| **Ekosistem** | Gelişmekte olan platform |

## ⚖️ Platform Karşılaştırması

### Özellik Karşılaştırması

| Özellik | Google Colab | Turuba |
|---------|--------------|--------|
| **Fiyat** | Ücretsiz/Ücretli | Ücretli |
| **GPU/TPU** | Ücretsiz sınırlı | Ücretli sınırsız |
| **Veri Güvenliği** | ABD/Global | Türkiye |
| **Dil Desteği** | İngilizce | Türkçe |
| **Topluluk** | Çok büyük | Küçük |
| **Dokümantasyon** | Kapsamlı | Gelişmekte |
| **Entegrasyon** | Google Workspace | Yerel sistemler |

### Kullanım Senaryoları

#### Google Colab Tercih Edilir:
- 🎓 **Eğitim ve öğrenme** projeleri
- 🔬 **Araştırma ve prototip** geliştirme
- 💡 **Hızlı deneyimler** yapma
- 🌍 **Uluslararası işbirliği**
- 💰 **Düşük bütçeli** projeler

#### Turuba Tercih Edilir:
- 🏢 **Kurumsal projeler**
- 🔒 **Hassas veri** işleme
- ⚖️ **KVKK uyumluluk** gerekliliği
- 🇹🇷 **Yerel pazara** odaklı projeler
- 🛡️ **Veri egemenliği** öncelikli

## 📖 Colab Kullanım Rehberi

### 1. Başlangıç

#### Hesap Oluşturma
```python
# Google hesabı ile giriş yapın
# https://colab.research.google.com/
```

#### İlk Notebook Oluşturma
```python
# Yeni dosya > Python 3 Notebook
# Dosya adını değiştirin
# İlk hücreyi çalıştırın
print("Merhaba Colab!")
```

### 2. GPU/TPU Aktivasyonu

#### GPU Etkinleştirme
```python
# Çalışma zamanı > Çalışma zamanı türünü değiştir > GPU
import torch
print(f"CUDA Available: {torch.cuda.is_available()}")
print(f"Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'}")
```

#### TPU Etkinleştirme
```python
# Çalışma zamanı > Çalışma zamanı türünü değiştir > TPU
import tensorflow as tf
print(f"TPU Available: {tf.test.is_built_with_cuda()}")
```

### 3. Temel Kütüphane Kurulumu

```python
# Gerekli kütüphaneleri yükle
!pip install torch torchvision torchaudio
!pip install tensorflow
!pip install scikit-learn pandas numpy matplotlib seaborn
!pip install transformers datasets

# Kurulumları kontrol et
import torch
import tensorflow as tf
import pandas as pd
import numpy as np
print("Tüm kütüphaneler başarıyla yüklendi!")
```

### 4. Veri Yükleme Yöntemleri

#### Google Drive Bağlantısı
```python
from google.colab import drive
drive.mount('/content/drive')

# Veri dosyasını okuma
import pandas as pd
data = pd.read_csv('/content/drive/MyDrive/dataset.csv')
print(data.head())
```

#### URL'den Veri İndirme
```python
!wget https://example.com/dataset.csv
data = pd.read_csv('dataset.csv')
```

#### Kaggle Veri Seti
```python
!pip install kaggle
!mkdir ~/.kaggle
!cp /content/drive/MyDrive/kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d dataset-name
```

### 5. Model Eğitimi Örneği

#### Basit CNN Modeli
```python
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Model oluşturma
model = keras.Sequential([
    keras.layers.Conv2D(32, 3, activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(64, 3, activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Model derleme
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Model eğitimi
history = model.fit(
    train_images, train_labels,
    epochs=10,
    validation_data=(test_images, test_labels),
    verbose=1
)
```

### 6. Model Kaydetme

```python
# Model kaydetme
model.save('/content/drive/MyDrive/my_model.h5')

# Model yükleme
loaded_model = keras.models.load_model('/content/drive/MyDrive/my_model.h5')
```

## 🔧 Turuba Kullanım Rehberi

### 1. Platform Erişimi

#### Hesap Oluşturma
```bash
# Turuba'nın resmi web sitesini ziyaret edin
# Kurumsal hesap başvurusu yapın
# API anahtarlarınızı alın
```

#### Bağlantı Kurma
```python
import requests
import json

# API konfigürasyonu
TURUBA_API_URL = "https://api.turuba.ai"
API_KEY = "your-api-key"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
```

### 2. Proje Başlatma

```python
# Yeni proje oluşturma
project_data = {
    "name": "İris Çiçek Sınıflandırma",
    "description": "Makine öğrenmesi ile çiçek türü tahmini",
    "type": "classification"
}

response = requests.post(
    f"{TURUBA_API_URL}/projects",
    headers=headers,
    json=project_data
)

project_id = response.json()["project_id"]
print(f"Proje ID: {project_id}")
```

### 3. Veri Yükleme

```python
# Veri seti yükleme
files = {'dataset': open('iris.csv', 'rb')}
response = requests.post(
    f"{TURUBA_API_URL}/projects/{project_id}/datasets",
    headers={"Authorization": f"Bearer {API_KEY}"},
    files=files
)

dataset_id = response.json()["dataset_id"]
```

### 4. Model Eğitimi

```python
# Eğitim parametreleri
training_config = {
    "algorithm": "random_forest",
    "parameters": {
        "n_estimators": 100,
        "max_depth": 10,
        "random_state": 42
    },
    "validation_split": 0.2
}

# Eğitimi başlatma
response = requests.post(
    f"{TURUBA_API_URL}/projects/{project_id}/train",
    headers=headers,
    json=training_config
)

job_id = response.json()["job_id"]
```

### 5. Eğitim Durumu Takibi

```python
import time

while True:
    response = requests.get(
        f"{TURUBA_API_URL}/jobs/{job_id}/status",
        headers=headers
    )
    
    status = response.json()["status"]
    print(f"Eğitim durumu: {status}")
    
    if status in ["completed", "failed"]:
        break
    
    time.sleep(10)
```

## 💡 Model Eğitimi Best Practices

### 1. Veri Ön İşleme

```python
# Veri kalitesi kontrolü
def check_data_quality(df):
    print(f"Veri boyutu: {df.shape}")
    print(f"Eksik değerler:\n{df.isnull().sum()}")
    print(f"Veri tipleri:\n{df.dtypes}")
    print(f"İstatistikler:\n{df.describe()}")

# Veri temizleme
def clean_data(df):
    # Eksik değerleri doldurma
    df = df.fillna(df.mean())
    
    # Outlier'ları temizleme
    from scipy import stats
    df = df[(np.abs(stats.zscore(df.select_dtypes(include=[np.number]))) < 3).all(axis=1)]
    
    return df
```

### 2. Model Performans Takibi

```python
# Eğitim sürecini görselleştirme
import matplotlib.pyplot as plt

def plot_training_history(history):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Doğruluk grafiği
    ax1.plot(history.history['accuracy'], label='Eğitim')
    ax1.plot(history.history['val_accuracy'], label='Doğrulama')
    ax1.set_title('Model Doğruluğu')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Doğruluk')
    ax1.legend()
    
    # Loss grafiği
    ax2.plot(history.history['loss'], label='Eğitim')
    ax2.plot(history.history['val_loss'], label='Doğrulama')
    ax2.set_title('Model Kaybı')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Kayıp')
    ax2.legend()
    
    plt.show()
```

### 3. Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

# Parametre ızgarası
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Grid search
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)
print(f"En iyi parametreler: {grid_search.best_params_}")
```

## 💰 Maliyet Analizi

### Google Colab Fiyatlandırma

| Plan | Fiyat | Özellikler |
|------|--------|------------|
| **Ücretsiz** | $0/ay | 12 saat oturum, sınırlı GPU |
| **Colab Pro** | $10/ay | Daha uzun oturum, öncelikli GPU |
| **Colab Pro+** | $50/ay | En uzun oturum, en iyi GPU |

### Turuba Fiyatlandırma

| Hizmet | Tahmini Maliyet | Açıklama |
|---------|----------------|-----------|
| **Temel Plan** | ₺500-1000/ay | Küçük projeler için |
| **Kurumsal** | ₺2000-5000/ay | Orta ölçekli projeler |
| **Özel Çözüm** | Teklif bazında | Büyük kurumsal projeler |

### ROI Hesaplama

```python
def calculate_roi(development_time_saved, cost_per_hour, platform_cost):
    """
    Yatırım getirisi hesaplama
    """
    time_savings_value = development_time_saved * cost_per_hour
    roi_percentage = ((time_savings_value - platform_cost) / platform_cost) * 100
    
    return {
        "time_savings_value": time_savings_value,
        "platform_cost": platform_cost,
        "net_benefit": time_savings_value - platform_cost,
        "roi_percentage": roi_percentage
    }

# Örnek hesaplama
result = calculate_roi(
    development_time_saved=40,  # 40 saat tasarruf
    cost_per_hour=100,          # Saat başı ₺100
    platform_cost=500           # Aylık platform maliyeti
)
print(f"ROI: %{result['roi_percentage']:.1f}")
```

## 🛠️ Troubleshooting

### Colab Yaygın Sorunlar

#### 1. GPU Erişim Sorunu
```python
# Çözüm: Runtime'ı resetleme
# Çalışma zamanı > Tümünü yeniden başlat
# Sonra GPU'yu tekrar etkinleştir

# GPU durumunu kontrol et
import torch
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
else:
    print("GPU bulunamadı!")
```

#### 2. Bellek Yetersizliği
```python
# Bellek temizleme
import gc
import torch

# Pytorch cache temizleme
if torch.cuda.is_available():
    torch.cuda.empty_cache()

# Python garbage collector
gc.collect()

# Bellek kullanımını kontrol et
!nvidia-smi
```

#### 3. Oturum Kesintisi
```python
# Otomatik yeniden bağlanma
import time
from IPython.display import Javascript

def keep_alive():
    display(Javascript('''
        function ClickConnect(){
            console.log("Keeping alive...");
            document.querySelector("colab-connect-button").click()
        }
        setInterval(ClickConnect,60000)
    '''))

keep_alive()
```

### Turuba Yaygın Sorunlar

#### 1. API Bağlantı Sorunu
```python
def test_connection():
    try:
        response = requests.get(
            f"{TURUBA_API_URL}/health",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            print("✅ Bağlantı başarılı")
        else:
            print(f"❌ Bağlantı hatası: {response.status_code}")
    except Exception as e:
        print(f"❌ Bağlantı hatası: {str(e)}")

test_connection()
```

#### 2. Veri Yükleme Hatası
```python
def upload_with_retry(file_path, max_retries=3):
    for attempt in range(max_retries):
        try:
            with open(file_path, 'rb') as f:
                files = {'dataset': f}
                response = requests.post(
                    f"{TURUBA_API_URL}/projects/{project_id}/datasets",
                    headers={"Authorization": f"Bearer {API_KEY}"},
                    files=files,
                    timeout=300
                )
            
            if response.status_code == 200:
                return response.json()["dataset_id"]
        except Exception as e:
            print(f"Deneme {attempt + 1} başarısız: {str(e)}")
            time.sleep(2 ** attempt)  # Exponential backoff
    
    raise Exception("Veri yükleme başarısız")
```

## 📚 Ek Kaynaklar

### Resmi Dokümantasyon
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Colab Pro Features](https://colab.research.google.com/signup)
- [Turuba Documentation](https://docs.turuba.ai) (varsayımsal)

### Eğitim Kaynakları
- [Colab ile Deep Learning](https://www.tensorflow.org/tutorials)
- [PyTorch Colab Tutorials](https://pytorch.org/tutorials/)
- [Makine Öğrenmesi Temelleri](https://developers.google.com/machine-learning/crash-course)

### Topluluk Kaynakları
- [Kaggle Colab Notebooks](https://www.kaggle.com/notebooks?search=colab)
- [GitHub Colab Examples](https://github.com/googlecolab)
- [Reddit r/MachineLearning](https://reddit.com/r/MachineLearning)

## 🎯 Sonuç ve Öneriler

### Platform Seçimi Kriterleri

1. **Bütçe Durumu**: Colab ücretsiz başlangıç için ideal
2. **Veri Güvenliği**: Hassas veriler için Turuba tercih edilmeli
3. **Proje Süresi**: Uzun projeler için Turuba daha uygun
4. **Ekip Büyüklüğü**: Büyük ekipler için kurumsal çözümler
5. **Teknik Destek**: Türkçe destek için Turuba avantajlı

### En İyi Uygulamalar

✅ **Her zaman veri yedeği** alın
✅ **Kod versiyonlaması** kullanın
✅ **Düzenli checkpoint** kayıtları yapın
✅ **Resource monitoring** uygulayın
✅ **Dokümantasyon** ihmal etmeyin

### Gelecek Trendleri

🔮 **AutoML** platformlarının yaygınlaşması
🔮 **MLOps** araçlarının entegrasyonu  
🔮 **Edge AI** çözümlerinin gelişimi
🔮 **Quantum ML** platformlarının ortaya çıkışı
🔮 **Sustainability** odaklı AI altyapıları

---

**📅 Son Güncelleme**: 2024
**✍️ Katkıda Bulunanlar**: BTK Atölye Ekibi
**🏷️ Etiketler**: #CloudComputing #MachineLearning #AI #Colab #Turuba #ModelTraining

**📞 İletişim**: BTK Atölye Multimedya Güvenliği Projesi kapsamında hazırlanmıştır.