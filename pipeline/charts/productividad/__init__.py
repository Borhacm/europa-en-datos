from . import dentro, elige, gigantes

THEME = {"id": "productividad", "es": "Productividad y crecimiento", "en": "Productivity and growth"}
ORDER = 3

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
