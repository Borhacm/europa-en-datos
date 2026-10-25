"""Empleo. Mirada 3: el paro de los jóvenes en cada país y la edad a la que se van de casa."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

YEAR = "2025"
BASE = "2015"


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def paro_juvenil_paises():
    raw = sources.eurostat("une_rt_a", unit="PC_ACT", sex="T", age="Y15-24", time=YEAR)
    out = [r for r in from_eurostat(raw, []) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    for r in out:
        r["value"] = round(r["value"], 1)
    v = {r["geo"]: r["value"] for r in out}
    countries = sorted((c for c in geo.EU27 if c in v), key=lambda c: v[c])
    missing = [geo.name(c, "es") for c in geo.EU27 if c not in v]
    missing_en = [geo.name(c, "en") for c in geo.EU27 if c not in v]
    low, top, second = countries[0], countries[-1], countries[-2]
    assert top == "ROU" and second == "ESP" and low == "DEU", (top, second, low)
    return chart(
        id="emd1-paro-juvenil-paises",
        lens="dentro", theme="empleo",
        title={"es": f"El paro de los jóvenes va del {fmt_es(v[low])} % de {geo.name(low, 'es')} al {fmt_es(v[top])} % de {geo.name(top, 'es')} y el {fmt_es(v[second])} % de {geo.name(second, 'es')}",
               "en": f"Youth unemployment ranges from {v[low]:g}% in {geo.name(low, 'en')} to {v[top]:g}% in {geo.name(top, 'en')} and {v[second]:g}% in {geo.name(second, 'en')}"},
        subtitle={"es": f"Tasa de paro de 15 a 24 años, en % de los activos de esa edad, {YEAR}. UE: {fmt_es(v['EU27'])} %",
                  "en": f"Unemployment rate aged 15-24, as % of the labour force of that age, {YEAR}. EU: {v['EU27']:g}%"},
        unit={"es": "% de los activos de 15 a 24 años", "en": "% of the labour force aged 15-24"},
        source=eurostat_source("une_rt_a"),
        notes={"es": ["Encuesta de Población Activa. La tasa se calcula sobre los jóvenes que trabajan o buscan empleo, no sobre todos los jóvenes: donde muchos estudiantes buscan trabajo a la vez, la tasa sube aunque estén estudiando.",
                      *([f"Sin dato de {YEAR} para {', '.join(missing)}."] if missing else [])],
               "en": ["Labour Force Survey. The rate is calculated over young people who work or look for work, not over all young people: where many students look for work at the same time, the rate rises even though they are studying.",
                      *([f"No {YEAR} figure for {', '.join(missing_en)}."] if missing else [])]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
    )


def edad_emancipacion():
    raw = sources.eurostat("yth_demo_030", unit="AVG", sex="T", time=[BASE, YEAR])
    out = [r for r in from_eurostat(raw, []) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    for r in out:
        r["value"] = round(r["value"], 1)
        r.pop("flag", None)
    v = {(r["geo"], r["time"]): r["value"] for r in out}
    countries = sorted((c for c in geo.EU27 if (c, YEAR) in v), key=lambda c: v[(c, YEAR)])
    low, top = countries[0], countries[-1]
    later = [c for c in countries if (c, BASE) in v and v[(c, YEAR)] > v[(c, BASE)]]
    assert top == "HRV" and low == "FIN", (top, low)
    return chart(
        id="emd2-edad-emancipacion",
        lens="dentro", theme="empleo",
        title={"es": f"Los jóvenes se van de casa de sus padres a los {fmt_es(v[(top, YEAR)])} años en {geo.name(top, 'es')} y a los {fmt_es(v[(low, YEAR)])} en {geo.name(low, 'es')}; en la UE, a los {fmt_es(v[('EU27', YEAR)])}, casi igual que en {BASE}",
               "en": f"Young people leave their parents' home at {v[(top, YEAR)]:g} in {geo.name(top, 'en')} and at {v[(low, YEAR)]:g} in {geo.name(low, 'en')}; in the EU, at {v[('EU27', YEAR)]:g}, almost the same as in {BASE}"},
        subtitle={"es": f"Edad media a la que los jóvenes dejan el hogar de sus padres, en años, {BASE} y {YEAR}",
                  "en": f"Average age at which young people leave the parental home, in years, {BASE} and {YEAR}"},
        unit={"es": "años", "en": "years"},
        source=eurostat_source("yth_demo_030"),
        notes={"es": [f"Entre {BASE} y {YEAR}, la edad ha subido en {len(later)} de los {len(countries)} países. En la UE pasó de {fmt_es(v[('EU27', BASE)])} a {fmt_es(v[('EU27', YEAR)])} años.",
                      "Estimación de Eurostat a partir de la Encuesta de Condiciones de Vida (EU-SILC): la edad a la que la mitad de los jóvenes ya no vive con sus padres. En 2021 hay una ruptura de serie."],
               "en": [f"Between {BASE} and {YEAR}, the age rose in {len(later)} of the {len(countries)} countries. In the EU it went from {v[('EU27', BASE)]:g} to {v[('EU27', YEAR)]:g} years.",
                      "Eurostat estimate based on the Survey on Income and Living Conditions (EU-SILC): the age at which half of young people no longer live with their parents. There is a break in the series in 2021."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [paro_juvenil_paises, edad_emancipacion]
