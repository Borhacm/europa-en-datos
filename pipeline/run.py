"""Genera los JSON de los gráficos en data/charts/.

Uso (desde pipeline/):
    uv run run.py                  todos los gráficos (usa la caché de data/raw)
    uv run run.py --refresh        vuelve a descargar todo
    uv run run.py --only sanidad   solo los gráficos de los módulos cuyo nombre contiene "sanidad"
                                   (un tema: --only sanidad; una nota: --only n01)

Una ejecución con --only no modifica los demás gráficos.
"""

import sys
import traceback

from charts import BUILDERS
from lib import http
from lib.output import write


def main(args: list[str]) -> int:
    http.REFRESH = "--refresh" in args
    only = args[args.index("--only") + 1] if "--only" in args else None

    builders = [b for b in BUILDERS if not only or only in b.__module__]
    if only and not builders:
        print(f"ERR ningún módulo contiene '{only}'")
        return 1

    built, failed = [], []
    for build in builders:
        try:
            c = build()
        except Exception:
            failed.append(f"{build.__module__}.{build.__name__}")
            traceback.print_exc()
            continue
        built.append(c)
        print(f"ok  {c['id']:<32} {len(c['rows']):>6} filas")

    write(built)
    for name in failed:
        print(f"ERR {name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
