from . import dentro, elige, gigantes

THEME = {"id": "educacion", "es": "Educación y talento", "en": "Education and talent"}
ORDER = 14

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
