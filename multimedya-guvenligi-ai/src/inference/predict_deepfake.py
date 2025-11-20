import torch

from src.models.deepfake_detector import SimpleDeepfakeCNN


def predict_video(video_path: str | None = None, model_path: str | None = None) -> None:
    """Bir video için deepfake tahmini yapan örnek fonksiyon.

    Gerçek senaryoda:
      - video_path içinden frame çıkarılır,
      - model_path'ten ağırlıklar yüklenir,
      - frame'ler modele verilerek skor üretilir.

    Şimdilik sadece rastgele bir örnek görüntü ile
    modelin ileri yayılımını çalıştırıp skor basıyoruz.
    """

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = SimpleDeepfakeCNN().to(device)
    model.eval()

    # Sahte bir 1x3x224x224 giriş tensörü üret
    x = torch.rand(1, 3, 224, 224, device=device)

    with torch.no_grad():
        score = model(x).item()

    print("Dummy deepfake skoru (0=real, 1=fake'e yakın):", score)


if __name__ == "__main__":
    predict_video()
