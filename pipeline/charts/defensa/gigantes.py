"""Defensa. Mirada 1: cuánto gastan en defensa la UE, EE. UU., China y Rusia, y quién vende armas."""

from lib import geo
from lib.output import chart

from ..common import worldbank_source
from ._sipri import TIV_NOTES, five_year, wb

BLOCS = ["EUU", "USA", "CHN", "RUS"]
START, LAST = 2000, 2025


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def gasto_dolares():
    rows = wb("MS.MIL.XPND.CD", BLOCS, START, LAST)
    out = [{**r, "value": round(r["value"] / 1e9, 1)} for r in rows]
    v = {(r["geo"], r["time"]): r["value"] for r in out}
    y = str(LAST)
    eu, us, cn, ru = (v[(g, y)] for g in ("EU27", "USA", "CHN", "RUS"))
    assert eu < us / 2 and eu > cn
    return chart(
        id="dfg1-gasto-dolares",
        lens="gigantes", theme="defensa",
        title={"es": f"En {y}, la UE gastó en defensa {round(eu)}.000 millones de dólares: menos de la mitad que EE. UU., más que China y {fmt_es(round(eu / ru, 1))} veces lo que Rusia",
               "en": f"In {y}, the EU spent {round(eu)} billion dollars on defence: less than half as much as the US, more than China and {round(eu / ru, 1):g} times as much as Russia"},
        subtitle={"es": f"Gasto militar, en miles de millones de dólares corrientes, {START}-{LAST}",
                  "en": f"Military expenditure, in billions of current dollars, {START}-{LAST}"},
        unit={"es": "miles de millones de dólares", "en": "billion dollars"},
        source=worldbank_source("MS.MIL.XPND.CD", "gasto militar (dólares corrientes), con datos del SIPRI"),
        notes={"es": ["Datos del Instituto Internacional de Estudios para la Paz de Estocolmo (SIPRI) publicados por el Banco Mundial. Incluyen personal, operaciones, compras de armamento e investigación militar.",
                      "En dólares de cada año: no descuentan la inflación, y el gasto de la UE sube o baja también con el tipo de cambio del euro.",
                      "UE: suma de los 27 países."],
               "en": ["Stockholm International Peace Research Institute (SIPRI) data published by the World Bank. They include personnel, operations, arms procurement and military research.",
                      "In each year's dollars: they are not adjusted for inflation, and EU spending also rises or falls with the euro exchange rate.",
                      "EU: sum of the 27 countries."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def exportaciones_armas():
    out = five_year("MS.MIL.XPRT.KD", BLOCS)
    v = {(r["geo"], r["time"]): r["value"] for r in out}
    change = {g: round(100 * (v[(g, "2021-2025")] / v[(g, "2016-2020")] - 1)) for g in ("EU27", "RUS")}
    assert change["RUS"] < 0 < change["EU27"]
    return chart(
        id="dfg2-exportaciones-armas",
        lens="gigantes", theme="defensa",
        title={"es": f"Rusia exportó entre 2021 y 2025 un {-change['RUS']} % menos de armas que en los cinco años anteriores; los países de la UE, un {change['EU27']} % más",
               "en": f"Russia exported {-change['RUS']}% fewer arms in 2021-2025 than in the previous five years; EU countries, {change['EU27']}% more"},
        subtitle={"es": "Exportaciones de armas, en miles de millones de valores indicadores de tendencia (TIV) del SIPRI, 2016-2020 y 2021-2025",
                  "en": "Arms exports, in billions of SIPRI trend-indicator values (TIV), 2016-2020 and 2021-2025"},
        unit={"es": "miles de millones de TIV", "en": "billion TIV"},
        source=worldbank_source("MS.MIL.XPRT.KD", "exportaciones de armas (TIV del SIPRI)"),
        notes={"es": [*TIV_NOTES["es"], "UE: suma de las exportaciones de los 27, incluidas las que van de un país de la UE a otro."],
               "en": [*TIV_NOTES["en"], "EU: sum of the 27 countries' exports, including those from one EU country to another."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [gasto_dolares, exportaciones_armas]
