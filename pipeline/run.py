"""Genera data/charts/*.json y data/index.json.

Uso (desde pipeline/):
    uv run run.py            usa la caché de data/raw si existe
    uv run run.py --refresh  vuelve a descargar todo
"""

import sys
import traceback

from charts import BUILDERS
from lib import http
from lib.output import write


def main(args: list[str]) -> int:
    http.REFRESH = "--refresh" in args

    built, failed = [], []
    for build in BUILDERS:
        try:
            c = build()
        except Exception:
            failed.append(build.__name__)
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
