"""Finanzas públicas. Mirada 1: el déficit de la UE, EE. UU. y China, y cuánto se va en intereses."""

from lib import geo
from lib.output import chart

from ._imf import FM_SOURCE, WEO_SOURCE, eu_weighted, series

# Igual que la nota N06: desde 2025, el World Economic Outlook da estimaciones y proyecciones
START, LAST = 2001, 2024
BLOCS = {"USA": "USA", "CHN": "CHN", "EU": "EU27"}
REFERENCE = -3


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def deficit():
    v = series("GGXCNL_NGDP", list(BLOCS))
    out = [{"geo": BLOCS[c], "time": t, "value": round(x, 1)} for (c, t), x in v.items() if START <= int(t) <= LAST]
    years = LAST - START + 1
    over = {b: sum(1 for r in out if r["geo"] == b and r["value"] < REFERENCE) for b in ("USA", "EU27")}
    return chart(
        id="fpg1-deficit",
        lens="gigantes", theme="finanzas",
        title={"es": f"EE. UU. ha tenido un déficit superior al 3 % del PIB en {over['USA']} de los {years} años entre {START} y {LAST}; la UE, en {over['EU27']}",
               "en": f"The US has run a deficit above 3% of GDP in {over['USA']} of the {years} years from {START} to {LAST}; the EU, in {over['EU27']}"},
        subtitle={"es": f"Saldo de las administraciones públicas (capacidad o necesidad de financiación), en % del PIB, {START}-{LAST}",
                  "en": f"General government balance (net lending or borrowing), as % of GDP, {START}-{LAST}"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source=WEO_SOURCE,
        notes={"es": ["Ingresos menos gastos de todas las administraciones (central, regional, local y seguridad social). Un valor negativo es déficit.",
                      "Las tres series salen del FMI para que sean comparables. Se cortan en 2024: desde 2025, el World Economic Outlook da estimaciones y proyecciones.",
                      "La línea de -3 % es el valor de referencia del Tratado para los países de la UE; no obliga a EE. UU. ni a China."],
               "en": ["Revenue minus expenditure of all levels of government (central, regional, local and social security). A negative value is a deficit.",
                      "All three series come from the IMF so they are comparable. They stop in 2024: from 2025 on, the World Economic Outlook gives estimates and projections.",
                      "The -3% line is the Treaty reference value for EU countries; it does not bind the US or China."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"targets": [{"geo": "EU27", "time": str(LAST), "value": REFERENCE,
                            "label": {"es": "Valor de referencia del Tratado", "en": "Treaty reference value"}}]},
    )


MEASURES = {"primario": {"es": "Déficit sin intereses", "en": "Deficit excluding interest"},
            "total": {"es": "Déficit con intereses", "en": "Deficit including interest"}}


def intereses():
    year = str(LAST)
    overall, primary = series("GGXCNL_G01_GDP_PT", ["USA", "CHN"]), series("GGXONLB_G01_GDP_PT", ["USA", "CHN"])
    vals = {"EU27": (eu_weighted("GGXONLB_G01_GDP_PT", year), eu_weighted("GGXCNL_G01_GDP_PT", year)),
            **{c: (primary[(c, year)], overall[(c, year)]) for c in ("USA", "CHN")}}
    out = []
    for g, (p, o) in vals.items():
        # En positivo: el gráfico compara déficits, y los tres bloques los tienen
        assert p < 0 and o < 0
        out += [{"geo": g, "time": year, "measure": "primario", "value": round(-p, 1)},
                {"geo": g, "time": year, "measure": "total", "value": round(-o, 1)}]
    interest = {g: round(p - o, 1) for g, (p, o) in vals.items()}
    ratio = interest["USA"] / interest["EU27"]
    times_es = "más del doble que la UE" if ratio > 2 else f"{fmt_es(round(ratio, 1))} veces lo de la UE"
    times_en = "more than twice the EU" if ratio > 2 else f"{round(ratio, 1):g} times the EU"
    return chart(
        id="fpg2-intereses",
        lens="gigantes", theme="finanzas",
        title={"es": f"EE. UU. dedica a pagar intereses el {fmt_es(interest['USA'])} % de su PIB, {times_es}; aun sin ellos, su déficit sería del {fmt_es(-round(vals['USA'][0], 1))} %",
               "en": f"The US spends {interest['USA']:g}% of its GDP on interest, {times_en}; even without it, its deficit would be {-round(vals['USA'][0], 1):g}%"},
        subtitle={"es": f"Déficit de las administraciones públicas sin contar los intereses netos (déficit primario) y con ellos, en % del PIB, {year}",
                  "en": f"General government deficit excluding net interest (primary deficit) and including it, as % of GDP, {year}"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source={**FM_SOURCE, "also": [{**FM_SOURCE, "dataset": "GGXCNL_G01_GDP_PT", "url": "https://www.imf.org/external/datamapper/GGXCNL_G01_GDP_PT@FM"},
                                      {**WEO_SOURCE, "dataset": "NGDPD", "url": "https://www.imf.org/external/datamapper/NGDPD@WEO"}]},
        notes={"es": ["La distancia entre los dos puntos son los intereses netos: los que pagan las administraciones menos los que cobran.",
                      "UE: media de los 27 ponderada por su PIB en dólares corrientes, con los datos del Fiscal Monitor de cada país. El saldo resultante coincide con el agregado de la UE del World Economic Outlook.",
                      "Eurostat publica los intereses brutos (sin restar los que se cobran), que son algo más altos: son los del gráfico D2."],
               "en": ["The distance between the two dots is net interest: what governments pay minus what they receive.",
                      "EU: average of the 27 weighted by GDP in current dollars, using each country's Fiscal Monitor data. The resulting balance matches the World Economic Outlook EU aggregate.",
                      "Eurostat publishes gross interest (without subtracting what is received), which is somewhat higher: it is the measure in chart D2."]},
        rows=out,
        geos=geo.geo_table(vals),
        extra={"dimensions": {"measure": MEASURES}},
    )


BUILDERS = [deficit, intereses]
