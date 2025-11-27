# 1. Gerekli kütüphanelerin yüklenmesi
import torch                                     # PyTorch'un temel bileşenleri için
import torch.nn as nn                            # Sinir ağı katmanlarını oluşturmak için
import torch.nn.functional as F                  # Aktivasyon fonksiyonları vb. için
from torchvision import datasets, transforms, models  # Görüntü veri setleri ve dönüşümler için
from torch.utils.data import DataLoader          # Veriyi mini-batch'lerle yüklemek için
from PIL import Image                            # Tekil görselleri yüklemek için (tahmin aşamasında kullanılır)

# 2. Donanım (GPU varsa kullanılır, yoksa CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # Eğitim için uygun donanımı seç

# 3. Görüntü dönüşümleri ve veri seti hazırlığı
# 3. Görüntü dönüşümleri ve veri seti hazırlığı
transform = transforms.Compose([
    transforms.Resize((32, 32)),                 # CIFAR-10 zaten 32x32, ancak model yapısını korumak için explicit belirtelim
    transforms.ToTensor(),                       # Görselleri PyTorch tensörüne dönüştür
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Piksel değerlerini normalize et (RGB için)
])

# CIFAR-10 Veri Setini İndir ve Yükle
print("Veri seti indiriliyor/yükleniyor...")
train_dataset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)         # Eğitim verisini batch'lere böl ve karıştır
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)          # Test verisini batch'lere böl, sıralı şekilde yükle

# 4. CNN model tanımı
class CNNModel(nn.Module):                         # PyTorch model sınıfı tanımlanır
    def __init__(self, num_classes):               # Sınıf sayısı parametre olarak alınır
        super(CNNModel, self).__init__()           # Üst sınıf başlatılır
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1) # 3 kanal (RGB) giriş → 16 filtreli konvolüsyon, 3x3 filtre, padding=1
        self.pool = nn.MaxPool2d(2, 2)              # 2x2 boyutlu max pooling işlemi
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)# 16 giriş → 32 filtreli ikinci konvolüsyon katmanı
        self.fc1 = nn.Linear(32 * 8 * 8, 128)       # Flatten sonrası 128 nöronlu fully connected katman (32x32 -> 16x16 -> 8x8)
        self.fc2 = nn.Linear(128, num_classes)      # Çıkış katmanı: sınıf sayısı kadar nöron

    def forward(self, x):                           # İleri yayılım fonksiyonu
        x = self.pool(F.relu(self.conv1(x)))        # 1. konvolüsyon → ReLU → pooling (32x32 → 16x16)
        x = self.pool(F.relu(self.conv2(x)))        # 2. konvolüsyon → ReLU → pooling (16x16 → 8x8)
        x = x.view(-1, 32 * 8 * 8)                  # 3D tensörü 1D vektöre düzleştir (Flatten)
        x = F.relu(self.fc1(x))                      # FC katmanda aktivasyon uygula
        x = self.fc2(x)                              # Çıkış katmanından geç
        return x                                     # Model çıktısını döndür

model = CNNModel(num_classes=10).to(device)  # Model oluşturulur ve cihaza gönderilir (GPU/CPU)

# 5. Kayıp fonksiyonu ve optimizasyon
criterion = nn.CrossEntropyLoss()                   # Sınıflandırma için uygun kayıp fonksiyonu
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)  # Adam optimizasyon algoritması, öğrenme oranı 0.001

# 6. Modelin eğitimi
num_epochs = 5                                      # Eğitimde kullanılacak epoch sayısı (Hızlı test için 5 yapıldı)

for epoch in range(num_epochs):                     # Her epoch için döngü
    model.train()                                   # Model eğitim moduna alınır
    running_loss = 0.0                              # Epoch boyunca biriken kayıp
    correct = 0                                     # Doğru tahmin sayısı
    total = 0                                       # Toplam örnek sayısı

    for images, labels in train_loader:             # Eğitim verisi üzerinde batch batch dön
        images, labels = images.to(device), labels.to(device)  # Veriyi cihaza aktar

        optimizer.zero_grad()                       # Önceki gradyanlar sıfırlanır
        outputs = model(images)                     # Modelin tahmini alınır
        loss = criterion(outputs, labels)           # Tahmin ile gerçek etiket arasındaki kayıp hesaplanır
        loss.backward()                             # Geri yayılım yapılır
        optimizer.step()                            # Ağırlıklar güncellenir

        running_loss += loss.item()                 # Kayıp değeri toplanır
        _, predicted = torch.max(outputs.data, 1)   # En yüksek skorlu sınıf tahmini yapılır
        total += labels.size(0)                     # Toplam örnek sayısı güncellenir
        correct += (predicted == labels).sum().item()  # Doğru tahmin sayısı toplanır

    accuracy = 100 * correct / total                # Doğruluk oranı hesaplanır
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {running_loss/len(train_loader):.4f}, Accuracy: {accuracy:.2f}%")  # Epoch sonuçları yazdırılır

# 7. Modelin test verisiyle değerlendirilmesi
model.eval()                                        # Model değerlendirme moduna alınır
correct = 0                                         # Doğru tahmin sayısı
total = 0                                           # Toplam test örneği

with torch.no_grad():                               # Gradyan hesabı kapatılır (daha hızlı çalışır)
    for images, labels in test_loader:              # Test verisi batch batch alınır
        images, labels = images.to(device), labels.to(device)  # Veriler cihaza aktarılır
        outputs = model(images)                     # Tahmin yapılır
        _, predicted = torch.max(outputs.data, 1)   # En yüksek olasılıklı sınıf seçilir
        total += labels.size(0)                     # Toplam test örneği güncellenir
        correct += (predicted == labels).sum().item()  # Doğru tahmin sayısı eklenir

print(f"Test Accuracy: {100 * correct / total:.2f}%")  # Test doğruluğu yazdırılır

# 8. Tek bir görsel üzerinde tahmin yapılması (Test setinden rastgele bir örnek)
import random
idx = random.randint(0, len(test_dataset)-1)
img_tensor, label = test_dataset[idx]
img_tensor = img_tensor.unsqueeze(0).to(device) # Batch boyutu ekle ve cihaza gönder

model.eval()
with torch.no_grad():
    output = model(img_tensor)
    _, predicted = torch.max(output, 1)

classes = train_dataset.classes
print(f"Örnek Test - Gerçek: {classes[label]}, Tahmin: {classes[predicted.item()]}")
