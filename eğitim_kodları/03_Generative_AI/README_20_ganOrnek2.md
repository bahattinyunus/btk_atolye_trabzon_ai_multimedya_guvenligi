# 20. Yüksek Çözünürlüklü Stil Transferi (Neural Style Transfer)

Bu kod, **VGG19** ön eğitimli modelini kullanarak bir içerik (content) görüntüsüne başka bir görüntünün stilini (style) aktarır. `13_ganOrnek.py`'den farklı olarak, bu kod **optimizasyon tabanlı** bir yaklaşım kullanır ve daha yüksek çözünürlüklü sonuçlar üretebilir.

## 📝 Kod Ne Yapıyor?

1.  **Görüntü Yükleme:** İçerik ve stil görüntülerini yükler ve tensöre çevirir.
2.  **Model Hazırlığı:** VGG19 modelinin öznitelik katmanlarını kullanır.
3.  **Kayıp Fonksiyonları (Loss Functions):**
    *   **Content Loss:** İçerik görüntüsünün ana hatlarını korumak için.
    *   **Style Loss:** Stil görüntüsünün dokusunu ve renklerini transfer etmek için (Gram Matrisi kullanarak).
4.  **Optimizasyon:** LBFGS optimizasyon algoritması ile giriş görüntüsünü (başlangıçta içerik görüntüsü) iteratif olarak günceller.
5.  **Sonuç:** Hem içeriği koruyan hem de stil görüntüsünün sanatsal özelliklerini taşıyan yeni bir görüntü oluşturur.

## 🛠️ Kurulum

Gerekli kütüphaneler:

```bash
pip install torch torchvision Pillow matplotlib
```

## ▶️ Kullanım

Kodu çalıştırmak için:

```bash
python 20_ganOrnek2.py
```

Kod, `../veriler/ai_content.png` ve `../veriler/ai_style.png` dosyalarını kullanır ve sonucu `../veriler/output_hd.jpg` olarak kaydeder.

## ⚙️ Ayarlar

Kod içerisindeki şu değişkenlerle oynayabilirsiniz:

*   `IMSIZE`: Çıktı çözünürlüğü (Örn: 512, 1024). Yüksek değerler daha fazla bellek (VRAM) ve zaman gerektirir.
*   `NUM_STEPS`: Optimizasyon adım sayısı. Arttıkça kalite artabilir ama süre uzar.
*   `STYLE_WEIGHT` / `CONTENT_WEIGHT`: Stil ve içerik arasındaki dengeyi ayarlar.

## ⚠️ Notlar

*   Bu işlem CPU üzerinde yavaş çalışabilir. Mümkünse GPU (CUDA) kullanılması önerilir.
*   1024px gibi yüksek çözünürlükler için en az 8GB+ VRAM gerekebilir. Hata alırsanız `IMSIZE` değerini düşürün (örn: 512).
