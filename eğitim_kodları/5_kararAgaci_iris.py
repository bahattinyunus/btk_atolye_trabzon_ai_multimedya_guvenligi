# Gerekli kütüphaneleri import edelim
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("=== KARAR AĞAÇLARI - IRIS ÇİÇEĞİ SINIFLANDIRMA ===")
print("Bu kod, Karar Ağacı algoritmasının temel kullanımını göstermektedir.\n")

# 1. VERİ HAZIRLAMA
# Iris veri setini yükleyelim - bu veri seti 3 farklı çiçek türünü içerir
iris = load_iris()
X = iris.data  # 4 özellik: taç yaprak uzunluk/genişlik, çanak yaprak uzunluk/genişlik
y = iris.target  # 3 sınıf: setosa, versicolor, virginica

# Özellik ve sınıf isimlerini al
feature_names = iris.feature_names
target_names = iris.target_names

print("1. VERİ HAZIRLAMA")
print("Veri Seti Boyutu:", X.shape)  # (150 örnek, 4 özellik)
print("Sınıf Dağılımı:", np.bincount(y))  # Her sınıftan 50 örnek
print("Sınıf İsimleri:", target_names)
print("Özellik İsimleri:", feature_names)

# 2. VERİYİ BÖLME (EĞİTİM VE TEST)
# Veriyi %80 eğitim, %20 test olarak bölelim
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,  # Test seti için %20
    random_state=42,  # Aynı sonuçları almak için
    stratify=y  # Sınıf dağılımını koru
)

print("\n2. VERİ BÖLME SONUÇLARI")
print(f"Eğitim seti boyutu: {X_train.shape}")  # (120, 4)
print(f"Test seti boyutu: {X_test.shape}")  # (30, 4)
print(f"Eğitim seti sınıf dağılımı: {np.bincount(y_train)}")
print(f"Test seti sınıf dağılımı: {np.bincount(y_test)}")

# 3. KARAR AĞACI MODELİNİ OLUŞTURMA VE EĞİTME
print("\n3. MODEL EĞİTİMİ")
# DecisionTreeClassifier parametreleri:
# - criterion='gini': Bölme kriteri (Gini indeksi)
# - max_depth=3: Ağacın maksimum derinliği (overfitting'i önlemek için)
# - random_state=42: Tekrarlanabilir sonuçlar için
model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)

# Modeli eğitim verisiyle eğitelim
model.fit(X_train, y_train)

print("Model eğitimi tamamlandı!")
print(f"Eğitim doğruluğu: {model.score(X_train, y_train):.3f}")

# 4. TAHMİN YAPMA
print("\n4. TAHMİN SONUÇLARI")
# Test seti üzerinde tahmin yapalım
y_pred = model.predict(X_test)

print("Test seti için ilk 10 tahmin:")
print("Gerçek Değerler:", y_test[:10])
print("Tahminler:      ", y_pred[:10])

# 5. MODEL PERFORMANS DEĞERLENDİRME
print("\n5. MODEL PERFORMANSI")
# Doğruluk skoru
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Doğruluğu: {accuracy:.3f}")

# Karışıklık Matrisi - modelin hangi sınıfları doğru/yanlış tahmin ettiğini gösterir
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nKarışıklık Matrisi:")
print(conf_matrix)
print("Açıklama: Satırlar gerçek değerleri, sütunlar tahminleri gösterir")

# Detaylı Sınıflandırma Raporu
class_report = classification_report(y_test, y_pred, target_names=target_names)
print("\nSınıflandırma Raporu:")
print(class_report)

# 6. ÖZELLİK ÖNEM DERECELERİ
print("\n6. ÖZELLİK ÖNEM SIRALAMASI")
# Her özelliğin modele katkısını gösterir (toplam 1.0)
feature_importance = pd.DataFrame({
    'Özellik': feature_names,
    'Önem': model.feature_importances_
}).sort_values('Önem', ascending=False)

print(feature_importance)
print("\nNot: Önem değerleri 0-1 arasındadır, toplamı 1.0'dır")
print("Yüksek önem = özellik karar vermede daha etkili")

# 7. FARKLI PARAMETRELERİN PERFORMANSA ETKİSİ
print("\n7. PARAMETRE KARŞILAŞTIRMASI")
print("Farklı parametrelerle model performansı:")

parametreler = [
    {'criterion': 'gini', 'max_depth': 2, 'aciklama': 'Sığ ağaç (Gini)'},
    {'criterion': 'gini', 'max_depth': 5, 'aciklama': 'Orta derinlik (Gini)'},
    {'criterion': 'entropy', 'max_depth': 3, 'aciklama': 'Orta derinlik (Entropi)'},
    {'criterion': 'entropy', 'max_depth': None, 'aciklama': 'Sınırsız derinlik (Entropi)'}
]

for i, params in enumerate(parametreler, 1):
    # Model oluştur ve eğit
    temp_model = DecisionTreeClassifier(
        criterion=params['criterion'],
        max_depth=params['max_depth'],
        random_state=42
    )
    temp_model.fit(X_train, y_train)

    # Performansı hesapla
    train_score = temp_model.score(X_train, y_train)
    test_score = temp_model.score(X_test, y_test)

    print(f"\n{i}. {params['aciklama']}:")
    print(f"   Eğitim Doğruluğu: {train_score:.3f}")
    print(f"   Test Doğruluğu: {test_score:.3f}")
    print(f"   Düğüm Sayısı: {temp_model.tree_.node_count}")

# 8. YENİ ÖRNEK İLE TAHMİN
print("\n8. YENİ ÖRNEK TAHMİNİ")
# Yeni bir çiçek ölçümü için tahmin yapalım
new_flower = np.array([[5.0, 3.5, 1.5, 0.2]])  # [taç uzunluk, taç genişlik, çanak uzunluk, çanak genişlik]

prediction = model.predict(new_flower)
probability = model.predict_proba(new_flower)

print(f"Yeni çiçek özellikleri: {new_flower[0]}")
print(f"Tahmin edilen sınıf: {target_names[prediction[0]]}")
print(f"Olasılık dağılımı: {probability[0]}")

print("\nDetaylı olasılıklar:")
for i, prob in enumerate(probability[0]):
    print(f"  {target_names[i]}: {prob:.3f}")

# 9. OVERFITTING ANALİZİ
print("\n9. OVERFITTING ANALİZİ")
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
accuracy_gap = train_accuracy - test_accuracy

print(f"Eğitim Doğruluğu: {train_accuracy:.3f}")
print(f"Test Doğruluğu: {test_accuracy:.3f}")
print(f"Performans Farkı: {accuracy_gap:.3f}")

if accuracy_gap > 0.1:
    print("UYARI: Overfitting olabilir (eğitim-test farkı yüksek)")
elif accuracy_gap < 0.05:
    print("İYİ: Model iyi genelleme yapıyor")
else:
    print("BİLGİ: Model makul genelleme yapıyor")

# 10. ÇAPRAZ DOĞRULAMA İLE MODEL GÜVENİLİRLİĞİ
print("\n10. ÇAPRAZ DOĞRULAMA SONUÇLARI")
# 5 katlı çapraz doğrulama ile modelin daha güvenilir performansını ölçelim
cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"Çapraz Doğrulama Skorları: {cv_scores}")
print(f"Ortalama Doğruluk: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")

# 11. MODEL DETAYLARI
print("\n11. MODEL DETAYLARI")
print(f"Ağaç derinliği: {model.get_depth()}")
print(f"Yaprak sayısı: {model.get_n_leaves()}")
print(f"Toplam düğüm sayısı: {model.tree_.node_count}")

# 12. KARAR AĞACI ALGORİTMASI ÖZETİ
print("\n" + "=" * 60)
print("KARAR AĞAÇLARI ALGORİTMASI ÖZETİ")
print("=" * 60)

print("\nAVANTAJLARI:")
print("• Yorumlanması kolay (beyaz kutu modeli)")
print("• Hem kategorik hem sayısal verilerle çalışabilir")
print("• Veri ön işleme (normalizasyon) gerektirmez")
print("• Doğrusal olmayan ilişkileri modelleyebilir")

print("\nDEZAVANTAJLARI:")
print("• Aşırı öğrenmeye (overfitting) eğilimli")
print("• Küçük veri setlerinde kararsız olabilir")
print("• Eğik karar sınırlarında zorlanır")

print("\nKULLANIM ALANLARI:")
print("• Müşteri segmentasyonu")
print("• Kredi risk değerlendirmesi")
print("• Tıbbi teşhis sistemleri")
print("• Kalite kontrol")

print("\nONEMLI PARAMETRELER:")
print("• max_depth: Ağaç derinliği (overfitting kontrolü)")
print("• min_samples_split: Bölme için minimum örnek sayısı")
print("• min_samples_leaf: Yaprak için minimum örnek sayısı")
print("• criterion: Bölme kriteri (gini/entropy)")

print("\nPERFORMANS METRIKLERI:")
print("• Doğruluk (Accuracy): Genel doğruluk oranı")
print("• Precision: Pozitif tahminlerin doğruluğu")
print("• Recall: Gerçek pozitiflerin ne kadarını bulduğu")
print("• F1-Score: Precision ve Recall harmonik ortalaması")

print(f"\nUYGULAMA TAMAMLANDI!")
print(f"Final test dogruluğu: {accuracy:.3f}")
print("Karar agaci basariyla olusturuldu ve degerlendirildi!")