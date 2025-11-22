# Gerekli kütüphaneleri içe aktarıyoruz
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing

# 1. VERİ SETİNİ YÜKLEME
print("=== CALIFORNIA EV FİYATLARI VERİ SETİ ===")

# California ev fiyatları veri setini yüklüyoruz
housing = fetch_california_housing()
# parametre: data -> özellikler (bağımsız değişkenler)
X = housing.data
# parametre: target -> hedef değişken (bağımlı değişken)
y = housing.target

print(f"Veri seti boyutu: {X.shape}")  # (20640 örnek, 8 özellik)
print(f"Özellik isimleri: {housing.feature_names}")
print(f"Hedef değişken: Ev fiyatları (yüzbinlerce dolar)")

# 2. VERİYİ İNCELEME
# DataFrame oluşturarak veriyi daha kolay analiz edebiliriz
df = pd.DataFrame(X, columns=housing.feature_names)
df['Price'] = y

print("\n=== VERİ SETİNİN İLK 5 SATIRI ===")
print(df.head())

print("\n=== TEMEL İSTATİSTİKLER ===")
print(df.describe())

# 3. VERİYİ BÖLME
# Veriyi eğitim ve test setlerine ayırıyoruz
# parametre: test_size -> test setinin oranı (0.2 = %20)
# parametre: random_state -> rastgelelik için seed değeri (tekrarlanabilirlik)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print(f"\nEğitim seti boyutu: {X_train.shape}")
print(f"Test seti boyutu: {X_test.shape}")

# 4. MODEL OLUŞTURMA VE EĞİTME
print("\n=== MODEL EĞİTİMİ ===")

# LinearRegression modelini oluşturuyoruz
model = LinearRegression()

# Modeli eğitim verisi ile eğitiyoruz
# parametre: X_train -> eğitim özellikleri
# parametre: y_train -> eğitim hedef değişkeni
model.fit(X_train, y_train)

print("Model eğitimi tamamlandı!")

# 5. MODEL PARAMETRELERİ
print("\n=== MODEL PARAMETRELERİ ===")
print(f"Bias (Kesim Noktası): {model.intercept_:.4f}")

# Katsayıları inceleyelim
feature_importance = pd.DataFrame({
    'Özellik': housing.feature_names,
    'Katsayı': model.coef_
}).sort_values('Katsayı', key=abs, ascending=False)

print("\nÖzellik Önem Sıralaması:")
print(feature_importance)

# 6. TAHMİN YAPMA
print("\n=== TAHMİN YAPMA ===")

# Eğitilmiş model ile test setinde tahmin yapıyoruz
# parametre: X_test -> test özellikleri
y_pred = model.predict(X_test)

# 7. MODEL DEĞERLENDİRME
print("\n=== MODEL PERFORMANSI ===")

# Ortalama Kare Hata (MSE)
# parametre: y_test -> gerçek değerler
# parametre: y_pred -> tahmin edilen değerler
mse = mean_squared_error(y_test, y_pred)

# Kök Ortalama Kare Hata (RMSE)
rmse = np.sqrt(mse)

# R² Skoru - Açıklanan varyans oranı
r2 = r2_score(y_test, y_pred)

print(f"Ortalama Kare Hata (MSE): {mse:.4f}")
print(f"Kök Ortalama Kare Hata (RMSE): {rmse:.4f}")
print(f"R² Skoru: {r2:.4f}")

# 8. ÖRNEK TAHMİN
print("\n=== ÖRNEK TAHMİN ===")

# Test setinden ilk örneği seçelim
sample_idx = 0
sample_features = X_test[sample_idx].reshape(1, -1)
actual_price = y_test[sample_idx]
predicted_price = model.predict(sample_features)[0]

print("Örnek Ev Özellikleri:")
for i, feature_name in enumerate(housing.feature_names):
    print(f"  {feature_name}: {sample_features[0][i]:.2f}")

print(f"\nGerçek Fiyat: {actual_price:.2f}")
print(f"Tahmin Edilen Fiyat: {predicted_price:.2f}")
print(f"Hata: {abs(actual_price - predicted_price):.4f}")

# 9. MODEL YORUMU
print("\n=== SONUÇLAR ===")
print(f"Model, ev fiyatlarındaki değişimin %{r2 * 100:.1f}'ini açıklıyor.")
print("En önemli özellikler:")
print("1. MedInc (Medyan Gelir) - Gelir arttıkça fiyat artıyor")
print("2. AveRooms (Oda Sayısı) - Daha büyük evler daha pahalı")
print("3. Latitude (Enlem) - Konum fiyatı etkiliyor")

# 10. BASİT BİR TAHMİN FONKSİYONU
print("\n=== TAHMİN FONKSİYONU ===")


def ev_fiyati_tahmin_et(model, ornek_ozellikler):
    """
    Verilen özelliklere göre ev fiyatı tahmini yapar

    Parameters:
    model: Eğitilmiş doğrusal regresyon modeli
    ornek_ozellikler: 8 özellikten oluşan liste [MedInc, HouseAge, AveRooms, ...]

    Returns:
    tahmin: Tahmin edilen ev fiyatı
    """
    tahmin = model.predict([ornek_ozellikler])[0]
    return tahmin


# Örnek kullanım
ornek_ev = [3.0, 25.0, 5.0, 1500.0, 500.0, 2.0, 35.0, -120.0]
tahmin = ev_fiyati_tahmin_et(model, ornek_ev)
print(f"Örnek ev için tahmin edilen fiyat: {tahmin:.2f}")