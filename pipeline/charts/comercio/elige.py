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


def exportaciones_destino():
    out = _partner_shares("PC_EXP_PART")
    return chart(
        id="ce2-exportaciones-destino",
        lens="elige", theme="comercio",
        title={"es": "Para vender, la UE depende de EE. UU.: su primer cliente, muy por delante de China",
               "en": "To sell, the EU depends on the US: its first customer, far ahead of China"},
        subtitle={"es": "Parte de las exportaciones de la UE fuera de la Unión que va a EE. UU. y a China, en %",
                  "en": "Share of the EU's exports outside the Union that goes to the US and China, in %"},
        unit={"es": "% de las exportaciones extra-UE", "en": "% of extra-EU exports"},
        source=eurostat_source("ext_lt_maineu", also=[
            {"name": f"Eurostat, {ds}", "url": f"https://ec.europa.eu/eurostat/databrowser/view/{ds}/default/table"}
            for ds in ("ext_lt_mainmach", "ext_lt_mainmanu", "ext_lt_mainchem")]),
        notes=NOTES,
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"product": {k: v[1] for k, v in PRODUCTS.items()}}},
    )


BUILDERS = [importaciones_origen, exportaciones_destino]
