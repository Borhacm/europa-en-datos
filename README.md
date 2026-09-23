# Europa en datos

Visualización de datos abiertos europeos: la UE frente a EE. UU. y China, y las diferencias entre sus países, contada desde tres miradas que se pueden combinar.

- **Entre dos gigantes**: la UE comparada con EE. UU. y China.
- **¿Pierde Europa o elige?**: lo que el modelo europeo gana y lo que cede.
- **Europa por dentro**: diferencias entre los 27 países y sus regiones.

Piloto actual: **IA y digital** (ver [docs/piloto-ia-digital.md](docs/piloto-ia-digital.md)).

## Datos

Fuentes: Eurostat, OCDE, Banco Mundial, Epoch AI y V-Dem. Cada gráfico cita su fuente y licencia.

```bash
cd pipeline
uv run run.py            # usa la caché de data/raw
uv run run.py --refresh  # vuelve a descargar todo
```

Salida:

- `data/charts/<id>.json`: un fichero por gráfico, con textos en ES y EN, fuente, notas y observaciones.
- `data/index.json`: catálogo de gráficos, miradas y temas.
- `data/geo/nuts{0,1,2}.json`: geometrías NUTS 2024 (TopoJSON, Eurostat GISCO).

## Estructura

```
pipeline/
  lib/sources.py   lectores de Eurostat, OCDE, Banco Mundial, Epoch y V-Dem
  lib/geo.py       códigos de país (ISO3 + EU27) y nombres en ES y EN
  lib/output.py    formato común y validación
  charts/          un módulo por mirada: gigantes.py, elige.py, dentro.py
docs/              inventario de datos y decisiones del piloto
data/              salida del pipeline (data/raw es caché, no se versiona)
```
