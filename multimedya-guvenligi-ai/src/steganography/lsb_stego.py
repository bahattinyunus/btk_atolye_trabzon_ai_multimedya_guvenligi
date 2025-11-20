"""Basit LSB (Least Significant Bit) görüntü stenografisi örneği.

Bu modül, bir PNG/JPEG görüntüsü içine kısa bir metin mesajı gömme
ve mesajı geri okuma işlevlerini gösterir.

Not: Eğitim/demonstrasyon amaçlıdır; gerçek saldırı/savunma ortamları için
optimizasyon ve ek güvenlik kontrolleri gerekir.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import cv2
import numpy as np


def _text_to_bits(text: str) -> Iterable[int]:
    data = text.encode("utf-8")
    for byte in data:
        for i in range(8):
            yield (byte >> (7 - i)) & 1


def _bits_to_text(bits: Iterable[int]) -> str:
    bits_list = list(bits)
    bytes_out = []
    for i in range(0, len(bits_list), 8):
        byte_bits = bits_list[i : i + 8]
        if len(byte_bits) < 8:
            break
        value = 0
        for b in byte_bits:
            value = (value << 1) | b
        bytes_out.append(value)
    return bytes(bytes_out).decode("utf-8", errors="ignore")


def hide_message(input_image: str, output_image: str, message: str) -> None:
    """Bir görüntünün en düşük bitlerine metin mesajı gömer.

    Mesajın sonuna sonlandırma için özel bir bit dizisi eklenir.
    """

    img = cv2.imread(input_image)
    if img is None:
        raise FileNotFoundError(f"Girdi görüntüsü bulunamadı: {input_image}")

    # BGR -> tek kanal vektör
    h, w, c = img.shape
    total_bits = h * w * c

    # Mesaj + bit sonlandırma işareti
    terminator = "<END>"
    full_message = message + terminator
    msg_bits = list(_text_to_bits(full_message))

    if len(msg_bits) > total_bits:
        raise ValueError("Mesaj bu görüntüye sığmayacak kadar uzun.")

    flat = img.flatten()

    for i, bit in enumerate(msg_bits):
        flat[i] = (flat[i] & ~1) | bit

    stego = flat.reshape((h, w, c))
    cv2.imwrite(output_image, stego)


def reveal_message(stego_image: str) -> str:
    """LSB ile gizlenmiş mesajı çözmeye çalışır."""

    img = cv2.imread(stego_image)
    if img is None:
        raise FileNotFoundError(f"Stego görüntü bulunamadı: {stego_image}")

    h, w, c = img.shape
    flat = img.flatten()

    bits = [int(px & 1) for px in flat]
    text = _bits_to_text(bits)

    terminator = "<END>"
    if terminator in text:
        return text.split(terminator, 1)[0]
    return text


def demo() -> None:
    """Basit uçtan uca demo: örnek bir görüntüye mesaj gizle ve geri oku.

    Kullanım:
        python -m src.steganography.lsb_stego
    """

    in_path = Path("data/images/example_input.png")
    out_path = Path("data/images/example_stego.png")

    if not in_path.exists():
        raise FileNotFoundError(
            f"Demo için {in_path} altında bir görüntü bekleniyor. "
            "Lütfen küçük bir PNG/JPEG koy ve tekrar dene."
        )

    msg = "Merhaba, bu bir LSB demo mesajıdır."
    hide_message(str(in_path), str(out_path), msg)
    print("Mesaj gizlendi, stego görüntü kaydedildi:", out_path)

    recovered = reveal_message(str(out_path))
    print("Çözülen mesaj:", recovered)


if __name__ == "__main__":
    demo()
