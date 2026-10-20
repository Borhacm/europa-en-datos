import { p, type Theme } from "../../lib/content-types";

// Rehecho el 20/10/2026 (ver editorial/registro/productividad.md): guion, dos gráficos explicativos (PR-E1 y PR-D2),
// ficha de la Directiva de tiempo de trabajo con dos estudios, párrafo de límites y enlaces a N03, N06 y AN02
// sin repetir sus cifras. Cifras comprobadas contra data/charts/p*.json y las fuentes de `sources`.
const theme: Theme = {
  id: "productividad",
  code: "PR",
  slug: { es: "productividad", en: "productivity" },
  title: { es: "Productividad y crecimiento", en: "Productivity and growth" },
  status: "published",
  order: 1,
  published: "2026-09-25",
  updated: "2026-10-20",
  dek: {
    es: "La UE pesa en la economía mundial casi lo mismo que EE. UU., pero tiene menos renta por habitante. Ya no es porque trabaje menos gente: es porque cada ocupado hace menos horas y, sobre todo, porque cada hora produce menos.",
    en: "The EU weighs almost as much as the United States in the world economy, but it has less income per person. It is no longer because fewer people work: it is because each worker puts in fewer hours and, above all, because each hour produces less.",
  },
  lenses: {
    gigantes: {
      lede: { es: "China ya es la mayor economía del mundo. La UE y EE. UU. pesan casi lo mismo, pero no producen igual.", en: "China is now the world's largest economy. The EU and the US weigh almost the same, but they do not produce the same." },
      body: [
        p("Medida en poder adquisitivo, la economía china supera a la estadounidense desde 2014 y ya aporta el 19,1 % del PIB mundial. La UE (14,4 %) y EE. UU. (14,7 %) están prácticamente empatadas, y las dos pesan mucho menos que en 1990, cuando cada una superaba el 20 %.",
          "Measured in purchasing power, China's economy has been larger than the US's since 2014 and now accounts for 19.1% of world GDP. The EU (14.4%) and the US (14.7%) are practically level, and both weigh far less than in 1990, when each was above 20%."),
        { fig: "pg1-peso-pib-mundial", code: "G1" },
        { see: { es: "Nota: cuánto ha crecido cada economía desde 2000, y qué pedía el informe Draghi", en: "Note: how much each economy has grown since 2000, and what the Draghi report asked for" }, href: { es: "/es/notas/informe-draghi/", en: "/en/notes/draghi-report/" } },
        p("Pesar lo mismo no es producir lo mismo por hora. En 2024, cada hora trabajada en la UE produjo 69,8 dólares; en EE. UU., 80,6, y en Japón, 52,1. China, con 19,7, sigue lejos, pero ha multiplicado por 4,3 lo que produce por hora desde 2005. La media europea esconde mucha distancia: siete países de la UE producen por hora más que EE. UU. (Austria, Bélgica, Dinamarca, Irlanda, Luxemburgo, Países Bajos y Suecia), y Bulgaria y Chipre, menos de la mitad.",
          "Weighing the same is not producing the same per hour. In 2024, each hour worked in the EU produced 69.8 dollars; in the US, 80.6, and in Japan, 52.1. China, at 19.7, is still far behind, but it has multiplied its output per hour by 4.3 since 2005. The European average hides a lot of distance: seven EU countries produce more per hour than the US (Austria, Belgium, Denmark, Ireland, Luxembourg, the Netherlands and Sweden), and Bulgaria and Cyprus, less than half."),
        { fig: "pg2-productividad-hora", code: "G2" },
        { see: { es: "Análisis: el informe Draghi, dos años después, y cómo ha evolucionado esta distancia", en: "Analysis: the Draghi report two years on, and how this gap has evolved" }, href: { es: "/es/notas/informe-draghi-dos-anos-despues/", en: "/en/notes/draghi-report-two-years-on/" } },
      ],
    },
    elige: {
      lede: { es: "La renta por habitante depende de tres cosas: lo que se produce por hora, las horas de cada ocupado y cuánta gente trabaja. En la última, la UE ya ha alcanzado a EE. UU.", en: "Income per person depends on three things: output per hour, the hours each worker puts in and how many people work. On the last, the EU has now caught up with the US." },
      body: [
        p("En 2000, la parte de la población con empleo en la UE era el 88,8 % de la de EE. UU. En 2025 era el 100,7 %: esa diferencia ha desaparecido. La de las horas, no. Cada ocupado europeo trabaja al año un 9,5 % menos que uno estadounidense, casi lo mismo que en 2000, cuando era un 9,1 % menos. En 2020, con la pandemia, la UE mantuvo más empleo y recortó más horas que EE. UU.; en 2024, las horas ya habían vuelto a su nivel anterior.",
          "In 2000, the share of the population in work in the EU was 88.8% of the US share. In 2025 it was 100.7%: that gap has disappeared. The hours gap has not. Each European worker puts in 9.5% fewer hours a year than an American one, almost the same as in 2000, when it was 9.1% fewer. In 2020, during the pandemic, the EU kept more jobs and cut more hours than the US; by 2024, hours were back at their earlier level."),
        { fig: "pe3-empleo-horas", code: "E1" },
        p("Con el empleo igualado, lo que separa hoy la renta por habitante de los dos bloques son las horas y, sobre todo, lo que se produce en cada una (G2). Y las horas no son iguales en toda Europa. Un ocupado de Países Bajos trabaja 31 horas a la semana; uno de Alemania, 33,5; uno de EE. UU., 37,5. En Grecia, Polonia o Lituania se trabaja más que en EE. UU. España, con 36,4, queda algo por debajo. Trabajar menos horas es, sobre todo, un rasgo de los países más ricos del oeste y el norte.",
          "With employment level, what now separates income per person in the two blocs is hours and, above all, what is produced in each of them (G2). And hours are not the same across Europe. A worker in the Netherlands puts in 31 hours a week; in Germany, 33.5; in the US, 37.5. In Greece, Poland or Lithuania people work more than in the US. Spain, at 36.4, is slightly below. Working fewer hours is above all a feature of the richest countries of the west and north."),
        { fig: "pe2-horas-trabajadas", code: "E2" },
        { h: { es: "La ficha: qué fija la ley sobre las horas", en: "The policy card: what the law sets on hours" }, id: "ficha-tiempo-trabajo" },
        p("La Directiva 2003/88/CE, de 4 de noviembre de 2003, obliga a los países de la UE a que la jornada media no supere las 48 horas por cada periodo de siete días, incluidas las horas extraordinarias, con una media que puede calcularse sobre periodos de hasta cuatro meses. También obliga a garantizar al menos cuatro semanas de vacaciones pagadas al año, que no pueden cambiarse por dinero salvo al terminar el contrato. Un país puede no aplicar el límite de 48 horas si el trabajador da su consentimiento. En EE. UU., la ley federal de normas laborales no obliga a pagar vacaciones ni festivos: depende de lo que acuerden empresa y trabajador.",
          "Directive 2003/88/EC of 4 November 2003 requires EU countries to ensure that average working time does not exceed 48 hours for each seven-day period, including overtime, with an average that can be calculated over periods of up to four months. It also requires at least four weeks of paid annual leave, which cannot be replaced by money except when the contract ends. A country may not apply the 48-hour limit if the worker consents. In the US, the federal Fair Labor Standards Act does not require payment for vacations or holidays: it is up to employer and employee."),
        p("El límite europeo queda muy por encima de las horas medias de E2, así que no explica por sí solo la diferencia. Los economistas no se ponen de acuerdo sobre la causa. Edward Prescott (2004) atribuye casi toda la diferencia de horas entre los países del G7 a los impuestos sobre las rentas del trabajo. Alberto Alesina, Edward Glaeser y Bruce Sacerdote (2005) concluyen que los impuestos explican poco y que pesan más las regulaciones del mercado laboral que impulsaron los sindicatos; recuerdan, además, que en los años sesenta los europeos trabajaban más que los estadounidenses.",
          "The European limit is well above the average hours in E2, so it does not explain the difference on its own. Economists disagree about the cause. Edward Prescott (2004) attributes almost all the difference in hours among G7 countries to taxes on labour income. Alberto Alesina, Edward Glaeser and Bruce Sacerdote (2005) conclude that taxes explain little and that labour market regulations pushed by unions matter more; they also note that in the 1960s Europeans worked more than Americans."),
      ],
    },
    dentro: {
      lede: { es: "Desde 2004, el este se ha acercado a la media europea. El sur se ha quedado atrás.", en: "Since 2004, the east has closed in on the European average. The south has fallen behind." },
      body: [
        p("En 2004, Rumanía tenía un PIB por habitante del 35 % de la media europea; en 2025, del 78 %. Polonia ha pasado del 52 % al 81 %, y Lituania, del 50 % al 87 %. En el sur ha ocurrido lo contrario: Grecia ha caído del 95 % al 68 %, Italia del 114 % al 96 % y España del 101 % al 92 %.",
          "In 2004, Romania's GDP per person was 35% of the European average; in 2025, 78%. Poland has gone from 52% to 81%, and Lithuania from 50% to 87%. The south has gone the other way: Greece has fallen from 95% to 68%, Italy from 114% to 96% and Spain from 101% to 92%."),
        { fig: "pd1-convergencia", code: "D1" },
        p("La convergencia del este ha ido de la mano de un fuerte aumento de la productividad. Entre 2004 y 2025, lo que se produce por hora trabajada creció un 19,6 % en el conjunto de la UE. En Rumanía, un 114,5 %; en Lituania, un 83,8 %, y en Polonia, un 78,2 %. En Italia apenas creció, un 1,5 %, y en Grecia cayó un 10,6 %. España, con un 17,7 %, creció casi como la media, así que su retroceso en D1 no se explica solo por la productividad por hora. Irlanda, con un 113,1 %, es un caso aparte: parte de su PIB son beneficios de multinacionales que salen del país.",
          "The east's convergence has gone hand in hand with a sharp rise in productivity. Between 2004 and 2025, output per hour worked grew 19.6% in the EU as a whole. In Romania, 114.5%; in Lithuania, 83.8%, and in Poland, 78.2%. In Italy it barely grew, 1.5%, and in Greece it fell 10.6%. Spain, at 17.7%, grew almost as much as the average, so its decline in D1 is not explained by output per hour alone. Ireland, at 113.1%, is a special case: part of its GDP is multinational profits that leave the country."),
        { fig: "pd3-productividad-paises", code: "D2" },
        p("Por regiones, las distancias son todavía mayores. La región de Dublín y el este de Irlanda (268 % de la media), Luxemburgo (245 %) y el sur de Irlanda (217 %) encabezan la lista, seguidos de Hamburgo (196 %). En España, la Comunidad de Madrid llega al 125 % y Melilla se queda en el 59 %.",
          "By region, the gaps are even wider. The Dublin and eastern Ireland region (268% of the average), Luxembourg (245%) and southern Ireland (217%) top the list, followed by Hamburg (196%). In Spain, the Madrid region reaches 125% and Melilla stays at 59%."),
        { fig: "pd2-mapa-renta", code: "D3" },
        p("Lo que no dicen estos datos. Comparar lo que produce una hora en distintos países exige convertir monedas con paridades de poder adquisitivo, y el resultado cambia según la fuente: con las estimaciones de la OIT de G2, a precios de 2021, la UE produce por hora un 13 % menos que EE. UU.; con las cuentas nacionales que reúne la OCDE, a precios de 2025, en torno a un 20 % menos. Las horas tampoco se miden igual: E1 usa las de las cuentas nacionales y E2, encuestas a los hogares. El PIB mide lo que se produce, no cómo se reparte ni lo que vale el tiempo libre. Y ninguno de estos gráficos dice qué causa las diferencias de productividad, como la inversión, la tecnología o el tamaño de las empresas, ni qué pasa con las cuentas públicas cuando se crece poco.",
          "What these data do not say. Comparing what an hour produces in different countries requires converting currencies with purchasing power parities, and the result changes with the source: with the ILO estimates in G2, at 2021 prices, the EU produces 13% less per hour than the US; with the national accounts compiled by the OECD, at 2025 prices, around 20% less. Hours are not measured the same way either: E1 uses national accounts and E2, household surveys. GDP measures what is produced, not how it is shared or what free time is worth. And none of these charts says what causes the differences in productivity, such as investment, technology or company size, or what happens to public finances when growth is low."),
        { see: { es: "Nota: la deuda pública de la UE, EE. UU. y China", en: "Note: public debt in the EU, the US and China" }, href: { es: "/es/notas/deuda-publica/", en: "/en/notes/public-debt/" } },
      ],
    },
  },
  sources: [
    { name: "EUR-Lex: Directiva 2003/88/CE, relativa a determinados aspectos de la ordenación del tiempo de trabajo", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32003L0088" },
    { name: "Departamento de Trabajo de EE. UU.: vacaciones (Fair Labor Standards Act)", url: "https://www.dol.gov/general/topic/workhours/vacation_leave" },
    { name: "Prescott, E. C. (2004): Why Do Americans Work So Much More Than Europeans? NBER, documento de trabajo 10316", url: "https://www.nber.org/papers/w10316" },
    { name: "Alesina, A., Glaeser, E. y Sacerdote, B. (2005): Work and Leisure in the U.S. and Europe: Why So Different? NBER, documento de trabajo 11278", url: "https://www.nber.org/papers/w11278" },
    { name: "OCDE, Productivity Database: PIB por hora trabajada en paridades de poder adquisitivo corrientes", url: "https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_PDB%40DF_PDB&df[ag]=OECD.SDD.TPS" },
    { name: "Oficina Central de Estadística de Irlanda: la renta nacional modificada (GNI*)", url: "https://www.cso.ie/en/interactivezone/statisticsexplained/nationalaccountsexplained/modifiedgni/" },
  ],
};

export default theme;
