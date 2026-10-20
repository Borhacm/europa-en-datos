# A04. Transporte y transición verde (20 de octubre de 2026)

Tema nuevo del calendario (`a04`, código TR). Se lleva aquí la nota N05 (cuota del coche eléctrico en las ventas), que estaba en Energía. No se repite su hallazgo: N05 cuenta qué parte de los coches nuevos son eléctricos; este tema cuenta las emisiones, cómo se mueven los viajeros, qué tipo de motor compran y cuántos eléctricos circulan.

## Guion

1. ¿Ha bajado lo que emite el transporte en la UE, EE. UU. y China? → G1
2. ¿Qué parte de las emisiones es transporte, y cómo ha cambiado? → G2 (explicativo: composición de las emisiones)
3. ¿Se mueven los europeos en tren o en coche? → E1 (explicativo: reparto por modo)
4. ¿Qué coches compran? → E2 (explicativo: composición por motor)
5. ¿Dónde pesa más el tren? → D1
6. ¿Cuántos coches eléctricos circulan en cada país? → D2
7. ¿Qué ha decidido la UE? → ficha del Reglamento (UE) 2023/851 (fin de las emisiones de los coches nuevos en 2035) y estado de la propuesta de 2025

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| JRC, EDGAR 2025 (GHG por sector y país) | 1, 2 | G1 y G2 (UE, EE. UU. y China con la misma metodología, CC BY 4.0) |
| Eurostat `tran_hv_psmod` | 3, 5 | E1 y D1 |
| Eurostat `road_eqr_carpda` | 4 | E2 |
| Eurostat `road_eqs_carpda` | 6 | D2 |
| AIE, Global EV Data Explorer | 4 | Descartada: la descarga pide registrarse y no se puede automatizar |
| Eurostat `env_air_gge` | 1 | Descartada: no tiene EE. UU. ni China |
| Banco Mundial `EN.CO2.TRAN.ZS` | 2 | Descartada: serie interrumpida |
| Eurostat `sdg_12_30` (CO2 de los coches nuevos) | 4 | Descartada: el dataset ya no existe (404) |
| Banco Mundial `IS.RRS.PASG.KM` (pasajeros-km en tren) | 3 | Descartada: cobertura irregular y reciente incompleta |
| EEA, emisiones de CO2 de los coches nuevos | 4 | Descartada: sin API sencilla; la ficha cita el reglamento |
| Eurostat `nrg_ind_ren` (renovables en el transporte) | ninguna | Descartada: ya la usa Energía, que se enlaza |

## Solapes con lo publicado

- `solapes road_ coche eléctric emisiones transporte`: N05 usa `road_eqr_carpda` (cuota del eléctrico de batería por país y en la UE, 17,3 % en 2025). E2 usa el mismo dataset para todos los tipos de motor; el texto no repite la cuota del eléctrico y enlaza N05. D2 usa el parque (`road_eqs_carpda`), no las ventas.
- Libertades (`le1-emisiones-1990`): emisiones totales de CO2 de los bloques. G1 y G2 cuentan solo el transporte y su peso; se enlaza Libertades.
- Comercio (`ce4-coches-china`): importaciones de eléctricos chinos. Sin solape.
- Energía: renovables en el transporte (11,2 %). Se enlaza desde Por dentro.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| Transporte UE 2024: 791 Mt, +21 % frente a 1990 | 791,3 frente a 655,2 | trg1-emisiones |
| Único sector que sube en la UE | `assert` en el pipeline; nota de trg1 | trg1-emisiones |
| Máximo en 2007 (853,8); 2024 por encima de 2000 (780,4) | filas | trg1-emisiones |
| EE. UU. 1.702,8 Mt (más del doble), +17 % | 1.702,8/791,3 = 2,15; 1.702,8/1.456,3 | trg1-emisiones |
| China ×10, 957,4 Mt | 957,4/95,3 = 10,05 | trg1-emisiones |
| Peso del transporte: UE 13,5 → 25 %; EE. UU. 23,4 → 28,8 %; China 6,2 % | filas | trg2-peso-transporte |
| El sector que más emite en la UE, por delante de la electricidad y el calor (598 Mt) | nota de trg2 | trg2-peso-transporte |
| Coche 82 % (2000) → 82,5 % (2024); tren 7,5 → 8,9 %; autobús 10,5 → 8,6 %; tren 7,9 % en 2019 | filas | tre1-reparto-viajeros |
| Datos de 2010-2012: Francia con el tren al 99,1 %; UE marcada `be` de 2009 a 2013 | banderas de Eurostat | tre1-reparto-viajeros |
| Híbridos sin enchufe 25,2 → 33,1 %; gasolina 35,6 → 27,3 %; diésel 14,1 → 9,8 %; enchufables 9,4 % | filas 2023 y 2025 | tre2-combustible-nuevos |
| Casi ocho de cada diez con motor de combustión en 2025 | 33,1 + 27,3 + 9,8 + 9,4 = 79,6 | tre2-combustible-nuevos |
| Tren 2024: Hungría 14, Austria 13,7, Francia 11,6, Suecia 11,3, Países Bajos 11; Grecia 0,6, Lituania 1,1, Bulgaria 2,2; España 8,8 (UE 8,9) | filas | trd1-tren-paises |
| Eléctricos en el parque: UE 0,44 (2020) → 2,88 % (2025); Dinamarca 17,9; Luxemburgo 8,7; Suecia 8,6; Polonia 0,44, Grecia 0,49, Croacia 0,61; España 1,15 | filas | trd2-electricos-parque |
| Reglamento 2023/851: 19/04/2023; -55 % en 2030 y -100 % desde 2035 frente al objetivo de 2021 (art. 1) | EUR-Lex, versión ES | sources |
| -15 % desde 2025; prima por exceso de emisiones; propuesta del 16/12/2025 (90 % en 2035, compensación con acero bajo en carbono de la UE y combustibles renovables); pleno el 23/11/2026; orientación general del Consejo el 11/12/2026 | Legislative Train del Parlamento Europeo (actualizado el 20/09/2026) y página de la Comisión | sources |

## Filtros

| Gráfico | Consulta (filtros) | Lo que dice el subtítulo | ¿Coinciden? |
|---|---|---|---|
| G1 | EDGAR, sector Transport, EU27/USA/CHN, cuatro gases sumados, 1990-2024 | GEI del transporte, Mt CO2e, 1990-2024 | Sí |
| G2 | EDGAR, Transport entre la suma de los ocho sectores, 1990 y 2024 | % del total de emisiones, 1990 y 2024 | Sí |
| E1 | `tran_hv_psmod` EU27_2020 PC, CAR/BUS_TOT/TRN, desde 2000 | reparto por modo, % de pasajeros-km, 2000-2024 | Sí |
| E2 | `road_eqr_carpda` EU27_2020 NR, grupos de motor entre TOTAL, 2023 y 2025 | matriculaciones por motor, % del total, 2023 y 2025 | Sí |
| D1 | `tran_hv_psmod` TRN PC, último año | tren, % de pasajeros-km, 2024 | Sí |
| D2 | `road_eqs_carpda` NR, ELC entre TOTAL, 2020 y 2025 | eléctricos de batería, % del parque, 2020 y 2025 | Sí |

2022 no se usa en E2: ese año Eurostat no da los híbridos de diésel ni los enchufables de diésel para la UE.

`revisar.py pieza transporte`: el «8,6 %» que aparece en Elige y en Por dentro es una coincidencia de dos medidas distintas (el autobús en E1 y Suecia en D2).

## Autoevaluación (paso 7b)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada (la cuota del eléctrico en las ventas queda en N05, enlazada), y ninguna cifra de titular está en dos gráficos.
- [x] Dos gráficos explicativos o más: G2 (peso del transporte en las emisiones), E1 (reparto por modo) y E2 (composición por motor).
- [x] Ficha de política con enlace oficial: Reglamento (UE) 2023/851, en EUR-Lex, con el estado de la propuesta de 2025 en el Parlamento Europeo.
- [x] Párrafo de "Lo que no dicen estos datos".
- [x] Enlace a otra pieza publicada en el texto: N05, Libertades y Energía.
- [x] Los filtros de cada consulta coinciden con los subtítulos y las notas.
- [x] Las notas de los gráficos no repiten el texto: explican definiciones, lo que falta y los problemas de datos.
- [x] Tres cosas que aprende un lector que sigue la prensa: 1) el transporte es el único sector en el que la UE emite más que en 1990, y ya es el que más emite; 2) los híbridos sin enchufe ya son el coche nuevo más vendido, por delante del de gasolina; 3) solo el 2,9 % de los coches que circulan por la UE son eléctricos, a nueve años de 2035.
