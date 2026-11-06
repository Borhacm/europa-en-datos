"""Educación. Mirada 1: matrícula universitaria e investigadores de la UE, EE. UU. y China."""

from lib import geo
from lib.output import chart

from ..common import worldbank_rows, worldbank_source

FIRST, LAST = 2000, 2024
BLOCS = ["EU27", "USA", "CHN"]


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def fmt_int_es(x: float) -> str:
    return f"{x:,.0f}".replace(",", ".")


def bloc_rows(indicator: str, digits: int) -> list[dict]:
    rows = [r for r in worldbank_rows(indicator, FIRST, LAST) if r["geo"] in BLOCS]
    for r in rows:
        r["value"] = round(r["value"], digits)
    return rows


def last_year(v: dict, g: str) -> str:
    return max(t for (gg, t) in v if gg == g)


def matricula_bloques():
    rows = bloc_rows("SE.TER.ENRR", 1)
    v = {(r["geo"], r["time"]): r["value"] for r in rows}
    ly = {g: last_year(v, g) for g in BLOCS}
    eu, us, cn = (v[(g, ly[g])] for g in BLOCS)
    cn0 = v[("CHN", str(FIRST))]
    # EE. UU. no tiene serie completa: años con dato
    us_years = sorted(t for (g, t) in v if g == "USA")
    assert ly["EU27"] == ly["CHN"] == str(LAST) and ly["USA"] == "2022", ly
    assert cn0 < 10 and cn > 10 * cn0 and abs(eu - us) < 1 and cn < eu, (eu, us, cn, cn0)
    return chart(
        id="edg1-matricula-superior",
        lens="gigantes", theme="educacion",
        title={"es": f"En China, la matrícula en estudios superiores ha pasado del {fmt_es(cn0)} % en {FIRST} al {fmt_es(cn)} % y se acerca a la de la UE ({fmt_es(eu)} %) y EE. UU. ({fmt_es(us)} %)",
               "en": f"In China, enrolment in higher education has gone from {cn0:g}% in {FIRST} to {cn:g}%, close to the EU ({eu:g}%) and the US ({us:g}%)"},
        subtitle={"es": f"Tasa bruta de matrícula en educación terciaria, en % de la población en edad de cursarla, {FIRST}-{LAST}",
                  "en": f"Gross enrolment ratio in tertiary education, as % of the population of tertiary age, {FIRST}-{LAST}"},
        unit={"es": "% del grupo de edad", "en": "% of the age group"},
        source=worldbank_source("SE.TER.ENRR", "Matrícula en educación terciaria (% bruto), datos del Instituto de Estadística de la UNESCO"),
        notes={"es": ["Estudiantes matriculados en educación terciaria (ciclos cortos, grado, máster y doctorado), de cualquier edad, divididos por la población de los cinco años siguientes a la edad de terminar la secundaria. Por eso se llama tasa bruta: cuenta también a los mayores y no es la parte de los jóvenes que estudia.",
                      f"Para EE. UU., la UNESCO solo publica algunos años; el último es {ly['USA']}. En la UE, son los 27 países actuales en todos los años.",
                      "La tasa no dice nada de la calidad ni de cuántos terminan los estudios."],
               "en": ["Students enrolled in tertiary education (short cycle, bachelor's, master's and doctoral), of any age, divided by the population in the five years after the age of finishing secondary school. That is why it is called a gross ratio: it also counts older students and is not the share of young people who study.",
                      f"For the US, UNESCO only publishes some years; the latest is {ly['USA']}. For the EU, the figures cover today's 27 countries in every year.",
                      "The ratio says nothing about quality or about how many finish their studies."]},
        rows=rows,
        geos=geo.geo_table(r["geo"] for r in rows),
    )


def investigadores_bloques():
    rows = bloc_rows("SP.POP.SCIE.RD.P6", 0)
    v = {(r["geo"], r["time"]): r["value"] for r in rows}
    ly = {g: last_year(v, g) for g in BLOCS}
    eu, us, cn = (v[(g, ly[g])] for g in BLOCS)
    eu0, us0, cn0 = (v[(g, str(FIRST))] for g in BLOCS)
    # Número total de investigadores con la población del mismo año
    pop = {(r["geo"], r["time"]): r["value"] for r in worldbank_rows("SP.POP.TOTL", 2020, LAST) if r["geo"] in BLOCS}
    tot = {g: round(v[(g, ly[g])] * pop[(g, ly[g])] / 1e6 / 1e6, 1) for g in BLOCS}
    assert ly == {"EU27": "2023", "USA": "2022", "CHN": "2023"}, ly
    assert us > eu > 2 * cn and eu > 2 * eu0 * 0.99 and tot["CHN"] > tot["EU27"] > tot["USA"], (eu, us, cn, tot)
    return chart(
        id="edg2-investigadores",
        lens="gigantes", theme="educacion",
        title={"es": f"La UE tiene {fmt_int_es(eu)} investigadores por millón de habitantes, cerca de EE. UU. ({fmt_int_es(us)}); China, {fmt_int_es(cn)}, aunque en número total ya tiene más",
               "en": f"The EU has {eu:,.0f} researchers per million people, close to the US ({us:,.0f}); China has {cn:,.0f}, although it now has more in total"},
        subtitle={"es": f"Investigadores en I+D por millón de habitantes, {FIRST}-{ly['EU27']}",
                  "en": f"Researchers in R&D per million people, {FIRST}-{ly['EU27']}"},
        unit={"es": "por millón de habitantes", "en": "per million people"},
        source=worldbank_source("SP.POP.SCIE.RD.P6", "Investigadores en I+D (por millón de personas), datos del Instituto de Estadística de la UNESCO"),
        notes={"es": ["Personas que se dedican a crear conocimiento, productos, procesos o métodos nuevos, en empresas, universidades y administraciones, contadas en equivalencia a jornada completa.",
                      f"Último año con dato: {ly['EU27']} para la UE y China y {ly['USA']} para EE. UU.",
                      f"Con la población del Banco Mundial (SP.POP.TOTL), equivale a unos {fmt_es(tot['CHN'])} millones de investigadores en China, {fmt_es(tot['EU27'])} millones en la UE y {fmt_es(tot['USA'])} millones en EE. UU.",
                      "Las definiciones siguen el Manual de Frascati de la OCDE, pero cada país aplica sus propias encuestas, así que las cifras son aproximadas."],
               "en": ["People engaged in creating new knowledge, products, processes or methods, in businesses, universities and government, counted in full-time equivalents.",
                      f"Latest year with data: {ly['EU27']} for the EU and China and {ly['USA']} for the US.",
                      f"With World Bank population figures (SP.POP.TOTL), that is about {tot['CHN']:g} million researchers in China, {tot['EU27']:g} million in the EU and {tot['USA']:g} million in the US.",
                      "Definitions follow the OECD Frascati Manual, but each country runs its own surveys, so the figures are approximate."]},
        rows=rows,
        geos=geo.geo_table(r["geo"] for r in rows),
    )


BUILDERS = [matricula_bloques, investigadores_bloques]
