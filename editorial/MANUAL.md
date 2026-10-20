# Manual de publicación

Procedimiento para preparar y publicar una **nota** o un **artículo** del [calendario](calendario.yaml). Lo siguen las tareas automáticas y sirve igual para hacerlo a mano.

**La publicación es automática.** Cada ejecución abre un pull request en GitHub (que deja registro de la entrada y de su tabla de verificación) y, cuando todas las comprobaciones pasan, lo fusiona ella misma: al llegar a `main`, Vercel publica la web. Por eso las comprobaciones de este manual no son opcionales: nadie revisa antes de publicar.

## Reglas que no se rompen

- Nunca hagas commit ni push directamente en `main`. Solo fusionas **tu propio** pull request, y solo cuando `npm run check` y la comprobación de Vercel han pasado. Nunca fusiones pull requests ajenos ni borres ramas ajenas.
- Nunca regeneres los datos de otros temas: ejecuta el pipeline siempre con `--only`. Nunca uses `--refresh`.
- No cambies la configuración de Vercel, de GitHub ni la licencia (el proyecto no tiene licencia de código a propósito).
- **Cada cifra y cada afirmación de un título o de un texto tiene que salir de los datos del JSON.** Si no puedes comprobarla, no la escribas. Esta es la regla más importante: en el pasado se colaron titulares como "casi todos los países", "más que nunca" o "uno de cada tres" que los datos no sostenían.
- **Lo que dice el texto tiene que coincidir con lo que pide la consulta.** Si el subtítulo dice "sin IVA", el filtro es `tax="X_VAT"`; si dice "de 25 a 34 años", el filtro de edad es ese. En octubre de 2026 se publicó un gráfico con el precio con todos los impuestos rotulado como "sin IVA".
- **Un hallazgo ya publicado no se repite: se enlaza.** Ni entre las miradas de una pieza ni entre piezas distintas (Libertades y Energía llegaron a publicar el mismo ranking de renovables).
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

## 2b. Guion antes de los datos

Antes de abrir ninguna fuente, copia `editorial/registro/PLANTILLA.md` en `editorial/registro/<id>.md` y escribe el **guion**. El registro se publica con la pieza (va en el pull request) y es lo que permite revisarla después.

**Artículos:**

- **Entre 5 y 7 preguntas** que se haría un lector informado sobre el tema, no solo "cuánto" y "dónde": también "quién", "por qué", "qué ha cambiado", "qué ha decidido la UE" y "qué dice la evidencia".
- **Inventario de fuentes:** al menos 10 conjuntos de datos candidatos (Eurostat, OCDE, Banco Mundial, BCE, BIS, FMI, AIE, JRC...) con la pregunta que respondería cada uno, y por qué se descartan los que no se usan. Elige los gráficos por las preguntas, no por lo primero que encuentres.
- **Solapes:** antes de elegir, busca lo ya publicado con `python3 editorial/revisar.py solapes <dataset> <palabra>` (por ejemplo `solapes nrg_ind_ren renovables`). Si un hallazgo ya está en otro tema o nota, no lo repitas: enlázalo y cuenta otra cosa.
- **Una pregunta, un gráfico.** Cada gráfico responde a una pregunta distinta del guion. Un mismo hallazgo no se repite en dos miradas, y ninguna cifra de un titular se repite en el titular de otro gráfico.
- **Mínimos de un artículo** (si no se cumplen, no se publica: ver paso 7b):
  1. Seis gráficos, dos por mirada.
  2. Al menos dos gráficos **explicativos**: composición (por fuente, uso, edad, sector...), descomposición de un cambio o relación entre dos variables. No basta con niveles y rankings.
  3. Una **ficha de política** sobre una norma o decisión europea vigente relacionada (directiva, reglamento, objetivo, plan), con su enlace a EUR-Lex o a la fuente oficial: qué es, quién la aprobó y cuándo, qué debería pasar y con qué se puede comparar. Se escribe con un bloque `h` y un bloque `steps` dentro de la mirada que corresponda. Si no hay ninguna relevante, al menos **dos evaluaciones o estudios independientes** (BCE, Comisión o JRC, OCDE, FMI, AIE, Tribunal de Cuentas Europeo, Bruegel, bancos centrales nacionales, artículos académicos), diciendo dónde la evidencia no es concluyente. Todo va en `sources`.
  4. Un párrafo que empiece por **"Lo que no dicen estos datos."**: qué falta, qué no se puede comparar entre bloques o países y qué no se puede atribuir.
  5. Un enlace en el texto a otro tema, nota o análisis publicado cuando estén conectados (además del campo `notes` si hay `relacionada`).

**Notas:** una o dos preguntas, el resultado de `revisar.py solapes` y la fuente. Una nota no repite el titular de un tema publicado: si el dato ya está, aporta otro ángulo (otro año, otro desglose) o se elige otra entrada. Lleva al menos una frase de límites y enlaza el tema al que pertenece.

## 3. Buscar y comprobar los datos

- Empieza por las fuentes del calendario, pero compruébalas: que existen, qué dimensiones tienen y cuál es el **último año con datos para casi todos los países**. Si una fuente no sirve, busca otra fiable (Eurostat, OCDE, Banco Mundial, OIT, FMI, V-Dem) y explícalo en el pull request.
- Lectores disponibles en `pipeline/lib/sources.py`: `eurostat`, `oecd`, `worldbank`, `ilo`, `vdem`, `epoch_models`, `imf` (DataMapper del FMI; pide los países en grupos de diez), `edgar_sectors` (emisiones por sector de EDGAR, del JRC), `bis` (estadísticas del BIS, p. ej. pagos del CPMI), `ecb` (Data Portal del BCE) y `comext` (comercio de Eurostat por producto, p. ej. `DS-045409`; usa `GR` para Grecia y `EU` para la UE, y da euros, no millones). El BIS usa `XM` para la eurozona: no es la UE27, dilo en las notas. Funciones comunes en `pipeline/charts/common.py`: `from_eurostat`, `eurostat_source`, `worldbank_rows`, `worldbank_source`, `vdem_with_eu`, `nuts_map` (mapas regionales).
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

**Lo que se publica es el JSON, no el código.** Si cambias un título, un subtítulo o una nota en el pipeline, vuelve a ejecutar `uv run run.py --only <id>` antes del commit. Si `--only` regenera piezas ajenas (filtra por subcadena) y solo cambia su fecha `retrieved`, devuélvelas a su estado con `git checkout <archivo>`.

## 5. Verificar cada afirmación

Antes de escribir textos, abre los JSON y calcula lo que vas a afirmar. Para cada número de un título, entradilla o párrafo, anota de dónde sale. Comprueba sobre todo:

- **Cuantificadores:** "casi todos", "la mayoría", "solo X": cuenta los países de verdad.
- **Récords:** "más que nunca", "el más alto", "mínimo del siglo": comprueba toda la serie, no solo el último año.
- **Proporciones:** "uno de cada tres", "el doble", "la mitad": haz la división.
- **Rankings:** "el quinto", "encabeza": ordena los datos.
- **Periodos:** el año inicial y el final que citas existen para esos países.
- **Comparabilidad:** si mezclas fuentes o definiciones, dilo en las notas del gráfico.
- **Filtros:** cada condición del subtítulo y de las notas (impuestos, banda de consumo, unidad, edad, sexo, año, precios corrientes o constantes) coincide con el filtro de la consulta. `python3 editorial/revisar.py pieza <id>` las pone una al lado de otra.
- **Coherencia con lo publicado:** si otra pieza usa el mismo dataset, tus cifras para el mismo año y país coinciden con las suyas o explicas en las notas por qué no (otro filtro, otro año).

Apunta cada cifra en la tabla de verificación del registro (`editorial/registro/<id>.md`) a medida que la compruebas.

Cuando todas las cifras estén comprobadas, apunta la huella de sus datos: `python3 editorial/revisar.py verificada <id o tema_id>`. Así, si una actualización cambia las filas de un gráfico, `revisar.py todo` lo señala y sabes que hay que volver a comprobar sus titulares y su texto.

Si la historia que esperabas no se sostiene, cuenta la que sí dicen los datos.

## 6. Escribir la web

Mira los ejemplos: `web/src/content/notes/n01.ts` y `web/src/content/charts/n01.ts` (nota); `web/src/content/themes/comercio.ts` y `web/src/content/charts/comercio.ts` (tema).

- **Configuración de los gráficos:** `web/src/content/charts/<id o tema_id>.ts`. Renderizadores: `line` (series temporales), `rank` (ranking de países, admite `targets` y `extraGeos`), `paired` (UE frente a un país por categorías), `dumbbell` (dos años por país), `stack` (barras al 100 %), `map` (regiones NUTS). Las opciones están documentadas en `web/src/lib/charts-config.ts`.
- **Nota:** `web/src/content/notes/<id>.ts` con `id`, `code` (`N02`...), `slug` ES y EN, `title`, `dek`, `published` (fecha de hoy), `lens`, `theme` y `body` (párrafos con `p(es, en)` y gráficos `{ fig, code: "1" }`). Unas 250 palabras por idioma.
- **Artículo:** `web/src/content/themes/<tema_id>.ts` con `code` (el del calendario), `slug`, `title`, `status: "published"`, `published` (hoy), `dek`, `lenses` (entradilla y cuerpo de cada mirada, con gráficos `G1`, `G2`, `E1`...) y `sources` (normas y estudios citados en el texto). Si el calendario indica `relacionada`, añade `notes: ["<id de la nota>"]` y menciona la nota en el texto. La ficha de política, el párrafo de "Lo que no dicen estos datos" y los enlaces a otras piezas siguen el paso 2b.
- **Las notas de los gráficos no repiten el texto:** explican qué mide la serie, qué falta y qué no es comparable. Cada gráfico lleva al menos una nota.

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

Después, desde la raíz del repositorio:

```bash
python3 editorial/revisar.py pieza <id o tema_id>
```

Resuelve cada AVISO (titulares en pregunta, gráficos sin notas, cifras repetidas en dos titulares). Los REVISAR y los apartados de filtros y de datasets compartidos se miran uno a uno: una cifra repetida entre miradas solo se queda si es un dato de contexto (un objetivo, un umbral) y no el mismo hallazgo contado dos veces.

Revisa también `git status`: solo archivos tuyos (contenido, configuración, pipeline y `data/charts`).

## 7b. Autoevaluación (artículos)

Rellena al final de `editorial/registro/<id>.md` esta lista:

- [ ] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [ ] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada, y ninguna cifra de titular está en dos gráficos.
- [ ] Dos gráficos explicativos o más (di cuáles).
- [ ] Ficha de política con enlace oficial, o dos estudios independientes citados en `sources`.
- [ ] Párrafo de "Lo que no dicen estos datos".
- [ ] Enlace a otra pieza publicada en el texto.
- [ ] Los filtros de cada consulta coinciden con los subtítulos y las notas.
- [ ] Las notas de los gráficos no repiten el texto.
- [ ] Un lector que sigue la prensa aprende al menos tres cosas que no sabía (escríbelas).

Compárala con los mejores ejemplos publicados de la misma familia, en `/Users/bcm/espana-en-datos`: `web/src/content/themes/empleo.ts` (ficha de la reforma laboral, evaluaciones de la AIReF y del Banco de España, límites) y `editorial/registro/a04.md` (guion, inventario, verificación y autoevaluación).

Si alguna casilla queda sin marcar y no se puede resolver en esta ejecución, **no publiques el artículo**: sube la rama como `borrador/<id>-<palabra>`, no abras pull request contra `main` y explica en el resumen final qué falta.

## 7c. Después de actualizar los datos

Si una ejecución del pipeline cambia datos ya publicados (por ejemplo, una nueva versión de Epoch o de Eurostat), ejecuta `python3 editorial/revisar.py todo`. Los gráficos marcados con datos sin verificar tienen titulares o textos que pueden haberse quedado viejos: vuelve a hacer el paso 5 con ellos, corrige lo que haga falta y apúntalos con `revisar.py verificada <id>`.

## 8. Abrir el pull request

```bash
git add -A && git commit -m "<Nota|Artículo> <id>: <título>"   # termina el mensaje con la línea Co-Authored-By
git push -u origin HEAD
gh pr create --title "<Nota|Artículo> <id>: <título>" --body-file <archivo>
```

El commit usa el email noreply configurado en el repositorio. El cuerpo del pull request incluye:

1. Qué cuenta, en dos o tres frases.
2. Los gráficos, con su código y su título.
3. **Tabla de verificación:** cada cifra del texto, el valor exacto en el JSON y el gráfico del que sale (la misma del registro).
   En los artículos, además, el guion y la autoevaluación del paso 7b, o un enlace a `editorial/registro/<id>.md`.
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
