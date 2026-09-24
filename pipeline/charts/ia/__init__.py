from . import dentro, elige, gigantes

THEME = {"id": "ia-digital", "es": "IA y digital", "en": "AI and digital"}
ORDER = 1

BUILDERS = [*gigantes.BUILDERS, *elige.BUILDERS, *dentro.BUILDERS]
