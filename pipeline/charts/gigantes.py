"""Mirada 1. Entre dos gigantes: la UE frente a EE. UU. y China."""

from lib import geo, sources
from lib.output import chart

BLOCS = ["USA", "CHN", "EU27"]
CONTEXT = ["ESP", "DEU", "FRA", "JPN", "KOR"]


def _oecd_geo(code: str) -> str | None:
    return geo.from_iso3(code)


def inversion_id():
    rows = sources.oecd(
        "OECD.STI.STP,DSD_MSTI@DF_MSTI,1.3",
        "USA+CHN+EU27_2020+ESP+DEU+FRA+JPN+KOR.A.G+B.PT_B1GQ..",
        start="2000",
    )
    out = []
    for r in rows:
        # MSTI mezcla niveles y transformaciones (tasas de crecimiento): nos quedamos con el nivel
        if r.get("TRANSFORMATION", "_Z") != "_Z" or not r["OBS_VALUE"]:
            continue
        out.append({
            "geo": _oecd_geo(r["REF_AREA"]),
            "time": r["TIME_PERIOD"],
            "value": round(float(r["OBS_VALUE"]), 3),
            "measure": {"G": "total", "B": "empresas"}[r["MEASURE"]],
        })
    return chart(
        id="g1-inversion-id",
        lens="gigantes", theme="ia-digital",
        title={"es": "Europa invierte menos en investigación, y la brecha está en las empresas",
               "en": "Europe invests less in research, and the gap lies in business"},
        subtitle={"es": "Gasto en I+D, total y empresarial, en % del PIB",
                  "en": "R&D expenditure, total and business, as % of GDP"},
        unit={"es": "% del PIB", "en": "% of GDP"},
        source={"name": "OCDE, Main Science and Technology Indicators", "dataset": "DSD_MSTI@DF_MSTI",
                "url": "https://data-explorer.oecd.org/?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_MSTI%40DF_MSTI&df[ag]=OECD.STI.STP",
                "license": "CC BY 4.0"},
        rows=sorted(out, key=lambda r: (r["measure"], r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"measure": {
            "total": {"es": "I+D total (GERD)", "en": "Total R&D (GERD)"},
            "empresas": {"es": "I+D de las empresas (BERD)", "en": "Business R&D (BERD)"}}},
            "highlight": BLOCS},
    )


def patentes_ia():
    rows = sources.oecd(
        "OECD.STI.PIE,DSD_PATENTS@DF_PATENTS_OECDSPECIFIC,1.0",
        "9P50_1.A.AP.PATN.PRIORITY.USA+CHN+EU27_2020+ESP+DEU+FRA+JPN+KOR._Z.INVENTOR._Z._Z.AI",
        start="2005",
    )
    pop = {(geo.from_iso3(p["iso3"]), p["time"]): p["value"]
           for p in sources.worldbank("SP.POP.TOTL", ["USA", "CHN", "EUU", "ESP", "DEU", "FRA", "JPN", "KOR"], 2005, 2025)}
    out = []
    for r in rows:
        if not r["OBS_VALUE"]:
            continue
        code, t = _oecd_geo(r["REF_AREA"]), r["TIME_PERIOD"]
        n = float(r["OBS_VALUE"])
        row = {"geo": code, "time": t, "value": round(n, 1)}
        # La población de 2025 aún no está publicada para todos: usamos la del último año disponible
        p = pop.get((code, t)) or pop.get((code, str(int(t) - 1)))
        if p:
            row["per_million"] = round(n / p * 1e6, 2)
        if r.get("OBS_STATUS"):
            row["flag"] = r["OBS_STATUS"]
        out.append(row)
    return chart(
        id="g2-patentes-ia",
        lens="gigantes", theme="ia-digital",
        title={"es": "En patentes de IA, EE. UU. y China juegan otra liga",
               "en": "In AI patents, the US and China are in another league"},
        subtitle={"es": "Solicitudes internacionales (PCT) de patentes de IA, por país del inventor y año de prioridad",
                  "en": "International (PCT) AI patent applications, by inventor country and priority year"},
        unit={"es": "solicitudes", "en": "applications"},
        source={"name": "OCDE, Patents in OECD selected technologies", "dataset": "DSD_PATENTS@DF_PATENTS_OECDSPECIFIC",
                "url": "https://data-explorer.oecd.org/?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_PATENTS%40DF_PATENTS_OECDSPECIFIC&df[ag]=OECD.STI.PIE",
                "license": "CC BY 4.0",
                "also": [{"name": "Banco Mundial, población (SP.POP.TOTL)", "url": "https://data.worldbank.org/indicator/SP.POP.TOTL"}]},
        notes={"es": ["Las solicitudes con varios inventores se reparten entre sus países (recuento fraccional).",
                      "Los dos o tres últimos años pueden estar incompletos por el retraso en la publicación de patentes.",
                      "El campo per_million divide por la población del Banco Mundial."],
               "en": ["Applications with several inventors are split between their countries (fractional count).",
                      "The last two or three years may be incomplete due to publication lags.",
                      "per_million divides by World Bank population."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"highlight": BLOCS},
    )


EPOCH_BLOCS = {
    "USA": lambda c: c == "United States of America",
    "CHN": lambda c: c in ("China", "Hong Kong"),
    "EU27": lambda c: c in {geo.COUNTRIES[i][2] for i in geo.EU27},
    "GBR": lambda c: c == "United Kingdom",
}


def epoch_blocs(model: dict) -> set[str]:
    countries = {c.strip() for c in model["Country (of organization)"].split(",") if c.strip()}
    return {b for b, test in EPOCH_BLOCS.items() if any(test(c) for c in countries)}


def modelos_ia():
    counts = {}
    for m in sources.epoch_models():
        year = m["Publication date"][:4]
        if not year.isdigit() or not 2015 <= int(year):
            continue
        blocs = epoch_blocs(m)
        for b in blocs:
            counts[(b, year, "participa")] = counts.get((b, year, "participa"), 0) + 1
            if len(blocs) == 1:
                counts[(b, year, "solo")] = counts.get((b, year, "solo"), 0) + 1

    years = sorted({y for _, y, _ in counts})
    out = [{"geo": b, "time": y, "rule": rule, "value": counts.get((b, y, rule), 0)}
           for b in EPOCH_BLOCS for y in years for rule in ("participa", "solo")]
    return chart(
        id="g3-modelos-ia",
        lens="gigantes", theme="ia-digital",
        title={"es": "Los modelos de IA que marcan el ritmo se hacen en EE. UU. y China",
               "en": "The AI models that set the pace are built in the US and China"},
        subtitle={"es": "Modelos de IA destacados publicados cada año, según el país de las organizaciones que los desarrollan",
                  "en": "Notable AI models released each year, by country of the developing organisations"},
        unit={"es": "modelos", "en": "models"},
        source={"name": "Epoch AI, Data on AI Models", "dataset": "notable_ai_models.csv",
                "url": "https://epoch.ai/data/ai-models", "license": "CC BY 4.0"},
        notes={"es": ["'Destacado' sigue los criterios de Epoch: estado del arte, muchas citas, más de un millón de usuarios, relevancia histórica o coste de entrenamiento superior a un millón de dólares.",
                      "Regla 'participa': el modelo cuenta para un bloque si al menos una organización es de ese bloque. Regla 'solo': únicamente modelos desarrollados dentro de un solo bloque.",
                      "China incluye Hong Kong. El Reino Unido se muestra aparte porque no es de la UE.",
                      f"El año {years[-1]} está incompleto (datos hasta la fecha de descarga): no se dibuja en el gráfico, pero sí está en la tabla y en la descarga."],
               "en": ["'Notable' follows Epoch's criteria: state of the art, highly cited, over a million users, historical significance or training cost above one million dollars.",
                      "'participa' rule: a model counts for a bloc if at least one organisation is from that bloc. 'solo' rule: only models developed within a single bloc.",
                      "China includes Hong Kong. The United Kingdom is shown separately as it is not in the EU.",
                      f"{years[-1]} is incomplete (data up to download date): it is not drawn in the chart, but it is in the table and the download."]},
        rows=out,
        geos={**geo.geo_table(["USA", "CHN", "EU27", "GBR"])},
        extra={"dimensions": {"rule": {
            "participa": {"es": "Con participación del bloque", "en": "With bloc participation"},
            "solo": {"es": "Solo del bloque", "en": "Bloc only"}}},
            "highlight": BLOCS, "partial_year": years[-1]},
    )


BUILDERS = [inversion_id, patentes_ia, modelos_ia]
