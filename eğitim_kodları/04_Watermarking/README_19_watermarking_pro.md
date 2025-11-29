# 19. Profesyonel Damgalama (IWT + QIM)

Bu kod, **Integer Wavelet Transform (IWT)** ve **Quantization Index Modulation (QIM)** tekniklerini kullanarak daha dayanıklı ve profesyonel bir damgalama işlemi gerçekleştirir.

## 📝 Kod Ne Yapıyor?

1.  **Dönüşüm (IWT):** Görüntüyü frekans bantlarına (LL, LH, HL, HH) ayırır. IWT (Integer Wavelet Transform) kullanıldığı için işlem tersine çevrilebilir ve kayıpsızdır.
2.  **Gömme (QIM):** Damga verisi, görüntünün en önemli frekans bandı olan **LL (Low-Low)** bandına gömülür. Bu, damganın sıkıştırma ve gürültüye karşı daha dayanıklı olmasını sağlar.
3.  **Quantization:** Katsayılar belirli bir aralığa (T) göre kuantize edilerek veri gizlenir.
4.  **Ters Dönüşüm:** İşlenmiş frekans katsayıları tekrar görüntü uzayına dönüştürülür.

## 🛠️ Kurulum

Gerekli kütüphaneler:

```bash
pip install Pillow numpy matplotlib scikit-image
```

## ▶️ Kullanım

Kodu çalıştırmak için:

```bash
python 19_watermarking_pro.py
```

Kod, `../veriler/ai_content.png` içine `../veriler/gan_face_256.png` görüntüsünü gizler.

## 📊 Avantajları

*   **Dayanıklılık:** LSB yöntemine göre JPEG sıkıştırmasına ve gürültüye karşı çok daha dirençlidir.
*   **Kayıpsızlık:** Integer Wavelet Transform sayesinde, damga eklenmemiş piksellerde bozulma minimumdur.
*   **Güvenlik:** QIM parametresi (T) bilinmeden damganın çıkarılması zordur.

## ⚠️ Notlar

*   Kodda `bit_sayisi` parametresi ile oynayarak dayanıklılık (robustness) ve görünmezlik (imperceptibility) arasındaki dengeyi ayarlayabilirsiniz.
*   JPEG formatında kaydederken veri kaybı olabileceği için uyarı verir, ancak bu yöntem JPEG'e karşı da belirli bir direnç gösterir.
