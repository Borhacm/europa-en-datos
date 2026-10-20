"""Productividad. Mirada 2: ¿trabaja Europa peor, o trabaja menos horas?"""

from collections import Counter

from lib import geo, sources
from lib.output import chart

from .gigantes import LAST_YEAR

PDB_FLOW = "OECD.SDD.TPS,DSD_PDB@DF_PDB,2.0"
PDB_SOURCE = {"name": "OCDE, Productivity Database", "dataset": "DSD_PDB@DF_PDB",
              "url": "https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_PDB%40DF_PDB&df[ag]=OECD.SDD.TPS",
              "license": "CC BY 4.0"}
SERIES = {
    "empleo": {"es": "Tasa de empleo", "en": "Employment rate"},
    "horas": {"es": "Horas por ocupado", "en": "Hours per worker"},
}


def empleo_horas():
    # Empleo, población y horas por habitante: no dependen de precios ni de paridades de poder adquisitivo
    rows = sources.oecd(PDB_FLOW, "USA+EU27_2020.A.EMP+POP+HRSPOP._T.PS+H_PS._Z.N._Z._Z", start="2000")
    v = {(r["REF_AREA"], r["MEASURE"], r["TIME_PERIOD"]): float(r["OBS_VALUE"]) for r in rows if r["OBS_VALUE"]}
    out = []
    years = sorted({t for (_, _, t) in v})
    for t in years:
        try:
            rate = {a: v[(a, "EMP", t)] / v[(a, "POP", t)] for a in ("EU27_2020", "USA")}
            hours = {a: v[(a, "HRSPOP", t)] / rate[a] for a in ("EU27_2020", "USA")}
        except KeyError:
            continue
        out.append({"geo": "EU27", "series": "empleo", "time": t, "value": round(100 * rate["EU27_2020"] / rate["USA"], 1)})
        out.append({"geo": "EU27", "series": "horas", "time": t, "value": round(100 * hours["EU27_2020"] / hours["USA"], 1)})
    latest = max(r["time"] for r in out)
    return chart(
        id="pe3-empleo-horas",
        lens="elige", theme="productividad",
        title={"es": "En la UE ya trabaja la misma parte de la población que en EE. UU.; cada ocupado hace casi un 10 % menos de horas",
               "en": "The same share of the population now works in the EU as in the US; each worker puts in almost 10% fewer hours"},
        subtitle={"es": f"UE en % del nivel de EE. UU. (100 = EE. UU.), personas ocupadas por habitante y horas al año por persona ocupada, 2000 a {latest}",
                  "en": f"EU as % of the US level (100 = US), employed people per inhabitant and hours a year per employed person, 2000 to {latest}"},
        unit={"es": "% del nivel de EE. UU.", "en": "% of US level"},
        source=PDB_SOURCE,
        notes={"es": ["Tasa de empleo: ocupados entre población total, no solo la de edad de trabajar. Horas trabajadas en el año entre ocupados, de las cuentas nacionales. No dependen de precios ni de paridades de poder adquisitivo.",
                      "El PIB por habitante es el producto de tres factores: lo que se produce por hora, las horas de cada ocupado y los ocupados por habitante. Este gráfico muestra los dos últimos."],
               "en": ["Employment rate: employed people over the total population, not only the working-age population. Hours worked in the year over employed people, from national accounts. They do not depend on prices or purchasing power parities.",
                      "GDP per person is the product of three factors: output per hour, hours per worker and workers per inhabitant. This chart shows the last two."]},
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


BUILDERS = [empleo_horas, horas_trabajadas]
