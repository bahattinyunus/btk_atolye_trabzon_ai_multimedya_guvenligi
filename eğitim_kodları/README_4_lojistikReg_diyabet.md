# 4_lojistikReg_diyabet.py - Lojistik Regresyon (Diyabet Tahmini)

## 📖 Kod Açıklaması

Bu kod, **lojistik regresyon** (logistic regression) kullanarak diyabet riskini sınıflandırır. Doğrusal regresyondan farklı olarak, **kategorik çıktı** (0/1, evet/hayır) tahmin eder.

---

## 🎯 Amaç

Hastanın sağlık verilerine bakarak **diyabet riskini** (düşük/yüksek) tahmin etmek.

**Problem Tipi:** İkili Sınıflandırma (Binary Classification)
- **Sınıf 0:** Düşük risk / Negatif
- **Sınıf 1:** Yüksek risk / Pozitif

---

## 🔄 Doğrusal vs Lojistik Regresyon

| Özellik | Doğrusal Regresyon | Lojistik Regresyon |
|---------|--------------------|--------------------|
| **Çıktı tipi** | Sürekli sayı | Kategorik (0/1) |
| **Örnek** | Ev fiyatı tahmini | Hastalık var/yok |
| **Fonksiyon** | y = wx + b | y = σ(wx + b) |
| **Amaç** | Değer tahmini | Sınıflandırma |
| **Metrik** | MSE, R² | Accuracy, Precision |

**Sigmoid Fonksiyonu:**
```
σ(z) = 1 / (1 + e^(-z))
```
Çıktıyı 0-1 arasına sıkıştırır (olasılık)

---

## 📊 Kod İçeriği ve Adımlar

### 1. **Veri Seti Hazırlama**
```python
diabetes = load_diabetes()
X = diabetes.data[:, :10]  # 10 özellik
y = (diabetes.target > diabetes.target.median()).astype(int)
```

**10 Özellik:**
- age (yaş)
- sex (cinsiyet)
- bmi (vücut kitle indeksi)
- bp (kan basıncı)
- s1, s2, s3, s4, s5, s6 (çeşitli kan testi sonuçları)

**Hedef Değişken:**
- Orijinal veri sürekli → İkili sınıfa dönüştürüldü
- Medyan değerin üstü: **1** (Yüksek risk)
- Medyan değerin altı: **0** (Düşük risk)

### 2. **Sınıf Dağılımı**
```python
print("Sınıf Dağılımı:", np.bincount(y))
```

**Çıktı:**
```
Sınıf Dağılımı: [242 200]
0 (Negatif/Düşük Risk): 242
1 (Pozitif/Yüksek Risk): 200
```

Dengeli bir veri seti (iyi durum!)

### 3. **Veri Bölme**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
```

**stratify=y:** Her sette sınıf oranlarını korur

### 4. **Model Eğitimi**
```python
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)
```

**Lojistik Regresyon Denklemi:**
```
P(y=1|X) = σ(w₁x₁ + w₂x₂ + ... + w₁₀x₁₀ + b)
```

- Model, 0.5'ten büyük olasılıkları **1**, küçükleri **0** olarak sınıflandırır

### 5. **Tahmin ve Olasılıklar**
```python
y_pred = model.predict(X_test)               # Sınıf (0 veya 1)
y_pred_proba = model.predict_proba(X_test)  # Olasılık [P(0), P(1)]
```

**Örnek:**
```
Tahmin: 1 (Yüksek risk)
Olasılıklar: [0.38, 0.62]
  → %38 düşük risk, %62 yüksek risk
```

### 6. **Model Performansı**
```python
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Doğruluğu: {accuracy:.3f}")
```

**Çıktı:**
```
Test Doğruluğu: 0.775 (%77.5)
```

### 7. **Karmaşıklık Matrisi (Confusion Matrix)**
```python
confusion = confusion_matrix(y_test, y_pred)
```

**Çıktı:**
```
[[44  5]    True Negative: 44  | False Positive: 5
 [15 25]]   False Negative: 15 | True Positive: 25
```

**Yorumlama:**
- **True Negative (44):** Düşük risk dediğimiz 44 kişi gerçekten düşük riskli ✓
- **False Positive (5):** 5 kişiye yanlış yüksek risk dedik ✗
- **False Negative (15):** 15 yüksek riskli hastayı kaçırdık ✗ (TEHLİKELİ!)
- **True Positive (25):** 25 yüksek riskli hastayı doğru bulduk ✓

### 8. **Sınıflandırma Raporu**
```python
print(classification_report(y_test, y_pred))
```

**Çıktı:**
```
              precision    recall  f1-score   support

           0       0.75      0.90      0.81        49
           1       0.83      0.62      0.71        40

    accuracy                           0.78        89
```

**Metrik Açıklamaları:**

**Precision (Kesinlik):**
```
Precision = TP / (TP + FP)
```
- Sınıf 1 için: 25 / (25 + 5) = 0.83
- "Pozitif dediğimizin %83'ü gerçekten pozitif"

**Recall (Duyarlılık):**
```
Recall = TP / (TP + FN)
```
- Sınıf 1 için: 25 / (25 + 15) = 0.62
- "Gerçek pozitiflerin %62'sini bulduk"

**F1-Score (Harmonik Ortalama):**
```
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

### 9. **Özellik Önemi**
```python
feature_importance = pd.DataFrame({
    'Özellik': feature_names,
    'Katsayı': model.coef_[0]
}).sort_values('Katsayı', key=abs, ascending=False)
```

**Çıktı:**
```
  Özellik   Katsayı
      s5  2.616106   # EN ÖNEMLİ
     bmi  2.461243
      bp  2.215508
      s3 -1.562480   # Negatif etki
```

**Yorumlama:**
- **s5 (+2.62):** En güçlü pozitif etki (arttıkça risk artar)
- **bmi (+2.46):** Yüksek BMI → Yüksek risk
- **s3 (-1.56):** Negatif katsayı (arttıkça risk azalır)

### 10. **Yeni Hasta Tahmini**
```python
yeni_hasta = [[0.02, -0.04, 0.05, 0.01, -0.03, 0.02, 0.01, 0.00, 0.03, -0.01]]
tahmin = model.predict(yeni_hasta)
olasilik = model.predict_proba(yeni_hasta)
```

**Çıktı:**
```
Tahmin Edilen Sınıf: 0
Olasılık Dağılımı: [0.509, 0.491]
Pozitif Sınıf Olasılığı: 0.491
SONUÇ: Diyabet riski DÜŞÜK
```

---

## 🔑 Önemli Kavramlar

### **Sigmoid Fonksiyonu**
```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

- Herhangi bir sayıyı 0-1 arasına çevirir
- 0.5 eşik değeri: >0.5 → Sınıf 1, <0.5 → Sınıf 0

### **Karar Eşiği (Decision Threshold)**
```python
# Varsayılan: 0.5
# Özelleştirilmiş:
threshold = 0.7  # Daha muhafazakar
y_pred_custom = (y_pred_proba[:, 1] >= threshold).astype(int)
```

Medikal uygulamalarda False Negative azaltmak için eşik düşürülür.

### **Precision vs Recall Trade-off**
- **Yüksek Precision ister misiniz?** → Eşiği artırın (0.7, 0.8)
- **Yüksek Recall ister misiniz?** → Eşiği azaltın (0.3, 0.4)
- **Diyabet vakasında:** Recall önemli (hasta kaçırmak tehlikeli!)

---

## 📈 Performans Analizi

```
Test Doğruluğu: 77.5%
```

**İyi mi Kötü mü?**
- Medikal uygulamalarda %77.5 kabul edilebilir ama ideal değil
- False Negative oranı yüksek (15/40 = %37.5)
- Gerçek hastalarda yanlış negatif tehlikelidir!

**İyileştirme Önerileri:**
1. Daha fazla veri topla
2. Özellik mühendisliği yap
3. Eşik değerini optimize et
4. Ensemble metodları dene (Random Forest, XGBoost)

---

## 🎓 Öğrenme Hedefleri

✅ Lojistik regresyon nasıl çalışır
✅ Sınıflandırma problemleri nasıl çözülür
✅ Confusion matrix nasıl yorumlanır
✅ Precision, Recall, F1-Score ne demek
✅ Olasılık tahmini nasıl yapılır
✅ Özellik önem analizi nasıl yapılır
✅ Medikal veri analizi temelleri

---

## 🚀 Nasıl Çalıştırılır?

```bash
python 4_lojistikReg_diyabet.py
```

---

## 📦 Gerekli Kütüphaneler

```python
numpy
pandas
scikit-learn
```

---

## 🔍 İleri Seviye İçin

### **1. ROC Eğrisi ve AUC Skoru**
```python
from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:, 1])
roc_auc = auc(fpr, tpr)
print(f"AUC: {roc_auc:.3f}")
```

### **2. Hiperparametre Optimizasyonu**
```python
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.01, 0.1, 1, 10, 100]}
grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
```

### **3. Class Weight (Dengesiz Veri için)**
```python
model = LogisticRegression(class_weight='balanced')
```

---

## 🆚 Regresyon Karşılaştırması

| Model | Problem | Çıktı | Örnek |
|-------|---------|-------|-------|
| **Doğrusal** | Regresyon | Sürekli sayı | Fiyat: 250,000 TL |
| **Lojistik** | Sınıflandırma | Kategori (0/1) | Risk: Yüksek |

---

## 📌 Notlar

- **False Negative** medikal uygulamalarda çok kritik!
- Recall'u artırmak için eşik değeri düşürülebilir
- Model basit ama etkili (yorumlanabilir)
- Daha karmaşık modellerle (SVM, Neural Nets) performans artırılabilir

---

**Hazırlayan:** BTK Atölye - Multimedya Güvenliği
**Tarih:** 2025
**Seviye:** Orta-İleri
