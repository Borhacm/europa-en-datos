"""Finanzas públicas. Mirada 3: el déficit de cada país frente al 3 % y lo que paga en intereses."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

LAST, BASE = "2025", "2021"
EDP_NOTE = {"es": "Datos de la notificación del procedimiento de déficit excesivo (abril de 2026), con la definición del Tratado.",
            "en": "Excessive deficit procedure notification data (April 2026), using the Treaty definition."}
ECB_HIKE = {"name": "BCE (21/07/2022): decisiones de política monetaria",
            "url": "https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp220721~53e5bdd317.en.html"}
REG = {"name": "Reglamento (UE) 2024/1263, sobre la coordinación eficaz de las políticas económicas y la supervisión presupuestaria multilateral",
       "url": "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R1263"}


def _edp(item: str, times: list[str]) -> list[dict]:
    rows = sources.eurostat("gov_10dd_edpt1", na_item=item, sector="S13", unit="PC_GDP")
    rows = [r for r in rows if r["time"] in times]
    return [r for r in from_eurostat(rows, []) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]


def deficit_paises():
    out = _edp("B9", [LAST])
    over = sorted(r["geo"] for r in out if r["geo"] != "EU27" and r["value"] < -3)
    surplus = sorted(r["geo"] for r in out if r["geo"] != "EU27" and r["value"] > 0)
    return chart(
        id="fpd1-deficit-paises",
        lens="dentro", theme="finanzas",
        title={"es": f"{len(over)} de los 27 países de la UE superaron en {LAST} un déficit del 3 % de su PIB; {len(surplus)} tuvieron superávit",
               "en": f"{len(over)} of the 27 EU countries ran a deficit above 3% of GDP in {LAST}; {len(surplus)} ran a surplus"},
        subtitle={"es": f"Saldo de las administraciones públicas, en % del PIB, {LAST}",
                  "en": f"General government balance, as % of GDP, {LAST}"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source={**eurostat_source("gov_10dd_edpt1"), "also": [REG]},
        notes={"es": [EDP_NOTE["es"], "Un valor negativo es déficit. La línea marca el -3 % del PIB, el valor de referencia del Tratado para el déficit."],
               "en": [EDP_NOTE["en"], "A negative value is a deficit. The line marks -3% of GDP, the Treaty reference value for the deficit."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"targets": [{"geo": "EU27", "time": LAST, "value": -3,
                            "label": {"es": "Valor de referencia del Tratado", "en": "Treaty reference value"}}]},
    )


def intereses_paises():
    out = _edp("D41PAY", [BASE, LAST])
    v = {(r["geo"], r["time"]): r["value"] for r in out}
    up = [c for c in geo.EU27 if v[(c, LAST)] > v[(c, BASE)]]
    return chart(
        id="fpd2-intereses-paises",
        lens="dentro", theme="finanzas",
        title={"es": f"Desde {BASE}, el pago de intereses ha subido en {len(up)} de los 27 países; Italia y Hungría dedican a ello casi el 4 % de su PIB",
               "en": f"Since {BASE}, interest payments have risen in {len(up)} of the 27 countries; Italy and Hungary spend almost 4% of their GDP on them"},
        subtitle={"es": f"Intereses pagados por las administraciones públicas, en % del PIB, {BASE} y {LAST}",
                  "en": f"Interest paid by general government, as % of GDP, {BASE} and {LAST}"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source={**eurostat_source("gov_10dd_edpt1"), "also": [ECB_HIKE]},
        notes={"es": [EDP_NOTE["es"], "Intereses brutos: lo que pagan las administraciones, sin restar lo que cobran. Por eso la cifra de la UE es algo más alta que la de G2, que da los intereses netos.",
                      f"{BASE} es el último año antes de las subidas de tipos del Banco Central Europeo, que empezaron en julio de 2022."],
               "en": [EDP_NOTE["en"], "Gross interest: what governments pay, without subtracting what they receive. That is why the EU figure is somewhat higher than in G2, which shows net interest.",
                      f"{BASE} is the last year before the European Central Bank's rate rises, which began in July 2022."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [deficit_paises, intereses_paises]
