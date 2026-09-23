"""Mirada 2. ¿Pierde Europa o elige? Lo que el modelo europeo gana y lo que cede."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat
from .gigantes import EPOCH_BLOCS, epoch_blocs

REASONS = {
    "I_IUAIX_NUNN": {"es": "No la necesito", "en": "No need"},
    "I_IUAIX_NUUSE": {"es": "No sé usarla", "en": "Did not know how to use them"},
    "I_IUAIX_NUUNK": {"es": "No sabía que existía", "en": "Did not know they existed"},
    "I_IUAIX_NUSEC": {"es": "Privacidad, seguridad o protección", "en": "Privacy, security or safety concerns"},
    "I_IUAIX_NUOTH": {"es": "Otros motivos", "en": "Other reasons"},
}


def motivos_no_ia_generativa():
    rows = sources.eurostat("isoc_ai_iaiuxr", unit="PC_IND_IUAIX", ind_type="IND_TOTAL", indic_is=list(REASONS))
    out = from_eurostat(rows, ["indic_is"])
    for r in out:
        r["reason"] = r.pop("indic_is")
    return chart(
        id="e1-motivos-no-ia-generativa",
        lens="elige", theme="ia-digital",
        title={"es": "Quien no usa IA generativa no es por prudencia: dice que no la necesita",
               "en": "Europeans who skip generative AI are not being cautious: they say they don't need it"},
        subtitle={"es": "Motivos para no usar herramientas de IA generativa, en % de quienes no las usaron en los últimos 3 meses (16 a 74 años)",
                  "en": "Reasons for not using generative AI tools, as % of those who did not use them in the last 3 months (aged 16-74)"},
        unit={"es": "% de quienes no usan IA generativa", "en": "% of non-users of generative AI"},
        source=eurostat_source("isoc_ai_iaiuxr"),
        notes={"es": ["Pregunta con respuesta múltiple: los porcentajes pueden sumar más de 100.",
                      "Encuesta de 2025, la primera que incluye esta pregunta."],
               "en": ["Multiple-choice question: shares may add up to more than 100.",
                      "2025 survey, the first to include this question."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["reason"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"reason": REASONS}},
    )


VDEM_MEASURES = {
    "v2smgovfilprc": {"es": "Filtrado de internet por el Gobierno", "en": "Government internet filtering"},
    "v2smgovsmcenprc": {"es": "Censura de redes sociales por el Gobierno", "en": "Government social media censorship"},
}


def control_internet():
    df = sources.vdem(list(VDEM_MEASURES))
    df = df[(df.year >= 2000) & df.country_text_id.isin(["USA", "CHN", *geo.EU27])]
    out = []
    for m in VDEM_MEASURES:
        for r in df[["country_text_id", "year", m]].dropna().itertuples(index=False):
            out.append({"geo": r[0], "time": str(int(r[1])), "measure": m, "value": round(float(r[2]), 3), "stat": "country"})
        # Mediana de los 27 como referencia de la UE (V-Dem no publica agregados)
        eu = df[df.country_text_id.isin(geo.EU27)].groupby("year")[m]
        for year, med in eu.median().dropna().items():
            out.append({"geo": "EU27", "time": str(int(year)), "measure": m, "value": round(float(med), 3), "stat": "median"})
        for year, lo in eu.min().dropna().items():
            out.append({"geo": "EU27", "time": str(int(year)), "measure": m, "value": round(float(lo), 3), "stat": "min"})
    return chart(
        id="e2-control-internet",
        lens="elige", theme="ia-digital",
        title={"es": "China adopta tecnología bajo control estatal. Europa elige otro camino",
               "en": "China adopts technology under state control. Europe takes another path"},
        subtitle={"es": "Grado en que el Gobierno filtra internet y censura las redes sociales en la práctica (valores altos = menos control)",
                  "en": "Extent to which the government filters the internet and censors social media in practice (higher = less control)"},
        unit={"es": "índice V-Dem (estimación del modelo de medición)", "en": "V-Dem index (measurement model estimate)"},
        source={"name": "V-Dem, Digital Society Project (v16)", "dataset": "vdem.RData",
                "url": "https://www.v-dem.net/our-work/collaborations/digital-society-project/",
                "license": "CC BY-SA 4.0"},
        notes={"es": ["Índices elaborados a partir de encuestas a expertos por país. La escala no tiene límites fijos: aproximadamente entre -4 (control total) y +4 (sin control).",
                      "Para la UE se muestra la mediana de los 27 países y el valor del país con más control (stat=min).",
                      "Licencia CC BY-SA: los datos derivados deben compartirse con la misma licencia."],
               "en": ["Indices built from country expert surveys. The scale is unbounded, roughly from -4 (full control) to +4 (no control).",
                      "For the EU, the median of the 27 countries and the most controlled country (stat=min) are shown.",
                      "CC BY-SA licence: derived data must be shared under the same licence."]},
        rows=sorted(out, key=lambda r: (r["measure"], r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"measure": VDEM_MEASURES}},
    )


ACCESS_GROUPS = {
    "abierto": {"es": "Pesos abiertos", "en": "Open weights"},
    "api": {"es": "Acceso por API o web", "en": "API or hosted access"},
    "cerrado": {"es": "No publicado", "en": "Unreleased"},
    "desconocido": {"es": "Sin dato", "en": "Unknown"},
}


def _access_group(value: str) -> str:
    if value.startswith("Open weights"):
        return "abierto"
    if value in ("API access", "Hosted access (no API)", "Limited access"):
        return "api"
    if value == "Unreleased":
        return "cerrado"
    return "desconocido"


def modelos_abiertos(since: int = 2023):
    counts = {}
    for m in sources.epoch_models():
        year = m["Publication date"][:4]
        if not year.isdigit() or int(year) < since:
            continue
        g = _access_group(m["Model accessibility"])
        for b in epoch_blocs(m):
            counts[(b, g)] = counts.get((b, g), 0) + 1
    out = []
    for b in EPOCH_BLOCS:
        total = sum(counts.get((b, g), 0) for g in ACCESS_GROUPS)
        for g in ACCESS_GROUPS:
            n = counts.get((b, g), 0)
            out.append({"geo": b, "time": f"{since}+", "access": g, "value": round(100 * n / total, 1) if total else 0.0,
                        "count": n, "total": total})
    return chart(
        id="e3-modelos-abiertos",
        lens="elige", theme="ia-digital",
        title={"es": "¿Apuesta Europa por la IA abierta?",
               "en": "Is Europe betting on open AI?"},
        subtitle={"es": f"Modelos de IA destacados desde {since} según cómo se publican, en % del total de cada bloque",
                  "en": f"Notable AI models since {since} by release type, as % of each bloc's total"},
        unit={"es": "% de los modelos del bloque", "en": "% of the bloc's models"},
        source={"name": "Epoch AI, Data on AI Models", "dataset": "notable_ai_models.csv",
                "url": "https://epoch.ai/data/ai-models", "license": "CC BY 4.0"},
        notes={"es": ["Regla 'participa': un modelo cuenta para cada bloque con al menos una organización participante.",
                      "La UE tiene pocos modelos destacados en el periodo: los porcentajes se basan en muestras pequeñas (ver 'total')."],
               "en": ["'participa' rule: a model counts for every bloc with at least one participating organisation.",
                      "The EU has few notable models in the period: shares rest on small samples (see 'total')."]},
        rows=out,
        geos=geo.geo_table(["USA", "CHN", "EU27", "GBR"]),
        extra={"dimensions": {"access": ACCESS_GROUPS}},
    )


BUILDERS = [motivos_no_ia_generativa, control_internet, modelos_abiertos]
