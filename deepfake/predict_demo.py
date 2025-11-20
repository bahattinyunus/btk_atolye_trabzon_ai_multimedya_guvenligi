"""Bu script, multimedya-guvenligi-ai projesindeki
predict_deepfake modülünü çağırarak basit bir tahmin demosu çalıştırır.
"""

from __future__ import annotations

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROJECT_ROOT = os.path.join(REPO_ROOT, "multimedya-guvenligi-ai")
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")

if SRC_ROOT not in sys.path:
    sys.path.insert(0, SRC_ROOT)

from inference.predict_deepfake import predict_video  # type: ignore[import]


if __name__ == "__main__":
    # Şu an predict_video rastgele bir tensör ile dummy skor üretiyor.
    predict_video()
