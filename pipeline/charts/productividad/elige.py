"""Productividad. Mirada 2: ¿trabaja Europa peor, o trabaja menos horas?"""

from collections import Counter

from lib import geo, sources
from lib.output import chart

from .gigantes import LAST_YEAR

SERIES = {
    "hora": {"es": "PIB por hora trabajada", "en": "GDP per hour worked"},
    "habitante": {"es": "PIB por habitante", "en": "GDP per person"},
}


def brecha_ee_uu():
    # Por hora: OIT, UE-27 (X92) sobre EE. UU.
    per_hour = {}
    for r in sources.ilo("DF_GDP_2HRW_NOC_NB", "USA+X92..", start="2000"):
        if r["FREQ"] == "A" and r["OBS_VALUE"] and int(r["TIME_PERIOD"]) <= LAST_YEAR:
            per_hour.setdefault(r["TIME_PERIOD"], {})[r["REF_AREA"]] = float(r["OBS_VALUE"])
    # Por habitante: Eurostat, índice de volumen en PPS (UE = 100) de EE. UU.
    us_index = {r["time"]: r["value"] for r in sources.eurostat(
        "sdg_10_10", indic_ppp="VI_PPS_EU27_2020_HAB", ppp_cat18="GDP", geo="US")}

    out = []
    for t, v in per_hour.items():
        if "USA" in v and "X92" in v:
            out.append({"geo": "EU27", "series": "hora", "time": t, "value": round(100 * v["X92"] / v["USA"], 1)})
    for t, us in us_index.items():
        if int(t) <= LAST_YEAR:
            out.append({"geo": "EU27", "series": "habitante", "time": t, "value": round(100 * 100 / us, 1)})
    return chart(
        id="pe1-brecha-ee-uu",
        lens="elige", theme="productividad",
        title={"es": "Por hora trabajada, la UE está al 87 % de EE. UU.; por habitante, solo al 74 %",
               "en": "Per hour worked, the EU is at 87% of the US; per person, only at 74%"},
        subtitle={"es": "PIB de la UE en % del de EE. UU. (100 = EE. UU.), por hora trabajada y por habitante",
                  "en": "EU GDP as % of US GDP (100 = US), per hour worked and per person"},
        unit={"es": "% del nivel de EE. UU.", "en": "% of US level"},
        source={"name": "OIT, ILOSTAT, y Eurostat", "dataset": "DF_GDP_2HRW_NOC_NB, sdg_10_10",
                "url": "https://ec.europa.eu/eurostat/databrowser/view/sdg_10_10/default/table", "license": "CC BY 4.0",
                "also": [{"name": "OIT, ILOSTAT", "url": "https://ilostat.ilo.org/data/"}]},
        notes={"es": ["Por hora: PIB por hora trabajada de la OIT (estimaciones modelizadas). Por habitante: PIB por habitante en paridad de poder adquisitivo de Eurostat.",
                      "La diferencia entre las dos líneas se explica por las horas trabajadas y por la parte de la población que tiene empleo."],
               "en": ["Per hour: ILO GDP per hour worked (modelled estimates). Per person: Eurostat GDP per person at purchasing power parity.",
                      "The difference between the two lines comes from hours worked and from the share of the population in work."]},
        rows=sorted(out, key=lambda r: (r["series"], r["time"])),
        geos=geo.geo_table(["EU27"]),
        extra={"dimensions": {"series": SERIES}, "ref_line": {"value": 100, "label": {"es": "Estados Unidos", "en": "United States"}}},
    )


def horas_trabajadas():
    areas = ["USA", *geo.EU27]
    rows = sources.ilo("DF_HOW_TEMP_SEX_ECO_NB", f"{'+'.join(areas)}.A..SEX_T.ECO_AGGREGATE_TOTAL", start="2015")
    out = [{"geo": geo.from_iso3(r["REF_AREA"]), "time": r["TIME_PERIOD"], "value": round(float(r["OBS_VALUE"]), 1)}
           for r in rows if r["OBS_VALUE"] and len(r["TIME_PERIOD"]) == 4 and int(r["TIME_PERIOD"]) <= LAST_YEAR + 1]
    # Año de referencia: el más reciente con datos de casi todos los países
    counts = Counter(r["time"] for r in out)
    ref_year = max(t for t, n in counts.items() if n >= 25)
    return chart(
        id="pe2-horas-trabajadas",
        lens="elige", theme="productividad",
        title={"es": "El oeste y el norte de Europa trabajan menos horas que EE. UU.; casi todo el este y parte del sur, más",
               "en": "Western and northern Europe work fewer hours than the US; most of the east and part of the south, more"},
        subtitle={"es": "Horas trabajadas de verdad a la semana por cada persona con empleo",
                  "en": "Hours actually worked per week by each employed person"},
        unit={"es": "horas a la semana", "en": "hours per week"},
        source={"name": "OIT, ILOSTAT (encuestas de población activa)", "dataset": "DF_HOW_TEMP_SEX_ECO_NB",
                "url": "https://ilostat.ilo.org/data/", "license": "CC BY 4.0"},
        notes={"es": ["Media de todas las personas ocupadas, a tiempo completo y parcial. En la UE, datos de la Encuesta de Población Activa de la UE; en EE. UU., de la Current Population Survey.",
                      "Las encuestas son comparables en lo esencial, pero no idénticas."],
               "en": ["Average over all employed people, full- and part-time. EU data from the EU Labour Force Survey; US data from the Current Population Survey.",
                      "The surveys are broadly comparable, but not identical."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"ref_year": ref_year},
    )


BUILDERS = [brecha_ee_uu, horas_trabajadas]
