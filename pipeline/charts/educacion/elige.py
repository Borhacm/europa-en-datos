"""Educación. Mirada 2: en qué etapa se gasta el dinero público de educación y qué rinde estudiar."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

EXP_YEAR = "2024"
# Grupos de la clasificación COFOG (función 09, educación)
LEVELS = {
    "SCHOOL": {"es": "Infantil, primaria y secundaria", "en": "Pre-primary, primary and secondary"},
    "TERTIARY": {"es": "Educación superior", "en": "Tertiary education"},
    "OTHER": {"es": "Servicios auxiliares, I+D y otros", "en": "Subsidiary services, R&D and other"},
}
GROUPS = {
    "SCHOOL": ["GF0901", "GF0902", "GF0903"],
    "TERTIARY": ["GF0904"],
    "OTHER": ["GF0905", "GF0906", "GF0907", "GF0908"],
}


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def gasto_niveles():
    codes = [c for cs in GROUPS.values() for c in cs]
    raw = sources.eurostat("gov_10a_exp", unit="MIO_EUR", sector="S13", na_item="TE", cofog99=["GF09", *codes], time=EXP_YEAR)
    v = {(r["geo"], r["cofog99"]): r["value"] for r in from_eurostat(raw, ["cofog99"])}
    pct = sources.eurostat("gov_10a_exp", unit="PC_GDP", sector="S13", na_item="TE", cofog99="GF09", time=EXP_YEAR)
    gdp = {r["geo"]: r["value"] for r in from_eurostat(pct, [])}
    out = []
    for g in ["EU27", *geo.EU27]:
        total = v.get((g, "GF09"))
        if not total:
            continue
        for k, cs in GROUPS.items():
            out.append({"geo": g, "time": EXP_YEAR, "reason": k, "value": round(100 * sum(v.get((g, c), 0) for c in cs) / total, 1)})
    s = {(r["geo"], r["reason"]): r["value"] for r in out}
    countries = sorted((c for c in geo.EU27 if (c, "TERTIARY") in s), key=lambda c: s[(c, "TERTIARY")])
    low, top = countries[0], countries[-1]
    eu_t = s[("EU27", "TERTIARY")]
    assert len(countries) == 27 and top == "GRC" and low == "FRA", (top, low)
    return chart(
        id="ede1-gasto-niveles",
        lens="elige", theme="educacion",
        title={"es": f"De cada 100 euros de gasto público en educación, la UE dedica {fmt_es(eu_t)} a la educación superior; {geo.name(top, 'es')}, {fmt_es(s[(top, 'TERTIARY')])}, y {geo.name(low, 'es')}, {fmt_es(s[(low, 'TERTIARY')])}",
               "en": f"Of every 100 euros of public spending on education, the EU devotes {eu_t:g} to tertiary education; {geo.name(top, 'en')}, {s[(top, 'TERTIARY')]:g}, and {geo.name(low, 'en')}, {s[(low, 'TERTIARY')]:g}"},
        subtitle={"es": f"Gasto de las administraciones públicas en educación por etapa, en % del gasto público en educación, {EXP_YEAR}. UE: {fmt_es(gdp['EU27'])} % del PIB en total",
                  "en": f"General government spending on education by level, as % of public spending on education, {EXP_YEAR}. EU: {gdp['EU27']:g}% of GDP in total"},
        unit={"es": "% del gasto público en educación", "en": "% of public spending on education"},
        source=eurostat_source("gov_10a_exp"),
        notes={"es": ["Gasto de todas las administraciones públicas (estatal, regional y local) en la función educación de la clasificación COFOG, en millones de euros. No incluye lo que pagan las familias ni las empresas.",
                      "«Infantil, primaria y secundaria» suma también la postsecundaria no terciaria. «Servicios auxiliares, I+D y otros» incluye el transporte escolar, los comedores y el alojamiento, la investigación sobre educación y el gasto que no se puede asignar a un nivel.",
                      f"Cada país asigna su gasto a los niveles a su manera, así que la comparación es aproximada. En {geo.name(low, 'es')}, por ejemplo, los servicios auxiliares y otros suman el {fmt_es(s[(low, 'OTHER')])} %, frente al {fmt_es(s[('EU27', 'OTHER')])} % de la UE."],
               "en": ["Spending by all levels of government (central, regional and local) on the education function of the COFOG classification, in millions of euros. It does not include what households or businesses pay.",
                      "«Pre-primary, primary and secondary» also includes post-secondary non-tertiary education. «Subsidiary services, R&D and other» includes school transport, meals and accommodation, research on education and spending that cannot be assigned to a level.",
                      f"Each country assigns its spending to levels in its own way, so the comparison is approximate. In {geo.name(low, 'en')}, for example, subsidiary services and other spending add up to {s[(low, 'OTHER')]:g}%, against {s[('EU27', 'OTHER')]:g}% in the EU."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["reason"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"reason": LEVELS}},
    )


EMP_YEAR = "2025"
ISCED = {
    "ED0-2": {"es": "Hasta secundaria obligatoria", "en": "Lower secondary at most"},
    "ED3_4": {"es": "Bachillerato o FP media", "en": "Upper secondary or vocational"},
    "ED5-8": {"es": "Estudios superiores", "en": "Tertiary education"},
}


def empleo_nivel():
    raw = sources.eurostat("edat_lfse_24", sex="T", age="Y20-34", unit="PC", duration="TOTAL", isced11=list(ISCED), time=EMP_YEAR)
    out = [r for r in from_eurostat(raw, ["isced11"]) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    v = {(r["geo"], r["isced11"]): r["value"] for r in out}
    countries = [c for c in geo.EU27 if all((c, k) in v for k in ISCED)]
    gap = {c: round(v[(c, "ED5-8")] - v[(c, "ED0-2")], 1) for c in countries}
    big = max(countries, key=gap.get)
    small = min(countries, key=gap.get)
    inverted = [c for c in countries if v[(c, "ED5-8")] < v[(c, "ED3_4")]]
    eu_hi, eu_lo = v[("EU27", "ED5-8")], v[("EU27", "ED0-2")]
    assert len(countries) == 27 and inverted == ["CZE"] and big == "SVK" and small == "CYP", (inverted, big, small)
    for r in out:
        r.pop("flag", None)
    return chart(
        id="ede2-empleo-nivel",
        lens="elige", theme="educacion",
        title={"es": f"En la UE trabaja el {fmt_es(eu_hi)} % de los jóvenes con estudios superiores y el {fmt_es(eu_lo)} % de los que no pasaron de la secundaria obligatoria; en {geo.name(big, 'es')}, la distancia es de {fmt_es(gap[big])} puntos",
               "en": f"In the EU, {eu_hi:g}% of young people with tertiary education are in work, against {eu_lo:g}% of those with lower secondary at most; in {geo.name(big, 'en')}, the gap is {gap[big]:g} points"},
        subtitle={"es": f"Tasa de empleo de las personas de 20 a 34 años que ya no estudian, por nivel de estudios, en %, {EMP_YEAR}",
                  "en": f"Employment rate of people aged 20 to 34 no longer in education, by educational attainment, in %, {EMP_YEAR}"},
        unit={"es": "% con empleo", "en": "% in employment"},
        source=eurostat_source("edat_lfse_24"),
        notes={"es": ["Encuesta de Población Activa de la UE. Cuenta a las personas de 20 a 34 años que no siguen estudiando ni formándose, sea cual sea el tiempo que haya pasado desde que terminaron.",
                      "Más empleo con más estudios no prueba que los estudios lo causen: también influyen otros factores, como el origen familiar, que estos datos no separan. El gráfico compara niveles, no mide el efecto de estudiar.",
                      f"{geo.name(inverted[0], 'es')} es el único país en el que los titulados superiores tienen menos empleo ({fmt_es(v[(inverted[0], 'ED5-8')])} %) que los de bachillerato o FP ({fmt_es(v[(inverted[0], 'ED3_4')])} %).",
                      "Eurostat marca como poco fiables por el tamaño de la muestra los datos del nivel más bajo en Croacia, Irlanda y Eslovenia, y señala cambios de definición en España y Francia y una ruptura de serie en Dinamarca."],
               "en": ["EU Labour Force Survey. It counts people aged 20 to 34 who are no longer in education or training, however long ago they finished.",
                      "More employment with more education does not prove that education causes it: other factors, such as family background, also play a part and these data do not separate them. The chart compares levels; it does not measure the effect of studying.",
                      f"{geo.name(inverted[0], 'en')} is the only country where tertiary graduates have a lower employment rate ({v[(inverted[0], 'ED5-8')]:g}%) than those with upper secondary or vocational education ({v[(inverted[0], 'ED3_4')]:g}%).",
                      "Eurostat flags the lowest-level figures for Croatia, Ireland and Slovenia as unreliable because of sample size, and notes definition changes in Spain and France and a break in the series for Denmark."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["isced11"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"isced11": ISCED}},
    )


BUILDERS = [gasto_niveles, empleo_nivel]
