# Auditoría de calidad de temas y notas (19 de octubre de 2026)

Revisión de los 8 temas y las 8 notas publicados con los criterios de profundidad que se aplicaron en España en datos (guion, gráficos explicativos, ficha de política o evidencia, límites, enlaces, sin repeticiones). Se comprobaron a mano varios titulares de los primeros temas (ld1, cd2, le1, lg3, sae2): las cifras se sostienen. El problema no son las cifras, sino la profundidad y los solapes.

## Resultado por tema

| Tema | Palabras por mirada | Explicativos | Ficha o estudios | Límites | Enlaces | Problemas |
|---|---|---|---|---|---|---|
| Comercio (CO) | ~100 | 1 (por producto) | No | No | No | El más corto; sin aranceles, CBAM ni reducción de riesgos |
| Libertades (LI) | ~100 | 0 | No | No | No | Mezcla democracia, salud, clima, gasto social, pobreza y renovables; LD3 repite el ranking de renovables de Energía (EN-D1), con 2025 provisional frente a 2024 en Energía |
| Productividad (PR) | ~110 | 1 (PE1) | No | No | No | No enlaza N03, N06 ni AN02, que tratan lo mismo |
| Sanidad (SA) | ~150 | 1 (SA-E1) | No | No | No | Sin evidencia sobre resultados |
| IA y digital (IA) | ~160 | 3 | No (AN01 sí, pero no se enlaza) | No | No | IA-G1 sin notas; IA-E3 con título en pregunta; IA-E2 con un titular valorativo ("Europa elige otro camino") |
| Dinero (DI) | ~220 | 2 | Cronología, `sources` | Sí | No | Le falta el párrafo de límites explícito |
| Vivienda (VI) | ~190 | 2 | No | No | N01 | El umbral del 40 % en dos titulares (es un umbral, aceptable) |
| Energía (EN) | ~200 | 2 | No | En parte | N04 | 25,2 %, 42,5 % y 45,8 % se repiten entre miradas; solape con Libertades (renovables) y con AN02 (luz para la industria) |

## Notas

- Los temas de varias notas son anteriores a los temas actuales: N01 está en Libertades (debería estar en Vivienda), N04 en Comercio (Energía), N05 en Libertades (Energía, o Transporte cuando exista), N06 en Productividad (Finanzas públicas cuando exista).
- N01 tiene 112 palabras y ninguna fuente en `sources`.
- Ninguna nota tiene una frase de límites.

## Errores encontrados en la última semana

- AN02-1 rotulaba "sin IVA" un precio con todos los impuestos (corregido en #15 y #16).
- El gráfico de líneas no admitía series semestrales: EN-E2 no se dibujaba (corregido en #14).
- Un título cambiado en el pipeline no se regeneró en el JSON (corregido en #16).

## Plan

- **P0 (hecho en este pull request):** guion y autoevaluación en el manual (pasos 2b y 7b), comprobación de filtros y de solapes, `editorial/revisar.py` y este registro.
- **P1:** (hecho: Libertades el 19 de octubre, y Comercio, Productividad, Sanidad e IA y digital el 20; ver `libertades.md`, `comercio.md`, `productividad.md`, `sanidad.md` e `ia-digital.md`) rehacer los cinco temas del piloto con el método del manual, por este orden: Libertades (dividir o recortar y quitar el solape con Energía), Comercio, Productividad (enlazar N03, N06 y AN02), Sanidad e IA y digital.
- **P2:** completar Energía, Vivienda y Dinero: ficha de política (por ejemplo, la directiva de renovables o la reforma del mercado eléctrico), párrafo de límites y cifras sin repetir entre miradas.
- **P3:** reasignar el tema de N01, N04 y N05; ampliar N01; una frase de límites en cada nota.
