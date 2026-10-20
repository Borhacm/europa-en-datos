# A06. Defensa y seguridad (20 de octubre de 2026)

Tema nuevo del calendario (`a06`, código DF). Se lleva aquí la nota N07 (gasto en defensa por país, en % del PIB), que estaba en Comercio. No se repiten sus hallazgos ni el de AN02 (gasto militar en % del PIB de los tres bloques): se enlazan, y este tema cuenta el gasto en dinero, el comercio de armas, en qué se gasta y el gasto por habitante.

## Guion

1. ¿Cuánto gastan en defensa la UE, EE. UU., China y Rusia, en dinero, y cuánto ha cambiado desde 2021? → G1
2. ¿Quién vende armas y qué ha pasado con Rusia? → G2
3. ¿Compra Europa sus armas fuera? → E1
4. ¿En qué se va el gasto europeo en defensa y cómo ha cambiado? → E2 (explicativo: composición)
5. ¿Cuánto gasta cada país por habitante? → D1
6. ¿Qué parte de su gasto invierte cada país en equipos? → D2 (explicativo: composición)
7. ¿Qué ha decidido la UE? → ficha del Reglamento (UE) 2025/1106 (SAFE); la cláusula de escape para defensa ya está en Finanzas públicas, que se enlaza

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| Banco Mundial `MS.MIL.XPND.CD` (SIPRI, dólares corrientes) | 1, 5 | G1 y D1 |
| Banco Mundial `MS.MIL.XPRT.KD` (SIPRI, TIV) | 2 | G2 |
| Banco Mundial `MS.MIL.MPRT.KD` (SIPRI, TIV) | 3 | E1 |
| Banco Mundial `SP.POP.TOTL` | 5 | D1 |
| Eurostat `gov_10a_exp` (COFOG GF02 por operación, MIO_EUR) | 4, 6 | E2 y D2 |
| Banco Mundial `MS.MIL.XPND.GD.ZS` (% del PIB) | ninguna | Descartada: es el hallazgo de AN02 (bloques) y N07 (países), que se enlazan |
| Banco Mundial `MS.MIL.XPND.ZS` (% del gasto público) | 1 | Descartada: repite la idea de E2 de Finanzas públicas (cuánto pesa la defensa en el presupuesto) |
| Banco Mundial `MS.MIL.TOTL.P1` (efectivos) | 5 | Descartada: el último año es 2020 |
| Eurostat `gov_10a_exp` GF0203 (ayuda militar exterior) | 4 | Descartada como gráfico: valores muy pequeños por país (0,5 % del PIB como máximo); su efecto se ve en las transferencias de E2 |
| SIPRI, Trends in International Arms Transfers 2025 (hoja de marzo de 2026) | 3 | Descartada: la web del SIPRI no respondía el 20/10/2026 y no se pudo comprobar la parte de EE. UU. en las importaciones europeas |
| OTAN, Defence Expenditure of NATO Countries | 4, 6 | Descartada: solo 23 países de la UE y con la definición de la OTAN; se usa la COFOG de Eurostat, que cubre a los 27 |

## Solapes con lo publicado

- `solapes MS.MIL defensa`: AN02 (`an02-defensa`, % del PIB de la UE, EE. UU. y China) y N07 (`n07-defensa-paises` y `n07-defensa-cambio`, % del PIB por país). Este tema no da ninguna cifra en % del PIB, salvo las pautas de la OTAN en el párrafo de límites. Enlaza AN02 desde Gigantes y N07 desde Por dentro.
- Finanzas públicas E2 (`gov_10a_exp`, COFOG por funciones): da la defensa como parte del presupuesto (1,5 % del PIB en la UE). Este tema usa el mismo dataset para otra pregunta: la composición del gasto en defensa (E2) y la inversión por país (D2). La cláusula de escape, que está en la ficha de Finanzas, se enlaza en lugar de repetirla.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| UE 2025: unos 461.000 millones de dólares; EE. UU. 954.400; China 335.500; Rusia 190.400; 2,4 veces Rusia | 460,6; 954,4; 335,5; 190,4; 460,6/190,4 = 2,42 | dfg1-gasto-dolares |
| Desde 2021: UE +76 %, EE. UU. +18 %, China +17 %, Rusia +189 % | 460,6/261,4; 954,4/806,2; 335,5/286,1; 190,4/65,9 | dfg1-gasto-dolares |
| EE. UU. gastó menos en 2025 que en 2024, cuando superó el billón | 954,4 frente a 1.004,9 | dfg1-gasto-dolares |
| Rusia 2016-2020 casi tanto como la UE; 2021-2025 un 64 % menos y menos de la cuarta parte que la UE | 29,32 frente a 31,55; 10,41/29,32; 10,41/42,77 = 0,24 | dfg2-exportaciones-armas |
| UE +36 %, EE. UU. +27 %, China +11 % | 42,77/31,55; 64,66/50,76; 8,58/7,76 | dfg2-exportaciones-armas |
| Importaciones de los 27 triplicadas | 26,73/8,68 = 3,08 (nota de dfe1) | dfe1-importaciones-armas |
| Polonia, casi diez veces más; luego Países Bajos y Alemania | 5,58/0,59 = 9,5; 2,77; 2,58 | dfe1-importaciones-armas |
| Solo Luxemburgo, Italia, Finlandia e Irlanda importaron menos | filas | dfe1-importaciones-armas |
| Personal 54 % (2014) → 39 % (2024); inversión 15,5 → 21,6; transferencias 2,3 → 8,4, casi todo desde 2022 (2,0 en 2021) | filas | dfe2-composicion-gasto |
| Los sueldos no han bajado | 54 % de 136.412 = 73.700 millones; 39 % de 266.360 = 103.900 millones | dfe2-composicion-gasto |
| Gasto en defensa: 136.412 millones (2014) → 266.360 millones (2024), casi el doble | nota de dfe2; 1,95 veces | dfe2-composicion-gasto |
| Por habitante 2025: Dinamarca 2.488 (89 % de EE. UU., 2.792); Países Bajos 1.600; Suecia 1.555; Finlandia 1.431; Malta 215; Irlanda 283 | filas | dfd1-gasto-habitante |
| Polonia, sexta por habitante (1.283) y la primera en % del PIB | filas; 4,5 % en n07-defensa-paises | dfd1, n07 |
| España 815; Italia 817; Grecia 805 | filas | dfd1-gasto-habitante |
| Inversión 2024: Estonia 43,6; Polonia 38,9; Lituania 37,6; Hungría 37,2; Irlanda 7,7; Bulgaria 9,3; Finlandia 9,6; Alemania 14,3; España 21,5 | filas | dfd2-inversion-paises |
| SAFE: Reglamento del Consejo de 27/05/2025, art. 122 TFUE; hasta 150.000 millones en préstamos (art. 6); solicitudes hasta el 30/11/2025 con un plan (art. 7); hasta 45 años con 10 de carencia (considerando 28); componentes de fuera de la UE, el EEE y Ucrania, como máximo el 35 % en las compras en común (considerando 19 y art. 16); en vigor al día siguiente de publicarse (art. 23) | EUR-Lex, versión ES | sources |
| Cláusula de escape en 18 países | página del Consejo (ver Finanzas públicas) | sources |
| Pautas de la OTAN: 2 % (Gales, 2014) y 3,5 % (La Haya, 2025) | declaraciones citadas también en N07 | sources |

## Filtros

| Gráfico | Consulta (filtros) | Lo que dice el subtítulo | ¿Coinciden? |
|---|---|---|---|
| G1 | `MS.MIL.XPND.CD`, EUU/USA/CHN/RUS, 2000-2025, /1e9 | gasto militar, miles de millones de dólares corrientes, 2000-2025 | Sí |
| G2 | `MS.MIL.XPRT.KD`, sumas de 2016-2020 y 2021-2025, /1e9 | exportaciones, miles de millones de TIV, dos periodos | Sí |
| E1 | `MS.MIL.MPRT.KD`, 27 países (y EUU en la nota), mismos periodos | importaciones, miles de millones de TIV, dos periodos | Sí |
| E2 | `gov_10a_exp` EU27_2020 S13 GF02 MIO_EUR; D1, P2, P51G, D7+D9 entre TE | gasto en defensa por tipo, % del total, 2014-2024 | Sí |
| D1 | `MS.MIL.XPND.CD` / `SP.POP.TOTL`, 2025 | gasto militar por habitante, dólares corrientes, 2025 | Sí |
| D2 | `gov_10a_exp` S13 GF02 MIO_EUR 2024; P51G entre TE | inversión en % del gasto en defensa, 2024 | Sí |

Los titulares se calculan con los datos en el pipeline, con `assert` para las afirmaciones que no son cifras (menos de la mitad que EE. UU., más que China; Rusia baja y la UE sube; dos países por debajo de 300 dólares).

Se añade Rusia (`RUS`) a `pipeline/lib/geo.py` sin código de Eurostat, para que no entre en gráficos de Eurostat ya publicados. Todas las consultas que usan `from_iso3` piden sus países de forma explícita, así que ningún otro gráfico cambia.

`revisar.py pieza defensa`: 0 avisos. El apartado 4 señala `gov_10a_exp` en Finanzas públicas E2: es otra pregunta (el presupuesto por funciones), ver solapes.

## Autoevaluación (paso 7b)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza publicada (el % del PIB queda en AN02 y N07 y la cláusula de escape en Finanzas, enlazados), y ninguna cifra de titular está en dos gráficos.
- [x] Dos gráficos explicativos o más: E2 (composición del gasto en defensa por tipo) y D2 (composición por país: parte que se invierte).
- [x] Ficha de política con enlace oficial: Reglamento (UE) 2025/1106 (SAFE), en EUR-Lex.
- [x] Párrafo de "Lo que no dicen estos datos".
- [x] Enlace a otra pieza publicada en el texto: AN02, N07 y Finanzas públicas.
- [x] Los filtros de cada consulta coinciden con los subtítulos y las notas.
- [x] Las notas de los gráficos no repiten el texto: explican definiciones (SIPRI, TIV, COFOG) y qué falta. El total de importaciones de la UE va solo en la nota de E1.
- [x] Tres cosas que aprende un lector que sigue la prensa: 1) Rusia ha triplicado su gasto militar desde 2021, pero exporta un 64 % menos de armas y ya menos de la cuarta parte que la UE; 2) en 2014 más de la mitad del gasto europeo en defensa eran sueldos, y en 2024 el 39 %; 3) Polonia, el país que más gasta en % del PIB, es sexto por habitante, y Dinamarca gasta por habitante casi como EE. UU.
