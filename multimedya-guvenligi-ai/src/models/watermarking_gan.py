import torch.nn as nn
import torch.nn.functional as F


class WatermarkGenerator(nn.Module):
    """Görseller üzerine basit bir filigran eklemek için örnek Generator.

    Girdi: (B, 3, H, W) orijinal görüntü
    Çıktı: (B, 3, H, W) filigranlı görüntü

    Not: Bu, eğitim için basit bir örnek mimaridir; gerçek projede
    daha güçlü ve kararlı bir mimari kullanmak gerekebilir.
    """

    def __init__(self) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 32, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(32, 3, kernel_size=1)

    def forward(self, x):
        residual = x
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.conv3(x)
        # Orijinal görüntüye küçük bir pertürbasyon ekleyerek filigranlı çıktı üret
        out = residual + 0.1 * x
        return out


class WatermarkDiscriminator(nn.Module):
    """Filigranlı ve normal görüntüleri ayırt etmek için basit Discriminator.

    Girdi: (B, 3, H, W)
    Çıktı: (B, 1) -> gerçek (1) / sahte (0) skoru
    """

    def __init__(self) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 56 * 56, 64)
        self.fc2 = nn.Linear(64, 1)

    def forward(self, x):
        x = self.pool(F.leaky_relu(self.conv1(x), 0.2))
        x = self.pool(F.leaky_relu(self.conv2(x), 0.2))
        x = x.view(x.size(0), -1)
        x = F.leaky_relu(self.fc1(x), 0.2)
        x = self.fc2(x)
        return x
