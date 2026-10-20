"""Defensa. Mirada 2: comprar fuera o en Europa, y en qué se va el gasto europeo en defensa."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, worldbank_source
from ._sipri import TIV_NOTES, five_year

SAFE = {"name": "Reglamento (UE) 2025/1106 del Consejo, por el que se crea el instrumento SAFE",
        "url": "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32025R1106"}


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def importaciones_armas():
    rows = five_year("MS.MIL.MPRT.KD", ["EUU", *geo.EU27])
    v = {(r["geo"], r["time"]): r["value"] for r in rows}
    # El total de la UE va en las notas: en el gráfico aplastaría la escala de los países
    out = [r for r in rows if r["geo"] in geo.EU27]
    eu_old, eu_new = (fmt_es(round(v[("EU27", t)], 1)) for t in ("2016-2020", "2021-2025"))
    ratio = v[("EU27", "2021-2025")] / v[("EU27", "2016-2020")]
    assert 2.9 < ratio < 3.5, ratio
    top = max(geo.EU27, key=lambda c: v.get((c, "2021-2025"), 0))
    return chart(
        id="dfe1-importaciones-armas",
        lens="elige", theme="defensa",
        title={"es": f"Los países de la UE han triplicado sus compras de armas al extranjero; {geo.name(top, 'es')} es el que más importa",
               "en": f"EU countries have tripled their arms imports; {geo.name(top, 'en')} imports the most"},
        subtitle={"es": "Importaciones de armas, en miles de millones de valores indicadores de tendencia (TIV) del SIPRI, 2016-2020 y 2021-2025",
                  "en": "Arms imports, in billions of SIPRI trend-indicator values (TIV), 2016-2020 and 2021-2025"},
        unit={"es": "miles de millones de TIV", "en": "billion TIV"},
        source={**worldbank_source("MS.MIL.MPRT.KD", "importaciones de armas (TIV del SIPRI)"), "also": [SAFE]},
        notes={"es": [f"En total, los 27 importaron {eu_new} miles de millones de TIV en 2021-2025, frente a {eu_old} en 2016-2020.",
                      *TIV_NOTES["es"], "Incluye las compras a otros países de la UE: estos datos no separan lo que viene de fuera de la Unión."],
               "en": [f"In total, the 27 imported {round(v[('EU27', '2021-2025')], 1):g} billion TIV in 2021-2025, against {round(v[('EU27', '2016-2020')], 1):g} in 2016-2020.",
                      *TIV_NOTES["en"], "Includes purchases from other EU countries: these data do not separate what comes from outside the Union."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


# Gasto en defensa (COFOG GF02) por tipo de operación
ITEMS = {
    "D1": {"es": "Personal", "en": "Personnel", "parts": ["D1"]},
    "P2": {"es": "Bienes y servicios", "en": "Goods and services", "parts": ["P2"]},
    "P51G": {"es": "Inversión", "en": "Investment", "parts": ["P51G"]},
    "TRANSF": {"es": "Transferencias", "en": "Transfers", "parts": ["D7", "D9"]},
}
START = 2014


def miles(x: float) -> str:
    return f"{round(x):,}".replace(",", ".")


def composicion_gasto():
    rows = sources.eurostat("gov_10a_exp", geo="EU27_2020", sector="S13", cofog99="GF02", unit="MIO_EUR")
    v = {(r["na_item"], r["time"]): r["value"] for r in rows}
    years = sorted(t for (i, t) in v if i == "TE" and int(t) >= START)
    out = []
    for t in years:
        for code, it in ITEMS.items():
            share = 100 * sum(v.get((p, t), 0) for p in it["parts"]) / v[("TE", t)]
            out.append({"geo": "EU27", "time": t, "series": code, "value": round(share, 1)})
    s = {(r["series"], r["time"]): r["value"] for r in out}
    first, last = years[0], years[-1]
    assert s[("D1", first)] > 50
    return chart(
        id="dfe2-composicion-gasto",
        lens="elige", theme="defensa",
        title={"es": f"En {first}, más de la mitad del gasto europeo en defensa eran sueldos; en {last}, el {fmt_es(s[('D1', last)])} %, y la inversión ha pasado del {fmt_es(s[('P51G', first)])} % al {fmt_es(s[('P51G', last)])} %",
               "en": f"In {first}, more than half of European defence spending went on pay; in {last}, {s[('D1', last)]:g}%, and investment has risen from {s[('P51G', first)]:g}% to {s[('P51G', last)]:g}%"},
        subtitle={"es": f"Gasto de las administraciones públicas de la UE en defensa por tipo, en % del total, {first}-{last}",
                  "en": f"EU general government defence expenditure by type, as % of the total, {first}-{last}"},
        unit={"es": "% del gasto en defensa", "en": "% of defence spending"},
        source=eurostat_source("gov_10a_exp"),
        notes={"es": [f"Función 02 (defensa) de la clasificación COFOG. En {last}, la UE gastó en defensa {miles(v[('TE', last)])} millones de euros, frente a {miles(v[('TE', first)])} millones en {first}.",
                      "Personal: sueldos y cotizaciones. Bienes y servicios: compras corrientes, como combustible o mantenimiento. Inversión: equipos e infraestructuras militares. Transferencias: pagos corrientes y de capital a otros sectores o a otros países.",
                      "Las cuatro partidas no suman el 100 %: falta una parte pequeña de otros gastos.",
                      "No es la misma medida que el gasto militar del SIPRI de G1, que tiene otra definición."],
               "en": [f"Function 02 (defence) of the COFOG classification. In {last}, the EU spent {round(v[('TE', last)]):,} million euros on defence, against {round(v[('TE', first)]):,} million in {first}.",
                      "Personnel: pay and contributions. Goods and services: current purchases such as fuel or maintenance. Investment: military equipment and infrastructure. Transfers: current and capital payments to other sectors or to other countries.",
                      "The four items do not add up to 100%: a small share of other spending is missing.",
                      "This is not the same measure as SIPRI military spending in G1, which uses another definition."]},
        rows=out,
        geos=geo.geo_table(["EU27"]),
        extra={"dimensions": {"series": {k: {"es": it["es"], "en": it["en"]} for k, it in ITEMS.items()}}},
    )


BUILDERS = [importaciones_armas, composicion_gasto]
