# A09. Educación y talento (6 de noviembre de 2026)

Artículo del viernes 6 de noviembre, preparado por la tarea semanal en la nube. Orden del calendario: a10 (dinero), a01, a02, a03, a04, a05, a06, a07 y a08 ya tienen su tema en `main`. Se descarta a11 («La agenda Draghi, sector a sector») porque su ángulo (índice de EPIC por sector y por dirección general) ya está publicado en el análisis AN02. Primera entrada pendiente: a09.

La entrada indica `relacionada: n12`, pero la nota n12 todavía no está publicada: no se añade al campo `notes`. Para dejarle su ángulo (universitarios de 25 a 34 años, país por país, frente al objetivo), este artículo solo da la cifra de la UE en la ficha y no tiene un gráfico por países de ese indicador.

## Guion

1. ¿Llega a la universidad una parte de los jóvenes tan grande en la UE como en EE. UU. y China, y qué ha cambiado desde 2000? → G1
2. ¿Tiene la UE tantos investigadores como EE. UU. y China? → G2
3. ¿Quién paga la educación pública y en qué etapa se gasta: escuela o universidad? → E1 (explicativo: composición del gasto público en educación por nivel)
4. ¿Qué rinde estudiar: cuánto cambia la probabilidad de tener empleo según el nivel de estudios? → E2 (explicativo: relación entre nivel educativo y empleo)
5. ¿Qué ha decidido la UE? → ficha de la Resolución del Consejo sobre el segundo ciclo del Espacio Europeo de Educación (2026-2030)
6. ¿Cuántos jóvenes dejan los estudios pronto en cada país y ha mejorado en diez años? → D1
7. ¿Forman los países suficientes estudiantes en ciencias, tecnología, ingeniería y matemáticas (CTIM), y cuántas son mujeres? → D2

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| Banco Mundial SE.TER.ENRR (tasa bruta de matrícula en educación terciaria, UNESCO) | 1 | G1 |
| Banco Mundial SE.TER.CUAT.BA.ZS (población de 25 o más con grado) | 1 | Descartada: sin agregado de la UE y China solo con datos de 2000, 2010 y 2020 |
| Banco Mundial SP.POP.SCIE.RD.P6 (investigadores en I+D por millón de habitantes, UNESCO) | 2 | G2 |
| Banco Mundial SP.POP.TOTL (población) | 2 | Nota de G2 (número total de investigadores) |
| Banco Mundial SE.XPD.TOTL.GD.ZS (gasto público en educación, % del PIB) | 3 | Descartada: para China solo hay un año (2023) y para EE. UU. termina en 2021; el gasto se mira dentro de la UE con COFOG |
| Eurostat gov_10a_exp, COFOG GF09 y subgrupos (gasto de las administraciones públicas en educación por nivel) | 3 | E1 |
| Eurostat educ_uoe_fine06 (gasto por alumno, UOE) | 3 | Descartada: último año más antiguo y huecos en varios países; COFOG da 2024 para los 27 |
| Eurostat edat_lfse_24 (tasa de empleo de los jóvenes de 20 a 34 años que ya no estudian, por nivel) | 4 | E2 |
| Eurostat edat_lfse_14 (abandono temprano de la educación y la formación, 18 a 24 años) | 6 | D1 |
| Eurostat educ_uoe_enrt03 (estudiantes de educación terciaria por campo de estudio y sexo) | 7 | D2 |
| Eurostat educ_uoe_grad04 (titulados CTIM por 1.000 habitantes de 20 a 29 años) | 7 | Descartada: el objetivo europeo se mide con la matrícula (educ_uoe_enrt03), no con los titulados |
| Eurostat edat_lfse_03 (población de 25 a 34 años con estudios terciarios) | 5 | Solo la cifra de la UE, en la ficha: el desglose por país es el ángulo de la nota n12 |
| OCDE PISA (bajo rendimiento a los 15 años) | 3, 5 | Descartada: no hay lector de PISA en el pipeline y la última edición es de 2022 |
| Consejo de la UE, Resolución C/2026/3720 (DO de 10/07/2026) y Resolución 2021/C 66/01 | 5 | Ficha |

## Solapes con lo publicado

`revisar.py solapes` con edat_lfse_14, edat_lfse_03, edat_lfse_24, SP.POP.SCIE.RD.P6, SE.TER.ENRR, educ_uoe_grad04 y las palabras «abandono», «universit», «investigador», «educaci», «STEM», «graduad»: 0 gráficos. gov_10a_exp aparece en Defensa (dfd2, dfe2) y en Finanzas (fpe2, gasto por funciones): este artículo usa solo la función educación (GF09) y su reparto por niveles, que no está publicado. En los textos, IA y digital cuenta el gasto en I+D en % del PIB (UE 2,1 %, EE. UU. 3,4 %, China 2,7 %): G2 mide personas (investigadores), no gasto, y enlaza ese tema. Empleo y jóvenes cuenta el paro juvenil y los jóvenes que ni estudian ni trabajan: E2 y D1 miden otra cosa (empleo según nivel de estudios y abandono temprano) y se enlaza.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| China: matrícula terciaria del 7,6 % (2000) al 76,9 % (2024), diez veces más (titular, entradilla y texto) | 7,6; 76,9; 76,9 / 7,6 = 10,1 | ED-G1 |
| UE: del 50,9 % (2000) al 79,5 % (2024); EE. UU. entre 87,6 % y 88,9 % de 2013 a 2020 y 79,4 % en 2022 | 50,9; 79,5; mínimo 87,6 (2020) y máximo 88,9 (2015) en 2013-2020; 79,4 | ED-G1 |
| En 2022, la UE (79,6 %) supera a EE. UU. por primera vez en los años con dato de los dos | años de EE. UU.: 2005 y 2013-2022; la UE va por debajo en todos salvo 2022 | ED-G1 |
| Investigadores por millón: UE 2.117 (2000) y 4.741 (2023), más del doble; EE. UU. 3.556 y 4.937 (2022); China 550 y 2.107 (titular y texto) | 2117; 4741; 3556; 4937; 550; 2107 | ED-G2 |
| Unos 3 millones de investigadores en China, 2,1 en la UE y 1,6 en EE. UU. («en número total ya tiene más») | por millón × SP.POP.TOTL del mismo año: 3,0; 2,1; 1,6 (assert) | ED-G2 (nota) |
| Gasto público en educación de la UE: 4,7 % del PIB (2024) | gov_10a_exp PC_GDP GF09 EU27_2020 2024: 4,7 | ED-E1 (subtítulo) |
| UE: 71,9 % escuela, 16 % superior, 12,2 % otros (titular «de cada 100 euros, 16») | 71,9; 16,0; 12,2 (calculado con millones de euros) | ED-E1 |
| Superior: Grecia 32,9 % (máximo), Hungría 28,4 %, Finlandia 27,5 %; Francia 8,3 % (mínimo); Italia y Eslovaquia 10,3 %; España 13,4 % | valores ordenados | ED-E1 |
| Francia: servicios auxiliares y otros 19,7 % frente a 12,2 % de la UE | 19,7; 12,2 | ED-E1 (nota) |
| Empleo 20-34 años que ya no estudian, 2025: superiores 88,4 %, bachillerato o FP 80,6 %, hasta secundaria obligatoria 56,5 %; 31,9 puntos | 88,4; 80,6; 56,5; 88,4 - 56,5 = 31,9 | ED-E2 |
| Eslovaquia 58 puntos (máxima), Finlandia 56,4, Chipre 11,9 (mínima); España 19,7, quinta menor; España 67,1 % y 86,8 % | 90,2 - 32,2; 89,2 - 32,8; 87,6 - 75,7; 86,8 - 67,1; orden CYP, MLT, CZE, PRT, ESP | ED-E2 |
| Chequia, único país con menos empleo en superiores (78,2 %) que en bachillerato o FP (84,3 %) | assert | ED-E2 (nota) |
| Abandono temprano UE: 9,1 % (2025) y 11 % (2015) | 9,1; 11,0 | ED-D1 |
| Baja en 20 de 27 países; sube en 7 (Alemania, Austria, Chipre, Dinamarca, Eslovenia, Finlandia, Lituania) (titular) | conteo (assert) | ED-D1 |
| Malta 16,3 → 8,6; Portugal 13,5 → 6,1; España 20 → 12,8: más de 7 puntos (titular) | caídas 7,7; 7,4; 7,2; la siguiente, Grecia, 4,9 | ED-D1 |
| Alemania 10,1 → 13,1, segunda más alta tras Rumanía (15,5); Chipre 5,2 → 9,8 | valores ordenados | ED-D1 |
| 14 países por debajo del 8 %; Croacia la más baja (2,1 %), dato poco fiable | conteo; flag «u» en Croacia y Luxemburgo | ED-D1 |
| CTIM: UE 27,1 % de los estudiantes terciarios (2024); mujeres 32,2 % (titular) | 27,1; women_share EU27 32,2 | ED-D2 |
| Cuatro países superan el 32 %: Irlanda 36,4, Finlandia 35,8, Alemania 35,4, Grecia 34,4; España 25,3 | valores ordenados (assert) | ED-D2 |
| Mujeres: Suecia 38,5 % (máximo, ningún país llega al 40 %), Alemania 29,8, Irlanda 25,6 | women_share | ED-D2 |
| Irlanda: ingeniería, industria y construcción de 28.585 (2023) a 59.544 (2024), sin ruptura marcada | educ_uoe_enrt03 F07 IE | ED-D2 (nota) |
| 44,8 % de 25 a 34 años con estudios superiores en la UE (2025) | edat_lfse_03 ED5-8 Y25-34 T EU27_2020 2025: 44,8 | Eurostat (ficha) |
| Objetivos 2030: abandono < 8 %, terciaria ≥ 47 %, CTIM ≥ 32 % con dos mujeres de cada cinco; PISA < 15 %; «niveles de referencia del rendimiento medio europeo», a alcanzar en conjunto; DO de 10/07/2026 | Resolución C/2026/3720, anexo II (texto en español leído en Cellar) | Ficha |
| Objetivos de 2021: abandono < 9 %, terciaria ≥ 45 %; publicados en febrero de 2021 | Resolución 2021/C 66/01, DO C 66 de 26/02/2021 | Ficha |

## Filtros

| Gráfico | Consulta (filtros) | Lo que dice el subtítulo | ¿Coinciden? |
|---|---|---|---|
| ED-G1 | Banco Mundial SE.TER.ENRR, EUU/USA/CHN, 2000-2024 | Tasa bruta de matrícula terciaria, 2000-2024 | Sí |
| ED-G2 | Banco Mundial SP.POP.SCIE.RD.P6, EUU/USA/CHN, 2000-2023 | Investigadores en I+D por millón, 2000-2023 | Sí |
| ED-E1 | gov_10a_exp S13, TE, MIO_EUR, GF0901-GF0908 / GF09, 2024; PC_GDP GF09 | Gasto de las administraciones públicas en educación por etapa, % del gasto en educación, 2024; UE 4,7 % del PIB | Sí |
| ED-E2 | edat_lfse_24 sex T, Y20-34, PC, duration TOTAL, ED0-2 / ED3_4 / ED5-8, 2025 | Empleo de 20 a 34 años que ya no estudian, por nivel, 2025 | Sí |
| ED-D1 | edat_lfse_14 sex T, Y18-24, PC, wstatus POP, 2015 y 2025 | 18 a 24 años con secundaria obligatoria como mucho que no estudian, 2015 y 2025 | Sí |
| ED-D2 | educ_uoe_enrt03 NR, ED5-8, F05+F06+F07 / TOTAL, sex T (y F para las mujeres), 2024 | Estudiantes terciarios en CTIM, % del total, 2024 | Sí |

Cifra repetida entre miradas resuelta: «9,1 %» (parte de Luxemburgo en el gasto en educación superior, en Elige, y abandono temprano de la UE, en Dentro) era una coincidencia, pero se quitó Luxemburgo del texto de Elige.

## Autoevaluación (paso 7b, artículos)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente: 1 G1, 2 G2, 3 E1, 4 E2, 5 ficha, 6 D1, 7 D2.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada, y ninguna cifra de titular está en dos gráficos. El gasto en I+D de IA y digital no se repite (G2 cuenta personas y enlaza ese tema); el paro juvenil y los ninis de Empleo no se repiten (se enlaza). La cifra de universitarios de 25 a 34 años solo aparece para la UE en la ficha.
- [x] Dos gráficos explicativos o más: E1 (composición del gasto público en educación por etapa) y E2 (relación entre nivel de estudios y empleo).
- [x] Ficha de política con enlace oficial: Resolución del Consejo C/2026/3720 (Oficina de Publicaciones de la UE) y la de 2021 (EUR-Lex).
- [x] Párrafo de "Lo que no dicen estos datos".
- [x] Enlace a otra pieza publicada en el texto: IA y digital (Gigantes) y Empleo y jóvenes (Elige).
- [x] Los filtros de cada consulta coinciden con los subtítulos y las notas.
- [x] Las notas de los gráficos no repiten el texto: explican definiciones (tasa bruta, COFOG, CTIM, abandono), huecos y avisos de fiabilidad de Eurostat.
- [x] Tres cosas que aprende un lector que sigue la prensa: 1) en 2026 la UE endureció sus objetivos de educación para 2030 (abandono por debajo del 8 % y 47 % de universitarios de 25 a 34 años) cuando aún no cumplía los de 2021 (9,1 % y 44,8 %); 2) China ha multiplicado por diez su matrícula en estudios superiores desde 2000 y ya tiene más investigadores que la UE, unos 3 millones frente a 2,1; 3) el abandono temprano ha subido desde 2015 en Alemania, del 10,1 % al 13,1 %, mientras España lo ha bajado del 20 % al 12,8 %.

Comparada con `empleo.ts` de España en datos, esta pieza tiene ficha y límites, pero no cita evaluaciones independientes: la Resolución lleva cuatro meses publicada. La evaluación intermedia de la Comisión del primer ciclo [COM(2025) 340] se cita en la propia Resolución, pero no se ha podido leer en esta ejecución y no se usa.

## Límites

- La entrada del calendario indica `relacionada: n12`, que aún no está publicada: no hay campo `notes`. Cuando le toque, n12 debe usar el nuevo objetivo del 47 % (no el 45 % del calendario) y puede dar el desglose por país y por sexo de edat_lfse_03, que este artículo no publica.
- EUR-Lex no se pudo leer desde el entorno de esta ejecución (comprobación antibots); los dos textos se leyeron en el Cellar de la Oficina de Publicaciones. El enlace de 2021 apunta a EUR-Lex por su número CELEX.
- El dato irlandés de CTIM de 2024 tiene un salto sin ruptura de serie marcada (ver nota de D2).
- Para EE. UU., la UNESCO no publica matrícula terciaria después de 2022 ni investigadores después de 2022.
