"""Productividad. Mirada 3: la convergencia entre los 27 y las diferencias entre regiones."""

from lib import geo, sources
from lib.output import chart

from ..common import GISCO_SOURCE, eurostat_source, from_eurostat, nuts_map

ENLARGEMENT = "2004"


def convergencia():
    rows = sources.eurostat("sdg_10_10", indic_ppp="VI_PPS_EU27_2020_HAB", ppp_cat18="GDP")
    latest = max(r["time"] for r in rows if r["geo"] == "EU27_2020")
    out = from_eurostat([r for r in rows if r["time"] in (ENLARGEMENT, latest)], [])
    return chart(
        id="pd1-convergencia",
        lens="dentro", theme="productividad",
        title={"es": "El este de Europa se ha acercado a la media desde 2004. El sur, no",
               "en": "Eastern Europe has closed in on the average since 2004. The south has not"},
        subtitle={"es": f"PIB por habitante en paridad de poder adquisitivo, índice UE = 100, {ENLARGEMENT} y {latest}",
                  "en": f"GDP per person at purchasing power parity, index EU = 100, {ENLARGEMENT} and {latest}"},
        unit={"es": "índice (UE = 100)", "en": "index (EU = 100)"},
        source=eurostat_source("sdg_10_10"),
        notes={"es": ["Luxemburgo e Irlanda aparecen muy por encima de la media por los trabajadores transfronterizos (Luxemburgo) y la contabilidad de las multinacionales (Irlanda)."],
               "en": ["Luxembourg and Ireland appear far above average because of cross-border workers (Luxembourg) and multinational accounting (Ireland)."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def productividad_paises():
    rows = sources.eurostat("nama_10_lp_ulc", na_item="RLPR_HW", unit="I15")
    v = {(r["geo"], r["time"]): r["value"] for r in rows}
    latest = max(t for (g, t) in v if g == "EU27_2020")
    out = []
    for r in from_eurostat([r for r in rows if r["time"] == latest], []):
        src = "EU27_2020" if r["geo"] == "EU27" else geo.COUNTRIES[r["geo"]][0]
        base = v.get((src, ENLARGEMENT))
        if base and r["geo"] in (*geo.EU27, "EU27"):
            out.append({"geo": r["geo"], "time": latest, "value": round(100 * (v[(src, latest)] / base - 1), 1)})
    return chart(
        id="pd3-productividad-paises",
        lens="dentro", theme="productividad",
        title={"es": "Desde 2004, la productividad por hora se ha más que duplicado en Rumanía; en Italia apenas ha cambiado y en Grecia ha caído",
               "en": "Since 2004, output per hour has more than doubled in Romania; in Italy it has barely changed and in Greece it has fallen"},
        subtitle={"es": f"Variación de la productividad real por hora trabajada entre {ENLARGEMENT} y {latest}, en %",
                  "en": f"Change in real labour productivity per hour worked between {ENLARGEMENT} and {latest}, in %"},
        unit={"es": "% de variación", "en": "% change"},
        source=eurostat_source("nama_10_lp_ulc"),
        notes={"es": ["PIB a precios constantes de cada país por hora trabajada. Mide cuánto ha crecido cada economía, no su nivel frente a las demás.",
                      "Irlanda sale muy arriba porque parte de su PIB son beneficios de multinacionales que salen del país; su oficina de estadística publica por eso otra medida, la renta nacional modificada (GNI*).",
                      f"{latest}: primeras estimaciones de las cuentas nacionales, que pueden revisarse."],
               "en": ["GDP at each country's constant prices per hour worked. It measures how much each economy has grown, not its level compared with the others.",
                      "Ireland comes out very high because part of its GDP is multinational profits that leave the country; its statistics office therefore publishes another measure, modified national income (GNI*).",
                      f"{latest}: first national accounts estimates, which may be revised."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def mapa_renta():
    rows = sources.eurostat("nama_10r_2gdp", unit="PPS_HAB_EU27_2020")
    # Solo regiones NUTS 2 de la UE (fuera de la UE la cobertura por años es distinta y desplazaría el año de referencia)
    eu2 = {geo.COUNTRIES[c][0] for c in geo.EU27}
    rows = [r for r in rows if len(r["geo"]) == 4 and r["geo"][:2] in eu2]
    out, extra = nuts_map(rows)
    return chart(
        id="pd2-mapa-renta",
        lens="dentro", theme="productividad",
        title={"es": "Las regiones de las capitales tiran de la renta europea; el sur y el este quedan por debajo de la media",
               "en": "Capital regions drive European income; the south and east sit below average"},
        subtitle={"es": f"PIB por habitante por región en paridad de poder adquisitivo, en % de la media de la UE, {extra['latest']}",
                  "en": f"GDP per person by region at purchasing power parity, as % of the EU average, {extra['latest']}"},
        unit={"es": "% de la media de la UE", "en": "% of EU average"},
        source=eurostat_source("nama_10r_2gdp", also=[GISCO_SOURCE]),
        notes={"es": ["El PIB se mide donde se produce: las regiones con muchos trabajadores que viven en otra región (como las capitales) salen por encima de su renta real.",
                      "La escala de color se corta en el 200 %: las pocas regiones por encima aparecen con el color más intenso."],
               "en": ["GDP is measured where it is produced: regions with many workers living elsewhere (such as capitals) come out above their residents' real income.",
                      "The colour scale is capped at 200%: the few regions above it take the darkest colour."]},
        rows=out,
        geos=geo.geo_table(extra["best_level"]),
        extra={**extra, "map_max": 200},
    )


BUILDERS = [convergencia, productividad_paises, mapa_renta]
