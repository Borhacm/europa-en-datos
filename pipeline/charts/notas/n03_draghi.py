"""N03. El informe Draghi: el diagnóstico en dos gráficos, crecimiento e inversión."""

from lib import geo
from lib.output import chart

from ..common import worldbank_rows, worldbank_source

BASE = "2000"


def crecimiento():
    rows = [r for r in worldbank_rows("NY.GDP.MKTP.KD", int(BASE), 2025) if r["geo"] in ("USA", "CHN", "EU27")]
    base = {r["geo"]: r["value"] for r in rows if r["time"] == BASE}
    out = [{**r, "value": round(100 * r["value"] / base[r["geo"]], 1)} for r in rows]
    return chart(
        id="n03-crecimiento",
        lens="gigantes", theme="productividad",
        title={"es": "Desde 2000, la economía de EE. UU. ha crecido un 69 %; la de la UE, un 41 %",
               "en": "Since 2000, the US economy has grown 69%; the EU's, 41%"},
        subtitle={"es": "PIB real, índice 2000 = 100", "en": "Real GDP, index 2000 = 100"},
        unit={"es": "índice (2000 = 100)", "en": "index (2000 = 100)"},
        source=worldbank_source("NY.GDP.MKTP.KD", "PIB a precios constantes"),
        notes={"es": ["China queda fuera de la escala: su PIB real se ha multiplicado por 6,9 en el mismo periodo. Está en la tabla y en la descarga."],
               "en": ["China is off the scale: its real GDP has multiplied by 6.9 over the same period. It is in the table and the download."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"ref_line": {"value": 100, "label": {"es": "Nivel de 2000", "en": "2000 level"}}},
    )


def inversion():
    out = [r for r in worldbank_rows("NE.GDI.FTOT.ZS", int(BASE), 2025) if r["geo"] in ("USA", "CHN", "EU27")]
    return chart(
        id="n03-inversion",
        lens="gigantes", theme="productividad",
        title={"es": "La UE ya invierte lo mismo que EE. UU. en proporción a su PIB; Draghi pide llegar al 27 %",
               "en": "The EU already invests as much as the US relative to GDP; Draghi calls for 27%"},
        subtitle={"es": "Formación bruta de capital fijo (inversión en equipos, edificios, infraestructuras y tecnología), en % del PIB",
                  "en": "Gross fixed capital formation (investment in equipment, buildings, infrastructure and technology), as % of GDP"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source=worldbank_source("NE.GDI.FTOT.ZS", "formación bruta de capital fijo"),
        notes={"es": ["La línea marca el 27 % del PIB que, según el informe Draghi (2024), necesitaría la UE: entre 750.000 y 800.000 millones de euros más al año."],
               "en": ["The line marks the 27% of GDP the EU would need according to the Draghi report (2024): an extra 750 to 800 billion euros a year."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"ref_line": {"value": 27, "label": {"es": "Lo que pide Draghi para la UE", "en": "Draghi's target for the EU"}}},
    )


BUILDERS = [crecimiento, inversion]
