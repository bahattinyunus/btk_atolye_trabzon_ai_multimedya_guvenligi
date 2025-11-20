from typing import Tuple

from sklearn.metrics import accuracy_score, f1_score


def classification_metrics(y_true, y_pred) -> Tuple[float, float]:
    """Basit sınıflandırma metrikleri (accuracy ve F1)."""
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    return acc, f1
