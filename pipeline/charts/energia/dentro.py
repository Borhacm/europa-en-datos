"""Energía. Mirada 3: renovables y precio de la electricidad para la industria en los 27."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat
from .elige import PRICE_FILTERS, PRICE_NOTES, REN_LAST

PRICE_TIMES = ["2021-S1", "2025-S2"]


def renovables_paises():
    rows = sources.eurostat("nrg_ind_ren", unit="PC", nrg_bal="REN")
    out = [{k: v for k, v in r.items() if k != "nrg_bal"} for r in from_eurostat(rows, ["nrg_bal"])
           if (r["geo"] in geo.EU27 or r["geo"] == "EU27") and r["time"] <= REN_LAST]
    out = [{**r, "value": round(r["value"], 1)} for r in out]
    return chart(
        id="end1-renovables-paises",
        lens="dentro", theme="energia",
        title={"es": "Suecia cubre con renovables el 62,9 % de su consumo de energía; Bélgica, el 14,3 %",
               "en": "Sweden covers 62.9% of its energy consumption with renewables; Belgium, 14.3%"},
        subtitle={"es": "Energías renovables, en % del consumo final bruto de energía",
                  "en": "Renewable energy, as % of gross final energy consumption"},
        unit={"es": "% del consumo final bruto", "en": "% of gross final consumption"},
        source=eurostat_source("nrg_ind_ren"),
        notes={"es": ["Consumo final bruto: la energía que llega a hogares, empresas y transporte, más las pérdidas de la red y el consumo propio de las centrales. Se calcula con las reglas de la directiva de renovables.",
                      "Cada país tiene su propia contribución al objetivo común del 42,5 % en 2030, fijada en su plan nacional de energía y clima.",
                      f"Se muestra hasta {REN_LAST}, el último año con datos definitivos; el de 2025 es provisional."],
               "en": ["Gross final consumption: the energy delivered to households, businesses and transport, plus grid losses and power plants' own use. It is calculated under the rules of the renewable energy directive.",
                      "Each country has its own contribution to the common 42.5% target for 2030, set in its national energy and climate plan.",
                      f"Shown up to {REN_LAST}, the last year with final data; 2025 is provisional."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def precio_industria_paises():
    rows = sources.eurostat("nrg_pc_205", tax="X_VAT", time=PRICE_TIMES, **PRICE_FILTERS)
    out = []
    for r in rows:
        code = geo.from_eurostat(r["geo"])
        if code in geo.EU27 or code == "EU27":
            out.append({"geo": code, "time": r["time"], "value": round(100 * r["value"], 2),
                        **({"flag": r["flag"]} if r.get("flag") else {})})
    return chart(
        id="end2-precio-industria-paises",
        lens="dentro", theme="energia",
        title={"es": "Desde 2021, la electricidad para la industria se ha encarecido en los 27 países; en Chipre cuesta 3,5 veces lo que en Finlandia",
               "en": "Since 2021, electricity for industry has become more expensive in all 27 countries; in Cyprus it costs 3.5 times as much as in Finland"},
        subtitle={"es": "Precio de la electricidad para la industria, sin IVA ni impuestos recuperables, primer semestre de 2021 y segundo semestre de 2025, en céntimos de euro por kWh",
                  "en": "Electricity price for industry, excluding VAT and recoverable taxes, first half of 2021 and second half of 2025, in euro cents per kWh"},
        unit={"es": "céntimos de euro por kWh", "en": "euro cents per kWh"},
        source=eurostat_source("nrg_pc_205"),
        notes={"es": [*PRICE_NOTES["es"],
                      "El primer semestre de 2021 es el último antes de la subida de precios de la energía de 2021 y 2022.",
                      "En Malta el precio apenas ha cambiado (+0,9 %). Austria: dato estimado en 2025."],
               "en": [*PRICE_NOTES["en"],
                      "The first half of 2021 is the last one before the 2021-2022 energy price surge.",
                      "In Malta the price has barely changed (+0.9%). Austria: estimated 2025 data."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [renovables_paises, precio_industria_paises]
