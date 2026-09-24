"""Códigos geográficos. Canónico: ISO3 para países y 'EU27' para la UE, con nombres en ES y EN."""

# ISO3: (código Eurostat, nombre ES, nombre EN, es miembro de la UE)
COUNTRIES = {
    "AUT": ("AT", "Austria", "Austria", True),
    "BEL": ("BE", "Bélgica", "Belgium", True),
    "BGR": ("BG", "Bulgaria", "Bulgaria", True),
    "HRV": ("HR", "Croacia", "Croatia", True),
    "CYP": ("CY", "Chipre", "Cyprus", True),
    "CZE": ("CZ", "Chequia", "Czechia", True),
    "DNK": ("DK", "Dinamarca", "Denmark", True),
    "EST": ("EE", "Estonia", "Estonia", True),
    "FIN": ("FI", "Finlandia", "Finland", True),
    "FRA": ("FR", "Francia", "France", True),
    "DEU": ("DE", "Alemania", "Germany", True),
    "GRC": ("EL", "Grecia", "Greece", True),
    "HUN": ("HU", "Hungría", "Hungary", True),
    "IRL": ("IE", "Irlanda", "Ireland", True),
    "ITA": ("IT", "Italia", "Italy", True),
    "LVA": ("LV", "Letonia", "Latvia", True),
    "LTU": ("LT", "Lituania", "Lithuania", True),
    "LUX": ("LU", "Luxemburgo", "Luxembourg", True),
    "MLT": ("MT", "Malta", "Malta", True),
    "NLD": ("NL", "Países Bajos", "Netherlands", True),
    "POL": ("PL", "Polonia", "Poland", True),
    "PRT": ("PT", "Portugal", "Portugal", True),
    "ROU": ("RO", "Rumanía", "Romania", True),
    "SVK": ("SK", "Eslovaquia", "Slovakia", True),
    "SVN": ("SI", "Eslovenia", "Slovenia", True),
    "ESP": ("ES", "España", "Spain", True),
    "SWE": ("SE", "Suecia", "Sweden", True),
    # Europa fuera de la UE
    "NOR": ("NO", "Noruega", "Norway", False),
    "ISL": ("IS", "Islandia", "Iceland", False),
    "CHE": ("CH", "Suiza", "Switzerland", False),
    "GBR": ("UK", "Reino Unido", "United Kingdom", False),
    "TUR": ("TR", "Turquía", "Türkiye", False),
    "SRB": ("RS", "Serbia", "Serbia", False),
    "MNE": ("ME", "Montenegro", "Montenegro", False),
    "BIH": ("BA", "Bosnia y Herzegovina", "Bosnia and Herzegovina", False),
    "ALB": ("AL", "Albania", "Albania", False),
    "MKD": ("MK", "Macedonia del Norte", "North Macedonia", False),
    "XKX": ("XK", "Kosovo", "Kosovo", False),
    "UKR": ("UA", "Ucrania", "Ukraine", False),
    "MDA": ("MD", "Moldavia", "Moldova", False),
    # Resto del mundo
    "USA": (None, "Estados Unidos", "United States", False),
    "CHN": (None, "China", "China", False),
    "JPN": (None, "Japón", "Japan", False),
    "KOR": (None, "Corea del Sur", "South Korea", False),
}

EU27 = [iso3 for iso3, c in COUNTRIES.items() if c[3]]
EU_NAMES = {"es": "Unión Europea", "en": "European Union"}

_FROM_EUROSTAT = {c[0]: iso3 for iso3, c in COUNTRIES.items() if c[0]}
_AGGREGATES = {"EU27_2020": "EU27", "EU27": "EU27", "EUU": "EU27"}
# Códigos de socios comerciales de Eurostat fuera de Europa (China sin Hong Kong)
_PARTNERS = {"US": "USA", "CN_X_HK": "CHN", "JP": "JPN", "KR": "KOR"}
# Agregado UE-27 en la OIT
_ILO = {"X92": "EU27"}


def from_eurostat(code: str) -> str | None:
    """Código Eurostat a canónico. Devuelve None para agregados que no usamos (zona euro, etc.)."""
    return _AGGREGATES.get(code) or _PARTNERS.get(code) or _FROM_EUROSTAT.get(code)


def from_iso3(code: str) -> str | None:
    return _AGGREGATES.get(code) or _ILO.get(code) or (code if code in COUNTRIES else None)


def name(code: str, lang: str) -> str:
    if code == "EU27":
        return EU_NAMES[lang]
    return COUNTRIES[code][1 if lang == "es" else 2]


def geo_table(codes) -> dict:
    """Tabla de nombres para incluir en cada JSON de salida."""
    out = {}
    for c in sorted(set(codes)):
        out[c] = {"es": name(c, "es"), "en": name(c, "en"),
                  "eu": c == "EU27" or (c in COUNTRIES and COUNTRIES[c][3]),
                  "aggregate": c == "EU27"}
    return out
