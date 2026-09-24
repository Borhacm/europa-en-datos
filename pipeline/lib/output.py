"""Formato común de salida: un JSON por gráfico en data/charts."""

import datetime as dt
import json
import math
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
CHARTS_DIR = DATA_DIR / "charts"

LENSES = {
    "gigantes": {"es": "Entre dos gigantes", "en": "Between two giants"},
    "elige": {"es": "¿Pierde Europa o elige?", "en": "Is Europe losing, or choosing?"},
    "dentro": {"es": "Europa por dentro", "en": "Europe from within"},
}
# Se rellena al importar charts/: cada paquete de tema declara su THEME
THEMES: dict[str, dict] = {}


def chart(*, id, lens, theme, title, subtitle, unit, source, rows, geos=None, notes=None, extra=None) -> dict:
    """Valida y empaqueta un gráfico. `rows` es una lista de observaciones con al menos 'value'."""
    assert lens in LENSES and theme in THEMES, id
    assert rows, f"{id}: sin datos"
    for r in rows:
        v = r["value"]
        assert isinstance(v, (int, float)) and not math.isnan(v), f"{id}: valor no numérico {r}"
    return {
        "id": id,
        "lens": lens,
        "theme": theme,
        "title": title,
        "subtitle": subtitle,
        "unit": unit,
        "source": source,
        "notes": notes or {"es": [], "en": []},
        "retrieved": dt.date.today().isoformat(),
        "geos": geos or {},
        **(extra or {}),
        "rows": rows,
    }


def write(charts: list[dict]) -> None:
    """Escribe solo los gráficos generados: una ejecución parcial no toca los demás."""
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    for c in charts:
        (CHARTS_DIR / f"{c['id']}.json").write_text(json.dumps(c, ensure_ascii=False, indent=1))
