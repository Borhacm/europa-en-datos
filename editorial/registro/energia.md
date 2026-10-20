# EN. Energía (publicado el 16 de octubre de 2026; completado el 20 de octubre de 2026)

P2 de la auditoría del 19 de octubre: faltaban ficha de política y párrafo de límites, y 25,2 %, 42,5 % y 45,8 % se repetían entre miradas. Además, `revisar.py` detecta dos solapes con otras piezas: el 31,5 % de la luz de los hogares es el hallazgo de N04, y el «3,5 veces» entre la industria de Chipre y la de Finlandia es el titular de AN02-1.

## Guion (sin cambios en los gráficos)

1. ¿Cuánta energía consume cada bloque? → G1
2. ¿De dónde sale su electricidad? → G2
3. ¿Cuánto pesan las renovables y qué se ha fijado la UE? → E1 y ficha de la Directiva (UE) 2023/2413
4. ¿Cuánto paga la industria por la luz? → E2
5. ¿Qué países van por delante en renovables? → D1
6. ¿Dónde paga más la industria? → D2

## Cambios

- Dentro: sin «42,5 %» (ahora «el objetivo de la UE para 2030»), sin «(25,2 %)» y sin la última frase (31,5 % de N04 y 45,8 % de E2).
- Entradilla de dentro: sin «se multiplica por 3,5», que es el titular de AN02-1; las cifras de los países siguen en el texto de D2, que es el gráfico propio del tema.
- Ficha en elige: Directiva (UE) 2023/2413 y enlace a AN02 tras E2.
- Párrafo de límites y enlace a Libertades (emisiones). `updated` y `sources`.

## Verificación de la ficha

| Afirmación | Fuente |
|---|---|
| Directiva (UE) 2023/2413 de 18/10/2023, modifica la 2018/2001 | Título, EUR-Lex |
| Al menos el 42,5 % del consumo final bruto de la Unión en 2030; «velarán conjuntamente»; «procurarán conjuntamente» el 45 % | Art. 1, que sustituye el art. 3.1 de la 2018/2001 |
| Edificios: objetivo indicativo de al menos el 49 % | Art. 15 bis.1 |
| Transporte: al menos el 29 % o reducción del 14,5 % de la intensidad de gases, como obligación a los proveedores de combustible | Art. 25.1 a) |

## Autoevaluación (paso 7b)

- [x] Ficha de política con enlace a EUR-Lex.
- [x] Párrafo de «Lo que no dicen estos datos».
- [x] `revisar.py pieza energia`: 0 cifras repetidas entre miradas.
- [x] Sin repetir N04 ni AN02; los dos se enlazan.
