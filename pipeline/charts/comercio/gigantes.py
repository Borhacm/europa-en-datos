"""Comercio. Mirada 1: la UE frente a EE. UU. y China en el comercio mundial."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source

BLOCS = ["EU27_2020", "US", "CN_X_HK", "JP"]
TRADE_NOTE = {
    "es": ["Para la UE solo cuenta el comercio con países de fuera de la Unión: las ventas entre Estados miembros no son exportaciones mundiales.",
           "China no incluye Hong Kong.",
           "Comercio de bienes. No incluye servicios."],
    "en": ["For the EU only trade with non-EU countries counts: sales between member states are not world exports.",
           "China excludes Hong Kong.",
           "Trade in goods. Services are not included."],
}


def _rows(indics: dict[str, str], scale: float = 1.0) -> list[dict]:
    rows = sources.eurostat("ext_lt_introeu27_2020", indic_et=list(indics), sitc06="TOTAL", geo=BLOCS)
    return [{"geo": geo.from_eurostat(r["geo"]), "time": r["time"], "flow": indics[r["indic_et"]],
             "value": round(r["value"] * scale, 2)} for r in rows]


def cuota_mundial():
    out = _rows({"PC_EXP_WRL": "exportaciones", "PC_IMP_WRL": "importaciones"})
    return chart(
        id="cg1-cuota-mundial",
        lens="gigantes", theme="comercio",
        title={"es": "China ya exporta más que la UE: desde 2002 casi ha triplicado su cuota del comercio mundial",
               "en": "China now exports more than the EU: its share of world trade has almost tripled since 2002"},
        subtitle={"es": "Cuota de cada economía en las exportaciones o importaciones mundiales de bienes, en %",
                  "en": "Each economy's share of world exports or imports of goods, in %"},
        unit={"es": "% del total mundial", "en": "% of world total"},
        source=eurostat_source("ext_lt_introeu27_2020"),
        notes=TRADE_NOTE,
        rows=sorted(out, key=lambda r: (r["flow"], r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"flow": {
            "exportaciones": {"es": "Exportaciones", "en": "Exports"},
            "importaciones": {"es": "Importaciones", "en": "Imports"}}}},
    )


def saldo_comercial():
    out = _rows({"MIO_BAL_VAL": "saldo"}, scale=1 / 1000)
    for r in out:
        r.pop("flow")
    return chart(
        id="cg2-saldo-comercial",
        lens="gigantes", theme="comercio",
        title={"es": "En 2024, China vendió al mundo 916.000 millones de euros más de lo que compró; EE. UU. compró 1,19 billones más de lo que vendió",
               "en": "In 2024, China sold the world 916 billion euros more than it bought; the US bought 1.19 trillion more than it sold"},
        subtitle={"es": "Saldo comercial de bienes (exportaciones menos importaciones), en miles de millones de euros",
                  "en": "Trade balance in goods (exports minus imports), in billions of euros"},
        unit={"es": "miles de millones de euros", "en": "billions of euros"},
        source=eurostat_source("ext_lt_introeu27_2020"),
        notes=TRADE_NOTE,
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


PARTNERS = {"CN_X_HK": "CHN", "US": "USA"}


def saldo_bilateral():
    rows = sources.eurostat("ext_lt_maineu", indic_et="MIO_BAL_VAL", partner=list(PARTNERS), geo="EU27_2020")
    out = [{"geo": PARTNERS[r["partner"]], "time": r["time"], "value": round(r["value"] / 1000, 1)} for r in rows]
    return chart(
        id="cg3-saldo-bilateral",
        lens="gigantes", theme="comercio",
        title={"es": "La UE compra a China 371.600 millones de euros más de lo que le vende, y vende a EE. UU. 198.000 millones más de lo que le compra",
               "en": "The EU buys 371.6 billion euros more from China than it sells to it, and sells 198 billion more to the US than it buys"},
        subtitle={"es": "Saldo comercial de bienes de la UE con China y con EE. UU. (exportaciones de la UE menos importaciones), en miles de millones de euros",
                  "en": "EU trade balance in goods with China and with the US (EU exports minus imports), in billions of euros"},
        unit={"es": "miles de millones de euros", "en": "billions of euros"},
        source=eurostat_source("ext_lt_maineu"),
        notes={"es": ["Un saldo positivo significa que la UE vende a ese país más de lo que le compra.",
                      "Euros corrientes, sin descontar la inflación. China no incluye Hong Kong. Comercio de bienes: no incluye servicios."],
               "en": ["A positive balance means the EU sells that country more than it buys from it.",
                      "Current euros, not adjusted for inflation. China excludes Hong Kong. Trade in goods: services are not included."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"ref_line": {"value": 0, "label": {"es": "Equilibrio", "en": "Balance"}}},
    )


BUILDERS = [cuota_mundial, saldo_comercial, saldo_bilateral]
