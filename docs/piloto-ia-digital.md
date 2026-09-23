# Piloto: IA y digital

Diez gráficos, tres miradas. Datos generados por `pipeline/run.py` en `data/charts/`.

## Selección

| Id | Mirada | Qué cuenta | Forma sugerida | Fuente |
|---|---|---|---|---|
| `g1-inversion-id` | Gigantes | La UE invierte en I+D un 2,13 % del PIB, frente al 3,44 % de EE. UU. y el 2,69 % de China (2024). La brecha está en la I+D de las empresas | Líneas, con selector total / empresas | OCDE MSTI |
| `g2-patentes-ia` | Gigantes | Patentes de IA (PCT, 2024): EE. UU. 5.193, China 4.914, UE 1.776. Por millón de habitantes: EE. UU. 15,3, UE 3,9, China 3,5 | Líneas, con selector total / por habitante | OCDE Patents + Banco Mundial |
| `g3-modelos-ia` | Gigantes | Modelos de IA destacados (2025): EE. UU. 64, China 35, UE 1 | Barras por año | Epoch AI |
| `e1-motivos-no-ia-generativa` | Elige | El 64 % de quienes no usan IA generativa en la UE dice que no la necesita; solo el 7 % alega privacidad. En España pesa más no saber usarla (28 %) o no conocerla (25 %) | Barras horizontales, UE frente a país elegido | Eurostat |
| `e2-control-internet` | Elige | Filtrado de internet (2025, más alto = menos control): mediana UE 2,19 · EE. UU. 1,53 · China -2,82. EE. UU. empeora desde 2023 | Líneas con banda UE (mediana y mínimo) | V-Dem |
| `e3-modelos-abiertos` | Elige | Desde 2023, el 72 % de los modelos destacados de la UE se publican con pesos abiertos (China 64 %, EE. UU. 29 %). Muestra pequeña en la UE (18 modelos) | Barras apiladas al 100 % | Epoch AI |
| `d1-empresas-ia` | Dentro | Empresas con IA (2025): Dinamarca 42 %, UE 20 %, España 20,3 %, Rumanía 5,2 % | Gráfico de puntos 2021 frente a 2025, selector de tamaño | Eurostat |
| `d2-mapa-regional-ia` | Dentro | La región de la capital es la primera en 12 de los 13 países con datos regionales. Madrid 27,4 % frente a Melilla 3,5 % | Mapa de coropletas mixto (país y región) | Eurostat + GISCO |
| `d3-ia-generativa` | Dentro | Uso de IA generativa (2025): UE 32,7 %, España 37,9 %, jóvenes de 16 a 24 años 63,8 % en la UE y 75,6 % en España | Barras por país, selector de edad y uso | Eurostat |
| `d4-competencias-digitales` | Dentro | Competencias digitales básicas: UE 60,4 % frente al objetivo del 80 % en 2030 | Barras por país con línea de objetivo | Eurostat |

## Formato de cada JSON

```
id, lens, theme            identificación y etiquetas para combinar historias
title, subtitle, unit      textos en {es, en}
source                     nombre, dataset, url, licencia (y fuentes adicionales en "also")
notes                      advertencias metodológicas en {es, en}
geos                       nombres de país en {es, en} y si es UE o agregado
dimensions                 etiquetas de las dimensiones extra (measure, size, age...)
highlight / targets / ...  extras propios de cada gráfico
rows                       observaciones: {geo, time, value, ...dimensiones}
```

## Límites conocidos

- **Mapa regional**: Alemania, Francia, Italia, Países Bajos y otros solo publican el dato nacional. El mapa mezcla niveles.
- **IA generativa**: solo hay un año (2025).
- **Patentes**: los últimos años pueden estar incompletos.
- **Modelos de Epoch**: la UE tiene muestras muy pequeñas. Hay que decirlo en el gráfico.
- **Licencia V-Dem (CC BY-SA)**: los datos derivados de `e2` deben publicarse con la misma licencia.
