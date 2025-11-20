from pathlib import Path


def ensure_dir(path: str | Path) -> None:
    """Verilen klasör yoksa oluşturur."""
    Path(path).mkdir(parents=True, exist_ok=True)
