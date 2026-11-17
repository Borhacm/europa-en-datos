"""N09. Envejecimiento país por país: cuánto han crecido los mayores de 65 años desde 2005 y dónde hay más mayores de 80."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

START, END = "2005", "2025"

COMMON_NOTES = {
    "es": ["Población residente a 1 de enero de cada año, según los registros y estimaciones de cada instituto nacional de estadística (indicadores de estructura de la población de Eurostat).",
           "El porcentaje de mayores depende de cuánto se vive, de cuántos niños nacen y de quién llega o se va: un país con mucha inmigración joven envejece más despacio aunque su gente viva lo mismo."],
    "en": ["Resident population on 1 January of each year, from the registers and estimates of each national statistical office (Eurostat population structure indicators).",
           "The share of older people depends on how long people live, how many children are born and who arrives or leaves: a country with a lot of young immigration ages more slowly even if its people live just as long."],
}


def _eu(rows):
    return [r for r in rows if r["geo"] in geo.EU27 or r["geo"] == "EU27"]


def mayores_cambio():
    raw = sources.eurostat("demo_pjanind", indic_de="PC_Y65_MAX", time=[START, END])
    out = _eu(from_eurostat(raw, []))
    v = {(r["geo"], r["time"]): r["value"] for r in out}
    rise = {c: round(v[(c, END)] - v[(c, START)], 1) for c in geo.EU27}
    order = sorted(geo.EU27, key=lambda c: -rise[c])
    young_2005 = sorted(geo.EU27, key=lambda c: v[(c, START)])
    assert order[0] == "POL" and rise["POL"] == 7.9 and young_2005.index("POL") == 3, (order[:3], young_2005[:4])
    assert v[("EU27", START)] == 16.7 and v[("EU27", END)] == 21.9, (v[("EU27", START)], v[("EU27", END)])
    return chart(
        id="n09-mayores-cambio",
        lens="dentro", theme="demografia",
        title={"es": f"Polonia, uno de los países más jóvenes de la UE en {START}, es el que más ha envejecido: el {v[('POL', END)]:g} % de su población tiene 65 años o más, {rise['POL']:g} puntos más".replace(".", ","),
               "en": f"Poland, one of the youngest EU countries in {START}, has aged the most: {v[('POL', END)]:g}% of its population is 65 or older, {rise['POL']:g} points more"},
        subtitle={"es": f"Población de 65 años o más, en % de la población total, a 1 de enero de {START} y de {END}",
                  "en": f"Population aged 65 or older, as % of the total population, on 1 January {START} and {END}"},
        unit={"es": "% de la población", "en": "% of the population"},
        source=eurostat_source("demo_pjanind"),
        notes={"es": COMMON_NOTES["es"] + [
                   f"Los datos de {END} de Polonia y de la UE son estimados y provisionales; los de Francia, provisionales, y los de Rumanía, estimados (marcas «e» y «p» de Eurostat).",
                   "La UE es la de 27 países en los dos años. Las cifras de la UE, EE. UU. y China del tema Demografía vienen del Banco Mundial (estimaciones de Naciones Unidas) y no coinciden exactamente con las de Eurostat."],
               "en": COMMON_NOTES["en"] + [
                   f"The {END} figures for Poland and the EU are estimated and provisional; France's are provisional and Romania's estimated (Eurostat flags \"e\" and \"p\").",
                   "The EU is the 27-country EU in both years. The EU, US and China figures in the Population topic come from the World Bank (United Nations estimates) and do not exactly match Eurostat's."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def mayores_80():
    raw = sources.eurostat("demo_pjanind", indic_de="PC_Y80_MAX", time=END)
    out = _eu(from_eurostat(raw, []))
    v = {r["geo"]: r["value"] for r in out}
    order = sorted(geo.EU27, key=lambda c: -v[c])
    assert order[0] == "ITA" and order[-1] == "SVK" and v["ITA"] == 7.8 and v["SVK"] == 3.7, (order[0], order[-1])
    return chart(
        id="n09-mayores-80",
        lens="dentro", theme="demografia",
        title={"es": f"En Italia, el {v['ITA']:g} % de los habitantes tiene 80 años o más; en Eslovaquia, el {v['SVK']:g} %".replace(".", ","),
               "en": f"In Italy, {v['ITA']:g}% of residents are 80 or older; in Slovakia, {v['SVK']:g}%"},
        subtitle={"es": f"Población de 80 años o más, en % de la población total, a 1 de enero de {END}",
                  "en": f"Population aged 80 or older, as % of the total population, on 1 January {END}"},
        unit={"es": "% de la población", "en": "% of the population"},
        source=eurostat_source("demo_pjanind"),
        notes={"es": COMMON_NOTES["es"] + [
                   "Los mayores de 80 años son los que más usan la sanidad y los cuidados de larga duración, pero este dato no dice cuántos necesitan ayuda ni quién se la da.",
                   "Los datos de Polonia y de la UE son estimados y provisionales; los de Francia, provisionales, y los de Rumanía, estimados."],
               "en": COMMON_NOTES["en"] + [
                   "People aged 80 and over are the heaviest users of health and long-term care, but this figure does not say how many need help or who provides it.",
                   "The figures for Poland and the EU are estimated and provisional; France's are provisional and Romania's estimated."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [mayores_cambio, mayores_80]
