from . import dentro, elige, gigantes

THEME = {"id": "libertades", "es": "Libertades, bienestar y clima", "en": "Freedoms, well-being and climate"}
ORDER = 4

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
