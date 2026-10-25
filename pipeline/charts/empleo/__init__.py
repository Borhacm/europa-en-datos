from . import dentro, elige, gigantes

THEME = {"id": "empleo", "es": "Empleo y jóvenes", "en": "Jobs and young people"}
ORDER = 12

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
