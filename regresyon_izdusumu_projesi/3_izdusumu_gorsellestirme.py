"""
İzdüşüm Kavramı - İnteraktif 3D Görselleştirme

Bu kod, regresyonda izdüşüm kavramını 3D uzayda görselleştirir.
İki bağımsız değişken (X1, X2) ve bir bağımlı değişken (y) kullanarak
regresyon düzlemini ve veri noktalarının bu düzleme izdüşümünü gösterir.

Amaç:
  - İzdüşüm kavramını geometrik olarak anlamak
  - Regresyon düzlemini 3D'de görmek
  - Hata vektörlerini (residuals) görselleştirmek
  - En küçük kareler yöntemini anlamak
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

print("=" * 70)
print("REGRESYON İZDÜŞÜMÜ - 3D GÖRSELLEŞTİRME")
print("=" * 70)

# ============================================================================
# 1. VERİ SETİ OLUŞTURMA
# ============================================================================
print("\n[ADIM 1] 3D VERİ SETİ OLUŞTURMA")
print("-" * 70)

np.random.seed(42)
n_samples = 50

# İki bağımsız değişken
X1 = np.random.uniform(0, 10, n_samples)
X2 = np.random.uniform(0, 10, n_samples)

# Bağımlı değişken: Gerçek ilişki + gürültü
# y = 3*X1 + 2*X2 + 5 + gürültü
y = 3 * X1 + 2 * X2 + 5 + np.random.normal(0, 2, n_samples)

# Özellik matrisi
X = np.column_stack([X1, X2])

print(f"✓ {n_samples} adet 3D veri noktası oluşturuldu")
print("✓ Gerçek ilişki: y = 3*X1 + 2*X2 + 5 + gürültü")
print(f"✓ X1 aralığı: [{X1.min():.1f}, {X1.max():.1f}]")
print(f"✓ X2 aralığı: [{X2.min():.1f}, {X2.max():.1f}]")
print(f"✓ y aralığı: [{y.min():.1f}, {y.max():.1f}]")

# ============================================================================
# 2. MODEL EĞİTİMİ
# ============================================================================
print("\n[ADIM 2] REGRESYON MODELİ EĞİTİMİ")
print("-" * 70)

model = LinearRegression()
model.fit(X, y)

w1, w2 = model.coef_
b = model.intercept_

print("✓ Model eğitimi tamamlandı!")
print(f"\nÖğrenilen Denklem:")
print(f"  y = {w1:.2f}*X1 + {w2:.2f}*X2 + {b:.2f}")
print(f"\nGerçek Denklem:")
print(f"  y = 3.00*X1 + 2.00*X2 + 5.00")
print("\n→ Model, gerçek ilişkiye çok yakın bir düzlem buldu!")

# Tahminler
y_pred = model.predict(X)

# Hata metrikleri
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"\nPerformans:")
print(f"  • MSE: {mse:.2f}")
print(f"  • R² Skoru: {r2:.4f}")

# ============================================================================
# 3. REGRESYON DÜZLEMİNİ OLUŞTURMA
# ============================================================================
print("\n[ADIM 3] REGRESYON DÜZLEMİNİ OLUŞTURMA")
print("-" * 70)

# Düzlem için grid oluştur
x1_range = np.linspace(X1.min(), X1.max(), 20)
x2_range = np.linspace(X2.min(), X2.max(), 20)
x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)

# Her grid noktası için tahmin yap
X_grid = np.column_stack([x1_grid.ravel(), x2_grid.ravel()])
y_grid = model.predict(X_grid).reshape(x1_grid.shape)

print("✓ Regresyon düzlemi oluşturuldu")
print(f"✓ Düzlem grid boyutu: {x1_grid.shape}")

# ============================================================================
# 4. 3D GÖRSELLEŞTİRME - İZDÜŞÜM
# ============================================================================
print("\n[ADIM 4] 3D GÖRSELLEŞTİRME")
print("-" * 70)

# Figür 1: Regresyon düzlemi ve veri noktaları
fig = plt.figure(figsize=(16, 6))

# Sol grafik: Regresyon düzlemi + veri noktaları
ax1 = fig.add_subplot(121, projection='3d')

# Regresyon düzlemini çiz
surface = ax1.plot_surface(x1_grid, x2_grid, y_grid,
                           alpha=0.3, cmap='viridis',
                           edgecolor='none')

# Gerçek veri noktaları
ax1.scatter(X1, X2, y, c='red', marker='o', s=50, alpha=0.8,
           label='Gerçek Veri Noktaları')

# Tahmin edilen noktalar (düzlem üzerinde)
ax1.scatter(X1, X2, y_pred, c='blue', marker='x', s=50, alpha=0.6,
           label='Düzlem Üzerindeki Tahminler')

ax1.set_xlabel('X1', fontsize=11)
ax1.set_ylabel('X2', fontsize=11)
ax1.set_zlabel('y', fontsize=11)
ax1.set_title('Regresyon Düzlemi ve Veri Noktaları', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left')
ax1.view_init(elev=20, azim=45)

# Sağ grafik: İzdüşüm vektörleri
ax2 = fig.add_subplot(122, projection='3d')

# Regresyon düzlemi
ax2.plot_surface(x1_grid, x2_grid, y_grid,
                alpha=0.2, cmap='viridis',
                edgecolor='none')

# Veri noktaları
ax2.scatter(X1, X2, y, c='red', marker='o', s=50, alpha=0.8,
           label='Gerçek Veri')

# İzdüşüm çizgileri (ilk 30 nokta için görsel karmaşayı önlemek)
n_show = min(30, n_samples)
for i in range(n_show):
    ax2.plot([X1[i], X1[i]], [X2[i], X2[i]], [y[i], y_pred[i]],
            'g--', linewidth=1, alpha=0.5)

# Tahminler
ax2.scatter(X1[:n_show], X2[:n_show], y_pred[:n_show],
           c='blue', marker='x', s=50, alpha=0.6,
           label='Düzlem Üzerindeki İzdüşümler')

ax2.set_xlabel('X1', fontsize=11)
ax2.set_ylabel('X2', fontsize=11)
ax2.set_zlabel('y', fontsize=11)
ax2.set_title('İzdüşüm Vektörleri (Residuals)', fontsize=12, fontweight='bold')
ax2.legend(loc='upper left')
ax2.view_init(elev=20, azim=45)

# Açıklama metni
fig.text(0.5, 0.02,
        'Yeşil kesikli çizgiler: Veri noktalarının düzleme dik izdüşümleri\n'
        'Regresyon, bu çizgilerin karelerinin toplamını minimize eder (En Küçük Kareler Yöntemi)',
        ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('C:/github repolarım/btk_atolye_multimedya_güvenligi/regresyon_izdusumu_projesi/3d_regresyon_izdusumu.png', dpi=150)
plt.show()

print("✓ 3D görselleştirme kaydedildi: 3d_regresyon_izdusumu.png")

# ============================================================================
# 5. HATA ANALİZİ
# ============================================================================
print("\n[ADIM 5] HATA ANALİZİ (RESIDUALS)")
print("-" * 70)

# Hata vektörleri (residuals)
residuals = y - y_pred

print(f"Hata İstatistikleri:")
print(f"  • Ortalama Hata: {np.mean(residuals):.4f}")
print(f"  • Standart Sapma: {np.std(residuals):.4f}")
print(f"  • Min Hata: {np.min(residuals):.4f}")
print(f"  • Max Hata: {np.max(residuals):.4f}")

# Hata dağılımı grafiği
fig, axes = plt.subplots(1, 2, figoia=(14, 5))

# Hata histogramı
axes[0].hist(residuals, bins=20, edgecolor='black', alpha=0.7)
axes[0].axvline(x=0, color='red', linestyle='--', linewidth=2, label='Sıfır Hata')
axes[0].set_xlabel('Hata (y_gerçek - y_tahmin)', fontsize=11)
axes[0].set_ylabel('Frekans', fontsize=11)
axes[0].set_title('Hata Dağılımı', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Hata vs Tahmin
axes[1].scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.5)
axes[1].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[1].set_xlabel('Tahmin Edilen Değer', fontsize=11)
axes[1].set_ylabel('Hata (Residual)', fontsize=11)
axes[1].set_title('Residual Plot', fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('C:/github repolarım/btk_atolye_multimedya_güvenligi/regresyon_izdusumu_projesi/hata_analizi.png', dpi=150)
plt.show()

print("✓ Hata analizi grafiği kaydedildi: hata_analizi.png")

# ============================================================================
# 6. MATEMATİKSEL AÇIKLAMA
# ============================================================================
print("\n[ADIM 6] MATEMATİKSEL İZDÜŞÜM AÇIKLAMASI")
print("-" * 70)

print("""
REGRESYONDA İZDÜŞÜM KAVRAMI:

1. PROBLEM:
   • n adet veri noktamız var: (x₁ᵢ, x₂ᵢ, yᵢ)
   • Bu noktalar 3 boyutlu uzayda dağılmış durumda
   • Amacımız: Bu noktaları en iyi temsil eden düzlemi bulmak

2. ÇÖZÜM - EN KÜÇÜK KARELER YÖNTEMİ:
   • Minimize et: Σ(yᵢ - ŷᵢ)²
   • ŷᵢ = w₁·x₁ᵢ + w₂·x₂ᵢ + b  (düzlem denklemi)

3. GEOMETRİK ANLAM (İZDÜŞÜM):
   • Her veri noktası (x₁ᵢ, x₂ᵢ, yᵢ), düzleme DİK olarak projeksiyon edilir
   • Projeksiyon noktası: (x₁ᵢ, x₂ᵢ, ŷᵢ)
   • Hata vektörü: eᵢ = yᵢ - ŷᵢ  (dikey mesafe)

4. OPTİMİZASYON:
   • Tüm dikey mesafelerin karelerinin toplamını minimize et
   • Bu, veri noktalarının düzleme "en yakın" olmasını sağlar
   • Sonuç: Optimal w₁, w₂, b değerleri bulunur

5. SONUÇ:
   • Bulunan düzlem, veri bulutuna "en iyi uyan" düzlemdir
   • Her nokta, bu düzleme matematiksel olarak projekte edilmiştir
   • Bu işlem LINEAR REGRESSION'dur!
""")

print(f"\nBU ÖRNEKTE:")
print(f"  • {n_samples} veri noktası 3D uzayda dağılmış")
print(f"  • Model, en iyi düzlemi buldu: y = {w1:.2f}*X1 + {w2:.2f}*X2 + {b:.2f}")
print(f"  • Her nokta, bu düzleme dikey olarak projekte edildi")
print(f"  • Toplam kare hata minimize edildi: MSE = {mse:.2f}")
print(f"  • Model başarısı: R² = {r2:.4f} (%{r2*100:.1f} açıklama gücü)")

# ============================================================================
# 7. İNTERAKTİF AÇIKLAAMA
# ============================================================================
print("\n[ADIM 7] İNTERAKTİF GÖRSELLEŞTIRME")
print("-" * 70)

# Farklı açılardan görünümler
fig = plt.figure(figsize=(15, 5))

views = [(20, 45), (20, 135), (60, 45)]
titles = ['Görünüm 1: 45°', 'Görünüm 2: 135°', 'Görünüm 3: Yukarıdan']

for i, (elev, azim) in enumerate(views):
    ax = fig.add_subplot(1, 3, i+1, projection='3d')

    # Düzlem
    ax.plot_surface(x1_grid, x2_grid, y_grid,
                   alpha=0.3, cmap='viridis')

    # Veri noktaları
    ax.scatter(X1, X2, y, c='red', marker='o', s=30, alpha=0.8)

    # İzdüşüm çizgileri (10 nokta)
    for j in range(10):
        ax.plot([X1[j], X1[j]], [X2[j], X2[j]], [y[j], y_pred[j]],
               'g--', linewidth=1, alpha=0.5)

    ax.set_xlabel('X1', fontsize=9)
    ax.set_ylabel('X2', fontsize=9)
    ax.set_zlabel('y', fontsize=9)
    ax.set_title(titles[i], fontsize=11, fontweight='bold')
    ax.view_init(elev=elev, azim=azim)

plt.tight_layout()
plt.savefig('C:/github repolarım/btk_atolye_multimedya_güvenligi/regresyon_izdusumu_projesi/farkli_acılar.png', dpi=150)
plt.show()

print("✓ Farklı açılardan görünümler kaydedildi: farkli_acılar.png")

# ============================================================================
# ÖZET
# ============================================================================
print("\n" + "=" * 70)
print("PROJE ÖZETİ - İZDÜŞÜM GÖRSELLEŞTİRMESİ")
print("=" * 70)
print(f"""
✓ 3D regresyon düzlemi başarıyla görselleştirildi
✓ İzdüşüm vektörleri (residuals) gösterildi
✓ Model Performansı: R² = {r2:.4f}, MSE = {mse:.2f}

İZDÜŞÜM KAVRAMI - ÖZET:
  • Regresyon = Veri noktalarını bir düzleme projekte etme
  • Her nokta, düzleme EN KISA MESAFEDE (dik) izdüşüm yapar
  • Hata vektörleri (yeşil çizgiler) bu dikey mesafeleri gösterir
  • En küçük kareler: Σ(dikey mesafe)² minimize edilir
  • Sonuç: Veriye en uygun düzlem bulunur

GÖRSELLEŞTİRİLEN KAVRAMLAR:
  1. Regresyon düzlemi (mavi yüzey)
  2. Gerçek veri noktaları (kırmızı)
  3. İzdüşüm noktaları (mavi X)
  4. Hata vektörleri (yeşil kesikli çizgiler)
  5. Farklı açılardan görünümler

ÖĞRENILENLER:
  1. İzdüşüm kavramının geometrik anlamı
  2. Regresyon düzlemi nasıl oluşur
  3. En küçük kareler yönteminin görsel karşılığı
  4. 3D veri görselleştirme teknikleri
  5. Residual analizi
""")

print("=" * 70)
print("Program tamamlandı! Tüm görseller kaydedildi.")
print("=" * 70)
