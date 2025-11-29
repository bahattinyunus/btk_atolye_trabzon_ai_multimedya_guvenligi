from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import os
from skimage.metrics import structural_similarity as ssim


# =========================
# PSNR (host için)
# =========================
def mse(img1, img2):
    return np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)


def psnr(img1, img2):
    m = mse(img1, img2)
    if m == 0:
        return float("inf")
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(m))


# =========================
# 1D / 2D INTEGER HAAR IWT
# =========================

def fwd_haar_1d_int(signal):
    """Integer 1D Haar ileri dönüşüm (çift uzunluk gerekli)."""
    n = len(signal)
    assert n % 2 == 0
    s = np.zeros(n, dtype=int)
    half = n // 2
    for i in range(half):
        s0 = int(signal[2 * i])
        s1 = int(signal[2 * i + 1])
        d = s1 - s0
        a = s0 + (d >> 1)      # integer ortalama
        s[i] = a               # low (approx)
        s[half + i] = d        # high (detail)
    return s

def inv_haar_1d_int(coeffs):
    """Integer 1D Haar ters dönüşüm (çift uzunluk gerekli)."""
    n = len(coeffs)
    assert n % 2 == 0
    out = np.zeros(n, dtype=int)
    half = n // 2
    for i in range(half):
        a = int(coeffs[i])
        d = int(coeffs[half + i])
        s0 = a - (d >> 1)
        s1 = d + s0
        out[2 * i] = s0
        out[2 * i + 1] = s1
    return out

def fwd_haar_2d_int(block4x4):
    """4x4 blok için 2D integer Haar ileri dönüşüm."""
    assert block4x4.shape == (4, 4)
    tmp = np.zeros_like(block4x4, dtype=int)

    # satırlarda 1D
    for r in range(4):
        tmp[r, :] = fwd_haar_1d_int(block4x4[r, :])

    # sütunlarda 1D
    out = np.zeros_like(block4x4, dtype=int)
    for c in range(4):
        out[:, c] = fwd_haar_1d_int(tmp[:, c])

    return out

def inv_haar_2d_int(coeff4x4):
    """4x4 blok için 2D integer Haar ters dönüşüm."""
    assert coeff4x4.shape == (4, 4)
    tmp = np.zeros_like(coeff4x4, dtype=int)

    # sütunlarda ters 1D
    for c in range(4):
        tmp[:, c] = inv_haar_1d_int(coeff4x4[:, c])

    # satırlarda ters 1D
    out = np.zeros_like(coeff4x4, dtype=int)
    for r in range(4):
        out[r] = inv_haar_1d_int(tmp[r, :])

    return out


# ============================================
# DAMGA EKLEME: 4x4 IWT + LL bandı QIM gömme
# ============================================

def damga_ekle_iwt4x4(kaynak_yol, watermark_yol, cikti_yol, bit_sayisi=1):
    """
    kaynak_yol    : Kaynak görüntü (png/jpg olabilir)
    watermark_yol : Gri/binary watermark
    cikti_yol     : Damgalı görüntünün kaydedileceği yol
    bit_sayisi    : Gömme kuvvet seviyesi (1..4) -> T = 2^(bit_sayisi+1)
                    (T büyüdükçe daha robust, ama PSNR biraz düşer)
    """
    if bit_sayisi < 1 or bit_sayisi > 4:
        raise ValueError("bit_sayisi 1-4 arasında olmalı (QIM kuvvet seviyesi).")

    # QIM kuantizasyon adımı
    T = 2 ** (bit_sayisi + 1)  # 1->4, 2->8, 3->16, 4->32

    # Çıktı formatı kontrolü (JPG kayıplı)
    root, ext = os.path.splitext(cikti_yol)
    if ext.lower() in [".jpg", ".jpeg"]:
        print("[UYARI] Stego'yu JPG kaydediyorsun (kayıplı). Watermark bozulabilir.")
    # PNG için ekstra bir şey yapmıyoruz, kayıpsız.

    # Görselleri yükle ve gri seviye (L) yap
    host_img = Image.open(kaynak_yol).convert("L")
    wm_img = Image.open(watermark_yol).convert("L")

    host = np.array(host_img, dtype=np.int32)
    wm_gray = np.array(wm_img, dtype=np.uint8)

    H, W = host.shape

    # Host'un 4x4 bloklara tam bölünebilen kısmını kullan
    H4 = (H // 4) * 4
    W4 = (W // 4) * 4
    if H4 == 0 or W4 == 0:
        raise ValueError("Görüntü boyutları 4x4 bloklara bölünebilmeli (en az 4x4).")

    # Kapasite: her blokta LL bandında 2x2=4 katsayı -> 4 bit
    blok_sayisi = (H4 // 4) * (W4 // 4)
    kapasite_bit = blok_sayisi * 4

    # Watermark bitleri (binary)
    wm_bits = (wm_gray > 127).astype(np.uint8).flatten()  # 0/1
    toplam_wm_bit = len(wm_bits)
    max_kullanilacak = min(toplam_wm_bit, kapasite_bit)

    host_stego = host.copy()

    bit_index = 0

    # 4x4 bloklar üzerinde dolaş
    for by in range(0, H4, 4):
        for bx in range(0, W4, 4):
            if bit_index >= max_kullanilacak:
                break

            blok = host[by:by+4, bx:bx+4]
            coeff = fwd_haar_2d_int(blok)

            # LL bandı: coeff[0:2, 0:2] -> 2x2 = 4 katsayı
            for iy in range(2):
                for ix in range(2):
                    if bit_index >= max_kullanilacak:
                        break

                    c = int(coeff[iy, ix])
                    bit = int(wm_bits[bit_index])  # 0 veya 1

                    # ----- QIM tabanlı gömme -----
                    q = c // T  # bölge indeksi (integer division, negatifleri de idare eder)
                    if (q & 1) != bit:
                        # parite uymuyorsa, en yakın doğru bölgeye kaydır
                        q = q + 1 if q >= 0 else q - 1
                    c_new = q * T
                    coeff[iy, ix] = c_new
                    # -----------------------------

                    bit_index += 1

            # Ters IWT ile damgalı blok
            stego_blok = inv_haar_2d_int(coeff)

            # [0,255] aralığına kliple ve host_stego'ya yaz
            stego_blok = np.clip(stego_blok, 0, 255)
            host_stego[by:by+4, bx:bx+4] = stego_blok

        if bit_index >= max_kullanilacak:
            break

    # PSNR için orijinal host'u uint8'e çevir
    host_uint8 = np.clip(host, 0, 255).astype(np.uint8)
    host_stego_uint8 = host_stego.astype(np.uint8)

    # Damgalı görüntüyü kaydet
    stego_img = Image.fromarray(host_stego_uint8, mode="L")
    stego_img.save(cikti_yol)
    print(f"Damga eklendi. Kullanılan watermark bit sayısı: {bit_index}/{toplam_wm_bit}, çıktı: {cikti_yol}")

    # Host vs stego PSNR
    psnr_val = psnr(host_uint8, host_stego_uint8)

    # Görselleştirme
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(host_uint8, cmap="gray")
    plt.title("Orijinal Host")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(host_stego_uint8, cmap="gray")
    plt.title(f"Damgalı Host (QIM)\nPSNR = {psnr_val:.2f} dB")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


# ==================================================
# DAMGA ÇIKARMA: 4x4 IWT + LL QIM'den bit okuma + SSIM
# ==================================================

def damga_cikar_iwt4x4(stego_yol, watermark_yol,
                        wm_genislik, wm_yukseklik,
                        cikti_wm_yol, bit_sayisi=1):
    """
    stego_yol     : Damgalı görüntü dosyası
    watermark_yol : Orijinal watermark görüntü yolu (gri/binary)
    wm_genislik   : Orijinal watermark genişliği (piksel)
    wm_yukseklik  : Orijinal watermark yüksekliği (piksel)
    cikti_wm_yol  : Çıkarılan watermark'ın kaydedileceği yol
    bit_sayisi    : Gömmede kullanılan QIM seviyesi (aynı olmalı!)
    """
    if bit_sayisi < 1 or bit_sayisi > 4:
        raise ValueError("bit_sayisi 1-4 arasında olmalı (QIM seviyesi).")

    # QIM adımı (embed ile aynı olmalı)
    T = 2 ** (bit_sayisi + 1)

    stego_img = Image.open(stego_yol).convert("L")
    stego = np.array(stego_img, dtype=np.int32)

    H, W = stego.shape
    H4 = (H // 4) * 4
    W4 = (W // 4) * 4

    if H4 == 0 or W4 == 0:
        raise ValueError("Görüntü boyutları 4x4 bloklara bölünebilmeli.")

    hedef_bit_sayisi = wm_genislik * wm_yukseklik
    wm_bits = []

    # 4x4 bloklar üzerinde aynı sırayla dolaş
    for by in range(0, H4, 4):
        for bx in range(0, W4, 4):
            if len(wm_bits) >= hedef_bit_sayisi:
                break

            blok = stego[by:by+4, bx:bx+4]
            coeff = fwd_haar_2d_int(blok)

            # LL bandı: 2x2
            for iy in range(2):
                for ix in range(2):
                    if len(wm_bits) >= hedef_bit_sayisi:
                        break

                    c = int(coeff[iy, ix])

                    # ----- QIM tabanlı bit okuma -----
                    q = c // T
                    bit = q & 1
                    # -------------------------------
                    wm_bits.append(bit)

        if len(wm_bits) >= hedef_bit_sayisi:
            break

    # Eksik kalırsa kalanları 0 doldur (çok gerekmez ama güvenlik)
    if len(wm_bits) < hedef_bit_sayisi:
        wm_bits.extend([0] * (hedef_bit_sayisi - len(wm_bits)))

    wm_bits_arr = np.array(wm_bits, dtype=np.uint8)
    wm_pixels = (wm_bits_arr * 255).astype(np.uint8)
    wm_img_arr = wm_pixels.reshape(wm_yukseklik, wm_genislik)

    wm_img = Image.fromarray(wm_img_arr, mode="L")
    wm_img.save(cikti_wm_yol)
    print(f"Damga çıkarıldı. Çıktı watermark kaydedildi: {cikti_wm_yol}")

    # ---- SSIM hesapla (orijinal watermark da binary'e çekilerek) ----
    orj_wm_img = Image.open(watermark_yol).convert("L")
    orj_wm_gray = np.array(orj_wm_img.resize((wm_genislik, wm_yukseklik)), dtype=np.uint8)
    orj_wm_bin = (orj_wm_gray > 127).astype(np.uint8) * 255

    ssim_val = ssim(orj_wm_bin, wm_img_arr, data_range=255)

    # Görselleştirme
    plt.figure(figsize=(10, 5))
    plt.suptitle(f"SSIM = {ssim_val:.4f}", fontsize=14)

    plt.subplot(1, 2, 1)
    plt.imshow(orj_wm_bin, cmap="gray")
    plt.title("Orijinal (Binary) Watermark")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(wm_img_arr, cmap="gray")
    plt.title("Çıkarılan Watermark (QIM)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


# =====================
# ÖRNEK KULLANIM
# =====================
if __name__ == "__main__":
    # 1) Damga ekle (host png/jpg olabilir)
    damga_ekle_iwt4x4(
        kaynak_yol="../veriler/ai_content.png",
        watermark_yol="../veriler/gan_face_256.png",
        cikti_yol="../veriler/watermarked_pro.png",
        bit_sayisi=2   # QIM kuvveti (T=8)
    )

    # Burada istersen "../veriler/watermarked_pro.png" dosyasını elle JPG'e çevirip
    # dayanıklılık test edebilirsin.

    # 2) Damga çıkar + SSIM (stego PNG veya sıkıştırılmış JPG olabilir)
    damga_cikar_iwt4x4(
        stego_yol="../veriler/watermarked_pro.png",   # veya "../veriler/watermarked_pro.jpg" (JPEG test)
        watermark_yol="../veriler/gan_face_256.png",
        wm_genislik=256,
        wm_yukseklik=256,
        cikti_wm_yol="../veriler/extracted_watermark_pro.png",
        bit_sayisi=2
    )
