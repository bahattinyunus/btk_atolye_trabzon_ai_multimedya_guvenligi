"""
Basit Doğrusal Regresyon - Tek Değişkenli İzdüşüm Örneği

Bu kod, tek bir bağımsız değişken (X) ile bağımlı değişken (y) arasındaki
ilişkiyi modelleyerek regresyonun temellerini ve izdüşüm kavramını gösterir.

Kod Ana Hatları:
1. Veri Seti Hazırlama
2. Veriyi Eğitim/Test Olarak Bölme
3. Model Oluşturma ve Eğitim
4. Tahmin Yapma
5. Model Değerlendirme
6. Görselleştirme (İzdüşüm)
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("=" * 60)
print("BASİT DOĞRUSAL REGRESYON - İZDÜŞÜM ÖRNEĞİ")
print("=" * 60)

# ============================================================================
# 1. VERİ SETİ HAZIRLAMA
# ============================================================================
print("\n[ADIM 1] VERİ SETİ HAZIRLANMASI")
print("-" * 60)

# Örnek: Çalışma saati (X) ile sınav notu (y) ilişkisi
np.random.seed(42)

# Bağımsız değişken: Çalışma saati (0-10 saat arası)
X = np.random.rand(100, 1) * 10

# Bağımlı değişken: Sınav notu
# Gerçek ilişki: y = 5 * X + 50 + gürültü
# Her 1 saat çalışma 5 puan artırır, temel not 50
y = 5 * X.squeeze() + 50 + np.random.randn(100) * 5

print(f"✓ Veri seti oluşturuldu: {X.shape[0]} örnek")
print(f"✓ Bağımsız değişken (X): Çalışma saati (0-10 saat)")
print(f"✓ Bağımlı değişken (y): Sınav notu (0-100)")
print(f"✓ Gerçek ilişki: y = 5*X + 50 + gürültü")

# ============================================================================
# 2. VERİYİ EĞİTİM VE TEST SETİNE AYIRMA
# ============================================================================
print("\n[ADIM 2] VERİ SETİNİN BÖLÜNMESI")
print("-" * 60)

# %80 eğitim, %20 test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print(f"✓ Eğitim seti: {X_train.shape[0]} örnek (%80)")
print(f"✓ Test seti: {X_test.shape[0]} örnek (%20)")
print("\nNeden bölüyoruz?")
print("  → Eğitim: Modelin öğrenmesi için")
print("  → Test: Modelin gerçek performansını ölçmek için")

# ============================================================================
# 3. MODEL OLUŞTURMA VE EĞİTİM
# ============================================================================
print("\n[ADIM 3] MODEL EĞİTİMİ")
print("-" * 60)

# Doğrusal regresyon modeli oluştur
model = LinearRegression()

# Modeli eğit - burada izdüşüm gerçekleşir!
# Model, en küçük kareler yöntemiyle w ve b değerlerini hesaplar
model.fit(X_train, y_train)

print("✓ Model eğitimi tamamlandı!")
print("\nArka planda neler oldu?")
print("  1. Model, w (ağırlık) ve b (bias) değerlerini hesapladı")
print("  2. En küçük kareler yöntemi kullanıldı")
print("  3. Veri noktaları regresyon doğrusuna izdüşüm yapıldı")

# ============================================================================
# 4. MODEL KATSAYILARI
# ============================================================================
print("\n[ADIM 4] MODEL KATSAYILARI (w ve b)")
print("-" * 60)

w = model.coef_[0]  # Ağırlık (eğim)
b = model.intercept_  # Bias (kesim noktası)

print(f"✓ Öğrenilen denklem: y = {w:.2f} * X + {b:.2f}")
print(f"\n  Ağırlık (w) = {w:.2f}")
print(f"  Bias (b) = {b:.2f}")

print("\nYORUM:")
print(f"  → Her 1 saat çalışma, notu ortalama {w:.2f} puan artırır")
print(f"  → Hiç çalışmadan alınabilecek temel not: {b:.2f}")
print(f"\n  Gerçek ilişki: y = 5.00 * X + 50.00")
print(f"  Model bulduğu: y = {w:.2f} * X + {b:.2f}")
print("  → Model gerçeğe çok yakın bir ilişki öğrendi!")

# ============================================================================
# 5. TAHMİN YAPMA
# ============================================================================
print("\n[ADIM 5] TAHMİN YAPMA")
print("-" * 60)

# Eğitim ve test setleri için tahmin yap
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

print("✓ Eğitim ve test setleri için tahminler yapıldı")
print("\nÖrnek Tahminler (Test Seti):")
print("-" * 40)
for i in range(5):
    print(f"  Çalışma: {X_test[i][0]:.1f} saat → "
          f"Gerçek: {y_test[i]:.1f}, "
          f"Tahmin: {y_test_pred[i]:.1f}")

# ============================================================================
# 6. MODEL DEĞERLENDİRME
# ============================================================================
print("\n[ADIM 6] MODEL PERFORMANSI")
print("-" * 60)

# Eğitim seti metrikleri
mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)

# Test seti metrikleri
mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

print("EĞİTİM SETİ:")
print(f"  MSE (Ortalama Kare Hata): {mse_train:.2f}")
print(f"  R² Skoru: {r2_train:.4f}")

print("\nTEST SETİ:")
print(f"  MSE (Ortalama Kare Hata): {mse_test:.2f}")
print(f"  R² Skoru: {r2_test:.4f}")

print("\nMETRİK AÇIKLAMALARI:")
print("  • MSE: Tahminlerin gerçek değerlerden sapması (düşük iyi)")
print("  • R²: Modelin açıklama gücü (0-1 arası, 1'e yakın iyi)")
print(f"\n  → Model, veri varyansının %{r2_test*100:.1f}'ini açıklıyor")

# ============================================================================
# 7. GÖRSELLEŞTİRME - İZDÜŞÜM KAVRAMI
# ============================================================================
print("\n[ADIM 7] GÖRSELLEŞTİRME")
print("-" * 60)
print("✓ İzdüşüm grafiği oluşturuluyor...")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Sol grafik: Eğitim verisi ve regresyon doğrusu
axes[0].scatter(X_train, y_train, alpha=0.6, label='Eğitim Verisi')
axes[0].plot(X_train, y_train_pred, color='red', linewidth=2, label='Regresyon Doğrusu')

# İzdüşüm çizgileri (ilk 20 nokta için)
for i in range(min(20, len(X_train))):
    axes[0].plot([X_train[i], X_train[i]],
                [y_train[i], y_train_pred[i]],
                'g--', alpha=0.3, linewidth=1)

axes[0].set_xlabel('Çalışma Saati (X)', fontsize=11)
axes[0].set_ylabel('Sınav Notu (y)', fontsize=11)
axes[0].set_title('EĞİTİM SETİ: İzdüşüm Görselleştirmesi', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Açıklama metni
axes[0].text(0.5, 0.95,
            'Yeşil çizgiler: Noktaların regresyon doğrusuna izdüşümü\n'
            'Model, bu dikmelerin karelerinin toplamını minimize eder',
            transform=axes[0].transAxes,
            fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Sağ grafik: Test verisi ve tahminler
axes[1].scatter(X_test, y_test, alpha=0.6, color='blue', label='Test Verisi (Gerçek)')
axes[1].scatter(X_test, y_test_pred, alpha=0.6, color='red', marker='x', s=100, label='Tahminler')

# Regresyon doğrusu
X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_line = model.predict(X_line)
axes[1].plot(X_line, y_line, 'r-', linewidth=2, label='Regresyon Doğrusu')

axes[1].set_xlabel('Çalışma Saati (X)', fontsize=11)
axes[1].set_ylabel('Sınav Notu (y)', fontsize=11)
axes[1].set_title(f'TEST SETİ: R² = {r2_test:.3f}', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('C:/github repolarım/btk_atolye_multimedya_güvenligi/regresyon_izdusumu_projesi/basit_regresyon_izdusumu.png', dpi=150)
plt.show()

print("✓ Grafik kaydedildi: basit_regresyon_izdusumu.png")

# ============================================================================
# 8. YENİ TAHMİN YAPMA
# ============================================================================
print("\n[ADIM 8] YENİ VERİ İÇİN TAHMİN")
print("-" * 60)

yeni_calisma_saatleri = np.array([[3], [5], [7], [9]])
yeni_tahminler = model.predict(yeni_calisma_saatleri)

print("Yeni öğrenciler için not tahminleri:")
print("-" * 40)
for saat, tahmin in zip(yeni_calisma_saatleri, yeni_tahminler):
    print(f"  {saat[0]:.0f} saat çalışma → Tahmini not: {tahmin:.1f}")

# ============================================================================
# ÖZET
# ============================================================================
print("\n" + "=" * 60)
print("PROJE ÖZETİ")
print("=" * 60)
print(f"""
✓ Model başarıyla eğitildi ve test edildi
✓ Test R² Skoru: {r2_test:.4f} (Model %{r2_test*100:.1f} açıklama gücüne sahip)
✓ Öğrenilen ilişki: y = {w:.2f} * X + {b:.2f}

İZDÜŞÜM KAVRAMI:
  • Regresyon, veri noktalarını bir doğruya "projekte eder"
  • Her noktanın doğruya olan dik mesafesi (hata) minimize edilir
  • Bu, en küçük kareler yöntemiyle gerçekleşir
  • Sonuç: Veriye en uygun doğru bulunur

ÖĞRENILENLER:
  1. Basit doğrusal regresyon nasıl çalışır
  2. İzdüşüm kavramı nedir
  3. Veri nasıl bölünür (train/test)
  4. Model nasıl değerlendirilir
  5. Katsayılar nasıl yorumlanır
""")

print("=" * 60)
print("Program tamamlandı!")
print("=" * 60)
