"""Productividad. Mirada 1: el tamaño y la productividad de la UE frente a EE. UU. y China."""

from lib import geo, sources
from lib.output import chart

from ..common import worldbank_source

# Último año con datos observados: la OIT publica estimaciones modelizadas y proyecciones posteriores
LAST_YEAR = 2024


def peso_pib_mundial():
    rows = sources.worldbank("NY.GDP.MKTP.PP.CD", ["USA", "CHN", "EUU", "JPN", "WLD"], 1990, LAST_YEAR)
    world = {r["time"]: r["value"] for r in rows if r["iso3"] == "WLD"}
    out = [{"geo": geo.from_iso3(r["iso3"]), "time": r["time"], "value": round(100 * r["value"] / world[r["time"]], 2)}
           for r in rows if r["iso3"] != "WLD" and r["time"] in world]
    return chart(
        id="pg1-peso-pib-mundial",
        lens="gigantes", theme="productividad",
        title={"es": "China ya es la mayor economía del mundo en poder adquisitivo. La UE y EE. UU. pesan casi lo mismo",
               "en": "China is now the world's largest economy in purchasing power. The EU and the US weigh almost the same"},
        subtitle={"es": "Peso de cada economía en el PIB mundial, medido en paridad de poder adquisitivo, en %",
                  "en": "Each economy's share of world GDP, measured in purchasing power parity, in %"},
        unit={"es": "% del PIB mundial", "en": "% of world GDP"},
        source=worldbank_source("NY.GDP.MKTP.PP.CD", "PIB en paridad de poder adquisitivo"),
        notes={"es": ["La paridad de poder adquisitivo corrige las diferencias de precios entre países: un dólar compra más en China que en EE. UU."],
               "en": ["Purchasing power parity corrects for price differences between countries: a dollar buys more in China than in the US."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def productividad_hora():
    areas = ["USA", "CHN", "X92", "JPN", *geo.EU27]
    rows = sources.ilo("DF_GDP_2HRW_NOC_NB", f"{'+'.join(areas)}..", start="2000")
    out = []
    for r in rows:
        if r["FREQ"] != "A" or not r["OBS_VALUE"] or int(r["TIME_PERIOD"]) > LAST_YEAR:
            continue
        code = geo.from_iso3(r["REF_AREA"])
        if code:
            out.append({"geo": code, "time": r["TIME_PERIOD"], "value": round(float(r["OBS_VALUE"]), 2)})
    return chart(
        id="pg2-productividad-hora",
        lens="gigantes", theme="productividad",
        title={"es": "Por cada hora trabajada, la UE produce un 13 % menos que EE. UU., y la distancia ha crecido desde 2019",
               "en": "For every hour worked, the EU produces 13% less than the US, and the gap has widened since 2019"},
        subtitle={"es": "PIB por hora trabajada, en dólares constantes de 2021 en paridad de poder adquisitivo",
                  "en": "GDP per hour worked, in constant 2021 dollars at purchasing power parity"},
        unit={"es": "dólares por hora (PPA de 2021)", "en": "dollars per hour (2021 PPP)"},
        source={"name": "OIT, ILOSTAT (estimaciones modelizadas)", "dataset": "DF_GDP_2HRW_NOC_NB",
                "url": "https://ilostat.ilo.org/data/", "license": "CC BY 4.0"},
        notes={"es": ["Estimaciones modelizadas de la Organización Internacional del Trabajo, que combinan cuentas nacionales y encuestas de empleo.",
                      f"La OIT publica proyecciones para años posteriores a {LAST_YEAR}; aquí no se muestran."],
               "en": ["Modelled estimates by the International Labour Organization, combining national accounts and labour surveys.",
                      f"The ILO publishes projections beyond {LAST_YEAR}; they are not shown here."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [peso_pib_mundial, productividad_hora]
