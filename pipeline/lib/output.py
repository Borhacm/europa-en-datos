"""Formato común de salida: un JSON por gráfico en data/charts, más un índice."""

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
THEMES = {
    "ia-digital": {"es": "IA y digital", "en": "AI and digital"},
    "comercio": {"es": "Comercio y dependencias", "en": "Trade and dependencies"},
    "productividad": {"es": "Productividad y crecimiento", "en": "Productivity and growth"},
    "libertades": {"es": "Libertades, bienestar y clima", "en": "Freedoms, well-being and climate"},
}


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
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    index = []
    for c in charts:
        (CHARTS_DIR / f"{c['id']}.json").write_text(json.dumps(c, ensure_ascii=False, indent=1))
        index.append({k: c[k] for k in ("id", "lens", "theme", "title", "retrieved")} | {"n_rows": len(c["rows"])})
    (DATA_DIR / "index.json").write_text(json.dumps(
        {"lenses": LENSES, "themes": THEMES, "charts": index}, ensure_ascii=False, indent=1))
