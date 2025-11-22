# SVM BASİT UYGULAMA - IRIS ÇİÇEK SINIFLANDIRMA
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

print("🌸 SVM İLE ÇİÇEK SINIFLANDIRMA - BAŞLIYORUZ!")
print("=" * 50)

# 1. VERİYİ YÜKLE VE İNCELE
print("\n1. VERİ SETİNİ YÜKLÜYORUM...")
iris = load_iris()
X = iris.data  # Çiçek özellikleri
y = iris.target  # Çiçek türleri

print(f"✓ Toplam çiçek sayısı: {len(X)}")
print(f"✓ Özellik sayısı: {X.shape[1]}")
print(f"✓ Çiçek türleri: {iris.target_names}")

# Özellik isimlerini göster
print("\n📋 ÇİÇEK ÖZELLİKLERİ:")
for i, ozellik in enumerate(iris.feature_names):
    print(f"  {i + 1}. {ozellik}")

# Sınıf dağılımını göster
print("\n📊 SINIF DAĞILIMI:")
for i, tur in enumerate(iris.target_names):
    sayi = sum(y == i)
    print(f"  {tur}: {sayi} çiçek")
i
# 2. VERİYİ HAZIRLA
print("\n2. VERİYİ HAZIRLIYORUM...")
# Veriyi standardize et (SVM için önemli!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("✓ Veri standardizasyonu tamamlandı")

# 3. VERİYİ BÖL
print("\n3. VERİYİ EĞİTİM VE TEST OLARAK BÖLÜYORUM...")
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,  # Sınıf dağılımını koru
)

print(f"✓ Eğitim seti: {X_train.shape[0]} çiçek")
print(f"✓ Test seti: {X_test.shape[0]} çiçek")

# 4. SVM MODELİNİ OLUŞTUR VE EĞİT
print("\n4. SVM MODELİNİ EĞİTİYORUM...")
model = SVC(kernel="rbf", C=1.0, random_state=42)
model.fit(X_train, y_train)
print("✓ Model eğitimi tamamlandı")

# 5. MODELİ TEST ET
print("\n5. MODELİ TEST EDİYORUM...")
tahminler = model.predict(X_test)
dogruluk = accuracy_score(y_test, tahminler)

print(f"🎯 TEST SONUÇLARI:")
print(f"✓ Doğruluk: {dogruluk:.1%}")

# Karışıklık matrisi
print(f"\n📊 KARIŞIKLIK MATRİSİ:")
cm = confusion_matrix(y_test, tahminler)
print(cm)

# Sınıflandırma raporu
print(f"\n📈 DETAYLI RAPOR:")
print(classification_report(y_test, tahminler, target_names=iris.target_names))

# 6. MODEL HAKKINDA BİLGİ
print("\n6. MODEL BİLGİLERİ:")
print(f"✓ Kullanılan çekirdek: {model.kernel}")
print(f"✓ Destek vektör sayısı: {len(model.support_vectors_)}")
print(f"✓ Toplam eğitim örneği: {len(X_train)}")
print(f"✓ Destek vektör oranı: {len(model.support_vectors_) / len(X_train):.1%}")

# 7. FARKLI ÇEKİRDEKLERİ DENEYELİM
print("\n7. FARKLI ÇEKİRDEKLERİ KARŞILAŞTIRIYORUM...")
cekirdekler = ["linear", "rbf", "poly"]

for cekirdek in cekirdekler:
    if cekirdek == "poly":
        gecici_model = SVC(kernel=cekirdek, degree=3, random_state=42)
    else:
        gecici_model = SVC(kernel=cekirdek, random_state=42)

    gecici_model.fit(X_train, y_train)
    skor = gecici_model.score(X_test, y_test)
    print(f"  {cekirdek:8} çekirdek: {skor:.1%} doğru")

# 8. C PARAMETRESİNİ TEST EDELİM
print("\n8. C PARAMETRESİNİ TEST EDİYORUM...")
C_degerleri = [0.1, 1, 10, 100]

for C in C_degerleri:
    gecici_model = SVC(kernel="rbf", C=C, random_state=42)
    gecici_model.fit(X_train, y_train)
    skor = gecici_model.score(X_test, y_test)
    print(f"  C = {C:4}: {skor:.1%} doğru")

# 9. YENİ BİR ÇİÇEK TAHMİNİ
print("\n9. YENİ BİR ÇİÇEK İÇİN TAHMİN YAPIYORUM...")
# Örnek bir çiçek oluşturalım (setosa benzeri)
yeni_cicek = np.array([[5.1, 3.5, 1.4, 0.2]])

# Aynı şekilde ölçeklendir
yeni_cicek_scaled = scaler.transform(yeni_cicek)

# Tahmin yap
tahmin = model.predict(yeni_cicek_scaled)[0]
tahmin_olasilik = model.decision_function(yeni_cicek_scaled)

print(f"📝 YENİ ÇİÇEK ÖZELLİKLERİ:")
print(f"  Taç yaprak uzunluğu: 5.1 cm")
print(f"  Taç yaprak genişliği: 3.5 cm")
print(f"  Çanak yaprak uzunluğu: 1.4 cm")
print(f"  Çanak yaprak genişliği: 0.2 cm")

print(f"\n🔮 TAHMİN SONUCU:")
print(f"  Tahmin edilen tür: {iris.target_names[tahmin]}")

print(f"\n📊 KARAR FONKSİYONU DEĞERLERİ:")
for i, deger in enumerate(tahmin_olasilik[0]):
    print(f"  {iris.target_names[i]}: {deger:7.3f}")

# 10. ÖZELLİK ÖNEMİ
print("\n10. ÖZELLİK ÖNEM ANALİZİ:")
# Linear kernel ile özellik önemlerini hesapla
linear_model = SVC(kernel="linear", random_state=42)
linear_model.fit(X_train, y_train)

print("📈 ÖZELLİKLERİN ÖNEM SIRALAMASI:")
onemler = np.abs(linear_model.coef_[0])
for i in np.argsort(onemler)[::-1]:
    print(f"  {iris.feature_names[i]}: {onemler[i]:.3f}")

# 11. SONUÇ ÖZETİ
print("\n" + "=" * 50)
print("🎉 SONUÇ ÖZETİ")
print("=" * 50)
print(f"✅ Model başarısı: {dogruluk:.1%}")
print(f"✅ En iyi çekirdek: {model.kernel}")
print(f"✅ Destek vektör sayısı: {len(model.support_vectors_)}")

if dogruluk > 0.95:
    print("🔥 MÜKEMMEL: Model çok yüksek doğrulukta!")
elif dogruluk > 0.90:
    print("👍 ÇOK İYİ: Model iyi çalışıyor!")
elif dogruluk > 0.85:
    print("👌 İYİ: Model kabul edilebilir düzeyde!")
else:
    print("💡 GELİŞTİRİLEBİLİR: Modelin iyileştirilmesi gerekebilir.")

print(f"\n🏁 UYGULAMA TAMAMLANDI!")

"""


"""
