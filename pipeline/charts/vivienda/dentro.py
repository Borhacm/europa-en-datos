"""Vivienda. Mirada 3: sobrecarga del coste de la vivienda y hacinamiento en los 27."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat
from .elige import SILC_NOTE


def _silc(dataset: str) -> list[dict]:
    rows = sources.eurostat(dataset, unit="PC", rskpovth="TOTAL", age="TOTAL", sex="T")
    rows = [r for r in rows if r["time"] >= "2010"]
    out = [r for r in from_eurostat(rows, []) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    return sorted(out, key=lambda r: (r["geo"], r["time"]))


def sobrecarga():
    out = _silc("ilc_lvho07a")
    return chart(
        id="vid1-sobrecarga",
        lens="dentro", theme="vivienda",
        title={"es": "En Grecia, el 26,4 % de la población dedica más del 40 % de sus ingresos a la vivienda; en Chipre, el 2,4 %",
               "en": "In Greece, 26.4% of people spend more than 40% of their income on housing; in Cyprus, 2.4%"},
        subtitle={"es": "Población que vive en hogares que gastan más del 40 % de su renta disponible en vivienda, en %",
                  "en": "Population living in households that spend more than 40% of their disposable income on housing, in %"},
        unit={"es": "% de la población", "en": "% of population"},
        source=eurostat_source("ilc_lvho07a"),
        notes={"es": [SILC_NOTE["es"],
                      "Gastos de vivienda: alquiler o intereses de la hipoteca, más suministros, comunidad y reparaciones habituales, descontadas las ayudas a la vivienda. No incluye la devolución del capital de la hipoteca.",
                      "Dinamarca tiene una ruptura de serie en 2025: su dato pasa del 14,6 % al 23,4 % por un cambio de método, no por un cambio real de esa magnitud. Lituania es provisional."],
               "en": [SILC_NOTE["en"],
                      "Housing costs: rent or mortgage interest, plus utilities, service charges and regular repairs, net of housing allowances. Mortgage principal repayments are not included.",
                      "Denmark has a break in series in 2025: its figure goes from 14.6% to 23.4% because of a change in method, not a real change of that size. Lithuania is provisional."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
    )


def hacinamiento():
    out = _silc("ilc_lvho05a")
    return chart(
        id="vid2-hacinamiento",
        lens="dentro", theme="vivienda",
        title={"es": "En Rumanía y Letonia, cerca de cuatro de cada diez personas viven en una casa con menos habitaciones de las necesarias; en Chipre, el 2,2 %",
               "en": "In Romania and Latvia, about four in ten people live in a home with fewer rooms than they need; in Cyprus, 2.2%"},
        subtitle={"es": "Tasa de hacinamiento: población que vive en una vivienda con menos habitaciones de las que necesita su hogar, en %",
                  "en": "Overcrowding rate: population living in a dwelling with fewer rooms than their household needs, in %"},
        unit={"es": "% de la población", "en": "% of population"},
        source=eurostat_source("ilc_lvho05a"),
        notes={"es": [SILC_NOTE["es"],
                      "Eurostat considera que un hogar necesita una habitación común, una por pareja, una por adulto soltero de 18 años o más y una por cada dos niños del mismo sexo de 12 a 17 años o por cada dos menores de 12.",
                      "Mide el número de habitaciones, no los metros cuadrados ni el estado de la vivienda."],
               "en": [SILC_NOTE["en"],
                      "Eurostat considers that a household needs one common room, one room per couple, one per single adult aged 18 or over, and one for every two children of the same sex aged 12 to 17 or every two children under 12.",
                      "It measures the number of rooms, not floor space or the condition of the dwelling."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [sobrecarga, hacinamiento]
