# 🌺 K-Means ile Iris Çiçek Kümeleme Projesi

Bu proje, **K-Means Kümeleme Algoritması**'nı kullanarak Iris çiçek türlerini denetimsiz öğrenme yöntemiyle gruplandıran kapsamlı bir makine öğrenmesi uygulamasıdır.

## 📋 İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Algoritma Detayları](#algoritma-detayları)
- [Kod Yapısı](#kod-yapısı)
- [Sonuçlar](#sonuçlar)
- [Teknik Detaylar](#teknik-detaylar)
- [Öğrenme Çıktıları](#öğrenme-çıktıları)

## 🎯 Proje Hakkında

### Amaç
Bu proje, **K-Means Kümeleme** algoritmasının nasıl çalıştığını öğretmek ve **denetimsiz öğrenme** konseptini Iris çiçek veri seti üzerinde pratik olarak göstermeyi amaçlar.

### Veri Seti
- **Iris Çiçek Veri Seti** (scikit-learn'den)
- **150 çiçek örneği**
- **4 özellik**: Çanak ve taç yaprak uzunluk/genişlik
- **3 doğal grup**: Setosa, Versicolor, Virginica

### Temel Özellikler
- ✅ Denetimsiz öğrenme yaklaşımı
- ✅ K-Means kümeleme implementasyonu
- ✅ Veri ön işleme ve standardizasyon
- ✅ Küme merkezi analizi
- ✅ Gerçek etiketlerle karşılaştırma
- ✅ Yeni veri noktalari tahmini
- ✅ Küme kalite değerlendirmesi

## 🔧 Kurulum

### Gerekli Kütüphaneler
```bash
pip install numpy pandas scikit-learn
```

### Dosya Yapısı
```
├── 7_kMeans_iris.py              # Ana uygulama dosyası
└── README_7_kMeans_iris.md       # Bu döküman
```

## 🚀 Kullanım

### Basit Çalıştırma
```bash
python 7_kMeans_iris.py
```

### Program Akışı
Program şu aşamaları takip eder:
1. **Veri setini yükleme ve inceleme**
2. **Veri standardizasyonu**
3. **K-Means model kurulumu**
4. **Model eğitimi (kümeleme)**
5. **Kümeleme sonuçları analizi**
6. **Gerçek türlerle karşılaştırma**
7. **Küme merkezi inceleme**
8. **Yeni veri tahmini**
9. **Performans değerlendirmesi**
10. **Detaylı sonuç raporu**

## 🧠 Algoritma Detayları

### K-Means Nedir?

K-Means, **denetimsiz öğrenme** algoritmasıdır ve şu prensiple çalışır:
- Veriyi **K adet küme**ye ayırır
- Her nokta en yakın **küme merkezine** atanır
- Küme merkezleri **iteratif** olarak güncellenir
- **Yakınsama** sağlanana kadar devam eder

### Algoritma Adımları

1. **Başlangıç**: K adet rastgele küme merkezi seç
2. **Atama**: Her veri noktasını en yakın merkeze ata
3. **Güncelleme**: Küme merkezlerini yeniden hesapla
4. **Yakınsama**: Merkezler değişmeyene kadar tekrar et

### Denetimsiz Öğrenme Avantajları
- **Etiket gerekmez**: Önceden sınıf bilgisi olmadan çalışır
- **Keşfedici**: Veri setindeki doğal grupları bulur
- **Hızlı**: Büyük veri setlerinde etkili
- **Basit**: Anlaması ve uygulaması kolay

## 📁 Kod Yapısı

### 1. Veri Yükleme ve İnceleme
```python
# Iris veri setini yükle (etiketleri kullanmayız!)
iris = load_iris()
X = iris.data  # Sadece özellikler
y = iris.target  # Sadece doğruluk kontrolü için
```

### 2. Veri Standardizasyonu
```python
# K-Means ölçek hassasiyeti vardır
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 3. K-Means Modeli
```python
# K=3 (çünkü 3 çiçek türü olduğunu biliyoruz)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
```

### 4. Kümeleme Sonuçları
```python
# Küme etiketlerini al
cluster_labels = kmeans.labels_
# Küme merkezlerini al
cluster_centers = kmeans.cluster_centers_
```

## 📊 Sonuçlar

### Beklenen Performans

| Metrik | Değer |
|--------|--------|
| **Genel Doğruluk** | ~80-90% |
| **Küme Sayısı** | 3 |
| **İterasyon** | 3-6 |
| **Yakınsama** | Hızlı |

### Küme Başarı Oranları

| Çiçek Türü | Kümeleme Başarısı |
|------------|-------------------|
| **Setosa** | ~100% (Mükemmel) |
| **Versicolor** | ~70-80% |
| **Virginica** | ~70-80% |

### Küme Merkezi Özellikleri

| Küme | Çanak Uzunluk | Çanak Genişlik | Taç Uzunluk | Taç Genişlik |
|------|---------------|----------------|-------------|--------------|
| **0** | ~5.8 cm | ~2.7 cm | ~4.4 cm | ~1.4 cm |
| **1** | ~5.0 cm | ~3.4 cm | ~1.5 cm | ~0.2 cm |
| **2** | ~6.8 cm | ~3.1 cm | ~5.5 cm | ~2.0 cm |

## ⚙️ Teknik Detaylar

### K-Means Parametreleri

**n_clusters**: Küme sayısı
- Bu projede **K=3** (3 çiçek türü için)

**random_state**: Rastgelelik kontrolü
- **42** (tekrarlanabilir sonuçlar için)

**n_init**: Farklı başlangıç denemesi
- **10** (en iyi sonucu seçmek için)

**max_iter**: Maksimum iterasyon
- **300** (yakınsama için yeterli)

### Mesafe Hesaplama
- **Öklid mesafesi** kullanılır
- **Standardizasyon** kritik öneme sahiptir
- **Küme merkezleri** sürekli güncellenir

### Değerlendirme Metrikleri

**Küme İç Tutarlılık**:
- Aynı kümedeki noktalar benzer olmalı

**Küme Ayrımı**:
- Farklı kümeler birbirinden uzak olmalı

**Silhouette Score**:
- Küme kalitesini ölçer (-1 ile +1 arası)

## 🎓 Öğrenme Çıktıları

Bu projeyi tamamladıktan sonra öğrenecekleriniz:

### Teorik Bilgiler
- ✅ **Denetimsiz öğrenme** konsepti
- ✅ **K-Means algoritması** çalışma prensibi
- ✅ **Küme analizi** teknikleri
- ✅ **Mesafe metrikleri** kullanımı
- ✅ **Yakınsama** kriterleri
- ✅ **Küme sayısı** seçim stratejileri

### Pratik Beceriler
- ✅ **Scikit-learn** ile kümeleme
- ✅ **Veri ön işleme** teknikleri
- ✅ **Küme görselleştirmesi**
- ✅ **Model değerlendirmesi**
- ✅ **Sonuç yorumlama**

## 🔍 Program Çıktısı Analizi

### Başarı Değerlendirmesi

**Mükemmel (>%85)**:
- Setosa tamamen ayrılır
- Diğer türlerde minimal karışıklık

**İyi (%75-85)**:
- Çoğu çiçek doğru kümelenir
- Bazı sınır vakaları karışır

**Orta (%65-75)**:
- Genel grup yapısı korunur
- Versicolor-Virginica karışıklığı

**Zayıf (<%65)**:
- Kümeleme rastgele görünür
- Algoritmik parametreler gözden geçirilmeli

### Küme Kalite İndikatörleri

1. **Setosa İzolasyonu**: En kolay ayrılan grup
2. **Küme Boyut Dengesi**: ~50'şer çiçek ideal
3. **Merkez Stabilite**: Az iterasyonda yakınsama
4. **Özellik Ayrımı**: Taç yaprak en belirleyici

## 🛠️ Troubleshooting

### Sık Karşılaşılan Sorunlar

**Problem**: Düşük kümeleme kalitesi
**Çözümler**:
- Veri standardizasyonu uygulayın
- Farklı K değerleri deneyin
- Random state değiştirin
- Daha fazla n_init kullanın

**Problem**: Yavaş yakınsama
**Çözümler**:
- max_iter artırın
- Daha iyi başlangıç noktaları seçin
- Veri ön işlemeyi kontrol edin

**Problem**: İstikrarsız sonuçlar
**Çözümler**:
- random_state sabitleyip
- n_init değerini artırın
- Veri kalitesini kontrol edin

## 🔬 Denetimsiz vs Denetimli Öğrenme

### Bu Projede Karşılaştırma

| Özellik | K-Means (Denetimsiz) | SVM (Denetimli) |
|---------|----------------------|-----------------|
| **Etiket Gereksinimi** | Hayır | Evet |
| **Doğruluk** | ~83% | ~97% |
| **Keşif Yeteneği** | Yüksek | Düşük |
| **Hız** | Hızlı | Orta |
| **Yorumlama** | Kolay | Orta |

### Ne Zaman Hangisini Kullanmalı?

**K-Means Tercih Edilir**:
- Etiket yoksa
- Veri keşfi amaçlıysa
- Hızlı sonuç gerekiyorsa
- Grup yapısını anlamak istiyorsak

**SVM Tercih Edilir**:
- Etiket mevcutsa
- Yüksek doğruluk gerekiyorsa
- Sınıflandırma amaçlıysa
- Karmaşık karar sınırları varsa

## 📈 Gelişmiş Özellikler

### Optimal K Seçimi (Elbow Method)
```python
# Farklı K değerleri için WCSS hesapla
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
```

### Silhouette Analizi
```python
from sklearn.metrics import silhouette_score
score = silhouette_score(X_scaled, cluster_labels)
```

### Küme Görselleştirme
```python
import matplotlib.pyplot as plt
# PCA ile 2D'ye indirge ve görselleştir
```

## 📚 Ek Kaynaklar

### Teorik Kaynaklar
- [K-Means Wikipedia](https://en.wikipedia.org/wiki/K-means_clustering)
- [Scikit-learn K-Means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [Clustering Algorithms Comparison](https://scikit-learn.org/stable/modules/clustering.html)

### Pratik Kaynaklar
- [K-Means Tutorial](https://www.datacamp.com/tutorial/k-means-clustering-python)
- [Clustering Evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation)

## 💡 İleri Seviye Konular

### K-Means Varyasyonları
- **K-Means++**: Daha iyi başlangıç seçimi
- **Mini-batch K-Means**: Büyük veriler için
- **Fuzzy C-Means**: Yumuşak kümeleme

### Alternatif Kümeleme Algoritmaları
- **Hierarchical Clustering**: Dendogram ile
- **DBSCAN**: Yoğunluk tabanlı
- **Gaussian Mixture Models**: Olasılıksal yaklaşım

## 🎯 Proje Genişletme Fikirleri

1. **Görselleştirme**: Kümeleri 2D/3D çizim
2. **Optimizasyon**: Otomatik K seçimi
3. **Karşılaştırma**: Diğer algoritmalarla
4. **Interaktif**: Web arayüzü ekleme
5. **Gerçek Veri**: Farklı veri setlerinde test

---

**🔗 İlgili Projeler**: 
- `6_destekvektor_iris.py` - SVM Sınıflandırma
- `anamoli_tespiti/` - Anomali Tespiti
- `kümeler/` - Kümeleme Projeleri

**📧 İletişim**: BTK Atölye Multimedya Güvenliği Projesi kapsamında hazırlanmıştır.

**🏷️ Etiketler**: #MachineLearning #Clustering #KMeans #UnsupervisedLearning #Iris #DataScience #Python