"""Dinero. Mirada 2: cómo pagan los europeos y de quién dependen los pagos electrónicos."""

from lib.output import chart

from ._ecb import PAY_SOURCE, pay_annual
from .gigantes import EA

SPACE_URL = "https://www.ecb.europa.eu/stats/ecb_surveys/space/html/ecb.space2024~19d46f0f17.en.html"

# Cifras del texto del informe SPACE 2024 del BCE (apartados 2.2 y 3.2; 2016: estudio SUCH)
SPACE = {
    "efectivo": {"2016": 79, "2019": 72, "2022": 59, "2024": 52},
    "prefiere_tarjeta": {"2016": 43, "2019": 49, "2022": 55, "2024": 55},
    "prefiere_efectivo": {"2016": 32, "2019": 27, "2022": 22, "2024": 22},
}
SPACE_SERIES = {
    "efectivo": {"es": "Pagos en efectivo", "en": "Cash payments"},
    "prefiere_tarjeta": {"es": "Prefiere tarjeta", "en": "Prefer cards"},
    "prefiere_efectivo": {"es": "Prefiere efectivo", "en": "Prefer cash"},
}


def pago_en_tienda():
    out = [{"geo": "EA", "series": s, "time": t, "value": v} for s, by in SPACE.items() for t, v in by.items()]
    return chart(
        id="die1-pago-en-tienda",
        lens="elige", theme="dinero",
        title={"es": "El efectivo ha pasado del 79 % al 52 % de los pagos en tienda desde 2016; el 55 % ya prefiere la tarjeta",
               "en": "Cash has fallen from 79% to 52% of in-store payments since 2016; 55% now prefer cards"},
        subtitle={"es": "Zona del euro. Parte de los pagos en tiendas, bares y otros puntos de venta hechos con efectivo, y medio de pago que prefieren los consumidores, en %",
                  "en": "Euro area. Share of payments in shops, bars and other points of sale made in cash, and consumers' preferred means of payment, in %"},
        unit={"es": "%", "en": "%"},
        source={"name": "BCE, estudio sobre las actitudes de pago de los consumidores de la zona del euro (SPACE 2024)",
                "dataset": "SPACE 2024", "url": SPACE_URL, "license": "ECB, reutilización con cita de la fuente"},
        notes={"es": ["Encuesta con diario de pagos: cuenta el número de pagos, no su importe. Por importe, en 2024 las tarjetas suponían el 45 % y el efectivo el 39 %.",
                      "El dato de 2016 procede de un estudio anterior del BCE (SUCH), solo en parte comparable con las encuestas SPACE de 2019, 2022 y 2024.",
                      "«Prefiere tarjeta» incluye otros medios sin efectivo, como el móvil. Cifras tomadas del texto del informe. Quien no prefiere ni efectivo ni tarjeta no tiene una preferencia clara.",
                      "En la misma encuesta, el 62 % considera importante o muy importante poder pagar con efectivo, y el 60 % dice preocuparse por su privacidad en los pagos digitales (2024)."],
               "en": ["Payment diary survey: it counts the number of payments, not their value. By value, cards accounted for 45% and cash for 39% in 2024.",
                      "The 2016 figure comes from an earlier ECB study (SUCH), only partly comparable with the 2019, 2022 and 2024 SPACE surveys.",
                      "\"Prefer cards\" includes other cashless means, such as phones. Figures taken from the text of the report. People who prefer neither cash nor cards have no clear preference.",
                      "In the same survey, 62% consider it important or very important to be able to pay in cash, and 60% say they are concerned about their privacy in digital payments (2024)."]},
        rows=sorted(out, key=lambda r: (r["series"], r["time"])),
        geos={"EA": EA},
        extra={"dimensions": {"series": SPACE_SERIES}},
    )


INSTRUMENTS = {
    "TOTL1": {"es": "Total sin efectivo", "en": "All cashless"},
    "CP0": {"es": "Tarjetas", "en": "Cards"},
    "CT0": {"es": "Transferencias", "en": "Credit transfers"},
    "DD": {"es": "Adeudos", "en": "Direct debits"},
}


def pagos_zona_euro():
    data = pay_annual(list(INSTRUMENTS))
    out = [{"geo": "EA", "series": i, "time": y, "value": round(v / 1000, 2)}
           for (area, i, y), v in data.items() if area == "U2"]
    return chart(
        id="die2-pagos-zona-euro",
        lens="elige", theme="dinero",
        title={"es": "Las tarjetas suman el 57 % de los pagos sin efectivo de la zona del euro",
               "en": "Cards account for 57% of cashless payments in the euro area"},
        subtitle={"es": "Zona del euro. Número de operaciones al año por medio de pago, en miles de millones",
                  "en": "Euro area. Number of transactions per year by payment instrument, in billions"},
        unit={"es": "miles de millones de operaciones", "en": "billion transactions"},
        source=PAY_SOURCE,
        notes={"es": ["Suma de los dos semestres de cada año. El BCE publica esta serie con la metodología actual desde 2022.",
                      "El total incluye también el dinero electrónico, los cheques y otros pagos, y no las retiradas de efectivo. No es la suma exacta de las series, que el BCE mide por separado. La zona del euro incluye a Croacia desde 2023.",
                      "El BCE no publica en esta serie qué parte de los pagos con tarjeta pasa por sistemas internacionales como Visa o Mastercard: según su informe de febrero de 2025, fueron el 61 % en 2022."],
               "en": ["Sum of the two half-years of each year. The ECB publishes this series under the current methodology from 2022.",
                      "The total also includes e-money, cheques and other payments, but not cash withdrawals. It is not the exact sum of the series, which the ECB measures separately. The euro area includes Croatia from 2023.",
                      "This series does not show what share of card payments goes through international schemes such as Visa or Mastercard: according to an ECB report of February 2025, it was 61% in 2022."]},
        rows=sorted(out, key=lambda r: (r["series"], r["time"])),
        geos={"EA": EA},
        extra={"dimensions": {"series": INSTRUMENTS}},
    )


BUILDERS = [pago_en_tienda, pagos_zona_euro]
