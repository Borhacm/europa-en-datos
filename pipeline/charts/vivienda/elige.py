"""Vivienda. Mirada 2: vivienda en propiedad frente a alquiler."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

TENURE = {
    "OWN": {"es": "En propiedad", "en": "Owner"},
    "OWN_L": {"es": "Propietario con hipoteca", "en": "Owner with a mortgage"},
    "OWN_NL": {"es": "Propietario sin hipoteca", "en": "Owner without a mortgage"},
    "RENT_MKT": {"es": "Inquilino a precio de mercado", "en": "Tenant at market rent"},
    "RENT_FR": {"es": "Alquiler reducido o gratuito", "en": "Reduced-rent or free"},
}
SILC_NOTE = {
    "es": "Encuesta de condiciones de vida (EU-SILC). La encuesta cambió de base legal en 2021; algunos países tienen rupturas de serie.",
    "en": "EU Statistics on Income and Living Conditions (EU-SILC). The survey changed its legal basis in 2021; some countries have breaks in series.",
}


def tenencia():
    rows = sources.eurostat("ilc_lvho02", rskpovth="TOTAL", hhcomp="TOTAL", unit="PC", tenure=list(TENURE))
    rows = [r for r in rows if r["time"] >= "2010"]
    out = [r for r in from_eurostat(rows, ["tenure"]) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    return chart(
        id="vie1-tenencia",
        lens="elige", theme="vivienda",
        title={"es": "Casi siete de cada diez europeos viven en una casa propia; solo en Alemania es menos de la mitad",
               "en": "Almost seven in ten Europeans live in a home they own; only in Germany is it fewer than half"},
        subtitle={"es": "Población según el régimen de tenencia de su vivienda, en %",
                  "en": "Population by tenure status of their home, in %"},
        unit={"es": "% de la población", "en": "% of population"},
        source=eurostat_source("ilc_lvho02"),
        notes={"es": [SILC_NOTE["es"],
                      "Cuenta personas, no viviendas: es la parte de la población que vive en un hogar propietario o inquilino.",
                      "El alquiler reducido o gratuito incluye la vivienda social con renta por debajo del mercado y la cedida por familiares o empresas."],
               "en": [SILC_NOTE["en"],
                      "It counts people, not dwellings: the share of the population living in an owner or tenant household.",
                      "Reduced-rent or free housing includes social housing below market rent and homes provided by relatives or employers."]},
        rows=sorted(out, key=lambda r: (r["tenure"], r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"tenure": TENURE}},
    )


def sobrecarga_tenencia():
    keys = ["OWN_NL", "OWN_L", "RENT_FR", "RENT_MKT"]
    rows = sources.eurostat("ilc_lvho07c", unit="PC", geo="EU27_2020", tenure=keys)
    out = [{"geo": r["geo"], "series": r["tenure"], "time": r["time"], "value": r["value"],
            **({"flag": r["flag"]} if r.get("flag") else {})}
           for r in from_eurostat(rows, ["tenure"]) if r["time"] >= "2010"]
    return chart(
        id="vie2-sobrecarga-tenencia",
        lens="elige", theme="vivienda",
        title={"es": "El 18,6 % de los inquilinos a precio de mercado dedica más del 40 % de sus ingresos a la vivienda; entre los propietarios, el 5 % o menos",
               "en": "18.6% of tenants at market rent spend more than 40% of their income on housing; among owners, 5% or less"},
        subtitle={"es": "Población de la UE que vive en hogares que gastan más del 40 % de su renta disponible en vivienda, según régimen de tenencia, en %",
                  "en": "EU population living in households that spend more than 40% of their disposable income on housing, by tenure status, in %"},
        unit={"es": "% de cada grupo", "en": "% of each group"},
        source=eurostat_source("ilc_lvho07c"),
        notes={"es": [SILC_NOTE["es"],
                      "Gastos de vivienda: alquiler o intereses de la hipoteca, más suministros, comunidad y reparaciones habituales, descontadas las ayudas a la vivienda. No incluye la devolución del capital de la hipoteca.",
                      "Eurostat marca como estimación el agregado de la UE de 2010 a 2018."],
               "en": [SILC_NOTE["en"],
                      "Housing costs: rent or mortgage interest, plus utilities, service charges and regular repairs, net of housing allowances. Mortgage principal repayments are not included.",
                      "Eurostat flags the EU aggregate for 2010 to 2018 as an estimate."]},
        rows=sorted(out, key=lambda r: (r["series"], r["time"])),
        geos=geo.geo_table(["EU27"]),
        extra={"dimensions": {"series": {k: TENURE[k] for k in keys}}},
    )


BUILDERS = [tenencia, sobrecarga_tenencia]
