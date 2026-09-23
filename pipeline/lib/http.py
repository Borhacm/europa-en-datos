"""Descargas con caché en disco (data/raw), para no castigar las APIs en cada ejecución."""

import hashlib
import time
import urllib.request
from pathlib import Path

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
REFRESH = False  # run.py lo activa con --refresh


def fetch(url: str, suffix: str = "", headers: dict | None = None, retries: int = 3) -> Path:
    """Devuelve la ruta local del recurso, descargándolo si no está en caché."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / (hashlib.sha1(url.encode()).hexdigest()[:16] + suffix)
    if path.exists() and not REFRESH:
        return path

    req = urllib.request.Request(url, headers={"User-Agent": "europa-en-datos/0.1", **(headers or {})})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                path.write_bytes(resp.read())
            return path
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))
    return path
