"""N04. El precio de la luz para los hogares en cada país."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source

BASE, LAST = "2021-S1", "2025-S2"
TAXES = {
    "I_TAX": {"es": "Con impuestos", "en": "Including taxes"},
    "X_TAX": {"es": "Sin impuestos", "en": "Excluding taxes"},
}
# Consumidor tipo de Eurostat (banda DC): entre 2.500 y 5.000 kWh al año
FILTERS = dict(siec="E7000", unit="KWH", currency="EUR", nrg_cons="KWH2500-4999")

NOTES_ES = [
    "Hogares con un consumo de entre 2.500 y 5.000 kWh al año, el tramo de referencia de Eurostat. Precio medio del semestre en euros corrientes, sin descontar la inflación.",
    "El precio sin impuestos incluye la energía, el suministro y las redes. Los impuestos incluyen el IVA, otros impuestos y cargos, y restan las bonificaciones y ayudas públicas que se aplican a través de ellos.",
]
NOTES_EN = [
    "Households consuming 2,500 to 5,000 kWh a year, Eurostat's reference band. Average price for the half-year in current euros, not adjusted for inflation.",
    "The price excluding taxes covers energy, supply and networks. Taxes include VAT, other taxes and levies, net of the allowances and public support applied through them.",
]


def _rows(tax, times):
    rows = sources.eurostat("nrg_pc_204", tax=tax, time=times, **FILTERS)
    # Como from_eurostat, pero en céntimos de euro por kWh (el dato viene en euros con cuatro decimales)
    out = []
    for r in rows:
        code = geo.from_eurostat(r["geo"])
        if code in geo.EU27 or code == "EU27":
            row = {"geo": code, "time": r["time"], "value": round(100 * r["value"], 2), "tax": r["tax"]}
            if r.get("flag"):
                row["flag"] = r["flag"]
            out.append(row)
    return out


def precio_hogares():
    out = _rows(list(TAXES), LAST)
    return chart(
        id="n04-luz-precio",
        lens="dentro", theme="comercio",
        title={"es": "En Irlanda, la luz de los hogares cuesta 3,7 veces lo que en Hungría",
               "en": "Household electricity in Ireland costs 3.7 times as much as in Hungary"},
        subtitle={"es": "Precio de la electricidad para los hogares, segundo semestre de 2025, en céntimos de euro por kWh",
                  "en": "Household electricity price, second half of 2025, in euro cents per kWh"},
        unit={"es": "céntimos de euro por kWh", "en": "euro cents per kWh"},
        source=eurostat_source("nrg_pc_204"),
        notes={"es": NOTES_ES + ["En Países Bajos y Luxemburgo el precio con impuestos es más bajo que sin ellos: Eurostat registra impuestos netos negativos (-5,2 % y -6,3 % del precio), porque las deducciones y ayudas superan a los impuestos.",
                             "Austria: dato estimado. Croacia y Malta: datos provisionales."],
               "en": NOTES_EN + ["In the Netherlands and Luxembourg the price including taxes is lower than without them: Eurostat records negative net taxes (-5.2% and -6.3% of the price), because allowances and support exceed taxes.",
                             "Austria: estimated. Croatia and Malta: provisional."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["tax"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"tax": TAXES}},
    )


def cambio_2021():
    out = [{k: v for k, v in r.items() if k != "tax"} for r in _rows("I_TAX", [BASE, LAST])]
    return chart(
        id="n04-luz-cambio",
        lens="dentro", theme="comercio",
        title={"es": "Desde 2021, la luz de los hogares se ha encarecido en 26 de los 27 países; en la UE, un 31,5 %",
               "en": "Since 2021, household electricity has become more expensive in 26 of the 27 countries; in the EU, by 31.5%"},
        subtitle={"es": "Precio de la electricidad para los hogares, con impuestos, primer semestre de 2021 y segundo semestre de 2025, en céntimos de euro por kWh",
                  "en": "Household electricity price including taxes, first half of 2021 and second half of 2025, in euro cents per kWh"},
        unit={"es": "céntimos de euro por kWh", "en": "euro cents per kWh"},
        source=eurostat_source("nrg_pc_204"),
        notes={"es": NOTES_ES + ["El primer semestre de 2021 es el último antes de la subida de precios de la energía de 2021 y 2022.",
                                 "En Malta el precio apenas ha cambiado (-0,2 %). Austria: dato estimado. Croacia y Malta: datos provisionales en 2025."],
               "en": NOTES_EN + ["The first half of 2021 is the last one before the 2021-2022 energy price surge.",
                                 "In Malta the price has barely changed (-0.2%). Austria: estimated. Croatia and Malta: provisional 2025 data."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [precio_hogares, cambio_2021]
