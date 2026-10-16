"""Energía. Mirada 2: la apuesta por las renovables y lo que paga la industria por la electricidad."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

REN = {
    "REN": {"es": "Total", "en": "Total"},
    "REN_ELC": {"es": "Electricidad", "en": "Electricity"},
    "REN_HEAT_CL": {"es": "Calefacción y refrigeración", "en": "Heating and cooling"},
    "REN_TRA": {"es": "Transporte", "en": "Transport"},
}
REN_LAST = "2024"
TAXES = {
    "X_TAX": {"es": "Sin impuestos", "en": "Excluding taxes"},
    "X_VAT": {"es": "Sin IVA ni impuestos recuperables", "en": "Excluding VAT and recoverable taxes"},
}
# Consumidor industrial tipo de Eurostat (banda ID): entre 2.000 y 20.000 MWh al año
PRICE_FILTERS = dict(siec="E7000", unit="KWH", currency="EUR", nrg_cons="MWH2000-19999")
PRICE_NOTES = {
    "es": ["Empresas que consumen entre 2.000 y 20.000 MWh al año, la banda de referencia de Eurostat para la industria. Precio medio del semestre en euros corrientes, sin descontar la inflación.",
           "Las empresas suelen recuperar el IVA y algunos impuestos: el precio sin IVA ni impuestos recuperables es lo que pagan de verdad. El precio sin impuestos incluye la energía, el suministro y las redes."],
    "en": ["Businesses consuming 2,000 to 20,000 MWh a year, Eurostat's reference band for industry. Average price for the half-year in current euros, not adjusted for inflation.",
           "Businesses usually recover VAT and some taxes: the price excluding VAT and recoverable taxes is what they actually pay. The price excluding taxes covers energy, supply and networks."],
}


def renovables_ue():
    rows = sources.eurostat("nrg_ind_ren", unit="PC", geo="EU27_2020", nrg_bal=list(REN))
    out = [{"geo": r["geo"], "series": r["nrg_bal"], "time": r["time"], "value": round(r["value"], 1),
            **({"flag": r["flag"]} if r.get("flag") else {})}
           for r in from_eurostat(rows, ["nrg_bal"]) if r["time"] <= REN_LAST]
    return chart(
        id="ene1-renovables-ue",
        lens="elige", theme="energia",
        title={"es": "Las renovables ya cubren el 47,5 % de la electricidad que consume la UE, pero solo el 25,2 % de toda su energía",
               "en": "Renewables now cover 47.5% of the electricity the EU consumes, but only 25.2% of all its energy"},
        subtitle={"es": "Energías renovables en la UE, en % del consumo final bruto de energía, total y por uso",
                  "en": "Renewable energy in the EU, as % of gross final energy consumption, total and by use"},
        unit={"es": "% del consumo final bruto", "en": "% of gross final consumption"},
        source=eurostat_source("nrg_ind_ren"),
        notes={"es": ["Consumo final bruto: la energía que llega a hogares, empresas y transporte, más las pérdidas de la red y el consumo propio de las centrales. Se calcula con las reglas de la directiva de renovables.",
                      "El objetivo de la UE para 2030 es que las renovables lleguen al 42,5 % del consumo final bruto de energía (Directiva (UE) 2023/2413).",
                      f"Se muestra hasta {REN_LAST}, el último año con datos definitivos de todos los usos. Eurostat ya publica un dato provisional de 2025 para el total (26,2 % en la UE), pero no para el transporte.",
                      "No coincide con la mezcla de producción eléctrica del gráfico G2: aquí se mide el consumo, y la directiva corrige la hidráulica y la eólica para quitar el efecto de los años más o menos lluviosos y ventosos."],
               "en": ["Gross final consumption: the energy delivered to households, businesses and transport, plus grid losses and power plants' own use. It is calculated under the rules of the renewable energy directive.",
                      "The EU target for 2030 is for renewables to reach 42.5% of gross final energy consumption (Directive (EU) 2023/2413).",
                      f"Shown up to {REN_LAST}, the last year with final data for every use. Eurostat already publishes a provisional 2025 figure for the total (26.2% in the EU), but not for transport.",
                      "It does not match the electricity production mix in chart G2: this measures consumption, and the directive normalises hydro and wind to remove the effect of wetter or windier years."]},
        rows=sorted(out, key=lambda r: (r["series"], r["time"])),
        geos=geo.geo_table(["EU27"]),
        extra={"dimensions": {"series": REN},
               "target": {"value": 42.5, "year": "2030", "source": "https://eur-lex.europa.eu/eli/dir/2023/2413/oj"}},
    )


def precio_industria_ue():
    rows = sources.eurostat("nrg_pc_205", geo="EU27_2020", tax=list(TAXES), **PRICE_FILTERS)
    out = [{"geo": "EU27", "series": r["tax"], "time": r["time"], "value": round(100 * r["value"], 2),
            **({"flag": r["flag"]} if r.get("flag") else {})} for r in rows]
    return chart(
        id="ene2-precio-industria",
        lens="elige", theme="energia",
        title={"es": "La electricidad para la industria de la UE cuesta un 45,8 % más que a principios de 2021, pero un 20,8 % menos que en su máximo de finales de 2022",
               "en": "Electricity for EU industry costs 45.8% more than in early 2021, but 20.8% less than at its peak in late 2022"},
        subtitle={"es": "Precio medio de la electricidad para la industria en la UE, en céntimos de euro por kWh",
                  "en": "Average electricity price for industry in the EU, in euro cents per kWh"},
        unit={"es": "céntimos de euro por kWh", "en": "euro cents per kWh"},
        source=eurostat_source("nrg_pc_205"),
        notes={"es": [*PRICE_NOTES["es"],
                      "No hay una serie abierta y comparable de precios industriales de EE. UU. y China con la misma metodología."],
               "en": [*PRICE_NOTES["en"],
                      "There is no open, comparable series of industrial prices for the US and China using the same method."]},
        rows=sorted(out, key=lambda r: (r["series"], r["time"])),
        geos=geo.geo_table(["EU27"]),
        extra={"dimensions": {"series": TAXES}},
    )


BUILDERS = [renovables_ue, precio_industria_ue]
