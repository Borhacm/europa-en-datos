"""Utilidades compartidas por los gráficos."""

from lib import geo


def eurostat_source(dataset: str, **extra) -> dict:
    return {
        "name": "Eurostat",
        "dataset": dataset,
        "url": f"https://ec.europa.eu/eurostat/databrowser/view/{dataset}/default/table",
        "license": "CC BY 4.0",
        **extra,
    }


def from_eurostat(rows: list[dict], dims: list[str]) -> list[dict]:
    """Convierte filas de Eurostat a {geo, time, value, <dims>}, descartando agregados que no usamos."""
    out = []
    for r in rows:
        code = geo.from_eurostat(r["geo"])
        if code is None:
            continue
        row = {"geo": code, "time": r["time"], "value": round(r["value"], 2)}
        row.update({d: r[d] for d in dims})
        if r.get("flag"):
            row["flag"] = r["flag"]
        out.append(row)
    return out


def ordinal_rows(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda r: (r["geo"], r["time"]))
