import { p, type Note } from "../../lib/content-types";

// Análisis AN02. Fuentes comprobadas el 10/10/2026:
// - Informe: "The future of European competitiveness", parte A (Comisión Europea, 9/09/2024), leído en el PDF original.
// - Discurso de Draghi en la conferencia "un año después" (16/09/2025), leído en el PDF original.
// - Seguimiento: Banco de España (blog, 8/09/2026, datos de julio de 2026, a partir de EPIC y del Real Instituto Elcano);
//   JEDI Draghi Tracker (Euronews, 10/09/2026); Comisión Europea (Brújula, SAFE, hoja de ruta "One Europe, One Market").
// - Datos: N03 (Banco Mundial), PR-G2 (OIT), IA-G1 (OCDE) y los dos gráficos nuevos (Eurostat nrg_pc_205; Banco Mundial/SIPRI).
// Los porcentajes de aplicación de cada seguimiento no son comparables entre sí: cada uno cuenta las propuestas de una forma.

const t = (es: string, en: string) => ({ es, en });

const note: Note = {
  id: "an02",
  kind: "analisis",
  code: "AN02",
  slug: { es: "informe-draghi-dos-anos-despues", en: "draghi-report-two-years-on" },
  title: {
    es: "El informe Draghi, dos años después: qué pedía, qué se ha hecho y qué dicen hoy los datos",
    en: "The Draghi report, two years on: what it asked for, what has been done and what the data say today",
  },
  dek: {
    es: "Mario Draghi avisó en 2024 de que Europa se enfrentaba a un desafío existencial: crece menos, innova menos, paga la energía más cara y depende de otros para su seguridad. Dos años después, el gasto en defensa ha subido con fuerza, pero la inversión y la energía siguen lejos de lo que pedía.",
    en: "In 2024 Mario Draghi warned that Europe faced an existential challenge: it grows less, innovates less, pays more for energy and relies on others for its security. Two years on, defence spending has risen sharply, but investment and energy remain far from what he asked for.",
  },
  published: "2026-10-10",
  lens: "gigantes",
  theme: "productividad",
  body: [
    { h: t("Qué es el informe Draghi", "What the Draghi report is"), id: "que-es" },
    p("En septiembre de 2023, Ursula von der Leyen pidió a Mario Draghi, expresidente del Banco Central Europeo, un informe sobre el futuro de la competitividad europea. Lo entregó el 9 de septiembre de 2024 en dos partes: una estrategia de unas setenta páginas y un análisis detallado por sectores. El Banco de España cuenta en él 176 propuestas, agrupadas en nueve pilares.",
      "In September 2023, Ursula von der Leyen asked Mario Draghi, former president of the European Central Bank, for a report on the future of European competitiveness. He delivered it on 9 September 2024 in two parts: a strategy of around seventy pages and a detailed analysis by sector. The Bank of Spain counts 176 proposals in it, grouped into nine pillars."),
    p("Su tesis es sencilla. Europa necesita crecer más y ser más productiva para pagar a la vez tres cosas: liderar las nuevas tecnologías, descarbonizar su economía y defenderse. Si no lo consigue, tendrá que elegir entre ellas, y tampoco podrá financiar su modelo social. Draghi lo llamó, en el prólogo, \"un desafío existencial\".",
      "His thesis is simple. Europe needs to grow faster and become more productive to pay for three things at once: leading in new technologies, decarbonising its economy and defending itself. If it fails, it will have to choose between them, and will not be able to finance its social model either. In the foreword, Draghi called this \"an existential challenge\"."),

    { h: t("El diagnóstico: Europa crece menos", "The diagnosis: Europe grows less"), id: "diagnostico" },
    p("El punto de partida es el crecimiento. Entre 2000 y 2025, el PIB real de EE. UU. aumentó un 69 %; el de la UE, un 41 %. China lo multiplicó por 6,9. El informe añade que, por habitante, la renta disponible real ha crecido casi el doble en EE. UU. que en la UE desde 2000.",
      "The starting point is growth. Between 2000 and 2025, US real GDP rose 69%; the EU's, 41%. China multiplied its GDP by 6.9. The report adds that, per person, real disposable income has grown almost twice as much in the US as in the EU since 2000."),
    { fig: "n03-crecimiento", code: "N03-1" },
    p("Según Draghi, la causa principal es la productividad: explica en torno al 70 % de la diferencia de PIB por habitante con EE. UU. Los datos posteriores no han cerrado esa brecha. En 2019, la UE producía por hora trabajada un 7 % menos que EE. UU.; en 2024, un 13 % menos.",
      "According to Draghi, the main cause is productivity: it explains around 70% of the gap in GDP per person with the US. Later data have not closed that gap. In 2019, the EU produced 7% less per hour worked than the US; in 2024, 13% less."),
    { fig: "pg2-productividad-hora", code: "PR-G2" },

    { h: t("Tres frentes: innovación, energía y defensa", "Three fronts: innovation, energy and defence"), id: "frentes" },
    p("Innovación. Solo cuatro de las 50 mayores empresas tecnológicas del mundo son europeas, y entre 2008 y 2021 cerca del 30 % de los unicornios fundados en Europa trasladó su sede fuera, casi siempre a EE. UU. El informe calcula que las empresas europeas gastaron en 2021 unos 270.000 millones de euros menos que las estadounidenses en investigación e innovación. Los datos de la OCDE muestran la misma brecha: en 2024, la UE dedicó a I+D el 2,13 % de su PIB, EE. UU. el 3,45 % y China el 2,69 %. China supera a la UE desde 2015. La diferencia está sobre todo en las empresas: las europeas invierten algo más de la mitad que las estadounidenses en proporción al PIB.",
      "Innovation. Only four of the world's 50 largest tech companies are European, and between 2008 and 2021 close to 30% of the unicorns founded in Europe moved their headquarters abroad, nearly always to the US. The report estimates that European companies spent around 270 billion euros less than US ones on research and innovation in 2021. OECD data show the same gap: in 2024 the EU spent 2.13% of its GDP on R&D, the US 3.45% and China 2.69%. China has been ahead of the EU since 2015. The difference lies mainly in business: European companies invest just over half as much as US ones relative to GDP."),
    { fig: "g1-inversion-id", code: "IA-G1" },
    p("Energía. Según el informe, las empresas europeas pagaban la electricidad entre dos y tres veces más cara que las de EE. UU., y el gas, entre cuatro y cinco veces. Eurostat no compara con EE. UU., pero sí muestra cómo ha cambiado el precio dentro de la UE. En el segundo semestre de 2025, una empresa mediana pagaba de media 19,2 céntimos por kWh, un 51 % más que en el mismo semestre de 2019, y el precio había subido en los 27 países. Entre ellos, las diferencias son enormes: 27,6 céntimos en Chipre y 27,3 en Dinamarca, frente a 8,5 en Finlandia. En España, 14,3.",
      "Energy. According to the report, European companies paid two to three times as much for electricity as US ones, and four to five times as much for gas. Eurostat does not compare with the US, but it does show how prices have changed within the EU. In the second half of 2025, a medium-sized business paid 19.2 cents per kWh on average, 51% more than in the same half of 2019, and the price had risen in all 27 countries. The differences between them are huge: 27.6 cents in Cyprus and 27.3 in Denmark, against 8.5 in Finland. In Spain, 14.3."),
    { fig: "an02-luz-industria", code: "1" },
    p("Defensa. Draghi recordaba que la UE, en conjunto, es el segundo mayor gasto militar del mundo, pero que su industria está fragmentada: en Europa se usan doce tipos de carros de combate distintos; EE. UU. fabrica uno. Desde entonces, el gasto ha subido con rapidez. En 2025, la UE dedicó a defensa el 2,18 % de su PIB, su nivel más alto desde 2000 y por encima de China (1,73 %). En 2015 era el 1,3 %. EE. UU. sigue muy por delante, con el 3,12 %.",
      "Defence. Draghi noted that the EU as a whole is the world's second largest military spender, but that its industry is fragmented: twelve different types of battle tank are used in Europe; the US builds one. Since then, spending has risen fast. In 2025 the EU spent 2.18% of its GDP on defence, its highest level since 2000 and above China (1.73%). In 2015 it was 1.3%. The US remains far ahead, at 3.12%."),
    { fig: "an02-defensa", code: "2" },

    { h: t("La factura", "The bill"), id: "factura" },
    p("Para hacer todo eso, el informe calcula que la UE necesita invertir como mínimo entre 750.000 y 800.000 millones de euros más cada año, entre el 4,4 % y el 4,7 % de su PIB de 2023. La inversión tendría que pasar de en torno al 22 % del PIB al 27 %. Para comparar: el Plan Marshall supuso entre el 1 % y el 2 % del PIB al año entre 1948 y 1951. Draghi pedía además algo de financiación conjunta para bienes públicos europeos, como la innovación de vanguardia.",
      "To do all this, the report estimates that the EU needs to invest at least an extra 750 to 800 billion euros a year, 4.4% to 4.7% of its 2023 GDP. Investment would have to rise from around 22% of GDP to 27%. For comparison, the Marshall Plan amounted to 1% to 2% of GDP a year between 1948 and 1951. Draghi also called for some joint funding of European public goods, such as breakthrough innovation."),
    p("La inversión no ha despegado. En 2025, la UE invirtió el 21,3 % de su PIB, casi lo mismo que EE. UU. (21,4 % en 2024) y lejos del 27 %. Y la factura ha crecido: en septiembre de 2025, el propio Draghi citó un cálculo del BCE que eleva las necesidades a casi 1,2 billones de euros al año entre 2025 y 2031, sobre todo por el gasto en defensa.",
      "Investment has not taken off. In 2025, the EU invested 21.3% of its GDP, almost the same as the US (21.4% in 2024) and far from 27%. And the bill has grown: in September 2025, Draghi himself cited an ECB estimate that raises the needs to almost 1.2 trillion euros a year between 2025 and 2031, mainly because of defence spending."),
    { fig: "n03-inversion", code: "N03-2" },

    { h: t("Dos años después: qué se ha hecho", "Two years on: what has been done"), id: "que-se-ha-hecho" },
    { timeline: [
      { date: t("9 de septiembre de 2024", "9 September 2024"), text: t("Draghi presenta el informe en Bruselas.", "Draghi presents the report in Brussels.") },
      { date: t("Enero de 2025", "January 2025"), text: t("La Comisión presenta la Brújula para la Competitividad, su hoja de ruta basada en el informe.", "The Commission presents the Competitiveness Compass, its roadmap based on the report.") },
      { date: t("Mayo de 2025", "May 2025"), text: t("El Consejo aprueba SAFE: hasta 150.000 millones de euros en préstamos de la UE para compras conjuntas de defensa.", "The Council adopts SAFE: up to 150 billion euros in EU loans for joint defence procurement.") },
      { date: t("16 de septiembre de 2025", "16 September 2025"), text: t("Conferencia \"un año después\". La Comisión afirma que el 90 % de sus iniciativas principales se inspiran en el informe; Draghi advierte de que Europa está en una situación más difícil.", "\"One year after\" conference. The Commission says 90% of its flagship initiatives are inspired by the report; Draghi warns that Europe is in a harder place.") },
      { date: t("Marzo de 2026", "March 2026"), text: t("El Consejo Europeo lanza la agenda \"Una Europa, un mercado\".", "The European Council launches the \"One Europe, One Market\" agenda.") },
      { date: t("24 de abril de 2026", "24 April 2026"), text: t("Parlamento, Consejo y Comisión firman su hoja de ruta, con acuerdos sobre todas las iniciativas como tarde a finales de 2027.", "Parliament, Council and Commission sign its roadmap, with agreement on all initiatives by the end of 2027 at the latest.") },
      { date: t("Septiembre de 2026", "September 2026"), text: t("Los seguimientos independientes coinciden: avance real, pero lento y desigual.", "Independent trackers agree: real progress, but slow and uneven.") },
    ] },
    { quote: t("Un año después, Europa está en una situación más difícil.", "One year on, Europe is therefore in a harder place."),
      who: t("Mario Draghi, 16 de septiembre de 2025", "Mario Draghi, 16 September 2025"),
      url: "https://commission.europa.eu/document/download/0951a4ff-cd1a-4ea3-bc1d-f603decc1ed9_en?filename=Draghi_Speech_High_Level_Conference_One_Year_After.pdf" },
    p("Cuánto se ha aplicado depende de quién cuente y cómo. Estos son los dos seguimientos más recientes:",
      "How much has been implemented depends on who is counting and how. These are the two most recent trackers:"),
    { list: [
      t("Banco de España (datos de julio de 2026, con el seguimiento de EPIC): el 16 % de las medidas está aplicado del todo y el 26 %, en parte. Otro 42 % avanza con compromiso político, pero sin una norma o un instrumento en vigor. La energía apenas supera el 1 %, la cifra más baja de todos los pilares; en defensa, las medidas aplicadas total o parcialmente pasaron del 22 % al 53 % entre septiembre de 2025 y julio de 2026.",
        "Bank of Spain (July 2026 data, using EPIC's tracker): 16% of measures are fully implemented and 26% partly. Another 42% are moving forward with political commitment but without a rule or instrument in force. Energy barely exceeds 1%, the lowest of all pillars; in defence, fully or partly implemented measures rose from 22% to 53% between September 2025 and July 2026."),
      t("JEDI Draghi Tracker (10 de septiembre de 2026): se ha aplicado el 26 % de las recomendaciones y ninguna de las 30 clave se ha ejecutado por completo. Por áreas, energía y materias primas llegan al 35 %, y salud, al 13 %.",
        "JEDI Draghi Tracker (10 September 2026): 26% of the recommendations have been implemented and none of the 30 key ones has been fully executed. By area, energy and raw materials reach 35%, and health 13%."),
    ] },
    p("Las cifras no se pueden comparar entre sí: el Banco de España separa la energía de las materias primas, que es donde más se ha avanzado (casi el 40 %), y el JEDI las agrupa. Lo que sí coincide es el retrato: se ha movido lo que tenía urgencia compartida, como la defensa o las materias primas críticas, y mucho menos lo que más cambiaría las cosas, como la energía o la financiación de la inversión. Y no todo es cuestión de dinero: según el Banco de España, el 53 % de las propuestas no necesita inversión pública adicional.",
      "The figures cannot be compared with each other: the Bank of Spain separates energy from raw materials, where most progress has been made (almost 40%), while JEDI groups them. What does coincide is the picture: things with a shared sense of urgency, such as defence or critical raw materials, have moved, and much less so the things that would change most, such as energy or investment financing. And not everything is about money: according to the Bank of Spain, 53% of the proposals need no additional public investment."),

    { h: t("Qué dicen hoy los datos", "What the data say today"), id: "datos-hoy" },
    p("Dos años después, los datos confirman el diagnóstico más que la cura. La brecha de productividad con EE. UU. era en 2024 mayor que cuando se escribió el informe, la inversión sigue en torno al 21 % del PIB, lejos del 27 % que pedía el informe, y la electricidad para la industria cuesta la mitad más que antes de la crisis energética. El cambio más visible está en la defensa, donde el gasto ya ha superado el 2 % del PIB. Los líderes europeos se han dado hasta finales de 2027 para cerrar los acuerdos. Los próximos datos dirán si llegan a tiempo.",
      "Two years on, the data confirm the diagnosis more than the cure. The productivity gap with the US was wider in 2024 than when the report was written, investment remains around 21% of GDP, far from the 27% the report called for, and electricity for industry costs half as much again as before the energy crisis. The most visible change is in defence, where spending has now passed 2% of GDP. European leaders have given themselves until the end of 2027 to close the agreements. The next data will show whether they make it in time."),
  ],
  sources: [
    { name: "Comisión Europea: el informe Draghi sobre la competitividad de la UE", url: "https://commission.europa.eu/topics/competitiveness/draghi-report_en" },
    { name: "Informe Draghi, parte A: A competitiveness strategy for Europe (9/09/2024)", url: "https://commission.europa.eu/document/download/97e481fd-2dc3-412d-be4c-f152a8232961_en?filename=The%20future%20of%20European%20competitiveness%20_%20A%20competitiveness%20strategy%20for%20Europe.pdf" },
    { name: "Comisión Europea: un año después del informe Draghi (16/09/2025)", url: "https://commission.europa.eu/topics/competitiveness/draghi-report/one-year-after_en" },
    { name: "Discurso de Mario Draghi en la conferencia \"un año después\" (16/09/2025)", url: "https://commission.europa.eu/document/download/0951a4ff-cd1a-4ea3-bc1d-f603decc1ed9_en?filename=Draghi_Speech_High_Level_Conference_One_Year_After.pdf" },
    { name: "Comisión Europea: SAFE, Security Action for Europe", url: "https://defence-industry-space.ec.europa.eu/eu-defence-industry/safe-security-action-europe_en" },
    { name: "Comisión Europea: hoja de ruta \"Una Europa, un mercado\"", url: "https://commission.europa.eu/topics/competitiveness/one-europe-one-market-roadmap_es" },
    { name: "Banco de España: el informe Draghi, dos años después (8/09/2026)", url: "https://www.bde.es/wbe/en/noticias-eventos/blog/el-informe-draghi-dos-anos-despues-que-se-ha-cumplido.html" },
    { name: "Euronews (10/09/2026): EU falls short on Draghi reform agenda", url: "https://www.euronews.com/my-europe/2026/09/10/eu-falls-short-on-draghi-reform-agenda-new-report-shows" },
    { name: "JEDI Draghi Tracker", url: "https://draghitracker.org/" },
  ],
};

export default note;
