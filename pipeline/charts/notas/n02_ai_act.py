"""N02. El AI Act: ¿frena la regulación el uso de la IA en las empresas?"""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat

# Motivos para no usar IA, preguntados a las empresas que se plantearon usarla y no lo hicieron
REASONS = {
    "E_AI_BLE": {"es": "Faltan conocimientos", "en": "Lack of expertise"},
    "E_AI_BLEG": {"es": "Consecuencias legales poco claras", "en": "Unclear legal consequences"},
    "E_AI_BCDP": {"es": "Protección de datos y privacidad", "en": "Data protection and privacy"},
    "E_AI_BDDT": {"es": "Datos no disponibles o de mala calidad", "en": "Data unavailable or poor quality"},
    "E_AI_BINC": {"es": "Incompatible con sus sistemas", "en": "Incompatible with their systems"},
    "E_AI_BCST": {"es": "Costes demasiado altos", "en": "Costs too high"},
    "E_AI_BEC": {"es": "Consideraciones éticas", "en": "Ethical considerations"},
    "E_AI_BNU": {"es": "No le resulta útil", "en": "Not useful for the company"},
}
UNIT = "PC_ENT_AI_EC"
NOTES = {
    "es": ["Pregunta hecha a las empresas que no usan IA pero se plantearon usarla. Respuesta múltiple: los porcentajes suman más de 100.",
           "Empresas de 10 o más empleados, sin el sector financiero."],
    "en": ["Question asked of enterprises that do not use AI but considered using it. Multiple answers: shares add up to more than 100.",
           "Enterprises with 10 or more employees, excluding the financial sector."],
}


def _rows(indic, years):
    rows = sources.eurostat("isoc_eb_ai", unit=UNIT, size_emp="GE10", indic_is=indic, time=years)
    return from_eurostat(rows, ["indic_is"])


def frenos():
    out = _rows(list(REASONS), ["2025"])
    for r in out:
        r["reason"] = r.pop("indic_is")
    return chart(
        id="n02-ia-frenos",
        lens="elige", theme="ia-digital",
        title={"es": "La falta de conocimientos sigue siendo el primer freno a la IA; la incertidumbre legal ya es el segundo",
               "en": "Lack of expertise is still the main barrier to AI; legal uncertainty is now the second"},
        subtitle={"es": "Motivos para no usar IA, en % de las empresas que se plantearon usarla y no lo hicieron, 2025",
                  "en": "Reasons for not using AI, as % of enterprises that considered using it but did not, 2025"},
        unit={"es": "% de las empresas que se plantearon usar IA", "en": "% of enterprises that considered AI"},
        source=eurostat_source("isoc_eb_ai"),
        notes=NOTES,
        rows=sorted(out, key=lambda r: (r["geo"], r["reason"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"reason": REASONS}},
    )


def incertidumbre_legal():
    out = _rows("E_AI_BLEG", ["2023", "2025"])
    for r in out:
        r.pop("indic_is")
    return chart(
        id="n02-ia-incertidumbre-legal",
        lens="elige", theme="ia-digital",
        title={"es": "La incertidumbre legal frena a más empresas que en 2023",
               "en": "Legal uncertainty holds back more companies than in 2023"},
        subtitle={"es": "Empresas que no usan IA por la falta de claridad sobre sus consecuencias legales, en % de las que se plantearon usarla, 2023 y 2025",
                  "en": "Enterprises not using AI because of unclear legal consequences, as % of those that considered it, 2023 and 2025"},
        unit={"es": "% de las empresas que se plantearon usar IA", "en": "% of enterprises that considered AI"},
        source=eurostat_source("isoc_eb_ai"),
        notes=NOTES,
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [frenos, incertidumbre_legal]
