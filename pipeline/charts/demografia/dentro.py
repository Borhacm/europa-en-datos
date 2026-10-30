"""Demografía. Mirada 3: fecundidad y población nacida fuera de la UE en cada país."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


TFR_BASE, TFR_YEAR = "2014", "2024"


def fecundidad_paises():
    raw = sources.eurostat("demo_find", indic_de="TOTFERRT", time=[TFR_BASE, TFR_YEAR])
    out = [r for r in from_eurostat(raw, []) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    for r in out:
        r.pop("flag", None)
    v = {(r["geo"], r["time"]): r["value"] for r in out}
    countries = sorted((c for c in geo.EU27 if (c, TFR_YEAR) in v), key=lambda c: v[(c, TFR_YEAR)])
    down = [c for c in countries if v[(c, TFR_YEAR)] < v[(c, TFR_BASE)]]
    up = [c for c in countries if v[(c, TFR_YEAR)] > v[(c, TFR_BASE)]]
    low, top = countries[0], countries[-1]
    assert len(countries) == 27 and top == "BGR" and low == "MLT", (top, low)
    up_es = ", ".join(geo.name(c, "es") for c in up[:-1]) + f" y {geo.name(up[-1], 'es')}"
    up_en = ", ".join(geo.name(c, "en") for c in up[:-1]) + f" and {geo.name(up[-1], 'en')}"
    return chart(
        id="dmd1-fecundidad-paises",
        lens="dentro", theme="demografia",
        title={"es": f"La fecundidad ha bajado desde {TFR_BASE} en {len(down)} de los 27 países; solo ha subido en {up_es}",
               "en": f"Fertility has fallen since {TFR_BASE} in {len(down)} of the 27 countries; it has only risen in {up_en}"},
        subtitle={"es": f"Tasa de fecundidad: hijos por mujer, {TFR_BASE} y {TFR_YEAR}. UE: {fmt_es(v[('EU27', TFR_YEAR)])}",
                  "en": f"Fertility rate: births per woman, {TFR_BASE} and {TFR_YEAR}. EU: {v[('EU27', TFR_YEAR)]:g}"},
        unit={"es": "hijos por mujer", "en": "births per woman"},
        source=eurostat_source("demo_find"),
        notes={"es": [f"En {TFR_YEAR}, la tasa va de {fmt_es(v[(low, TFR_YEAR)])} hijos por mujer en {geo.name(low, 'es')} a {fmt_es(v[(top, TFR_YEAR)])} en {geo.name(top, 'es')}. Ningún país llega a los 2,1 que mantienen la población sin migración.",
                      "Datos de los registros civiles de cada país. La tasa de un año depende también de cuándo se tienen los hijos: si las mujeres los retrasan, baja aunque al final tengan los mismos."],
               "en": [f"In {TFR_YEAR}, the rate ranges from {v[(low, TFR_YEAR)]:g} births per woman in {geo.name(low, 'en')} to {v[(top, TFR_YEAR)]:g} in {geo.name(top, 'en')}. No country reaches the 2.1 that keeps a population steady without migration.",
                      "Data from each country's civil registers. The rate in a given year also depends on when children are born: if women delay them, it falls even if in the end they have the same number."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


POP_BASE, POP_YEAR = "2021", "2025"


def nacidos_fuera():
    raw = sources.eurostat("migr_pop3ctb", age="TOTAL", sex="T", c_birth=["TOTAL", "NEU27_2020_FOR"], time=[POP_BASE, POP_YEAR])
    rows = from_eurostat(raw, ["c_birth"])
    n = {(r["geo"], r["time"], r["c_birth"]): r["value"] for r in rows}
    out = []
    for (g, t, cb), val in n.items():
        if cb != "NEU27_2020_FOR" or not (g in geo.EU27 or g == "EU27") or (g, t, "TOTAL") not in n:
            continue
        out.append({"geo": g, "time": t, "value": round(100 * val / n[(g, t, "TOTAL")], 1)})
    v = {(r["geo"], r["time"]): r["value"] for r in out}
    countries = sorted((c for c in geo.EU27 if (c, POP_YEAR) in v), key=lambda c: v[(c, POP_YEAR)])
    missing = [c for c in geo.EU27 if (c, POP_YEAR) not in v]
    low, top = countries[0], countries[-1]
    rose = [c for c in countries if (c, POP_BASE) in v and v[(c, POP_YEAR)] > v[(c, POP_BASE)]]
    eu_m = round(n[("EU27", POP_YEAR, "NEU27_2020_FOR")] / 1e6, 1)
    assert top == "MLT" and low == "SVK" and missing == ["PRT"], (top, low, missing)
    miss_es = ", ".join(geo.name(c, "es") for c in missing)
    miss_en = ", ".join(geo.name(c, "en") for c in missing)
    return chart(
        id="dmd2-nacidos-fuera",
        lens="dentro", theme="demografia",
        title={"es": f"En {geo.name(top, 'es')}, el {fmt_es(v[(top, POP_YEAR)])} % de los habitantes nació fuera de la UE; en {geo.name(low, 'es')}, el {fmt_es(v[(low, POP_YEAR)])} %",
               "en": f"In {geo.name(top, 'en')}, {v[(top, POP_YEAR)]:g}% of residents were born outside the EU; in {geo.name(low, 'en')}, {v[(low, POP_YEAR)]:g}%"},
        subtitle={"es": f"Población nacida fuera de la UE, en % de la población, {POP_BASE} y {POP_YEAR}. UE: {fmt_es(v[('EU27', POP_YEAR)])} %",
                  "en": f"Population born outside the EU, as % of the population, {POP_BASE} and {POP_YEAR}. EU: {v[('EU27', POP_YEAR)]:g}%"},
        unit={"es": "% de la población", "en": "% of the population"},
        source=eurostat_source("migr_pop3ctb"),
        notes={"es": [f"Población a 1 de enero. En {POP_YEAR}, {fmt_es(eu_m)} millones de residentes en la UE habían nacido fuera de ella. La parte ha subido desde {POP_BASE} en {len(rose)} de los {len(countries)} países con dato.",
                      "Cuenta el país de nacimiento, no la nacionalidad: incluye a quienes ya tienen la nacionalidad del país en el que viven y no incluye a los nacidos en otro país de la UE.",
                      f"Se empieza en {POP_BASE} porque es el primer año con dato para todos los países. Sin dato de {POP_YEAR} para {miss_es}."],
               "en": [f"Population on 1 January. In {POP_YEAR}, {eu_m:g} million EU residents had been born outside it. The share has risen since {POP_BASE} in {len(rose)} of the {len(countries)} countries with data.",
                      "It counts country of birth, not nationality: it includes people who already hold the nationality of the country they live in and excludes those born in another EU country.",
                      f"The chart starts in {POP_BASE} because it is the first year with data for every country. No {POP_YEAR} figure for {miss_en}."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [fecundidad_paises, nacidos_fuera]
