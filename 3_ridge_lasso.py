# Gerekli kütüphaneleri içe aktar
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing

print("=== RIDGE VE LASSO REGRESYON KARŞILAŞTIRMASI ===")

# 1. VERİ SETİNİ YÜKLE VE HAZIRLA
# parametre: fetch_california_housing() -> California ev fiyatları veri seti
housing = fetch_california_housing()
X, y = housing.data, housing.target

# parametre: test_size=0.2 -> verinin %20'si test için
# parametre: random_state=42 -> tekrarlanabilirlik için
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print(f"Eğitim seti boyutu: {X_train.shape}")
print(f"Test seti boyutu: {X_test.shape}")

# 2. VERİYİ STANDARTLAŞTIRMA
# StandardScaler: veriyi standart normal dağılıma dönüştürür (ortalama=0, std=1)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit_transform: hem öğren hem dönüştür
X_test_scaled = scaler.transform(X_test)  # transform: öğrenileni uygula

print("\nVeri standartlaştırma tamamlandı!")

# 3. FARKLI MODELLERİ TANIMLA
models = {
    'Linear Regression': LinearRegression(),  # parametre: alpha yok - düzenlileştirme yok
    'Ridge (alpha=1.0)': Ridge(alpha=1.0),  # parametre: alpha=1.0 - L2 düzenlileştirme
    'Ridge (alpha=10.0)': Ridge(alpha=10.0),  # parametre: alpha=10.0 - daha güçlü düzenlileştirme
    'Lasso (alpha=0.1)': Lasso(alpha=0.1, max_iter=10000),  # parametre: max_iter=10000 - yakınsama için
    'Lasso (alpha=1.0)': Lasso(alpha=1.0, max_iter=10000)  # parametre: alpha=1.0 - L1 düzenlileştirme
}

# 4. MODELLERİ EĞİT VE KARŞILAŞTIR
print("\n=== MODEL KARŞILAŞTIRMASI ===")

results = []

for name, model in models.items():
    # Modeli eğit
    model.fit(X_train_scaled, y_train)

    # Tahmin yap
    y_pred = model.predict(X_test_scaled)

    # Performans metriklerini hesapla
    mse = mean_squared_error(y_test, y_pred)  # parametre: y_test (gerçek), y_pred (tahmin)
    r2 = r2_score(y_test, y_pred)  # parametre: y_test (gerçek), y_pred (tahmin)

    # Katsayı analizi
    coefficients = model.coef_
    non_zero_coef = np.sum(coefficients != 0)
    total_coef = len(coefficients)

    results.append({
        'Model': name,
        'MSE': mse,
        'R2': r2,
        'Non_Zero_Coefficients': non_zero_coef,
        'Total_Coefficients': total_coef
    })

    print(f"\n{name}:")
    print(f"  MSE: {mse:.4f}")
    print(f"  R²: {r2:.4f}")
    print(f"  Sıfır Olmayan Katsayılar: {non_zero_coef}/{total_coef}")

# 5. SONUÇLARI TABLO HALİNE GETİR
results_df = pd.DataFrame(results)
print("\n=== TÜM MODELLERİN KARŞILAŞTIRMASI ===")
print(results_df.round(4))

# 6. KATSAYILARI KARŞILAŞTIR
print("\n=== KATSAYI KARŞILAŞTIRMASI ===")

# Linear Regression katsayıları
linear_model = LinearRegression()
linear_model.fit(X_train_scaled, y_train)

# Ridge katsayıları
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train_scaled, y_train)

# Lasso katsayıları
lasso_model = Lasso(alpha=0.1, max_iter=10000)
lasso_model.fit(X_train_scaled, y_train)

# Katsayıları karşılaştır
coefficient_comparison = pd.DataFrame({
    'Özellik': housing.feature_names,
    'Linear Regression': linear_model.coef_,
    'Ridge (alpha=1.0)': ridge_model.coef_,
    'Lasso (alpha=0.1)': lasso_model.coef_
})

print("\nKatsayı Karşılaştırması:")
print(coefficient_comparison.round(4))

# 7. ALFA DEĞERİNİN ETKİSİNİ İNCELE
print("\n=== ALFA PARAMETRESİNİN ETKİSİ ===")

# Farklı alpha değerleri
alphas = [0.001, 0.01, 0.1, 1, 10, 100]

ridge_performance = []
lasso_performance = []

for alpha in alphas:
    # Ridge modeli - parametre: alpha -> düzenlileştirme gücü
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train_scaled, y_train)
    ridge_r2 = ridge.score(X_test_scaled, y_test)  # parametre: X_test, y_test -> test skoru
    ridge_non_zero = np.sum(ridge.coef_ != 0)
    ridge_performance.append({
        'Alpha': alpha,
        'R2': ridge_r2,
        'Non_Zero_Coefficients': ridge_non_zero,
        'Type': 'Ridge'
    })

    # Lasso modeli - parametre: alpha -> düzenlileştirme gücü
    lasso = Lasso(alpha=alpha, max_iter=10000)
    lasso.fit(X_train_scaled, y_train)
    lasso_r2 = lasso.score(X_test_scaled, y_test)
    lasso_non_zero = np.sum(lasso.coef_ != 0)
    lasso_performance.append({
        'Alpha': alpha,
        'R2': lasso_r2,
        'Non_Zero_Coefficients': lasso_non_zero,
        'Type': 'Lasso'
    })

# Sonuçları göster
print("\nRidge Performansı:")
ridge_df = pd.DataFrame(ridge_performance)
print(ridge_df.round(4))

print("\nLasso Performansı:")
lasso_df = pd.DataFrame(lasso_performance)
print(lasso_df.round(4))

# 8. EN İYİ MODELLERİ BUL
print("\n=== EN İYİ MODELLER ===")

# En iyi Ridge modeli
best_ridge_idx = ridge_df['R2'].idxmax()
best_ridge = ridge_df.loc[best_ridge_idx]
print(f"En iyi Ridge Modeli:")
print(f"  Alpha: {best_ridge['Alpha']}")
print(f"  R²: {best_ridge['R2']:.4f}")

# En iyi Lasso modeli
best_lasso_idx = lasso_df['R2'].idxmax()
best_lasso = lasso_df.loc[best_lasso_idx]
print(f"\nEn iyi Lasso Modeli:")
print(f"  Alpha: {best_lasso['Alpha']}")
print(f"  R²: {best_lasso['R2']:.4f}")
print(f"  Sıfır Olmayan Katsayılar: {best_lasso['Non_Zero_Coefficients']}")

# 9. LASSO İLE ÖZELLİK SEÇİMİNİ GÖSTER
print("\n=== LASSO İLE ÖZELLİK SEÇİMİ ===")

best_lasso_model = Lasso(alpha=best_lasso['Alpha'], max_iter=10000)
best_lasso_model.fit(X_train_scaled, y_train)

# Sıfır olan katsayıları bul (düzeltilmiş versiyon)
lasso_coef = best_lasso_model.coef_
feature_names = housing.feature_names

# Sıfır katsayılı özellikleri bul
zero_features = []
non_zero_features = []

for i, coef in enumerate(lasso_coef):
    if coef == 0:
        zero_features.append(feature_names[i])
    else:
        non_zero_features.append(feature_names[i])

print("Lasso Modeli Tarafından Seçilen Özellikler:")
for feature in non_zero_features:
    print(f"  ✓ {feature}")

if zero_features:
    print("\nLasso Modeli Tarafından Çıkarılan Özellikler:")
    for feature in zero_features:
        print(f"  ✗ {feature}")
else:
    print("\nLasso modeli hiç özellik çıkarmadı")

# 10. MODEL YORUMU
print("\n" + "=" * 50)
print("SONUÇ VE TAVSİYELER")
print("=" * 50)

print("\n1. RIDGE REGRESYON:")
print("   - Tüm özellikleri korur, sadece katsayıları küçültür")
print("   - Çoklu bağlantı (multicollinearity) problemlerinde iyi çalışır")
print("   - Alpha arttıkça katsayılar küçülür ama asla sıfır olmaz")

print("\n2. LASSO REGRESYON:")
print("   - Özellik seçimi yapar, gereksiz özellikleri çıkarır")
print("   - Daha basit ve yorumlanabilir modeller oluşturur")
print("   - Alpha arttıkça daha fazla özellik sıfırlanır")

print("\n3. HANGİSİNİ KULLANMALI?")
print("   - Tüm özellikler önemliyse → RIDGE")
print("   - Özellik seçimi yapmak istiyorsan → LASSO")
print("   - Alpha değerini cross-validation ile optimize et")
print("   - Veriyi mutlaka standartlaştır")

print("\n4. PRATİK ÖRNEK:")
print("   - Linear Regression: Tüm özellikler kullanılır")
print("   - Ridge: Tüm özellikler kullanılır, katsayılar küçülür")
print("   - Lasso: Önemli özellikler seçilir, diğerleri çıkarılır")

# 11. BASİT TAHMİN ÖRNEĞİ
print("\n=== TAHMİN ÖRNEĞİ ===")

# Test setinden ilk örneği al
sample_idx = 0
sample_features = X_test_scaled[sample_idx].reshape(1, -1)
actual_price = y_test[sample_idx]

# Farklı modellerle tahmin yap
linear_pred = linear_model.predict(sample_features)[0]
ridge_pred = ridge_model.predict(sample_features)[0]
lasso_pred = lasso_model.predict(sample_features)[0]

print(f"Gerçek Fiyat: {actual_price:.4f}")
print(f"Linear Regression Tahmini: {linear_pred:.4f}")
print(f"Ridge Regression Tahmini: {ridge_pred:.4f}")
print(f"Lasso Regression Tahmini: {lasso_pred:.4f}")

# Hataları hesapla
linear_error = abs(actual_price - linear_pred)
ridge_error = abs(actual_price - ridge_pred)
lasso_error = abs(actual_price - lasso_pred)

print(f"\nHatalar:")
print(f"Linear: {linear_error:.4f}")
print(f"Ridge: {ridge_error:.4f}")
print(f"Lasso: {lasso_error:.4f}")