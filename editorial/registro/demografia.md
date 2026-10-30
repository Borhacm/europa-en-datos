# A08. Demografía y migración (30 de octubre de 2026)

Artículo del viernes 30 de octubre, preparado por la tarea semanal en la nube. Orden del calendario: a10 (dinero), a01, a02, a03, a04, a05, a06 y a07 ya tienen su tema en `main`. Se descarta a11 («La agenda Draghi, sector a sector») porque su ángulo (índice de EPIC por sector y por dirección general) ya está publicado en el análisis AN02. Primera entrada pendiente: a08.

La entrada indica `relacionada: n10`, pero la nota n10 todavía no está publicada: no se añade al campo `notes`. Cuando le toque, n10 (población nacida fuera de la UE) tendrá que aportar otro ángulo que el gráfico D2 de este artículo.

## Guion

1. ¿Envejece la UE más deprisa que EE. UU. y China? → G1
2. ¿Por qué envejecen los tres bloques: cuántos hijos se tienen? → G2 (al preparar los datos se cambió la pregunta inicial, «de dónde sale el crecimiento de cada bloque», porque el saldo migratorio del Banco Mundial para la UE no es fiable; la descomposición se hace solo para la UE en E1)
3. ¿Cuánto pesa la migración en la población de la UE año a año, y desde cuándo mueren más europeos de los que nacen? → E1 (explicativo: descomposición del crecimiento de la UE)
4. ¿Por qué viene la gente de fuera: trabajo, familia, estudios, asilo? → E2 (explicativo: composición de los primeros permisos de residencia por motivo)
5. ¿Qué ha decidido la UE sobre migración? → ficha del Pacto sobre Migración y Asilo
6. ¿Cuántos hijos se tienen en cada país y ha cambiado en diez años? → D1
7. ¿Qué parte de la población de cada país ha nacido fuera de la UE? → D2

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| Banco Mundial SP.POP.65UP.TO.ZS (población de 65 años o más) | 1 | G1 |
| Banco Mundial SP.DYN.CBRT.IN y SP.DYN.CDRT.IN (natalidad y mortalidad brutas) | 2 | Descartada con SM.POP.NETM: la descomposición por bloque no se publica (ver autoevaluación) |
| Banco Mundial SM.POP.NETM (saldo migratorio, estimación de Naciones Unidas) | 2 | Descartada: para la UE en 2024 da 194.612, frente a 2,49 millones de Eurostat |
| Eurostat demo_gind (saldo natural y saldo migratorio ajustado de la UE) | 3 | E1 |
| Eurostat migr_resfirst (primeros permisos de residencia por motivo) | 4 | E2 |
| Eurostat migr_asyappctza (solicitantes de asilo por primera vez) | 5 | Texto de la ficha (escala del asilo frente a los permisos) |
| Eurostat migr_resoth (permisos por «otros motivos», desglose) | 4 | Nota de E2 (protección internacional dentro de «otros») |
| Eurostat migr_asytpsm (beneficiarios de protección temporal) | 4 | Párrafo de límites |
| Comisión Europea: Pacto sobre Migración y Asilo (página y preguntas y respuestas del 12/06/2026) | 5 | Ficha. EUR-Lex no se pudo leer en esta ejecución (responde con una comprobación antibots), así que la ficha enlaza la web de la Comisión |
| Eurostat demo_find (fecundidad por país) | 6 | D1 |
| Eurostat migr_pop3ctb (población por país de nacimiento) | 7 | D2 |
| Banco Mundial SP.DYN.TFRT.IN (fecundidad de los tres bloques) | 2 | G2 |
| Eurostat proj_23ndbi (proyecciones EUROPOP2023, tasa de dependencia) | 1, 3 | Descartada: el artículo se queda en datos observados; una proyección añade supuestos que no se pueden verificar con los datos |
| Eurostat demo_pjanind (indicadores de estructura por edad) | 1 | Descartada: G1 ya compara la población de 65 o más con EE. UU. y China, con una fuente común |
| Banco Mundial SP.POP.TOTL (población total) | 2 | Descartada con SM.POP.NETM |
| OCDE International Migration Database | 4 | Descartada: cubre menos años recientes y no todos los países de la UE; migr_resfirst es la fuente oficial de los permisos |

## Solapes con lo publicado

`revisar.py solapes` con SP.POP.65UP.TO.ZS, SP.DYN.TFRT.IN, SM.POP.NETM, demo_gind, demo_find, demo_pjanind, migr_pop3ctb, migr_resfirst, proj_23ndbi y las palabras «envejec», «fecundidad», «natalidad», «migra», «nacid», «permiso»: 0 gráficos. «Dependencia» solo devuelve gráficos de energía, vivienda y empleo que no tratan de demografía. En los textos, Finanzas públicas habla del gasto en pensiones y protección social: se enlaza desde Gigantes para no repetirlo. Empleo y jóvenes (edad de emancipación, tasa de empleo) se enlaza desde Elige.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| 65 años o más: UE 22 % (2024), 15,7 % (2000); EE. UU. 17,9 % y 12,2 %; China 14,7 % y 7 % (titular y texto) | 22,0; 15,7; 17,9; 12,2; 14,7; 7,0 | DM-G1 |
| China, el doble que en 2000; la que más sube, 7,7 puntos (UE 6,3; EE. UU. 5,7) | 14,7 / 7,0 = 2,1; diferencias calculadas | DM-G1 |
| Fecundidad 2024: EE. UU. 1,63, UE 1,34, China 1,01 (titular); UE 1,44 en 2000; China 1,63 en 2000; EE. UU. por encima de 2 en 2000 | 1,63; 1,34; 1,01; 1,44; 1,63; 2,06 | DM-G2 |
| China por encima de la UE hasta 2017 | 2017: 1,79 frente a 1,56; 2018: 1,54 frente a 1,55 y por debajo desde entonces (assert) | DM-G2 |
| Saldo natural negativo todos los años desde 2012 (titular) | NATGROW < 0 de 2012 a 2025 (assert) | DM-E1 |
| 2025: 3,46 millones de nacimientos, 4,81 millones de defunciones, 1,35 millones más; saldo migratorio 2,06 millones; la población crece 705.756 | demo_gind LBIRTH 3.459.677; DEATH 4.812.382; NATGROW -1.352.705; CNMIGRAT 2.058.461; GROW 705.756 = suma (assert) | DM-E1 y Eurostat |
| Desde 2012 la población solo bajó en 2020 | GROW < 0 solo en 2020 (assert) | DM-E1 (nota) |
| Máximo del saldo migratorio en 2022 | 3.440.705, máximo de la serie (assert) | DM-E1 (nota) |
| 3,86 millones de primeros permisos (2025); trabajo 33,6 %, familia 28,1 %, estudios 15,5 %, otros 22,8 % (titular «uno de cada tres») | 3.860.000; 33,6; 28,1; 15,5; 22,8 | DM-E2 |
| En 10 países el trabajo supera la mitad (titular) | BGR, CYP, HRV, HUN, LTU, POL, PRT, ROU, SVK, SVN | DM-E2 |
| Croacia 93 %, Rumanía 81,5 % trabajo; España familia 43,4 %, Italia 40,8 %; Irlanda estudios 47,6 % | 93,0; 81,5; 43,4; 40,8; 47,6 (y es el motivo más frecuente en cada uno) | DM-E2 |
| 279.922 permisos de protección internacional (nota) | migr_resoth RFG_SPROT 2025 | DM-E2 (nota) |
| 671.895 solicitantes de asilo por primera vez en 2025; menos de una quinta parte de los permisos | migr_asyappctza FRST, EXT_EU27_2020: 671.895; 671.895 / 3.860.000 = 17,4 % | Eurostat |
| Pacto: diez actos, adoptado en junio de 2024, en aplicación desde el 12 de junio de 2026; procedimiento fronterizo de 12 semanas con recurso, tasa de reconocimiento de 20 % o menos; mínimo anual de 30.000 reubicaciones y 600 millones | Preguntas y respuestas de la Comisión (12/06/2026) | Ficha |
| Fecundidad bajó en 23 de 27 países; subió en Chipre, Portugal, Eslovaquia y Bulgaria (titular) | conteo calculado | DM-D1 |
| Finlandia 1,71 → 1,25; Lituania 1,57 → 1,11; Suecia 1,88 → 1,43 (mayores caídas: 0,46, 0,46, 0,45) | valores de 2014 y 2024 | DM-D1 |
| Francia 2 → 1,61, segunda más alta; España 1,1, segunda más baja tras Malta (1,01); Bulgaria 1,72 | valores ordenados | DM-D1 |
| Nacidos fuera de la UE: UE 10,4 % (2025) y 8,5 % (2021); Malta 15,6 → 24,6 (mayor subida, 9 puntos); España 12 → 16; Polonia 1,9; Eslovaquia 1,1 | valores del JSON | DM-D2 |
| Polonia y Grecia sin cambio; Letonia baja (10,9 → 10,4) | diferencias 0,0; 0,0; -0,5 | DM-D2 |
| 46,7 millones de residentes nacidos fuera; sube en 23 de 26 países (nota) | NEU27_2020_FOR EU27 2025: 46.682.685; conteo | DM-D2 (nota) |
| 4,35 millones de beneficiarios de protección temporal a finales de 2025 | migr_asytpsm, EU27_2020, 2025-12: 4.353.665 | Eurostat |

## Filtros

| Gráfico | Consulta (filtros) | Lo que dice el subtítulo | ¿Coinciden? |
|---|---|---|---|
| DM-G1 | Banco Mundial SP.POP.65UP.TO.ZS, EUU/USA/CHN, 2000-2024 | 65 años o más, % de la población total, 2000-2024 | Sí |
| DM-G2 | Banco Mundial SP.DYN.TFRT.IN, EUU/USA/CHN, 2000-2024 | Hijos por mujer, 2000-2024 | Sí |
| DM-E1 | demo_gind EU27_2020, NATGROW y CNMIGRAT, 2000-2025, en miles | Cambio de la población por componentes, miles de personas, 2000-2025 | Sí |
| DM-E2 | migr_resfirst citizen TOTAL (ciudadanos de fuera de la UE), duration TOTAL (3 meses o más), unit PER, 2025, % del TOTAL | Primeros permisos a ciudadanos de fuera de la UE por motivo, % del total, 2025 | Sí |
| DM-D1 | demo_find TOTFERRT, 2014 y 2024 | Hijos por mujer, 2014 y 2024 | Sí |
| DM-D2 | migr_pop3ctb age TOTAL, sex T, NEU27_2020_FOR / TOTAL, 2021 y 2025 | Nacida fuera de la UE, % de la población, 2021 y 2025 | Sí |

Cifra repetida entre miradas resuelta: «2,06» (fecundidad de EE. UU. en 2000 en Gigantes y saldo migratorio de 2025 en millones en Elige) era una coincidencia, pero se quitó de Gigantes para que no haya duda.

## Autoevaluación (paso 7b, artículos)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente: 1 G1, 2 G2 y E1, 3 E1, 4 E2, 5 ficha, 6 D1, 7 D2.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada, y ninguna cifra de titular está en dos gráficos. G2 (fecundidad de los bloques) y D1 (fecundidad por país, cambio desde 2014) cuentan cosas distintas, y la cifra de la UE de D1 solo está en el subtítulo. El gasto en pensiones no se repite: se enlaza a Finanzas públicas.
- [x] Dos gráficos explicativos o más: E1 (descomposición del cambio de población en saldo natural y saldo migratorio) y E2 (composición de los primeros permisos por motivo). Cambio de la pregunta 2 del guion: la descomposición por bloque se descartó porque el saldo migratorio del Banco Mundial para la UE en 2024 (194.612) no cuadra con Eurostat (2,49 millones); G2 explica el envejecimiento por la fecundidad.
- [x] Ficha de política con enlace oficial: Pacto sobre Migración y Asilo (web de la Comisión Europea).
- [x] Párrafo de "Lo que no dicen estos datos".
- [x] Enlace a otra pieza publicada en el texto: Finanzas públicas (Gigantes) y Empleo y jóvenes (Elige).
- [x] Los filtros de cada consulta coinciden con los subtítulos y las notas.
- [x] Las notas de los gráficos no repiten el texto: explican definiciones (saldo natural, primer permiso, país de nacimiento), fuentes y huecos.
- [x] Tres cosas que aprende un lector que sigue la prensa: 1) desde 2012 mueren en la UE más personas de las que nacen cada año, y en 2025 la diferencia fue de 1,35 millones: sin migración, la población bajaría; 2) China ya tiene menos hijos por mujer (1,01) que la UE (1,34), cuando hasta 2017 tenía más; 3) el trabajo es el primer motivo de los permisos de residencia en la UE, pero en España e Italia lo es la familia, y en Irlanda los estudios; las solicitudes de asilo son menos de una quinta parte de los permisos.

Comparada con `empleo.ts` de España en datos, esta pieza tiene ficha y límites, pero no cita evaluaciones independientes del Pacto: lleva menos de cinco meses en aplicación.

## Límites

- La entrada del calendario indica `relacionada: n10`, que aún no está publicada: no hay campo `notes`. Cuando le toque a n10, su ángulo (población nacida fuera de la UE) ya está en D2: tendrá que aportar otro desglose (por ejemplo, por continente de nacimiento o por edad) o elegirse otra entrada. Lo mismo para n09 (envejecimiento en los tres bloques), que repetiría G1.
- EUR-Lex no se pudo leer desde el entorno de esta ejecución; la ficha se basa en las páginas de la Comisión Europea.
- Portugal no tiene dato de 2025 en migr_pop3ctb.
