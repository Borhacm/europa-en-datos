"""Dinero. Mirada 3: pagos con tarjeta y retiradas de efectivo por habitante en cada país."""

from lib import geo, sources
from lib.output import chart

from ._ecb import PAY_SOURCE, pay_annual

YEARS = ["2022", "2025"]


def _population() -> dict[tuple[str, str], float]:
    """Población a 1 de enero (Eurostat tps00001), por país canónico y año."""
    out = {}
    for r in sources.eurostat("tps00001"):
        code = geo.from_eurostat(r["geo"])
        if code in geo.EU27 and r["time"] in YEARS:
            out[(code, r["time"])] = r["value"]
    return out


def _per_person(instrument: str) -> list[dict]:
    data, pop = pay_annual([instrument]), _population()
    out = []
    for (area, _, year), v in data.items():
        code = geo.from_eurostat("EL" if area == "GR" else area)  # el BCE usa GR para Grecia
        if code in geo.EU27 and year in YEARS and (code, year) in pop:
            out.append({"geo": code, "time": year, "value": round(v * 1e6 / pop[(code, year)], 1)})
    return sorted(out, key=lambda r: (r["geo"], r["time"]))


NOTES_ES = ["Operaciones de cada año (suma de los dos semestres) divididas por la población a 1 de enero.",
            "El BCE asigna cada operación al país de la entidad que emitió la tarjeta, no al de quien la usa. Las cifras muy altas de Lituania, Luxemburgo o Irlanda pueden reflejar entidades de pago con clientes en otros países.",
            "Dinamarca y Suecia no aparecen en esta serie del BCE. Faltan algunos países en 2022 porque no publicaron los dos semestres."]
NOTES_EN = ["Transactions in each year (sum of both half-years) divided by the population on 1 January.",
            "The ECB assigns each transaction to the country of the institution that issued the card, not to that of the user. The very high figures for Lithuania, Luxembourg and Ireland may reflect payment institutions with customers in other countries.",
            "Denmark and Sweden are not included in this ECB series. Some countries are missing in 2022 because they did not report both half-years."]
SOURCE = {**PAY_SOURCE, "name": "BCE, estadísticas de pagos (PAY); Eurostat, población (tps00001)"}


def pagos_tarjeta():
    out = _per_person("CP0")
    return chart(
        id="did1-pagos-tarjeta",
        lens="dentro", theme="dinero",
        title={"es": "Los pagos con tarjeta por habitante aumentaron en los 24 países con datos de 2022 y 2025; Alemania e Italia siguen entre los que menos los usan",
               "en": "Card payments per person rose in all 24 countries with data for 2022 and 2025; Germany and Italy are still among those using them least"},
        subtitle={"es": "Pagos con tarjeta por habitante y año", "en": "Card payments per person per year"},
        unit={"es": "pagos por habitante", "en": "payments per person"},
        source=SOURCE,
        notes={"es": NOTES_ES, "en": NOTES_EN},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
    )


def retiradas_efectivo():
    out = _per_person("CW1")
    return chart(
        id="did2-retiradas-efectivo",
        lens="dentro", theme="dinero",
        title={"es": "Las retiradas de efectivo con tarjeta bajaron en 20 de los 21 países con datos de 2022 y 2025",
               "en": "Cash withdrawals with cards fell in 20 of the 21 countries with data for 2022 and 2025"},
        subtitle={"es": "Retiradas de efectivo con tarjeta por habitante y año, 2022 y 2025",
                  "en": "Cash withdrawals with cards per person per year, 2022 and 2025"},
        unit={"es": "retiradas por habitante", "en": "withdrawals per person"},
        source=SOURCE,
        notes={"es": [*NOTES_ES, "No mide cuánto se paga con efectivo, pero indica con qué frecuencia se recurre a él."],
               "en": [*NOTES_EN, "It does not measure how much is paid in cash, but shows how often people turn to it."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [pagos_tarjeta, retiradas_efectivo]
