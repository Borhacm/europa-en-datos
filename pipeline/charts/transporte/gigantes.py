"""Transporte. Mirada 1: las emisiones del transporte en la UE, EE. UU. y China."""

from collections import defaultdict

from lib import geo, sources
from lib.output import chart

BLOCS = ["EU27", "USA", "CHN"]
START, LAST = "1990", "2024"
EDGAR_SOURCE = {"name": "Comisión Europea, JRC: EDGAR, emisiones de gases de efecto invernadero (informe de 2025)",
                "dataset": "EDGAR_2025_GHG", "url": "https://edgar.jrc.ec.europa.eu/report_2025", "license": "CC BY 4.0"}
NOTES = {
    "es": ["Todos los gases de efecto invernadero (CO2, metano, óxido nitroso y gases fluorados), en millones de toneladas de CO2 equivalente con el potencial de calentamiento a 100 años del IPCC (AR5).",
           "Transporte: carretera, ferrocarril, navegación y aviación dentro de cada país. No incluye la aviación ni la navegación internacionales, que EDGAR cuenta aparte, sin asignarlas a ningún país."],
    "en": ["All greenhouse gases (CO2, methane, nitrous oxide and fluorinated gases), in million tonnes of CO2 equivalent using the IPCC 100-year warming potentials (AR5).",
           "Transport: road, rail, shipping and aviation within each country. It excludes international aviation and shipping, which EDGAR counts separately without assigning them to any country."],
}


def _sectors() -> dict[tuple[str, str, str], float]:
    """{(bloque, sector, año): Mt CO2e}, sumando los cuatro gases."""
    out = defaultdict(float)
    for r in sources.edgar_sectors():
        if r["code"] in BLOCS:
            out[(r["code"], r["sector"], r["time"])] += r["value"]
    return out


def fmt_es(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def emisiones():
    v = _sectors()
    years = sorted({t for (_, s, t) in v if s == "Transport" and START <= t <= LAST})
    out = [{"geo": b, "time": t, "value": round(v[(b, "Transport", t)], 1)} for b in BLOCS for t in years]
    sectors = {s for (_, s, _) in v}
    up = [s for s in sectors if v[("EU27", s, LAST)] > v[("EU27", s, START)]]
    assert up == ["Transport"], up
    change = {b: round(100 * (v[(b, "Transport", LAST)] / v[(b, "Transport", START)] - 1)) for b in BLOCS}
    return chart(
        id="trg1-emisiones",
        lens="gigantes", theme="transporte",
        title={"es": f"En la UE, el transporte es el único sector que emite más gases que en {START}, un {change['EU27']} % más; en EE. UU., un {change['USA']} % más",
               "en": f"In the EU, transport is the only sector emitting more greenhouse gases than in {START}, {change['EU27']}% more; in the US, {change['USA']}% more"},
        subtitle={"es": f"Emisiones de gases de efecto invernadero del transporte, en millones de toneladas de CO2 equivalente, {START}-{LAST}",
                  "en": f"Greenhouse gas emissions from transport, in million tonnes of CO2 equivalent, {START}-{LAST}"},
        unit={"es": "Mt de CO2 equivalente", "en": "Mt CO2 equivalent"},
        source=EDGAR_SOURCE,
        notes={"es": [*NOTES["es"], f"EDGAR divide las emisiones en ocho sectores. En la UE, los otros siete emitieron en {LAST} menos que en {START}."],
               "en": [*NOTES["en"], f"EDGAR splits emissions into eight sectors. In the EU, the other seven emitted less in {LAST} than in {START}."]},
        rows=out,
        geos=geo.geo_table(BLOCS),
    )


def peso_transporte():
    v = _sectors()
    out = []
    share = {}
    for b in BLOCS:
        for t in (START, LAST):
            total = sum(x for (bb, _, tt), x in v.items() if bb == b and tt == t)
            share[(b, t)] = round(100 * v[(b, "Transport", t)] / total, 1)
            out.append({"geo": b, "time": t, "value": share[(b, t)]})
    top = {b: max((s for (bb, s, tt) in v if bb == b and tt == LAST), key=lambda s: v[(b, s, LAST)]) for b in BLOCS}
    assert top["EU27"] == "Transport" and 24.5 <= share[("EU27", LAST)] < 25.5 and 13 < share[("EU27", START)] < 14.3
    power = round(v[("EU27", "Power Industry", LAST)])
    transport = round(v[("EU27", "Transport", LAST)])
    return chart(
        id="trg2-peso-transporte",
        lens="gigantes", theme="transporte",
        title={"es": f"El transporte ya supone una de cada cuatro toneladas de gases que emite la UE; en {START}, una de cada siete",
               "en": f"Transport now accounts for one in four tonnes of greenhouse gases the EU emits; in {START}, one in seven"},
        subtitle={"es": f"Emisiones del transporte, en % del total de emisiones de gases de efecto invernadero, {START} y {LAST}",
                  "en": f"Transport emissions, as % of total greenhouse gas emissions, {START} and {LAST}"},
        unit={"es": "% de las emisiones", "en": "% of emissions"},
        source=EDGAR_SOURCE,
        notes={"es": [*NOTES["es"], f"En {LAST}, el transporte fue el sector que más emitió en la UE ({transport} millones de toneladas), por delante de la generación de electricidad y calor ({power}). El total no incluye el uso de la tierra y los bosques."],
               "en": [*NOTES["en"], f"In {LAST}, transport was the EU's largest emitting sector ({transport} million tonnes), ahead of power and heat generation ({power}). The total excludes land use and forestry."]},
        rows=out,
        geos=geo.geo_table(BLOCS),
    )


BUILDERS = [emisiones, peso_transporte]
