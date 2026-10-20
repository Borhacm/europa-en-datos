"""Transporte. Mirada 3: el tren y el coche eléctrico, país por país."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

BASE = "2020"


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def tren_paises():
    rows = sources.eurostat("tran_hv_psmod", vehicle="TRN", unit="PC")
    last = max(r["time"] for r in rows if r["geo"] == "EU27_2020")
    out = [r for r in from_eurostat([r for r in rows if r["time"] == last], []) if r["geo"] in (*geo.EU27, "EU27")]
    v = {r["geo"]: r["value"] for r in out}
    ranked = sorted((c for c in geo.EU27 if c in v), key=lambda c: v[c], reverse=True)
    assert len(ranked) == 25, ranked
    return chart(
        id="trd1-tren-paises",
        lens="dentro", theme="transporte",
        title={"es": f"En {geo.name(ranked[0], 'es')} y {geo.name(ranked[1], 'es')}, el tren mueve a más de uno de cada ocho viajeros; en {geo.name(ranked[-1], 'es')}, a menos de uno de cada cien",
               "en": f"In {geo.name(ranked[0], 'en')} and {geo.name(ranked[1], 'en')}, trains carry more than one in eight passengers; in {geo.name(ranked[-1], 'en')}, fewer than one in a hundred"},
        subtitle={"es": f"Tren (con metro y tranvía), en % de los pasajeros-kilómetro del transporte terrestre, {last}",
                  "en": f"Train (including metro and tram), as % of inland passenger-kilometres, {last}"},
        unit={"es": "% de los pasajeros-km", "en": "% of passenger-km"},
        source=eurostat_source("tran_hv_psmod"),
        notes={"es": ["Parte del tren en el transporte terrestre de viajeros (coche, autobús y tren). No incluye el avión.",
                      "Chipre y Malta no tienen ferrocarril."],
               "en": ["Rail's share of inland passenger transport (car, bus and train). It excludes air travel.",
                      "Cyprus and Malta have no railways."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def electricos_parque():
    rows = sources.eurostat("road_eqs_carpda", unit="NR")
    last = max(r["time"] for r in rows if r["geo"] == "EU27_2020" and r["mot_nrg"] == "ELC")
    v = {(r["geo"], r["mot_nrg"], r["time"]): r["value"] for r in rows}
    out = []
    for r in rows:
        if r["mot_nrg"] != "TOTAL" or r["time"] not in (BASE, last):
            continue
        code = geo.from_eurostat(r["geo"])
        el = v.get((r["geo"], "ELC", r["time"]))
        if code in (*geo.EU27, "EU27") and el is not None and r["value"]:
            out.append({"geo": code, "time": r["time"], "value": round(100 * el / r["value"], 2)})
    s = {(r["geo"], r["time"]): r["value"] for r in out}
    ranked = sorted(geo.EU27, key=lambda c: s[(c, last)], reverse=True)
    assert len([c for c in geo.EU27 if (c, last) in s]) == 27
    return chart(
        id="trd2-electricos-parque",
        lens="dentro", theme="transporte",
        title={"es": f"Solo el {fmt_es(round(s[('EU27', last)], 1))} % de los coches que circulan por la UE son eléctricos; en {geo.name(ranked[0], 'es')}, el {fmt_es(round(s[(ranked[0], last)], 1))} %",
               "en": f"Only {round(s[('EU27', last)], 1):g}% of the cars on EU roads are electric; in {geo.name(ranked[0], 'en')}, {round(s[(ranked[0], last)], 1):g}%"},
        subtitle={"es": f"Turismos eléctricos de batería, en % del parque de turismos, {BASE} y {last}",
                  "en": f"Battery electric passenger cars, as % of the passenger car fleet, {BASE} and {last}"},
        unit={"es": "% del parque", "en": "% of the fleet"},
        source=eurostat_source("road_eqs_carpda"),
        notes={"es": ["Coches matriculados a 31 de diciembre de cada año. Solo eléctricos de batería: no incluye los híbridos enchufables.",
                      "El parque cambia despacio: cada año se renueva una pequeña parte de los coches que circulan."],
               "en": ["Cars registered at 31 December of each year. Battery electric only: plug-in hybrids are not included.",
                      "The fleet changes slowly: only a small part of the cars on the road is replaced each year."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [tren_paises, electricos_parque]
