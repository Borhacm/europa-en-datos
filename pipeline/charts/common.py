"""Utilidades compartidas por los gráficos."""

import json
from collections import Counter

from lib import geo, sources
from lib.http import fetch
from lib.output import DATA_DIR


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


def vdem_with_eu(measures: dict, since: int, countries: list[str]) -> list[dict]:
    """Filas V-Dem por país y, para la UE, mediana de los 27 y país con el valor más bajo.

    V-Dem no publica agregados de la UE: la mediana resume el conjunto sin que pesen más los países grandes.
    """
    df = sources.vdem(list(measures))
    df = df[(df.year >= since) & df.country_text_id.isin([*countries, *geo.EU27])]
    out = []
    for m in measures:
        for r in df[["country_text_id", "year", m]].dropna().itertuples(index=False):
            out.append({"geo": r[0], "time": str(int(r[1])), "measure": m, "value": round(float(r[2]), 3), "stat": "country"})
        eu = df[df.country_text_id.isin(geo.EU27)].groupby("year")[m]
        for year, med in eu.median().dropna().items():
            out.append({"geo": "EU27", "time": str(int(year)), "measure": m, "value": round(float(med), 3), "stat": "median"})
        for year, lo in eu.min().dropna().items():
            out.append({"geo": "EU27", "time": str(int(year)), "measure": m, "value": round(float(lo), 3), "stat": "min"})
    return sorted(out, key=lambda r: (r["measure"], r["geo"], r["time"]))


def worldbank_rows(indicator: str, start: int, end: int, extra: list[str] | None = None) -> list[dict]:
    """Serie del Banco Mundial para EE. UU., China, la UE (EUU) y los 27 países."""
    iso = ["USA", "CHN", "EUU", *geo.EU27, *(extra or [])]
    out = []
    for r in sources.worldbank(indicator, iso, start, end):
        code = geo.from_iso3(r["iso3"])
        if code:
            out.append({"geo": code, "time": r["time"], "value": round(r["value"], 3)})
    return sorted(out, key=lambda r: (r["geo"], r["time"]))


def worldbank_source(indicator: str, name: str) -> dict:
    return {"name": f"Banco Mundial, {name}", "dataset": indicator,
            "url": f"https://data.worldbank.org/indicator/{indicator}", "license": "CC BY 4.0"}


GISCO = "https://gisco-services.ec.europa.eu/distribution/v2/nuts/topojson/NUTS_RG_20M_2024_4326_LEVL_{level}.json"
GISCO_SOURCE = {"name": "Eurostat GISCO, NUTS 2024 (geometrías)",
                "url": "https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics"}


def nuts_map(rows: list[dict]) -> tuple[list[dict], dict]:
    """Prepara filas regionales de Eurostat para el mapa y guarda las geometrías NUTS en data/geo.

    Cada país publica al nivel regional que puede: el mapa usa el más detallado disponible en el año
    de referencia, que es el que tiene más regiones con dato (y, si empatan, el más reciente).
    """
    out = []
    for r in rows:
        nuts = r["geo"]
        if nuts.startswith(("EU", "EA")):
            continue
        country = geo.from_eurostat(nuts[:2])
        if country is None:
            continue
        out.append({"geo": nuts, "country": country, "level": len(nuts) - 2, "time": r["time"],
                    "value": round(r["value"], 2), "name": r["geo_label"]})

    counts = Counter(r["time"] for r in out)
    latest = max(counts, key=lambda t: (counts[t], t))
    best_level: dict[str, int] = {}
    for r in out:
        if r["time"] == latest:
            best_level[r["country"]] = max(best_level.get(r["country"], 0), r["level"])

    geo_dir = DATA_DIR / "geo"
    geo_dir.mkdir(parents=True, exist_ok=True)
    missing = {}
    for level in (0, 1, 2):
        topo = json.loads(fetch(GISCO.format(level=level), ".json").read_text())
        (geo_dir / f"nuts{level}.json").write_text(json.dumps(topo, separators=(",", ":")))
        obj = next(iter(topo["objects"].values()))
        ids = {g["properties"].get("id") or g.get("id") for g in obj["geometries"]}
        missing[level] = sorted({r["geo"] for r in out if r["level"] == level} - ids)

    extra = {"best_level": best_level, "latest": latest,
             "geometry": {str(lvl): f"geo/nuts{lvl}.json" for lvl in (0, 1, 2)},
             "unmatched_geometry": missing}
    return sorted(out, key=lambda r: (r["geo"], r["time"])), extra
