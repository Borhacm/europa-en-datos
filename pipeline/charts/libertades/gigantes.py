"""Libertades, bienestar y clima. Mirada 1: democracia y salud en los tres bloques."""

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


# Componentes del índice de democracia liberal (todos de 0 a 1)
COMPONENTS = {
    "v2xlg_legcon": {"es": "Control legislativo", "en": "Legislative constraints"},
    "v2x_freexp_altinf": {"es": "Libertad de expresión", "en": "Free expression"},
    "v2xcl_rol": {"es": "Igualdad ante la ley", "en": "Equality before the law"},
    "v2x_jucon": {"es": "Control judicial", "en": "Judicial constraints"},
    "v2x_frassoc_thick": {"es": "Libertad de asociación", "en": "Freedom of association"},
    "v2xel_frefair": {"es": "Elecciones limpias", "en": "Clean elections"},
}
# Nombres completos de V-Dem, para las notas
FULL = {
    "v2xlg_legcon": {"es": "control del legislativo sobre el ejecutivo", "en": "legislative constraints on the executive"},
    "v2x_freexp_altinf": {"es": "libertad de expresión y fuentes alternativas de información", "en": "freedom of expression and alternative sources of information"},
    "v2xcl_rol": {"es": "igualdad ante la ley y libertades individuales", "en": "equality before the law and individual liberty"},
    "v2x_jucon": {"es": "control judicial del ejecutivo", "en": "judicial constraints on the executive"},
    "v2x_frassoc_thick": {"es": "libertad de asociación", "en": "freedom of association"},
    "v2xel_frefair": {"es": "elecciones limpias", "en": "clean elections"},
}
COMPONENT_YEARS = ("2024", "2025")


def componentes():
    rows = vdem_with_eu(COMPONENTS, since=int(COMPONENT_YEARS[0]), countries=["USA"])
    out = [{"geo": r["measure"], "time": r["time"], "value": r["value"]}
           for r in rows if r["geo"] == "USA" and r["time"] in COMPONENT_YEARS]
    eu = {r["measure"]: r["value"] for r in rows if r["geo"] == "EU27" and r["stat"] == "median" and r["time"] == COMPONENT_YEARS[1]}
    return chart(
        id="lg4-componentes-democracia",
        lens="gigantes", theme="libertades",
        title={"es": "En 2025, lo que más cayó en EE. UU. fue el control del Congreso sobre el presidente: de 0,86 a 0,61",
               "en": "In 2025, what fell most in the US was Congress's check on the president: from 0.86 to 0.61"},
        subtitle={"es": "Componentes del índice de democracia liberal de V-Dem en EE. UU., de 0 a 1, 2024 y 2025",
                  "en": "Components of V-Dem's liberal democracy index in the US, from 0 to 1, 2024 and 2025"},
        unit={"es": "índice de 0 a 1", "en": "index from 0 to 1"},
        source=VDEM_SOURCE,
        notes={"es": ["Seis de los índices con los que V-Dem construye el de democracia liberal. El índice final no es su media: combina la democracia electoral con un componente liberal (límites al poder y derechos).",
                      "Mediana de los 27 países de la UE en 2025, como referencia: " + "; ".join(f"{FULL[k]['es']}, {f'{v:.2f}'.replace('.', ',')}" for k, v in eu.items()) + ".",
                      "Licencia CC BY-SA: los datos derivados deben compartirse con la misma licencia."],
               "en": ["Six of the indices V-Dem uses to build its liberal democracy index. The final index is not their average: it combines electoral democracy with a liberal component (limits on power and rights).",
                      "Median of the 27 EU countries in 2025, for reference: " + "; ".join(f"{FULL[k]['en']}, {v:.2f}" for k, v in eu.items()) + ".",
                      "CC BY-SA licence: derived data must be shared under the same licence."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos={k: {**v, "eu": False, "aggregate": False} for k, v in COMPONENTS.items()},
    )


BUILDERS = [democracia, componentes, esperanza_vida]
