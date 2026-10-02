"""Pagos del BCE (dataset PAY): número de operaciones por país, semestral, sumado por año."""

from collections import defaultdict

from lib import sources

PAY_SOURCE = {"name": "BCE, estadísticas de pagos (indicadores clave)", "dataset": "PAY",
              "url": "https://data.ecb.europa.eu/data/datasets/PAY", "license": "ECB, reutilización con cita de la fuente"}


def pay_annual(instruments: list[str]) -> dict[tuple[str, str, str], float]:
    """{(área BCE, instrumento, año): millones de operaciones}, solo años con los dos semestres."""
    total, halves = defaultdict(float), defaultdict(int)
    for r in sources.ecb("PAY", "H..W0..1._Z.N.PN"):
        if r["TYP_TRNSCTN"] not in instruments:
            continue
        assert r["UNIT_MULT"] == "6", r["KEY"]
        key = (r["REF_AREA"], r["TYP_TRNSCTN"], r["TIME_PERIOD"][:4])
        total[key] += float(r["OBS_VALUE"])
        halves[key] += 1
    return {k: v for k, v in total.items() if halves[k] == 2}
