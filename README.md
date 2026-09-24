# Europa en datos

Visualización de datos abiertos europeos: la UE frente a EE. UU. y China, y las diferencias entre sus países, contada desde tres miradas que se pueden combinar.

- **Entre dos gigantes**: la UE comparada con EE. UU. y China.
- **¿Pierde Europa o elige?**: lo que el modelo europeo gana y lo que cede.
- **Europa por dentro**: diferencias entre los 27 países y sus regiones.

Temas publicados: **IA y digital**, **Comercio y dependencias**, **Productividad y crecimiento** y **Libertades, bienestar y clima**. Publicado en https://europa.bocal.online.

## Cómo se organiza

- **Tema** (o artículo): una historia completa con las tres miradas (`/es/<tema>/`).
- **Nota**: una o dos gráficas sobre un dato concreto, contadas desde una mirada (`/es/notas/<nota>/`).
- **Mirada**: una de las tres miradas a través de todos los temas (`/es/miradas/<mirada>/`). Aquí es donde las historias se combinan.
- Cada gráfico tiene un código único con el prefijo del tema o de la nota: `IA-G1`, `CO-D2`, `N01-1`...

## Publicación editorial

Cada semana se prepara una nota y un artículo a partir de [editorial/calendario.yaml](editorial/calendario.yaml), siguiendo [editorial/MANUAL.md](editorial/MANUAL.md). Dos tareas programadas en la app de Claude preparan cada entrada en una rama, abren un pull request con su tabla de verificación y, si todas las comprobaciones pasan, lo fusionan: la publicación es automática.

Cada tema y cada nota vive en sus propios archivos, así que un tema nuevo solo añade archivos:

- `pipeline/charts/<tema>/` o `pipeline/charts/notas/<id>_<palabra>.py`: los datos de sus gráficos.
- `web/src/content/themes/<tema>.ts` o `web/src/content/notes/<id>.ts`: los textos en ES y EN.
- `web/src/content/charts/<tema o id>.ts`: cómo se dibuja cada gráfico.

Las páginas del tema o de la nota, las miradas, la portada, los índices y la metodología se actualizan solos.

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
