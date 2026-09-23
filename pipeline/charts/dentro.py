"""Mirada 3. Europa por dentro: diferencias entre los 27 países y sus regiones."""

import json

from lib import geo, sources
from lib.http import fetch
from lib.output import DATA_DIR, chart

from .common import eurostat_source, from_eurostat

SIZES = {
    "GE10": {"es": "Todas (10 o más empleados)", "en": "All (10+ employees)"},
    "10-49": {"es": "Pequeñas (10 a 49)", "en": "Small (10-49)"},
    "50-249": {"es": "Medianas (50 a 249)", "en": "Medium (50-249)"},
    "GE250": {"es": "Grandes (250 o más)", "en": "Large (250+)"},
}


def empresas_ia():
    rows = sources.eurostat("isoc_eb_ai", indic_is="E_AI_TANY", unit="PC_ENT", size_emp=list(SIZES))
    out = from_eurostat(rows, ["size_emp"])
    for r in out:
        r["size"] = r.pop("size_emp")
    return chart(
        id="d1-empresas-ia",
        lens="dentro", theme="ia-digital",
        title={"es": "Dos Europas de la IA: en Dinamarca la usan más de cuatro de cada diez empresas; en Rumanía, una de cada veinte",
               "en": "Two AI Europes: in Denmark more than four in ten firms use it; in Romania, one in twenty"},
        subtitle={"es": "Empresas que usan al menos una tecnología de IA, en % del total (10 o más empleados, sin sector financiero)",
                  "en": "Enterprises using at least one AI technology, as % of all enterprises (10+ employees, excl. financial sector)"},
        unit={"es": "% de empresas", "en": "% of enterprises"},
        source=eurostat_source("isoc_eb_ai"),
        notes={"es": ["No hay datos de 2022: la pregunta no se hizo ese año.",
                      "En 2025 cambió la lista de tecnologías de IA de la encuesta, lo que puede influir en el salto respecto a 2024."],
               "en": ["No 2022 data: the question was not asked that year.",
                      "The list of AI technologies in the survey changed in 2025, which may affect the jump from 2024."]},
        rows=sorted(out, key=lambda r: (r["size"], r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"size": SIZES}},
    )


GISCO = "https://gisco-services.ec.europa.eu/distribution/v2/nuts/topojson/NUTS_RG_20M_2024_4326_LEVL_{level}.json"


def mapa_regional_ia():
    rows = sources.eurostat("isoc_r_eb_ain2", indic_is="E_AI_TANY", unit="PC_ENT", size_emp="GE10", nace_r2="C10-S951_X_K")
    out = []
    for r in rows:
        nuts = r["geo"]
        if nuts.startswith(("EU", "EA")):
            continue
        country = geo.from_eurostat(nuts[:2])
        if country is None:
            continue
        out.append({"geo": nuts, "country": country, "level": len(nuts) - 2, "time": r["time"],
                    "value": round(r["value"], 2), "name": r["geo_label"]})

    # Cada país publica al nivel regional que puede: elegimos el más detallado del último año
    latest = max(r["time"] for r in out)
    best_level = {}
    for r in out:
        if r["time"] == latest:
            best_level[r["country"]] = max(best_level.get(r["country"], 0), r["level"])

    geo_dir = DATA_DIR / "geo"
    geo_dir.mkdir(parents=True, exist_ok=True)
    missing = {}
    for level in (0, 1, 2):
        topo = json.loads(fetch(GISCO.format(level=level), ".json").read_text())
        (geo_dir / f"nuts{level}.json").write_text(json.dumps(topo, separators=(",", ":")))
        obj = next(iter(topo["objects"].values()))
        ids = {g["properties"].get("id") or g.get("id") for g in obj["geometries"]}
        missing[level] = sorted({r["geo"] for r in out if r["level"] == level} - ids)

    return chart(
        id="d2-mapa-regional-ia",
        lens="dentro", theme="ia-digital",
        title={"es": "La IA se concentra en las capitales: la región de la capital va primera en casi todos los países con datos regionales",
               "en": "AI clusters around capitals: the capital region leads in almost every country with regional data"},
        subtitle={"es": "Empresas que usan al menos una tecnología de IA, por región, en % del total (10 o más empleados)",
                  "en": "Enterprises using at least one AI technology, by region, as % of all enterprises (10+ employees)"},
        unit={"es": "% de empresas", "en": "% of enterprises"},
        source=eurostat_source("isoc_r_eb_ain2", also=[{"name": "Eurostat GISCO, NUTS 2024 (geometrías)",
                                                        "url": "https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics"}]),
        notes={"es": ["Algunos países solo publican datos de grandes regiones (NUTS 1) o del país entero. El mapa usa el nivel más detallado disponible en cada país (best_level)."],
               "en": ["Some countries only publish data for large regions (NUTS 1) or the whole country. The map uses the most detailed level available per country (best_level)."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(best_level),
        extra={"best_level": best_level, "latest": latest,
               "geometry": {str(lvl): f"geo/nuts{lvl}.json" for lvl in (0, 1, 2)},
               "unmatched_geometry": missing},
    )


AGES = {
    "IND_TOTAL": {"es": "16 a 74 años", "en": "Aged 16-74"},
    "Y16_24": {"es": "16 a 24 años", "en": "Aged 16-24"},
    "Y25_54": {"es": "25 a 54 años", "en": "Aged 25-54"},
    "Y55_74": {"es": "55 a 74 años", "en": "Aged 55-74"},
}
GENAI_USES = {
    "I_IUAI": {"es": "Cualquier uso", "en": "Any use"},
    "I_IUAIWP": {"es": "Para el trabajo", "en": "For work"},
}


def ia_generativa():
    rows = sources.eurostat("isoc_ai_iaiu", unit="PC_IND", ind_type=list(AGES), indic_is=list(GENAI_USES))
    out = from_eurostat(rows, ["ind_type", "indic_is"])
    for r in out:
        r["age"], r["use"] = r.pop("ind_type"), r.pop("indic_is")
    return chart(
        id="d3-ia-generativa",
        lens="dentro", theme="ia-digital",
        title={"es": "Uno de cada tres europeos ya usa IA generativa: casi la mitad en Dinamarca, menos de uno de cada cinco en Italia o Rumanía",
               "en": "One in three Europeans already uses generative AI: nearly half in Denmark, fewer than one in five in Italy or Romania"},
        subtitle={"es": "Personas que usaron herramientas de IA generativa en los últimos 3 meses, en % de la población",
                  "en": "People who used generative AI tools in the last 3 months, as % of the population"},
        unit={"es": "% de personas", "en": "% of individuals"},
        source=eurostat_source("isoc_ai_iaiu"),
        notes={"es": ["Solo hay un año de datos (2025). La serie empezará a tener tendencia con la encuesta de 2026."],
               "en": ["Only one year of data (2025). A trend will emerge with the 2026 survey."]},
        rows=sorted(out, key=lambda r: (r["use"], r["age"], r["geo"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"age": AGES, "use": GENAI_USES}},
    )


def competencias_digitales():
    rows = sources.eurostat("isoc_sk_dskl_i21", indic_is="I_DSK2_BAB", unit="PC_IND", ind_type="IND_TOTAL")
    out = from_eurostat(rows, [])
    return chart(
        id="d4-competencias-digitales",
        lens="dentro", theme="ia-digital",
        title={"es": "Europa se queda lejos de su objetivo de competencias digitales para 2030",
               "en": "Europe falls far short of its 2030 digital skills target"},
        subtitle={"es": "Personas con competencias digitales básicas o superiores, en % de la población de 16 a 74 años",
                  "en": "People with basic or above basic digital skills, as % of the population aged 16-74"},
        unit={"es": "% de personas", "en": "% of individuals"},
        source=eurostat_source("isoc_sk_dskl_i21", also=[{
            "name": "Década Digital 2030, objetivo del 80 %",
            "url": "https://digital-strategy.ec.europa.eu/en/policies/europes-digital-decade"}]),
        notes={"es": ["La encuesta se hace cada dos años (2021, 2023, 2025)."],
               "en": ["The survey runs every two years (2021, 2023, 2025)."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"targets": [{"geo": "EU27", "time": "2030", "value": 80,
                            "label": {"es": "Objetivo de la UE para 2030", "en": "EU 2030 target"}}]},
    )


BUILDERS = [empresas_ia, mapa_regional_ia, ia_generativa, competencias_digitales]
