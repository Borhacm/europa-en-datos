"""N07. Gasto en defensa por país."""

from lib import geo
from lib.output import chart

from ..common import worldbank_rows, worldbank_source

# 2021 es el último año completo antes de la invasión rusa de Ucrania (febrero de 2022)
BASE, LAST = "2021", "2025"
SOURCE = worldbank_source("MS.MIL.XPND.GD.ZS", "gasto militar (% del PIB), con datos del SIPRI")
WALES = {"name": "OTAN, Declaración de la cumbre de Gales (5/09/2014)",
         "url": "https://www.nato.int/cps/en/natohq/official_texts_112964.htm"}

NOTES_ES = [
    "Datos del Instituto Internacional de Estudios para la Paz de Estocolmo (SIPRI) publicados por el Banco Mundial. Incluyen personal, operaciones, compras de armamento e investigación militar.",
    "No es la definición que usa la OTAN para medir su objetivo, así que las cifras pueden diferir de las que publican la OTAN y los gobiernos. Eurostat publica otra medida, el gasto de las administraciones públicas en defensa (COFOG GF02), con otra definición.",
]
NOTES_EN = [
    "Stockholm International Peace Research Institute (SIPRI) data published by the World Bank. They include personnel, operations, arms procurement and military research.",
    "This is not the definition NATO uses to measure its target, so the figures may differ from those published by NATO and by governments. Eurostat publishes another measure, general government expenditure on defence (COFOG GF02), with a different definition.",
]


def _rows(times):
    out = [r for r in worldbank_rows("MS.MIL.XPND.GD.ZS", int(times[0]), int(times[-1]))
           if (r["geo"] in geo.EU27 or r["geo"] == "EU27") and r["time"] in times]
    return [{**r, "value": round(r["value"], 2)} for r in out]


def paises():
    out = _rows([LAST])
    return chart(
        id="n07-defensa-paises",
        lens="dentro", theme="comercio",
        title={"es": "Polonia dedica a defensa el 4,5 % de su PIB, unas 20 veces más que Irlanda",
               "en": "Poland spends 4.5% of its GDP on defence, about 20 times as much as Ireland"},
        subtitle={"es": "Gasto militar, en % del PIB, 2025", "en": "Military expenditure, as % of GDP, 2025"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source={**SOURCE, "also": [WALES]},
        notes={"es": NOTES_ES + ["La línea marca el 2 % del PIB, la pauta que los aliados de la OTAN se comprometieron en 2014 a alcanzar en una década. Austria, Chipre, Irlanda y Malta no son miembros de la OTAN."],
               "en": NOTES_EN + ["The line marks 2% of GDP, the guideline NATO allies pledged in 2014 to reach within a decade. Austria, Cyprus, Ireland and Malta are not NATO members."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"targets": [{"geo": "EU27", "time": LAST, "value": 2,
                            "label": {"es": "Pauta de la OTAN (2014)", "en": "NATO guideline (2014)"}}]},
    )


def cambio():
    out = _rows([BASE, LAST])
    return chart(
        id="n07-defensa-cambio",
        lens="dentro", theme="comercio",
        title={"es": "En 2021, 4 de los 27 países de la UE gastaban en defensa el 2 % de su PIB o más; en 2025, 18",
               "en": "In 2021, 4 of the 27 EU countries spent 2% of GDP or more on defence; in 2025, 18 did"},
        subtitle={"es": "Gasto militar, en % del PIB, 2021 y 2025", "en": "Military expenditure, as % of GDP, 2021 and 2025"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source=SOURCE,
        notes={"es": NOTES_ES + ["2021 es el último año completo antes de la invasión rusa de Ucrania, en febrero de 2022.",
                                 "Es una proporción del PIB: puede bajar aunque el gasto suba, si la economía crece más deprisa."],
               "en": NOTES_EN + ["2021 is the last full year before Russia's invasion of Ukraine in February 2022.",
                                 "It is a share of GDP: it can fall even if spending rises, when the economy grows faster."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [paises, cambio]
