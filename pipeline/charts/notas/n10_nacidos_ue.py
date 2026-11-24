"""N10. Población nacida en otro país de la UE frente a la nacida fuera de la UE.

El tema Demografía (DM-D2) ya cuenta la parte nacida fuera de la UE por país y su subida desde 2021.
Esta nota la pone al lado de la nacida en otro país de la Unión, que el tema no publica.
"""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

START, END = "2021", "2025"
YEARS = [str(y) for y in range(int(START), int(END) + 1)]

BIRTH = {
    "EU27_2020_FOR": {"es": "Nacidos en otro país de la UE", "en": "Born in another EU country"},
    "NEU27_2020_FOR": {"es": "Nacidos fuera de la UE", "en": "Born outside the EU"},
}

COMMON_NOTES = {
    "es": ["Población residente a 1 de enero, por país de nacimiento. Cuenta dónde nació cada persona, no su nacionalidad: incluye a quienes ya tienen la nacionalidad del país en el que viven.",
           "«Otro país de la UE» es cualquiera de los 26 restantes, con la UE de 27 en todos los años; los nacidos en el Reino Unido cuentan como nacidos fuera de la UE."],
    "en": ["Resident population on 1 January, by country of birth. It counts where each person was born, not their nationality: it includes people who already hold the nationality of the country they live in.",
           "\"Another EU country\" is any of the other 26, using the 27-member EU in every year; people born in the United Kingdom count as born outside the EU."],
}


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def _counts(years):
    raw = sources.eurostat("migr_pop3ctb", age="TOTAL", sex="T", c_birth=["TOTAL", *BIRTH], time=years)
    return {(r["geo"], r["time"], r["c_birth"]): r["value"] for r in from_eurostat(raw, ["c_birth"])}


def nacidos_ue_fuera():
    n = _counts([END])
    out = []
    for g in [*geo.EU27, "EU27"]:
        total = n.get((g, END, "TOTAL"))
        if not total:
            continue
        for cb in BIRTH:
            if (g, END, cb) in n:
                out.append({"geo": g, "time": END, "c_birth": cb, "value": round(100 * n[(g, END, cb)] / total, 1)})
    v = {(r["geo"], r["c_birth"]): r["value"] for r in out}
    countries = [c for c in geo.EU27 if (c, "EU27_2020_FOR") in v and (c, "NEU27_2020_FOR") in v]
    # Se compara con los recuentos, no con los porcentajes redondeados (en Hungría difieren en una décima)
    more_eu = sorted((c for c in countries if n[(c, END, "EU27_2020_FOR")] > n[(c, END, "NEU27_2020_FOR")]),
                     key=lambda c: -v[(c, "EU27_2020_FOR")])
    assert len(countries) == 27 and more_eu == ["LUX", "HUN", "SVK"], (len(countries), more_eu)
    assert v[("EU27", "EU27_2020_FOR")] == 4.0 and v[("EU27", "NEU27_2020_FOR")] == 10.6, v[("EU27", "EU27_2020_FOR")]
    names_es = ", ".join(geo.name(c, "es") for c in more_eu[:-1]) + f" y {geo.name(more_eu[-1], 'es')}"
    names_en = ", ".join(geo.name(c, "en") for c in more_eu[:-1]) + f" and {geo.name(more_eu[-1], 'en')}"
    return chart(
        id="n10-nacidos-ue-fuera",
        lens="dentro", theme="demografia",
        title={"es": f"Solo en {names_es} viven más personas nacidas en otro país de la UE que fuera de ella",
               "en": f"Only in {names_en} do more residents come from another EU country than from outside the EU"},
        subtitle={"es": f"Población nacida en otro país de la UE y nacida fuera de la UE, en % de la población, {END}. UE: {fmt_es(v[('EU27', 'EU27_2020_FOR')])} % y {fmt_es(v[('EU27', 'NEU27_2020_FOR')])} %",
                  "en": f"Population born in another EU country and born outside the EU, as % of the population, {END}. EU: {v[('EU27', 'EU27_2020_FOR')]:g}% and {v[('EU27', 'NEU27_2020_FOR')]:g}%"},
        unit={"es": "% de la población", "en": "% of the population"},
        source=eurostat_source("migr_pop3ctb"),
        notes={"es": COMMON_NOTES["es"] + [
                   "Para la UE, «otro país de la UE» suma a todos los que viven en un país de la Unión distinto del suyo de nacimiento. El dato de Alemania es una estimación de Eurostat; el de Francia y el agregado de la UE son provisionales.",
                   "Eurostat ha actualizado la serie después de publicarse el tema Demografía: ya incluye a Portugal en 2025 y la parte de la UE nacida fuera de ella en 2025 es ahora del 10,6 %, no del 10,4 %."],
               "en": COMMON_NOTES["en"] + [
                   "For the EU, \"another EU country\" adds up everyone living in an EU country other than the one they were born in. Germany's figure is a Eurostat estimate; France's and the EU aggregate are provisional.",
                   "Eurostat has updated the series since the Demography theme was published: it now includes Portugal for 2025, and the EU share born outside the EU in 2025 is now 10.6%, not 10.4%."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["c_birth"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"c_birth": BIRTH}},
    )


def nacidos_ue_evolucion():
    n = _counts(YEARS)
    out = [{"geo": "EU27", "time": t, "series": cb, "value": round(n[("EU27", t, cb)] / 1e6, 1)} for cb in BIRTH for t in YEARS]
    gain = {cb: n[("EU27", END, cb)] - n[("EU27", START, cb)] for cb in BIRTH}
    gain_m = {cb: round(g / 1e6, 1) for cb, g in gain.items()}
    assert gain_m == {"EU27_2020_FOR": 0.5, "NEU27_2020_FOR": 9.9}, gain_m
    return chart(
        id="n10-nacidos-ue-evolucion",
        lens="dentro", theme="demografia",
        title={"es": f"Desde {START}, los residentes en la UE nacidos fuera de ella han aumentado en {fmt_es(gain_m['NEU27_2020_FOR'])} millones; los nacidos en otro país de la Unión, en medio millón",
               "en": f"Since {START}, EU residents born outside the EU have increased by {gain_m['NEU27_2020_FOR']:g} million; those born in another EU country, by half a million"},
        subtitle={"es": f"Residentes en la UE según dónde nacieron, en millones de personas, {START}-{END}",
                  "en": f"EU residents by place of birth, in millions of people, {START}-{END}"},
        unit={"es": "millones de personas", "en": "million people"},
        source=eurostat_source("migr_pop3ctb"),
        notes={"es": COMMON_NOTES["es"] + [
                   f"Agregado de la UE calculado por Eurostat. Es provisional y en parte estimado; de {START} a 2023 tiene ruptura de serie (marca «b» de Eurostat), porque algunos países, como Chequia, Croacia, Polonia y Portugal, cambiaron sus fuentes en {START} o 2022.",
                   f"Se empieza en {START} porque es el primer año para el que Eurostat publica el agregado de la UE en esta serie.",
                   "Los aumentos del titular se calculan con las cifras sin redondear (9,88 y 0,47 millones), por eso no coinciden exactamente con la resta de los valores del gráfico."],
               "en": COMMON_NOTES["en"] + [
                   f"EU aggregate calculated by Eurostat. It is provisional and partly estimated; from {START} to 2023 it has breaks in series (Eurostat flag \"b\"), because some countries, such as Czechia, Croatia, Poland and Portugal, changed their sources in {START} or 2022.",
                   f"The chart starts in {START} because it is the first year for which Eurostat publishes the EU aggregate in this series.",
                   "The increases in the title are calculated from unrounded figures (9.88 and 0.47 million), so they do not exactly match the difference between the values in the chart."]},
        rows=out,
        geos=geo.geo_table(["EU27"]),
        extra={"dimensions": {"series": BIRTH}},
    )


BUILDERS = [nacidos_ue_fuera, nacidos_ue_evolucion]
