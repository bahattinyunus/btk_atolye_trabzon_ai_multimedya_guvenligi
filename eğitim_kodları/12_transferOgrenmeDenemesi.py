# transfer_learning_with_metrics.py

# ============================ #
#         KÜTÜPHANELER         #
# ============================ #

import os  # Dosya yolları için kullanılır
import torch  # PyTorch ana kütüphanesi
import torch.nn as nn  # Sinir ağı katmanları ve kayıp fonksiyonları
from torchvision import datasets, models, transforms  # Görüntü veri setleri, modeller, dönüşümler
from torch.utils.data import DataLoader  # Mini-batch veri yükleyici
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score  # Değerlendirme metrikleri

# ============================ #
#       CİHAZ SEÇİMİ           #
# ============================ #

# GPU varsa kullan, yoksa CPU kullanılır
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ============================ #
#      VERİ DÖNÜŞÜMLERİ       #
# ============================ #

# Eğitim verisi için dönüşümler
train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),          # Görüntüyü rastgele kırp ve 224x224'e yeniden boyutlandır
    transforms.RandomHorizontalFlip(),          # %50 olasılıkla yatay çevirme uygula
    transforms.ToTensor(),                      # Görüntüyü tensöre çevir (0-1 arası normalize eder)
    transforms.Normalize([0.485, 0.456, 0.406],  # RGB kanal ortalamaları
                         [0.229, 0.224, 0.225])  # RGB kanal standart sapmaları
])

# Doğrulama verisi için dönüşümler (augmentasyon içermez)
val_transform = transforms.Compose([
    transforms.Resize(256),                     # Görüntüyü 256 piksele yeniden boyutlandır
    transforms.CenterCrop(224),                 # Ortadan 224x224 boyutunda kırp
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# ============================ #
#         VERİ SETİ           #
# ============================ #

# ImageFolder formatındaki veri setlerini yükle (alt klasörler sınıf adlarıdır)
train_dataset = datasets.ImageFolder("data2/train", transform=train_transform)
val_dataset = datasets.ImageFolder("data2/test", transform=val_transform)

# Mini-batch veri yükleyici (shuffle=True → sıralamayı karıştırır)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# ============================ #
#       MODELİ YÜKLE          #
# ============================ #

# ResNet18 modelini ImageNet ağırlıklarıyla yükle
model = models.resnet18(pretrained=True)

# Modelin son katmanını (fc) kendi sınıf sayımıza göre değiştir
num_classes = len(train_dataset.classes)  # Kaç farklı sınıf varsa öğren
model.fc = nn.Linear(model.fc.in_features, num_classes)  # Yeni Linear katman ile değiştir

# Modeli GPU/CPU üzerine taşı
model = model.to(device)

# ============================ #
#    KAYIP FONKSİYONU ve OPTİMİZER   #
# ============================ #

# Çok sınıflı sınıflandırma için uygun kayıp fonksiyonu
criterion = nn.CrossEntropyLoss()

# Ağırlıkları optimize etmek için Adam algoritması kullan
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

# ============================ #
#         EĞİTİM DÖNGÜSÜ       #
# ============================ #

model.train()  # Modeli eğitim moduna geçir (dropout vs. aktifleşir)

# Eğitim metrikleri için listeler oluştur
all_preds = []    # Tahmin edilen sınıflar
all_labels = []   # Gerçek etiketler

# Tüm eğitim verisi üzerinde bir epoch'luk eğitim
for images, labels in train_loader:
    images, labels = images.to(device), labels.to(device)  # Veriyi cihaza aktar (GPU/CPU)

    outputs = model(images)                # Model üzerinden tahmin al
    loss = criterion(outputs, labels)      # Gerçek etiketlerle karşılaştır, kaybı hesapla

    optimizer.zero_grad()                  # Önceki gradyanları sıfırla
    loss.backward()                        # Geri yayılım işlemi (gradyan hesaplama)
    optimizer.step()                       # Ağırlıkları güncelle (optimizasyon)

    # Tahminleri listeye ekle (metrikler için)
    _, preds = torch.max(outputs, 1)       # En yüksek olasılığa sahip sınıf tahmini
    all_preds.extend(preds.cpu().numpy())  # GPU'dan CPU'ya taşı, numpy dizisine çevir
    all_labels.extend(labels.cpu().numpy())

# ============================ #
#      EĞİTİM METRİKLERİ       #
# ============================ #

# Doğruluk: Toplam doğru tahmin / toplam örnek
train_acc = accuracy_score(all_labels, all_preds)

# Kesinlik: Doğru pozitif tahminler / toplam pozitif tahminler
train_prec = precision_score(all_labels, all_preds, average='macro')

# Duyarlılık: Doğru pozitif tahminler / toplam gerçek pozitifler
train_rec = recall_score(all_labels, all_preds, average='macro')

# F1-Skor: Precision ve Recall'un harmonik ortalaması
train_f1 = f1_score(all_labels, all_preds, average='macro')

# Eğitim sonuçlarını ekrana yaz
print(f"[EĞİTİM] Accuracy: {train_acc:.4f} | Precision: {train_prec:.4f} | Recall: {train_rec:.4f} | F1: {train_f1:.4f}")

# ============================ #
#      DOĞRULAMA DÖNGÜSÜ       #
# ============================ #

model.eval()  # Modeli değerlendirme moduna al (dropout, batchnorm sabitlenir)

# Metrikler için liste oluştur
all_preds = []
all_labels = []

# Gradyan takibi kapalıyken doğrulama yapılır (daha az bellek kullanımı)
with torch.no_grad():
    for images, labels in val_loader:
        images, labels = images.to(device), labels.to(device)  # Veriyi cihaza aktar

        outputs = model(images)              # Tahmin üret
        _, preds = torch.max(outputs, 1)     # Tahmin sınıfı

        all_preds.extend(preds.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())

# ============================ #
#    DOĞRULAMA METRİKLERİ      #
# ============================ #

val_acc = accuracy_score(all_labels, all_preds)
val_prec = precision_score(all_labels, all_preds, average='macro')
val_rec = recall_score(all_labels, all_preds, average='macro')
val_f1 = f1_score(all_labels, all_preds, average='macro')

print(f"[DOĞRULAMA] Accuracy: {val_acc:.4f} | Precision: {val_prec:.4f} | Recall: {val_rec:.4f} | F1: {val_f1:.4f}")
