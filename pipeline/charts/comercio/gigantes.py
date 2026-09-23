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
        title={"es": "China vende al mundo, EE. UU. le compra y la UE está en medio",
               "en": "China sells to the world, the US buys, and the EU sits in between"},
        subtitle={"es": "Saldo comercial de bienes (exportaciones menos importaciones), en miles de millones de euros",
                  "en": "Trade balance in goods (exports minus imports), in billions of euros"},
        unit={"es": "miles de millones de euros", "en": "billions of euros"},
        source=eurostat_source("ext_lt_introeu27_2020"),
        notes=TRADE_NOTE,
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [cuota_mundial, saldo_comercial]
