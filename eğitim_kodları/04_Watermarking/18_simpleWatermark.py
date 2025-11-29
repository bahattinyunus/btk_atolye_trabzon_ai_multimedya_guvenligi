from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
from skimage.metrics import structural_similarity as ssim


# ===========================
# MSE & PSNR HESABI
# (MSE sadece PSNR için kullanılıyor, RMSE artık yok)
# ===========================
def mse(img1, img2):
    return np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)


def psnr(img1, img2):
    """0-255 aralığında iki görüntü için PSNR hesaplama"""
    m = mse(img1, img2)
    if m == 0:
        return float("inf")
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(m))


# ===========================
# DAMGA EKLEME
# ===========================
def damga_ekle(kaynak_yol, watermark_yol, cikti_yol, bit_sayisi=1):
    if bit_sayisi < 1 or bit_sayisi > 7:
        raise ValueError("bit_sayisi 1 ile 7 arasında olmalıdır.")

    # Görselleri yükle ve gri seviye yap
    kaynak_img = Image.open(kaynak_yol).convert("L")
    wm_img = Image.open(watermark_yol).convert("L")

    kaynak = np.array(kaynak_img, dtype=np.uint8)
    wm = np.array(wm_img, dtype=np.uint8)

    h_k, w_k = kaynak.shape
    h_w, w_w = wm.shape

    # Watermark’ı binary’e çevir
    wm_bits = (wm > 127).astype(np.uint8)
    wm_flat = wm_bits.flatten()

    # Kaynağı düzleştir
    kaynak_flat = kaynak.flatten()
    src_n = len(kaynak_flat)
    wm_n = len(wm_flat)

    if wm_n > src_n:
        raise ValueError("Watermark piksel sayısı, kaynak görüntüden fazla olamaz.")

    # Bit temizleme maskesi
    clear_mask = 0xFF ^ ((1 << bit_sayisi) - 1)

    # Damga işlemi
    for i in range(wm_n):
        bit = wm_flat[i]
        p = kaynak_flat[i] & clear_mask
        p = p | (bit * ((1 << bit_sayisi) - 1))
        kaynak_flat[i] = p

    # Eski haline getir
    stego = kaynak_flat.reshape(h_k, w_k).astype(np.uint8)

    # Kaydet
    stego_img = Image.fromarray(stego, mode="L")
    stego_img.save(cikti_yol)

    print(f"Damga eklendi → {cikti_yol}")

    # PSNR hesapla
    psnr_degeri = psnr(kaynak, stego)

    # Plotla
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(kaynak, cmap="gray")
    plt.title("Orijinal Görüntü")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(stego, cmap="gray")
    plt.title(f"Damgalı Görüntü\nPSNR = {psnr_degeri:.2f} dB")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


# ===========================
# DAMGA ÇIKARMA + KARŞILAŞTIRMA (SSIM)
# ===========================
def damga_cikar(
        stego_yol,
        watermark_yol,
        wm_genislik,
        wm_yukseklik,
        cikti_wm_yol,
        bit_sayisi=1):

    """
    stego_yol: Damgalı görüntü
    watermark_yol: ORİJİNAL watermark görüntüsü yolu
    wm_genislik, wm_yukseklik: watermark boyutu
    cikti_wm_yol: çıkarılan watermark kaydedileceği yol
    """

    if bit_sayisi < 1 or bit_sayisi > 7:
        raise ValueError("bit_sayisi 1-7 arasında olmalıdır.")

    # 1) Stego yükle
    stego_img = Image.open(stego_yol).convert("L")
    stego = np.array(stego_img, dtype=np.uint8)

    # 2) Orijinal watermark yükle
    orj_wm_img = Image.open(watermark_yol).convert("L")
    orj_wm = np.array(orj_wm_img.resize((wm_genislik, wm_yukseklik)), dtype=np.uint8)

    wm_n = wm_genislik * wm_yukseklik
    stego_flat = stego.flatten()

    if wm_n > len(stego_flat):
        raise ValueError("Watermark boyutu stego görüntüsünden büyük!")

    # LSB maskesi
    lsb_mask = (1 << bit_sayisi) - 1

    wm_bits_flat = np.zeros(wm_n, dtype=np.uint8)

    # 3) LSB bitlerini oku
    for i in range(wm_n):
        val = stego_flat[i] & lsb_mask
        wm_bits_flat[i] = 1 if val > 0 else 0

    # 4) Binary → görüntü
    wm_pixels = (wm_bits_flat * 255).astype(np.uint8)
    wm_img_arr = wm_pixels.reshape(wm_yukseklik, wm_genislik)

    # 5) Çıkarılan watermark'ı kaydet
    wm_img = Image.fromarray(wm_img_arr, mode="L")
    wm_img.save(cikti_wm_yol)

    print(f"Damga çıkarıldı → {cikti_wm_yol}")

    # 6) SSIM hesapla
    ssim_degeri = ssim(orj_wm, wm_img_arr, data_range=255)

    # 7) Orijinal ve çıkarılmış watermark'ı yan yana plotla
    plt.figure(figsize=(10, 5))

    plt.suptitle(f"SSIM = {ssim_degeri:.4f}", fontsize=14)

    plt.subplot(1, 2, 1)
    plt.imshow(orj_wm, cmap="gray")
    plt.title("Orijinal Watermark")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(wm_img_arr, cmap="gray")
    plt.title("Çıkarılan Watermark")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


# ===========================
# ÖRNEK KULLANIM
# ===========================
if __name__ == "__main__":
    # Damga ekle
    damga_ekle(
        kaynak_yol="../veriler/ai_content.png",
        watermark_yol="../veriler/gan_face_256.png",
        cikti_yol="../veriler/watermarked_content.png",
        bit_sayisi=1
    )

    # Damga çıkar
    damga_cikar(
        stego_yol="../veriler/watermarked_content.png",
        watermark_yol="../veriler/gan_face_256.png",
        wm_genislik=256,
        wm_yukseklik=256,
        cikti_wm_yol="../veriler/extracted_watermark.png",
        bit_sayisi=1
    )
