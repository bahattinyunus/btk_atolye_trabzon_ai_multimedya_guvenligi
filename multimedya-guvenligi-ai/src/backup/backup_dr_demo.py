"""Basit yedekleme ve felaket kurtarma (Backup & DR) demosu.

Bu modül, küçük bir "veri" kümesi üzerinde:
- 3-2-1 kuralına uygun mantıksal yedek kopyaları üretir,
- Basit bir RPO / RTO senaryosu simüle eder,
- Ransomware benzeri bir felaket sonrası hangi yedekten
  dönülebileceğini örnek olarak gösterir.

Eğitim amaçlıdır; gerçek sistemlere doğrudan uygulanmamalıdır.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List


@dataclass
class BackupSnapshot:
    name: str
    timestamp: datetime
    location: str  # local / remote / cloud
    data_version: int


def create_backup_plan() -> List[BackupSnapshot]:
    """Örnek bir 3-2-1 yedekleme planı üretir."""

    base_time = datetime(2025, 1, 1, 10, 0, 0)

    snapshots: List[BackupSnapshot] = [
        BackupSnapshot("full_local_day0", base_time, "local_disk", 1),
        BackupSnapshot("inc_local_day1", base_time + timedelta(days=1), "local_disk", 2),
        BackupSnapshot("inc_local_day2", base_time + timedelta(days=2), "local_disk", 3),
        BackupSnapshot("full_remote_day0", base_time, "remote_site", 1),
        BackupSnapshot("full_cloud_day0", base_time, "cloud", 1),
    ]
    return snapshots


def simulate_ransomware_attack(current_version: int) -> None:
    print("\n[!] Ransomware saldırısı simüle ediliyor...")
    print(f"    Üretimdeki veri versiyonu: v{current_version}")
    print("    Tüm yerel disk verisi şifrelendi ve kullanılamaz durumda.")


def find_recovery_point(snapshots: List[BackupSnapshot], max_data_loss_versions: int) -> BackupSnapshot | None:
    """Basit bir RPO mantığı ile en uygun snapshot'ı seçer.

    max_data_loss_versions: En fazla kaç versiyon veri kaybı tolere edilebilir.
    """

    latest_version = max(s.data_version for s in snapshots)
    allowed_min_version = latest_version - max_data_loss_versions

    candidates = [s for s in snapshots if s.data_version >= allowed_min_version]
    if not candidates:
        return None

    # Zaman olarak en yeni snapshot'ı seç
    return sorted(candidates, key=lambda s: s.timestamp, reverse=True)[0]


def demo() -> None:
    """Uçtan uca backup + DR senaryosu demosu.

    Çalıştırmak için:
        python -m src.backup.backup_dr_demo
    """

    print("[+] Örnek yedekleme planı (3-2-1 mantığı ile):")
    snapshots = create_backup_plan()
    for s in snapshots:
        print(f"  - {s.name:18s} | versiyon=v{s.data_version} | konum={s.location:11s} | zaman={s.timestamp}")

    current_version = 3
    simulate_ransomware_attack(current_version)

    max_loss = 1
    print(f"\n[+] RPO politikası: En fazla {max_loss} versiyon veri kaybı tolere edilebilir.")
    rp = find_recovery_point(snapshots, max_loss)

    if rp is None:
        print("[-] Uygun bir yedek bulunamadı! RPO hedefi karşılanamıyor.")
        return

    lost_versions = current_version - rp.data_version
    print("\n[+] Önerilen geri dönüş noktası (Recovery Point):")
    print(f"    Snapshot: {rp.name}")
    print(f"    Konum   : {rp.location}")
    print(f"    Zaman   : {rp.timestamp}")
    print(f"    Veri versiyonu: v{rp.data_version} (kayıp: {lost_versions} versiyon)")

    print("\n[+] Özet:")
    print("    - Ransomware sonrası tüm yerel veri kaybedildi.")
    print(f"    - Offsite/cloud yedek sayesinde v{rp.data_version} seviyesine dönüş yapılabildi.")
    print(f"    - Toplam veri kaybı {lost_versions} versiyon; bu, RPO hedefi ile uyumlu.")


if __name__ == "__main__":
    demo()
