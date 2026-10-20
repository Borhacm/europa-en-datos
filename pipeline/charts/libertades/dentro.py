"""Libertades, bienestar y clima. Mirada 3: democracia y Estado de bienestar en los 27."""

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


CASES = ["HUN", "POL", "SVK"]


def trayectorias():
    rows = vdem_with_eu(LIBDEM, since=int(DEMOCRACY_FROM), countries=[])
    out = [{"geo": r["geo"], "time": r["time"], "value": r["value"], **({"stat": "median"} if r["geo"] == "EU27" else {})}
           for r in rows if (r["geo"] in CASES and r["stat"] == "country") or (r["geo"] == "EU27" and r["stat"] == "median")]
    return chart(
        id="ld4-trayectorias-democracia",
        lens="dentro", theme="libertades",
        title={"es": "Hungría no ha mejorado desde la suspensión de fondos de 2022; Polonia subió de 0,46 a 0,65 entre 2023 y 2025",
               "en": "Hungary has not improved since its funds were suspended in 2022; Poland rose from 0.46 to 0.65 between 2023 and 2025"},
        subtitle={"es": f"Índice de democracia liberal de V-Dem, de 0 a 1, desde {DEMOCRACY_FROM}",
                  "en": f"V-Dem liberal democracy index, from 0 to 1, since {DEMOCRACY_FROM}"},
        unit={"es": "índice de 0 a 1", "en": "index from 0 to 1"},
        source={**VDEM_SOURCE, "also": [
            {"name": "Reglamento (UE, Euratom) 2020/2092, régimen de condicionalidad", "url": "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32020R2092"},
            {"name": "Decisión de Ejecución (UE) 2022/2506 del Consejo (Hungría)", "url": "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32022D2506"}]},
        notes={"es": ["La línea de la UE es la mediana de los 27 países.",
                      "V-Dem puntúa cada año con encuestas a expertos; un cambio de pocas centésimas puede estar dentro de su margen de error.",
                      "Licencia CC BY-SA: los datos derivados deben compartirse con la misma licencia."],
               "en": ["The EU line is the median of the 27 countries.",
                      "V-Dem scores each year with expert surveys; a change of a few hundredths may be within its margin of error.",
                      "CC BY-SA licence: derived data must be shared under the same licence."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


TRANSFERS = {"before": {"es": "Antes de las transferencias sociales", "en": "Before social transfers"},
             "after": {"es": "Después de las transferencias", "en": "After transfers"}}
POVERTY_YEAR = "2025"


def pobreza_transferencias():
    filters = dict(age="TOTAL", sex="T", unit="PC", rskpovth="B_60", statinfo="MED_EI", time=POVERTY_YEAR)
    out = []
    for ds, key in (("ilc_li10", "before"), ("ilc_li02", "after")):
        for r in from_eurostat(sources.eurostat(ds, **filters), []):
            if r["geo"] in geo.EU27 or r["geo"] == "EU27":
                out.append({**r, "transfers": key})
    return chart(
        id="ld5-pobreza-transferencias",
        lens="dentro", theme="libertades",
        title={"es": "Las prestaciones sociales sacan de la pobreza a un tercio de quienes estarían en ella; en España, a menos de una cuarta parte",
               "en": "Social benefits lift a third of those who would be poor out of poverty; in Spain, less than a quarter"},
        subtitle={"es": f"Población en riesgo de pobreza (ingresos por debajo del 60 % de la mediana de su país) antes y después de las transferencias sociales, en %, {POVERTY_YEAR}",
                  "en": f"Population at risk of poverty (income below 60% of their country's median) before and after social transfers, in %, {POVERTY_YEAR}"},
        unit={"es": "% de la población", "en": "% of the population"},
        source=eurostat_source("ilc_li02", also=[{"name": "Eurostat, ilc_li10 (antes de las transferencias)",
                                                    "url": "https://ec.europa.eu/eurostat/databrowser/view/ilc_li10/default/table"}]),
        notes={"es": ["Las pensiones de jubilación y supervivencia cuentan como ingreso en las dos series: las transferencias que se restan son el resto (desempleo, familia, vivienda, discapacidad, rentas mínimas...).",
                      "Es un cálculo mecánico: supone que, sin prestaciones, nadie cambiaría su conducta ni sus ingresos. No mide lo que pasaría de verdad sin ellas.",
                      "Pobreza relativa: el umbral es el 60 % de la mediana de cada país, así que no compara niveles de vida entre países. Encuesta EU-SILC; los ingresos son del año anterior.",
                      "Eslovaquia y Luxemburgo tienen una ruptura de serie en 2025; Lituania es provisional."],
               "en": ["Old-age and survivors' pensions count as income in both series: the transfers removed are the rest (unemployment, family, housing, disability, minimum income...).",
                      "It is a mechanical calculation: it assumes that, without benefits, nobody would change their behaviour or income. It does not measure what would really happen without them.",
                      "Relative poverty: the threshold is 60% of each country's median, so it does not compare living standards across countries. EU-SILC survey; incomes refer to the previous year.",
                      "Slovakia and Luxembourg have a break in series in 2025; Lithuania is provisional."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["transfers"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"transfers": TRANSFERS}},
    )


BUILDERS = [democracia_ue, trayectorias, pobreza_transferencias]
