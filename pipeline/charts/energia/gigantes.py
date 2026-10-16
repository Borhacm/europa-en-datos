"""Energía. Mirada 1: consumo de energía y mezcla eléctrica de la UE, EE. UU. y China."""

from collections import defaultdict

from lib import geo
from lib.output import chart

from ..common import worldbank_rows, worldbank_source

# Último año con datos de los tres bloques (China no tiene 2025)
LAST_YEAR = 2024
BLOCS = ["USA", "CHN", "EU27"]
IEA_NOTE = {
    "es": "Estadísticas de energía de la Agencia Internacional de la Energía (AIE) publicadas por el Banco Mundial.",
    "en": "International Energy Agency (IEA) energy statistics published by the World Bank.",
}
# Fuentes de generación eléctrica del Banco Mundial (% de la producción total)
SOURCES = {
    "coal": ("EG.ELC.COAL.ZS", {"es": "Carbón", "en": "Coal"}),
    "gas": ("EG.ELC.NGAS.ZS", {"es": "Gas natural", "en": "Natural gas"}),
    "oil": ("EG.ELC.PETR.ZS", {"es": "Petróleo", "en": "Oil"}),
    "nuclear": ("EG.ELC.NUCL.ZS", {"es": "Nuclear", "en": "Nuclear"}),
    "hydro": ("EG.ELC.HYRO.ZS", {"es": "Hidráulica", "en": "Hydro"}),
}
MIX = {
    "fossil": {"es": "Combustibles fósiles", "en": "Fossil fuels"},
    "coal": SOURCES["coal"][1],
    "gas": SOURCES["gas"][1],
    "nuclear": SOURCES["nuclear"][1],
    "hydro": SOURCES["hydro"][1],
    "other": {"es": "Eólica, solar y otras", "en": "Wind, solar and other"},
}


def consumo():
    out = worldbank_rows("EG.USE.PCAP.KG.OE", 2000, LAST_YEAR)
    out = [{**r, "value": round(r["value"])} for r in out]
    return chart(
        id="eng1-consumo-habitante",
        lens="gigantes", theme="energia",
        title={"es": "Un habitante de China ya consume más energía que uno de la UE; uno de EE. UU., 2,3 veces más",
               "en": "A person in China now uses more energy than one in the EU; a person in the US, 2.3 times as much"},
        subtitle={"es": "Consumo de energía primaria por habitante, en kilos equivalentes de petróleo",
                  "en": "Primary energy use per person, in kilograms of oil equivalent"},
        unit={"es": "kg equivalentes de petróleo por habitante", "en": "kg of oil equivalent per person"},
        source=worldbank_source("EG.USE.PCAP.KG.OE", "consumo de energía (kg de equivalente de petróleo por habitante)"),
        notes={"es": [IEA_NOTE["es"],
                      "Energía primaria: la que entra en el sistema antes de transformarse (petróleo, gas, carbón, uranio, viento, sol...), incluida la que se pierde al generar electricidad. Por eso pesan más las centrales térmicas y nucleares, que pierden buena parte de la energía en forma de calor, que la eólica o la solar.",
                      "En gris, los países de la UE."],
               "en": [IEA_NOTE["en"],
                      "Primary energy: what enters the system before it is transformed (oil, gas, coal, uranium, wind, sun...), including what is lost when generating electricity. That is why thermal and nuclear plants, which lose much of their energy as heat, weigh more than wind or solar.",
                      "In grey, EU countries."]},
        rows=out,
        geos=geo.geo_table(r["geo"] for r in out),
    )


def mezcla_electrica():
    values = defaultdict(dict)  # (geo, time) -> {fuente: valor}
    for key, (indicator, _) in SOURCES.items():
        for r in worldbank_rows(indicator, 2000, LAST_YEAR):
            if r["geo"] in BLOCS:
                values[(r["geo"], r["time"])][key] = r["value"]
    out = []
    for (g, t), v in values.items():
        if len(v) < len(SOURCES):
            continue
        fossil = v["coal"] + v["gas"] + v["oil"]
        shares = {"fossil": fossil, "coal": v["coal"], "gas": v["gas"], "nuclear": v["nuclear"],
                  "hydro": v["hydro"], "other": 100 - fossil - v["nuclear"] - v["hydro"]}
        out += [{"geo": g, "time": t, "source": k, "value": round(x, 1)} for k, x in shares.items()]
    return chart(
        id="eng2-mezcla-electrica",
        lens="gigantes", theme="energia",
        title={"es": "En la UE, el 27,8 % de la electricidad sale de combustibles fósiles; en EE. UU., el 58,3 %, y en China, el 61,6 %",
               "en": "In the EU, 27.8% of electricity comes from fossil fuels; in the US, 58.3%, and in China, 61.6%"},
        subtitle={"es": "Producción de electricidad según la fuente, en % del total",
                  "en": "Electricity production by source, as % of the total"},
        unit={"es": "% de la producción eléctrica", "en": "% of electricity production"},
        source={**worldbank_source("EG.ELC.COAL.ZS", "producción de electricidad por fuente (% del total)"),
                "dataset": ", ".join(ind for ind, _ in SOURCES.values())},
        notes={"es": [IEA_NOTE["es"],
                      "Combustibles fósiles: carbón, gas natural y petróleo. 'Eólica, solar y otras' es lo que queda al restar los fósiles, la nuclear y la hidráulica: sobre todo eólica, solar y biomasa, más una pequeña parte de residuos y otras fuentes.",
                      f"Se muestra hasta {LAST_YEAR}, el último año con datos de los tres bloques."],
               "en": [IEA_NOTE["en"],
                      "Fossil fuels: coal, natural gas and oil. 'Wind, solar and other' is what remains after subtracting fossil fuels, nuclear and hydro: mostly wind, solar and biomass, plus a small share of waste and other sources.",
                      f"Shown up to {LAST_YEAR}, the last year with data for all three blocs."]},
        rows=sorted(out, key=lambda r: (r["source"], r["geo"], r["time"])),
        geos=geo.geo_table(BLOCS),
        extra={"dimensions": {"source": MIX}},
    )


BUILDERS = [consumo, mezcla_electrica]
