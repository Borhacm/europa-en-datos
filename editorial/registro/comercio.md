# CO. Comercio y dependencias (publicado el 24 de septiembre de 2026; rehecho el 20 de octubre de 2026)

Rehecho por la auditoría del 19 de octubre (`auditoria-2026-10-19.md`): unas 100 palabras por mirada, un solo gráfico explicativo, sin ficha ni evidencia, sin límites ni enlaces, y dos titulares sin cifras (CO-G2 y CO-E2).

## Guion

1. ¿Quién pesa más en el comercio mundial y cómo ha cambiado? → G1
2. ¿Quién vende al mundo más de lo que compra? → G2
3. ¿Qué balance tiene la UE con cada gigante? → G3 (explicativo: saldo bilateral)
4. ¿De quién depende la UE para comprar, y en qué productos? → E1
5. ¿Ha cambiado la UE de proveedor de energía tras la invasión de Ucrania? → E2 (explicativo: composición por origen)
6. ¿Qué ha decidido la UE frente a China y qué ha pasado después? → ficha de los derechos compensatorios a los eléctricos chinos y E3 (explicativo: composición por tipo)
7. ¿Qué países están más expuestos a EE. UU. y cuánto comercian entre ellos? → D2 y D1
8. ¿Qué países dependen más de la energía importada? → D3

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| Eurostat `ext_lt_introeu27_2020` (UE, EE. UU., China y Japón en el comercio mundial) | 1, 2 | G1, G2 |
| Eurostat `ext_lt_maineu` (comercio de la UE por socio) | 3, 4 | G3, E1 |
| Eurostat `ext_lt_mainmach`, `ext_lt_mainmanu`, `ext_lt_mainchem` | 4 | E1 (por producto) |
| Eurostat Comext `DS-045409` (por producto NC/SA, por país declarante) | 6, 7 | E3, D2 |
| Eurostat `nrg_ti_gas` (importaciones de gas por socio) | 5 | E2 |
| Eurostat `nrg_ind_id` (dependencia energética) | 8 | D3 |
| Eurostat `ext_lt_intratrd` (comercio dentro de la UE) | 7 | D1 |
| Eurostat `nama_10_gdp` (PIB a precios corrientes) | 7 | D2 (denominador) |
| Eurostat `ext_lt_maineu`, cuota de exportaciones por destino (era CO-E2) | 4 | Retirada: su hallazgo (EE. UU., primer cliente) lo cuentan mejor G3 y D2 |
| OMC, estadísticas de comercio y aranceles | 1 | Descartada: Eurostat ya publica las cuotas mundiales con la misma definición de UE |
| OCDE, TiVA (valor añadido en el comercio) | 3 | Descartada en esta revisión: series hasta 2020, menos recientes que Comext |
| Eurostat `ext_st_eu27_2020sitc` (por SITC) | 4 | Descartada: los cuatro grupos de E1 bastan para la pregunta |
| Comisión Europea, análisis de dependencias estratégicas (2021 y 2022) | 4 | Descartada como gráfico: es un análisis puntual, no una serie |
| EUR-Lex: Reglamentos de Ejecución (UE) 2024/1866 y 2024/2754 | 6 | Ficha |

## Solapes con lo publicado

- `nrg_pc_*` (precios de la energía): Energía, N04 y AN02. Este tema no habla de precios.
- `nrg_ind_id` (dependencia energética): solo en este tema (D3).
- `nrg_ti_gas`: no estaba publicado.
- Coche eléctrico: N05 cuenta la cuota de eléctricos en las matriculaciones. E3 cuenta de dónde vienen los importados: se enlaza N05 y no se repite su cifra.
- Comercio y EE. UU.: ningún otro tema ni nota. AN02 cita aranceles de forma general; sin solape.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| UE 18,9 % y China 6,5 % de las exportaciones mundiales en 2002 | 18,9; 6,5 | CO-G1 |
| China por delante desde 2015; 18,7 % frente a 14,7 % en 2024 | primer año CHN > EU27: 2015; 18,7; 14,7 | CO-G1 |
| EE. UU., primero en importaciones, 16,8 % en 2024 | USA 16,8; EU27 13,3; CHN 12,9 | CO-G1 |
| 2024: China +916.000 millones, EE. UU. -1,19 billones, UE +133.000; 2025 UE +114.000 | 915,94; -1.194,58; 133,11; 114,14 | CO-G2 |
| 2025: déficit con China 371.600 millones, nueve veces el de 2002 (40.900); máximo 2022 (397.800) | -371,6; -40,9; 9,09; mínimo -397,8 en 2022 | CO-G3 |
| Superávit con EE. UU. 198.000 millones, tres veces el de 2002 | 198,0; 64,9; 3,05 | CO-G3 |
| Cubre algo más de la mitad del déficit con China | 198,0 / 371,6 = 0,53 | CO-G3 |
| China 7,8 % (2002) y 22,6 % (2025) de las importaciones extra-UE; maquinaria 40,6 % (2022) y 35,8 % (2025); EE. UU. 14,7 % a 14,1 % | TOTAL CHN 7,8 y 22,6; SITC7 máximo 40,6 en 2022, 35,8; TOTAL USA 14,7 y 14,1 | CO-E1 |
| Gas: Rusia 46,9 % (2021), 12,2 % (2023), 14,6 % (2024) | RU 46,9; 12,2; 14,6 | CO-E2 |
| Noruega 18,2 % a 32,2 %; EE. UU. 6,2 % a 17,1 % | NO 18,2 y 32,2; US 6,2 y 17,1 | CO-E2 |
| EE. UU., mayor cliente de la UE | `ext_lt_maineu` PC_EXP_PART 2025: US 21,0, el mayor | Eurostat |
| Reglamentos 2024/1866 (3/07/2024) y 2024/2754 (29/10/2024, en vigor al día siguiente); solo eléctricos de batería nuevos | Título, art. 1 y disposición final; nota 4 del Reglamento 2024/2754 | EUR-Lex |
| Tipos: Tesla 7,8 %, BYD 17,0 %, Geely 18,8 %, SAIC 35,3 %, otras que cooperaron 20,7 %, resto 35,3 % | Art. 1.2 del Reglamento 2024/2754 | EUR-Lex |
| Eléctricos chinos 11.030 millones (2023) a 6.350 (2025), -42 % | 11,03; 6,35; -42,4 % | CO-E3 |
| Enchufables 1.090 (2024) a 3.590 (2025), se triplican; híbridos 190 (2023) a 1.810 (2025) | 1,09; 3,59 (x3,3); 0,19; 1,81 | CO-E3 |
| Total 11.750 millones en 2025, -4 % frente a 2023 | 6,35 + 3,59 + 1,81 = 11,75; 12,29 en 2023; -4,4 % | CO-E3 |
| 61,0 % de las exportaciones dentro de la UE en 2025; 61,5 % en 2004 | 61,0; 61,5 | CO-D1 |
| Chequia y Eslovaquia casi el 80 %; Irlanda 33,5 %; Chipre 27,6 %; España 61,8 % | 78,8; 78,3; 33,5; 27,6; 61,8 | CO-D1 |
| Exportaciones a EE. UU.: UE 2,9 % del PIB; Irlanda 18,5 %; Bélgica 5,0 %; Países Bajos 3,7 %; Alemania 3,2 %; España 1,0 %, octava más baja | 2,94; 18,46; 5,00; 3,69; 3,24; 1,01 (tras CYP, LUX, ROU, MLT, HRV, BGR, GRC) | CO-D2 |
| Alemania, la que más vende en euros | exports_bn: DEU 146,9; IRL 111,2 | CO-D2 |
| Irlanda: 82 % químicos orgánicos y medicamentos | Comext 2025, IE a US: capítulo 29 60.200 + capítulo 30 31.000 de 111.200 millones | Comext (nota de CO-D2) |
| Energía 2024: UE 57,3 %; Malta 98,4 %; Luxemburgo 91,0 %; Chipre 87,7 %; España 68,9 %; Estonia 4,6 %, la única por debajo del 10 % | 57,29; 98,39; 91,03; 87,71; 68,87; 4,62; la siguiente, Suecia, 26,5 | CO-D3 |

## Filtros

| Gráfico | Consulta | Subtítulo | ¿Coinciden? |
|---|---|---|---|
| CO-G3 | `ext_lt_maineu`, MIO_BAL_VAL, CN_X_HK y US, EU27_2020 | Saldo de bienes de la UE con China y EE. UU. | Sí |
| CO-E2 | `nrg_ti_gas`, G3000, TJ_GCV, EU27_2020, sin socios de la UE ni TOTAL/NSP | Origen de las importaciones de gas desde fuera de la Unión | Sí |
| CO-E3 | Comext DS-045409, EU, CN, 870380/870360/870340, importación, valor | Importaciones de turismos desde China por tipo de motor | Sí. El arancel es solo para 8703 80 10: dicho en notas |
| CO-D2 | Comext DS-045409, 27 países y EU, US, TOTAL, exportación, 2025; `nama_10_gdp` B1GQ CP_MEUR 2025 | Exportaciones a EE. UU. en % del PIB, 2025 | Sí |

`revisar.py pieza comercio`: un REVISAR por «14,7 %» (cuota de la UE en las exportaciones mundiales de 2024 y cuota de EE. UU. en las importaciones de la UE en 2002). Son datos distintos.

## Autoevaluación (paso 7b)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada; ninguna cifra de titular está en dos gráficos. "Compra a uno y vende a otro" solo se cuenta en G3; el antiguo CO-E2, que lo repetía, sale. N05 se enlaza sin repetir su cuota de eléctricos.
- [x] Dos gráficos explicativos o más: G3 (saldo bilateral), E2 (gas por origen), E3 (coches chinos por tipo de motor) y D2 (exportaciones a EE. UU. en relación con el PIB).
- [x] Ficha de política: derechos compensatorios a los eléctricos chinos (Reglamentos 2024/1866 y 2024/2754), con enlaces a EUR-Lex.
- [x] Párrafo de "Lo que no dicen estos datos".
- [x] Enlaces a Energía y a N05.
- [x] Los filtros coinciden con subtítulos y notas.
- [x] Las notas de los gráficos no repiten el texto.
- [x] Tres cosas que aprende un lector: 1) el superávit con EE. UU. solo cubre algo más de la mitad del déficit con China; 2) tras los aranceles, China vende menos eléctricos a la UE pero casi lo mismo en total, porque crecen los híbridos; 3) la UE ha cambiado gas ruso por noruego y estadounidense, y ahora depende más de EE. UU. también para la energía.

## Cambios del 20 de octubre de 2026

- Fuera: CO-E2 (exportaciones por destino), que repetía el hallazgo de G3.
- Nuevos: CO-G3 (`cg3-saldo-bilateral`), CO-E2 (`ce3-gas-origen`), CO-E3 (`ce4-coches-china`) y CO-D2 (`cd3-exposicion-eeuu`). La dependencia energética pasa de D2 a D3.
- CO-G2 tiene titular con cifras. Quitadas dos afirmaciones sin fuente: "gracias a su esquisto bituminoso" (Estonia) y "con grandes filiales de multinacionales" (Irlanda y Chipre).
- Pipeline: nuevo lector `sources.comext` (Comext de Eurostat), documentado en el manual.
