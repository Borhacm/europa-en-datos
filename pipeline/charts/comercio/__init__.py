from . import dentro, elige, gigantes

THEME = {"id": "comercio", "es": "Comercio y dependencias", "en": "Trade and dependencies"}
ORDER = 2

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
