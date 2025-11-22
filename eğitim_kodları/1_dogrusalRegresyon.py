# Gerekli kütüphaneleri içe aktarıyoruz
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. VERİ SETİ HAZIRLAMA
# Örnek bir veri seti oluşturuyoruz. Gerçek bir veri seti de kullanabiliriz.
# Bu örnekte, bir evin metrekaresi (X) ile fiyatı (y) arasındaki ilişkiyi modellediğimizi varsayalım.

# Rastgele sayı üretecini sabitliyoruz ki sonuçlar her seferinde aynı olsun
np.random.seed(42)
# 0 ile 100 arasında 100 rastgele sayı (metrekare) oluşturuyoruz
X = np.random.rand(100, 1) * 100
# Hedef değişkeni (fiyat) oluşturuyoruz: y = 3 * X + 10 + gürültü
# Burada gerçek ilişkinin y = 3*X + 10 olduğunu biliyoruz. Gürültü ekleyerek gerçekçi yapıyoruz.
y = 3 * X.squeeze() + 10 #+ np.random.randn(100) * 30

# 2. VERİYİ GÖRSELLEŞTİRME
# Veriye bir göz atalım
plt.scatter(X, y, alpha=0.7)
plt.xlabel('Metrekare (m²)')
plt.ylabel('Fiyat (Bin TL)')
plt.title('Ev Fiyatları vs Metrekare')
plt.show()
# GÖRSELLEŞTİRME GEREKÇESİ: Verinin dağılımını anlamak ve doğrusal ilişki olup olmadığını görmek için

# 3. VERİYİ EĞİTİM VE TEST SETİNE AYIRMA
# Verinin %80'ini eğitim, %20'sini test için ayırıyoruz
# random_state parametresi, her seferinde aynı bölme işleminin yapılmasını sağlar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# BÖLME GEREKÇESİ: Modelin gerçek performansını, görmediği veriler üzerinde değerlendirmek için

# 4. MODELİ OLUŞTURMA VE EĞİTME
# Doğrusal Regresyon modelini oluşturuyoruz
model = LinearRegression()
# Modeli eğitim verisi ile eğitiyoruz
# Model, X_train ve y_train arasındaki ilişkiyi öğrenir
model.fit(X_train, y_train)
# EĞİTİM GEREKÇESİ: Modelin verideki kalıbı (pattern) öğrenmesi için

# 5. MODEL KATSAYILARINI GÖRME
# Modelin bulduğu katsayıları (w ve b) yazdırıyoruz
print(f"Ağırlık (w): {model.coef_[0]:.2f}")
print(f"Bias (b): {model.intercept_:.2f}")
# KATSAYI GÖRME GEREKÇESİ: Modelin nasıl bir ilişki öğrendiğini anlamak için

# 6. TAHMİN YAPMA
# Eğitilmiş modeli kullanarak test seti üzerinde tahmin yapıyoruz
y_pred = model.predict(X_test)
# TAHMİN GEREKÇESİ: Modelin performansını değerlendirmek için

# 7. MODEL PERFORMANSINI DEĞERLENDİRME
# Test seti üzerindeki performansı değerlendirmek için metrikler kullanıyoruz

# Ortalama Kare Hata (MSE): Tahminlerin gerçek değerlerden ne kadar saptığını gösterir
mse = mean_squared_error(y_test, y_pred)
print(f"Ortalama Kare Hata (MSE): {mse:.2f}")

# R² Skoru: Modelin veriye ne kadar iyi uyduğunu gösterir (0-1 arası, 1'e yakın iyi)
r2 = r2_score(y_test, y_pred)
print(f"R² Skoru: {r2:.2f}")
# DEĞERLENDİRME GEREKÇESİ: Modelin kalitesini objektif olarak ölçmek için

# 8. SONUÇLARI GÖRSELLEŞTİRME
# Test seti ve tahminleri görselleştirelim

# Önce gerçek test verilerini scatter ile çizdiriyoruz
plt.scatter(X_test, y_test, color='blue', label='Gerçek Veri')
# Modelin tahmin ettiği doğruyu çizdiriyoruz
# Doğruyu çizmek için X_test'i sıralayıp tahminleri alıyoruz
sorted_indices = np.argsort(X_test.squeeze())
X_test_sorted = X_test[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]
plt.plot(X_test_sorted, y_pred_sorted, color='red', linewidth=2, label='Doğrusal Regresyon')

plt.xlabel('Metrekare (m²)')
plt.ylabel('Fiyat (Bin TL)')
plt.title('Doğrusal Regresyon: Tahmin vs Gerçek')
plt.legend()
plt.show()
# GÖRSELLEŞTİRME GEREKÇESİ: Modelin performansını görsel olarak değerlendirmek için