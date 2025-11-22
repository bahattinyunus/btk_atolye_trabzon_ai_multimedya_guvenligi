# 1_dogrusalRegresyon.py - Basit Doğrusal Regresyon

## 📖 Kod Açıklaması

Bu kod, **basit doğrusal regresyon** algoritmasının temel kullanımını öğretmek için hazırlanmış eğitim amaçlı bir örnektir.

---

## 🎯 Amaç

Tek bir bağımsız değişken (X) ile bağımlı değişken (y) arasındaki **doğrusal ilişkiyi** modellemek ve tahmin yapmak.

**Örnek Senaryo:** Bir evin metrekaresi ile fiyatı arasındaki ilişki

---

## 📊 Kod İçeriği ve Adımlar

### 1. **Veri Seti Hazırlama**
```python
X = np.random.rand(100, 1) * 100  # 0-100 arası metrekare
y = 3 * X.squeeze() + 10          # y = 3*X + 10 (gerçek ilişki)
```

- 100 adet sentetik veri noktası oluşturulur
- Gerçek ilişki: `y = 3*X + 10`
- Her 1 m² artış, fiyatı 3 bin TL artırır
- Temel fiyat: 10 bin TL

### 2. **Veriyi Görselleştirme**
```python
plt.scatter(X, y, alpha=0.7)
plt.xlabel('Metrekare (m²)')
plt.ylabel('Fiyat (Bin TL)')
```

**Neden?** Verinin dağılımını görmek ve doğrusal ilişki olup olmadığını anlamak için.

### 3. **Veri Bölme (Train-Test Split)**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

- **%80 Eğitim:** Model bu veriden öğrenir
- **%20 Test:** Modelin gerçek performansını ölçeriz
- `random_state=42`: Her çalıştırmada aynı bölmeyi sağlar

### 4. **Model Oluşturma ve Eğitim**
```python
model = LinearRegression()
model.fit(X_train, y_train)
```

**Arka planda neler olur?**
- Model, en küçük kareler yöntemiyle ağırlık (w) ve bias (b) değerlerini hesaplar
- Hata fonksiyonu minimize edilir: `minimize Σ(y_gerçek - y_tahmin)²`

### 5. **Model Katsayıları**
```python
print(f"Ağırlık (w): {model.coef_[0]:.2f}")
print(f"Bias (b): {model.intercept_:.2f}")
```

**Çıktı:**
```
Ağırlık (w): 3.00
Bias (b): 10.00
```

Model, gerçek ilişkiyi (`y = 3*X + 10`) mükemmel şekilde buldu!

### 6. **Tahmin Yapma**
```python
y_pred = model.predict(X_test)
```

Model, test setindeki metrekare değerlerine bakarak fiyat tahmini yapar.

### 7. **Model Değerlendirme**
```python
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

**Metrikler:**
- **MSE (Mean Squared Error):** Ortalama kare hata → 0.00 (mükemmel!)
- **R² Skoru:** Modelin açıklama gücü → 1.00 (mükemmel!)

### 8. **Sonuçları Görselleştirme**
```python
plt.scatter(X_test, y_test, color='blue', label='Gerçek Veri')
plt.plot(X_test_sorted, y_pred_sorted, color='red', linewidth=2, label='Doğrusal Regresyon')
```

Kırmızı çizgi (regresyon doğrusu), mavi noktaların (gerçek veri) arasından geçer.

---

## 🔑 Önemli Kavramlar

### **Doğrusal Regresyon Denklemi**
```
y = w * X + b
```

- **w (weight/ağırlık):** Eğim - X'in y üzerindeki etkisi
- **b (bias/kesim):** Y eksenini kestiği nokta
- **X:** Bağımsız değişken (girdi)
- **y:** Bağımlı değişken (çıktı/tahmin)

### **En Küçük Kareler Yöntemi**
Model, tahmin hataların karelerinin toplamını minimize eder:
```
minimize: Σ(y_gerçek - y_tahmin)²
```

---

## 📈 Çıktı Örneği

```
Ağırlık (w): 3.00
Bias (b): 10.00
Ortalama Kare Hata (MSE): 0.00
R² Skoru: 1.00
```

**Yorum:**
- Model, veriye mükemmel uyum sağladı (R² = 1.00)
- Tahminler gerçek değerlerle birebir örtüşüyor (MSE = 0.00)
- Her 1 m² artış, fiyatı 3 bin TL artırıyor

---

## 🎓 Öğrenme Hedefleri

Bu kodu çalıştırdıktan sonra şunları öğrenmiş olursunuz:

✅ Doğrusal regresyon nasıl çalışır
✅ Veri nasıl bölünür (train/test)
✅ Model nasıl eğitilir
✅ Katsayılar nasıl yorumlanır
✅ Model performansı nasıl değerlendirilir
✅ Tahmin sonuçları nasıl görselleştirilir

---

## 🚀 Nasıl Çalıştırılır?

```bash
python 1_dogrusalRegresyon.py
```

---

## 📦 Gerekli Kütüphaneler

```
numpy
matplotlib
scikit-learn
```

Kurulum:
```bash
pip install numpy matplotlib scikit-learn
```

---

## 🔍 İleri Seviye İçin

Bu basit örneği anladıktan sonra:

1. **Gürültülü veri** ekleyerek modelin performansını gözlemleyin
2. **Farklı veri setleri** deneyin
3. **Çoklu doğrusal regresyon**'a (2_dogrusalRegresyon2.py) geçin
4. **Polynomial regression** ile doğrusal olmayan ilişkileri modellemeyi öğrenin

---

## 📌 Notlar

- Bu kod **eğitim amaçlıdır**, gerçek projelerde veri ön işleme ve validasyon gereklidir
- Sentetik veri kullanılmıştır, gerçek veri setleriyle de deneyebilirsiniz
- Grafikler otomatik olarak açılır, kapatmak için pencereyi kapatın

---

**Hazırlayan:** BTK Atölye - Multimedya Güvenliği
**Tarih:** 2025
**Seviye:** Başlangıç
