# SA. Sanidad (publicado el 25 de septiembre de 2026; rehecho el 20 de octubre de 2026)

Rehecho por la auditoría del 19 de octubre (`auditoria-2026-10-19.md`): unas 150 palabras por mirada, un solo gráfico explicativo (SA-E1), sin evidencia sobre resultados, sin ficha, sin límites ni enlaces, y la esperanza de vida repetida de Libertades (LI-G3) con otro año y otras cifras.

## Guion

1. ¿Cuánto gasta en sanidad cada bloque? → G1 y G2
2. ¿En qué se va la diferencia entre EE. UU. y la UE? → G3 (explicativo: gasto por función)
3. ¿Quién paga: el Estado o el paciente? → E1 y E2
4. ¿Compra mejores resultados el gasto de EE. UU.? → E3 (explicativo: mortalidad tratable y prevenible)
5. ¿Cuántos médicos hay en cada país? → D1
6. ¿Quién se queda sin atención, y por qué? → D2
7. ¿Qué puede hacer un paciente que espera demasiado? → ficha de la Directiva 2011/24/UE

## Inventario de fuentes consideradas

| Fuente | Pregunta | Uso |
|---|---|---|
| Banco Mundial (OMS) `SH.XPD.CHEX.GD.ZS`, `SH.XPD.CHEX.PP.CD` | 1 | G1, G2 |
| OCDE `DSD_SHA@DF_SHA` 1.1 (gasto por función, USD PPA por habitante, 2023) + Banco Mundial `SP.POP.TOTL` | 2 | G3 (UE ponderada por población) |
| Banco Mundial `SH.XPD.GHED.CH.ZS`, pago de bolsillo | 3 | E1, E2 |
| OCDE `DSD_HEALTH_STAT@DF_AM` 1.1 (TRTM y PREVM, tasa estandarizada) | 4 | E3 |
| Eurostat `hlth_cd_apr` (mortalidad evitable) | 4 | Descartada: no tiene EE. UU. y usa otra población estándar |
| Banco Mundial `SP.DYN.LE00.IN` (esperanza de vida) | 4 | Retirada del texto: es LI-G3; se enlaza Libertades |
| OCDE `DSD_HEALTH_REAC_EMP@DF_REMUN` (remuneración de médicos) | 2 | Descartada: asalariados y autónomos no comparables entre países |
| OCDE `DSD_SHA@DF_SHA`, HC7 en % del gasto | 2 | Descartada como ranking: muy volátil (Eslovaquia 7,1 % en 2022 y 2,9 % en 2024) |
| Eurostat `hlth_rs_prs2` | 5 | D1 |
| Eurostat `hlth_silc_08` | 6 | D2 |
| EUR-Lex: Directiva 2011/24/UE (considerando 4, arts. 6, 7 y 8) | 7 | Ficha |

## Solapes con lo publicado

- Esperanza de vida: LI-G3 (`lg2-esperanza-vida`). El texto anterior repetía la cifra con otro año (81,4 y 78,4 en 2023 frente a 81,6 y 78,9 en 2024). Se quita y se enlaza Libertades.
- Gasto social: LI-E3 (OCDE SOCX) incluye sanidad pública en otro agregado; no se repite ninguna cifra.
- `revisar.py solapes` para `hlth`, `SHA`, `HEALTH`, «mortalidad», «vida»: sin otros gráficos sobre sanidad.

## Verificación

| Cifra del texto | Valor en el JSON o la fuente | Gráfico o fuente |
|---|---|---|
| 2023: EE. UU. 16,7 %, UE 10 %, China 5,9 %; 2000: 12,5 %, 8,4 %, 4,5 % | 16,69; 10,00; 5,94; 12,49; 8,42; 4,45 | SA-G1 |
| 13.473, 5.806 y 1.487 dólares; 2,3 veces; 2000: 4.549 y 1.814 | idénticos; 13.473 / 5.806 = 2,32 | SA-G2 |
| 2023: EE. UU. 13.933; UE 6.138 en las mismas partidas; diferencia 7.795 | suma de las cinco funciones: 13.933 y 6.138 | SA-G3 |
| Curativa 5.765 de diferencia, tres de cada cuatro | 9.376 - 3.611 = 5.765; 74 % | SA-G3 |
| Administración 886; 1.102 frente a 216, cinco veces | 1.102 - 216; 5,1 | SA-G3 |
| Medicamentos 793; larga duración casi igual | 1.895 - 1.102; 1.065 frente a 989 | SA-G3 |
| Gasto público 74,4 % UE, 54 % EE. UU., 57,1 % China; 2000: 74,8, 44,4, 22 | 74,43; 53,95; 57,1; 74,83; 44,38; 21,98 | SA-E1 |
| Bolsillo 10,9 % EE. UU., 14,9 % UE; menos que EE. UU. solo Luxemburgo, Francia, Croacia; Bulgaria, Letonia, Grecia > 34 %; España 20,9 % | 10,93; 14,88; 8,77, 9,26, 9,38; 35,5, 35,06, 34,3; 20,86 | SA-E2 |
| 1.472 frente a 898 dólares; Malta y Bélgica por encima de EE. UU. | 1.472; 898; 1.765; 1.611 | SA-E2 |
| Tratable 2022: EE. UU. 95; menos en 16 de 24; Luxemburgo 45; Francia, Países Bajos, Suecia 48; España 51 | conteo; idénticos | SA-E3 |
| Los ocho con tasas más altas, todos del este; Rumanía 179 | EST, POL, SVK, HUN, LTU, BGR, LVA, ROU | SA-E3 |
| Prevenible: EE. UU. 217 supera a 18 de 24 | conteo | SA-E3 |
| Médicos: Grecia, Italia, Austria > 560; Letonia y Bélgica ~340; España 464; mediana 410 | 626,9; 575,4; 563,5; 340,2; 334,3; 463,8; 410,1 | SA-D1 |
| Necesidades no cubiertas 2025: UE 2,4 %; Grecia 11,5 % (precio 8,8 %); Finlandia 7,8 %; Estonia 7,7 %; desde 2023 esperas > precio; España 1,6 %, esperas 0,4 % a 1,5 % | idénticos; 2023: 1,2 frente a 1,0 | SA-D2 |
| Directiva 2011/24/UE de 9/03/2011; reembolso si la prestación está cubierta, hasta lo que costaría en casa sin superar el coste real | Arts. 7.1 y 7.4 | EUR-Lex |
| Autorización previa para al menos una noche de hospital o equipos especializados y caros; no puede negarse si no hay plazo médicamente justificado | Arts. 8.2 a) y 8.5 | EUR-Lex |
| Puntos nacionales de contacto; no debe animar a tratarse fuera; cada país sigue siendo responsable | Art. 6.1; considerando 4 | EUR-Lex |

## Filtros

| Gráfico | Consulta | Subtítulo | ¿Coinciden? |
|---|---|---|---|
| SA-G3 | SHA, EXP_HEALTH, USD_PPP_PS, todos los esquemas de financiación, HC1HC2+HC4, HC3, HC5, HC6, HC7, precios corrientes, 2023 | Gasto sanitario corriente por habitante según su destino, en dólares PPA, 2023 | Sí; la suma de HC1HC2 y HC4 se explica en la nota |
| SA-E3 | DF_AM, TRTM y PREVM, DT_10P5HB, ambos sexos, STANDARD, 2022 | Muertes antes de los 75 años evitables, por 100.000, estandarizada, 2022 | Sí |

`revisar.py pieza sanidad`: un REVISAR por «100.000» (es la unidad de E3 y D1, no un hallazgo).

## Autoevaluación (paso 7b)

- [x] Cada pregunta del guion tiene su gráfico o su párrafo con fuente.
- [x] Ningún hallazgo se repite en dos miradas ni en otra pieza; la esperanza de vida sale y se enlaza Libertades.
- [x] Dos gráficos explicativos nuevos: G3 (gasto por función) y E3 (resultados), además de E1.
- [x] Ficha de política: Directiva 2011/24/UE, con enlace a EUR-Lex.
- [x] Párrafo de «Lo que no dicen estos datos».
- [x] Enlace a Libertades.
- [x] Los filtros coinciden con subtítulos y notas.
- [x] Las notas de los gráficos no repiten el texto.
- [x] Tres cosas que aprende un lector: 1) tres cuartas partes del gasto extra de EE. UU. van a atención curativa y su administración cuesta cinco veces más por habitante; 2) con más del doble de gasto, EE. UU. tiene más muertes tratables que 16 de 24 países de la UE; 3) un paciente europeo que no puede tratarse a tiempo en su país tiene derecho a que le autoricen y reembolsen el tratamiento en otro.

## Cambios del 20 de octubre de 2026

- Nuevos: SA-G3 (`sag3-gasto-funciones`) y SA-E3 (`sae3-mortalidad-evitable`).
- Texto: sin la esperanza de vida repetida; ficha, límites, `sources`, `updated` y nueva entradilla.
