from . import dentro, elige, gigantes

THEME = {"id": "dinero", "es": "Dinero y pagos", "en": "Money and payments"}
ORDER = 6

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
