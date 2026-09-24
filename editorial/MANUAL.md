# Manual de publicación

Procedimiento para preparar y publicar una **nota** o un **artículo** del [calendario](calendario.yaml). Lo siguen las tareas automáticas y sirve igual para hacerlo a mano.

**La publicación es automática.** Cada ejecución abre un pull request en GitHub (que deja registro de la entrada y de su tabla de verificación) y, cuando todas las comprobaciones pasan, lo fusiona ella misma: al llegar a `main`, Vercel publica la web. Por eso las comprobaciones de este manual no son opcionales: nadie revisa antes de publicar.

## Reglas que no se rompen

- Nunca hagas commit ni push directamente en `main`. Solo fusionas **tu propio** pull request, y solo cuando `npm run check` y la comprobación de Vercel han pasado. Nunca fusiones pull requests ajenos ni borres ramas ajenas.
- Nunca regeneres los datos de otros temas: ejecuta el pipeline siempre con `--only`. Nunca uses `--refresh`.
- No cambies la configuración de Vercel, de GitHub ni la licencia (el proyecto no tiene licencia de código a propósito).
- **Cada cifra y cada afirmación de un título o de un texto tiene que salir de los datos del JSON.** Si no puedes comprobarla, no la escribas. Esta es la regla más importante: en el pasado se colaron titulares como "casi todos los países", "más que nunca" o "uno de cada tres" que los datos no sostenían.
- Si algo falla y no sabes arreglarlo, o tienes dudas serias sobre algún dato, **no publiques**: deja la rama sin fusionar y explica el problema en el resumen final.

## 1. Preparar el repositorio

```bash
cd /Users/bcm/europa-en-datos
git status --short          # debe estar vacío; si no, para y explica qué hay
git checkout main && git pull --ff-only
```

## 2. Elegir la entrada

Lee `editorial/calendario.yaml` y toma la **primera** entrada del tipo que te toca (nota o artículo) que no esté hecha:

- está hecha si existe `web/src/content/notes/<id>.ts` (notas) o `web/src/content/themes/<tema_id>.ts` (artículos) en `main`;
- o si hay un pull request abierto de una rama que empieza por `editorial/<id>`: `gh pr list --state open --json headRefName`.

Si no queda ninguna, termina y dilo.

Crea la rama: `git checkout -b editorial/<id>-<palabra-clave>` (por ejemplo `editorial/n02-luz`).

## 3. Buscar y comprobar los datos

- Empieza por las fuentes del calendario, pero compruébalas: que existen, qué dimensiones tienen y cuál es el **último año con datos para casi todos los países**. Si una fuente no sirve, busca otra fiable (Eurostat, OCDE, Banco Mundial, OIT, FMI, V-Dem) y explícalo en el pull request.
- Lectores disponibles en `pipeline/lib/sources.py`: `eurostat`, `oecd`, `worldbank`, `ilo`, `vdem`, `epoch_models`. Funciones comunes en `pipeline/charts/common.py`: `from_eurostat`, `eurostat_source`, `worldbank_rows`, `worldbank_source`, `vdem_with_eu`, `nuts_map` (mapas regionales).
- Para comparar bloques: la UE es `EU27` (UE de 27, desde 2020), EE. UU. `USA`, China `CHN`. Eurostat usa `EU27_2020`, `US` y `CN_X_HK`; el Banco Mundial `EUU`; la OIT `X92`. `pipeline/lib/geo.py` los traduce.
- Las series con proyecciones (la OIT, por ejemplo) se cortan en el último año observado.

## 4. Escribir los gráficos (pipeline)

Mira un ejemplo antes de empezar: `pipeline/charts/notas/n01_vivienda.py` (nota) o `pipeline/charts/comercio/` (tema).

**Nota:** un archivo `pipeline/charts/notas/<id>_<palabra>.py` con `BUILDERS`. Uno o dos gráficos. Identificador de cada gráfico: `<id>-<palabras>` (por ejemplo `n02-precio-luz`). `lens` = la mirada del calendario; `theme` = el tema del calendario.

**Artículo:** un paquete `pipeline/charts/<tema_id>/` con:
- `__init__.py` con `THEME = {"id": "<tema_id>", "es": "...", "en": "..."}`, `ORDER` (el siguiente número tras los temas existentes) y `BUILDERS`;
- `gigantes.py`, `elige.py` y `dentro.py`, con **dos gráficos por mirada** (seis en total; como mínimo uno por mirada).
- Identificadores: `<codigo en minúsculas><g|e|d><n>-<palabras>`, por ejemplo `sag1-gasto-sanitario`, `sae1-...`, `sad2-...`.

Cada gráfico lleva título y subtítulo en ES y EN, unidad, fuente con licencia, notas metodológicas (qué mide, qué falta, qué no se puede comparar) y las filas. El título es una frase que dice el hallazgo principal.

Genera solo lo tuyo:

```bash
cd pipeline && uv run run.py --only <id o tema_id>
```

`git status` solo debe mostrar archivos nuevos tuyos en `data/charts/` (y, si hiciste un mapa, `data/geo/` sin cambios de contenido).

## 5. Verificar cada afirmación

Antes de escribir textos, abre los JSON y calcula lo que vas a afirmar. Para cada número de un título, entradilla o párrafo, anota de dónde sale. Comprueba sobre todo:

- **Cuantificadores:** "casi todos", "la mayoría", "solo X": cuenta los países de verdad.
- **Récords:** "más que nunca", "el más alto", "mínimo del siglo": comprueba toda la serie, no solo el último año.
- **Proporciones:** "uno de cada tres", "el doble", "la mitad": haz la división.
- **Rankings:** "el quinto", "encabeza": ordena los datos.
- **Periodos:** el año inicial y el final que citas existen para esos países.
- **Comparabilidad:** si mezclas fuentes o definiciones, dilo en las notas del gráfico.

Si la historia que esperabas no se sostiene, cuenta la que sí dicen los datos.

## 6. Escribir la web

Mira los ejemplos: `web/src/content/notes/n01.ts` y `web/src/content/charts/n01.ts` (nota); `web/src/content/themes/comercio.ts` y `web/src/content/charts/comercio.ts` (tema).

- **Configuración de los gráficos:** `web/src/content/charts/<id o tema_id>.ts`. Renderizadores: `line` (series temporales), `rank` (ranking de países, admite `targets` y `extraGeos`), `paired` (UE frente a un país por categorías), `dumbbell` (dos años por país), `stack` (barras al 100 %), `map` (regiones NUTS). Las opciones están documentadas en `web/src/lib/charts-config.ts`.
- **Nota:** `web/src/content/notes/<id>.ts` con `id`, `code` (`N02`...), `slug` ES y EN, `title`, `dek`, `published` (fecha de hoy), `lens`, `theme` y `body` (párrafos con `p(es, en)` y gráficos `{ fig, code: "1" }`). Unas 250 palabras por idioma.
- **Artículo:** `web/src/content/themes/<tema_id>.ts` con `code` (el del calendario), `slug`, `title`, `status: "published"`, `published` (hoy), `dek` y `lenses` (entradilla y cuerpo de cada mirada, con gráficos `G1`, `G2`, `E1`...). Si el calendario indica `relacionada`, añade `notes: ["<id de la nota>"]` y menciona la nota en el texto.

### Estilo

- Español de España y un inglés natural, no una traducción literal. Frases cortas.
- **Nunca uses la raya (—).** Usa punto, coma o dos puntos.
- En español, coma decimal y espacio antes de %: "12,5 %". En inglés, punto decimal y sin espacio: "12.5%".
- "EE. UU." en español, "the US" en inglés. "UE" y "EU".
- Títulos en frase normal (sin mayúsculas en cada palabra), afirmando el hallazgo.
- Cita la fuente en cada gráfico; el texto no necesita repetirla.

## 7. Comprobar

```bash
cd web && npm run build && npm run check
```

`npm run check` comprueba en un navegador sin interfaz que todos los gráficos se dibujan. Tiene que terminar sin errores. Si falla por Chromium: `npx playwright install chromium`.

Revisa también `git status`: solo archivos tuyos (contenido, configuración, pipeline y `data/charts`).

## 8. Abrir el pull request

```bash
git add -A && git commit -m "<Nota|Artículo> <id>: <título>"   # termina el mensaje con la línea Co-Authored-By
git push -u origin HEAD
gh pr create --title "<Nota|Artículo> <id>: <título>" --body-file <archivo>
```

El commit usa el email noreply configurado en el repositorio. El cuerpo del pull request incluye:

1. Qué cuenta, en dos o tres frases.
2. Los gráficos, con su código y su título.
3. **Tabla de verificación:** cada cifra del texto, el valor exacto en el JSON y el gráfico del que sale.
4. Decisiones y límites: fuentes cambiadas, países que faltan, comparaciones con matices.
5. Recordatorio: "Al fusionar este pull request, la web se publica en europa.bocal.online".

## 9. Publicar

Espera a que Vercel compile la vista previa del pull request y comprueba que pasa:

```bash
gh pr checks <número> --watch      # "Vercel" debe terminar en pass
```

Si la comprobación de Vercel falla, no fusiones: revisa el error, corrígelo en la rama y vuelve a empezar este paso. Si pasa:

```bash
gh pr merge <número> --squash --delete-branch
git checkout main && git pull --ff-only
```

Espera un par de minutos a que Vercel publique `main` y comprueba la web real: la página nueva responde (`curl -s -o /dev/null -w "%{http_code}" https://europa.bocal.online/es/notas/<slug>/` o `/es/<tema>/` debe dar 200) y sus datos también (`/data/charts/<id del gráfico>.json`).

## 10. Terminar

Deja un resumen breve: qué has publicado, el enlace a la página en la web y al pull request, y cualquier límite o duda que convenga que Borja conozca. Si no has publicado, di por qué.
