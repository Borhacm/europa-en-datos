# P3. Notas: temas, ampliación de N01 y límites (20 de octubre de 2026)

P3 de la auditoría del 19 de octubre (`auditoria-2026-10-19.md`).

## Temas reasignados

| Nota | Antes | Ahora | Motivo |
|---|---|---|---|
| N01 (vivienda desde 2015) | Libertades | Vivienda | El tema de vivienda ya existe y enlazaba la nota con `notes: ["n01"]` |
| N04 (luz de los hogares) | Comercio | Energía | Ídem con `notes: ["n04"]` |
| N05 (coche eléctrico) | Libertades | Energía | No hay tema de transporte; el coche eléctrico es consumo de energía en el transporte (EN-E1) |

Se quitan los `notes: [...]` de Vivienda y Energía, que ya no hacen falta. El campo `theme` de los gráficos de las tres notas se regenera con el pipeline (`--only n01`, `n04`, `n05`): solo cambia ese campo y la fecha.

N06 sigue en Productividad (no existe aún Finanzas públicas) y N07, en Comercio (no existe Defensa); se revisarán si se crean esos temas.

## N01 ampliada

- Nuevo gráfico N01-2 (`n01-alquiler-compra`): subida de la compra (`prc_hpi_a`) frente al alquiler (`prc_hicp_aind`, CP041) entre 2015 y 2025.
- No repite Vivienda: VI-G2 compara alquileres de la zona del euro y EE. UU. (OCDE) hasta 2024; N01-2 compara compra y alquiler por país en la UE.

| Cifra | Valor en el JSON |
|---|---|
| Alquiler UE +20,5 %; compra tres veces más | 20,5; 61,9 / 20,5 = 3,0 |
| 25 de 26 países con más subida de compra; solo Finlandia al revés | conteo; FIN alquiler 18,4, compra -1,0 |
| Hungría 266,6 % frente a 105,4 %; Portugal 163,9 % frente a 36,4 % | idénticos; las dos mayores distancias |
| España 80,6 % frente a 13,6 % | idénticos |

## Frase de límites en cada nota

Añadida al final de N01, N02, N03, N04, N05, N06, N07, AN01 y AN02, con `updated: "2026-10-20"`, que la página de la nota muestra ahora como «revisada el». Todas son afirmaciones de definición (qué mide cada dato) salvo la de N03, que se apoya en la población del Banco Mundial (EE. UU. de 282,2 a 341,8 millones entre 2000 y 2025, +21 %; UE de 429,3 a 451,1 millones, +5 %), añadida a sus fuentes.

## Comprobaciones

- `npm run build` y `npm run check`: 288 gráficos comprobados en 50 páginas.
- Vivienda lista N01; Energía, N04 y N05; Libertades ya no lista notas; Comercio, N07 (N05 aparece además por el enlace «see» del texto de Comercio, junto al gráfico de coches chinos).
- Captura de N01-2 a 390 px.
