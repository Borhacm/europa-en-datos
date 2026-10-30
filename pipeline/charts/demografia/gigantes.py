"""Demografía. Mirada 1: envejecimiento y fecundidad de la UE, EE. UU. y China."""

from lib import geo
from lib.output import chart

from ..common import worldbank_rows, worldbank_source

FIRST, LAST = 2000, 2024
BLOCS = ["EU27", "USA", "CHN"]


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def bloc_rows(indicator: str, digits: int) -> list[dict]:
    rows = [r for r in worldbank_rows(indicator, FIRST, LAST) if r["geo"] in BLOCS]
    for r in rows:
        r["value"] = round(r["value"], digits)
    return rows


def mayores_bloques():
    rows = bloc_rows("SP.POP.65UP.TO.ZS", 1)
    v = {(r["geo"], r["time"]): r["value"] for r in rows}
    last, first = str(LAST), str(FIRST)
    eu, us, cn, cn0 = v[("EU27", last)], v[("USA", last)], v[("CHN", last)], v[("CHN", first)]
    assert eu > us > cn and cn >= 2 * cn0, (eu, us, cn, cn0)
    return chart(
        id="dmg1-mayores-bloques",
        lens="gigantes", theme="demografia",
        title={"es": f"En la UE, el {fmt_es(eu)} % de la población tiene 65 años o más; en EE. UU., el {fmt_es(us)} %, y en China, el {fmt_es(cn)} %, el doble que en {first}",
               "en": f"In the EU, {eu:g}% of the population is 65 or older; in the US, {us:g}%, and in China, {cn:g}%, twice the {first} share"},
        subtitle={"es": f"Población de 65 años o más, en % de la población total, {first}-{last}",
                  "en": f"Population aged 65 and over, as % of the total population, {first}-{last}"},
        unit={"es": "% de la población", "en": "% of the population"},
        source=worldbank_source("SP.POP.65UP.TO.ZS", "Población de 65 años o más (% del total)"),
        notes={"es": ["El Banco Mundial elabora la serie con las estimaciones de población de Naciones Unidas (World Population Prospects), que usan el mismo método para los tres bloques.",
                      f"En la UE, la cifra de {first} es la de los 27 países actuales, aunque entonces no todos eran miembros.",
                      f"Para años posteriores a {last}, Naciones Unidas publica proyecciones; aquí no se muestran."],
               "en": ["The World Bank builds the series from United Nations population estimates (World Population Prospects), which use the same method for all three blocs.",
                      f"For the EU, the {first} figure covers today's 27 countries, although not all of them were members then.",
                      f"The United Nations publishes projections beyond {last}; they are not shown here."]},
        rows=rows,
        geos=geo.geo_table(r["geo"] for r in rows),
    )


def fecundidad_bloques():
    rows = bloc_rows("SP.DYN.TFRT.IN", 2)
    v = {(r["geo"], r["time"]): r["value"] for r in rows}
    last, first = str(LAST), str(FIRST)
    eu, us, cn = v[("EU27", last)], v[("USA", last)], v[("CHN", last)]
    eu0, cn0 = v[("EU27", first)], v[("CHN", first)]
    # Primer año en que China queda por debajo de la UE y ya no vuelve a superarla
    years = sorted({r["time"] for r in rows})
    below = [t for t in years if all(v[("CHN", s)] < v[("EU27", s)] for s in years if s >= t)]
    cross = below[0]
    assert cn < eu < us and cn0 > eu0 and max(eu, us, cn) < 2.1, (eu, us, cn)
    return chart(
        id="dmg2-fecundidad-bloques",
        lens="gigantes", theme="demografia",
        title={"es": f"Las mujeres tienen de media {fmt_es(us)} hijos en EE. UU., {fmt_es(eu)} en la UE y {fmt_es(cn)} en China, que estaba por encima de la UE hasta {int(cross) - 1}",
               "en": f"Women have {us:g} children on average in the US, {eu:g} in the EU and {cn:g} in China, which was above the EU until {int(cross) - 1}"},
        subtitle={"es": f"Tasa de fecundidad: hijos por mujer, {first}-{last}",
                  "en": f"Fertility rate: births per woman, {first}-{last}"},
        unit={"es": "hijos por mujer", "en": "births per woman"},
        source=worldbank_source("SP.DYN.TFRT.IN", "Tasa de fecundidad (hijos por mujer)"),
        notes={"es": ["Número medio de hijos que tendría una mujer a lo largo de su vida si tuviera los hijos que corresponden a cada edad en ese año. Para que una población se mantenga sin migración hacen falta unos 2,1.",
                      "Estimaciones de Naciones Unidas recogidas por el Banco Mundial. Para los países de la UE, Eurostat publica cifras propias que pueden diferir en algunas centésimas (gráfico D1)."],
               "en": ["Average number of children a woman would have over her lifetime if she had the births corresponding to each age in that year. Around 2.1 are needed for a population to hold steady without migration.",
                      "United Nations estimates collected by the World Bank. For EU countries, Eurostat publishes its own figures, which may differ by a few hundredths (chart D1)."]},
        rows=rows,
        geos=geo.geo_table(r["geo"] for r in rows),
    )


BUILDERS = [mayores_bloques, fecundidad_bloques]
