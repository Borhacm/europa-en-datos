"""Comercio. Mirada 2: ¿de quién depende Europa para comprar y para vender?"""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source

# Un dataset de Eurostat por grupo de productos
PRODUCTS = {
    "TOTAL": ("ext_lt_maineu", {"es": "Todos los bienes", "en": "All goods"}),
    "SITC7": ("ext_lt_mainmach", {"es": "Maquinaria y transporte", "en": "Machinery and transport"}),
    "SITC6_8": ("ext_lt_mainmanu", {"es": "Otras manufacturas", "en": "Other manufactured goods"}),
    "SITC5": ("ext_lt_mainchem", {"es": "Químicos", "en": "Chemicals"}),
}
PARTNERS = ["CN_X_HK", "US"]


def _partner_shares(indic: str) -> list[dict]:
    out = []
    for code, (dataset, _) in PRODUCTS.items():
        for r in sources.eurostat(dataset, indic_et=indic, partner=PARTNERS, geo="EU27_2020"):
            out.append({"geo": geo.from_eurostat(r["partner"]), "time": r["time"], "product": code,
                        "value": round(r["value"], 2)})
    return sorted(out, key=lambda r: (r["product"], r["geo"], r["time"]))


NOTES = {
    "es": ["Porcentaje sobre el comercio de la UE con países de fuera de la Unión.",
           "China no incluye Hong Kong."],
    "en": ["Share of the EU's trade with non-EU countries.",
           "China excludes Hong Kong."],
}


def importaciones_origen():
    out = _partner_shares("PC_IMP_PART")
    return chart(
        id="ce1-importaciones-origen",
        lens="elige", theme="comercio",
        title={"es": "Más de una de cada cinco importaciones de la UE ya llega de China; en maquinaria, más de una de cada tres",
               "en": "More than one in five EU imports now comes from China; in machinery, more than one in three"},
        subtitle={"es": "Parte de las importaciones de la UE desde fuera de la Unión que llega de China y de EE. UU., en %",
                  "en": "Share of the EU's imports from outside the Union that comes from China and the US, in %"},
        unit={"es": "% de las importaciones extra-UE", "en": "% of extra-EU imports"},
        source=eurostat_source("ext_lt_maineu", also=[
            {"name": f"Eurostat, {ds}", "url": f"https://ec.europa.eu/eurostat/databrowser/view/{ds}/default/table"}
            for ds in ("ext_lt_mainmach", "ext_lt_mainmanu", "ext_lt_mainchem")]),
        notes=NOTES,
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"product": {k: v[1] for k, v in PRODUCTS.items()}}},
    )


EU_EUROSTAT = {geo.COUNTRIES[c][0] for c in geo.EU27}
GAS_PARTNERS = {"RU": {"es": "Rusia", "en": "Russia"}, "NO": {"es": "Noruega", "en": "Norway"},
                "US": {"es": "Estados Unidos", "en": "United States"}, "DZ": {"es": "Argelia", "en": "Algeria"},
                "QA": {"es": "Catar", "en": "Qatar"}, "OTH": {"es": "Resto", "en": "Others"}}


def gas_origen():
    rows = sources.eurostat("nrg_ti_gas", geo="EU27_2020", siec="G3000", unit="TJ_GCV")
    by_year = {}
    for r in rows:
        # Solo países de fuera de la UE; los agregados (TOTAL, NSP, *_OTH) se descartan salvo los "otros" regionales
        p = r["partner"]
        if p in EU_EUROSTAT or p in ("TOTAL", "NSP") or r["time"] < "2010":
            continue
        y = by_year.setdefault(r["time"], {})
        key = p if p in GAS_PARTNERS else "OTH"
        y[key] = y.get(key, 0) + r["value"]
    out = []
    for t, parts in by_year.items():
        total = sum(parts.values())
        out += [{"geo": "EU27", "series": k, "time": t, "value": round(100 * v / total, 1)} for k, v in parts.items()]
    return chart(
        id="ce3-gas-origen",
        lens="elige", theme="comercio",
        title={"es": "Rusia pasó de casi la mitad del gas que la UE compra fuera al 14,6 %; Noruega y EE. UU. han ocupado su lugar",
               "en": "Russia went from almost half the gas the EU buys abroad to 14.6%; Norway and the US have taken its place"},
        subtitle={"es": "Origen de las importaciones de gas natural de la UE desde fuera de la Unión, en % del total",
                  "en": "Origin of the EU's natural gas imports from outside the Union, as % of the total"},
        unit={"es": "% de las importaciones extra-UE", "en": "% of extra-EU imports"},
        source=eurostat_source("nrg_ti_gas"),
        notes={"es": ["Gas por gasoducto y gas natural licuado (GNL), en energía (terajulios de poder calorífico superior).",
                      "El porcentaje es sobre lo que se importa de fuera de la UE: no cuenta el gas que se compran entre sí los países miembros. 'Resto' suma los demás países y los orígenes que Eurostat no detalla.",
                      "El origen es el país del que llega el gas según las estadísticas de energía, que no siempre es el país donde se extrae."],
               "en": ["Pipeline gas and liquefied natural gas (LNG), in energy terms (terajoules, gross calorific value).",
                      "The share is of imports from outside the EU: gas member states buy from each other is not counted. 'Others' adds the remaining countries and origins Eurostat does not detail.",
                      "The origin is the country the gas arrives from according to energy statistics, which is not always where it is extracted."]},
        rows=sorted(out, key=lambda r: (r["series"], r["time"])),
        geos=geo.geo_table(["EU27"]),
        extra={"dimensions": {"series": GAS_PARTNERS}},
    )


# Etiquetas cortas para que quepan al final de cada línea; las notas dan las partidas completas
CARS = {"870380": {"es": "Eléctricos", "en": "Electric"},
        "870360": {"es": "Enchufables", "en": "Plug-in"},
        "870340": {"es": "Híbridos", "en": "Hybrids"}}
CARS_FROM = "2019"


def coches_china():
    rows = sources.comext("DS-045409", reporter="EU", partner="CN", product=list(CARS), flow="1", freq="A",
                          indicators="VALUE_IN_EUROS")
    out = [{"geo": "EU27", "series": r["product"], "time": r["time"], "value": round(r["value"] / 1e9, 2)}
           for r in rows if r["time"] >= CARS_FROM]
    return chart(
        id="ce4-coches-china",
        lens="elige", theme="comercio",
        title={"es": "Tras los aranceles, la UE importa de China un 42 % menos en eléctricos, pero los híbridos casi compensan la caída",
               "en": "After the duties, EU imports of Chinese electric cars are down 42%, but hybrids almost make up for the fall"},
        subtitle={"es": "Importaciones de turismos de la UE desde China por tipo de motor, en miles de millones de euros",
                  "en": "EU imports of passenger cars from China by type of engine, in billions of euros"},
        unit={"es": "miles de millones de euros", "en": "billions of euros"},
        source={"name": "Eurostat, Comext (comercio por producto)", "dataset": "DS-045409",
                "url": "https://ec.europa.eu/eurostat/comext/newxtweb/", "license": "CC BY 4.0",
                "also": [{"name": "Reglamento de Ejecución (UE) 2024/2754 (derechos compensatorios definitivos)",
                          "url": "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R2754"}]},
        notes={"es": ["Eléctricos: partida 8703 80 del Sistema Armonizado (solo motor eléctrico). Enchufables: 8703 60 (híbridos de gasolina que se cargan en la red). Híbridos: 8703 40 (gasolina y eléctrico, no enchufables). Valor en euros corrientes, sin descontar la inflación.",
                      "El derecho compensatorio solo se aplica a los eléctricos de batería nuevos (partida 8703 80 10): provisional desde julio de 2024 y definitivo desde el 30 de octubre de 2024.",
                      "Mide valor, no número de coches: si bajan los precios, el valor baja aunque se vendan los mismos."],
               "en": ["Electric: Harmonised System heading 8703 80 (electric motor only). Plug-in: 8703 60 (petrol hybrids charged from the grid). Hybrids: 8703 40 (petrol and electric, not plug-in). Value in current euros, not adjusted for inflation.",
                      "The countervailing duty applies only to new battery electric vehicles (heading 8703 80 10): provisional from July 2024 and definitive from 30 October 2024.",
                      "It measures value, not the number of cars: if prices fall, value falls even if the same number are sold."]},
        rows=sorted(out, key=lambda r: (r["series"], r["time"])),
        geos=geo.geo_table(["EU27"]),
        extra={"dimensions": {"series": CARS}},
    )


BUILDERS = [importaciones_origen, gas_origen, coches_china]
