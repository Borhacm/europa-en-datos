"""N01. Cuánto ha subido la vivienda desde 2015, país por país."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

BASE, LAST = "2015", "2025"


def precio_vivienda():
    rows = sources.eurostat("prc_hpi_a", purchase="TOTAL", unit="I15_A_AVG", time=LAST)
    out = [{**r, "value": round(r["value"] - 100, 1)} for r in from_eurostat(rows, [])]
    # Referencia: inflación acumulada de la UE en el mismo periodo (IPCA, índice 2015 = 100)
    hicp = {r["time"]: r["value"] for r in sources.eurostat(
        "prc_hicp_aind", unit="INX_A_AVG", coicop="CP00", geo="EU27_2020", time=[BASE, LAST])}
    inflation = round(100 * hicp[LAST] / hicp[BASE] - 100, 1)
    inflation_es = f"{inflation}".replace(".", ",")
    return chart(
        id="n01-vivienda-precios",
        lens="dentro", theme="libertades",
        title={"es": f"La vivienda ha subido un {round(next(r['value'] for r in out if r['geo'] == 'EU27'))} % en la UE desde {BASE}, casi el doble que los precios en general",
               "en": f"Housing has risen {round(next(r['value'] for r in out if r['geo'] == 'EU27'))}% in the EU since {BASE}, almost twice as much as prices overall"},
        subtitle={"es": f"Subida del precio de la vivienda entre {BASE} y {LAST}, en %",
                  "en": f"Rise in house prices between {BASE} and {LAST}, in %"},
        unit={"es": "% de subida", "en": "% rise"},
        source=eurostat_source("prc_hpi_a", also=[{
            "name": "Eurostat, prc_hicp_aind (inflación)",
            "url": "https://ec.europa.eu/eurostat/databrowser/view/prc_hicp_aind/default/table"}]),
        notes={"es": ["Índice de precios de la vivienda: compraventas de vivienda nueva y usada. Precios nominales, sin descontar la inflación.",
                      f"La línea marca la inflación acumulada de la UE (IPCA) entre {BASE} y {LAST}: {inflation_es} %. Cada país tiene su propia inflación.",
                      "Grecia no publica este índice en Eurostat."],
               "en": ["House price index: purchases of new and existing dwellings. Nominal prices, not adjusted for inflation.",
                      f"The line marks cumulative EU inflation (HICP) between {BASE} and {LAST}: {inflation}%. Each country has its own inflation.",
                      "Greece does not publish this index on Eurostat."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"targets": [{"geo": "EU27", "time": LAST, "value": inflation,
                            "label": {"es": "Inflación de la UE", "en": "EU inflation"}}]},
    )


BUILDERS = [precio_vivienda]
