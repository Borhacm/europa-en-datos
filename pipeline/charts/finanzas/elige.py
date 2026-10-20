"""Finanzas públicas. Mirada 2: cuánto recauda la UE frente a EE. UU., con qué impuestos y en qué lo gasta."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source

BLOC_PAIR = {"EU27": {"es": "UE", "en": "EU"}, "USA": {"es": "EE. UU.", "en": "US"}}

# Impuestos: Global Revenue Statistics de la OCDE, que cubre a los 27 (menos Chipre), EE. UU. y China con la misma clasificación
REV_FLOW = "OECD.CTP.TPS,DSD_REV_COMP_GLOBAL@DF_RSGLOBAL,2.1"
REV_YEAR = "2023"
REV_SOURCE = {"name": "OCDE, Global Revenue Statistics", "dataset": "DSD_REV_COMP_GLOBAL@DF_RSGLOBAL",
              "url": "https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_REV_COMP_GLOBAL%40DF_RSGLOBAL&df[ag]=OECD.CTP.TPS",
              "license": "CC BY 4.0"}
TAXES = {
    "T_1000": {"es": "Renta y beneficios", "en": "Income and profits", "parts": ["T_1000"]},
    "T_2000": {"es": "Cotizaciones sociales", "en": "Social contributions", "parts": ["T_2000"]},
    "T_5000": {"es": "Consumo (IVA y otros)", "en": "Consumption (VAT etc.)", "parts": ["T_5000"]},
    "T_4000": {"es": "Propiedad", "en": "Property", "parts": ["T_4000"]},
    "T_OTH": {"es": "Otros", "en": "Other", "parts": ["T_3000", "T_6000"]},
}


def _revenue(unit: str) -> dict[tuple[str, str], float]:
    rows = sources.oecd(REV_FLOW, f".TAX_REV.S13...{unit}.A", start=REV_YEAR)
    return {(r["REF_AREA"], r["STANDARD_REVENUE"]): float(r["OBS_VALUE"]) for r in rows
            if r["TIME_PERIOD"] == REV_YEAR and r["SECTOR"] == "S13" and r["CTRY_SPECIFIC_REVENUE"] == "_T" and r["OBS_VALUE"]}


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def impuestos():
    pct, usd = _revenue("PT_B1GQ"), _revenue("USD")
    eu = [c for c in geo.EU27 if (c, "_T") in pct and (c, "_T") in usd]
    assert len(eu) >= 26, eu
    # PIB de cada país en dólares, deducido de la recaudación en dólares y en % del PIB
    gdp = sum(usd[(c, "_T")] / (pct[(c, "_T")] / 100) for c in eu)
    out = []
    for code, t in [("_T", {"parts": ["_T"]}), *TAXES.items()]:
        e = sum(usd.get((c, part), 0) for c in eu for part in t["parts"]) / gdp * 100
        u = sum(pct.get(("USA", part), 0) for part in t["parts"])
        if code == "_T":
            total = (round(e, 1), round(u, 1))
            continue
        out += [{"geo": code, "time": REV_YEAR, "bloc": "EU27", "value": round(e, 1)},
                {"geo": code, "time": REV_YEAR, "bloc": "USA", "value": round(u, 1)}]
    gap = round(total[0] - total[1], 1)
    v = {(r["geo"], r["bloc"]): r["value"] for r in out}
    assert abs(v[("T_1000", "EU27")] - v[("T_1000", "USA")]) < 0.5, "el titular dice que la renta recauda lo mismo"
    return chart(
        id="fpe1-impuestos",
        lens="elige", theme="finanzas",
        title={"es": f"La UE recauda en impuestos {fmt_es(gap)} puntos de PIB más que EE. UU.; la diferencia está en las cotizaciones sociales y los impuestos sobre el consumo, no en los de la renta",
               "en": f"The EU collects {gap:g} points of GDP more in taxes than the US; the gap lies in social contributions and consumption taxes, not in income taxes"},
        subtitle={"es": f"Ingresos tributarios de las administraciones públicas por tipo de impuesto, en % del PIB, {REV_YEAR}",
                  "en": f"General government tax revenue by type of tax, as % of GDP, {REV_YEAR}"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source={**REV_SOURCE, "also": [{"name": "FMI, World Economic Outlook (octubre de 2026)", "dataset": "NGDPD",
                                        "url": "https://www.imf.org/external/datamapper/NGDPD@WEO",
                                        "license": "Términos de uso del FMI (uso libre citando la fuente)"}]},
        notes={"es": [f"En total, la UE recauda el {fmt_es(total[0])} % de su PIB y EE. UU., el {fmt_es(total[1])} %.",
                      "UE: 26 países, ponderados por su PIB; la OCDE no publica todavía los datos de Chipre, que supone menos del 0,3 % del PIB de la UE.",
                      "Las cotizaciones sociales son las obligatorias que se pagan a las administraciones. En EE. UU., las pensiones privadas de empresa y los seguros médicos privados no cuentan como impuestos, aunque cumplen funciones que en Europa se pagan con cotizaciones.",
                      "Consumo: IVA, impuestos especiales (carburantes, tabaco, alcohol) y aranceles. EE. UU. no tiene IVA: sus impuestos sobre las ventas son de los estados."],
               "en": [f"In total, the EU collects {total[0]:g}% of its GDP and the US {total[1]:g}%.",
                      "EU: 26 countries, weighted by GDP; the OECD does not yet publish data for Cyprus, which accounts for less than 0.3% of EU GDP.",
                      "Social contributions are compulsory payments to government. In the US, private occupational pensions and private health insurance do not count as taxes, although they do jobs that in Europe are paid for with contributions.",
                      "Consumption: VAT, excise duties (fuel, tobacco, alcohol) and customs duties. The US has no VAT: its sales taxes are levied by the states."]},
        rows=out,
        geos={k: {"es": t["es"], "en": t["en"], "eu": False, "aggregate": False} for k, t in TAXES.items()},
        extra={"dimensions": {"bloc": BLOC_PAIR}},
    )


# Gasto por funciones (COFOG): la UE de Eurostat y EE. UU. de la OCDE, con la misma clasificación de Naciones Unidas
COFOG_YEAR = "2024"
COFOG_FLOW = "OECD.GOV.GIP,DSD_GOV_COFOG@DF_GOV_COFOG_YU,1.0"
COFOG_SOURCE = {"name": "OCDE, Government at a Glance: gasto público por funciones", "dataset": "DSD_GOV_COFOG@DF_GOV_COFOG_YU",
                "url": "https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_GOV_COFOG%40DF_GOV_COFOG_YU&df[ag]=OECD.GOV.GIP",
                "license": "CC BY 4.0"}
FUNCTIONS = {
    "GF10": {"es": "Protección social", "en": "Social protection"},
    "GF07": {"es": "Sanidad", "en": "Health"},
    "GF01": {"es": "Servicios generales", "en": "General services"},
    "GF09": {"es": "Educación", "en": "Education"},
    "GF04": {"es": "Asuntos económicos", "en": "Economic affairs"},
    "GF02": {"es": "Defensa", "en": "Defence"},
    "GF03": {"es": "Orden público", "en": "Public order"},
    "GF_OTH": {"es": "Otros", "en": "Other"},
}
OTHER = ["GF05", "GF06", "GF08"]


def gasto_funciones():
    eu_rows = sources.eurostat("gov_10a_exp", geo="EU27_2020", sector="S13", na_item="TE", unit="PC_GDP", time=COFOG_YEAR)
    eu = {r["cofog99"]: r["value"] for r in eu_rows}
    us_rows = sources.oecd(COFOG_FLOW, "A.USA.GE.PT_B1GQ.S13....", start=COFOG_YEAR)
    us = {r["EXPENDITURE"]: float(r["OBS_VALUE"]) for r in us_rows if r["TIME_PERIOD"] == COFOG_YEAR and r["OBS_VALUE"]}
    out = []
    for code in FUNCTIONS:
        parts = OTHER if code == "GF_OTH" else [code]
        out += [{"geo": code, "time": COFOG_YEAR, "bloc": "EU27", "value": round(sum(eu[p] for p in parts), 1)},
                {"geo": code, "time": COFOG_YEAR, "bloc": "USA", "value": round(sum(us[p] for p in parts), 1)}]
    v = {(r["geo"], r["bloc"]): r["value"] for r in out}
    total_eu = round(sum(v[(c, "EU27")] for c in FUNCTIONS), 1)
    total_us = round(sum(v[(c, "USA")] for c in FUNCTIONS), 1)
    gap = round(total_eu - total_us, 1)
    social = round(v[("GF10", "EU27")] - v[("GF10", "USA")], 1)
    assert social > gap and v[("GF07", "USA")] > v[("GF07", "EU27")] and v[("GF02", "USA")] > v[("GF02", "EU27")]
    return chart(
        id="fpe2-gasto-funciones",
        lens="elige", theme="finanzas",
        title={"es": f"La UE gasta {fmt_es(gap)} puntos de PIB más que EE. UU.: solo en protección social, {fmt_es(social)} más; EE. UU. dedica más a sanidad y defensa",
               "en": f"The EU spends {gap:g} points of GDP more than the US: in social protection alone, {social:g} more; the US spends more on health and defence"},
        subtitle={"es": f"Gasto de las administraciones públicas por funciones, en % del PIB, {COFOG_YEAR}",
                  "en": f"General government expenditure by function, as % of GDP, {COFOG_YEAR}"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source={**eurostat_source("gov_10a_exp"), "also": [COFOG_SOURCE]},
        notes={"es": [f"En total, las administraciones de la UE gastan el {fmt_es(total_eu)} % del PIB y las de EE. UU., el {fmt_es(total_us)} %.",
                      "Clasificación de las funciones de las administraciones públicas de Naciones Unidas (COFOG). UE: Eurostat; EE. UU.: OCDE, con los mismos códigos.",
                      f"Protección social incluye pensiones, desempleo, familia, invalidez y vivienda social. En la UE, solo la vejez supone el {fmt_es(eu['GF1002'])} % del PIB; la OCDE no publica ese desglose para EE. UU.",
                      "En EE. UU., la sanidad pública incluye Medicare y Medicaid. Otros: medio ambiente, vivienda y servicios comunitarios, y cultura y deporte."],
               "en": [f"In total, EU governments spend {total_eu:g}% of GDP and US governments {total_us:g}%.",
                      "United Nations Classification of the Functions of Government (COFOG). EU: Eurostat; US: OECD, with the same codes.",
                      f"Social protection includes pensions, unemployment, family, disability and social housing. In the EU, old age alone accounts for {eu['GF1002']:g}% of GDP; the OECD does not publish that breakdown for the US.",
                      "In the US, public health spending includes Medicare and Medicaid. Other: environment, housing and community amenities, and recreation and culture."]},
        rows=out,
        geos={k: {"es": f["es"], "en": f["en"], "eu": False, "aggregate": False} for k, f in FUNCTIONS.items()},
        extra={"dimensions": {"bloc": BLOC_PAIR}},
    )


BUILDERS = [impuestos, gasto_funciones]
