"""N08. Paro juvenil: la tasa sobre los activos frente a la proporción sobre todos los jóvenes."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

YEAR = "2025"
FILTERS = dict(sex="T", age="Y15-24", time=YEAR)

MEASURES = {
    "tasa": {"es": "Sobre los jóvenes activos (tasa de paro)", "en": "Over young people in the labour force (unemployment rate)"},
    "proporcion": {"es": "Sobre todos los jóvenes (proporción de paro)", "en": "Over all young people (unemployment ratio)"},
}


def _eu(rows):
    return [r for r in rows if r["geo"] in geo.EU27 or r["geo"] == "EU27"]


def _round(rows):
    return [{**r, "value": round(r["value"], 1)} for r in rows]


def paro_dos_medidas():
    out = []
    for unit, key in (("PC_ACT", "tasa"), ("PC_POP", "proporcion")):
        rows = _round(_eu(from_eurostat(sources.eurostat("une_rt_a", unit=unit, **FILTERS), [])))
        out += [{**r, "measure": key} for r in rows]
    ratio = {r["geo"]: r["value"] for r in out if r["measure"] == "proporcion"}
    top = sorted((c for c in geo.EU27 if c in ratio), key=lambda c: -ratio[c])
    assert top[0] == "SWE" and ratio["SWE"] == 13.9 and ratio["ESP"] == 8.4 and ratio["ROU"] == 6.2, top[:3]
    return chart(
        id="n08-paro-dos-medidas",
        lens="dentro", theme="empleo",
        title={"es": "Contados sobre todos los jóvenes, en Suecia hay más parados (13,9 %) que en España (8,4 %) o Rumanía (6,2 %)",
               "en": "Counted over all young people, Sweden has more unemployed (13.9%) than Spain (8.4%) or Romania (6.2%)"},
        subtitle={"es": f"Parados de 15 a 24 años, en % de los activos de esa edad y en % de toda la población de esa edad, {YEAR}",
                  "en": f"Unemployed people aged 15-24, as % of the labour force of that age and as % of the whole population of that age, {YEAR}"},
        unit={"es": "%", "en": "%"},
        source=eurostat_source("une_rt_a"),
        notes={"es": ["Encuesta de Población Activa. Los dos indicadores tienen el mismo numerador, los jóvenes en paro. La tasa los divide entre los jóvenes activos (los que trabajan o buscan empleo); la proporción, entre todos los jóvenes de 15 a 24 años, estudien o no.",
                      "Un estudiante que busca un trabajo a tiempo parcial cuenta como parado si no lo encuentra. Un aprendiz con contrato cuenta como ocupado.",
                      "España y Francia tienen una definición que difiere en parte de la común (marca «d» de Eurostat)."],
               "en": ["Labour Force Survey. Both indicators have the same numerator, unemployed young people. The rate divides them by young people in the labour force (those who work or look for work); the ratio, by all young people aged 15 to 24, whether studying or not.",
                      "A student looking for a part-time job counts as unemployed if they do not find one. An apprentice with a contract counts as employed.",
                      "Spain and France use a definition that partly differs from the common one (Eurostat flag \"d\")."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["measure"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"measure": MEASURES}},
    )


def jovenes_activos():
    raw = sources.eurostat("lfsi_emp_a", unit="PC_POP", indic_em="ACT", **FILTERS)
    out = _round(_eu(from_eurostat(raw, [])))
    v = {r["geo"]: r["value"] for r in out}
    order = sorted((c for c in geo.EU27 if c in v), key=lambda c: v[c])
    assert order[-1] == "NLD" and order[0] == "BGR", (order[0], order[-1])
    return chart(
        id="n08-jovenes-activos",
        lens="dentro", theme="empleo",
        title={"es": f"En los Países Bajos trabaja o busca empleo el {v['NLD']:g} % de los jóvenes; en Bulgaria, el {v['BGR']:g} %".replace(".", ","),
               "en": f"In the Netherlands {v['NLD']:g}% of young people work or look for work; in Bulgaria, {v['BGR']:g}%"},
        subtitle={"es": f"Tasa de actividad de 15 a 24 años, en % de la población de esa edad, {YEAR}",
                  "en": f"Activity rate aged 15-24, as % of the population of that age, {YEAR}"},
        unit={"es": "% de la población de 15 a 24 años", "en": "% of the population aged 15-24"},
        source=eurostat_source("lfsi_emp_a"),
        notes={"es": ["Encuesta de Población Activa. Activos son los que trabajan, aunque sea unas horas a la semana, y los que buscan empleo y están disponibles para empezar. Incluye a los estudiantes que cumplen alguna de esas dos condiciones.",
                      "Los aprendices con contrato cuentan como ocupados, y por eso como activos. España y Francia tienen una definición que difiere en parte de la común (marca «d» de Eurostat)."],
               "en": ["Labour Force Survey. The labour force covers those who work, even a few hours a week, and those who are looking for work and available to start. It includes students who meet either condition.",
                      "Apprentices with a contract count as employed, and therefore as part of the labour force. Spain and France use a definition that partly differs from the common one (Eurostat flag \"d\")."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [paro_dos_medidas, jovenes_activos]
