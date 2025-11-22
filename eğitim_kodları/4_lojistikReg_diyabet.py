# Gerekli kütüphaneleri import edelim
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_diabetes
import warnings
warnings.filterwarnings('ignore')

# 1. VERİ HAZIRLAMA
# Diabetes veri setini yükleyelim
diabetes = load_diabetes()

# Özellikleri DataFrame'e dönüştürelim
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

# Hedef değişkeni ikili sınıflandırma problemine dönüştürelim
y = (diabetes.target > 150).astype(int)

print("Veri Seti Boyutu:", X.shape)
print("Sınıf Dağılımı:", np.bincount(y))  # DÜZELTİLDİ
print("0 (Negatif/Düşük Risk):", np.sum(y == 0))
print("1 (Pozitif/Yüksek Risk):", np.sum(y == 1))
print("\nİlk 5 gözlem:")
print(X.head())

# 2. VERİYİ BÖLME (TRAIN-TEST SPLIT)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nEğitim seti boyutu: {X_train.shape}")
print(f"Test seti boyutu: {X_test.shape}")
print(f"Eğitim seti sınıf dağılımı: {np.bincount(y_train)}")  # DÜZELTİLDİ
print(f"Test seti sınıf dağılımı: {np.bincount(y_test)}")     # DÜZELTİLDİ

# 3. MODEL OLUŞTURMA VE EĞİTME
model = LogisticRegression(penalty='l2', C=1.0, solver='liblinear', random_state=42, max_iter=1000)
model.fit(X_train, y_train)

print(f"\nModel eğitimi tamamlandı!")
print(f"Eğitim doğruluğu: {model.score(X_train, y_train):.3f}")

# 4. TAHMİN YAPMA
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)

print("\nTest seti için ilk 10 tahmin:")
print("Gerçek Değerler:", y_test[:10])
print("Tahminler:      ", y_pred[:10])
print("\nİlk 5 gözlem için olasılık değerleri:")
print("[[P(sınıf=0), P(sınıf=1)]]")
print(y_pred_proba[:5])

# 5. MODEL PERFORMANS METRİKLERİ
accuracy = accuracy_score(y_test, y_pred)
print(f"\nTest Doğruluğu: {accuracy:.3f}")

conf_matrix = confusion_matrix(y_test, y_pred)
print("\nKarışıklık Matrisi:")
print(conf_matrix)
print("\nKarışıklık Matrisi Açıklaması:")
print("[[True Negative  False Positive]")
print(" [False Negative True Positive ]]")

print("\nSınıflandırma Raporu:")
print(classification_report(y_test, y_pred))

# 6. MODEL KATSAYILARINI İNCELEME
feature_importance = pd.DataFrame({
    'Özellik': diabetes.feature_names,
    'Katsayı': model.coef_[0],
    'Mutlak_Değer': np.abs(model.coef_[0])
}).sort_values('Mutlak_Değer', ascending=False)

print("\nÖzellik Önem Sıralaması:")
print(feature_importance)
print(f"\nBias Terimi (intercept): {model.intercept_[0]:.3f}")

# 7. YENİ BİR HASTA İÇİN TAHMİN YAPMA
new_patient = np.array([[0.05, -0.02, 0.03, -0.01, 0.1, 0.05, -0.03, 0.02, 0.01, -0.05]])

prediction = model.predict(new_patient)
probability = model.predict_proba(new_patient)

print(f"\nYeni Hasta Tahmini:")
print(f"Tahmin Edilen Sınıf: {prediction[0]}")
print(f"Olasılık Dağılımı: {probability[0]}")
print(f"Pozitif Sınıf Olasılığı: {probability[0][1]:.3f}")

if probability[0][1] > 0.5:
    print("SONUÇ: Diyabet riski YÜKSEK")
else:
    print("SONUÇ: Diyabet riski DÜŞÜK")