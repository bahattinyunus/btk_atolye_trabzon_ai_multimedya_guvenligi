# 17. EXIF Analizi ile Sahtecilik İpuçları

Bu örnek, bir görüntü dosyasının **EXIF (Exchangeable Image File Format)** verilerini okuyarak, görüntü üzerinde oynama yapılıp yapılmadığına dair basit ipuçları elde etmeyi amaçlar.

## 📝 Kod Ne Yapıyor?

1.  **Görüntü Yükleme:** `Pillow` kütüphanesi kullanılarak belirtilen görüntü dosyası (`veriler/ornek_exifli.jpg`) açılır.
2.  **EXIF Okuma:** Görüntüye gömülü olan ham EXIF verileri okunur.
3.  **Veri Çözümleme:** Ham veriler, insan tarafından okunabilir etiket isimlerine (Örn: "Make", "Model", "Software") dönüştürülür.
4.  **Analiz ve Raporlama:**
    *   **Kamera Bilgisi:** Fotoğrafın hangi cihazla çekildiği.
    *   **Yazılım (Software):** Görüntünün en son hangi yazılımla kaydedildiği. Eğer burada "Photoshop", "GIMP" gibi düzenleme programları görünüyorsa, görüntü manipüle edilmiş olabilir.
    *   **Tarih:** Orijinal çekim zamanı.
    *   **GPS:** Konum bilgisinin olup olmadığı.

## 🛠️ Kurulum

Gerekli kütüphaneleri yüklemek için:

```bash
pip install Pillow
```

## ▶️ Kullanım

Kodu çalıştırmak için:

```bash
python 17_exifOrnek.py
```

## 📊 Örnek Çıktı

Aşağıda, EXIF verileri manipüle edilmiş (veya düzenleme yazılımı ile kaydedilmiş) bir görüntü için örnek çıktı verilmiştir:

```text
=== Temel EXIF Bilgileri ===
Dosya      : ..\veriler\ornek_exifli.jpg
Kamera     : Canon / EOS 5D Mark IV
Çekim Zamanı (DateTimeOriginal): 2023:10:27 10:00:00
Yazılım    : Adobe Photoshop Lightroom Classic 10.0 (Windows)
GPS        : YOK (GPSInfo alanı bulunamadı)

=== Basit Sahtecilik İpuçları (Kaba Analiz) ===
- UYARI: EXIF 'Software' alanında bir düzenleme yazılımı görünüyor.
  Bu, görüntü üzerinde sonradan işlem yapılmış olabileceğine işaret eder.
  (Bu her zaman sahtecilik demek değildir; basit parlaklık/renk düzeltmeleri de olabilir.)
- Çekim zamanı EXIF'te mevcut: 2023:10:27 10:00:00
  (Bu zamanın doğru olup olmadığı, cihaz saati ve olayla ilgili iddialarla karşılaştırılmalıdır.)
- GPS bilgisi yok. Bu normal olabilir (GPS kapalıyken çekilmiş olabilir).
- Kamera bilgisi: Canon / EOS 5D Mark IV
  Bu bilgi, aynı olayla ilgili farklı fotoğrafların aynı cihazdan çıkıp çıkmadığını karşılaştırmak için kullanılabilir.

NOT:
- Bu analiz, sadece EXIF üzerinden çok basit ipuçları verir.
- EXIF bilgisi manipüle edilebilir, eksik olabilir veya tamamen silinmiş olabilir.
- Gerçek sahtecilik tespiti için EXIF analizi, görüntü içeriği analizi (ışık, gölge, JPEG artefaktları,
  copy-move/splicing tespiti, derin öğrenme tabanlı yöntemler vb.) ile birlikte değerlendirilmelidir.
```

## ⚠️ Önemli Notlar

*   **Software Alanı:** Bir görüntünün EXIF verisinde "Photoshop" yazması, o görüntünün kesinlikle "sahte" (içeriği değiştirilmiş) olduğu anlamına gelmez. Sadece renk ayarı yapılmış veya kırpılmış olabilir. Ancak, haber değeri taşıyan bir fotoğrafta bu alan şüphe uyandırır.
*   **EXIF Silinmesi:** WhatsApp, Facebook, Instagram gibi platformlar, yüklenen fotoğrafların EXIF verilerini otomatik olarak siler. Bu nedenle sosyal medyadan indirilen fotoğraflarda genellikle EXIF verisi bulunmaz.
*   **Manipülasyon:** EXIF verileri çok kolay bir şekilde değiştirilebilir (editlenebilir). Bu nedenle tek başına kesin bir kanıt olarak kullanılamaz.
