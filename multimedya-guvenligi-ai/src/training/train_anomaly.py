import numpy as np

from src.models.anomaly_detector import AnomalyDetector


def load_example_features() -> np.ndarray:
    """Örnek amaçlı sahte bir feature matrisi üretir."""
    return np.random.randn(1000, 10)


def main() -> None:
    X = load_example_features()
    model = AnomalyDetector(n_estimators=100, contamination=0.05)
    model.fit(X)
    preds = model.predict(X)
    print("Örnek anomali tespiti tamamlandı. Örnek çıktı:", preds[:10])


if __name__ == "__main__":
    main()
