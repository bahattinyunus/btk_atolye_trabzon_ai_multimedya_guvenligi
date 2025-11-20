"""Basit dijital imza (digital signature) demosu.

RSA anahtar çifti ile bir mesajın imzalanması ve imzanın doğrulanması
sürecini gösterir. Eğitim amaçlıdır.
"""

from __future__ import annotations

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_keypair(key_size: int = 2048):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
    public_key = private_key.public_key()
    return private_key, public_key


def sign_message(private_key, message: str) -> bytes:
    """Mesajın özetini alıp özel anahtarla imzalar."""

    return private_key.sign(
        message.encode("utf-8"),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )


def verify_signature(public_key, message: str, signature: bytes) -> bool:
    """İmzanın geçerli olup olmadığını kontrol eder."""

    try:
        public_key.verify(
            signature,
            message.encode("utf-8"),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )
        return True
    except Exception:
        return False


def demo() -> None:
    """Uçtan uca dijital imza demosu.

    Çalıştırmak için:
        python -m src.crypto.digital_signature_demo
    """

    private_key, public_key = generate_keypair()

    message = "Bu mesaj dijital olarak imzalanacaktır."
    print("Mesaj:", message)

    signature = sign_message(private_key, message)
    print("İmza (ilk 80 byte):", signature[:80], b"...")

    ok = verify_signature(public_key, message, signature)
    print("Doğrulama sonucu (doğru mesaj):", ok)

    tampered = message + " (degistirildi)"
    ok2 = verify_signature(public_key, tampered, signature)
    print("Doğrulama sonucu (değişmiş mesaj):", ok2)


if __name__ == "__main__":
    demo()
