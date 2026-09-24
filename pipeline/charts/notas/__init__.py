"""Notas: una o dos gráficas sobre un tema ya existente. Un módulo por nota (n01_vivienda.py...)."""

import importlib
import pkgutil

ORDER = 100
BUILDERS = []
for info in sorted(pkgutil.iter_modules(__path__), key=lambda i: i.name):
    BUILDERS.extend(importlib.import_module(f"{__name__}.{info.name}").BUILDERS)
