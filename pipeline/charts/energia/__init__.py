from . import dentro, elige, gigantes

THEME = {"id": "energia", "es": "Energía", "en": "Energy"}
ORDER = 8

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
