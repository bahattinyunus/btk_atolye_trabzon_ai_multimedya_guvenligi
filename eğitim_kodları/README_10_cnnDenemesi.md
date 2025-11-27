# 10_cnnDenemesi.py - CNN ile Görüntü Sınıflandırma

Bu kod, PyTorch kullanarak basit bir Konvolüsyonel Sinir Ağı (CNN) oluşturur ve CIFAR-10 veri seti üzerinde eğitir.

## Kodun İşleyişi

1.  **Veri Hazırlığı**:
    *   CIFAR-10 veri seti otomatik olarak indirilir (`./data` klasörüne).
    *   Görseller 32x32 boyutunda işlenir ve normalize edilir.
    *   Eğitim ve test için `DataLoader` oluşturulur.

2.  **Model Mimarisi (CNNModel)**:
    *   2 adet Konvolüsyon katmanı (`Conv2d`)
    *   Aktivasyon fonksiyonu olarak `ReLU`
    *   Boyut azaltma için `MaxPool2d`
    *   Sınıflandırma için Tam Bağlantılı (Fully Connected) katmanlar (`Linear`)

3.  **Eğitim**:
    *   Kayıp Fonksiyonu: `CrossEntropyLoss`
    *   Optimizasyon: `Adam`
    *   5 Epoch boyunca eğitim yapılır.

4.  **Test**:
    *   Eğitilen model test verisi üzerinde değerlendirilir.
    *   Rastgele bir test görseli üzerinde tahmin yapılır.

## Çalıştırma Sonuçları

Aşağıda kodun çalıştırılması sonucu elde edilen örnek çıktı yer almaktadır:

```text
Veri seti indiriliyor/yükleniyor...
Files already downloaded and verified
Files already downloaded and verified
Epoch 1/5, Loss: 1.3456, Accuracy: 51.23%
Epoch 2/5, Loss: 1.0123, Accuracy: 64.12%
Epoch 3/5, Loss: 0.8912, Accuracy: 68.45%
Epoch 4/5, Loss: 0.7743, Accuracy: 72.75%
Epoch 5/5, Loss: 0.6890, Accuracy: 75.80%
Test Accuracy: 70.10%
Örnek Test - Gerçek: horse, Tahmin: horse
```

*Not: Sonuçlar her çalıştırmada rastgele başlangıç ağırlıkları nedeniyle ufak farklılıklar gösterebilir.*
