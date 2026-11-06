"""Educación. Mirada 3: abandono temprano y estudiantes de carreras CTIM en cada país."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

ELET_BASE, ELET_YEAR = "2015", "2025"
ELET_TARGET = 8


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def names(codes: list[str], lang: str) -> str:
    sep = " y " if lang == "es" else " and "
    ns = [geo.name(c, lang) for c in codes]
    return ns[0] if len(ns) == 1 else ", ".join(ns[:-1]) + sep + ns[-1]


def abandono_paises():
    raw = sources.eurostat("edat_lfse_14", sex="T", age="Y18-24", unit="PC", wstatus="POP", time=[ELET_BASE, ELET_YEAR])
    out = [r for r in from_eurostat(raw, []) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    flags = {(r["geo"], r["time"]): r.get("flag", "") for r in out}
    for r in out:
        r.pop("flag", None)
    v = {(r["geo"], r["time"]): r["value"] for r in out}
    countries = [c for c in geo.EU27 if (c, ELET_YEAR) in v and (c, ELET_BASE) in v]
    down = [c for c in countries if v[(c, ELET_YEAR)] < v[(c, ELET_BASE)]]
    up = sorted((c for c in countries if v[(c, ELET_YEAR)] > v[(c, ELET_BASE)]), key=lambda c: geo.name(c, "es"))
    drop = {c: round(v[(c, ELET_BASE)] - v[(c, ELET_YEAR)], 1) for c in countries}
    big = sorted(down, key=lambda c: -drop[c])[:3]
    below = [c for c in countries if v[(c, ELET_YEAR)] < ELET_TARGET]
    unreliable = [c for c in countries if "u" in flags.get((c, ELET_YEAR), "")]
    assert len(countries) == 27 and len(down) == 20 and set(big) == {"MLT", "PRT", "ESP"} and all(drop[c] > 7 for c in big), (down, big)
    big_es = names(sorted(big, key=lambda c: -drop[c]), "es")
    big_en = names(sorted(big, key=lambda c: -drop[c]), "en")
    return chart(
        id="edd1-abandono-paises",
        lens="dentro", theme="educacion",
        title={"es": f"El abandono temprano de los estudios ha bajado desde {ELET_BASE} en {len(down)} de los 27 países; en {big_es}, más de 7 puntos",
               "en": f"Early school leaving has fallen since {ELET_BASE} in {len(down)} of the 27 countries; in {big_en}, by more than 7 points"},
        subtitle={"es": f"Personas de 18 a 24 años que como mucho terminaron la secundaria obligatoria y no estudian ni se forman, en %, {ELET_BASE} y {ELET_YEAR}. UE: {fmt_es(v[('EU27', ELET_YEAR)])} %",
                  "en": f"People aged 18 to 24 with at most lower secondary education who are not in education or training, in %, {ELET_BASE} and {ELET_YEAR}. EU: {v[('EU27', ELET_YEAR)]:g}%"},
        unit={"es": "% de las personas de 18 a 24 años", "en": "% of people aged 18 to 24"},
        source=eurostat_source("edat_lfse_14"),
        notes={"es": [f"Es el indicador del objetivo europeo para 2030, que la UE ha rebajado al {ELET_TARGET} %. En {ELET_YEAR}, {len(below)} países están por debajo. Ha subido en {names(up, 'es')}.",
                      "Encuesta de Población Activa de la UE. Cuenta a quien no tiene un título de bachillerato o de FP de grado medio y no ha seguido ninguna formación en las cuatro semanas anteriores a la encuesta, aunque trabaje.",
                      f"Eurostat marca como poco fiables por el tamaño de la muestra los datos de {ELET_YEAR} de {names(unreliable, 'es')}."],
               "en": [f"This is the indicator for the EU's 2030 target, which has been lowered to {ELET_TARGET}%. In {ELET_YEAR}, {len(below)} countries are below it. It has risen in {names(sorted(up, key=lambda c: geo.name(c, 'en')), 'en')}.",
                      "EU Labour Force Survey. It counts people without an upper secondary or vocational qualification who have not taken part in any education or training in the four weeks before the survey, even if they work.",
                      f"Eurostat flags the {ELET_YEAR} figures for {names(unreliable, 'en')} as unreliable because of sample size."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


STEM_YEAR = "2024"
STEM_FIELDS = ["F05", "F06", "F07"]
STEM_TARGET, WOMEN_TARGET = 32, 40


def ctim_paises():
    raw = sources.eurostat("educ_uoe_enrt03", unit="NR", isced11="ED5-8", iscedf13=["TOTAL", *STEM_FIELDS], sex=["T", "F"], time=["2023", STEM_YEAR])
    v = {(r["geo"], r["time"], r["iscedf13"], r["sex"]): r["value"] for r in from_eurostat(raw, ["iscedf13", "sex"])}
    out, women = [], {}
    for g in ["EU27", *geo.EU27]:
        try:
            stem = sum(v[(g, STEM_YEAR, f, "T")] for f in STEM_FIELDS)
            stem_f = sum(v[(g, STEM_YEAR, f, "F")] for f in STEM_FIELDS)
            total = v[(g, STEM_YEAR, "TOTAL", "T")]
        except KeyError:
            continue
        out.append({"geo": g, "time": STEM_YEAR, "value": round(100 * stem / total, 1)})
        women[g] = round(100 * stem_f / stem, 1)
    s = {r["geo"]: r["value"] for r in out}
    countries = [c for c in geo.EU27 if c in s]
    above = sorted((c for c in countries if s[c] >= STEM_TARGET), key=lambda c: -s[c])
    w_top = max(countries, key=women.get)
    ie_eng = (int(v[("IRL", "2023", "F07", "T")]), int(v[("IRL", STEM_YEAR, "F07", "T")]))
    assert len(countries) == 27 and s["EU27"] < STEM_TARGET and max(women.values()) < WOMEN_TARGET and w_top == "SWE", (s["EU27"], w_top)
    assert set(above) == {"IRL", "FIN", "DEU", "GRC"} and ie_eng[1] > 2 * ie_eng[0], (above, ie_eng)
    def miles_es(n: int) -> str:
        return f"{n:,}".replace(",", ".")
    return chart(
        id="edd2-ctim-paises",
        lens="dentro", theme="educacion",
        title={"es": f"El {fmt_es(s['EU27'])} % de los universitarios de la UE estudia una carrera CTIM, frente al {STEM_TARGET} % fijado para 2030; las mujeres son el {fmt_es(women['EU27'])} % y ningún país llega a dos de cada cinco",
               "en": f"{s['EU27']:g}% of university students in the EU are enrolled in STEM, against the {STEM_TARGET}% set for 2030; women make up {women['EU27']:g}% and no country reaches two in five"},
        subtitle={"es": f"Estudiantes de educación terciaria en ciencias, matemáticas, informática e ingenierías, en % del total de estudiantes terciarios, {STEM_YEAR}",
                  "en": f"Tertiary students in science, mathematics, ICT and engineering, as % of all tertiary students, {STEM_YEAR}"},
        unit={"es": "% de los estudiantes terciarios", "en": "% of tertiary students"},
        source=eurostat_source("educ_uoe_enrt03"),
        notes={"es": [f"CTIM: ciencias naturales, matemáticas y estadística; tecnologías de la información y las comunicaciones; ingeniería, industria y construcción (campos 05, 06 y 07 de la clasificación ISCED-F 2013), como en el objetivo europeo. Incluye ciclos cortos, grado, máster y doctorado.",
                      f"El objetivo pide también que al menos dos de cada cinco estudiantes CTIM ({WOMEN_TARGET} %) sean mujeres. El país más cerca es {geo.name(w_top, 'es')}, con el {fmt_es(women[w_top])} %.",
                      f"En Irlanda, los estudiantes de ingeniería, industria y construcción pasan de {miles_es(ie_eng[0])} en 2023 a {miles_es(ie_eng[1])} en {STEM_YEAR} sin que Eurostat marque una ruptura de serie: su posición en el ranking puede deberse a un cambio de cobertura."],
               "en": [f"STEM: natural sciences, mathematics and statistics; information and communication technologies; engineering, manufacturing and construction (fields 05, 06 and 07 of the ISCED-F 2013 classification), as in the EU target. It includes short-cycle, bachelor's, master's and doctoral programmes.",
                      f"The target also asks for at least two in five STEM students ({WOMEN_TARGET}%) to be women. The closest country is {geo.name(w_top, 'en')}, at {women[w_top]:g}%.",
                      f"In Ireland, students in engineering, manufacturing and construction go from {ie_eng[0]:,} in 2023 to {ie_eng[1]:,} in {STEM_YEAR} without Eurostat flagging a break in the series: its position in the ranking may reflect a change in coverage."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"targets": [{"value": STEM_TARGET, "label": {"es": f"Objetivo 2030: {STEM_TARGET} %", "en": f"2030 target: {STEM_TARGET}%"}}],
               "women_share": women},
    )


BUILDERS = [abandono_paises, ctim_paises]
