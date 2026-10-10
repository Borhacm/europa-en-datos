"""AN02. El informe Draghi, dos años después: los gráficos nuevos (luz para la industria y defensa).

El resto de gráficos del análisis se reutilizan de la nota N03 y de los temas de productividad e IA.
"""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat, worldbank_rows, worldbank_source

ELEC_TIMES = ["2019-S2", "2025-S2"]


def luz_industria():
    rows = sources.eurostat("nrg_pc_205", siec="E7000", nrg_cons="MWH2000-19999", unit="KWH",
                            tax="I_TAX", currency="EUR", time=ELEC_TIMES)
    # En céntimos: se multiplica antes de redondear para no perder precisión
    out = [r for r in from_eurostat([{**r, "value": r["value"] * 100} for r in rows], [])
           if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    return chart(
        id="an02-luz-industria",
        lens="gigantes", theme="productividad",
        title={"es": "Una empresa mediana paga la luz en Chipre o Dinamarca a más del triple que en Finlandia",
               "en": "A medium-sized firm pays more than three times as much for electricity in Cyprus or Denmark as in Finland"},
        subtitle={"es": "Precio de la electricidad para empresas con un consumo de 2.000 a 20.000 MWh al año, sin IVA ni impuestos recuperables, en céntimos de euro por kWh",
                  "en": "Electricity price for businesses using 2,000 to 20,000 MWh a year, excluding VAT and recoverable taxes, in euro cents per kWh"},
        unit={"es": "céntimos de euro por kWh", "en": "euro cents per kWh"},
        source=eurostat_source("nrg_pc_205"),
        notes={"es": ["Consumidores no domésticos de la banda ID (2.000 a 20.000 MWh al año), la de una fábrica mediana. Incluye los impuestos y cargos no recuperables; no incluye el IVA.",
                      "Datos semestrales: segundo semestre de 2019, antes de la pandemia y de la crisis energética, y segundo semestre de 2025, el último con datos de los 27 países y de la UE.",
                      "Eurostat no publica precios de EE. UU. o China. La comparación con EE. UU. (de dos a tres veces más cara) es la del informe Draghi, de 2024."],
               "en": ["Non-household consumers in band ID (2,000 to 20,000 MWh a year), typical of a medium-sized factory. Includes non-recoverable taxes and levies; excludes VAT.",
                      "Half-yearly data: second half of 2019, before the pandemic and the energy crisis, and second half of 2025, the latest with data for all 27 countries and the EU.",
                      "Eurostat does not publish US or Chinese prices. The comparison with the US (two to three times more expensive) is the one in the 2024 Draghi report."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"time": {
            "2019-S2": {"es": "2.º semestre de 2019", "en": "Second half of 2019"},
            "2025-S2": {"es": "2.º semestre de 2025", "en": "Second half of 2025"}}}},
    )


def defensa():
    share = [r for r in worldbank_rows("MS.MIL.XPND.GD.ZS", 2000, 2025) if r["geo"] in ("EU27", "USA", "CHN")]
    out = [{**r, "value": round(r["value"], 2)} for r in share]
    return chart(
        id="an02-defensa",
        lens="gigantes", theme="productividad",
        title={"es": "La UE ya dedica a defensa el 2,18 % de su PIB, más que China, pero menos que el 3,12 % de EE. UU.",
               "en": "The EU now spends 2.18% of its GDP on defence, more than China but less than the US's 3.12%"},
        subtitle={"es": "Gasto militar, en % del PIB", "en": "Military expenditure, as % of GDP"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source=worldbank_source("MS.MIL.XPND.GD.ZS", "gasto militar (% del PIB)"),
        notes={"es": ["Datos del Instituto Internacional de Estudios para la Paz de Estocolmo (SIPRI) publicados por el Banco Mundial. El agregado de la UE lo calcula el Banco Mundial con los 27 países.",
                      "El gasto de China es una estimación del SIPRI, más alta que el presupuesto oficial.",
                      "Incluye personal, operaciones, compras de armamento e investigación militar. No es la misma definición que usa la OTAN para su objetivo del 2 %."],
               "en": ["Stockholm International Peace Research Institute (SIPRI) data published by the World Bank. The EU aggregate is computed by the World Bank from the 27 countries.",
                      "China's spending is a SIPRI estimate, higher than the official budget.",
                      "Includes personnel, operations, arms procurement and military research. It is not the same definition NATO uses for its 2% target."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [luz_industria, defensa]
