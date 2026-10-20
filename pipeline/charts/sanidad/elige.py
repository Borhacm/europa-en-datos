"""Sanidad. Mirada 2: sanidad pública frente a privada, y lo que pagan los hogares de su bolsillo."""

from collections import Counter

from lib import geo, sources
from lib.output import chart

from ..common import worldbank_rows, worldbank_source
from .gigantes import BLOCS, LAST_YEAR

GHED_NOTE = {
    "es": ["Estimaciones de la Organización Mundial de la Salud (base de datos de gasto sanitario mundial) publicadas por el Banco Mundial.",
           f"Se muestra hasta {LAST_YEAR}, el último año con datos de casi todos los países."],
    "en": ["World Health Organization estimates (Global Health Expenditure Database) published by the World Bank.",
           f"Shown up to {LAST_YEAR}, the last year with data for almost every country."],
}


def gasto_publico():
    rows = worldbank_rows("SH.XPD.GHED.CH.ZS", 2000, LAST_YEAR)
    out = [{**r, "value": round(r["value"], 2)} for r in rows if r["geo"] in BLOCS]
    return chart(
        id="sae1-gasto-publico",
        lens="elige", theme="sanidad",
        title={"es": "Tres de cada cuatro euros de la sanidad europea son públicos; en EE. UU. y en China, algo más de la mitad",
               "en": "Three in every four euros of European healthcare are public; in the US and China, just over half"},
        subtitle={"es": "Gasto sanitario de las administraciones públicas y la seguridad social, en % del gasto sanitario corriente",
                  "en": "Health spending by government and social security, as % of current health expenditure"},
        unit={"es": "% del gasto sanitario", "en": "% of health spending"},
        source=worldbank_source("SH.XPD.GHED.CH.ZS", "gasto sanitario público nacional (% del gasto sanitario corriente)"),
        notes={"es": [*GHED_NOTE["es"],
                      "Incluye los seguros sociales obligatorios. En EE. UU., Medicare y Medicaid cuentan como gasto público; los seguros de empresa, como privado.",
                      "No incluye la ayuda exterior, muy pequeña en estos países."],
               "en": [*GHED_NOTE["en"],
                      "Includes compulsory social health insurance. In the US, Medicare and Medicaid count as public spending; employer insurance, as private.",
                      "Excludes foreign aid, which is very small in these countries."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
    )


def pago_bolsillo():
    share = worldbank_rows("SH.XPD.OOPC.CH.ZS", 2000, LAST_YEAR)
    per_capita = worldbank_rows("SH.XPD.OOPC.PP.CD", 2000, LAST_YEAR)
    out = ([{**r, "measure": "share", "value": round(r["value"], 2)} for r in share]
           + [{**r, "measure": "per_capita", "value": round(r["value"], 0)} for r in per_capita])
    return chart(
        id="sae2-pago-bolsillo",
        lens="elige", theme="sanidad",
        title={"es": "En 24 de los 27 países de la UE, los pacientes pagan de su bolsillo una parte del gasto sanitario mayor que en EE. UU.",
               "en": "In 24 of the 27 EU countries, patients pay a larger share of health spending out of pocket than in the US"},
        subtitle={"es": "Pagos directos de los hogares (copagos, medicamentos, consultas privadas), en % del gasto sanitario corriente",
                  "en": "Direct payments by households (co-payments, medicines, private visits), as % of current health expenditure"},
        unit={"es": "% del gasto sanitario", "en": "% of health spending"},
        source=worldbank_source("SH.XPD.OOPC.CH.ZS", "pagos directos de los hogares (% del gasto sanitario corriente)",
                                ) | {"also": [worldbank_source("SH.XPD.OOPC.PP.CD", "pagos directos de los hogares por habitante (PPA)")]},
        notes={"es": [*GHED_NOTE["es"],
                      "Es una proporción: como EE. UU. gasta mucho más, sus hogares pagan más dólares de su bolsillo por habitante aunque la proporción sea menor. El archivo de datos incluye también ese importe por habitante.",
                      "No incluye las primas de seguros privados, que se cuentan aparte."],
               "en": [*GHED_NOTE["en"],
                      "This is a share: since the US spends far more, its households pay more dollars out of pocket per person even though the share is smaller. The data file also includes that amount per person.",
                      "Premiums for private insurance are not included; they are counted separately."]},
        rows=sorted(out, key=lambda r: (r["measure"], r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"measure": {
            "share": {"es": "% del gasto sanitario", "en": "% of health spending"},
            "per_capita": {"es": "Dólares por habitante (PPA)", "en": "Dollars per person (PPP)"}}}},
    )


MORTALITY = {
    "TRTM": {"es": "Tratable (con atención a tiempo)", "en": "Treatable (with timely care)"},
    "PREVM": {"es": "Prevenible (con prevención y salud pública)", "en": "Preventable (with prevention and public health)"},
}


def mortalidad_evitable():
    rows = sources.oecd("OECD.ELS.HD,DSD_HEALTH_STAT@DF_AM,1.1",
                        f"{'+'.join(['USA', *geo.EU27])}.A.TRTM+PREVM.DT_10P5HB._T._T...STANDARD....", start="2010")
    out = [{"geo": r["REF_AREA"], "time": r["TIME_PERIOD"], "measure": r["MEASURE"], "value": round(float(r["OBS_VALUE"]))}
           for r in rows if r["OBS_VALUE"]]
    # Año de referencia: el más reciente con EE. UU. y casi todos los países de la UE
    counts = Counter(r["time"] for r in out if r["measure"] == "TRTM" and r["geo"] != "USA")
    ref_year = max(t for t, n in counts.items() if n >= 24 and any(r["geo"] == "USA" and r["time"] == t for r in out))
    out = [r for r in out if r["time"] == ref_year]
    return chart(
        id="sae3-mortalidad-evitable",
        lens="elige", theme="sanidad",
        title={"es": "EE. UU. gasta más del doble, pero tiene más muertes por causas tratables que 16 de los 24 países de la UE con datos",
               "en": "The US spends more than twice as much, but has more deaths from treatable causes than 16 of the 24 EU countries with data"},
        subtitle={"es": f"Muertes antes de los 75 años que se podrían haber evitado, por cada 100.000 habitantes, tasa estandarizada por edad, {ref_year}",
                  "en": f"Deaths before age 75 that could have been avoided, per 100,000 people, age-standardised rate, {ref_year}"},
        unit={"es": "muertes por 100.000 habitantes", "en": "deaths per 100,000 people"},
        source={"name": "OCDE, Health Status: mortalidad evitable", "dataset": "DSD_HEALTH_STAT@DF_AM",
                "url": "https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_HEALTH_STAT%40DF_AM&df[ag]=OECD.ELS.HD",
                "license": "CC BY 4.0"},
        notes={"es": ["Tratable: muertes que una atención sanitaria a tiempo y eficaz podría haber evitado (por ejemplo, algunos cánceres, infartos o infecciones). Prevenible: muertes que se podrían haber evitado con prevención y salud pública (por ejemplo, por tabaco, alcohol, accidentes o sobredosis).",
                      "Tasas estandarizadas con la población de referencia de la OCDE de 2010, para que la edad de cada población no altere la comparación. No hay datos de Chipre, Croacia ni Malta para este año."],
               "en": ["Treatable: deaths that timely and effective healthcare could have avoided (for example, some cancers, heart attacks or infections). Preventable: deaths that could have been avoided with prevention and public health (for example, from tobacco, alcohol, accidents or overdoses).",
                      "Rates standardised to the OECD 2010 reference population, so that each population's age does not distort the comparison. No data for Cyprus, Croatia or Malta for this year."]},
        rows=sorted(out, key=lambda r: (r["measure"], r["geo"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"measure": MORTALITY}, "ref_year": ref_year},
    )


BUILDERS = [gasto_publico, pago_bolsillo, mortalidad_evitable]
