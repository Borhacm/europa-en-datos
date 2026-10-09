"""Vivienda. Mirada 1: precio de la vivienda y alquileres en la zona del euro, EE. UU. y China."""

from collections import defaultdict

from lib import geo, sources
from lib.output import chart

# El BIS y la OCDE publican la zona del euro, no la UE27
EA = {"es": "Zona del euro", "en": "Euro area", "eu": False, "aggregate": True}
BIS_GEO = {"XM": "EA", "US": "USA", "CN": "CHN"}
START = 2005


def _geos(codes) -> dict:
    codes = set(codes)
    table = geo.geo_table(codes - {"EA"})
    if "EA" in codes:
        table["EA"] = EA
    return table


def _annual(quarters: dict[str, list[float]]) -> dict[str, float]:
    """Media anual de un índice trimestral, solo en los años con los cuatro trimestres."""
    return {y: sum(v) / 4 for y, v in quarters.items() if len(v) == 4}


def precio_real():
    # Precios reales de la vivienda residencial (deflactados con el IPC), índice 2010 = 100
    by_geo = defaultdict(lambda: defaultdict(list))
    for r in sources.bis("WS_SPP", "Q.US+CN+XM.R.628"):
        by_geo[BIS_GEO[r["REF_AREA"]]][r["TIME_PERIOD"][:4]].append(float(r["OBS_VALUE"]))
    out = [{"geo": g, "time": y, "value": round(v, 1)}
           for g, quarters in by_geo.items() for y, v in _annual(quarters).items() if int(y) >= START]
    return chart(
        id="vig1-precio-real",
        lens="gigantes", theme="vivienda",
        title={"es": "Descontada la inflación, la vivienda cuesta un 11 % más que en 2010 en la zona del euro, un 58,5 % más en EE. UU. y un 10,5 % menos en China",
               "en": "After inflation, housing costs 11% more than in 2010 in the euro area, 58.5% more in the US and 10.5% less in China"},
        subtitle={"es": "Precio real de la vivienda residencial, índice 2010 = 100, media anual",
                  "en": "Real residential property prices, index 2010 = 100, annual average"},
        unit={"es": "índice 2010 = 100", "en": "index 2010 = 100"},
        source={"name": "BIS, precios de la propiedad residencial (selección)", "dataset": "WS_SPP",
                "url": "https://data.bis.org/topics/RPP", "license": "BIS terms of use (reutilización con cita)"},
        notes={"es": ["Precios reales: el índice de precios de la vivienda de cada bloque, deflactado con su índice de precios de consumo.",
                      "El BIS publica la zona del euro (los países que usan el euro cada año), no la UE de 27.",
                      "Cada índice lo elabora una fuente nacional distinta y no mide lo mismo: el de EE. UU. cubre todo el país; el de China, las ventas de vivienda nueva en las grandes ciudades. Sirven para comparar la evolución, no el nivel de precios.",
                      "Media de los cuatro trimestres de cada año; China empieza en 2006, su primer año completo."],
               "en": ["Real prices: each bloc's house price index deflated by its consumer price index.",
                      "The BIS publishes the euro area (the countries using the euro each year), not the 27-country EU.",
                      "Each index is compiled by a different national source and they do not measure the same thing: the US index covers the whole country; China's, sales of new homes in large cities. They are useful to compare trends, not price levels.",
                      "Average of the four quarters of each year; China starts in 2006, its first full year."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=_geos(r["geo"] for r in out),
    )


def alquileres():
    rows = sources.oecd("OECD.ECO.MPD,DSD_AN_HOUSE_PRICES@DF_HOUSE_PRICES,1.0", "EA+USA.A.RPI.IX", start=str(START))
    out = [{"geo": r["REF_AREA"], "time": r["TIME_PERIOD"], "value": round(float(r["OBS_VALUE"]), 1)} for r in rows]
    return chart(
        id="vig2-alquileres",
        lens="gigantes", theme="vivienda",
        title={"es": "Entre 2015 y 2024, los alquileres subieron un 46,9 % en EE. UU. y un 15,5 % en la zona del euro",
               "en": "Between 2015 and 2024, rents rose 46.9% in the US and 15.5% in the euro area"},
        subtitle={"es": "Índice de precios del alquiler, 2015 = 100, en precios corrientes",
                  "en": "Rent price index, 2015 = 100, at current prices"},
        unit={"es": "índice 2015 = 100", "en": "index 2015 = 100"},
        source={"name": "OCDE, Analytical house prices indicators", "dataset": "DSD_AN_HOUSE_PRICES@DF_HOUSE_PRICES",
                "url": "https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_AN_HOUSE_PRICES%40DF_HOUSE_PRICES&df[ag]=OECD.ECO.MPD",
                "license": "CC BY 4.0"},
        notes={"es": ["Componente de alquiler del índice de precios de consumo: lo que pagan los inquilinos, en precios corrientes, sin descontar la inflación.",
                      "La OCDE publica la zona del euro, no la UE de 27. No hay serie comparable para China.",
                      "El de EE. UU. llega hasta 2024 en la serie anual de la OCDE."],
               "en": ["Rent component of the consumer price index: what tenants pay, at current prices, not adjusted for inflation.",
                      "The OECD publishes the euro area, not the 27-country EU. There is no comparable series for China.",
                      "The US series runs to 2024 in the OECD's annual data."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=_geos(r["geo"] for r in out),
    )


BUILDERS = [precio_real, alquileres]
