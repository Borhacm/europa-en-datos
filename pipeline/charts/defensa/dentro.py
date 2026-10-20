"""Defensa. Mirada 3: gasto en defensa por habitante y qué parte se invierte en cada país."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, worldbank_source

LAST = 2025
COFOG_YEAR = "2024"


def gasto_habitante():
    codes = [*geo.EU27, "USA"]
    mil = {r["iso3"]: r["value"] for r in sources.worldbank("MS.MIL.XPND.CD", codes, LAST, LAST)}
    pop = {r["iso3"]: r["value"] for r in sources.worldbank("SP.POP.TOTL", codes, LAST, LAST)}
    out = [{"geo": c, "time": str(LAST), "value": round(mil[c] / pop[c])} for c in codes if c in mil and c in pop]
    v = {r["geo"]: r["value"] for r in out}
    eu = sorted(geo.EU27, key=lambda c: v[c], reverse=True)
    top, low = eu[0], [c for c in eu if v[c] < 300]
    assert len(eu) == 27 and v[top] < v["USA"] and len(low) == 2
    return chart(
        id="dfd1-gasto-habitante",
        lens="dentro", theme="defensa",
        title={"es": f"Por habitante, {geo.name(top, 'es')} gasta en defensa el {round(v[top] / v['USA'] * 100)} % de lo que gasta EE. UU.; {geo.name(low[1], 'es')} y {geo.name(low[0], 'es')}, menos de 300 dólares",
               "en": f"Per person, {geo.name(top, 'en')} spends {round(v[top] / v['USA'] * 100)}% as much on defence as the US; {geo.name(low[1], 'en')} and {geo.name(low[0], 'en')}, less than 300 dollars"},
        subtitle={"es": f"Gasto militar por habitante, en dólares corrientes, {LAST}",
                  "en": f"Military expenditure per person, in current dollars, {LAST}"},
        unit={"es": "dólares por habitante", "en": "dollars per person"},
        source={**worldbank_source("MS.MIL.XPND.CD", "gasto militar (dólares corrientes), con datos del SIPRI"),
                "also": [worldbank_source("SP.POP.TOTL", "población total")]},
        notes={"es": ["Gasto militar del SIPRI publicado por el Banco Mundial, dividido entre la población de cada país.",
                      "En dólares corrientes, sin corregir las diferencias de precios entre países: un soldado o un cuartel cuestan menos en unos países que en otros."],
               "en": ["SIPRI military expenditure published by the World Bank, divided by each country's population.",
                      "In current dollars, without correcting for price differences between countries: a soldier or a barracks costs less in some countries than in others."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def inversion_paises():
    rows = sources.eurostat("gov_10a_exp", sector="S13", cofog99="GF02", unit="MIO_EUR", time=COFOG_YEAR)
    v = {(r["geo"], r["na_item"]): r["value"] for r in rows}
    out = []
    for c in [*geo.EU27, "EU27"]:
        code = "EU27_2020" if c == "EU27" else geo.COUNTRIES[c][0]
        if v.get((code, "TE")):
            out.append({"geo": c, "time": COFOG_YEAR, "value": round(100 * v.get((code, "P51G"), 0) / v[(code, "TE")], 1)})
    s = {r["geo"]: r["value"] for r in out}
    ranked = sorted(geo.EU27, key=lambda c: s[c], reverse=True)
    low = [c for c in ranked if s[c] < 10]
    assert len(ranked) == 27 and s[ranked[1]] > 38
    return chart(
        id="dfd2-inversion-paises",
        lens="dentro", theme="defensa",
        title={"es": f"{geo.name(ranked[0], 'es')} y {geo.name(ranked[1], 'es')} dedican cerca del 40 % o más de su gasto en defensa a inversión; {len(low)} países, menos del 10 %",
               "en": f"{geo.name(ranked[0], 'en')} and {geo.name(ranked[1], 'en')} put around 40% or more of their defence spending into investment; {len(low)} countries, less than 10%"},
        subtitle={"es": f"Inversión (formación bruta de capital) en % del gasto de las administraciones públicas en defensa, {COFOG_YEAR}",
                  "en": f"Investment (gross capital formation) as % of general government defence expenditure, {COFOG_YEAR}"},
        unit={"es": "% del gasto en defensa", "en": "% of defence spending"},
        source=eurostat_source("gov_10a_exp"),
        notes={"es": ["Función 02 (defensa) de la clasificación COFOG. Inversión: equipos e infraestructuras militares.",
                      "Un solo contrato grande puede mover mucho la proporción de un país en un año."],
               "en": ["Function 02 (defence) of the COFOG classification. Investment: military equipment and infrastructure.",
                      "A single large contract can move a country's share a lot in one year."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [gasto_habitante, inversion_paises]
