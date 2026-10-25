"""Empleo. Mirada 1: el paro de los jóvenes frente a EE. UU. y China, y en qué edades trabaja menos gente en la UE."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source

# Último año observado: la OIT publica estimaciones modelizadas y proyecciones para años posteriores
LAST_YEAR = 2024
ILO_SOURCE = {"name": "OIT, ILOSTAT (estimaciones modelizadas)", "dataset": "DF_UNE_2EAP_SEX_AGE_RT",
              "url": "https://ilostat.ilo.org/data/", "license": "CC BY 4.0"}


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def paro_juvenil_bloques():
    rows = sources.ilo("DF_UNE_2EAP_SEX_AGE_RT", "USA+CHN+X92.A..SEX_T.AGE_YTHADULT_Y15-24", start="2000")
    out = []
    for r in rows:
        if r["FREQ"] != "A" or not r["OBS_VALUE"] or int(r["TIME_PERIOD"]) > LAST_YEAR:
            continue
        code = geo.from_iso3(r["REF_AREA"])
        if code:
            out.append({"geo": code, "time": r["TIME_PERIOD"], "value": round(float(r["OBS_VALUE"]), 1)})
    v = {(r["geo"], r["time"]): r["value"] for r in out}
    last, first = str(LAST_YEAR), "2000"
    eu, us, cn, cn0 = v[("EU27", last)], v[("USA", last)], v[("CHN", last)], v[("CHN", first)]
    peak_year = max((t for (g, t) in v if g == "EU27"), key=lambda t: v[("EU27", t)])
    assert eu > us and abs(cn - eu) < 0.5, (eu, us, cn)
    return chart(
        id="emg1-paro-juvenil",
        lens="gigantes", theme="empleo",
        title={"es": f"El paro de los jóvenes es del {fmt_es(eu)} % en la UE y del {fmt_es(us)} % en EE. UU.; en China, que partía del {fmt_es(cn0)} %, ya es igual que en la UE",
               "en": f"Youth unemployment is {eu:g}% in the EU and {us:g}% in the US; in China, which started from {cn0:g}%, it is now level with the EU"},
        subtitle={"es": f"Tasa de paro de los jóvenes de 15 a 24 años, en % de los activos de esa edad, {first}-{last}",
                  "en": f"Unemployment rate of young people aged 15 to 24, as % of the labour force of that age, {first}-{last}"},
        unit={"es": "% de los activos de 15 a 24 años", "en": "% of the labour force aged 15-24"},
        source=ILO_SOURCE,
        notes={"es": ["Estimaciones modelizadas de la Organización Internacional del Trabajo, que armonizan las encuestas de empleo de cada país para poder compararlas.",
                      f"En la UE, el máximo de la serie fue en {peak_year} ({fmt_es(v[('EU27', peak_year)])} %).",
                      "Los parados son quienes buscan empleo y están disponibles para trabajar: los jóvenes que solo estudian no cuentan como activos.",
                      "Las cifras de la OIT para la UE no coinciden exactamente con las de Eurostat del gráfico D1, que son de otro año y de otra fuente.",
                      f"La OIT publica proyecciones para años posteriores a {last}; aquí no se muestran."],
               "en": ["Modelled estimates by the International Labour Organization, which harmonise each country's labour surveys so they can be compared.",
                      f"In the EU, the series peaked in {peak_year} ({v[('EU27', peak_year)]:g}%).",
                      "The unemployed are those looking for work and available to start: young people who only study do not count as part of the labour force.",
                      "The ILO figures for the EU do not exactly match Eurostat's in chart D1, which are for another year and from another source.",
                      f"The ILO publishes projections beyond {last}; they are not shown here."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


AGES = {
    "Y15-24": {"es": "De 15 a 24 años", "en": "Aged 15-24"},
    "Y25-54": {"es": "De 25 a 54 años", "en": "Aged 25-54"},
    "Y55-64": {"es": "De 55 a 64 años", "en": "Aged 55-64"},
}
ILO_AGES = {"Y15-24": "AGE_AGGREGATE_Y15-24", "Y25-54": "AGE_AGGREGATE_Y25-54", "Y55-64": "AGE_AGGREGATE_Y55-64"}


def empleo_edades():
    year = str(LAST_YEAR)
    eu = {r["age"]: r["value"] for r in sources.eurostat("lfsi_emp_a", geo="EU27_2020", unit="PC_POP", indic_em="EMP_LFS",
                                                        sex="T", age=list(AGES), time=year)}
    ilo = sources.ilo("DF_EMP_DWAP_SEX_AGE_RT", "USA.A..SEX_T.", start=year)
    us = {}
    for r in ilo:
        for a, code in ILO_AGES.items():
            if r["AGE"] == code and r["TIME_PERIOD"] == year and r["SOURCE"].startswith("LFS"):
                us[a] = round(float(r["OBS_VALUE"]), 1)
    assert set(eu) == set(us) == set(AGES), (eu, us)
    out = [{"geo": a, "time": year, "bloc": b, "value": d[a]} for a in AGES for b, d in (("EU27", eu), ("USA", us))]
    gap_young = us["Y15-24"] - eu["Y15-24"]
    assert gap_young > 10 and eu["Y25-54"] > us["Y25-54"] and eu["Y55-64"] > us["Y55-64"]
    return chart(
        id="emg2-empleo-edades",
        lens="gigantes", theme="empleo",
        title={"es": f"Entre los 25 y los 54 años trabaja en la UE más gente que en EE. UU.; entre los jóvenes, {round(gap_young)} puntos menos",
               "en": f"Between the ages of 25 and 54, more people work in the EU than in the US; among the young, {round(gap_young)} points fewer"},
        subtitle={"es": f"Tasa de empleo por edad, en % de la población de cada grupo, {year}",
                  "en": f"Employment rate by age, as % of the population in each group, {year}"},
        unit={"es": "% de la población de cada edad", "en": "% of the population of each age"},
        source={**eurostat_source("lfsi_emp_a"),
                "also": [{"name": "OIT, ILOSTAT (encuesta de población de EE. UU., CPS)", "dataset": "DF_EMP_DWAP_SEX_AGE_RT",
                          "url": "https://ilostat.ilo.org/data/", "license": "CC BY 4.0"}]},
        notes={"es": ["Tasa de empleo: ocupados de cada edad entre toda la población de esa edad, trabajen o no.",
                      "UE: Encuesta de Población Activa de Eurostat. EE. UU.: encuesta de población (Current Population Survey) publicada por la OIT, que en el grupo más joven empieza a los 16 años.",
                      "China no publica la tasa de empleo por edades con la misma periodicidad, por eso no aparece.",
                      "En los dos bloques, un joven que estudia y trabaja a la vez cuenta como ocupado."],
               "en": ["Employment rate: people in work at each age as a share of the whole population of that age, whether they work or not.",
                      "EU: Eurostat Labour Force Survey. US: Current Population Survey published by the ILO, whose youngest group starts at 16.",
                      "China does not publish employment rates by age on the same basis, so it is not shown.",
                      "In both blocs, a young person who studies and works at the same time counts as employed."]},
        rows=out,
        geos={a: {**lab, "eu": False, "aggregate": False} for a, lab in AGES.items()},
        extra={"dimensions": {"bloc": {"EU27": {"es": "UE", "en": "EU"}, "USA": {"es": "EE. UU.", "en": "US"}}}},
    )


BUILDERS = [paro_juvenil_bloques, empleo_edades]
