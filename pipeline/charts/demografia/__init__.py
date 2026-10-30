from . import dentro, elige, gigantes

THEME = {"id": "demografia", "es": "Demografía y migración", "en": "Population and migration"}
ORDER = 13

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
