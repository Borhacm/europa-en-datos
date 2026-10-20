"""Libertades, bienestar y clima. Mirada 2: las decisiones del modelo europeo y lo que cuestan."""

from lib import geo, sources
from lib.output import chart

from ..common import worldbank_rows, worldbank_source

BASE_YEAR = "1990"


def emisiones_1990():
    rows = [r for r in worldbank_rows("EN.GHG.CO2.MT.CE.AR5", int(BASE_YEAR), 2024) if r["geo"] in ("USA", "CHN", "EU27")]
    base = {r["geo"]: r["value"] for r in rows if r["time"] == BASE_YEAR}
    out = [{**r, "value": round(100 * r["value"] / base[r["geo"]], 1)} for r in rows]
    return chart(
        id="le1-emisiones-1990",
        lens="elige", theme="libertades",
        title={"es": "La UE emite un 35 % menos de CO₂ que en 1990. China, más de cinco veces más",
               "en": "The EU emits 35% less CO₂ than in 1990. China, more than five times as much"},
        subtitle={"es": "Emisiones totales de CO₂, índice 1990 = 100", "en": "Total CO₂ emissions, index 1990 = 100"},
        unit={"es": "índice (1990 = 100)", "en": "index (1990 = 100)"},
        source=worldbank_source("EN.GHG.CO2.MT.CE.AR5", "emisiones totales de CO₂ (EDGAR)"),
        notes={"es": ["Emisiones de CO₂ de combustibles fósiles y procesos industriales producidas en cada territorio, sin las de los bienes importados ni las del uso del suelo. El gráfico E2 compara las emisiones producidas con las que lleva lo que se consume.",
                      "El objetivo de la Ley Europea del Clima se refiere a todos los gases de efecto invernadero y descuenta las absorciones (bosques, suelos), así que no se puede leer directamente en esta serie."],
               "en": ["CO₂ emissions from fossil fuels and industrial processes produced in each territory, excluding those embodied in imports and those from land use. Chart E2 compares emissions produced with those embodied in what is consumed.",
                      "The European Climate Law target covers all greenhouse gases and nets out removals (forests, soils), so it cannot be read directly from this series."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"ref_line": {"value": 100, "label": {"es": "Nivel de 1990", "en": "1990 level"}}},
    )


BLOCS = {"EU27": {"es": "Unión Europea", "en": "European Union"},
         "USA": {"es": "Estados Unidos", "en": "United States"},
         "CHN": {"es": "China", "en": "China"}}
FOOTPRINT = {"PROD_GHG": {"es": "Producción", "en": "Production"},
             "FD_GHG": {"es": "Consumo (huella)", "en": "Consumption (footprint)"}}


def huella():
    rows = sources.oecd("OECD.STI.PIE,DSD_ICIO_GHG_MAIN_2025@DF_ICIO_GHG_MAIN_2025,1.0",
                        "A.PROD_GHG+FD_GHG.EU27_2020+USA+CHN._T.T_CO2E_PS")
    out = []
    for r in rows:
        code = geo.from_eurostat(r["REF_AREA"]) or r["REF_AREA"]
        out.append({"geo": code, "bloc": code, "series": r["MEASURE"], "time": r["TIME_PERIOD"],
                    "value": round(float(r["OBS_VALUE"]), 2)})
    return chart(
        id="le3-huella-emisiones",
        lens="elige", theme="libertades",
        title={"es": "Lo que consume un europeo lleva 10,2 toneladas de gases de efecto invernadero al año; lo que se produce en la UE, 8,1 por habitante",
               "en": "What a European consumes carries 10.2 tonnes of greenhouse gases a year; what is produced in the EU, 8.1 per person"},
        subtitle={"es": "Emisiones de gases de efecto invernadero por habitante, producidas en el territorio y contenidas en la demanda final, en toneladas de CO₂ equivalente",
                  "en": "Greenhouse gas emissions per person, produced in the territory and embodied in final demand, in tonnes of CO₂ equivalent"},
        unit={"es": "toneladas de CO₂ equivalente por habitante", "en": "tonnes of CO₂ equivalent per person"},
        source={"name": "OCDE, Greenhouse Gas Footprints, edición de 2025", "dataset": "DSD_ICIO_GHG_MAIN_2025@DF_ICIO_GHG_MAIN_2025",
                "url": "https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_ICIO_GHG_MAIN_2025%40DF_ICIO_GHG_MAIN_2025&df[ag]=OECD.STI.PIE", "license": "CC BY 4.0"},
        notes={"es": ["Producción: emisiones generadas en el territorio. Consumo: emisiones contenidas en lo que consumen e invierten sus habitantes, se produzca donde se produzca.",
                      "La huella suma las emisiones de todo lo que se consume o se invierte en un territorio, se produzca donde se produzca, y resta las de lo que exporta. Si la huella supera a las emisiones producidas, el territorio importa emisiones.",
                      "Se calcula con las tablas input-output de la OCDE (TIVA): es una estimación y se publica con varios años de retraso. Incluye todos los gases de efecto invernadero, no solo el CO₂, así que no coincide con el gráfico E1."],
               "en": ["Production: emissions generated in the territory. Consumption: emissions embodied in what its people consume and invest, wherever it is produced.",
                      "The footprint adds up the emissions of everything consumed or invested in a territory, wherever it is produced, and subtracts those of its exports. If the footprint exceeds the emissions produced, the territory imports emissions.",
                      "It is calculated with the OECD's input-output tables (TiVA): it is an estimate and is published with a lag of several years. It covers all greenhouse gases, not just CO₂, so it does not match chart E1."]},
        rows=sorted(out, key=lambda r: (r["bloc"], r["series"], r["time"])),
        geos=geo.geo_table(BLOCS),
        extra={"dimensions": {"bloc": BLOCS, "series": FOOTPRINT}},
    )


def gasto_social():
    countries = ["USA", *geo.EU27]
    rows = sources.oecd("OECD.ELS.SPD,DSD_SOCX_AGG@DF_SOCX_AGG,1.0", f"{'+'.join(countries)}.A.......", start="2000")
    out = []
    for r in rows:
        if (r["UNIT_MEASURE"], r["EXPEND_SOURCE"], r["SPENDING_TYPE"], r["PROGRAMME_TYPE"]) != ("PT_B1GQ", "ES10", "_T", "_T"):
            continue
        if r["OBS_VALUE"]:
            out.append({"geo": r["REF_AREA"], "time": r["TIME_PERIOD"], "value": round(float(r["OBS_VALUE"]), 1)})
    return chart(
        id="le2-gasto-social",
        lens="elige", theme="libertades",
        title={"es": "Francia, Italia, Alemania o España dedican al gasto social entre 7 y 12 puntos de PIB más que EE. UU.; varios países de la UE, menos",
               "en": "France, Italy, Germany or Spain devote 7 to 12 more points of GDP to social spending than the US; several EU countries, less"},
        subtitle={"es": "Gasto social público (pensiones, sanidad, desempleo, familia...), en % del PIB",
                  "en": "Public social spending (pensions, health, unemployment, family...), as % of GDP"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source={"name": "OCDE, Social Expenditure Database (SOCX)", "dataset": "DSD_SOCX_AGG@DF_SOCX_AGG",
                "url": "https://www.oecd.org/en/data/datasets/social-expenditure-database-socx.html", "license": "CC BY 4.0"},
        notes={"es": ["La OCDE no publica esta serie para Chipre ni Malta. Bulgaria, Croacia y Rumanía, que no son miembros de la OCDE, solo tienen algunos años.",
                      "Gasto público. En EE. UU. una parte importante de la sanidad y las pensiones es privada y no aparece aquí.",
                      "La OCDE no publica esta serie para China."],
               "en": ["The OECD does not publish this series for Cyprus or Malta. Bulgaria, Croatia and Romania, which are not OECD members, only have some years.",
                      "Public spending. In the US a large share of health care and pensions is private and does not appear here.",
                      "The OECD does not publish this series for China."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [emisiones_1990, huella, gasto_social]
