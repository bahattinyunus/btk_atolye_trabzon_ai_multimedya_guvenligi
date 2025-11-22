# 🌸 SVM ile Iris Çiçek Sınıflandırma Projesi

Bu proje, **Support Vector Machine (SVM)** algoritmasını kullanarak Iris çiçek türlerini sınıflandıran kapsamlı bir makine öğrenmesi uygulamasıdır.

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
Bu proje, **Destek Vektör Makinaları (Support Vector Machine)** algoritmasının nasıl çalıştığını öğretmek ve Iris çiçek veri seti üzerinde pratik uygulama yapmayı amaçlar.

### Veri Seti
- **Iris Çiçek Veri Seti** (scikit-learn'den)
- **150 çiçek örneği**
- **4 özellik**: Çanak ve taç yaprak uzunluk/genişlik
- **3 tür**: Setosa, Versicolor, Virginica

### Temel Özellikler
- ✅ Veri ön işleme ve standardizasyon
- ✅ SVM model eğitimi
- ✅ Farklı çekirdek fonksiyonları karşılaştırması
- ✅ Hyperparameter optimizasyonu
- ✅ Detaylı performans analizi
- ✅ Yeni veri tahmini
- ✅ Özellik önem analizi

## 🔧 Kurulum

### Gerekli Kütüphaneler
```bash
pip install numpy pandas scikit-learn
```

### Dosya Yapısı
```
├── 6_destekvektor_iris.py    # Ana uygulama dosyası
└── README_6_destekvektor_iris.md   # Bu döküman
```

## 🚀 Kullanım

### Basit Çalıştırma
```bash
python 6_destekvektor_iris.py
```

### Beklenen Çıktı
Program şu aşamaları takip eder:
1. **Veri yükleme ve inceleme**
2. **Veri standardizasyonu**
3. **Eğitim/test ayrımı**
4. **SVM model eğitimi**
5. **Model test etme**
6. **Çekirdek karşılaştırması**
7. **Parametre optimizasyonu**
8. **Yeni tahmin örneği**
9. **Özellik önem analizi**
10. **Sonuç özeti**

## 🧠 Algoritma Detayları

### Support Vector Machine (SVM) Nedir?

SVM, **denetimli öğrenme** algoritmasıdır ve şu prensiple çalışır:
- Sınıflar arasında **maksimum ayrım** sağlayan karar sınırı bulur
- **Destek vektörleri** kullanarak optimal karar yüzeyi oluşturur
- Hem **sınıflandırma** hem **regresyon** için kullanılabilir

### Çekirdek Fonksiyonları

Program 3 farklı çekirdek test eder:

1. **Linear (Doğrusal)**
   - Basit, hızlı
   - Doğrusal ayrılabilir veriler için ideal

2. **RBF (Radial Basis Function)**
   - En popüler çekirdek
   - Doğrusal olmayan problemler için

3. **Polynomial (Polinom)**
   - Karmaşık karar sınırları
   - Derece parametresi ayarlanabilir

## 📁 Kod Yapısı

### 1. Veri Yükleme ve İnceleme
```python
# Iris veri setini yükle
iris = load_iris()
X = iris.data  # Özellikler
y = iris.target  # Etiketler
```

### 2. Veri Ön İşleme
```python
# Standardizasyon (SVM için kritik!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 3. Model Eğitimi
```python
# SVM modeli oluştur ve eğit
model = SVC(kernel='rbf', C=1.0, random_state=42)
model.fit(X_train, y_train)
```

### 4. Performans Değerlendirmesi
```python
# Tahmin ve doğruluk
tahminler = model.predict(X_test)
dogruluk = accuracy_score(y_test, tahminler)
```

## 📊 Sonuçlar

### Beklenen Performans Metrikleri

| Metrik | Değer |
|--------|--------|
| **Doğruluk** | ~96-100% |
| **Test Seti Boyutu** | 30 çiçek |
| **Destek Vektör Oranı** | ~40% |

### Çekirdek Karşılaştırması

| Çekirdek | Ortalama Doğruluk |
|----------|-------------------|
| **Linear** | ~100% |
| **RBF** | ~97% |
| **Polynomial** | ~90% |

### Özellik Önemleri
1. **Taç yaprak genişliği** (en önemli)
2. **Taç yaprak uzunluğu**
3. **Çanak yaprak uzunluğu**
4. **Çanak yaprak genişliği**

## ⚙️ Teknik Detaylar

### Hyperparametreler

**C Parametresi**: Düzenleme katsayısı
- **C = 0.1**: Daha basit model, underfitting riski
- **C = 1.0**: Dengeli (varsayılan)
- **C = 10+**: Karmaşık model, overfitting riski

**Kernel Parametreleri**:
- **RBF**: Gamma parametresi (varsayılan: 'scale')
- **Poly**: Derece parametresi (varsayılan: 3)

### Veri Bölümü
- **Eğitim**: 80% (120 örnek)
- **Test**: 20% (30 örnek)
- **Stratify**: Sınıf dağılımı korunur

### Model Değerlendirme
- **Accuracy Score**: Genel doğruluk
- **Classification Report**: Detaylı metrikler
- **Confusion Matrix**: Sınıf karışıklığı
- **Decision Function**: Karar fonksiyonu değerleri

## 🎓 Öğrenme Çıktıları

Bu projeyi tamamladıktan sonra öğrenecekleriniz:

### Teorik Bilgiler
- ✅ SVM algoritmasının çalışma prensibi
- ✅ Çekirdek fonksiyonlarının rolü
- ✅ Hyperparameter optimizasyonu
- ✅ Veri standardizasyonunun önemi
- ✅ Overfitting/Underfitting kavramları

### Pratik Beceriler
- ✅ Scikit-learn ile SVM kullanımı
- ✅ Veri ön işleme teknikleri
- ✅ Model performans değerlendirmesi
- ✅ Çapraz doğrulama
- ✅ Görselleştirme teknikleri

## 🔍 Program Çıktısı Analizi

### Başarı Kriterleri
- **%95+ Doğruluk**: Mükemmel
- **%90-95 Doğruluk**: Çok İyi
- **%85-90 Doğruluk**: İyi
- **<%85 Doğruluk**: Geliştirilebilir

### Dikkat Edilecek Noktalar
1. **Setosa** türü genellikle mükemmel ayrılır
2. **Versicolor** ve **Virginica** arası karışıklık olabilir
3. **Linear çekirdek** bu veri setinde çok başarılı
4. **Standardizasyon** olmadan performans düşer

## 🛠️ Troubleshooting

### Sık Karşılaşılan Sorunlar

**Problem**: Düşük doğruluk oranı
**Çözüm**: 
- Veri standardizasyonu kontrol edin
- Farklı C değerleri deneyin
- Çekirdek fonksiyonunu değiştirin

**Problem**: Aşırı öğrenme (Overfitting)
**Çözüm**:
- C parametresini düşürün
- Cross-validation kullanın
- Daha fazla veri toplayın

## 📚 Ek Kaynaklar

- [Scikit-learn SVM Dokumentasyonu](https://scikit-learn.org/stable/modules/svm.html)
- [SVM Tutorial](https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf)
- [Iris Dataset Info](https://archive.ics.uci.edu/ml/datasets/iris)

## 👨‍💻 Geliştirici Notları

Bu kod eğitim amaçlı yazılmıştır ve şu özellikleri içerir:
- **Detaylı açıklamalar**
- **Adım adım işlem**
- **Görsel çıktılar**
- **Pratik örnekler**

---

**🔗 İlgili Projeler**: 
- `7_kMeans_iris.py` - K-Means Kümeleme
- `regresyon_izdusumu_projesi/` - Regresyon Analizi

**📧 İletişim**: BTK Atölye Multimedya Güvenliği Projesi kapsamında hazırlanmıştır.