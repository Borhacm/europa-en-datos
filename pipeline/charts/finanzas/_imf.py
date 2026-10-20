"""Datos del FMI (DataMapper) por bloques: la UE con el agregado del WEO o ponderando a los 27 por su PIB."""

from lib import geo, sources

WEO_SOURCE = {"name": "FMI, World Economic Outlook (octubre de 2026)", "dataset": "GGXCNL_NGDP",
              "url": "https://www.imf.org/external/datamapper/GGXCNL_NGDP@WEO",
              "license": "Términos de uso del FMI (uso libre citando la fuente)"}
FM_SOURCE = {"name": "FMI, Fiscal Monitor (octubre de 2026)", "dataset": "GGXONLB_G01_GDP_PT",
             "url": "https://www.imf.org/external/datamapper/GGXONLB_G01_GDP_PT@FM",
             "license": "Términos de uso del FMI (uso libre citando la fuente)"}


def series(indicator: str, codes: list[str]) -> dict[tuple[str, str], float]:
    """{(código, año): valor}. Se pide en grupos de diez países: la API rechaza las direcciones largas."""
    out = {}
    for i in range(0, len(codes), 10):
        for r in sources.imf(indicator, codes[i:i + 10]):
            out[(r["iso3"], r["time"])] = r["value"]
    return out


def eu_weighted(indicator: str, year: str) -> float:
    """Media de los 27 ponderada por su PIB en dólares corrientes (NGDPD), para indicadores en % del PIB."""
    v, gdp = series(indicator, geo.EU27), series("NGDPD", geo.EU27)
    missing = [c for c in geo.EU27 if (c, year) not in v or (c, year) not in gdp]
    assert not missing, f"{indicator} {year}: faltan {missing}"
    return sum(v[(c, year)] * gdp[(c, year)] for c in geo.EU27) / sum(gdp[(c, year)] for c in geo.EU27)
