# 5_kararAgaci_iris.py - Karar Ağaçları (Decision Tree - Iris)

## 📖 Kod Açıklaması

Bu kod, **karar ağaçları** (decision trees) algoritmasını kullanarak çiçek türlerini sınıflandırır. Karar ağaçları, "if-then-else" kurallarıyla çalışan, yorumlanması kolay bir makine öğrenmesi yöntemidir.

---

## 🎯 Amaç

**Iris çiçeği veri seti** kullanarak, çiçeğin fiziksel özelliklerine bakarak **türünü** tahmin etmek.

**Problem Tipi:** Çoklu Sınıflandırma (Multi-class Classification)
- **3 Sınıf:**
  - Setosa
  - Versicolor
  - Virginica

---

## 🌳 Karar Ağacı Nedir?

**Görsel Yapı:**
```
                [Petal Length <= 2.5?]
                /                    \
            YES/                      \NO
            /                          \
      [SETOSA]                  [Petal Width <= 1.7?]
                                /                    \
                            YES/                      \NO
                            /                          \
                    [VERSICOLOR]                  [VIRGINICA]
```

**Çalışma Prensibi:**
1. Kök düğümden başla
2. Her düğümde bir özelliği test et
3. Sonuca göre sola/sağa ilerle
4. Yaprak düğüme ulaş → Tahmin yap

---

## 📊 Kod İçeriği ve Adımlar

### 1. **Veri Seti Hazırlama**
```python
iris = load_iris()
X = iris.data    # 4 özellik
y = iris.target  # 3 sınıf
```

**4 Özellik:**
1. **sepal length** (cm) - Çanak yaprağı uzunluğu
2. **sepal width** (cm) - Çanak yaprağı genişliği
3. **petal length** (cm) - Taç yaprağı uzunluğu
4. **petal width** (cm) - Taç yaprağı genişliği

**3 Sınıf:**
- 0: Setosa (50 örnek)
- 1: Versicolor (50 örnek)
- 2: Virginica (50 örnek)

Dengeli veri seti!

### 2. **Veri Bölme**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
```

- Eğitim: 120 örnek (%80)
- Test: 30 örnek (%20)
- Her sınıftan 10'ar örnek test setinde

### 3. **Model Oluşturma ve Eğitim**
```python
model = DecisionTreeClassifier(
    criterion='entropy',    # Bilgi kazancı (Information Gain)
    max_depth=3,            # Maksimum derinlik
    random_state=42
)
model.fit(X_train, y_train)
```

**Parametreler:**
- **criterion:** Bölme kriteri
  - `'gini'`: Gini safsızlığı (varsayılan)
  - `'entropy'`: Bilgi kazancı
- **max_depth:** Ağacın maksimum derinliği (overfitting kontrolü)
- **min_samples_split:** Bölme için minimum örnek sayısı
- **min_samples_leaf:** Yaprak için minimum örnek sayısı

### 4. **Model Performansı**
```python
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Doğruluğu: {accuracy:.3f}")
```

**Çıktı:**
```
Eğitim Doğruluğu: 0.983 (%98.3)
Test Doğruluğu: 0.967 (%96.7)
```

Mükemmel performans! Overfitting yok (eğitim ve test skorları yakın).

### 5. **Karmaşıklık Matrisi**
```python
confusion = confusion_matrix(y_test, y_pred)
```

**Çıktı:**
```
[[10  0  0]   # Setosa: 10/10 doğru ✓
 [ 0  9  1]   # Versicolor: 9/10 doğru (1 Virginica ile karıştı)
 [ 0  0 10]]  # Virginica: 10/10 doğru ✓
```

**Yorumlama:**
- Setosa mükemmel ayrılıyor (kolay sınıf)
- 1 Versicolor örneği Virginica olarak yanlış sınıflandırıldı
- Genel başarı: 29/30 = %96.7

### 6. **Sınıflandırma Raporu**
```python
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

**Çıktı:**
```
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        10
  versicolor       1.00      0.90      0.95        10
   virginica       0.91      1.00      0.95        10

    accuracy                           0.97        30
```

**Metrik Analizi:**
- **Setosa:** Mükemmel (1.00 her metrikte)
- **Versicolor:** Recall düşük (0.90) → 1 örnek kaçırıldı
- **Virginica:** Precision düşük (0.91) → 1 yanlış pozitif

### 7. **Özellik Önem Sıralaması**
```python
feature_importance = pd.DataFrame({
    'Özellik': iris.feature_names,
    'Önem': model.feature_importances_
}).sort_values('Önem', ascending=False)
```

**Çıktı:**
```
             Özellik      Önem
  petal length (cm)  0.579077   # EN ÖNEMLİ
   petal width (cm)  0.420923
  sepal length (cm)  0.000000   # Kullanılmadı
   sepal width (cm)  0.000000   # Kullanılmadı
```

**Yorumlama:**
- Model, sadece **taç yaprağı** özelliklerini kullandı
- Çanak yaprağı özellikleri sınıflandırma için gereksiz
- Petal length en ayırt edici özellik

### 8. **Parametre Karşılaştırması**
Kod, farklı parametrelerle 4 model eğitir:

**Çıktı:**
```
1. Sığ ağaç (Gini):
   Eğitim: 0.967, Test: 0.933, Düğüm: 5

2. Orta derinlik (Gini):
   Eğitim: 1.000, Test: 0.933, Düğüm: 15

3. Orta derinlik (Entropi):
   Eğitim: 0.983, Test: 0.967, Düğüm: 9

4. Sınırsız derinlik (Entropi):
   Eğitim: 1.000, Test: 0.933, Düğüm: 15
```

**Gözlem:**
- Model 3 (max_depth=3, entropy) **en dengeli**
- Derin ağaçlar (model 2, 4) overfitting yaşıyor
- Sığ ağaç (model 1) underfitting

### 9. **Overfitting Analizi**
```python
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
difference = abs(train_accuracy - test_accuracy)
```

**Çıktı:**
```
Eğitim Doğruluğu: 0.983
Test Doğruluğu: 0.967
Performans Farkı: 0.017 (iyi!)
```

**Değerlendirme:**
- Fark < 0.05 → Model iyi genelleme yapıyor ✓
- Fark > 0.10 → Overfitting var ✗

### 10. **Çapraz Doğrulama**
```python
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"Ortalama: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")
```

**Çıktı:**
```
Skorlar: [0.967, 0.967, 0.933, 1.000, 1.000]
Ortalama: 0.973 (+/- 0.050)
```

5-fold çapraz doğrulama ile model tutarlılığı test edildi.

### 11. **Model Detayları**
```python
print(f"Ağaç derinliği: {model.get_depth()}")
print(f"Yaprak sayısı: {model.get_n_leaves()}")
```

**Çıktı:**
```
Ağaç derinliği: 3
Yaprak sayısı: 5
Toplam düğüm sayısı: 9
```

---

## 🔑 Önemli Kavramlar

### **1. Gini Safsızlığı (Gini Impurity)**
```
Gini = 1 - Σ(pᵢ²)
```

- pᵢ: i sınıfının oranı
- 0: Saf düğüm (tek sınıf)
- 0.5: Maksimum karışıklık (iki sınıf eşit)

**Örnek:**
```
Düğümde: 40 setosa, 0 versicolor, 0 virginica
Gini = 1 - (1² + 0² + 0²) = 0 → SAF!
```

### **2. Entropi ve Bilgi Kazancı**
```
Entropy = -Σ(pᵢ * log₂(pᵢ))
```

- Düzensizlik ölçüsü
- 0: Saf düğüm
- log₂(n): Maksimum entropi

**Bilgi Kazancı (Information Gain):**
```
IG = Entropy(parent) - Σ(weighted_entropy(children))
```

Model, en yüksek bilgi kazancını sağlayan özelliği seçer.

### **3. Overfitting Kontrolü**

**Budama (Pruning) Teknikleri:**
- **Pre-pruning:** Eğitim sırasında
  - `max_depth`: Derinlik sınırı
  - `min_samples_split`: Bölme için min örnek
  - `min_samples_leaf`: Yaprak için min örnek

- **Post-pruning:** Eğitim sonrası
  - `cost_complexity_pruning_path()` ile

---

## 📈 Performans Analizi

```
Test Doğruluğu: %96.7
Çapraz Doğrulama: %97.3 (±5%)
```

**Mükemmel Performans Nedenleri:**
1. Veri seti küçük ve temiz
2. Sınıflar iyi ayrılmış (özellikle Setosa)
3. Özellikler ayırt edici
4. Model karmaşıklığı uygun (max_depth=3)

---

## 🎓 Öğrenme Hedefleri

✅ Karar ağaçları nasıl çalışır
✅ Gini ve Entropi kriterleri
✅ Özellik önem analizi
✅ Overfitting nasıl kontrol edilir
✅ Hiperparametre etkisi
✅ Çapraz doğrulama neden önemli
✅ Confusion matrix detaylı yorumlama

---

## 🚀 Nasıl Çalıştırılır?

```bash
python 5_kararAgaci_iris.py
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

### **1. Ağaç Görselleştirme**
```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(model,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          filled=True,
          rounded=True)
plt.show()
```

### **2. Random Forest (Ensemble)**
```python
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
# Genellikle daha yüksek performans
```

### **3. Özellik Seçimi**
```python
from sklearn.feature_selection import SelectKBest, chi2

selector = SelectKBest(chi2, k=2)  # En iyi 2 özelliği seç
X_new = selector.fit_transform(X, y)
```

### **4. Hiperparametre Optimizasyonu**
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [2, 3, 4, 5],
    'criterion': ['gini', 'entropy'],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
print(f"En iyi parametreler: {grid_search.best_params_}")
```

---

## ⚖️ Avantajlar vs Dezavantajlar

### **AVANTAJLARI:**
✅ Yorumlanması kolay (beyaz kutu)
✅ Veri ön işleme gerektirmez
✅ Hem sayısal hem kategorik veri
✅ Doğrusal olmayan ilişkileri yakalar
✅ Özellik önem analizi built-in

### **DEZAVANTAJLARI:**
❌ Overfitting'e eğilimli
❌ Küçük veri değişikliğine hassas
❌ Dengesiz veride bias
❌ Eğik karar sınırlarında zayıf

---

## 🆚 Diğer Algoritmalarla Karşılaştırma

| Algoritma | Doğruluk | Yorumlanabilirlik | Hız |
|-----------|----------|-------------------|-----|
| **Karar Ağacı** | %96.7 | ⭐⭐⭐⭐⭐ | Hızlı |
| Lojistik Reg. | ~%95 | ⭐⭐⭐⭐ | Çok Hızlı |
| Random Forest | ~%98 | ⭐⭐ | Orta |
| Neural Network | ~%98 | ⭐ | Yavaş |

---

## 📌 Notlar

- Iris veri seti ML'in "Hello World"u
- Gerçek uygulamalarda Random Forest tercih edilir
- Ağaç görselleştirmesi öğretim için çok değerli
- Medikal/yasal alanlarda yorumlanabilirlik kritik

---

## 🔗 İlgili Konular

- **Random Forest:** Çoklu karar ağacı ensemble'ı
- **Gradient Boosting:** XGBoost, LightGBM
- **CART:** Classification and Regression Trees

---

**Hazırlayan:** BTK Atölye - Multimedya Güvenliği
**Tarih:** 2025
**Seviye:** Orta
