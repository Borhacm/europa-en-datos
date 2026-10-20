# A05. Finanzas públicas (20 de octubre de 2026)

Tema nuevo del calendario (`a05`, código FP). Se lleva aquí la nota N06 (deuda pública), que estaba en Productividad, y se enlaza sin repetir su hallazgo: la deuda la cuenta N06; este tema cuenta el déficit, los intereses, los impuestos y el gasto.

## Guion

1. ¿Gasta EE. UU. más de lo que ingresa que la UE y China, y desde cuándo? → G1
2. ¿Cuánto de ese déficit son intereses de la deuda? → G2 (explicativo: descomposición del déficit en saldo primario e intereses)
3. ¿Cuánto recauda cada bloque y con qué impuestos? → E1 (explicativo: composición)
4. ¿En qué gastan las administraciones de la UE y de EE. UU.? → E2 (explicativo: composición)
5. ¿Qué países de la UE incumplen el déficit del 3 %? → D1
6. ¿Ha subido lo que cada país paga en intereses desde que el BCE subió los tipos? → D2
7. ¿Qué ha decidido la UE? → ficha del Reglamento (UE) 2024/1263, procedimientos de déficit excesivo abiertos y cláusula de escape para defensa

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| FMI WEO `GGXCNL_NGDP` (UE, EE. UU., China) | 1 | G1 |
| FMI Fiscal Monitor `GGXCNL_G01_GDP_PT` y `GGXONLB_G01_GDP_PT` | 2 | G2 (la UE, ponderando a los 27 por `NGDPD`) |
| FMI WEO `NGDPD` | 2, 3 | Ponderaciones de G2 y peso de Chipre en E1 |
| OCDE Global Revenue Statistics `DF_RSGLOBAL` | 3 | E1 (cubre a 26 de los 27, EE. UU. y China con la misma clasificación) |
| Eurostat `gov_10a_exp` (COFOG, UE27) | 4 | E2 |
| OCDE Government at a Glance `DF_GOV_COFOG_YU` (COFOG, EE. UU.) | 4 | E2 |
| Eurostat `gov_10dd_edpt1` (B9, D41PAY) | 5, 6 | D1 y D2 |
| Eurostat `gov_10a_taxag` | 3 | Descartada: no tiene EE. UU. ni China; la OCDE da los tres bloques con la misma clasificación |
| OCDE Revenue Statistics `DF_RSOECD` | 3 | Descartada: no incluye China ni a los países de la UE que no son de la OCDE |
| FMI Public Finances in Modern History (`ie`, `rev`, `exp`) | 2 | Descartada: sin agregado de la UE y con datos hasta 2024 sin desglose del saldo primario |
| FMI WEO `GGXWDG_NGDP` (deuda) | ninguna | Descartada: es el hallazgo de N06, que se enlaza |
| Eurostat `gov_10a_main` (ingresos y gastos totales) | 3, 4 | Descartada: los totales salen ya en las notas de E1 y E2 |
| OCDE SOCX (gasto social) | 4 | Descartada: ya la usa Libertades (E3), que se enlaza |

## Solapes con lo publicado

- `solapes gov_10 imf deuda déficit impuest gasto interes`: N06 usa `GGXWDG_NGDP` (deuda de los bloques) y `gov_10dd_edpt1` (deuda por país). Este tema usa el mismo dataset de Eurostat, pero para el déficit y los intereses, no para la deuda; N06 se enlaza desde Gigantes y desde el párrafo de límites.
- Libertades E3 (`le2-gasto-social`, SOCX): gasto social de cada país frente a EE. UU. E2 cuenta otra cosa (todo el presupuesto por funciones, UE frente a EE. UU.) y enlaza Libertades.
- Sanidad (`sag1`, `sae1`): gasto sanitario total y parte pública. E2 da solo el gasto público en sanidad dentro del presupuesto; el texto no repite sus cifras.
- AN02 y N07 (`MS.MIL.XPND.GD.ZS`): gasto militar del SIPRI. E2 da defensa según la COFOG (1,5 % de la UE frente a 3,1 % de EE. UU.), con otra definición: lo dice la nota de E2.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| EE. UU. por encima del 3 % en 21 de 24 años; por debajo en 2001, 2006 y 2007 | -0,5, -2, -2,9 en esos años; el resto, < -3 | fpg1-deficit |
| UE por encima del 3 % en 10 años, 9 en 2009-2012 y desde 2020 | 2003, 2009-2012, 2020-2024 | fpg1-deficit |
| 2020: EE. UU. 14,1 %, UE 6,7 % | -14,1 y -6,7 | fpg1-deficit |
| 2024: EE. UU. 7,8 %, UE 3,1 %, China 7,2 % | -7,8, -3,1, -7,2 | fpg1-deficit |
| China: hasta 2015 nunca por encima del 3 %; desde 2016, todos los años | máximo hasta 2015: -2,8 (2002); 2016-2024 < -3 | fpg1-deficit |
| Intereses netos 2024: EE. UU. 3,2 %, UE 1,5 %, China 0,9 % | 7,8-4,6; 3,1-1,6; 7,2-6,3 | fpg2-intereses |
| Déficit primario: EE. UU. 4,6 %, UE 1,6 %, China 6,3 % | primario | fpg2-intereses |
| Saldo de la UE ponderado (Fiscal Monitor) = agregado WEO | -3,11 frente a -3,1 | cálculo en el registro |
| Impuestos 2023: UE 38,6 %, EE. UU. 25,6 % | notas de fpe1 | fpe1-impuestos |
| Renta: 12,4 y 12,4; cotizaciones 12,6 y 6; consumo 11 y 4,2; propiedad 1,7 y 2,9; otros 0,9 y 0 | filas | fpe1-impuestos |
| Diferencia de 13 puntos | 38,6 - 25,6 | fpe1-impuestos |
| Chipre, menos del 0,3 % del PIB de la UE | 0,19 % en 2023 (FMI `NGDPD`) | fuente citada en fpe1 |
| Gasto 2024: UE 48,9 %, EE. UU. 39,6 %; diferencia 9,3 | suma de funciones | fpe2-gasto-funciones |
| Protección social 19,6 y 7,8 (11,8 más) | GF10 | fpe2-gasto-funciones |
| EE. UU. gasta más en 5 de las otras 7 partidas: sanidad 10,3/7,3, servicios generales 6,9/6,1, educación 5,6/4,7, defensa 3,1/1,5, orden público 1,8/1,7 | filas | fpe2-gasto-funciones |
| Vejez, 10,7 % del PIB en la UE | GF1002, nota de fpe2 | Eurostat gov_10a_exp |
| 10 de 27 con déficit > 3 % en 2025: Rumanía 7,9, Polonia 7,3, Bélgica 5,2, Francia 5,1 | filas | fpd1-deficit-paises |
| 5 con superávit: Chipre 3,4, Dinamarca 2,9, Irlanda 1,8, Grecia 1,7, Portugal 0,7; España -2,4 | filas | fpd1-deficit-paises |
| Grecia, el país más endeudado | 146,1 % en 2025, el más alto | n06-deuda-paises |
| Procedimientos abiertos: AUT, BEL, BGR, FIN, FRA, HUN, ITA, POL, ROU, SVK | página de la Comisión, consultada el 20/10/2026 | sources |
| Intereses suben en 23 de 27 desde 2021; bajan en PRT, CYP, IRL, HRV | filas 2021 y 2025 | fpd2-intereses-paises |
| Italia 3,9, Hungría 3,8 (+1,6, la mayor subida); Luxemburgo 0,3; Estonia e Irlanda 0,5; España 2,4 (+0,3) | filas | fpd2-intereses-paises |
| BCE: primera subida en julio de 2022 | comunicado del 21/07/2022 ("first step") | sources |
| Reglamento 2024/1263: 29/04/2024, en vigor el 30/04/2024; gasto neto (art. 2); 3 % y 60 % (art. 6); 1 punto si deuda > 90 %, 0,5 entre 60 % y 90 % (art. 7); margen de 1,5 % (art. 8); cuatro años ampliables tres (considerando 14) | EUR-Lex, versión ES | sources |
| Cláusula de escape: 18 países desde julio de 2025, hasta 1,5 % del PIB al año en 2025-2028 | página del Consejo, consultada el 20/10/2026 | sources |

## Filtros

| Gráfico | Consulta (filtros) | Lo que dice el subtítulo | ¿Coinciden? |
|---|---|---|---|
| G1 | `GGXCNL_NGDP`, EU/USA/CHN, 2001-2024 | saldo, % del PIB, 2001-2024 | Sí |
| G2 | `GGXONLB_G01_GDP_PT` y `GGXCNL_G01_GDP_PT`, 2024, en positivo | déficit sin y con intereses netos, 2024 | Sí |
| E1 | `DF_RSGLOBAL`, TAX_REV, S13, PT_B1GQ y USD, 2023, `CTRY_SPECIFIC_REVENUE=_T` | ingresos tributarios por tipo, % del PIB, 2023 | Sí |
| E2 | `gov_10a_exp` S13 TE PC_GDP 2024; OCDE USA GE PT_B1GQ S13 2024 | gasto por funciones, % del PIB, 2024 | Sí |
| D1 | `gov_10dd_edpt1` B9 S13 PC_GDP 2025 | saldo, % del PIB, 2025 | Sí |
| D2 | `gov_10dd_edpt1` D41PAY S13 PC_GDP 2021 y 2025 | intereses pagados, % del PIB, 2021 y 2025 | Sí |

Los titulares de G1, G2, E1, E2, D1 y D2 se calculan con los datos en el pipeline, con comprobaciones (`assert`) de las afirmaciones que no son cifras (que la renta recauda lo mismo, que EE. UU. gasta más en sanidad y defensa).

`revisar.py pieza finanzas`: el «3 %» de los titulares de G1 y D1 es el valor de referencia del Tratado (contexto). Las cifras repetidas entre miradas (1,5; 1,7; 2,9; 3,1; 7,3; 7,8) son coincidencias de medidas distintas (por ejemplo, 7,8 % es el déficit de EE. UU. en G1 y su gasto en protección social en E2).

## Autoevaluación (paso 7b)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada (la deuda queda en N06 y el gasto social por país en Libertades, enlazados), y ninguna cifra de titular está en dos gráficos salvo el umbral del 3 %.
- [x] Dos gráficos explicativos o más: G2 (descomposición del déficit), E1 (composición de los impuestos) y E2 (composición del gasto).
- [x] Ficha de política con enlace oficial: Reglamento (UE) 2024/1263, en EUR-Lex, con los procedimientos abiertos (Comisión) y la cláusula de escape (Consejo).
- [x] Párrafo de "Lo que no dicen estos datos".
- [x] Enlace a otra pieza publicada en el texto: N06 y Libertades.
- [x] Los filtros de cada consulta coinciden con los subtítulos y las notas.
- [x] Las notas de los gráficos no repiten el texto: explican definiciones, ponderaciones y diferencias de fuente.
- [x] Tres cosas que aprende un lector que sigue la prensa: 1) la UE y EE. UU. recaudan lo mismo en impuestos sobre la renta; los 13 puntos de diferencia son cotizaciones e impuestos sobre el consumo; 2) EE. UU. ya gasta más dinero público en sanidad que la UE, en % del PIB; 3) los diez países con procedimiento de déficit excesivo son exactamente los diez que superaron el 3 % en 2025, y aun sin intereses el déficit de EE. UU. casi triplica el de la UE.
