"""N12. Universitarios de 25 a 34 años, país por país, frente al objetivo europeo para 2030."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

YEAR = "2025"
TARGET, OLD_TARGET = 47, 45
FILTERS = dict(isced11="ED5-8", age="Y25-34", unit="PC", time=YEAR)

SEX = {
    "M": {"es": "Hombres", "en": "Men"},
    "F": {"es": "Mujeres", "en": "Women"},
}

COMMON_NOTES = {
    "es": ["Encuesta de Población Activa de la UE. Estudios superiores: niveles 5 a 8 de la clasificación ISCED 2011 (ciclos cortos de educación superior, como la FP de grado superior en España, grado, máster y doctorado).",
           "El objetivo es para la media de la UE, no para cada país: la resolución del Consejo de 2026 lo subió del 45 % al 47 % de las personas de 25 a 34 años para 2030. La educación es competencia de cada Estado.",
           "Cuenta dónde viven las personas, no dónde estudiaron: un país que recibe titulados de otros sube y uno que los pierde baja."],
    "en": ["EU Labour Force Survey. Tertiary education: ISCED 2011 levels 5 to 8 (short-cycle tertiary, such as higher vocational training in Spain, bachelor's, master's and doctorate).",
           "The target applies to the EU average, not to each country: the Council's 2026 resolution raised it from 45% to 47% of 25 to 34-year-olds by 2030. Education is a national competence.",
           "It counts where people live, not where they studied: a country that attracts graduates from elsewhere rises and one that loses them falls."],
}


def _eu(rows):
    return [r for r in rows if r["geo"] in geo.EU27 or r["geo"] == "EU27"]


def universitarios_paises():
    out = _eu(from_eurostat(sources.eurostat("edat_lfse_03", sex="T", **FILTERS), []))
    v = {r["geo"]: r["value"] for r in out}
    above = [c for c in geo.EU27 if v[c] >= TARGET]
    low = min(geo.EU27, key=lambda c: v[c])
    assert len(v) == 28 and len(above) == 11 and low == "ROU" and v["ROU"] == 23.0 and v["EU27"] == 44.8, (len(above), low)
    return chart(
        id="n12-universitarios-paises",
        lens="dentro", theme="educacion",
        title={"es": f"{len(above)} de los 27 países superan ya el {TARGET} % de personas de 25 a 34 años con estudios superiores que la UE se ha fijado para 2030; Rumanía, con el 23 %, no llega a la mitad",
               "en": f"{len(above)} of the 27 countries already exceed the {TARGET}% of 25 to 34-year-olds with tertiary education the EU has set for 2030; Romania, at 23%, is below half of it"},
        subtitle={"es": f"Personas de 25 a 34 años con estudios superiores, en % de la población de esa edad, {YEAR}. UE: {str(v['EU27']).replace('.', ',')} %",
                  "en": f"People aged 25 to 34 with tertiary education, % of the population of that age, {YEAR}. EU: {v['EU27']:g}%"},
        unit={"es": "% de la población de 25 a 34 años", "en": "% of the population aged 25-34"},
        source=eurostat_source("edat_lfse_03"),
        notes={"es": COMMON_NOTES["es"] + [
                   "Hay una ruptura de serie en 2021 en casi todos los países por el nuevo reglamento de la encuesta: por eso esta nota no compara con años anteriores."],
               "en": COMMON_NOTES["en"] + [
                   "There is a break in series in 2021 in almost every country because of the survey's new regulation: that is why this note does not compare with earlier years."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"targets": [
            {"value": OLD_TARGET, "label": {"es": f"Objetivo de 2021: {OLD_TARGET} %", "en": f"2021 target: {OLD_TARGET}%"}},
            {"value": TARGET, "label": {"es": f"Objetivo 2030: {TARGET} %", "en": f"2030 target: {TARGET}%"}},
        ]},
    )


def universitarios_sexo():
    out = _eu(from_eurostat(sources.eurostat("edat_lfse_03", sex=list(SEX), **FILTERS), ["sex"]))
    v = {(r["geo"], r["sex"]): r["value"] for r in out}
    assert all(v[(c, "F")] > v[(c, "M")] for c in geo.EU27)
    assert v[("EU27", "F")] == 50.5 and v[("EU27", "M")] == 39.3, (v[("EU27", "F")], v[("EU27", "M")])
    return chart(
        id="n12-universitarios-sexo",
        lens="dentro", theme="educacion",
        title={"es": f"En la UE, el {v[('EU27', 'F')]:g} % de las mujeres de 25 a 34 años tiene estudios superiores, frente al {v[('EU27', 'M')]:g} % de los hombres; ellas van por delante en los 27 países".replace(".", ","),
               "en": f"In the EU, {v[('EU27', 'F')]:g}% of women aged 25 to 34 have tertiary education, against {v[('EU27', 'M')]:g}% of men; women lead in all 27 countries"},
        subtitle={"es": f"Personas de 25 a 34 años con estudios superiores, por sexo, en % de la población de esa edad y sexo, {YEAR}",
                  "en": f"People aged 25 to 34 with tertiary education, by sex, % of the population of that age and sex, {YEAR}"},
        unit={"es": "% de cada sexo", "en": "% of each sex"},
        source=eurostat_source("edat_lfse_03"),
        notes={"es": COMMON_NOTES["es"][:1] + [
                   f"El objetivo europeo del {TARGET} % es para hombres y mujeres juntos; no hay objetivo por sexo."],
               "en": COMMON_NOTES["en"][:1] + [
                   f"The EU's {TARGET}% target is for men and women together; there is no target by sex."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["sex"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"sex": SEX}},
    )


BUILDERS = [universitarios_paises, universitarios_sexo]
