# Gerekli kütüphaneleri içe aktar
import matplotlib.pyplot as plt                            # Görselleştirme için matplotlib
from sklearn.datasets import load_breast_cancer           # Hazır meme kanseri veri seti
from sklearn.linear_model import LogisticRegression        # Lojistik regresyon sınıflandırıcısı
from sklearn.model_selection import train_test_split       # Eğitim/test verisi ayırmak için
from sklearn.metrics import (                              # Değerlendirme metrikleri
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

# 1. Hazır veri setini yükle (meme kanseri veri seti)
data = load_breast_cancer()         # 30 özellikli, 2 sınıflı (malignant vs. benign)
X = data.data                       # Giriş özellikleri (özellik matrisi)
y = data.target                     # Sınıf etiketleri (0 = malign, 1 = benign)

# 2. Veriyi eğitim ve test setine ayır (80% eğitim, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,                           # Giriş ve hedef değişkenler
    test_size=0.2,                  # %20 test verisi
    random_state=42                # Tekrarlanabilirlik için sabit rastgelelik
)

# 3. Lojistik Regresyon modelini tanımla ve eğit
model = LogisticRegression(max_iter=10000)  # Maksimum iterasyon artırıldı, çünkü bazı veri setlerinde varsayılan değer yeterli olmayabilir
model.fit(X_train, y_train)                 # Modeli eğitim verisiyle eğit

# 4. Test verisi üzerinde tahmin yap
y_pred = model.predict(X_test)              # Test verileriyle sınıf tahmini yapılır

# 5. Değerlendirme metriklerini hesapla

acc = accuracy_score(y_test, y_pred)        # Toplam doğru tahmin oranı
prec = precision_score(y_test, y_pred)      # Pozitif tahminlerin ne kadarı doğru?
rec = recall_score(y_test, y_pred)          # Gerçek pozitiflerin ne kadarını yakaladık?
f1 = f1_score(y_test, y_pred)               # Precision ve recall’un harmonik ortalaması

# 6. Metrikleri ekrana yazdır
print("=== Değerlendirme Metrikleri ===")
print(f"Accuracy  : {acc:.4f}")             # Doğruluk oranı
print(f"Precision : {prec:.4f}")            # Kesinlik
print(f"Recall    : {rec:.4f}")             # Duyarlılık
print(f"F1-Score  : {f1:.4f}")              # F1 skoru

# 7. Sınıf bazlı performans raporu yazdır
print("\n=== Sınıf Bazlı Rapor ===")
print(classification_report(                # Her sınıf için precision, recall, f1 ve support (örnek sayısı)
    y_test,
    y_pred,
    target_names=data.target_names          # Sınıf isimlerini (benign / malignant) yaz
))

# 8. Karışıklık Matrisi Hesapla ve Görselleştir
cm = confusion_matrix(y_test, y_pred)       # Karışıklık matrisi: TP, TN, FP, FN değerleri
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,                    # Hesaplanan matris
    display_labels=data.target_names        # Eksende sınıf adlarını göster
)
disp.plot(cmap='Blues')                     # Matristen bir ısı haritası oluştur (Blues renk haritası)
plt.title("Karışıklık Matrisi")             # Grafik başlığı
plt.show()                                  # Grafiği göster
