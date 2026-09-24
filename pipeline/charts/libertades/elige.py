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
        notes={"es": ["Emisiones producidas en cada territorio, sin las de los bienes importados. Parte de la reducción europea se debe a que produce fuera bienes que consume."],
               "en": ["Emissions produced in each territory, excluding those embodied in imports. Part of Europe's cut comes from producing abroad goods it consumes."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"ref_line": {"value": 100, "label": {"es": "Nivel de 1990", "en": "1990 level"}}},
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


BUILDERS = [emisiones_1990, gasto_social]
