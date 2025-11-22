"""
Çoklu Doğrusal Regresyon - Çok Değişkenli İzdüşüm Örneği

Bu kod, birden fazla bağımsız değişken kullanarak bağımlı değişkeni tahmin eder.
Çok boyutlu uzayda izdüşüm kavramını gösterir.

Örnek Senaryo: Ev fiyatı tahmini
  - Bağımsız değişkenler: Metrekare, oda sayısı, yaş, mesafe
  - Bağımlı değişken: Fiyat

Kod Ana Hatları:
1. Sentetik veri seti oluşturma
2. Özellik mühendisliği ve keşif
3. Veriyi bölme
4. Model eğitimi
5. Özellik önem analizi
6. Model değerlendirme
7. Çok boyutlu görselleştirme
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from mpl_toolkits.mplot3d import Axes3D

print("=" * 70)
print("ÇOKLU DOĞRUSAL REGRESYON - ÇOK BOYUTLU İZDÜŞÜM")
print("=" * 70)

# ============================================================================
# 1. SENTETİK VERİ SETİ OLUŞTURMA
# ============================================================================
print("\n[ADIM 1] SENTETİK VERİ SETİ OLUŞTURMA")
print("-" * 70)

np.random.seed(42)
n_samples = 200

# Bağımsız değişkenler (özellikler)
metrekare = np.random.uniform(50, 200, n_samples)  # 50-200 m²
oda_sayisi = np.random.randint(1, 6, n_samples)    # 1-5 oda
ev_yasi = np.random.uniform(0, 30, n_samples)      # 0-30 yıl
merkeze_mesafe = np.random.uniform(1, 30, n_samples)  # 1-30 km

# Bağımlı değişken: Fiyat (gerçek ilişki)
# Fiyat = 2000*metrekare + 50000*oda + 1000*yaş - 5000*mesafe + 100000 + gürültü
fiyat = (2000 * metrekare +
         50000 * oda_sayisi -
         1000 * ev_yasi -
         5000 * merkeze_mesafe +
         100000 +
         np.random.normal(0, 50000, n_samples))  # Gürültü

# DataFrame oluştur
df = pd.DataFrame({
    'Metrekare': metrekare,
    'Oda_Sayisi': oda_sayisi,
    'Ev_Yasi': ev_yasi,
    'Merkeze_Mesafe': merkeze_mesafe,
    'Fiyat': fiyat
})

print(f"✓ Veri seti oluşturuldu: {n_samples} ev örneği")
print("\nÖZELLİKLER:")
print("  • Metrekare: Evin büyüklüğü (50-200 m²)")
print("  • Oda Sayısı: Oda adedi (1-5)")
print("  • Ev Yaşı: Evin yaşı (0-30 yıl)")
print("  • Merkeze Mesafe: Şehir merkezine uzaklık (1-30 km)")
print("  • Fiyat (HEDEF): Ev fiyatı (TL)")

print("\nGERÇEK İLİŞKİ:")
print("  Fiyat = 2000*Metrekare + 50000*Oda - 1000*Yaş - 5000*Mesafe + 100000")

print("\nİlk 5 örnek:")
print(df.head())

# ============================================================================
# 2. KEŞİFSEL VERİ ANALİZİ (EDA)
# ============================================================================
print("\n[ADIM 2] KEŞİFSEL VERİ ANALİZİ")
print("-" * 70)

print("\nTemel İstatistikler:")
print(df.describe())

print("\nKorelasyon Matrisi:")
print(df.corr()['Fiyat'].sort_values(ascending=False))

# Korelasyon matrisi görselleştirmesi
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Özellikler Arası Korelasyon Matrisi', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('C:/github repolarım/btk_atolye_multimedya_güvenligi/regresyon_izdusumu_projesi/korelasyon_matrisi.png', dpi=150)
plt.show()

print("✓ Korelasyon matrisi kaydedildi: korelasyon_matrisi.png")

# ============================================================================
# 3. VERİYİ BÖLME
# ============================================================================
print("\n[ADIM 3] VERİYİ EĞİTİM VE TEST SETİNE AYIRMA")
print("-" * 70)

X = df.drop('Fiyat', axis=1)  # Bağımsız değişkenler
y = df['Fiyat']                # Bağımlı değişken

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print(f"✓ Eğitim seti: {X_train.shape[0]} örnek (%80)")
print(f"✓ Test seti: {X_test.shape[0]} örnek (%20)")
print(f"✓ Özellik sayısı: {X.shape[1]}")

# ============================================================================
# 4. MODEL EĞİTİMİ
# ============================================================================
print("\n[ADIM 4] ÇOKLU REGRESYON MODELİ EĞİTİMİ")
print("-" * 70)

model = LinearRegression()
model.fit(X_train, y_train)

print("✓ Model eğitimi tamamlandı!")
print("\nÇOK BOYUTLU İZDÜŞÜM:")
print("  • 4 boyutlu uzayda (4 özellik) veri noktaları var")
print("  • Model, bu noktaları 4 boyutlu bir hiperdüzleme projekte eder")
print("  • Matematikte: y = w₁x₁ + w₂x₂ + w₃x₃ + w₄x₄ + b")
print("  • Her nokta, bu düzleme en kısa mesafede izdüşüm yapar")

# ============================================================================
# 5. MODEL KATSAYILARI VE ÖZELLİK ÖNEMİ
# ============================================================================
print("\n[ADIM 5] MODEL KATSAYILARI (ÖZELLİK ÖNEMİ)")
print("-" * 70)

# Katsayıları DataFrame'e çevir
ozellik_onemi = pd.DataFrame({
    'Özellik': X.columns,
    'Katsayı': model.coef_
}).sort_values('Katsayı', key=abs, ascending=False)

print("\nÖğrenilen Denklem:")
print(f"Fiyat = {model.intercept_:.0f}", end="")
for i, col in enumerate(X.columns):
    coef = model.coef_[i]
    sign = "+" if coef >= 0 else "-"
    print(f" {sign} {abs(coef):.0f}*{col}", end="")
print()

print("\nÖzellik Önem Sıralaması:")
print(ozellik_onemi.to_string(index=False))

print("\nYORUM:")
for _, row in ozellik_onemi.iterrows():
    ozellik = row['Özellik']
    katsayi = row['Katsayı']

    if katsayi > 0:
        print(f"  • {ozellik}: +{katsayi:.0f} (Artınca fiyat ARTAR)")
    else:
        print(f"  • {ozellik}: {katsayi:.0f} (Artınca fiyat AZALIR)")

# Katsayıları görselleştir
plt.figure(figsize=(10, 5))
colors = ['green' if x > 0 else 'red' for x in ozellik_onemi['Katsayı']]
plt.barh(ozellik_onemi['Özellik'], ozellik_onemi['Katsayı'], color=colors, alpha=0.7)
plt.xlabel('Katsayı Değeri', fontsize=11)
plt.title('Özellik Önem Analizi (Regresyon Katsayıları)', fontsize=13, fontweight='bold')
plt.axvline(x=0, color='black', linestyle='--', linewidth=1)
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('C:/github repolarım/btk_atolye_multimedya_güvenligi/regresyon_izdusumu_projesi/ozellik_onemi.png', dpi=150)
plt.show()

print("✓ Özellik önem grafiği kaydedildi: ozellik_onemi.png")

# ============================================================================
# 6. TAHMİN VE DEĞERLENDİRME
# ============================================================================
print("\n[ADIM 6] MODEL PERFORMANSI")
print("-" * 70)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Metrikler
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_mae = mean_absolute_error(y_train, y_train_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("EĞİTİM SETİ PERFORMANSI:")
print(f"  • R² Skoru: {train_r2:.4f}")
print(f"  • MSE: {train_mse:,.0f}")
print(f"  • MAE: {train_mae:,.0f} TL")

print("\nTEST SETİ PERFORMANSI:")
print(f"  • R² Skoru: {test_r2:.4f}")
print(f"  • MSE: {test_mse:,.0f}")
print(f"  • MAE: {test_mae:,.0f} TL")

print("\nDEĞERLENDİRME:")
print(f"  → Model, fiyat varyansının %{test_r2*100:.1f}'ini açıklıyor")
print(f"  → Ortalama tahmin hatası: ±{test_mae:,.0f} TL")

# ============================================================================
# 7. GÖRSELLEŞTİRME
# ============================================================================
print("\n[ADIM 7] GÖRSELLEŞTİRME")
print("-" * 70)

# 7.1: Gerçek vs Tahmin
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Sol: Scatter plot
axes[0].scatter(y_test, y_test_pred, alpha=0.6, edgecolors='k', linewidth=0.5)
axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
            'r--', linewidth=2, label='Mükemmel Tahmin')
axes[0].set_xlabel('Gerçek Fiyat (TL)', fontsize=11)
axes[0].set_ylabel('Tahmin Edilen Fiyat (TL)', fontsize=11)
axes[0].set_title(f'Gerçek vs Tahmin (R² = {test_r2:.3f})', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Sağ: Hata dağılımı
residuals = y_test - y_test_pred
axes[1].hist(residuals, bins=30, edgecolor='black', alpha=0.7)
axes[1].axvline(x=0, color='red', linestyle='--', linewidth=2, label='Sıfır Hata')
axes[1].set_xlabel('Tahmin Hatası (TL)', fontsize=11)
axes[1].set_ylabel('Frekans', fontsize=11)
axes[1].set_title('Hata Dağılımı (Residuals)', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('C:/github repolarım/btk_atolye_multimedya_güvenligi/regresyon_izdusumu_projesi/performans_analizi.png', dpi=150)
plt.show()

print("✓ Performans grafikleri kaydedildi: performans_analizi.png")

# 7.2: 3D Görselleştirme (2 özellik seçerek)
print("\n3 Boyutlu İzdüşüm Görselleştirmesi oluşturuluyor...")

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Test verisi için 3D scatter
scatter = ax.scatter(X_test['Metrekare'],
                    X_test['Oda_Sayisi'],
                    y_test,
                    c='blue',
                    marker='o',
                    alpha=0.6,
                    label='Gerçek Fiyat')

# Tahminler
ax.scatter(X_test['Metrekare'],
          X_test['Oda_Sayisi'],
          y_test_pred,
          c='red',
          marker='x',
          s=100,
          alpha=0.8,
          label='Tahmin')

ax.set_xlabel('Metrekare (m²)', fontsize=10)
ax.set_ylabel('Oda Sayısı', fontsize=10)
ax.set_zlabel('Fiyat (TL)', fontsize=10)
ax.set_title('3D İzdüşüm: Metrekare + Oda Sayısı → Fiyat', fontsize=12, fontweight='bold')
ax.legend()

plt.savefig('C:/github repolarım/btk_atolye_multimedya_güvenligi/regresyon_izdusumu_projesi/3d_izdusumu.png', dpi=150)
plt.show()

print("✓ 3D görselleştirme kaydedildi: 3d_izdusumu.png")

# ============================================================================
# 8. YENİ TAHMİN YAPMA
# ============================================================================
print("\n[ADIM 8] YENİ EVLER İÇİN FİYAT TAHMİNİ")
print("-" * 70)

yeni_evler = pd.DataFrame({
    'Metrekare': [100, 150, 80, 200],
    'Oda_Sayisi': [3, 4, 2, 5],
    'Ev_Yasi': [5, 10, 2, 15],
    'Merkeze_Mesafe': [10, 5, 20, 3]
})

yeni_tahminler = model.predict(yeni_evler)

print("Yeni evler için fiyat tahminleri:")
print("-" * 70)
for i in range(len(yeni_evler)):
    print(f"\nEv #{i+1}:")
    print(f"  Metrekare: {yeni_evler.iloc[i]['Metrekare']:.0f} m²")
    print(f"  Oda: {yeni_evler.iloc[i]['Oda_Sayisi']:.0f}")
    print(f"  Yaş: {yeni_evler.iloc[i]['Ev_Yasi']:.0f} yıl")
    print(f"  Mesafe: {yeni_evler.iloc[i]['Merkeze_Mesafe']:.0f} km")
    print(f"  → TAHMİNİ FİYAT: {yeni_tahminler[i]:,.0f} TL")

# ============================================================================
# ÖZET
# ============================================================================
print("\n" + "=" * 70)
print("PROJE ÖZETİ - ÇOKLU REGRESYON")
print("=" * 70)
print(f"""
✓ 4 özellikli çoklu regresyon modeli eğitildi
✓ Test R² Skoru: {test_r2:.4f} (Model %{test_r2*100:.1f} açıklama gücü)
✓ Ortalama tahmin hatası: ±{test_mae:,.0f} TL

ÇOK BOYUTLU İZDÜŞÜM KAVRAMI:
  • Tek değişkende: Noktalari bir doğruya projekte ediyorduk
  • Çok değişkende: Noktaları bir hiperdüzleme projekte ediyoruz
  • 4 boyutlu uzayda çalışıyoruz (görselleştirmesi zor!)
  • Matematiksel olarak aynı prensip: Minimize Σ(y_gerçek - y_tahmin)²

EN ÖNEMLİ ÖZELLİKLER:
  1. {ozellik_onemi.iloc[0]['Özellik']}: {ozellik_onemi.iloc[0]['Katsayı']:.0f}
  2. {ozellik_onemi.iloc[1]['Özellik']}: {ozellik_onemi.iloc[1]['Katsayı']:.0f}
  3. {ozellik_onemi.iloc[2]['Özellik']}: {ozellik_onemi.iloc[2]['Katsayı']:.0f}

ÖĞRENILENLER:
  1. Çoklu doğrusal regresyon nasıl çalışır
  2. Çok boyutlu izdüşüm kavramı
  3. Özellik önem analizi
  4. Korelasyon matrisi yorumlama
  5. Model performans metrikleri
  6. 3D görselleştirme teknikleri
""")

print("=" * 70)
print("Program tamamlandı! Tüm grafikler kaydedildi.")
print("=" * 70)
