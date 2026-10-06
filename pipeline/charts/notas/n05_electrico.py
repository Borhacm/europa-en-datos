"""N05. Coche eléctrico: qué parte de los coches nuevos ya lo son."""

from lib import geo, sources
from lib.output import chart

from ..common import eurostat_source

FIRST, LAST = "2013", "2025"
PLUGIN = ["ELC_PET_PI", "ELC_DIE_PI"]
FUELS = {
    "ELC": {"es": "Eléctricos de batería", "en": "Battery electric"},
    "ELC_PLUG": {"es": "Eléctricos e híbridos enchufables", "en": "Battery electric and plug-in hybrids"},
}

NOTES_ES = [
    "Cuota sobre el total de turismos nuevos matriculados en el año. Eléctricos de batería: solo con motor eléctrico. No incluye los híbridos no enchufables ni los de hidrógeno.",
    "Eurostat calcula el agregado de la UE como suma de los 27 países.",
]
NOTES_EN = [
    "Share of all new passenger cars registered in the year. Battery electric: electric motor only. Excludes non-plug-in hybrids and hydrogen cars.",
    "Eurostat computes the EU aggregate as the sum of the 27 countries.",
]


def _by_geo_time(times, extra=()):
    rows = sources.eurostat("road_eqr_carpda", unit="NR", mot_nrg=["TOTAL", "ELC", *PLUGIN], time=times)
    data, flags = {}, {}
    for r in rows:
        code = geo.from_eurostat(r["geo"])
        if code in geo.EU27 or code == "EU27" or code in extra:
            data.setdefault((code, r["time"]), {})[r["mot_nrg"]] = r["value"]
            if r.get("flag") and r["mot_nrg"] in ("TOTAL", "ELC"):
                flags[(code, r["time"])] = r["flag"]
    return data, flags


def _row(code, time, value, flag):
    row = {"geo": code, "time": time, "value": round(value, 2)}
    if flag:
        row["flag"] = flag
    return row


def cuota_2025():
    data, flags = _by_geo_time(LAST, extra=("NOR",))
    out = []
    for (code, time), v in data.items():
        if "TOTAL" not in v or "ELC" not in v:
            continue
        flag = flags.get((code, time))
        out.append({**_row(code, time, 100 * v["ELC"] / v["TOTAL"], flag), "fuel": "ELC"})
        if all(k in v for k in PLUGIN) or code == "NOR":
            plug = v["ELC"] + sum(v.get(k, 0) for k in PLUGIN)
            out.append({**_row(code, time, 100 * plug / v["TOTAL"], flag), "fuel": "ELC_PLUG"})
    return chart(
        id="n05-electricos-cuota",
        lens="elige", theme="libertades",
        title={"es": "En Dinamarca, más de dos de cada tres coches nuevos son eléctricos; en Croacia, menos de dos de cada cien",
               "en": "In Denmark, more than two in three new cars are electric; in Croatia, fewer than two in a hundred"},
        subtitle={"es": "Turismos eléctricos de batería, en % de los turismos nuevos matriculados, 2025",
                  "en": "Battery electric cars as a % of new passenger car registrations, 2025"},
        unit={"es": "% de los turismos nuevos", "en": "% of new passenger cars"},
        source=eurostat_source("road_eqr_carpda"),
        notes={"es": NOTES_ES + ["Híbridos enchufables: de gasolina o de diésel con batería que se recarga en la red.",
                                 "Noruega no es miembro de la UE; se incluye como referencia.",
                                 "Portugal: datos provisionales. Eslovenia: ruptura de serie en 2025. Varios países tienen alguna categoría marcada por Eurostat como información adicional en sus metadatos."],
               "en": NOTES_EN + ["Plug-in hybrids: petrol or diesel cars with a battery charged from the grid.",
                                 "Norway is not an EU member; it is shown for reference.",
                                 "Portugal: provisional. Slovenia: break in series in 2025. Several countries have some categories flagged by Eurostat with additional information in the metadata."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["fuel"])),
        geos=geo.geo_table(r["geo"] for r in out),
        extra={"dimensions": {"fuel": FUELS}},
    )


def evolucion():
    times = [str(y) for y in range(int(FIRST), int(LAST) + 1)]
    data, flags = _by_geo_time(times)
    out = [_row(code, time, 100 * v["ELC"] / v["TOTAL"], flags.get((code, time)))
           for (code, time), v in data.items() if "TOTAL" in v and "ELC" in v and v["TOTAL"]]
    return chart(
        id="n05-electricos-evolucion",
        lens="elige", theme="libertades",
        title={"es": "En la UE, la cuota del coche eléctrico pasó del 1,9 % en 2019 al 17,3 % en 2025",
               "en": "In the EU, the electric car share rose from 1.9% in 2019 to 17.3% in 2025"},
        subtitle={"es": "Turismos eléctricos de batería, en % de los turismos nuevos matriculados, 2013-2025",
                  "en": "Battery electric cars as a % of new passenger car registrations, 2013-2025"},
        unit={"es": "% de los turismos nuevos", "en": "% of new passenger cars"},
        source=eurostat_source("road_eqr_carpda"),
        notes={"es": NOTES_ES + ["En 2024 la cuota de la UE bajó por primera vez en la serie (del 14,5 % al 13,5 %). Alemania, el mayor mercado, dejó de aceptar solicitudes de su ayuda a la compra el 17 de diciembre de 2023."],
               "en": NOTES_EN + ["In 2024 the EU share fell for the first time in the series (from 14.5% to 13.5%). Germany, the largest market, stopped accepting applications for its purchase subsidy on 17 December 2023."]},
        rows=sorted(out, key=lambda r: (r["geo"], r["time"])),
        geos=geo.geo_table(r["geo"] for r in out),
    )


BUILDERS = [cuota_2025, evolucion]
