from . import dentro, elige, gigantes

THEME = {"id": "sanidad", "es": "Sanidad", "en": "Health"}
ORDER = 5

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
