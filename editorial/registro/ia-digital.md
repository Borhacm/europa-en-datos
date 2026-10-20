# IA. IA y digital (publicado el 24 de septiembre de 2026; rehecho el 20 de octubre de 2026)

Revisado por la auditoría del 19 de octubre (`auditoria-2026-10-19.md`): IA-G1 sin notas, IA-E3 con título en pregunta, IA-E2 e IA-E1 con titulares valorativos, sin ficha, sin límites y sin enlazar AN01. Ya tenía tres gráficos explicativos (G1 con la parte empresarial, E1 con los motivos y E3 con el tipo de publicación), así que no se añaden gráficos: se corrigen títulos, notas y texto.

## Guion

1. ¿Cuánto invierte cada bloque en investigación, y quién invierte? → G1 (explicativo: total frente a empresas)
2. ¿Se nota en lo que se inventa? → G2
3. ¿Y en los modelos que marcan el ritmo? → G3
4. ¿Por qué no usan IA generativa quienes no la usan? → E1 (explicativo: motivos)
5. ¿Cómo gobierna internet cada bloque? → E2
6. ¿Publica Europa sus modelos de otra forma? → E3 (explicativo: abiertos, API, cerrados)
7. ¿Qué empresas, regiones y personas usan IA dentro de la UE? → D1, D2, D3
8. ¿Tienen los europeos las competencias, y qué se ha propuesto la UE? → D4 y ficha de la Decisión (UE) 2022/2481

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| OCDE MSTI `DSD_MSTI@DF_MSTI` (GERD y BERD) | 1 | G1 |
| OCDE patentes `DF_PATENTS_OECDSPECIFIC` (PCT, IA) y Banco Mundial `SP.POP.TOTL` | 2 | G2 |
| Epoch AI, notable AI models | 3, 6 | G3, E3 |
| Eurostat `isoc_ai_iaiuxr` | 4 | E1 |
| V-Dem v16 (`v2smgovfilprc`, `v2smgovsmcenprc`) | 5 | E2 |
| Eurostat `isoc_eb_ai` | 7 | D1 (N02 usa el mismo dataset para los frenos, otra variable) |
| Eurostat `isoc_r_eb_ain2` | 7 | D2 |
| Eurostat `isoc_ai_iaiu` | 7 | D3 |
| Eurostat `isoc_sk_dskl_i21` | 8 | D4 |
| EUR-Lex: Decisión (UE) 2022/2481 (arts. 4, 6 y 8) | 8 | Ficha |
| Reglamento (UE) 2024/1689 (AI Act) | 5 | Descartado como ficha: lo cubren N02 y AN01, que se enlazan |

## Solapes con lo publicado

- AN02 cita IA-G1 con sus cifras de 2024 (2,13 %, 3,45 %, 2,69 %) y la parte de las empresas. El texto del tema cuenta ahora la evolución en diez años y los países de contexto (Corea, Alemania, España), mantiene solo la brecha empresarial (es el hallazgo del gráfico) y enlaza AN02.
- N02 y AN01: frenos de las empresas e incertidumbre legal del AI Act. No se repiten; se enlazan tras E1 y E3.
- V-Dem: Libertades usa otras variables (democracia liberal y componentes). Se enlaza tras E2.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| UE 2,0 % (2014) y 2,1 % (2024); EE. UU. 2,7 % a 3,4 %; China 2,0 % a 2,7 %, por encima de la UE desde 2015 | 2,001; 2,129; 2,709; 3,445; 1,985; 2,693; primer año 2015 | IA-G1 |
| Corea 5,1 %, Alemania 3,1 %, España 1,5 % | 5,125; 3,132; 1,501 | IA-G1 |
| Empresas: EE. UU. 2,7 %, UE 1,4 % | 2,668; 1,406 | IA-G1 |
| Patentes: casi el triple; por habitante cuatro veces; China y UE a la par | 2024: 5.193 y 4.914 frente a 1.776 (2,9 y 2,8); 15,27 frente a 3,94; 3,49 y 3,94 | IA-G2 |
| Modelos desde 2023: UE 18, EE. UU. 250, China 120 | idénticos | IA-G3, IA-E3 |
| No la necesitan 64 %; privacidad o seguridad 7 %; España 28 % y 25 % | 64,25; 7,25; 27,54; 24,69 | IA-E1 |
| China filtra y censura más que cualquier país de la UE | filtrado -2,82 frente a mínimo UE 0,52; censura -3,01 frente a 0,58 (2025) | IA-E2 |
| EE. UU.: filtrado aumentó en 2023 y sigue; la mediana UE filtra menos | 1,791 (2022), 1,527 (2023-2025); mediana UE 2,192 | IA-E2 |
| UE 13 de 18 abiertos; China 64 %; EE. UU. 29 %, más de la mitad API o web | 13/18; 64,2; 28,8; 51,6 | IA-E3 |
| Empresas con IA: Dinamarca 42 %, Rumanía 5 %, UE 20 % (×2,6 desde 2021), España en la media | 42,03; 5,21; 19,95 / 7,65 = 2,61; 20,27 | IA-D1 |
| Madrid 27 %, Melilla 3,5 % | 27,42; 3,49 | IA-D2 |
| IA generativa: UE 33 %, 16-24 años 64 %, España 38 % | 32,66; 63,81; 37,88 | IA-D3 |
| Competencias: 60,4 % en 2025; +6,5 puntos desde 2021; casi 20 hasta el 80 %; España 66,5 % | 60,4; 53,92; 19,6; 66,5 | IA-D4 |
| Decisión 2022/2481 de 14/12/2022: 80 % competencias, 20 millones de especialistas, 75 % de empresas con nube, macrodatos o IA, duplicar unicornios | Art. 4.1, puntos 1 a) y b), 3 a) y c) | EUR-Lex |
| «Cooperarán»; informe anual; medidas si los avances no bastan | Arts. 4.1, 6.1 y 8 | EUR-Lex |

## Filtros

Sin cambios en las consultas. Los subtítulos ya recogían los filtros (10 o más empleados sin sector financiero en D1; 16 a 74 años en E1 y D4; últimos 3 meses en D3).

`revisar.py pieza ia-digital`: 0 avisos; apartado 4 revisado (V-Dem con Libertades e `isoc_eb_ai` con N02: variables distintas).

## Autoevaluación (paso 7b)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza; AN02, N02 y AN01 se enlazan.
- [x] Tres gráficos explicativos (G1, E1, E3).
- [x] Ficha de política: Decisión (UE) 2022/2481, con enlace a EUR-Lex.
- [x] Párrafo de «Lo que no dicen estos datos».
- [x] Enlaces a AN02, N02, AN01 y Libertades.
- [x] Títulos sin preguntas ni valoraciones; IA-G1 con notas.
- [x] Las notas de los gráficos no repiten el texto.
- [x] Tres cosas que aprende un lector: 1) la UE lleva diez años sin mover su inversión en I+D mientras EE. UU. y China la suben, y la brecha está en las empresas; 2) quien no usa IA generativa dice sobre todo que no la necesita, no que le preocupe la privacidad; 3) la meta de competencias digitales para 2030 exige subir casi 20 puntos en cinco años, tres veces lo que subió en los cuatro anteriores.

## Cambios del 20 de octubre de 2026

- Títulos nuevos: IA-G2, IA-E1, IA-E2, IA-E3. Notas nuevas: IA-G1.
- Texto: G1 sin repetir AN02; E1, E2 y E3 sin valoraciones; D4 con la evolución; ficha, límites, enlaces, `sources` y `updated`.
