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


BUILDERS = [comercio_intra, dependencia_energetica]
