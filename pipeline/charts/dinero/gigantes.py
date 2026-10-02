"""Dinero. Mirada 1: efectivo y pagos sin efectivo en la zona del euro, EE. UU. y China."""

from lib import geo, sources
from lib.output import chart

# El BIS publica la zona del euro (XM), no la UE27
EA = {"es": "Zona del euro", "en": "Euro area", "eu": False, "aggregate": True}
BIS_GEO = {"XM": "EA", "US": "USA", "CN": "CHN", "BE": "BEL", "DE": "DEU", "ES": "ESP",
           "FR": "FRA", "IT": "ITA", "NL": "NLD", "SE": "SWE"}


def bis_source(what: str) -> dict:
    return {"name": f"BIS, estadísticas de pagos del CPMI ({what})", "dataset": "WS_CPMI_CT1",
            "url": "https://data.bis.org/topics/CPMI_CT", "license": "BIS terms of use (reutilización con cita)"}


def _bis(title: str, unit: str, digits: int) -> list[dict]:
    out = []
    for r in sources.bis("WS_CPMI_CT1"):
        code = BIS_GEO.get(r["REP_CTY"])
        if code and r["TITLE_TS"].split(" - ", 1)[1] == title and r["UNIT_MEASURE"] == unit:
            out.append({"geo": code, "time": r["TIME_PERIOD"], "value": round(float(r["OBS_VALUE"]), digits)})
    return sorted(out, key=lambda r: (r["geo"], r["time"]))


def _geos(codes) -> dict:
    codes = set(codes)
    table = geo.geo_table(codes - {"EA"})
    if "EA" in codes:
        table["EA"] = EA
    return table


def efectivo_pib():
    out = [r for r in _bis("Value of Banknotes and coins", "I", 2) if r["geo"] in ("EA", "USA", "CHN")]
    return chart(
        id="dig1-efectivo-pib",
        lens="gigantes", theme="dinero",
        title={"es": "La zona del euro tiene más efectivo en relación con su economía que China y EE. UU.: el 10,7 % de su PIB",
               "en": "The euro area holds more cash relative to its economy than China and the US: 10.7% of its GDP"},
        subtitle={"es": "Billetes y monedas en circulación, en % del PIB",
                  "en": "Banknotes and coins in circulation, as % of GDP"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source=bis_source("billetes y monedas en circulación"),
        notes={"es": ["El BIS publica la zona del euro (los países que usan el euro cada año), no la UE de 27: Suecia, Polonia o Hungría, por ejemplo, tienen su propia moneda.",
                      "Es todo el efectivo emitido, se use o no para pagar: incluye el que se guarda como ahorro y el que circula fuera de la zona emisora, algo habitual en monedas internacionales como el dólar y el euro.",
                      "La serie de cada bloque es la que publica su banco central al CPMI; China incluye los billetes y monedas en yuanes (M0)."],
               "en": ["The BIS publishes the euro area (the countries using the euro each year), not the 27-country EU: Sweden, Poland and Hungary, for example, have their own currency.",
                      "This is all the cash issued, whether or not it is used for payments: it includes cash kept as savings and cash circulating outside the issuing area, which is common for international currencies such as the dollar and the euro.",
                      "Each bloc's series is the one its central bank reports to the CPMI; for China it is yuan banknotes and coins (M0)."]},
        rows=out,
        geos=_geos(r["geo"] for r in out),
    )


def pagos_sin_efectivo():
    out = _bis("Number of Cashless payments, All", "Q", 1)
    out = [r for r in out if r["geo"] != "EA"]
    return chart(
        id="dig2-pagos-sin-efectivo",
        lens="gigantes", theme="dinero",
        title={"es": "Suecia hace más pagos sin efectivo por habitante que EE. UU.; China los ha multiplicado por casi 28 desde 2012",
               "en": "Sweden makes more cashless payments per person than the US; China has multiplied them by almost 28 since 2012"},
        subtitle={"es": "Pagos sin efectivo (tarjetas, transferencias, adeudos, dinero electrónico y cheques) por habitante y año",
                  "en": "Cashless payments (cards, credit transfers, direct debits, e-money and cheques) per person per year"},
        unit={"es": "pagos por habitante", "en": "payments per person"},
        source=bis_source("número de pagos sin efectivo por habitante"),
        notes={"es": ["El BIS no publica este dato para la zona del euro ni para la UE: se muestran los siete países de la UE que informan al CPMI. Los Países Bajos solo tienen datos hasta 2021 y España desde 2014.",
                      "Cada banco central recoge los pagos con sus propias fuentes y definiciones: las tendencias son más comparables que los niveles exactos entre países.",
                      "Cuenta operaciones, no su importe."],
               "en": ["The BIS does not publish this figure for the euro area or the EU: the chart shows the seven EU countries that report to the CPMI. The Netherlands only has data up to 2021, and Spain from 2014.",
                      "Each central bank collects payment data with its own sources and definitions: trends are more comparable than exact levels across countries.",
                      "It counts transactions, not their value."]},
        rows=out,
        geos=_geos(r["geo"] for r in out),
    )


BUILDERS = [efectivo_pib, pagos_sin_efectivo]
