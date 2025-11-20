"""Bu script, multimedya-guvenligi-ai projesindeki
train_deepfake modülünü çağırarak basit deepfake eğitim demosu çalıştırır.
"""

from __future__ import annotations

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROJECT_ROOT = os.path.join(REPO_ROOT, "multimedya-guvenligi-ai")
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")

if SRC_ROOT not in sys.path:
    sys.path.insert(0, SRC_ROOT)

from training.train_deepfake import train  # type: ignore[import]


if __name__ == "__main__":
    # Varsayılan parametrelerle kısa bir eğitim demosu
    train(num_epochs=1, batch_size=4, lr=1e-3)
