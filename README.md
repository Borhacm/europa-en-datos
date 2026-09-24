# Europa en datos

Visualización de datos abiertos europeos: la UE frente a EE. UU. y China, y las diferencias entre sus países, contada desde tres miradas que se pueden combinar.

- **Entre dos gigantes**: la UE comparada con EE. UU. y China.
- **¿Pierde Europa o elige?**: lo que el modelo europeo gana y lo que cede.
- **Europa por dentro**: diferencias entre los 27 países y sus regiones.

Temas publicados: **IA y digital**, **Comercio y dependencias**, **Productividad y crecimiento** y **Libertades, bienestar y clima**. Publicado en https://europa.bocal.online.

## Cómo se organiza

- **Tema**: una historia completa con las tres miradas (`/es/<tema>/`).
- **Mirada**: una de las tres miradas a través de todos los temas (`/es/miradas/<mirada>/`). Aquí es donde las historias se combinan.
- Cada gráfico tiene un código único con el prefijo del tema: `IA-G1`, `CO-D2`...

## Cómo añadir un tema

1. **Datos**: crea `pipeline/charts/<tema>/` con `gigantes.py`, `elige.py` y `dentro.py` (copia la estructura de `comercio/`), regístralo en `pipeline/charts/__init__.py` y en `THEMES` de `pipeline/lib/output.py`. Ejecuta `uv run run.py`.
2. **Gráficos**: añade la configuración de cada gráfico en `web/src/lib/charts-config.ts` (reutiliza los renderizadores: `line`, `rank`, `paired`, `dumbbell`, `stack`, `map`).
3. **Textos**: añade el tema en `web/src/lib/themes.ts` con su código, slugs, entradilla y los textos de cada mirada en ES y EN. Si estaba como `upcoming`, pásalo a `published`.

Las páginas del tema, de las miradas, la portada, el índice de temas y la metodología se actualizan solas.

## Datos

Fuentes: Eurostat, OCDE, Banco Mundial, la OIT, Epoch AI y V-Dem. Cada gráfico cita su fuente y licencia.

```bash
cd pipeline
uv run run.py            # usa la caché de data/raw
uv run run.py --refresh  # vuelve a descargar todo
```

Salida:

- `data/charts/<id>.json`: un fichero por gráfico, con textos en ES y EN, fuente, notas y observaciones.
- `data/index.json`: catálogo de gráficos, miradas y temas.
- `data/geo/nuts{0,1,2}.json`: geometrías NUTS 2024 (TopoJSON, Eurostat GISCO).

## Publicación

Cada push a `main` se publica automáticamente en https://europa.bocal.online (Vercel, directorio raíz `web`). Las demás ramas generan previsualizaciones privadas.

Vercel no ejecuta el pipeline de Python: para actualizar los datos, ejecuta `uv run run.py` en local y sube los cambios de `data/`.

## Estructura

```
pipeline/
  lib/sources.py   lectores de Eurostat, OCDE, Banco Mundial, Epoch y V-Dem
  lib/geo.py       códigos de país (ISO3 + EU27) y nombres en ES y EN
  lib/output.py    formato común y validación
  charts/<tema>/   un módulo por mirada: gigantes.py, elige.py, dentro.py
web/src/lib/themes.ts         registro de temas y miradas (textos en ES y EN)
web/src/lib/charts-config.ts  cómo se dibuja cada gráfico
docs/              inventario de datos y decisiones del piloto
data/              salida del pipeline (data/raw es caché, no se versiona)
```

## Licencias de los datos

Cada gráfico indica su fuente y su licencia, y lo mismo aplica a sus datos en `data/charts/`.

- **Eurostat, OCDE, Banco Mundial, OIT y Epoch AI**: CC BY 4.0. Se pueden reutilizar citando la fuente.
- **V-Dem** (gráficos IA-E2, LI-G1 y LI-D1): CC BY-SA 4.0. Los datos derivados deben compartirse con la misma licencia.
- **Geometrías NUTS** (`data/geo/`): © EuroGeographics para los límites administrativos, distribuidas por Eurostat GISCO.

Proyecto independiente de [Bocal](https://bocal.online). No está afiliado a la Unión Europea ni a ninguna de las fuentes citadas.
