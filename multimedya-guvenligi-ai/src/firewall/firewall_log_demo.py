"""Basit firewall log analizi ve kural simülasyonu demosu.

Bu modül, örnek bir firewall log listesini analiz ederek:
- En çok denenen portları,
- Hangi IP'lerin sürekli engellendiğini,
- Önerilebilecek basit bir kural listesini
çıkarır.

Eğitim amaçlıdır.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class FirewallLogEntry:
    src_ip: str
    dst_ip: str
    dst_port: int
    action: str  # ALLOW / DENY / DROP
    proto: str = "tcp"


def sample_logs() -> List[FirewallLogEntry]:
    """Örnek firewall logları üretir."""

    data = [
        FirewallLogEntry("185.204.2.50", "10.0.0.5", 22, "DENY"),
        FirewallLogEntry("185.204.2.50", "10.0.0.5", 22, "DENY"),
        FirewallLogEntry("185.204.2.50", "10.0.0.5", 80, "DENY"),
        FirewallLogEntry("203.0.113.10", "10.0.0.10", 3389, "DENY"),
        FirewallLogEntry("203.0.113.10", "10.0.0.10", 3389, "DENY"),
        FirewallLogEntry("192.168.1.20", "10.0.0.20", 443, "ALLOW"),
        FirewallLogEntry("192.168.1.20", "10.0.0.21", 443, "ALLOW"),
        FirewallLogEntry("198.51.100.77", "10.0.0.5", 22, "DENY"),
    ]
    return data


def analyze_logs(entries: Iterable[FirewallLogEntry]) -> None:
    """Basit istatistikler çıkarır ve örnek kurallar önerir."""

    entries = list(entries)
    print(f"Toplam log kaydı: {len(entries)}")

    denied = [e for e in entries if e.action != "ALLOW"]
    print(f"ENGELLENEN trafik sayısı: {len(denied)}")

    port_counts = Counter(e.dst_port for e in denied)
    ip_counts = Counter(e.src_ip for e in denied)

    print("\nEn çok hedeflenen portlar (DENY/DROP):")
    for port, count in port_counts.most_common():
        print(f"  Port {port}: {count} deneme")

    print("\nEn çok engellenen kaynak IP'ler:")
    for ip, count in ip_counts.most_common():
        print(f"  {ip}: {count} deneme")

    print("\nÖrnek kural önerileri:")
    # Örnek: 22 numaralı port için çok fazla başarısız deneme
    if port_counts.get(22, 0) >= 3:
        print("- SSH (22/tcp) için sadece belirli yönetim IP'lerine izin ver, diğerlerini engelle.")
    if port_counts.get(3389, 0) >= 2:
        print("- RDP (3389/tcp) portunu mümkünse kapat veya sadece VPN içinden erişime aç.")
    if ip_counts:
        top_ip, top_count = ip_counts.most_common(1)[0]
        if top_count >= 3:
            print(f"- {top_ip} IP adresini geçici olarak blacklist'e almayı düşünebilirsin.")


def demo() -> None:
    """Uçtan uca firewall log analizi demosu.

    Çalıştırmak için:
        python -m src.firewall.firewall_log_demo
    """

    logs = sample_logs()
    analyze_logs(logs)


if __name__ == "__main__":
    demo()
