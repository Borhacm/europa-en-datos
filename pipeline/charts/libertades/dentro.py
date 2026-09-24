"""Libertades, bienestar y clima. Mirada 3: las diferencias entre los 27."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat, vdem_with_eu
from .gigantes import LIBDEM, VDEM_SOURCE

DEMOCRACY_FROM = "2010"


def democracia_ue():
    rows = vdem_with_eu(LIBDEM, since=int(DEMOCRACY_FROM), countries=[])
    latest = max(r["time"] for r in rows)
    # Se conserva "stat" para que la fila de la UE se etiquete como mediana
    out = [{k: v for k, v in r.items() if k != "measure" and not (k == "stat" and v == "country")}
           for r in rows if r["time"] in (DEMOCRACY_FROM, latest) and r["stat"] != "min"]
    return chart(
        id="ld1-democracia-ue",
        lens="dentro", theme="libertades",
        title={"es": "La calidad democrática ha bajado desde 2010 en 24 de los 27 países de la UE, con Hungría a la cabeza",
               "en": "Democratic quality has fallen since 2010 in 24 of the 27 EU countries, led by Hungary"},
        subtitle={"es": f"Índice de democracia liberal de V-Dem, de 0 a 1, {DEMOCRACY_FROM} y {latest}",
                  "en": f"V-Dem liberal democracy index, from 0 to 1, {DEMOCRACY_FROM} and {latest}"},
        unit={"es": "índice de 0 a 1", "en": "index from 0 to 1"},
        source=VDEM_SOURCE,
        notes={"es": ["La fila de la UE es la mediana de los 27 países.",
                      "Licencia CC BY-SA: los datos derivados deben compartirse con la misma licencia."],
               "en": ["The EU row is the median of the 27 countries.",
                      "CC BY-SA licence: derived data must be shared under the same licence."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def pobreza():
    rows = sources.eurostat("ilc_peps01n", age="TOTAL", sex="T", unit="PC")
    out = from_eurostat(rows, [])
    return chart(
        id="ld2-pobreza",
        lens="dentro", theme="libertades",
        title={"es": "Uno de cada cinco europeos está en riesgo de pobreza o exclusión social; en Bulgaria, Grecia o Rumanía, más de uno de cada cuatro",
               "en": "One in five Europeans is at risk of poverty or social exclusion; in Bulgaria, Greece or Romania, more than one in four"},
        subtitle={"es": "Personas en riesgo de pobreza o exclusión social, en % de la población",
                  "en": "People at risk of poverty or social exclusion, as % of the population"},
        unit={"es": "% de la población", "en": "% of the population"},
        source=eurostat_source("ilc_peps01n"),
        notes={"es": ["Incluye a quien tiene ingresos por debajo del 60 % de la mediana de su país, sufre carencia material y social grave o vive en un hogar con muy poco empleo.",
                      "Es una medida relativa a cada país: no compara el nivel de vida entre países."],
               "en": ["Includes anyone with income below 60% of their country's median, in severe material and social deprivation, or in a household with very low work intensity.",
                      "It is relative to each country: it does not compare living standards across countries."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def renovables():
    rows = sources.eurostat("nrg_ind_ren", nrg_bal="REN", unit="PC")
    out = from_eurostat(rows, [])
    return chart(
        id="ld3-renovables",
        lens="dentro", theme="libertades",
        title={"es": "Suecia ya obtiene dos tercios de su energía de fuentes renovables; la UE, una cuarta parte, lejos de su objetivo para 2030",
               "en": "Sweden already gets two thirds of its energy from renewables; the EU, a quarter, far from its 2030 target"},
        subtitle={"es": "Energía renovable, en % del consumo final bruto de energía",
                  "en": "Renewable energy, as % of gross final energy consumption"},
        unit={"es": "% del consumo de energía", "en": "% of energy consumption"},
        source=eurostat_source("nrg_ind_ren", also=[{
            "name": "Directiva de energías renovables, objetivo del 42,5 % para 2030",
            "url": "https://energy.ec.europa.eu/topics/renewable-energy/renewable-energy-directive-targets-and-rules/renewable-energy-targets_en"}]),
        notes={"es": ["Incluye electricidad, calor y transporte, no solo electricidad."],
               "en": ["Covers electricity, heating and transport, not just electricity."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"targets": [{"geo": "EU27", "time": "2030", "value": 42.5,
                            "label": {"es": "Objetivo de la UE para 2030", "en": "EU 2030 target"}}]},
    )


BUILDERS = [democracia_ue, pobreza, renovables]
