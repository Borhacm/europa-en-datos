"""Empleo. Mirada 2: el objetivo de empleo de la UE para 2030 y por qué hay tantos contratos temporales."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

YEAR = "2025"
TARGET = 78
PILLAR = {"name": "Comisión Europea: Plan de Acción del Pilar Europeo de Derechos Sociales (objetivos para 2030)",
          "url": "https://ec.europa.eu/social/main.jsp?catId=1607&langId=es"}


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def objetivo_empleo():
    raw = sources.eurostat("lfsi_emp_a", unit="PC_POP", indic_em="EMP_LFS", sex="T", age="Y20-64", time=YEAR)
    out = [r for r in from_eurostat(raw, []) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    for r in out:
        r["value"] = round(r["value"], 1)
    v = {r["geo"]: r["value"] for r in out}
    ranked = sorted(geo.EU27, key=lambda c: v[c])
    reached = [c for c in geo.EU27 if v[c] >= TARGET]
    low = ranked[0]
    assert len(v) == 28 and v["EU27"] < TARGET
    return chart(
        id="eme1-objetivo-empleo",
        lens="elige", theme="empleo",
        title={"es": f"{len(reached)} de los 27 países ya emplean al menos al {TARGET} % de su población de 20 a 64 años, el objetivo de la UE para 2030; {geo.name(low, 'es')}, al {fmt_es(v[low])} %",
               "en": f"{len(reached)} of the 27 countries already employ at least {TARGET}% of their population aged 20-64, the EU's 2030 target; {geo.name(low, 'en')}, {v[low]:g}%"},
        subtitle={"es": f"Tasa de empleo de 20 a 64 años, en % de la población de esa edad, {YEAR}. UE: {fmt_es(v['EU27'])} %",
                  "en": f"Employment rate aged 20-64, as % of the population of that age, {YEAR}. EU: {v['EU27']:g}%"},
        unit={"es": "% de la población de 20 a 64 años", "en": "% of the population aged 20-64"},
        source={**eurostat_source("lfsi_emp_a"), "also": [PILLAR]},
        notes={"es": [f"La línea marca el objetivo del {TARGET} % para el conjunto de la UE. Cada país fijó además su propio objetivo nacional, más alto o más bajo según su punto de partida.",
                      "Encuesta de Población Activa. Ocupado es quien trabajó al menos una hora la semana de referencia, por cuenta propia o ajena."],
               "en": [f"The line marks the {TARGET}% target for the EU as a whole. Each country also set its own national target, higher or lower depending on where it started.",
                      "Labour Force Survey. Employed means having worked at least one hour in the reference week, as an employee or self-employed."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"targets": [{"value": TARGET, "label": {"es": f"Objetivo 2030: {TARGET} %", "en": f"2030 target: {TARGET}%"}}]},
    )


REASONS = {
    "NF_PJOB": {"es": "No encontró un empleo fijo", "en": "Could not find a permanent job"},
    "JOB_TCTR": {"es": "Solo había contrato temporal", "en": "Only a temporary contract"},
    "EDUC_TNG": {"es": "Está estudiando o formándose", "en": "In education or training"},
    "PROB": {"es": "Periodo de prueba", "en": "Probation period"},
    "NW_PJOB": {"es": "No quiere un empleo fijo", "en": "Does not want a permanent job"},
    "OTH": {"es": "Otro motivo", "en": "Other reason"},
}


def motivos_temporales():
    raw = sources.eurostat("lfsa_etgar", unit="PC_SAL_TEMP", sex="T", age="Y15-64", reason=list(REASONS), time=YEAR)
    out = [r for r in from_eurostat(raw, ["reason"]) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    for r in out:
        r["value"] = round(r["value"], 1)
    v = {(r["geo"], r["reason"]): r["value"] for r in out}
    share = {r["geo"]: round(r["value"], 1) for r in from_eurostat(
        sources.eurostat("lfsa_etgar", unit="PC_SAL", sex="T", age="Y15-64", reason="TOTAL", time=YEAR), [])}
    nf, job = v[("EU27", "NF_PJOB")], v[("EU27", "JOB_TCTR")]
    involuntary = round(nf + job, 1)
    assert 48 < involuntary < 52 and v[("DEU", "EDUC_TNG")] > 35
    return chart(
        id="eme2-motivos-temporales",
        lens="elige", theme="empleo",
        title={"es": f"La mitad de los temporales de la UE lo son porque no encontraron un empleo fijo o porque el puesto solo se ofrecía así; en Alemania, el {round(v[('DEU', 'EDUC_TNG')])} % se está formando",
               "en": f"Half of the EU's temporary employees are temporary because they could not find a permanent job or the job was only offered that way; in Germany, {round(v[('DEU', 'EDUC_TNG')])}% are in training"},
        subtitle={"es": f"Motivo principal de tener un contrato temporal, en % de los asalariados temporales de 15 a 64 años, {YEAR}",
                  "en": f"Main reason for having a temporary contract, as % of temporary employees aged 15-64, {YEAR}"},
        unit={"es": "% de los asalariados temporales", "en": "% of temporary employees"},
        source=eurostat_source("lfsa_etgar"),
        notes={"es": [f"En la UE, el {fmt_es(share['EU27'])} % de los asalariados de 15 a 64 años tiene un contrato temporal; en España, el {fmt_es(share['ESP'])} %, y en los Países Bajos, el {fmt_es(share['NLD'])} %.",
                      "Lo responde el propio trabajador en la Encuesta de Población Activa. Los porcentajes no suman 100 porque faltan quienes no contestan.",
                      "«Está estudiando o formándose» incluye los contratos de aprendizaje y de prácticas."],
               "en": [f"In the EU, {share['EU27']:g}% of employees aged 15-64 are on a temporary contract; in Spain {share['ESP']:g}%, and in the Netherlands {share['NLD']:g}%.",
                      "The answer is given by the worker in the Labour Force Survey. The percentages do not add up to 100 because non-responses are left out.",
                      "«In education or training» includes apprenticeship and traineeship contracts."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["reason"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"reason": REASONS}},
    )


BUILDERS = [objetivo_empleo, motivos_temporales]
