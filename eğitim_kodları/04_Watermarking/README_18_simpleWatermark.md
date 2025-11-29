# 18. Basit LSB Damgalama (Watermarking)

Bu kod, **En Az Anlamlı Bit (LSB - Least Significant Bit)** yöntemini kullanarak bir görüntünün içine başka bir görüntüyü (damgayı) gizler. Bu, steganografinin en temel yöntemlerinden biridir.

## 📝 Kod Ne Yapıyor?

1.  **Damga Ekleme (Embedding):**
    *   Kaynak görüntüyü ve damga görüntüsünü gri seviyeye çevirir.
    *   Damga görüntüsünü siyah-beyaz (binary) hale getirir.
    *   Kaynak görüntünün piksellerinin son bitlerini (LSB) temizler.
    *   Damga bitlerini bu temizlenen yerlere yazar.
    *   Sonuçta, insan gözüyle fark edilemeyen ama içinde veri taşıyan "damgalı" bir görüntü oluşur.

2.  **Damga Çıkarma (Extraction):**
    *   Damgalı görüntüden son bitleri okur.
    *   Bu bitleri tekrar bir görüntü matrisine dönüştürür.
    *   Orijinal damga ile çıkarılan damgayı karşılaştırır.

3.  **Analiz (PSNR & SSIM):**
    *   **PSNR (Peak Signal-to-Noise Ratio):** Orijinal görüntü ile damgalı görüntü arasındaki kalite farkını ölçer. Yüksek olması iyidir.
    *   **SSIM (Structural Similarity Index):** Orijinal damga ile çıkarılan damga arasındaki benzerliği ölçer. 1.0'a yakın olması iyidir.

## 🛠️ Kurulum

Gerekli kütüphaneler:

```bash
pip install Pillow numpy matplotlib scikit-image
```

## ▶️ Kullanım

Kodu çalıştırmak için:

```bash
python 18_simpleWatermark.py
```

Kod, `../veriler/ai_content.png` içine `../veriler/gan_face_256.png` görüntüsünü gizler.

## ⚠️ Sınırlamalar

*   **Kırılganlık:** LSB yöntemi çok kırılgandır. Görüntü sıkıştırılırsa (JPEG), yeniden boyutlandırılırsa veya üzerine filtre uygulanırsa damga bozulur.
*   **Kapasite:** Gizlenecek veri miktarı, taşıyıcı görüntünün boyutuyla sınırlıdır.
