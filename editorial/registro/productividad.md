# PR. Productividad y crecimiento (publicado el 25 de septiembre de 2026; rehecho el 20 de octubre de 2026)

Rehecho por la auditoría del 19 de octubre (`auditoria-2026-10-19.md`): unas 110 palabras por mirada, un solo gráfico explicativo, sin ficha ni evidencia, sin límites, sin enlaces a N03, N06 ni AN02, y el «87 %» repetido entre dos miradas.

## Guion

1. ¿Cuánto pesa la UE en la economía mundial frente a EE. UU. y China? → G1
2. ¿Cuánto produce cada hora en cada bloque, y en qué países de la UE? → G2 (la evolución de la brecha desde 2019 se queda en AN02, que se enlaza)
3. ¿De qué se compone la diferencia de renta por habitante: productividad, horas o empleo? → E1 (explicativo: tasa de empleo y horas por ocupado frente a EE. UU.)
4. ¿Trabajan menos horas todos los europeos? → E2
5. ¿Qué fija la ley sobre las horas, y por qué se trabaja menos en Europa? → ficha de la Directiva 2003/88/CE, ley federal de EE. UU. y dos estudios (Prescott 2004; Alesina, Glaeser y Sacerdote 2005)
6. ¿Quién converge dentro de la UE? → D1
7. ¿Qué hay detrás: la productividad por hora? → D2 (explicativo: crecimiento real por hora 2004-2025)
8. ¿Y por regiones? → D3

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| Banco Mundial `NY.GDP.MKTP.PP.CD` | 1 | G1 |
| OIT `DF_GDP_2HRW_NOC_NB` (PIB por hora, PPA de 2021) | 2 | G2 |
| OCDE Productivity Database `DSD_PDB@DF_PDB` 2.0: EMP, POP, HRSPOP | 3 | E1 |
| OCDE `DSD_PDB@DF_PDB`: GDPHRS, GDPEMP, GDPPOP en PPA corrientes | 3 | Citada en «Lo que no dicen» (UE al 80,5 % de EE. UU. por hora en 2025). Descartada como gráfico: en PPA corrientes la evolución mezcla precios y contradice a G2 |
| OCDE `DSD_PDB@DF_PDB_LV` | 3 | Descartada: archivada (error 500) |
| OIT `DF_GDP_211P_NOC_NB` (PIB por ocupado) y Banco Mundial `NY.GDP.PCAP.PP.KD` | 3 | Descartadas: mezclar las dos fuentes daba una tasa de empleo de EE. UU. incoherente |
| OCDE `HRSAV` (horas por ocupado) | 3 | Descartada: para EE. UU. no cuadra con EMP y HRSPOP (1.702 frente a 1.775 horas en 2024) |
| Eurostat `sdg_10_10` | 3, 6 | D1. Era también la parte por habitante del antiguo E1 |
| OIT `DF_HOW_TEMP_SEX_ECO_NB` | 4 | E2 |
| Eurostat `nama_10_lp_ulc` (RLPR_HW, I15) | 7 | D2 |
| Eurostat `nama_10r_2gdp` | 8 | D3 |
| EUR-Lex: Directiva 2003/88/CE (arts. 6, 7, 16 y 22) | 5 | Ficha |
| Departamento de Trabajo de EE. UU.: vacaciones (FLSA) | 5 | Ficha |
| NBER w10316 (Prescott, 2004) y w11278 (Alesina, Glaeser y Sacerdote, 2005) | 5 | Evidencia |
| CSO de Irlanda: renta nacional modificada (GNI*) | 7 | Nota de D2 y texto |

## Solapes con lo publicado

- N03: crecimiento del PIB desde 2000 (+69 % EE. UU., +41 % UE) e inversión. No se repite; se enlaza tras G1.
- AN02: usa G2 y cuenta la brecha por hora de 2019 a 2024 y el 70 % de Draghi. El texto de G2 ya no repite esas cifras (el título del gráfico sí, porque es el propio dato); se enlaza tras G2. Las cifras nuevas de G2 (Japón, China ×4,3, siete países por encima de EE. UU.) no están en AN02.
- N06: deuda pública. Sin cifras en común; se enlaza al final, tras los límites.
- `revisar.py solapes` para `nama_10_lp_ulc`, `DSD_PDB`, `sdg_10_10`, `DF_GDP_2HRW`, «horas», «empleo»: solo gráficos de este tema.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| China por encima de EE. UU. desde 2014; 19,1 %; UE 14,4 %, EE. UU. 14,7 %; más del 20 % en 1990 | primer año 2014; 19,14; 14,38; 14,66; 21,17 y 20,05 | PR-G1 |
| 2024: UE 69,8, EE. UU. 80,6, Japón 52,1, China 19,7 dólares por hora | 69,76; 80,56; 52,14; 19,65 | PR-G2 |
| China ×4,3 desde 2005 | 19,65 / 4,56 = 4,31 | PR-G2 |
| Siete países por encima de EE. UU.; Bulgaria y Chipre menos de la mitad | AUT, BEL, DNK, IRL, LUX, NLD, SWE > 80,56; BGR 36,06 y CYP 37,36 < 40,28 (Letonia 44,43) | PR-G2 |
| Empleo: 88,8 % en 2000, 100,7 % en 2025 | 88,8; 100,7 | PR-E1 |
| Horas: 9,5 % menos en 2025, 9,1 % en 2000 | 90,5; 90,9 | PR-E1 |
| 2020: más empleo y menos horas; horas en 2024 en su nivel anterior | empleo 102,9, horas 86,0; horas 2019 90,8, 2024 90,7 | PR-E1 |
| «Sobre todo, lo que se produce en cada hora» | brecha por hora 13,4 % (G2) > horas 9,5 % (E1) | PR-G2, PR-E1 |
| Países Bajos 31, Alemania 33,5, EE. UU. 37,5, España 36,4; Grecia, Polonia, Lituania por encima de EE. UU. | 31,0; 33,5; 37,5; 36,4; 39,5; 38,9; 38,7 | PR-E2 (2025) |
| 48 horas por cada siete días con extras; referencia de hasta cuatro meses; cuatro semanas pagadas, sin compensación salvo fin de contrato; excepción con consentimiento | Arts. 6 b), 16 b), 7.1, 7.2 y 22.1 a) | EUR-Lex 2003/88/CE |
| El límite queda muy por encima de las horas de E2 | máximo de E2: Grecia 39,5 | PR-E2 |
| EE. UU.: la FLSA no obliga a pagar vacaciones ni festivos | «does not require payment for time not worked, such as vacations…» | DOL |
| Prescott: el tipo marginal sobre el trabajo explica casi toda la diferencia en el G7 | Resumen de NBER w10316 | NBER |
| AGS: los impuestos explican poco; regulación impulsada por sindicatos; en los sesenta se trabajaba más en Europa | Resumen de NBER w11278 | NBER |
| Rumanía 35 a 78; Polonia 52 a 81; Lituania 50 a 87; Grecia 95 a 68; Italia 114 a 96; España 101 a 92 | idénticos | PR-D1 |
| 2004-2025: UE +19,6 %; Rumanía +114,5 %; Lituania +83,8 %; Polonia +78,2 %; Italia +1,5 %; Grecia -10,6 %; España +17,7 %; Irlanda +113,1 % | idénticos | PR-D2 |
| Irlanda: parte del PIB son beneficios de multinacionales que salen del país | «profits that are generated here but then go straight out…» | CSO |
| Región de Dublín y este 268 %, Luxemburgo 245 %, sur de Irlanda 217 %, Hamburgo 196 %, Madrid 125 %, Melilla 59 % | IE06 268, LU00 245, IE05 217, DE60 196, ES30 125, ES64 59 (2024) | PR-D3 |
| OIT: 13 % menos por hora (PPA de 2021); OCDE: en torno a un 20 % menos (PPA de 2025) | 86,6 %; GDPHRS V 2025 EU27 / USA = 80,5 % | PR-G2, OCDE |

El texto anterior decía que Dublín, Luxemburgo y Hamburgo encabezaban la lista: el sur de Irlanda (217 %) está por delante de Hamburgo. Corregido.

## Filtros

| Gráfico | Consulta | Subtítulo | ¿Coinciden? |
|---|---|---|---|
| PR-E1 | OCDE PDB, EU27_2020 y USA, EMP, POP, HRSPOP, total de actividades | Ocupados por habitante y horas al año por ocupado, UE en % de EE. UU., 2000 a 2025 | Sí. La nota explica que la tasa de empleo es sobre la población total |
| PR-D2 | `nama_10_lp_ulc`, RLPR_HW, I15, 2004 y 2025 | Variación de la productividad real por hora entre 2004 y 2025 | Sí |

`revisar.py pieza productividad`: un REVISAR por «20 %» en gigantes (peso en el PIB mundial en 1990) y dentro (brecha por hora de la OCDE). Son datos distintos.

## Autoevaluación (paso 7b)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada; el «87 %» repetido desaparece con el antiguo E1. N03, N06 y AN02 se enlazan sin repetir sus cifras.
- [x] Dos gráficos explicativos: E1 (descomposición: empleo y horas) y D2 (productividad detrás de la convergencia).
- [x] Ficha de política (Directiva 2003/88/CE frente a la FLSA) y dos estudios independientes con conclusiones distintas.
- [x] Párrafo de «Lo que no dicen estos datos».
- [x] Enlaces a N03, AN02 y N06.
- [x] Los filtros coinciden con subtítulos y notas.
- [x] Las notas de los gráficos no repiten el texto.
- [x] Tres cosas que aprende un lector: 1) la UE ya tiene la misma tasa de empleo que EE. UU. y en 2000 no; 2) la diferencia de renta viene de las horas y, sobre todo, de la productividad por hora, y siete países de la UE superan a EE. UU. por hora; 3) el este ha convergido con fuertes subidas de productividad, mientras en Italia apenas ha crecido y en Grecia ha caído.

## Cambios del 20 de octubre de 2026

- Fuera: PR-E1 antiguo (`pe1-brecha-ee-uu`, mezclaba la OIT por hora y Eurostat por habitante).
- Nuevos: PR-E1 (`pe3-empleo-horas`, OCDE) y PR-D2 (`pd3-productividad-paises`, Eurostat). El mapa pasa a PR-D3.
- Texto: G2 sin las cifras de AN02; ficha y estudios en «elige»; regiones corregidas; límites; enlaces; `updated`.
