from . import dentro, elige, gigantes

THEME = {"id": "defensa", "es": "Defensa y seguridad", "en": "Defence and security"}
ORDER = 10

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
