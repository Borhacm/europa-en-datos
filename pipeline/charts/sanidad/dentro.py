"""Sanidad. Mirada 3: médicos y necesidades médicas no cubiertas en los 27."""

from collections import Counter

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source, from_eurostat


def medicos():
    rows = sources.eurostat("hlth_rs_prs2", med_spec="PHYS", unit="P_HTHAB", wstatus=["PRACT", "PACT"])
    # Último año con médicos en ejercicio de al menos 20 países de la UE
    counts = Counter(r["time"] for r in rows if r["wstatus"] == "PRACT" and geo.from_eurostat(r["geo"]) in geo.EU27)
    latest = max(t for t, n in counts.items() if n >= 20)
    rows = [r for r in rows if r["time"] == latest]
    # Médicos en ejercicio; si un país no los publica, médicos profesionalmente activos
    practising = {r["geo"] for r in rows if r["wstatus"] == "PRACT"}
    rows = [r for r in rows if r["wstatus"] == "PRACT" or (r["wstatus"] == "PACT" and r["geo"] not in practising)]
    out = [r for r in from_eurostat(rows, ["wstatus"]) if r["geo"] in geo.EU27]
    return chart(
        id="sad1-medicos",
        lens="dentro", theme="sanidad",
        title={"es": "En Grecia, Italia o Austria hay más de 560 médicos por cada 100.000 habitantes; en Letonia o Bélgica, unos 340",
               "en": "Greece, Italy and Austria have more than 560 doctors per 100,000 people; Latvia and Belgium, about 340"},
        subtitle={"es": f"Médicos en ejercicio por cada 100.000 habitantes, {latest}",
                  "en": f"Practising physicians per 100,000 people, {latest}"},
        unit={"es": "por 100.000 habitantes", "en": "per 100,000 people"},
        source=eurostat_source("hlth_rs_prs2"),
        notes={"es": ["Médicos que atienden directamente a pacientes. Eslovaquia no publica ese dato: se usan los médicos profesionalmente activos, que incluyen también a los que trabajan en gestión o investigación.",
                      "Grecia y Portugal solo publican médicos en ejercicio desde 2023, y otros países, como Italia o Francia, tienen saltos en la serie: por eso se muestra solo el último año.",
                      "Eurostat marca el dato de Bélgica con una ruptura de serie y el de Eslovenia con una definición distinta; el de España es una estimación.",
                      "No hay un dato agregado de la UE para este indicador."],
               "en": ["Physicians who treat patients directly. Slovakia does not publish this figure: professionally active physicians are used instead, which also include those working in management or research.",
                      "Greece and Portugal have only reported practising physicians since 2023, and other countries, such as Italy or France, have jumps in the series: that is why only the latest year is shown.",
                      "Eurostat flags Belgium's figure with a break in series and Slovenia's with a different definition; Spain's is an estimate.",
                      "There is no EU aggregate for this indicator."]},
        rows=sorted(out, key=lambda r: r["geo"]),
        geos=geo.geo_table(r["geo"] for r in out),
    )


REASONS = {
    "TXP_TFAR_WLIST": {"es": "Cualquiera de los tres", "en": "Any of the three"},
    "TXP": {"es": "Demasiado caro", "en": "Too expensive"},
    "WLIST": {"es": "Lista de espera", "en": "Waiting list"},
    "TFAR": {"es": "Demasiado lejos", "en": "Too far"},
}


def necesidades_no_cubiertas():
    rows = sources.eurostat("hlth_silc_08", quant_inc="TOTAL", sex="T", age="Y_GE16", unit="PC", reason=list(REASONS))
    rows = [r for r in rows if r["time"] >= "2015"]
    out = [r for r in from_eurostat(rows, ["reason"]) if r["geo"] in geo.EU27 or r["geo"] == "EU27"]
    return chart(
        id="sad2-necesidades-no-cubiertas",
        lens="dentro", theme="sanidad",
        title={"es": "El precio deja sin atención médica a muchos griegos; las listas de espera, a finlandeses y estonios",
               "en": "Cost keeps many Greeks from getting medical care; waiting lists, many Finns and Estonians"},
        subtitle={"es": "Personas de 16 años o más que dicen no haber recibido un examen o tratamiento médico que necesitaban, por motivo, en %",
                  "en": "People aged 16 and over who report not getting a medical examination or treatment they needed, by reason, in %"},
        unit={"es": "% de la población de 16 años o más", "en": "% of population aged 16 and over"},
        source=eurostat_source("hlth_silc_08"),
        notes={"es": ["Encuesta de condiciones de vida (EU-SILC): es lo que declara cada persona, no un registro de las listas de espera.",
                      "No incluye la atención dental, que se mide aparte.",
                      "La encuesta cambió de base legal en 2021; algunos países tienen rupturas de serie."],
               "en": ["EU Statistics on Income and Living Conditions (EU-SILC): this is what people report, not a record of waiting lists.",
                      "Dental care is excluded; it is measured separately.",
                      "The survey changed its legal basis in 2021; some countries have breaks in series."]},
        rows=sorted(out, key=lambda r: (r["reason"], r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"reason": REASONS}},
    )


BUILDERS = [medicos, necesidades_no_cubiertas]
