"""Demografía. Mirada 2: la migración como respuesta al envejecimiento y por qué llega la gente de fuera."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

FIRST, LAST = "2000", "2025"
SERIES = {
    "NATGROW": {"es": "Saldo natural", "en": "Natural change"},
    "CNMIGRAT": {"es": "Saldo migratorio", "en": "Net migration"},
}


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def crecimiento_ue():
    raw = sources.eurostat("demo_gind", geo="EU27_2020", indic_de=[*SERIES, "GROW"])
    v = {(r["indic_de"], r["time"]): r["value"] for r in raw if FIRST <= r["time"] <= LAST}
    years = sorted({t for (_, t) in v})
    # Primer año desde el que el saldo natural es siempre negativo
    since = next(t for t in years if all(v[("NATGROW", s)] < 0 for s in years if s >= t))
    falls = [t for t in years if t >= since and v[("GROW", t)] < 0]
    nat, mig = v[("NATGROW", LAST)], v[("CNMIGRAT", LAST)]
    peak = max(years, key=lambda t: v[("CNMIGRAT", t)])
    assert since == "2012" and falls == ["2020"] and peak == "2022" and nat < 0 < nat + mig, (since, falls, peak)
    for t in years:
        assert v[("GROW", t)] == v[("NATGROW", t)] + v[("CNMIGRAT", t)], t
    out = [{"geo": "EU27", "time": t, "series": k, "value": round(v[(k, t)] / 1000)} for k in SERIES for t in years]
    nat_m, mig_m = round(-nat / 1e6, 2), round(mig / 1e6, 2)
    return chart(
        id="dme1-crecimiento-ue",
        lens="elige", theme="demografia",
        title={"es": f"Desde {since} mueren en la UE más personas de las que nacen; en {LAST}, {fmt_es(nat_m)} millones más, y la llegada neta de {fmt_es(mig_m)} millones hizo crecer la población",
               "en": f"Since {since}, more people have died in the EU than have been born; in {LAST}, {nat_m:g} million more, and net arrivals of {mig_m:g} million made the population grow"},
        subtitle={"es": f"Cambio de la población de la UE por sus dos componentes, en miles de personas, {FIRST}-{LAST}",
                  "en": f"Change in the EU population by its two components, in thousands of people, {FIRST}-{LAST}"},
        unit={"es": "miles de personas", "en": "thousands of people"},
        source=eurostat_source("demo_gind"),
        notes={"es": ["Los 27 países actuales en todos los años. El saldo natural es la diferencia entre nacimientos y defunciones. El saldo migratorio es la diferencia entre quienes llegan a vivir a un país de la UE y quienes se van, incluidos los movimientos entre países de la UE, que se compensan en el total.",
                      "Eurostat calcula el saldo migratorio como el cambio de población que no explican los nacimientos y las defunciones, por lo que incluye ajustes estadísticos (por ejemplo, tras un censo).",
                      f"Desde {since}, la población solo bajó en {falls[0]}, con la pandemia: más defunciones y menos llegadas.",
                      "El saldo migratorio más alto de la serie, en 2022, coincide con la llegada de refugiados de Ucrania tras la invasión rusa."],
               "en": ["Today's 27 countries in every year. Natural change is the difference between births and deaths. Net migration is the difference between people who come to live in an EU country and those who leave, including moves between EU countries, which cancel out in the total.",
                      "Eurostat calculates net migration as the change in population not explained by births and deaths, so it includes statistical adjustments (for example, after a census).",
                      f"Since {since}, the population only fell in {falls[0]}, with the pandemic: more deaths and fewer arrivals.",
                      "The highest net migration in the series, in 2022, coincides with the arrival of refugees from Ukraine after the Russian invasion."]},
        rows=out,
        geos=geo.geo_table(["EU27"]),
        extra={"dimensions": {"series": SERIES}},
    )


REASONS = {
    "EMP": {"es": "Trabajo", "en": "Work"},
    "FAM": {"es": "Familia", "en": "Family"},
    "EDUC": {"es": "Estudios", "en": "Education"},
    "OTH": {"es": "Otros motivos", "en": "Other reasons"},
}


def permisos_motivo():
    raw = sources.eurostat("migr_resfirst", citizen="TOTAL", duration="TOTAL", unit="PER", reason=[*REASONS, "TOTAL"], time=LAST)
    rows = from_eurostat(raw, ["reason"])
    total = {r["geo"]: r["value"] for r in rows if r["reason"] == "TOTAL"}
    out = []
    for r in rows:
        if r["reason"] == "TOTAL" or not total.get(r["geo"]) or not (r["geo"] in geo.EU27 or r["geo"] == "EU27"):
            continue
        out.append({"geo": r["geo"], "time": LAST, "reason": r["reason"], "value": round(100 * r["value"] / total[r["geo"]], 1)})
    v = {(r["geo"], r["reason"]): r["value"] for r in out}
    work = [c for c in geo.EU27 if (c, "EMP") in v and v[(c, "EMP")] > 50]
    top = max(REASONS, key=lambda k: v[("EU27", k)])
    assert top == "EMP" and v[("EU27", "EMP")] < 50, top
    eu_m = round(total["EU27"] / 1e6, 2)
    prot = int(next(r["value"] for r in sources.eurostat("migr_resoth", geo="EU27_2020", citizen="TOTAL", duration="TOTAL", unit="PER",
                                                         reason="RFG_SPROT", time=LAST)))
    return chart(
        id="dme2-permisos-motivo",
        lens="elige", theme="demografia",
        title={"es": f"Uno de cada tres primeros permisos de residencia de la UE se da por trabajo ({fmt_es(v[('EU27', 'EMP')])} %) y el {fmt_es(v[('EU27', 'FAM')])} %, por motivos familiares; en {len(work)} países, el trabajo supera la mitad",
               "en": f"One in three first residence permits in the EU is issued for work ({v[('EU27', 'EMP')]:g}%) and {v[('EU27', 'FAM')]:g}% for family reasons; in {len(work)} countries, work accounts for more than half"},
        subtitle={"es": f"Primeros permisos de residencia a ciudadanos de fuera de la UE por motivo, en % del total, {LAST}",
                  "en": f"First residence permits issued to non-EU citizens by reason, as % of the total, {LAST}"},
        unit={"es": "% de los primeros permisos", "en": "% of first permits"},
        source=eurostat_source("migr_resfirst"),
        notes={"es": [f"En {LAST}, los países de la UE dieron {fmt_es(eu_m)} millones de primeros permisos de residencia, de al menos tres meses, a ciudadanos de fuera de la UE.",
                      "Cuenta permisos concedidos, no personas que se quedan: un permiso de estudios o de temporada puede no renovarse.",
                      f"«Otros motivos» incluye la protección internacional (estatuto de refugiado y protección subsidiaria: {prot:,} permisos en {LAST}, según migr_resoth), las razones humanitarias y otros casos.".replace(f"{prot:,}", f"{prot:,}".replace(",", ".")),
                      "Los refugiados de Ucrania con protección temporal tienen su propia estadística (migr_asytpsm)."],
               "en": [f"In {LAST}, EU countries issued {eu_m:g} million first residence permits, valid for at least three months, to non-EU citizens.",
                      "It counts permits granted, not people who stay: a study or seasonal permit may not be renewed.",
                      f"«Other reasons» includes international protection (refugee status and subsidiary protection: {prot:,} permits in {LAST}, according to migr_resoth), humanitarian reasons and other cases.",
                      "Refugees from Ukraine under temporary protection have their own statistics (migr_asytpsm)."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["reason"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"reason": REASONS}},
    )


BUILDERS = [crecimiento_ue, permisos_motivo]
