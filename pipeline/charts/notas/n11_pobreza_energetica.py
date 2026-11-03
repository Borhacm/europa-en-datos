"""N11. Pobreza energética: personas que no pueden mantener su casa a una temperatura adecuada."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

START, END = "2021", "2025"

POVERTY = {
    "A_60": {"es": "Por encima del umbral de pobreza", "en": "Above the poverty threshold"},
    "B_60": {"es": "En riesgo de pobreza", "en": "At risk of poverty"},
}

COMMON_NOTES = {
    "es": ["Encuesta de condiciones de vida (EU-SILC). Es lo que declara cada hogar al responder si puede permitirse mantener su vivienda a una temperatura adecuada: no se miden temperaturas ni gasto en energía.",
           "Lo que cada hogar considera «adecuado» depende del clima, de la vivienda y de las costumbres, así que las diferencias entre países no solo reflejan dinero."],
    "en": ["EU Statistics on Income and Living Conditions (EU-SILC). It is what each household reports when asked whether it can afford to keep its home adequately warm: no temperatures or energy spending are measured.",
           "What each household considers \"adequate\" depends on climate, housing and habits, so differences between countries do not only reflect money."],
}


def _eu(rows):
    return [r for r in rows if r["geo"] in geo.EU27 or r["geo"] == "EU27"]


def frio_cambio():
    raw = sources.eurostat("ilc_mdes01", hhcomp="TOTAL", rskpovth="TOTAL", unit="PC", time=[START, END])
    out = _eu(from_eurostat(raw, []))
    v = {(r["geo"], r["time"]): r["value"] for r in out}
    up = [c for c in geo.EU27 if v[(c, END)] > v[(c, START)]]
    down = [c for c in geo.EU27 if v[(c, END)] < v[(c, START)]]
    assert len(up) == 19 and len(down) == 7, (len(up), len(down))
    return chart(
        id="n11-frio-cambio",
        lens="dentro", theme="energia",
        title={"es": f"No poder calentar la casa es más frecuente que en {START} en {len(up)} países de la UE y menos en {len(down)}",
               "en": f"Being unable to keep the home warm is more common than in {START} in {len(up)} EU countries and less common in {len(down)}"},
        subtitle={"es": f"Población que no puede permitirse mantener su vivienda a una temperatura adecuada, en % del total, {START} y {END}",
                  "en": f"Population unable to afford to keep their home adequately warm, % of the total, {START} and {END}"},
        unit={"es": "% de la población", "en": "% of the population"},
        source=eurostat_source("ilc_mdes01"),
        notes={"es": COMMON_NOTES["es"] + [
                   "Francia tiene una ruptura de serie en 2022 (marca «b» de Eurostat): parte de su subida entre 2021 y 2025 puede deberse al cambio de la encuesta. Luxemburgo también tiene ruptura en 2021 y 2025, y Portugal en 2021. El dato de Lituania de 2025 es provisional.",
                   "El año es el de la encuesta. Todos los hogares, sin distinguir su composición."],
               "en": COMMON_NOTES["en"] + [
                   "France has a break in series in 2022 (Eurostat flag \"b\"): part of its increase between 2021 and 2025 may be due to the change in the survey. Luxembourg also has breaks in 2021 and 2025, and Portugal in 2021. Lithuania's 2025 figure is provisional.",
                   "The year is the survey year. All households, regardless of their composition."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def frio_pobreza():
    raw = sources.eurostat("ilc_mdes01", hhcomp="TOTAL", rskpovth=list(POVERTY), unit="PC", time=END)
    out = _eu(from_eurostat(raw, ["rskpovth"]))
    v = {(r["geo"], r["rskpovth"]): r["value"] for r in out}
    assert v[("EU27", "B_60")] == 19.6 and v[("EU27", "A_60")] == 6.7, v[("EU27", "B_60")]
    top = max(geo.EU27, key=lambda c: v[(c, "B_60")])
    assert top == "GRC" and v[("GRC", "B_60")] == 36.1, top
    return chart(
        id="n11-frio-pobreza",
        lens="dentro", theme="energia",
        title={"es": f"Entre las personas en riesgo de pobreza, el {v[('EU27', 'B_60')]:g} % no puede calentar su casa; entre el resto, el {v[('EU27', 'A_60')]:g} %".replace(".", ","),
               "en": f"Among people at risk of poverty, {v[('EU27', 'B_60')]:g}% cannot keep their home warm; among the rest, {v[('EU27', 'A_60')]:g}%"},
        subtitle={"es": f"Población que no puede permitirse mantener su vivienda a una temperatura adecuada, según esté o no en riesgo de pobreza, en %, {END}",
                  "en": f"Population unable to afford to keep their home adequately warm, by whether they are at risk of poverty, %, {END}"},
        unit={"es": "% de cada grupo", "en": "% of each group"},
        source=eurostat_source("ilc_mdes01"),
        notes={"es": COMMON_NOTES["es"] + [
                   "En riesgo de pobreza: personas con una renta disponible equivalente inferior al 60 % de la mediana de su país. El umbral es nacional: un hogar en riesgo de pobreza en Luxemburgo tiene más renta que uno en Bulgaria.",
                   "La renta de la encuesta es la del año anterior. El dato de Lituania es provisional y el de Luxemburgo tiene ruptura de serie."],
               "en": COMMON_NOTES["en"] + [
                   "At risk of poverty: people with an equivalised disposable income below 60% of their country's median. The threshold is national: a household at risk of poverty in Luxembourg has more income than one in Bulgaria.",
                   "Survey income refers to the previous year. Lithuania's figure is provisional and Luxembourg's has a break in series."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["rskpovth"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"rskpovth": POVERTY}},
    )


BUILDERS = [frio_cambio, frio_pobreza]
