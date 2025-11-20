from pathlib import Path
from typing import Iterable, Optional

import cv2
import numpy as np


def load_image(path: str, resize_to: Optional[tuple[int, int]] = (224, 224)) -> np.ndarray:
    """Bir görüntü dosyasını okur ve isteğe bağlı olarak yeniden boyutlandırır."""
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Görüntü bulunamadı: {path}")

    if resize_to is not None:
        img = cv2.resize(img, resize_to)

    img = img.astype("float32") / 255.0
    return img


def load_images_from_dir(directory: str) -> Iterable[np.ndarray]:
    """Bir klasördeki tüm .jpg görüntüleri yükleyen basit yardımcı fonksiyon."""
    for img_path in Path(directory).glob("*.jpg"):
        yield load_image(str(img_path))
