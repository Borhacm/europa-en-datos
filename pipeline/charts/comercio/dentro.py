"""Comercio. Mirada 3: el mercado único y las dependencias de cada país."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

ENLARGEMENT = "2004"  # la gran ampliación: punto de partida comparable para los 27


def comercio_intra():
    rows = sources.eurostat("ext_lt_intratrd", indic_et="PC_TOT_EXP", partner="EU27_2020", sitc06="TOTAL")
    latest = max(r["time"] for r in rows)
    rows = [r for r in rows if r["time"] in (ENLARGEMENT, latest)]
    out = from_eurostat(rows, [])
    return chart(
        id="cd1-comercio-intra",
        lens="dentro", theme="comercio",
        title={"es": "El primer cliente de Europa es Europa: seis de cada diez euros exportados se quedan en la UE",
               "en": "Europe's first customer is Europe: six in every ten euros exported stay in the EU"},
        subtitle={"es": f"Parte de las exportaciones de bienes de cada país que va a otros países de la UE, en %, {ENLARGEMENT} y {latest}",
                  "en": f"Share of each country's goods exports that goes to other EU countries, in %, {ENLARGEMENT} and {latest}"},
        unit={"es": "% de las exportaciones", "en": "% of exports"},
        source=eurostat_source("ext_lt_intratrd"),
        notes={"es": ["Se compara con 2004, el año de la mayor ampliación de la UE.",
                      "Los países con grandes centros de multinacionales (Irlanda, Chipre o Eslovenia) pueden reflejar reexportaciones hacia fuera de la UE."],
               "en": ["Compared with 2004, the year of the EU's largest enlargement.",
                      "Countries hosting large multinational hubs (Ireland, Cyprus or Slovenia) may reflect re-exports outside the EU."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def dependencia_energetica():
    rows = sources.eurostat("nrg_ind_id", siec="TOTAL", unit="PC")
    out = from_eurostat(rows, [])
    return chart(
        id="cd2-dependencia-energetica",
        lens="dentro", theme="comercio",
        title={"es": "La UE importa más de la mitad de su energía. Solo Estonia es casi autosuficiente",
               "en": "The EU imports more than half its energy. Only Estonia is almost self-sufficient"},
        subtitle={"es": "Dependencia de las importaciones de energía: importaciones netas sobre la energía disponible, en %",
                  "en": "Energy import dependency: net imports as a share of available energy, in %"},
        unit={"es": "% de la energía disponible", "en": "% of available energy"},
        source=eurostat_source("nrg_ind_id"),
        notes={"es": ["Valores por encima del 100 % indican que el país importa más energía de la que consume, por ejemplo para acumular reservas.",
                      "Valores negativos indican que el país exporta más energía de la que importa."],
               "en": ["Values above 100% mean the country imports more energy than it uses, for instance to build up stocks.",
                      "Negative values mean the country exports more energy than it imports."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


EXPOSURE_YEAR = "2025"
# Comext usa GR para Grecia; Eurostat, EL
COMEXT_CODE = {c: ("GR" if geo.COUNTRIES[c][0] == "EL" else geo.COUNTRIES[c][0]) for c in geo.EU27}


def exposicion_eeuu():
    reporters = {v: k for k, v in COMEXT_CODE.items()} | {"EU": "EU27"}
    rows = sources.comext("DS-045409", reporter=list(reporters), partner="US", product="TOTAL", flow="2",
                          freq="A", indicators="VALUE_IN_EUROS", time=EXPOSURE_YEAR)
    exports = {reporters[r["reporter"]]: r["value"] for r in rows}
    gdp = {geo.from_eurostat(r["geo"]): r["value"] for r in sources.eurostat(
        "nama_10_gdp", na_item="B1GQ", unit="CP_MEUR", time=EXPOSURE_YEAR, geo=["EU27_2020", *(geo.COUNTRIES[c][0] for c in geo.EU27)])}
    out = [{"geo": g, "time": EXPOSURE_YEAR, "value": round(100 * v / (gdp[g] * 1e6), 2), "exports_bn": round(v / 1e9, 1)}
           for g, v in exports.items() if gdp.get(g)]
    assert len(out) == 28, f"exposicion_eeuu: {len(out)} de 28"
    return chart(
        id="cd3-exposicion-eeuu",
        lens="dentro", theme="comercio",
        title={"es": "Irlanda exporta a EE. UU. el equivalente al 18,5 % de su PIB; Alemania, el 3,2 %, y España, el 1 %",
               "en": "Ireland's exports to the US equal 18.5% of its GDP; Germany's, 3.2%, and Spain's, 1%"},
        subtitle={"es": f"Exportaciones de bienes a EE. UU., en % del PIB de cada país, {EXPOSURE_YEAR}",
                  "en": f"Goods exports to the US, as % of each country's GDP, {EXPOSURE_YEAR}"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source={"name": "Eurostat, Comext (comercio por producto) y cuentas nacionales", "dataset": "DS-045409",
                "url": "https://ec.europa.eu/eurostat/comext/newxtweb/", "license": "CC BY 4.0",
                "also": [{"name": "Eurostat, nama_10_gdp (PIB)", "url": "https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table"}]},
        notes={"es": ["Las exportaciones se atribuyen al país desde el que salen de la UE. Los puertos de Bélgica y Países Bajos pueden despachar bienes producidos en otros países, así que su exposición real puede ser menor y la de sus vecinos, mayor.",
                      "En 2025, el 82 % de lo que Irlanda vendió a EE. UU. fueron químicos orgánicos y productos farmacéuticos (capítulos 29 y 30 del Sistema Armonizado, 91.200 de 111.200 millones de euros en Comext).",
                      "Compara un flujo (exportaciones) con el PIB, que mide valor añadido: no es la parte del PIB que depende de EE. UU., sino una medida de tamaño relativo."],
               "en": ["Exports are attributed to the country they leave the EU from. Belgian and Dutch ports may ship goods produced in other countries, so their real exposure may be lower and their neighbours' higher.",
                      "In 2025, 82% of what Ireland sold to the US was organic chemicals and pharmaceuticals (Harmonised System chapters 29 and 30, 91.2 of 111.2 billion euros in Comext).",
                      "It compares a flow (exports) with GDP, which measures value added: it is not the share of GDP that depends on the US, but a measure of relative size."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [comercio_intra, exposicion_eeuu, dependencia_energetica]
