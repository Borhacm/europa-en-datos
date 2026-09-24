"""Libertades, bienestar y clima. Mirada 1: democracia, salud y emisiones en los tres bloques."""

from lib import geo
from lib.output import chart

from ..common import vdem_with_eu, worldbank_rows, worldbank_source

VDEM_SOURCE = {"name": "V-Dem (v16)", "dataset": "vdem.RData", "url": "https://www.v-dem.net/data/the-v-dem-dataset/",
               "license": "CC BY-SA 4.0"}
LIBDEM = {"v2x_libdem": {"es": "Índice de democracia liberal", "en": "Liberal democracy index"}}


def democracia():
    out = vdem_with_eu(LIBDEM, since=2000, countries=["USA", "CHN"])
    return chart(
        id="lg1-democracia",
        lens="gigantes", theme="libertades",
        title={"es": "La democracia de EE. UU. cayó en 2025 a su nivel más bajo del siglo, por debajo de la mediana de la UE",
               "en": "US democracy fell in 2025 to its lowest level this century, below the EU median"},
        subtitle={"es": "Índice de democracia liberal de V-Dem, de 0 (ninguna) a 1 (plena)",
                  "en": "V-Dem liberal democracy index, from 0 (none) to 1 (full)"},
        unit={"es": "índice de 0 a 1", "en": "index from 0 to 1"},
        source=VDEM_SOURCE,
        notes={"es": ["Mide elecciones libres, libertades civiles, estado de derecho y controles al poder, a partir de encuestas a expertos de cada país.",
                      "Para la UE se muestra la mediana de los 27 y el país con el valor más bajo de cada año.",
                      "Licencia CC BY-SA: los datos derivados deben compartirse con la misma licencia."],
               "en": ["Measures free elections, civil liberties, rule of law and checks on power, based on country expert surveys.",
                      "For the EU, the median of the 27 and the lowest-scoring country each year are shown.",
                      "CC BY-SA licence: derived data must be shared under the same licence."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"measure": LIBDEM}},
    )


def esperanza_vida():
    out = worldbank_rows("SP.DYN.LE00.IN", 1990, 2024)
    return chart(
        id="lg2-esperanza-vida",
        lens="gigantes", theme="libertades",
        title={"es": "En la UE se vive casi tres años más que en EE. UU., y China ya casi ha alcanzado a EE. UU.",
               "en": "People in the EU live almost three years longer than in the US, and China has nearly caught up with the US"},
        subtitle={"es": "Esperanza de vida al nacer, en años", "en": "Life expectancy at birth, in years"},
        unit={"es": "años", "en": "years"},
        source=worldbank_source("SP.DYN.LE00.IN", "esperanza de vida al nacer"),
        notes={"es": ["La caída de 2020 y 2021 refleja la pandemia de covid-19."],
               "en": ["The 2020 and 2021 drop reflects the covid-19 pandemic."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
    )


def co2_habitante():
    out = worldbank_rows("EN.GHG.CO2.PC.CE.AR5", 1990, 2024)
    return chart(
        id="lg3-co2-habitante",
        lens="gigantes", theme="libertades",
        title={"es": "Un chino ya emite más CO₂ que un europeo; un estadounidense, más del doble",
               "en": "A Chinese person now emits more CO₂ than a European; an American, more than twice as much"},
        subtitle={"es": "Emisiones de CO₂ por habitante, en toneladas al año (sin cambios de uso del suelo)",
                  "en": "CO₂ emissions per person, in tonnes a year (excluding land use change)"},
        unit={"es": "toneladas por habitante", "en": "tonnes per person"},
        source=worldbank_source("EN.GHG.CO2.PC.CE.AR5", "emisiones de CO₂ por habitante (EDGAR)"),
        notes={"es": ["Emisiones producidas en cada territorio. No incluyen las emisiones de los bienes importados."],
               "en": ["Emissions produced in each territory. They exclude emissions embodied in imported goods."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [democracia, esperanza_vida, co2_habitante]
