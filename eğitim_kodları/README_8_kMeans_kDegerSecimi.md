# 🎯 K-Means K Değeri Seçimi Projesi

Bu proje, **K-Means Kümeleme Algoritması**'nda en kritik parametrelerden biri olan **K değerini (küme sayısını)** seçmek için kullanılan çeşitli yöntemleri kapsamlı bir şekilde göstermektedir.

## 📋 İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [K Değeri Seçim Yöntemleri](#k-değeri-seçim-yöntemleri)
- [Kod Yapısı](#kod-yapısı)
- [Sonuçlar](#sonuçlar)
- [Teknik Detaylar](#teknik-detaylar)
- [Öğrenme Çıktıları](#öğrenme-çıktıları)

## 🎯 Proje Hakkında

### Amaç
Bu proje, K-Means kümeleme algoritmasında **en uygun K değerini** seçmek için kullanılan farklı yaklaşımları öğretmeyi ve pratik olarak uygulamayı amaçlar.

### Problem
K-Means algoritmasında **K (küme sayısı)** parametresi önceden belirlenmesi gereken kritik bir değerdir. Yanlış K seçimi:
- **Underclustering** (az küme): Farklı gruplar aynı kümede
- **Overclustering** (çok küme): Aynı grup farklı kümelerde

### Çözüm Yöntemleri
Bu proje 3 farklı yaklaşım kullanır:
- 🔧 **Elbow Method (Dirsek Yöntemi)**
- 📊 **Silhouette Analysis**
- 🧠 **Domain Knowledge (Alan Bilgisi)**

## 🔧 Kurulum

### Gerekli Kütüphaneler
```bash
pip install numpy scikit-learn
```

### Dosya Yapısı
```
├── 8_kMeans_kDegerSecimi.py          # Ana uygulama dosyası
└── README_8_kMeans_kDegerSecimi.md   # Bu döküman
```

## 🚀 Kullanım

### Basit Çalıştırma
```bash
python 8_kMeans_kDegerSecimi.py
```

### Program Akışı
1. **Veri hazırlama** ve standardizasyon
2. **Elbow Method** analizi (K=1-7)
3. **Silhouette Score** hesaplama (K=2-7)
4. **Domain Knowledge** değerlendirmesi
5. **Final K değeri** seçimi
6. **Seçilen K ile model** oluşturma

## 📊 K Değeri Seçim Yöntemleri

### 1. 🔧 Elbow Method (Dirsek Yöntemi)

**Prensip**: WCSS (Within-Cluster Sum of Squares) değişimini analiz eder

**Nasıl Çalışır**:
- Farklı K değerleri için WCSS hesaplanır
- WCSS azalma oranı incelenir
- En büyük azalma sonrası "dirsek noktası" bulunur

```python
# WCSS hesaplama
wcss_list = []
for k in range(1, 8):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X_scaled)
    wcss_list.append(kmeans.inertia_)
```

**Avantajları**:
- ✅ Basit ve anlaşılır
- ✅ Görsel olarak yorumlanabilir
- ✅ Hızlı hesaplama

**Dezavantajları**:
- ❌ Dirsek noktası belirsiz olabilir
- ❌ Subjektif yorum gerektirir

### 2. 📊 Silhouette Analysis

**Prensip**: Her veri noktasının kendi kümesine ne kadar uygun olduğunu ölçer

**Silhouette Score**:
- **+1**: Mükemmel kümeleme
- **0**: Küme sınırında
- **-1**: Yanlış kümede

```python
# Silhouette score hesaplama
for k in range(2, 8):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X_scaled)
    score = silhouette_score(X_scaled, kmeans.labels_)
```

**Avantajları**:
- ✅ Objektif metrik
- ✅ Küme kalitesini doğrudan ölçer
- ✅ -1 ile +1 arası normalize değer

**Dezavantajları**:
- ❌ Hesaplama maliyeti yüksek
- ❌ Büyük veriler için yavaş

### 3. 🧠 Domain Knowledge (Alan Bilgisi)

**Prensip**: Veri setinin doğal yapısını bilmek

**Iris Veri Seti İçin**:
- 3 çiçek türü → K=3 mantıklı
- Biyolojik sınıflandırma → Doğal gruplar

**Avantajları**:
- ✅ Gerçek dünya uyumu
- ✅ Yorumlanabilir sonuçlar
- ✅ İş gereksinimlerine uygun

**Dezavantajları**:
- ❌ Her zaman mevcut değil
- ❌ Öznel değerlendirme
- ❌ Verinin gizli yapıları kaçırılabilir

## 📁 Kod Yapısı

### 1. Veri Hazırlama
```python
# Iris veri setini yükle ve standardize et
iris = load_iris()
X = iris.data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 2. Elbow Method Implementasyonu
```python
# K değerleri için WCSS hesapla
K_degerleri = range(1, 8)
wcss_list = []
for k in K_degerleri:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss_list.append(kmeans.inertia_)
```

### 3. Silhouette Analizi
```python
# En iyi silhouette skorunu bul
best_silhouette = 0
best_k = 2
for k in range(2, 8):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    silhouette = silhouette_score(X_scaled, kmeans.labels_)
    if silhouette > best_silhouette:
        best_silhouette = silhouette
        best_k = k
```

### 4. Final Karar Mekanizması
```python
# Tüm yöntemlerin önerilerini birleştir
oylar = [dirsek_k, best_k, 3]  # Dirsek, Silhouette, Domain
final_k = max(set(oylar), key=oylar.count)
```

## 📈 Sonuçlar

### Beklenen Program Çıktısı

| Yöntem | Önerilen K | Değer/Skor |
|--------|------------|------------|
| **Elbow Method** | K = 2 | En büyük WCSS azalması |
| **Silhouette** | K = 2 | ~0.58 skor |
| **Domain Knowledge** | K = 3 | 3 çiçek türü |

### Tipik Sonuç Analizi
- **K=2**: Setosa vs (Versicolor+Virginica)
- **K=3**: Setosa vs Versicolor vs Virginica
- **Algoritmik tercih**: K=2 (daha iyi metrikler)
- **Mantıksal tercih**: K=3 (doğal gruplar)

### WCSS Değişim Tablosu
```
K |   WCSS   | Değişim
1 |   600.0  |    -
2 |   222.4  |  377.6  ← En büyük düşüş
3 |   139.8  |   82.5
4 |   114.1  |   25.7
5 |    90.9  |   23.2
```

## ⚙️ Teknik Detaylar

### WCSS (Within-Cluster Sum of Squares)
**Formül**: Σ(veri noktası - küme merkezi)²
- Küme içi homojenliği ölçer
- Düşük WCSS = İyi kümeleme
- K arttıkça her zaman azalır

### Silhouette Score Hesaplama
**Formül**: (b - a) / max(a, b)
- **a**: Kendi kümesindeki ortalama mesafe
- **b**: En yakın diğer kümedeki ortalama mesafe

### Model Parametreleri
```python
KMeans(
    n_clusters=k,      # Küme sayısı
    random_state=42,   # Tekrarlanabilirlik
    n_init=10,         # 10 farklı başlangıç
    max_iter=300       # Maksimum iterasyon
)
```

## 🎓 Öğrenme Çıktıları

### Teorik Bilgiler
- ✅ **Elbow Method** prensipleri
- ✅ **Silhouette Analysis** hesaplaması
- ✅ **WCSS** kavramı ve önemi
- ✅ **Optimal K seçimi** stratejileri
- ✅ **Domain Knowledge** kullanımı
- ✅ **Bias-Variance tradeoff** kümelemede

### Pratik Beceriler
- ✅ **K değeri optimizasyonu**
- ✅ **Çoklu metrik değerlendirmesi**
- ✅ **Sonuç yorumlama** teknikleri
- ✅ **Karar verme** süreci
- ✅ **Model validasyonu**

## 🔍 Program Çıktısı Yorumlama

### Elbow Method Sonuçları
**K=1 → K=2**: Büyük WCSS azalması (377.6)
- Bu en önemli iyileştirme
- Veriyi 2 ana gruba ayırmanın faydalı olduğunu gösterir

**K=2 → K=3**: Orta seviye azalma (82.5)
- Hala anlamlı bir iyileştirme
- 3. kümenin eklenmesinin değerli olabileceğini gösterir

**K=3+**: Küçük azalmalar
- Diminishing returns (azalan verim)
- Fazla kümeleme riski

### Silhouette Sonuçları
**K=2**: En yüksek skor (0.582)
- Veri setini 2 gruba ayırmanın en uygun olduğunu gösterir
- Setosa'nın diğerlerinden net ayrımını yansıtır

**K=3**: Azalan skor (0.460)
- Versicolor-Virginica arası benzerlik nedeniyle düşüş
- Yine de kabul edilebilir seviyede

### Domain Knowledge Değerlendirmesi
**Biyolojik Gerçek**: 3 farklı çiçek türü
- İris Setosa: Diğerlerinden çok farklı
- Iris Versicolor: Orta özellikler
- Iris Virginica: Versicolor'a benzer

## 🤔 Hangi K'yı Seçmeli?

### Senaryo Analizi

**K=2 Seçilirse**:
- ✅ En iyi algoritmik metrikler
- ✅ Net küme ayrımı
- ❌ Biyolojik gerçekliği kaçırır
- **Kullanım**: Basit sınıflandırma gerekiyorsa

**K=3 Seçilirse**:
- ✅ Biyolojik gerçeklik
- ✅ Yorumlanabilir sonuçlar
- ❌ Düşük silhouette skor
- **Kullanım**: Detaylı analiz gerekiyorsa

### Karar Rehberi
1. **İş gereksinimini** belirle
2. **Veri yapısını** anla
3. **Metrikleri** karşılaştır
4. **Pratik kullanımı** düşün
5. **Final kararı** ver

## 🛠️ Troubleshooting

### Sık Karşılaşılan Durumlar

**Belirsiz Elbow Noktası**:
- Daha fazla K değeri dene
- Görselleştirme ekle
- İkinci türev hesapla

**Düşük Silhouette Skorları**:
- Veri ön işlemeyi kontrol et
- PCA boyut azaltma uygula
- Farklı kümeleme algoritması dene

**Çelişkili Sonuçlar**:
- Domain knowledge'ı ön planda tut
- Hibrit yaklaşım kullan
- A/B testing yap

## 🎯 İleri Seviye Teknikler

### Gap Statistic
```python
# Rastgele veri ile karşılaştırma
gap_stats = []
for k in range(1, 8):
    # Gerçek veri WCSS'si
    real_wcss = calculate_wcss(X, k)
    # Rastgele veri WCSS'si
    random_wcss = calculate_random_wcss(X.shape, k)
    gap = np.log(random_wcss) - np.log(real_wcss)
    gap_stats.append(gap)
```

### X-Means Algoritması
- Otomatik K seçimi
- BIC (Bayesian Information Criterion) kullanır
- K alt ve üst sınırları belirlenir

### Görselleştirme İyileştirmeleri
```python
import matplotlib.pyplot as plt
# WCSS eğrisi
plt.plot(K_degerleri, wcss_list, 'bo-')
plt.xlabel('K değeri')
plt.ylabel('WCSS')
plt.title('Elbow Method')
```

## 📚 Ek Kaynaklar

### Akademik Makaleler
- [Determining the number of clusters](https://web.stanford.edu/~hastie/Papers/gap.pdf)
- [Silhouette Analysis](https://www.sciencedirect.com/science/article/pii/0377042787901257)

### Praktik Kaynaklar
- [K-Means Clustering in Python](https://realpython.com/k-means-clustering-python/)
- [Choosing the number of clusters](https://towardsdatascience.com/clustering-metrics-better-than-the-elbow-method-6926e1f723a6)

### Araçlar ve Kütüphaneler
- **Scikit-learn**: Temel implementasyon
- **Yellowbrick**: Görselleştirme araçları
- **Kneed**: Otomatik elbow detection

## 🔬 Deneysel Genişletmeler

### Farklı Veri Setleri
- **Make_blobs**: Sentetik küme verileri
- **Wholesale customers**: Gerçek iş verisi
- **Image segmentation**: Görüntü kümeleme

### Alternatif Metrikler
- **Calinski-Harabasz Index**
- **Davies-Bouldin Index**
- **Adjusted Rand Index**

### Hibrit Yaklaşımlar
```python
# Ağırlıklı karar verme
weights = {'elbow': 0.3, 'silhouette': 0.4, 'domain': 0.3}
final_score = sum(weights[method] * scores[method] for method in weights)
```

## 💡 Best Practices

### Genel Öneriler
1. **Hiç bir metrik tek başına yeterli değildir**
2. **Domain knowledge'ı göz ardı etmeyin**
3. **Görselleştirme her zaman yardımcıdır**
4. **Çoklu metrik kullanın**
5. **Business impact'i unutmayın**

### Kod Kalitesi
- Reproducible results için `random_state` kullanın
- Veriyi mutlaka standardize edin
- Exception handling ekleyin
- Logging implementasyonu yapın

## 🎨 Görselleştirme Fikirleri

### Temel Grafikler
```python
# Elbow curve
plt.plot(K_values, wcss_values)
# Silhouette scores
plt.bar(K_values, silhouette_scores)
# Küme dağılımları
plt.scatter(X[:, 0], X[:, 1], c=labels)
```

### İleri Seviye
- **3D scatter plots**: Çok boyutlu veri
- **Heatmaps**: Mesafe matrisleri
- **Interactive plots**: Plotly ile
- **Animation**: Küme evrim süreci

---

**🔗 İlgili Projeler**: 
- `7_kMeans_iris.py` - Temel K-Means Implementasyonu
- `6_destekvektor_iris.py` - SVM Karşılaştırması
- `kümeler/` - Diğer Kümeleme Projeleri

**📧 İletişim**: BTK Atölye Multimedya Güvenliği Projesi kapsamında hazırlanmıştır.

**🏷️ Etiketler**: #MachineLearning #KMeans #Clustering #OptimalK #ElbowMethod #SilhouetteAnalysis #DataScience #Python

**⭐ Zorluk Seviyesi**: Orta-İleri | **⏱️ Tahmini Süre**: 30-45 dakika | **👥 Hedef Kitle**: ML öğrencileri, veri bilimciler