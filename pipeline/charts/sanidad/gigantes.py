"""Sanidad. Mirada 1: cuánto gastan en salud la UE, EE. UU. y China."""

from lib import geo, sources
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


SHA_FLOW = "OECD.ELS.HD,DSD_SHA@DF_SHA,1.1"
SHA_SOURCE = {"name": "OCDE, System of Health Accounts", "dataset": "DSD_SHA@DF_SHA",
              "url": "https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_SHA%40DF_SHA&df[ag]=OECD.ELS.HD",
              "license": "CC BY 4.0", "also": [worldbank_source("SP.POP.TOTL", "población total")]}
SHA_YEAR = "2023"
# Funciones del gasto. En EE. UU., los servicios auxiliares (laboratorio, imagen, transporte) van dentro de la atención curativa
FUNCTIONS = {
    "HC1HC2": {"es": "Atención curativa", "en": "Curative care", "parts": ["HC1HC2", "HC4"]},
    "HC5": {"es": "Medicamentos", "en": "Medicines", "parts": ["HC5"]},
    "HC7": {"es": "Administración", "en": "Administration", "parts": ["HC7"]},
    "HC3": {"es": "Larga duración", "en": "Long-term care", "parts": ["HC3"]},
    "HC6": {"es": "Prevención", "en": "Prevention", "parts": ["HC6"]},
}
BLOC_PAIR = {"EU27": {"es": "UE", "en": "EU"}, "USA": {"es": "EE. UU.", "en": "US"}}


def gasto_funciones():
    areas = ["USA", *geo.EU27]
    rows = sources.oecd(SHA_FLOW, f"{'+'.join(areas)}.A.EXP_HEALTH.USD_PPP_PS._T._Z.HC1HC2+HC3+HC4+HC5+HC6+HC7._T._T._Z._Z.V",
                        start=SHA_YEAR)
    v = {(r["REF_AREA"], r["FUNCTION"]): float(r["OBS_VALUE"]) for r in rows if r["TIME_PERIOD"] == SHA_YEAR and r["OBS_VALUE"]}
    pop = {r["iso3"]: r["value"] for r in sources.worldbank("SP.POP.TOTL", geo.EU27, int(SHA_YEAR), int(SHA_YEAR))}
    eu_pop = sum(pop[c] for c in geo.EU27)
    out = []
    for code, f in FUNCTIONS.items():
        us = sum(v.get(("USA", part), 0) for part in f["parts"])
        # Media de la UE ponderada por población: gasto total de los 27 entre su población
        eu = sum(v.get((c, part), 0) * pop[c] for c in geo.EU27 for part in f["parts"]) / eu_pop
        out += [{"geo": code, "time": SHA_YEAR, "bloc": "EU27", "value": round(eu)},
                {"geo": code, "time": SHA_YEAR, "bloc": "USA", "value": round(us)}]
    return chart(
        id="sag3-gasto-funciones",
        lens="gigantes", theme="sanidad",
        title={"es": "Tres cuartas partes de lo que EE. UU. gasta de más se van en atención curativa; la administración y los medicamentos, una décima parte cada uno",
               "en": "Three quarters of what the US spends extra goes on curative care; administration and medicines, a tenth each"},
        subtitle={"es": f"Gasto sanitario corriente por habitante según su destino, en dólares en paridad de poder adquisitivo, {SHA_YEAR}",
                  "en": f"Current health expenditure per person by function, in dollars at purchasing power parity, {SHA_YEAR}"},
        unit={"es": "dólares por habitante (PPA)", "en": "dollars per person (PPP)"},
        source=SHA_SOURCE,
        notes={"es": ["UE: media de los 27 ponderada por población (gasto de cada país por habitante multiplicado por su población, entre la población total).",
                      "Atención curativa: consultas, hospitales y rehabilitación, con los servicios auxiliares (análisis, pruebas de imagen, transporte de pacientes), porque EE. UU. no los separa. Medicamentos: también otros productos médicos. Administración: del sistema público y de las aseguradoras. Larga duración: cuidados sanitarios de larga duración.",
                      "Las cifras de la OCDE difieren algo de las de la OMS de G2, que se calculan con otro método."],
               "en": ["EU: population-weighted average of the 27 (each country's spending per person times its population, over the total population).",
                      "Curative care: consultations, hospitals and rehabilitation, with ancillary services (tests, imaging, patient transport), because the US does not report them separately. Medicines: also other medical goods. Administration: of the public system and of insurers. Long-term care: health-related long-term care.",
                      "OECD figures differ somewhat from the WHO figures in G2, which are computed with another method."]},
        rows=out,
        geos={k: {"es": f["es"], "en": f["en"], "eu": False, "aggregate": False} for k, f in FUNCTIONS.items()},
        extra={"dimensions": {"bloc": BLOC_PAIR}},
    )


BUILDERS = [gasto_pib, gasto_habitante, gasto_funciones]
