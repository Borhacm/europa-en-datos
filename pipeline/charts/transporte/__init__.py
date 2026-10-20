from . import dentro, elige, gigantes

THEME = {"id": "transporte", "es": "Transporte y transición verde", "en": "Transport and the green transition"}
ORDER = 11

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
