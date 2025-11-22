# Regresyon ve İzdüşüm ile Tahmin Projesi

## 📚 Proje Amacı

Bu proje, **doğrusal regresyon** kullanarak bağımsız değişkenlerin bağımlı değişkene nasıl izdüşüm yaptığını görsel ve pratik olarak anlamayı hedefler. Makine öğrenmesinin temel konularından biri olan regresyon analizi, veri setini eğitim ve test setlerine ayırma, model eğitimi ve tahmin yapma süreçlerini kapsar.

---

## 🎯 Regresyon Nedir?

**Regresyon**, bağımsız değişkenler (X) ile bağımlı değişken (y) arasındaki matematiksel ilişkiyi modelleme yöntemidir.

### Matematiksel Gösterim:
```
y = w₁·x₁ + w₂·x₂ + ... + wₙ·xₙ + b
```

- **y**: Tahmin edilecek değer (bağımlı değişken)
- **x₁, x₂, ..., xₙ**: Girdiler (bağımsız değişkenler)
- **w₁, w₂, ..., wₙ**: Ağırlıklar (katsayılar) - her özelliğin önemi
- **b**: Bias (kesim noktası)

---

## 🔍 İzdüşüm (Projection) Kavramı

Regresyonda **izdüşüm**, çok boyutlu uzaydaki veri noktalarının bir doğru veya düzlem üzerine projeksiyon edilmesi anlamına gelir.

### Geometrik Açıklama:
1. **Bağımsız değişkenler** (X): Çok boyutlu bir uzayda noktalar oluşturur
2. **Regresyon doğrusu/düzlemi**: Bu noktaları en iyi temsil eden çizgi
3. **İzdüşüm**: Her veri noktasının regresyon doğrusuna dik uzaklığı minimize edilir

Bu işlem, **En Küçük Kareler Yöntemi (Least Squares)** ile gerçekleştirilir:
```
Minimize: Σ(y_gerçek - y_tahmin)²
```

---

## 📂 Proje Yapısı

```
regresyon_izdusumu_projesi/
│
├── README.md                    # Bu dosya - proje açıklaması
├── requirements.txt             # Gerekli Python kütüphaneleri
│
├── 1_basit_regresyon.py        # Tek değişkenli basit regresyon
├── 2_coklu_regresyon.py        # Çok değişkenli regresyon
├── 3_izdusumu_gorsellestirme.py # İzdüşüm görselleştirmesi (3D)
│
└── data/                        # Veri setleri (isteğe bağlı)
```

---

## 🚀 Kurulum

### Gerekli Kütüphaneler:
```bash
pip install -r requirements.txt
```

**requirements.txt içeriği:**
```
numpy
pandas
scikit-learn
matplotlib
seaborn
```

---

## 📝 Kod Ana Hatları

### 1️⃣ VERİ HAZIRLAMA
```python
# Veri setini yükle veya oluştur
import pandas as pd
from sklearn.datasets import load_boston

data = load_boston()
X = data.data  # Bağımsız değişkenler
y = data.target  # Bağımlı değişken
```

**Amaç:** Ham veriyi modele uygun formata getirmek.

---

### 2️⃣ VERİYİ BÖLME (Train-Test Split)
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,    # %20 test, %80 eğitim
    random_state=42   # Tekrarlanabilirlik için
)
```

**Neden bölüyoruz?**
- **Eğitim seti**: Modelin öğrenmesi için
- **Test seti**: Modelin gerçek performansını ölçmek için (görmediği veriler)

---

### 3️⃣ MODEL OLUŞTURMA
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
```

**Model parametreleri:**
- `fit_intercept=True`: Bias terimini (b) otomatik hesapla
- `normalize=False`: Veri normalizasyonu (isteğe bağlı)

---

### 4️⃣ MODEL EĞİTİMİ
```python
model.fit(X_train, y_train)
```

**Arka planda olan:**
1. Model, w (ağırlıklar) ve b (bias) değerlerini hesaplar
2. En küçük kareler yöntemiyle hata minimize edilir
3. **İzdüşüm** burada gerçekleşir: Veri noktaları regresyon düzlemine projeksiyon edilir

---

### 5️⃣ TAHMİN YAPMA
```python
y_pred = model.predict(X_test)
```

**Tahmin denklemi:**
```
y_pred = w₁·x₁ + w₂·x₂ + ... + wₙ·xₙ + b
```

---

### 6️⃣ MODEL DEĞERLENDİRME
```python
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.2f}")
print(f"R² Skoru: {r2:.2f}")
```

**Metrikler:**
- **MSE (Mean Squared Error)**: Ortalama kare hata (düşük iyi)
- **R² Skoru**: Modelin açıklama gücü (0-1 arası, 1'e yakın iyi)

---

### 7️⃣ MODEL KATSAYILARİ
```python
print("Ağırlıklar (w):", model.coef_)
print("Bias (b):", model.intercept_)
```

**Yorumlama:**
- Pozitif katsayı: X arttıkça y artar
- Negatif katsayı: X arttıkça y azalır
- Büyük katsayı: O özellik daha önemli

---

### 8️⃣ GÖRSELLEŞTİRME (İzdüşüm)
```python
import matplotlib.pyplot as plt

# 2D İzdüşüm Görselleştirmesi
plt.scatter(X_test, y_test, label='Gerçek Değerler')
plt.plot(X_test, y_pred, color='red', label='Regresyon Doğrusu')
plt.xlabel('Bağımsız Değişken')
plt.ylabel('Bağımlı Değişken')
plt.legend()
plt.show()
```

**3D İzdüşüm:**
İki bağımsız değişken kullanarak 3 boyutlu uzayda regresyon düzlemini görselleştirebiliriz.

---

## 🧮 İzdüşüm Matematiği

### Normal Denklemler (Closed-Form Solution):
```
w = (XᵀX)⁻¹Xᵀy
```

Bu formül, **projeksiyon matris teorisi** kullanarak optimal ağırlıkları hesaplar.

### Geometrik Anlam:
- Hata vektörü (e = y - Xw) regresyon düzlemine **dik**tir
- Bu, veri noktalarının düzleme en kısa mesafede izdüşüm yapmasını sağlar

---

## 📊 Örnek Kullanım

### Basit Regresyon:
```bash
python 1_basit_regresyon.py
```

### Çoklu Regresyon:
```bash
python 2_coklu_regresyon.py
```

### 3D İzdüşüm Görselleştirmesi:
```bash
python 3_izdusumu_gorsellestirme.py
```

---

## 🎓 Öğrenme Hedefleri

Bu projeyi tamamladıktan sonra:
- ✅ Regresyonun matematiksel temellerini anlarsınız
- ✅ İzdüşüm kavramını geometrik olarak kavrayacaksınız
- ✅ Veri setini eğitim/test olarak ayırmayı öğrenirsiniz
- ✅ Model performansını değerlendirme metriklerini kullanırsınız
- ✅ Katsayıları yorumlayarak özellik önemini anlarsınız

---

## 📖 Ek Kaynaklar

- [Scikit-Learn Documentation](https://scikit-learn.org/stable/modules/linear_model.html)
- [Linear Regression Mathematics](https://en.wikipedia.org/wiki/Linear_regression)
- [Least Squares Projection](https://en.wikipedia.org/wiki/Projection_(linear_algebra))

---

## 🏆 İleri Seviye Konular

- **Ridge Regression**: L2 regularizasyon ile overfitting önleme
- **Lasso Regression**: L1 regularizasyon ile özellik seçimi
- **Polynomial Regression**: Doğrusal olmayan ilişkileri modelleme
- **Multiple Linear Regression**: Çok değişkenli izdüşüm

---

**Hazırlayan:** BTK Atölye - Multimedya Güvenliği
**Tarih:** 2025
