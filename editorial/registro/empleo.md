# A07. Empleo y jóvenes (25 de octubre de 2026)

Artículo del viernes 23 de octubre: la tarea programada no se ejecutó ese día. Se prepara a mano el domingo 25. Se elige a07 y no a11 (primera entrada pendiente) porque el ángulo de a11 (índice de EPIC por sector, por dirección general y en tres cortes) ya está publicado en AN02 y el MANUAL prohíbe repetir hallazgos.

## Guion

1. ¿Tienen los jóvenes europeos más o menos paro que los de EE. UU. y China, y cómo ha cambiado? → G1
2. ¿En qué edades trabaja menos gente en la UE que en EE. UU. y China? → G2 (explicativo: composición por edad)
3. ¿Qué se ha propuesto la UE en empleo y qué países están lejos de su objetivo? → E1 y ficha del objetivo de empleo del Pilar Europeo de Derechos Sociales
4. ¿Por qué hay tantos contratos temporales en algunos países: los trabajadores los eligen o no encuentran otra cosa? → E2 (explicativo: composición por motivo) y párrafo con la Directiva 1999/70/CE
5. ¿En qué países tienen más paro los jóvenes? → D1
6. ¿A qué edad se van de casa los jóvenes en cada país y ha cambiado? → D2
7. ¿Cuántos jóvenes ni estudian ni trabajan? → párrafo con su fuente

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| OIT DF_UNE_2EAP_SEX_AGE_RT (paro de 15 a 24 años, estimaciones modelizadas) | 1 | G1 |
| OIT DF_EMP_DWAP_SEX_AGE_RT (tasa de empleo por edad) | 2 | G2 (EE. UU., encuesta CPS) |
| Eurostat lfsi_emp_a (tasa de empleo por edad) | 2, 3 | G2 (UE) y E1 |
| Comisión Europea, Plan de Acción del Pilar Europeo de Derechos Sociales (web oficial) | 3 | Ficha y línea de objetivo de E1 |
| Eurostat lfsa_etgar (temporales por motivo y % de asalariados temporales) | 4 | E2 y su nota |
| Eurostat une_rt_a (paro de 15 a 24 años) | 5 | D1 |
| Eurostat yth_demo_030 (edad media de emancipación) | 6 | D2 |
| Eurostat edat_lfse_20 (ninis de 15 a 29 años) | 7 | Texto |
| OIT, tasa de empleo de China por edades | 2 | Descartada: sin datos por edad después de 2019 |
| Eurostat lfsa_etpga (temporales por edad) | 4 | Descartada: la consulta no existe con esos filtros; lfsa_etgar da el mismo total |
| Banco Mundial (tasa de empleo, OIT modelizada) | 1, 2 | Descartada: repite PE3 (empleo total frente a EE. UU.) |
| Directiva 1999/70/CE (trabajo de duración determinada) | 4 | Descartada para la ficha: EUR-Lex no se pudo leer en esta ejecución; no se cita sin comprobar |
| Objetivo de ninis del Plan de Acción (9 %) | 7 | Descartado: no se pudo comprobar en la fuente oficial |

## Solapes con lo publicado

`revisar.py solapes` con lfsi_emp_a, une_rt_a, edat_lfse_20, yth_demo_030, lfsa_etgar, «paro», «jóvenes», «temporal» y «emancip»: 0 gráficos. Con «empleo»: PE3 (Productividad: «En la UE ya trabaja la misma parte de la población que en EE. UU.») y LE2. G2 no repite PE3: lo desglosa por edad y se enlaza a Productividad en el texto. La nota n08 del calendario («Paro juvenil: de Alemania a España») coincide con D1: cuando le toque, tendrá que aportar otro ángulo o elegirse otra entrada.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| Paro juvenil UE 14,9 %, EE. UU. 8,9 % (2024) (titular y entradilla) | EU27 14,9; USA 8,9 | EM-G1 |
| China 6,8 % en 2000, 15 % en 2024, igual que la UE | CHN 6,8 (2000); 15,0 (2024); assert |CHN-EU| < 0,5 | EM-G1 |
| Máximo de la UE en 2013, 24,3 % | máximo de la serie EU27: 2013, 24,3 | EM-G1 (nota) |
| EE. UU. se disparó en 2020 y bajó deprisa | 8,4 (2019); 14,9 (2020); 8,1 (2022) | EM-G1 |
| Empleo 25-54: UE 82,4 %, EE. UU. 80,7 %; 55-64: 65,2 % y 64,1 % | 82,4; 80,7; 65,2; 64,1 (2024) | EM-G2 |
| Jóvenes 15-24: UE 34,9 %, EE. UU. 50,9 %; 16 puntos menos (titular) | 34,9; 50,9 (redondeo de 50,89); 50,9 - 34,9 = 16,0 | EM-G2 |
| Empleo 20-64 UE 76,1 %, a dos puntos del 78 % | 76,1; 78 - 76,1 = 1,9 | EM-E1 |
| 16 de los 27 países en el 78 % o más (titular) | conteo v >= 78: 16 | EM-E1 |
| Malta 83,6 %, Países Bajos 83,4 %; Italia 67,6 %, Rumanía 69 %, Grecia 71 %, España 72,4 % | 83,6; 83,4; 67,6; 69,0; 71,0; 72,4 | EM-E1 |
| Objetivo del 78 % de 20 a 64 años para 2030; Oporto, mayo de 2021; tres objetivos | Web de la Comisión (Pilar Europeo de Derechos Sociales) | Ficha |
| Temporales: UE 12,7 %, Países Bajos 25,8 %, España 15,1 % | PC_SAL TOTAL: 12,7; 25,8; 15,1 (2025) | EM-E2 (nota) |
| La mitad: no encontró fijo 26,6 % + solo había temporal 23,3 % (titular) | 26,6 + 23,3 = 49,9 | EM-E2 |
| España 76,4 %; Italia 82,9 % | 57,6 + 18,8; 55,2 + 27,7 | EM-E2 |
| Alemania, el 40 % se forma (39,9 %); Países Bajos, 58,1 % en prueba | DEU EDUC_TNG 39,9; NLD PROB 58,1 | EM-E2 |
| Paro juvenil UE 15,2 % (2025); Rumanía 26,1 %, España 24,9 %; Alemania 7,1 %, Países Bajos 8,8 % (titular D1) | 15,2; 26,1; 24,9; 7,1; 8,8; sin dato de Luxemburgo | EM-D1 |
| Ninis: UE 11 % (2025) frente a 15,2 % (2015); España 19,4 % a 11,5 %; Rumanía 19,2 %; Países Bajos 5,3 % | edat_lfse_20 NEMP: 11,0; 15,2; 19,4; 11,5; 19,2 (máx.); 5,3 (mín.) | Eurostat |
| Emancipación UE 26,3 (2025) y 26,4 (2015); Croacia 31,5; Grecia y Eslovaquia 30,9; España e Italia 30,2; Finlandia 21,3; Dinamarca 21,8 | 26,3; 26,4; 31,5; 30,9; 30,9; 30,2; 30,2; 21,3; 21,8 | EM-D2 |
| España, más de un año desde 2015 | 29,0 → 30,2 | EM-D2 |
| La edad sube en 11 de 27 países (nota) | conteo calculado | EM-D2 |

## Filtros

| Gráfico | Consulta (filtros) | Lo que dice el subtítulo | ¿Coinciden? |
|---|---|---|---|
| EM-G1 | OIT, SEX_T, AGE_YTHADULT_Y15-24, años <= 2024 | 15 a 24 años, % de los activos, 2000-2024 | Sí |
| EM-G2 | Eurostat lfsi_emp_a PC_POP EMP_LFS, T; OIT AGE_AGGREGATE_Y15-24/25-54/55-64, fuente LFS; 2024 | Tasa de empleo por edad, % de la población, 2024 | Sí (EE. UU. empieza a los 16: nota) |
| EM-E1 | lfsi_emp_a PC_POP EMP_LFS, T, Y20-64, 2025 | 20 a 64 años, % de la población, 2025 | Sí |
| EM-E2 | lfsa_etgar PC_SAL_TEMP, T, Y15-64, 2025 | % de los asalariados temporales de 15 a 64, 2025 | Sí |
| EM-D1 | une_rt_a PC_ACT, T, Y15-24, 2025 | 15 a 24 años, % de los activos, 2025 | Sí |
| EM-D2 | yth_demo_030 AVG, T, 2015 y 2025 | Edad media, años, 2015 y 2025 | Sí |

Cifra repetida entre miradas resuelta: el 24,3 % de Suecia (D1) coincidía con el máximo de la UE de 2013 (G1); se quitó Suecia del texto.

## Autoevaluación (paso 7b, artículos)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada, y ninguna cifra de titular está en dos gráficos. G2 desglosa PE3 por edad y lo enlaza.
- [x] Dos gráficos explicativos o más: G2 (composición del empleo por edad, UE frente a EE. UU.) y E2 (composición de los temporales por motivo).
- [x] Ficha de política con enlace oficial: objetivo de empleo del Plan de Acción del Pilar Europeo de Derechos Sociales (web de la Comisión).
- [x] Párrafo de "Lo que no dicen estos datos".
- [x] Enlace a otra pieza publicada en el texto: Productividad (PE3) y Vivienda.
- [x] Los filtros de cada consulta coinciden con los subtítulos y las notas.
- [x] Las notas de los gráficos no repiten el texto.
- [x] Tres cosas que aprende un lector que sigue la prensa: 1) la UE emplea a más gente de 25 a 54 años que EE. UU.; la brecha está solo en los jóvenes (16 puntos); 2) China ya tiene tanto paro juvenil como la UE, tras partir del 6,8 % en 2000; 3) en España e Italia, más de tres de cada cuatro temporales lo son porque no encuentran otra cosa; en Alemania, el 40 % se está formando.

## Límites

Las fuentes de las piezas se publican con su nombre en español también en la versión inglesa, como en el resto de temas. Comparada con empleo.ts de España en datos, esta pieza tiene ficha y límites, pero no cita evaluaciones independientes del objetivo de 2030.
