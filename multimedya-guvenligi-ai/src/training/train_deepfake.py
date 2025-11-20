import torch
from torch.utils.data import DataLoader, Dataset

from src.models.deepfake_detector import SimpleDeepfakeCNN


class DummyFramesDataset(Dataset):
    """Örnek amaçlı sahte bir dataset.

    Gerçekte burada frame klasörlerinden görüntü okuyup gerçek etiketler
    döneceksin. Şimdilik modelin derlenip çalıştığını göstermek için
    rastgele tensörler ve etiketler üretiyoruz.
    """

    def __len__(self) -> int:
        return 100

    def __getitem__(self, idx):
        # Sahte bir 3x224x224 görüntü ve 0/1 etiket üret
        x = torch.rand(3, 224, 224)
        y = torch.randint(0, 2, (1,), dtype=torch.float32)
        return x, y


def train(num_epochs: int = 1, batch_size: int = 4, lr: float = 1e-3) -> None:
    """Deepfake CNN modelinin eğitimi için minimal örnek döngü."""

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    dataset = DummyFramesDataset()
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = SimpleDeepfakeCNN().to(device)
    criterion = torch.nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0
        for inputs, targets in dataloader:
            inputs = inputs.to(device)
            targets = targets.to(device).view(-1, 1)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * inputs.size(0)

        epoch_loss = running_loss / len(dataset)
        print(f"Epoch {epoch + 1}/{num_epochs} - Loss: {epoch_loss:.4f}")


if __name__ == "__main__":
    train()
