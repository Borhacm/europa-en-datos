# <ID>. <Título> (<fecha de publicación>)

Copia este archivo en `editorial/registro/<id>.md` antes de buscar datos (paso 2b del manual) y complétalo mientras trabajas. En las notas bastan el guion, los solapes, la verificación y los límites.

## Guion

1. ¿...? → G1
2. ¿...? → G2 (explicativo: composición)
3. ¿...? → E1
4. ¿...? → E2
5. ¿...? → D1
6. ¿...? → D2
7. ¿Qué ha decidido la UE y qué dice la evidencia? → ficha de <norma> y estudios

## Inventario de fuentes consideradas

Al menos 10 en los artículos.

| Fuente | Pregunta | Uso |
|---|---|---|
| Eurostat <dataset> | 1 | G1 |
| ... | ... | Descartada: <motivo> |

## Solapes con lo publicado

Salida resumida de `python3 editorial/revisar.py solapes <dataset> <palabra>` y qué se hace con cada coincidencia (enlazar, otro ángulo, descartar).

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| ... | ... | ... |

## Filtros

| Gráfico | Consulta (filtros) | Lo que dice el subtítulo | ¿Coinciden? |
|---|---|---|---|
| ... | ... | ... | Sí |

## Autoevaluación (paso 7b, artículos)

- [ ] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [ ] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada, y ninguna cifra de titular está en dos gráficos.
- [ ] Dos gráficos explicativos o más: ...
- [ ] Ficha de política con enlace oficial, o dos estudios independientes citados en `sources`.
- [ ] Párrafo de "Lo que no dicen estos datos".
- [ ] Enlace a otra pieza publicada en el texto.
- [ ] Los filtros de cada consulta coinciden con los subtítulos y las notas.
- [ ] Las notas de los gráficos no repiten el texto.
- [ ] Tres cosas que aprende un lector que sigue la prensa: 1) ... 2) ... 3) ...
