"""Datos del SIPRI publicados por el Banco Mundial: gasto militar y transferencias de armas."""

from lib import sources

# El agregado de la UE del Banco Mundial (EUU) suma a los 27
WB_CODES = {"EUU": "EU27"}
PERIODS = {"2016-2020": (2016, 2020), "2021-2025": (2021, 2025)}
TIV_NOTES = {
    "es": ["Datos del SIPRI publicados por el Banco Mundial, en valores indicadores de tendencia (TIV): miden el volumen de armas transferidas con un precio estándar por tipo de arma, no lo que se paga por ellas.",
           "El SIPRI recomienda comparar periodos de cinco años, porque las entregas de un año dependen de pocos contratos grandes."],
    "en": ["SIPRI data published by the World Bank, in trend-indicator values (TIV): they measure the volume of arms transferred using a standard price per type of weapon, not what is paid for them.",
           "SIPRI recommends comparing five-year periods, because a single year's deliveries depend on a few large contracts."],
}


def wb(indicator: str, codes: list[str], start: int, end: int) -> list[dict]:
    rows = sources.worldbank(indicator, codes, start, end)
    return [{"geo": WB_CODES.get(r["iso3"], r["iso3"]), "time": r["time"], "value": r["value"]} for r in rows]


def five_year(indicator: str, codes: list[str]) -> list[dict]:
    """Suma de cada periodo de cinco años, en miles de millones de TIV. Solo códigos con los diez años."""
    rows = wb(indicator, codes, 2016, 2025)
    out = []
    for g in sorted({r["geo"] for r in rows}):
        v = {int(r["time"]): r["value"] for r in rows if r["geo"] == g}
        for label, (a, b) in PERIODS.items():
            out.append({"geo": g, "time": label, "value": round(sum(v.get(y, 0) for y in range(a, b + 1)) / 1e9, 2)})
    return out
