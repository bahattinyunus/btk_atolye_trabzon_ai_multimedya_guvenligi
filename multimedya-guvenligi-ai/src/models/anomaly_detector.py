from typing import Any

import numpy as np
from sklearn.ensemble import IsolationForest


class AnomalyDetector:
    """Basit bir Isolation Forest tabanlı anomali tespit sınıfı iskeleti."""

    def __init__(self, **kwargs: Any) -> None:
        self.model = IsolationForest(**kwargs)

    def fit(self, X: np.ndarray) -> None:
        self.model.fit(X)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Çıktı: 1 (normal), -1 (anomali)"""
        return self.model.predict(X)
