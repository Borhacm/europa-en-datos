# LI. Libertades, bienestar y clima (publicado el 25 de septiembre de 2026; rehecho el 19 de octubre de 2026)

Rehecho por la auditoría del 19 de octubre (`auditoria-2026-10-19.md`): unas 100 palabras por mirada, ningún gráfico explicativo, sin ficha ni evidencia, sin límites ni enlaces, y un ranking de renovables que repetía el de Energía.

## Guion

1. ¿Es la UE más democrática que EE. UU. y China, y qué ha cambiado? → G1
2. ¿Qué parte de la democracia de EE. UU. se ha deteriorado en 2025? → G2 (explicativo: descomposición del índice)
3. ¿Se vive más en Europa? → G3
4. ¿Ha recortado la UE sus emisiones o las ha trasladado a lo que importa? → E1 y E2 (explicativo: producción frente a consumo)
5. ¿Cuánto gasta Europa en protección social y qué consigue con ello? → E3 y D3 (explicativo: pobreza antes y después de las transferencias)
6. ¿Qué países de la UE retroceden en democracia? → D1
7. ¿Qué puede hacer la UE cuando un país vulnera el Estado de derecho, y ha servido? → ficha del Reglamento (UE, Euratom) 2020/2092 y de su aplicación a Hungría, con D2

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| V-Dem v16, `v2x_libdem` | 1, 6 | G1, D1, D2 |
| V-Dem v16, componentes (`v2xlg_legcon`, `v2x_jucon`, `v2xcl_rol`, `v2x_freexp_altinf`, `v2x_frassoc_thick`, `v2xel_frefair`) | 2 | G2 |
| Banco Mundial `SP.DYN.LE00.IN` | 3 | G3 |
| Eurostat `demo_mlexpec` (esperanza de vida por país) | 3 | Descartada: es terreno de Sanidad y no tiene EE. UU. ni China |
| Banco Mundial `EN.GHG.CO2.MT.CE.AR5` (EDGAR) | 4 | E1 |
| OCDE, Greenhouse Gas Footprints 2025 (`DF_ICIO_GHG_MAIN_2025`) | 4 | E2 |
| Banco Mundial `EN.GHG.CO2.PC.CE.AR5` (CO₂ por habitante) | 4 | Retirada (era LI-G3): E2 da las emisiones por habitante de producción y de consumo, que responden mejor a la pregunta |
| Eurostat `env_air_gge` (gases de efecto invernadero por sector y país) | 4 | Descartada: el desglose por sectores encaja en Energía y en el futuro tema de Transporte |
| Eurostat `nrg_ind_ren` | 4 | Retirada (era LI-D3): repetía el ranking de Energía (EN-D1); se enlaza |
| OCDE SOCX (`DF_SOCX_AGG`) | 5 | E3 |
| Eurostat `spr_exp_sum` (ESSPROS) | 5 | Descartada: no tiene EE. UU. |
| Eurostat `ilc_li10` y `ilc_li02` | 5 | D3 |
| Eurostat `ilc_peps01n` (riesgo de pobreza o exclusión) | 5 | Retirada (era LI-D2): nivel sin explicación; D3 cuenta qué hace el Estado de bienestar |
| Freedom House, RSF | 1, 6 | Descartadas: sus condiciones de uso no permiten republicar los datos |
| EUR-Lex: Reglamento (UE, Euratom) 2020/2092 y Decisión de Ejecución (UE) 2022/2506 | 7 | Ficha |
| EUR-Lex: Reglamento (UE) 2021/1119, Ley Europea del Clima | 4 | Contexto de E1 y E2 |

## Solapes con lo publicado

- `nrg_ind_ren` y "renovables": EN-E1, EN-D1 y el antiguo LI-D3. Se retira LI-D3 y el texto enlaza Energía.
- `vdem`: IA-E2 (control de internet) usa otra variable; sin solape.
- CO₂ y emisiones: solo estaban en este tema. EN-G1 habla de consumo de energía, no de emisiones.
- SILC: Vivienda usa sobrecarga y hacinamiento; D3 usa pobreza de ingresos. Sin solape.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| EE. UU. 0,57 en 2025, el más bajo desde 2000 | USA 2025 0,571; mínimo de la serie | LI-G1 |
| 0,85 en 2015, mediana UE 0,79 | 0,848; 0,786 | LI-G1 |
| Otros años por debajo, nunca a más de 0,05 (2017 a 2021) | por debajo en 2001, 2002, 2005, 2006, 2017-2021 y 2024; mayor distancia fuera de 2025: 0,04 | LI-G1 |
| Distancia 0,17; mediana UE 0,74; China 0,04 | 0,741 - 0,571; 0,741; 0,039 | LI-G1 |
| Elecciones limpias 0,90 sin cambios | 0,900 y 0,902 | LI-G2 |
| Control legislativo 0,86 a 0,61; expresión 0,90 a 0,73; igualdad ante la ley 0,93 a 0,82; control judicial 0,90 a 0,84 | 0,863/0,610; 0,904/0,729; 0,931/0,822; 0,902/0,844 | LI-G2 |
| Esperanza de vida 2024: UE 81,6, EE. UU. 78,9, China 78,0 | 81,561; 78,890; 78,017 | LI-G3 |
| Desde 2010: UE casi dos años, China algo más de dos, EE. UU. menos de medio | +1,93; +2,35; +0,35 | LI-G3 |
| CO₂ 2024: UE -35,3 %, EE. UU. -7,1 %, China 5,4 veces | índice 64,7; 92,9; 543,6 | LI-E1 |
| Ley Europea del Clima: -55 % netas en 2030 frente a 1990; neutralidad en 2050 | Reglamento (UE) 2021/1119, art. 4 y considerandos | EUR-Lex |
| 2022: producción 8,1 t y huella 10,2 t por habitante en la UE; huella un 26 % mayor | 8,10; 10,24; 10,24 / 8,10 = 1,264 | LI-E2 |
| China produce más de lo que consume | 9,80 frente a 8,97 | LI-E2 |
| Desde 2005: huella -21,3 %, producción -24,6 % por habitante | 13,01 a 10,24; 10,74 a 8,10 | LI-E2 |
| China 9,0 t de huella; EE. UU. 22,2 t; menos de la mitad | 8,97; 22,21; 10,24 / 22,21 = 0,46 | LI-E2 |
| Gasto social 2022: Francia 31,4, Italia 28,2, Alemania 27,7, España 26,0, EE. UU. 19,0 | idénticos | LI-E3 |
| Seis de 22 países por debajo de EE. UU.; Irlanda 12,1 | SVK, NLD, HUN, LTU, EST, IRL; 22 países de la UE con dato en 2022 | LI-E3 |
| 24 de 27 bajan desde 2010; suben Letonia, Estonia (+0,008) e Irlanda (+0,002) | conteo; LVA +0,047 | LI-D1 |
| Hungría 0,68 a 0,32; siguen Grecia, Eslovenia, Polonia y Eslovaquia, todas más de 0,17 | -0,362; -0,244; -0,207; -0,182; -0,179 | LI-D1 |
| Reglamento 2020/2092 de 16/12/2020; afecta o amenaza gravemente la buena gestión financiera | Art. 4.1 y título | EUR-Lex |
| Notificación 27/04/2022; contratación pública, oferta única, conflictos de intereses, corrupción | Considerandos de la Decisión 2022/2506 | EUR-Lex |
| 15/12/2022: 55 % de compromisos de tres programas; fundaciones de la ley IX de 2021 | Art. 2 de la Decisión 2022/2506 | EUR-Lex |
| Informes cada tres meses; levantamiento si se corrige | Art. 3 de la Decisión; art. 7 del Reglamento | EUR-Lex |
| Hungría 0,34 (2022) a 0,32 (2025) | 0,335; 0,315 | LI-D2 |
| Polonia 0,42 (2022), 0,46 (2023), 0,65 (2025), mayor recuperación 2022-2025 | 0,417; 0,457; 0,645; +0,228, el siguiente Chipre +0,019 | LI-D2 |
| Eslovaquia 0,76 a 0,57 | 0,760; 0,573 | LI-D2 |
| Pobreza 2025: 24,4 % antes, 16,3 % después; un tercio | 24,4; 16,3; 8,1 / 24,4 = 0,332 | LI-D3 |
| Más de la mitad en Bélgica, Dinamarca e Irlanda | 52,6 %; 51,8 %; 51,5 % | LI-D3 |
| Grecia 15,5 %; España 23,2 %, quinto más bajo; 25,4 a 19,5 | GRC 0,155; ESP 0,232 tras GRC, ROU, LVA, HUN | LI-D3 |

## Filtros

| Gráfico | Consulta | Subtítulo | ¿Coinciden? |
|---|---|---|---|
| LI-G2 | V-Dem, seis componentes, USA, 2024 y 2025 | Componentes del índice en EE. UU., 2024 y 2025 | Sí |
| LI-E2 | OCDE GHGFP, PROD_GHG y FD_GHG, `_T`, T_CO2E_PS | Gases de efecto invernadero por habitante, producidas y en la demanda final | Sí |
| LI-D2 | V-Dem `v2x_libdem`, HUN, POL, SVK y mediana UE desde 2010 | Índice de democracia liberal desde 2010 | Sí |
| LI-D3 | `ilc_li10` y `ilc_li02`, B_60, MED_EI, TOTAL, T, PC, 2025 | Riesgo de pobreza (60 % de la mediana) antes y después de transferencias, 2025 | Sí. `ilc_li10` excluye las pensiones de las transferencias: dicho en notas y texto |

`revisar.py pieza libertades`: tres REVISAR por cifras coincidentes entre miradas (0,17; 0,57; 55 %). Son datos distintos (distancia EE. UU.-UE y caída de Polonia y Eslovaquia; EE. UU. y Eslovaquia en 2025; objetivo climático y fondos suspendidos), no el mismo hallazgo.

## Autoevaluación (paso 7b)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada; ninguna cifra de titular está en dos gráficos. Las renovables salen del tema y se enlazan con Energía.
- [x] Dos gráficos explicativos o más: G2 (descomposición del índice), E2 (producción frente a consumo), D3 (pobreza antes y después de transferencias).
- [x] Ficha de política: régimen de condicionalidad (Reglamento 2020/2092) y su aplicación a Hungría (Decisión 2022/2506), con enlaces a EUR-Lex.
- [x] Párrafo de "Lo que no dicen estos datos".
- [x] Enlaces a Sanidad, Energía y Vivienda.
- [x] Los filtros coinciden con subtítulos y notas.
- [x] Las notas de los gráficos no repiten el texto.
- [x] Tres cosas que aprende un lector: 1) la caída de EE. UU. en 2025 viene de los contrapesos al presidente, no de las elecciones; 2) la huella de un europeo supera a la de un chino y es un 26 % mayor que lo que emite la UE, pero también ha bajado; 3) Hungría no mejoró tras la suspensión de fondos, mientras Polonia se recuperó tras sus elecciones.

## Cambios del 19 de octubre de 2026

- Fuera: LI-G3 (CO₂ por habitante), LI-D2 (riesgo de pobreza o exclusión, nivel) y LI-D3 (renovables, repetido con EN-D1).
- Nuevos: LI-G2 (`lg4-componentes-democracia`), LI-E2 (`le3-huella-emisiones`), LI-D2 (`ld4-trayectorias-democracia`) y LI-D3 (`ld5-pobreza-transferencias`).
- Corregida la nota de LI-E1, que afirmaba sin datos que parte del recorte se debe a producir fuera; ahora lo mide LI-E2.
- Web: el gráfico de pesas admite `pair` (dos valores de una dimensión) y filas coloreadas con `seriesColors`; bloque `see` para enlazar piezas; campo `updated` en los temas; las tablas ordenan las columnas de una dimensión como las declara el JSON; la etiqueta final de la mediana de la UE se abrevia.
