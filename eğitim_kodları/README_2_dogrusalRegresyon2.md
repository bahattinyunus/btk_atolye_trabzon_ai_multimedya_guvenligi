# 2_dogrusalRegresyon2.py - Çoklu Doğrusal Regresyon (California Housing)

## 📖 Kod Açıklaması

Bu kod, **çoklu doğrusal regresyon** (multiple linear regression) kullanarak gerçek bir veri seti üzerinde ev fiyat tahmini yapar. Birden fazla özelliğin (bağımsız değişken) bir hedef değişkeni nasıl etkilediğini gösterir.

---

## 🎯 Amaç

**California Ev Fiyatları** veri setini kullanarak, ev özelliklerine bakarak fiyat tahmini yapmak.

**Veri Seti:** scikit-learn'ün California Housing dataset
- **20,640 örnek** (ev)
- **8 özellik** (gelir, oda sayısı, konum vb.)
- **1 hedef:** Ev fiyatı (yüz binlerce dolar)

---

## 📊 Kod İçeriği ve Adımlar

### 1. **Veri Setini Yükleme**
```python
housing = fetch_california_housing()
X = housing.data      # Özellikler
y = housing.target    # Hedef (fiyat)
```

**8 Özellik:**
1. **MedInc** - Medyan gelir
2. **HouseAge** - Ev yaşı
3. **AveRooms** - Ortalama oda sayısı
4. **AveBedrms** - Ortalama yatak odası sayısı
5. **Population** - Bölge nüfusu
6. **AveOccup** - Ortalama doluluk oranı
7. **Latitude** - Enlem (konum)
8. **Longitude** - Boylam (konum)

### 2. **Veriyi İnceleme**
```python
df = pd.DataFrame(X, columns=housing.feature_names)
print(df.describe())
```

**Çıktı:**
```
       MedInc    HouseAge   AveRooms  ...
count  20640.0   20640.0    20640.0  ...
mean   3.87      28.64      5.43     ...
std    1.90      12.59      2.47     ...
```

İstatistiksel özet ile veriyi tanıyoruz.

### 3. **Veri Bölme**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

- **Eğitim:** 16,512 örnek (%80)
- **Test:** 4,128 örnek (%20)

### 4. **Model Eğitimi**
```python
model = LinearRegression()
model.fit(X_train, y_train)
```

**Çoklu regresyon denklemi:**
```
y = w₁*x₁ + w₂*x₂ + ... + w₈*x₈ + b
```

Model, 8 farklı ağırlığı (w₁...w₈) ve 1 bias (b) öğrenir.

### 5. **Model Parametreleri**
```python
print(f"Bias: {model.intercept_:.4f}")
print("Katsayılar:", model.coef_)
```

**Çıktı Örneği:**
```
Bias (Kesim Noktası): -37.0233

Özellik Önem Sıralaması:
     Özellik   Katsayı
   AveBedrms  0.783145    # En yüksek etki
      MedInc  0.448675
   Longitude -0.433708
    Latitude -0.419792
    ...
```

**Yorumlama:**
- **MedInc (0.45):** Gelir 1 birim arttığında, fiyat ~0.45 birim artar
- **Latitude (-0.42):** Güneye gittikçe fiyat düşer (negatif katsayı)

### 6. **Tahmin Yapma**
```python
y_pred = model.predict(X_test)
```

Test setindeki 4,128 ev için fiyat tahmini yapılır.

### 7. **Model Değerlendirme**
```python
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

**Çıktı:**
```
MSE: 0.5559
RMSE: 0.7456
R² Skoru: 0.5758
```

**Yorumlama:**
- **R² = 0.5758:** Model, fiyat varyansının **%57.6'sını** açıklıyor
- **RMSE = 0.7456:** Ortalama tahmin hatası ~74,560 dolar

### 8. **Örnek Tahmin**
```python
sample_features = X_test[0].reshape(1, -1)
predicted_price = model.predict(sample_features)[0]
```

**Çıktı:**
```
Örnek Ev Özellikleri:
  MedInc: 1.68
  HouseAge: 25.00
  AveRooms: 4.19
  ...

Gerçek Fiyat: 0.48 (48,000 dolar)
Tahmin Edilen Fiyat: 0.72 (72,000 dolar)
Hata: 0.2421 (24,210 dolar)
```

---

## 🔑 Önemli Kavramlar

### **Çoklu Doğrusal Regresyon**
Birden fazla bağımsız değişken kullanır:
```
y = w₁*x₁ + w₂*x₂ + ... + wₙ*xₙ + b
```

### **Katsayı Yorumlama**
- **Pozitif katsayı (+):** O özellik arttıkça hedef artar
- **Negatif katsayı (-):** O özellik arttıkça hedef azalır
- **Büyük katsayı:** O özellik daha etkilidir

### **Performans Metrikleri**

**1. MSE (Mean Squared Error)**
```
MSE = Σ(y_gerçek - y_tahmin)² / n
```
Düşük değer = İyi model

**2. RMSE (Root Mean Squared Error)**
```
RMSE = √MSE
```
Hedef değişkenle aynı birimde (daha yorumlanabilir)

**3. R² Score (Coefficient of Determination)**
```
R² = 1 - (SS_res / SS_tot)
```
- **0-1 arası** değer alır
- **1'e yakın:** Model çok iyi açıklıyor
- **0'a yakın:** Model zayıf

---

## 📈 Çıktı Analizi

```
=== MODEL PERFORMANSI ===
MSE: 0.5559
RMSE: 0.7456
R² Skoru: 0.5758

Model, ev fiyatlarındaki değişimin %57.6'ini açıklıyor.
```

**Değerlendirme:**
- R² = 0.58 → Orta-iyi seviye model
- Geriye kalan %42.4, modelde olmayan faktörlerden kaynaklanıyor
  (örn: evin durumu, renovasyon, mahalle kalitesi vb.)

---

## 🎓 Öğrenme Hedefleri

Bu kodu çalıştırdıktan sonra:

✅ Çoklu doğrusal regresyon nasıl çalışır
✅ Gerçek veri seti nasıl yüklenir ve incelenir
✅ Birden fazla özellik nasıl kullanılır
✅ Katsayılar nasıl yorumlanır (özellik önemi)
✅ Model performansı nasıl değerlendirilir (MSE, RMSE, R²)
✅ Yeni veriler için tahmin nasıl yapılır

---

## 🚀 Nasıl Çalıştırılır?

```bash
python 2_dogrusalRegresyon2.py
```

---

## 📦 Gerekli Kütüphaneler

```python
numpy
pandas
scikit-learn
```

Kurulum:
```bash
pip install numpy pandas scikit-learn
```

---

## 🔍 İleri Seviye İçin

### **Model İyileştirme Fikirleri:**

1. **Özellik Mühendisliği:**
   ```python
   # Yeni özellik oluştur
   df['rooms_per_household'] = df['AveRooms'] / df['AveOccup']
   ```

2. **Özellik Normalizasyonu:**
   ```python
   from sklearn.preprocessing import StandardScaler
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)
   ```

3. **Polynomial Regression:**
   ```python
   from sklearn.preprocessing import PolynomialFeatures
   poly = PolynomialFeatures(degree=2)
   X_poly = poly.fit_transform(X)
   ```

4. **Regularization (Ridge/Lasso):**
   ```python
   from sklearn.linear_model import Ridge, Lasso
   model = Ridge(alpha=1.0)  # Overfitting'i önler
   ```

---

## 🆚 1. Kod ile Farkı

| Özellik | 1_dogrusalRegresyon.py | 2_dogrusalRegresyon2.py |
|---------|------------------------|-------------------------|
| Değişken sayısı | 1 (basit) | 8 (çoklu) |
| Veri | Sentetik | Gerçek (California) |
| R² Skoru | 1.00 (mükemmel) | 0.58 (gerçekçi) |
| Karmaşıklık | Basit | Orta |
| Amaç | Temel kavramlar | Gerçek dünya uygulaması |

---

## 📌 Notlar

- Gerçek veri setleri sentetik verilerden daha zorludur
- R² = 0.58 kötü değildir, gerçek dünyada normaldir
- Daha iyi performans için özellik mühendisliği şarttır
- Konum verileri (Latitude/Longitude) fiyatı ciddi etkiler

---

## 🔗 İlgili Kodlar

- `1_dogrusalRegresyon.py` - Basit doğrusal regresyon
- `regresyon_izdusumu_projesi/` - İzdüşüm ve detaylı regresyon

---

**Hazırlayan:** BTK Atölye - Multimedya Güvenliği
**Tarih:** 2025
**Seviye:** Orta
