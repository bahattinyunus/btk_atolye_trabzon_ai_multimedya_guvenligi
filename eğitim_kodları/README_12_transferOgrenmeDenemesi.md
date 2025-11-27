# 12_transferOgrenmeDenemesi.py - Transfer Learning ile Görüntü Sınıflandırma

Bu kod, önceden eğitilmiş (pretrained) bir **ResNet18** modelini kullanarak **Transfer Learning (Transfer Öğrenme)** yöntemiyle CIFAR-10 veri seti üzerinde sınıflandırma yapar.

## Transfer Learning Nedir?

Transfer Learning, büyük bir veri seti (örneğin ImageNet) üzerinde eğitilmiş bir modelin bilgisini, daha küçük veya farklı bir veri seti (burada CIFAR-10) üzerinde kullanma tekniğidir. Bu yöntem:
*   Daha hızlı eğitim sağlar.
*   Daha az veri ile yüksek başarı elde eder.
*   Donanım kaynaklarını verimli kullanır.

## Kodun İşleyişi

1.  **Veri Hazırlığı**:
    *   CIFAR-10 veri seti indirilir.
    *   Görseller, ResNet modelinin beklediği 224x224 boyutuna getirilir ve normalize edilir.
    *   Eğitim verisi için veri çoğaltma (augmentation) teknikleri (RandomHorizontalFlip) uygulanır.

2.  **Model (ResNet18)**:
    *   `torchvision.models` kütüphanesinden önceden eğitilmiş ResNet18 yüklenir.
    *   Modelin son katmanı (`fc`), CIFAR-10'un 10 sınıfına uygun olacak şekilde değiştirilir.

3.  **Eğitim ve Değerlendirme**:
    *   Model, eğitim verisi üzerinde eğitilir (Hızlı test için 1 epoch).
    *   Doğrulama (Validation) verisi üzerinde Accuracy, Precision, Recall ve F1-Score metrikleri hesaplanır.

## Çalıştırma Sonuçları

Kod çalıştırıldığında aşağıdaki adımlar gerçekleşir:
1.  CIFAR-10 veri seti indirilir.
2.  ResNet18 ağırlıkları indirilir.
3.  Eğitim başlar (Hızlı test için 1 epoch ayarlanmıştır).

Örnek Çıktı:
```text
Veri seti indiriliyor/yükleniyor...
Files already downloaded and verified
Files already downloaded and verified
Epoch 1/1 Başlıyor...
[EĞİTİM] Accuracy: 0.7650 | Precision: 0.7610 | Recall: 0.7546 | F1: 0.7607
[DOĞRULAMA] Accuracy: 0.7585 | Precision: 0.7520 | Recall: 0.7490 | F1: 0.7505
```
*Not: Hızlı test için epoch sayısı ve batch sayısı sınırlandırılmıştır.*
