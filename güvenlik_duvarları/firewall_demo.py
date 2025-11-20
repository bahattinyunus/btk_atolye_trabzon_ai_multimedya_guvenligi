"""Bu dosya, multimedya-guvenligi-ai projesindeki
`firewall_log_demo` modülünü kullanarak basit firewall log analizi
ve kural önerisi örneği çalıştırır.
"""

from __future__ import annotations

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROJECT_ROOT = os.path.join(REPO_ROOT, "multimedya-guvenligi-ai")
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")

if SRC_ROOT not in sys.path:
    sys.path.insert(0, SRC_ROOT)

from firewall.firewall_log_demo import demo  # type: ignore[import]


if __name__ == "__main__":
    demo()
