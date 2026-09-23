# Inventario de datos: piloto IA + digital

Consultado el 23/09/2026 directamente en las APIs. Los valores son preliminares, sirven para validar viabilidad, no para publicar tal cual.

Leyenda: ✅ viable · ⚠️ viable con matices · ❌ no viable

## Mirada 1. Entre dos gigantes (UE vs EE. UU. vs China)

| # | Bloque | Fuente y código | Cobertura | Estado | Dato preliminar |
|---|---|---|---|---|---|
| G1 | Inversión en I+D (% PIB) | OCDE MSTI `DSD_MSTI@DF_MSTI`, medida `G`, `PT_B1GQ` | USA, CHN, EU27, países UE · hasta 2024 | ✅ | 2024: EE. UU. 3,44 · China 2,69 · UE 2,13. La UE estancada, China subiendo |
| G2 | I+D empresarial (% PIB) | MSTI, medida `B`, `PT_B1GQ` | Igual | ✅ | 2024: 2,67 · 2,09 · 1,41. La brecha está en la empresa, no en lo público |
| G3 | Patentes de IA | OCDE `DSD_PATENTS@DF_PATENTS_OECDSPECIFIC`, tecnología `AI`, PCT (`9P50_1`), inventor, fecha de prioridad | USA, CHN, EU27, países · hasta 2024 | ✅ | 2024: EE. UU. 5.193 · China 4.914 · UE 1.776 |
| G4 | Patentes TIC | MSTI `P_ICTPCT` | Igual · hasta 2023 | ✅ | 2023: China 30.171 · EE. UU. 18.227 · UE 9.036 |
| G5 | Modelos de IA destacados | Epoch AI `notable_ai_models.csv` (CC BY) | Global, por país del desarrollador · al día | ⚠️ | 2025: EE. UU. 64 · China 35 · UE 1. Revisar la clasificación por país a mano |
| G6 | Capital riesgo en IA | OECD.AI (datos de Preqin) | Global | ⚠️ | Visible en OECD.AI, pero Preqin es privado: hay que confirmar si se puede redistribuir. Si no, enlazar y citar cifras agregadas del informe OCDE 2026 |
| G7 | Uso de internet | Banco Mundial WDI `IT.NET.USER.ZS` (dato de la UIT) | Global | ⚠️ | China salta de 75,6 a 90,6 entre 2022 y 2023: probable cambio de método. Señalarlo en el gráfico |
| G8 | Empresas que usan IA | OCDE `DSD_ICT_B@DF_BUSINESSES`, `G14_B` | UE y OCDE. EE. UU. solo 2021, China nada | ❌ | No hay comparación posible entre los tres bloques. Esta pregunta pasa a la mirada "por dentro" |

## Mirada 2. ¿Pierde Europa o elige?

| # | Bloque | Fuente y código | Estado | Dato preliminar |
|---|---|---|---|---|
| E1 | Por qué la gente no usa la IA generativa | Eurostat `isoc_ai_iaiuxr` (2025), unidad `PC_IND_IUAIX` | ✅ | Sobre quienes no la usan: "no la necesito" 64,3 % · "no sé usarla" 13,8 % · "privacidad y seguridad" solo 7,3 %. **El dato contradice el relato de una Europa que elige la prudencia**. (Corregido: la primera versión usaba por error el % sobre toda la población) |
| E2 | Control estatal de internet (filtrado, censura, vigilancia) | V-Dem Digital Society Project, v16 | ✅ (falta descargar) | Contraste directo: China adopta mucho, pero con control estatal |
| E3 | Apertura del comercio digital | OCDE `DSD_STRI@DF_STRI_DIGITAL` + índice INDIGO | ⚠️ (comprobar si incluye China) | Cuánto regula cada bloque lo digital |
| E4 | Modelos abiertos frente a cerrados | Epoch, campo `Model accessibility` | ⚠️ | ¿Apuesta la UE (Mistral) más por los modelos abiertos? |
| E5 | Empresas que usan IA con datos personales | Eurostat `isoc_eb_ai`, `PC_ENT_AI_PDI` | ✅ | Protección de datos en la práctica |
| E6 | Calendario del AI Act | EUR-Lex (cualitativo) | ✅ | Línea de tiempo para dar contexto, sin gráfico de datos |

## Mirada 3. Europa por dentro (27 países)

| # | Bloque | Fuente y código | Cobertura | Estado | Dato preliminar |
|---|---|---|---|---|---|
| D1 | Empresas que usan IA | Eurostat `isoc_eb_ai`, `E_AI_TANY`, `PC_ENT`, 10+ empleados | 35 países · 2021, 2023-2025 | ✅ | 2025: UE 20,0 % · Dinamarca 42,0 · España 20,3 · Rumanía 5,2. **8 veces de diferencia entre el primero y el último** |
| D2 | IA por región (mapa) | Eurostat `isoc_r_eb_ain2` | NUTS 2 · 2023-2025 | ✅ | Mapa de coropletas |
| D3 | IA por tamaño y sector | `isoc_eb_ai` (tamaño) · `isoc_eb_ain2` (sector) | 2021-2025 | ✅ | Brecha entre grandes empresas y pymes |
| D4 | Personas que usan IA generativa | Eurostat `isoc_ai_iaiu`, `I_IUAI` | 37 países · solo 2025 | ✅ | UE 32,7 % · Dinamarca 48,4 · España 37,9 · Alemania 32,3 · Italia 19,9 · Rumanía 17,8 |
| D5 | Competencias digitales básicas | Eurostat `isoc_sk_dskl_i21`, `I_DSK2_BAB` | 2021, 2023, 2025 | ✅ | UE 60,4 % frente al objetivo del 80 % para 2030 (Década Digital) · Países Bajos 83,6 · España 66,5 · Rumanía 31,8 |
| D6 | Empresas que usan la nube | Eurostat `isoc_cicce_use` | 2014-2025 | ✅ | Complemento para mostrar la base digital |

## El ángulo España

España está por encima de la media de la UE en adopción (empresas con IA 20,3 frente a 20,0, IA generativa 37,9 frente a 32,7, competencias 66,5 frente a 60,4). En cambio, está muy por debajo en inversión en I+D (1,50 % del PIB frente a 2,13 %) y en patentes de IA (48 PCT en 2024). **Usa la IA, pero apenas la produce.** Sirve de gancho para el público hispano.

## Tres historias que ya salen de los datos

1. **"Europa usa la IA, pero no la fabrica."** La adopción en la UE se ha multiplicado por 2,6 desde 2021. Pero en modelos destacados, patentes e I+D empresarial la UE va muy por detrás de EE. UU. y de China.
2. **"No es prudencia, es falta de necesidad."** Solo el 7 % de quienes no usan la IA generativa lo hacen por privacidad; el 64 % dice que no la necesita. Esto matiza el relato de una Europa que elige regular.
3. **"Dos Europas digitales."** El norte (Dinamarca, Finlandia, Suecia) está al nivel de cualquier potencia. El este y el sur (Rumanía, Polonia, Bulgaria, Grecia) están 4 a 8 veces por debajo.

## Notas técnicas

- **Eurostat**: API JSON-stat sin clave. El lector está en `pipeline/lib/sources.py`.
- **OCDE**: API SDMX REST (`sdmx.oecd.org/public/rest/data/...`, formato `csvfilewithlabels`). El MCP de la OCDE solo cubre una lista reducida de datasets, así que para el pipeline conviene la API directa.
- **Cuidado 1**: en MSTI, el filtro de `TRANSFORMATION` mezcla niveles y tasas de crecimiento. Hay que fijarlo siempre.
- **Cuidado 2**: las patentes de los 2 o 3 últimos años están incompletas (truncamiento por el retraso en la publicación). Hay que cortar la serie o marcarla.
- **Cuidado 3**: el código de la UE cambia según la fuente (`EU27_2020` en Eurostat y MSTI, `EU27` en OCDE ICT). Hace falta una tabla de equivalencias.
- **Resuelto**: V-Dem v16 descargado (llega a 2025). Asignación de países en Epoch revisada: se usa la regla "participa" (colaboraciones cuentan para cada bloque) y el Reino Unido va aparte.
- **Pendiente**: comprobar la licencia de OECD.AI/Preqin (fuera del piloto).
