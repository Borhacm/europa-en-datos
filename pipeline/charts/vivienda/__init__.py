from . import dentro, elige, gigantes

THEME = {"id": "vivienda", "es": "Vivienda", "en": "Housing"}
ORDER = 7

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
