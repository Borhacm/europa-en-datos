"""Descubre los paquetes de temas (con THEME y BUILDERS) y el paquete de notas.

Para añadir un tema basta con crear charts/<tema>/ con su __init__.py: no hay que tocar este archivo.
"""

import importlib
import pkgutil

from lib.output import THEMES

BUILDERS = []
_themes = []
for info in pkgutil.iter_modules(__path__):
    if not info.ispkg:
        continue
    module = importlib.import_module(f"{__name__}.{info.name}")
    theme = getattr(module, "THEME", None)
    if theme:
        THEMES[theme["id"]] = {"es": theme["es"], "en": theme["en"]}
    _themes.append((getattr(module, "ORDER", 99), info.name, module))

# Orden estable: temas por su ORDER y, dentro de cada tema, por mirada
for _, _, module in sorted(_themes, key=lambda t: (t[0], t[1])):
    BUILDERS.extend(getattr(module, "BUILDERS", []))
