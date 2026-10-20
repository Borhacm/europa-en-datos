"""N06. Deuda pública: la UE frente a EE. UU. y China, y los países de la UE."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

# Primer año con dato del FMI para EE. UU. y último observado: desde 2025, el WEO da estimaciones y proyecciones
START, LAST = 2001, 2024
LAST_EU = "2025"
IMF_CODES = {"USA": "USA", "CHN": "CHN", "EU": "EU27"}

IMF_SOURCE = {
    "name": "FMI, World Economic Outlook (octubre de 2026)",
    "dataset": "GGXWDG_NGDP",
    "url": "https://www.imf.org/external/datamapper/GGXWDG_NGDP@WEO",
    "license": "Términos de uso del FMI (uso libre citando la fuente)",
}
MAASTRICHT = {"name": "Protocolo n.º 12 del TFUE, sobre el procedimiento aplicable en caso de déficit excesivo",
              "url": "https://eur-lex.europa.eu/eli/treaty/tfeu_2016/pro_12/oj/eng"}


def bloques():
    out = []
    for r in sources.imf("GGXWDG_NGDP", list(IMF_CODES)):
        if START <= int(r["time"]) <= LAST:
            out.append({"geo": IMF_CODES[r["iso3"]], "time": r["time"], "value": round(r["value"], 1)})
    return chart(
        id="n06-deuda-bloques",
        lens="gigantes", theme="finanzas",
        title={"es": "Desde 2001, la deuda pública de EE. UU. ha pasado del 53,5 % al 122,3 % de su PIB; la de la UE, del 65,6 % al 81,6 %",
               "en": "Since 2001, US public debt has risen from 53.5% to 122.3% of GDP; the EU's, from 65.6% to 81.6%"},
        subtitle={"es": "Deuda bruta de las administraciones públicas, en % del PIB, 2001-2024",
                  "en": "General government gross debt, as % of GDP, 2001-2024"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source=IMF_SOURCE,
        notes={"es": ["Las tres series salen de la misma fuente, el FMI, para que sean comparables. La serie se corta en 2024: desde 2025, el World Economic Outlook da estimaciones y proyecciones.",
                      "La cifra de la UE del FMI (81,6 % en 2024) difiere un poco de la de Eurostat (80,7 %), que es la que usa el segundo gráfico.",
                      "China: el FMI publica varias medidas. En su consulta del artículo IV de febrero de 2026, la deuda pública con la definición estrecha era del 60,9 % del PIB en 2024, y la deuda 'aumentada', que suma la de los vehículos de financiación de los gobiernos locales, del 126,6 % en 2025. La serie del World Economic Outlook queda entre ambas."],
               "en": ["All three series come from the same source, the IMF, so they are comparable. The series stops in 2024: from 2025 on, the World Economic Outlook gives estimates and projections.",
                      "The IMF's EU figure (81.6% in 2024) differs slightly from Eurostat's (80.7%), which the second chart uses.",
                      "China: the IMF publishes several measures. In its February 2026 Article IV consultation, public debt on the narrow definition was 60.9% of GDP in 2024, and 'augmented' debt, which adds local government financing vehicles, 126.6% in 2025. The World Economic Outlook series falls between the two."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def paises():
    rows = sources.eurostat("gov_10dd_edpt1", na_item="GD", sector="S13", unit="PC_GDP", time=LAST_EU)
    out = [r for r in from_eurostat(rows, []) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    return chart(
        id="n06-deuda-paises",
        lens="gigantes", theme="finanzas",
        title={"es": "12 de los 27 países de la UE deben más del 60 % de su PIB, el valor de referencia del Tratado",
               "en": "12 of the 27 EU countries owe more than 60% of their GDP, the Treaty reference value"},
        subtitle={"es": "Deuda bruta de las administraciones públicas, en % del PIB, 2025",
                  "en": "General government gross debt, as % of GDP, 2025"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source=eurostat_source("gov_10dd_edpt1", also=[MAASTRICHT]),
        notes={"es": ["Deuda bruta consolidada a valor nominal al final del año, la definición del procedimiento de déficit excesivo.",
                      "La línea marca el 60 % del PIB, valor de referencia para la deuda pública fijado en el Protocolo n.º 12 del Tratado de Funcionamiento de la UE."],
               "en": ["Consolidated gross debt at nominal value at year end, the excessive deficit procedure definition.",
                      "The line marks 60% of GDP, the reference value for public debt set in Protocol No 12 of the Treaty on the Functioning of the EU."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"targets": [{"geo": "EU27", "time": LAST_EU, "value": 60,
                            "label": {"es": "Valor de referencia del Tratado", "en": "Treaty reference value"}}]},
    )


BUILDERS = [bloques, paises]
