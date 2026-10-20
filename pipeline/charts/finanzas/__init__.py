from . import dentro, elige, gigantes

THEME = {"id": "finanzas", "es": "Finanzas públicas", "en": "Public finances"}
ORDER = 9

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
