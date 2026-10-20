"""Transporte. Mirada 2: cómo se mueven los europeos y qué coches compran."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source

MODES = {"CAR": {"es": "Coche", "en": "Car"}, "BUS_TOT": {"es": "Autobús", "en": "Bus and coach"}, "TRN": {"es": "Tren", "en": "Train"}}
START = "2000"
CO2_CARS = {"name": "Reglamento (UE) 2023/851, que refuerza las normas de emisiones de CO2 de los turismos nuevos",
            "url": "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32023R0851"}


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def reparto_viajeros():
    rows = sources.eurostat("tran_hv_psmod", geo="EU27_2020", unit="PC")
    out = [{"geo": "EU27", "time": r["time"], "series": r["vehicle"], "value": r["value"]}
           for r in rows if r["vehicle"] in MODES and r["time"] >= START]
    v = {(r["series"], r["time"]): r["value"] for r in out}
    last = max(r["time"] for r in out)
    assert v[("CAR", last)] > 80 and v[("CAR", START)] > 80
    return chart(
        id="tre1-reparto-viajeros",
        lens="elige", theme="transporte",
        title={"es": f"El coche sigue moviendo a más de 8 de cada 10 viajeros en la UE, igual que en {START}; el tren, al {fmt_es(v[('TRN', last)])} %",
               "en": f"Cars still carry more than 8 in 10 passengers in the EU, as in {START}; trains, {v[('TRN', last)]:g}%"},
        subtitle={"es": f"Reparto del transporte terrestre de viajeros por modo, en % de los pasajeros-kilómetro, {START}-{last}",
                  "en": f"Inland passenger transport by mode, as % of passenger-kilometres, {START}-{last}"},
        unit={"es": "% de los pasajeros-km", "en": "% of passenger-km"},
        source=eurostat_source("tran_hv_psmod"),
        notes={"es": ["Solo transporte terrestre: coche, autobús y tren (con metro y tranvía). No incluye el avión, la bicicleta ni los desplazamientos a pie.",
                      "En 2020 y 2021, la pandemia hundió el transporte público: el tren y el autobús cayeron y el coche ganó peso.",
                      "De 2009 a 2013, Eurostat marca el dato de la UE como estimado y con ruptura de serie. El salto del tren de 2010 a 2012 coincide con unos datos anómalos de Francia, donde el tren aparece esos tres años con el 99,1 % de los viajeros."],
               "en": ["Inland transport only: car, bus and train (including metro and tram). It excludes air travel, cycling and walking.",
                      "In 2020 and 2021 the pandemic hit public transport: trains and buses fell and cars gained share.",
                      "From 2009 to 2013, Eurostat flags the EU figure as estimated and with a break in series. The jump in rail from 2010 to 2012 coincides with anomalous data for France, where trains appear with 99.1% of passengers in those three years."]},
        rows=sorted(out, key=lambda r: (r["series"], r["time"])),
        geos=geo.geo_table(["EU27"]),
        extra={"dimensions": {"series": MODES}},
    )


# Coches nuevos por tipo de motor. Los híbridos sin enchufe aparecen en Eurostat desde 2023
FUELS = {
    "HYB": {"es": "Híbrido sin enchufe", "en": "Non-plug-in hybrid", "parts": ["ELC_PET_HYB", "ELC_DIE_HYB"]},
    "PET": {"es": "Gasolina", "en": "Petrol", "parts": ["PET_X_HYB"]},
    "ELC": {"es": "Eléctrico", "en": "Battery electric", "parts": ["ELC"]},
    "DIE": {"es": "Diésel", "en": "Diesel", "parts": ["DIE_X_HYB"]},
    "PHEV": {"es": "Híbrido enchufable", "en": "Plug-in hybrid", "parts": ["ELC_PET_PI", "ELC_DIE_PI"]},
}
FUEL_YEARS = ("2023", "2025")


def combustible_nuevos():
    rows = sources.eurostat("road_eqr_carpda", geo="EU27_2020", unit="NR")
    v = {(r["mot_nrg"], r["time"]): r["value"] for r in rows}
    out = []
    for code, f in FUELS.items():
        for t in FUEL_YEARS:
            out.append({"geo": code, "time": t, "value": round(100 * sum(v.get((p, t), 0) for p in f["parts"]) / v[("TOTAL", t)], 1)})
    s = {(r["geo"], r["time"]): r["value"] for r in out}
    last = FUEL_YEARS[-1]
    assert max(FUELS, key=lambda c: s[(c, last)]) == "HYB" and s[("PET", FUEL_YEARS[0])] > s[("HYB", FUEL_YEARS[0])]
    return chart(
        id="tre2-combustible-nuevos",
        lens="elige", theme="transporte",
        title={"es": f"Los híbridos sin enchufe ya son el tipo de coche nuevo más vendido en la UE, el {fmt_es(s[('HYB', last)])} %; en {FUEL_YEARS[0]} lo era el de gasolina",
               "en": f"Non-plug-in hybrids are now the best-selling type of new car in the EU, at {s[('HYB', last)]:g}%; in {FUEL_YEARS[0]} it was petrol"},
        subtitle={"es": f"Matriculaciones de turismos nuevos por tipo de motor, en % del total, {FUEL_YEARS[0]} y {last}",
                  "en": f"New passenger car registrations by type of engine, as % of the total, {FUEL_YEARS[0]} and {last}"},
        unit={"es": "% de los coches nuevos", "en": "% of new cars"},
        source={**eurostat_source("road_eqr_carpda"), "also": [CO2_CARS]},
        notes={"es": ["Híbrido sin enchufe: combina un motor de combustión con uno eléctrico que no se enchufa a la red. Gasolina y diésel: sin ningún tipo de hibridación.",
                      f"Eurostat da el desglose completo de los híbridos (de gasolina y de diésel) desde {FUEL_YEARS[0]}. El resto, hasta el 100 %, son coches de gas, hidrógeno y otros combustibles."],
               "en": ["Non-plug-in hybrid: combines a combustion engine with an electric motor that is not plugged into the grid. Petrol and diesel: with no hybridisation.",
                      f"Eurostat gives the full breakdown of hybrids (petrol and diesel) since {FUEL_YEARS[0]}. The rest, up to 100%, are gas, hydrogen and other fuel cars."]},
        rows=out,
        geos={k: {"es": f["es"], "en": f["en"], "eu": False, "aggregate": False} for k, f in FUELS.items()},
    )


BUILDERS = [reparto_viajeros, combustible_nuevos]
