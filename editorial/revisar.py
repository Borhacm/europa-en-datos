"""Comprobaciones editoriales antes de publicar (pasos 3b, 6 y 8b del manual). Solo usa la biblioteca estándar.

  python3 editorial/revisar.py solapes <dataset o palabra> [...]
      Gráficos ya publicados que usan ese dataset o hablan de eso en el título.
      Úsalo al elegir los gráficos: un hallazgo publicado no se repite, se enlaza.

  python3 editorial/revisar.py pieza <tema_id o id de nota>
      Revisa una pieza: filtros de cada consulta frente al subtítulo, cifras repetidas entre
      titulares y entre miradas, gráficos sin notas, títulos en pregunta y datasets que ya usan
      otras piezas.

  python3 editorial/revisar.py verificada <tema_id o id de nota>
      Apunta en editorial/verificadas.json la huella de los datos de cada gráfico de la pieza.
      Ejecútalo cuando hayas comprobado sus cifras (paso 5), antes del commit.

  python3 editorial/revisar.py todo
      Repasa todas las piezas: avisos de la revisión y gráficos cuyos datos han cambiado desde
      la última verificación. Úsalo después de actualizar los datos: si las filas cambian, los
      titulares y los textos de esa pieza se vuelven a comprobar.
"""

import hashlib

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHARTS = ROOT / "data" / "charts"
CONTENT = ROOT / "web" / "src" / "content"
PIPELINE = ROOT / "pipeline" / "charts"
VERIFIED = ROOT / "editorial" / "verificadas.json"
# Cifras en español: "12,5 %", "40 %", "3,5"
NUM = re.compile(r"\d+(?:\.\d{3})*(?:,\d+)?\s%|\d+,\d+")


def published() -> dict[str, dict]:
    return {p.stem: json.loads(p.read_text()) for p in sorted(CHARTS.glob("*.json"))}


def owner_of() -> dict[str, str]:
    """Gráfico -> pieza que lo configura (web/src/content/charts/<pieza>.ts)."""
    out = {}
    for f in (CONTENT / "charts").glob("*.ts"):
        for cid in re.findall(r'^\s*"([a-z0-9-]+)":\s*\{', f.read_text(), re.M):
            out[cid] = f.stem
    return out


def dataset(c: dict) -> str:
    return str(c.get("source", {}).get("dataset", ""))


def solapes(terms: list[str]) -> None:
    owners = owner_of()
    for term in terms:
        t = term.lower()
        hits = [(cid, c) for cid, c in published().items()
                if t in dataset(c).lower() or t in c["title"]["es"].lower() or t in c["subtitle"]["es"].lower()]
        print(f"\n«{term}»: {len(hits)} gráficos publicados")
        for cid, c in hits:
            print(f"  {owners.get(cid, '?'):14s} {cid:32s} [{dataset(c)}] {c['title']['es']}")


def _shown(v) -> set[str]:
    """Formas en que un valor de las filas puede aparecer en un titular: 12,5 / 12 / 13."""
    if not isinstance(v, (int, float)):
        return set()
    out = {f"{round(v):d}", f"{v:.1f}".replace(".", ","), f"{v:.2f}".replace(".", ",")}
    return out | {x.rstrip("0").rstrip(",") for x in out if "," in x}


def stale_titles(c: dict) -> list[str]:
    """Cifras del titular en español que no salen tal cual de las filas (pueden ser derivadas)."""
    seen = set()
    for r in c.get("rows", []):
        for k, v in r.items():
            seen |= _shown(v)
            if k == "time":
                seen.add(str(v)[:4])
    nums = [n.replace(".", "") for n in re.findall(r"\d+(?:\.\d{3})*(?:,\d+)?", c["title"]["es"])]
    return [n for n in nums if n not in seen and not re.fullmatch(r"(19|20)\d\d", n)]


def fingerprint(c: dict) -> str:
    return hashlib.sha256(json.dumps(c.get("rows", []), sort_keys=True).encode()).hexdigest()[:16]


def verified() -> dict[str, str]:
    return json.loads(VERIFIED.read_text()) if VERIFIED.exists() else {}


def verificada(pid: str) -> None:
    charts, done = published(), verified()
    mine = sorted(cid for cid, o in owner_of().items() if o == pid and cid in charts)
    if not mine:
        sys.exit(f"No hay gráficos configurados en web/src/content/charts/{pid}.ts")
    for cid in mine:
        done[cid] = fingerprint(charts[cid])
    VERIFIED.write_text(json.dumps(dict(sorted(done.items())), indent=1, ensure_ascii=False) + "\n")
    print(f"{len(mine)} gráficos de {pid} apuntados como verificados")


def pieza(pid: str, quiet: bool = False) -> int:
    charts = published()
    owners = owner_of()
    mine = [cid for cid, o in owners.items() if o == pid and cid in charts]
    if not mine:
        sys.exit(f"No hay gráficos configurados en web/src/content/charts/{pid}.ts")
    problems = 0
    if quiet:
        print_ = print
        globals()["print"] = lambda *a, **k: None

    print("\n1. Filtros de cada consulta (compáralos con el subtítulo: impuestos, banda, unidad, edad, año)")
    files = sorted((PIPELINE / pid).glob("*.py")) if (PIPELINE / pid).is_dir() else sorted((PIPELINE / "notas").glob(f"{pid}_*.py"))
    for f in files:
        lines = f.read_text().splitlines()
        for i, line in enumerate(lines):
            if re.search(r"sources\.\w+\(|_FILTERS\s*=|FILTERS\s*=|worldbank_rows\(|_blocs\(", line):
                # La consulta completa, aunque ocupe varias líneas
                call, j = line.strip(), i
                while call.count("(") > call.count(")") and j + 1 < len(lines):
                    j += 1
                    call += " " + lines[j].strip()
                print(f"   {f.name}: {call}")
    for cid in mine:
        print(f"   {cid}: {charts[cid]['subtitle']['es']}")

    print("\n2. Titulares")
    by_num = defaultdict(list)
    for cid in mine:
        c = charts[cid]
        title = c["title"]["es"]
        for n in set(NUM.findall(title)):
            by_num[n].append(cid)
        if title.rstrip().endswith("?"):
            print(f"   AVISO {cid}: el título es una pregunta; debe afirmar el hallazgo")
            problems += 1
        if not c["notes"]["es"]:
            print(f"   AVISO {cid}: sin notas metodológicas")
            problems += 1
    for cid in mine:
        derived = stale_titles(charts[cid])
        if derived:
            print(f"   REVISAR {cid}: {', '.join(derived)} no está tal cual en las filas; si es un cálculo, compruébalo con los datos actuales")
    for n, ids in by_num.items():
        if len(ids) > 1:
            print(f"   AVISO la cifra «{n}» está en el titular de {', '.join(ids)}")
            problems += 1

    print("\n3. Cifras repetidas entre miradas (texto en español del tema)")
    theme_file = CONTENT / "themes" / f"{pid}.ts"
    if theme_file.exists():
        text = theme_file.read_text()
        parts = re.split(r"^\s{4}(gigantes|elige|dentro):\s*\{", text, flags=re.M)
        lens_nums = {parts[i]: set(NUM.findall(parts[i + 1])) for i in range(1, len(parts) - 1, 2)}
        seen = defaultdict(list)
        for lens, nums in lens_nums.items():
            for n in nums:
                seen[n].append(lens)
        for n, lenses in sorted(seen.items()):
            if len(lenses) > 1:
                print(f"   REVISAR «{n}» aparece en {', '.join(lenses)}: ¿es el mismo hallazgo contado dos veces?")
                problems += 1
    else:
        print("   (es una nota: no tiene miradas)")

    print("\n4. Datasets que ya usan otras piezas (no repitas su hallazgo: enlázalo)")
    for cid in mine:
        ds = dataset(charts[cid])
        if not ds:
            continue
        others = [(o, c) for o, c in charts.items() if o not in mine and dataset(c) == ds]
        for o, c in others:
            print(f"   {cid} [{ds}] también en {owners.get(o, '?')}/{o}: {c['title']['es']}")

    print(f"\n{problems} avisos. Los de los apartados 1 y 4 se revisan a mano.")
    if quiet:
        globals()["print"] = print_
    return problems


def todo() -> None:
    charts, done, owners = published(), verified(), owner_of()
    pieces = sorted(set(owners.values()))
    total = changed_total = 0
    for pid in pieces:
        n = pieza(pid, quiet=True)
        mine = sorted(cid for cid, o in owners.items() if o == pid and cid in charts)
        changed = [cid for cid in mine if done.get(cid) != fingerprint(charts[cid])]
        total += n
        changed_total += len(changed)
        flag = "ok " if not n and not changed else "-> "
        print(f"{flag}{pid:14s} {n} avisos, {len(changed)} gráficos con datos sin verificar")
        for cid in changed:
            print(f"      {cid}: {'cambió desde la verificación' if cid in done else 'nunca verificado'}: {charts[cid]['title']['es']}")
    print(f"\n{total} avisos y {changed_total} gráficos por verificar en {len(pieces)} piezas.")
    print("Detalle: python3 editorial/revisar.py pieza <id>. Tras comprobar las cifras: revisar.py verificada <id>.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "todo":
        todo()
    elif cmd == "verificada" and len(sys.argv) > 2:
        verificada(sys.argv[2])
    elif cmd in ("solapes", "pieza") and len(sys.argv) > 2:
        solapes(sys.argv[2:]) if cmd == "solapes" else pieza(sys.argv[2])
    else:
        sys.exit(__doc__)
