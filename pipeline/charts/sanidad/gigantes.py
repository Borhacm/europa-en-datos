"""Sanidad. Mirada 1: cuánto gastan en salud la UE, EE. UU. y China."""

from lib import geo
from lib.output import chart

from ..common import worldbank_rows, worldbank_source

# Último año con datos para casi todos los países: el agregado UE de años posteriores es incompleto
LAST_YEAR = 2023
BLOCS = {"USA", "CHN", "EU27"}
NOTES = {
    "es": ["Gasto sanitario corriente: público y privado, sin inversiones en hospitales o equipos.",
           "Estimaciones de la Organización Mundial de la Salud (base de datos de gasto sanitario mundial) publicadas por el Banco Mundial.",
           f"Se muestra hasta {LAST_YEAR}, el último año con datos de casi todos los países: el agregado de la UE para años posteriores se calcula con menos de 27."],
    "en": ["Current health expenditure: public and private, excluding investment in hospitals or equipment.",
           "World Health Organization estimates (Global Health Expenditure Database) published by the World Bank.",
           f"Shown up to {LAST_YEAR}, the last year with data for almost every country: the EU aggregate for later years is computed from fewer than 27."],
}


def _blocs(indicator: str, digits: int) -> list[dict]:
    rows = worldbank_rows(indicator, 2000, LAST_YEAR)
    return [{**r, "value": round(r["value"], digits)} for r in rows if r["geo"] in BLOCS]


def gasto_pib():
    out = _blocs("SH.XPD.CHEX.GD.ZS", 2)
    return chart(
        id="sag1-gasto-pib",
        lens="gigantes", theme="sanidad",
        title={"es": "EE. UU. dedica a la sanidad el 16,7 % de su PIB; la UE, el 10 %, y China, menos del 6 %",
               "en": "The US spends 16.7% of its GDP on health; the EU, 10%, and China, less than 6%"},
        subtitle={"es": "Gasto sanitario corriente, público y privado, en % del PIB",
                  "en": "Current health expenditure, public and private, as % of GDP"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source=worldbank_source("SH.XPD.CHEX.GD.ZS", "gasto sanitario corriente (% del PIB)"),
        notes=NOTES,
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
    )


def gasto_habitante():
    out = _blocs("SH.XPD.CHEX.PP.CD", 0)
    return chart(
        id="sag2-gasto-habitante",
        lens="gigantes", theme="sanidad",
        title={"es": "Por habitante, EE. UU. gasta en salud 2,3 veces más que la UE",
               "en": "Per person, the US spends 2.3 times as much on health as the EU"},
        subtitle={"es": "Gasto sanitario corriente por habitante, en dólares internacionales corrientes en paridad de poder adquisitivo",
                  "en": "Current health expenditure per person, in current international dollars at purchasing power parity"},
        unit={"es": "dólares por habitante (PPA)", "en": "dollars per person (PPP)"},
        source=worldbank_source("SH.XPD.CHEX.PP.CD", "gasto sanitario corriente por habitante (PPA)"),
        notes={"es": [*NOTES["es"], "La paridad de poder adquisitivo corrige las diferencias de precios entre países. Los valores están en dólares de cada año, sin descontar la inflación."],
               "en": [*NOTES["en"], "Purchasing power parity corrects for price differences between countries. Values are in each year's dollars, not adjusted for inflation."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [gasto_pib, gasto_habitante]
