import numpy as np

from src.models.anomaly_detector import AnomalyDetector


def main() -> None:
    X = np.random.randn(20, 10)
    model = AnomalyDetector()
    model.fit(X)
    preds = model.predict(X)
    print("Tahminler:", preds)


if __name__ == "__main__":
    main()
