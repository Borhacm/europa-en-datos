import { p, type Theme } from "../../lib/content-types";

// Rehecho el 20/10/2026 (ver editorial/registro/ia-digital.md): títulos sin valoraciones ni preguntas, notas de IA-G1,
// ficha de la Década Digital (Decisión 2022/2481), párrafo de límites y enlaces a AN01, N02 y AN02 sin repetir sus cifras.
// Cifras comprobadas contra data/charts/{g,e,d}*.json y EUR-Lex.
const theme: Theme = {
  id: "ia-digital",
  code: "IA",
  slug: { es: "ia-digital", en: "ai-digital" },
  title: { es: "IA y digital", en: "AI and digital" },
  status: "published",
  order: 1,
  published: "2026-09-24",
  updated: "2026-10-20",
  opener: "models-units",
  dek: {
    es: "La UE adopta la inteligencia artificial más rápido que nunca, pero casi toda la tecnología que usa se diseña fuera.",
    en: "The EU is adopting artificial intelligence faster than ever, but almost all the technology it uses is designed elsewhere.",
  },
  lenses: {
    gigantes: {
      lede: { es: "La brecha no está en el uso de la IA. Está en su producción.", en: "The gap is not in using AI. It is in making it." },
      body: [
        p("En diez años, la UE apenas ha movido lo que dedica a investigación: del 2,0 % de su PIB en 2014 al 2,1 % en 2024. En el mismo tiempo, EE. UU. ha pasado del 2,7 % al 3,4 %, y China, del 2,0 % al 2,7 %; China supera a la UE desde 2015. Corea del Sur dedica el 5,1 %; Alemania, el 3,1 %, y España, el 1,5 %. La diferencia está en las empresas: las estadounidenses invierten en I+D el 2,7 % del PIB, y las europeas, el 1,4 %.",
          "In ten years, the EU has barely changed what it spends on research: from 2.0% of GDP in 2014 to 2.1% in 2024. Over the same period, the US has gone from 2.7% to 3.4%, and China from 2.0% to 2.7%; China has been above the EU since 2015. South Korea spends 5.1%; Germany, 3.1%, and Spain, 1.5%. The difference lies in business: US companies invest 2.7% of GDP in R&D, and European ones 1.4%."),
        { fig: "g1-inversion-id", code: "G1" },
        { see: { es: "Análisis: el informe Draghi, dos años después, y lo que pedía para la innovación", en: "Analysis: the Draghi report two years on, and what it asked for innovation" }, href: { es: "/es/notas/informe-draghi-dos-anos-despues/", en: "/en/notes/draghi-report-two-years-on/" } },
        p("Esa inversión se nota en lo que se inventa. En solicitudes internacionales de patentes de IA, Estados Unidos y China presentan cada uno casi el triple que la UE. Por habitante, Estados Unidos patenta cuatro veces más IA que la UE, mientras que China y la UE están a la par.",
          "That investment shows up in what gets invented. In international AI patent applications, the US and China each file almost three times as many as the EU. Per person, the US patents four times more AI than the EU, while China and the EU are level."),
        { fig: "g2-patentes-ia", code: "G2" },
        p("En los modelos de IA que marcan el ritmo del sector, la distancia es todavía mayor. Desde 2023, las organizaciones de la UE han participado en 18 modelos destacados. Las de Estados Unidos, en 250. Las de China, en 120.",
          "In the AI models that set the pace of the field, the distance is even wider. Since 2023, EU organisations have taken part in 18 notable models. US organisations, in 250. Chinese ones, in 120."),
        { fig: "g3-modelos-ia", code: "G3" },
      ],
    },
    elige: {
      lede: { es: "Se suele decir que Europa va más despacio porque prefiere proteger. Los datos lo matizan.", en: "The usual story says Europe moves slower because it prefers to protect. The data adds nuance." },
      body: [
        p("En 2025, Eurostat preguntó a quienes no usan IA generativa por qué no lo hacen. El 64 % respondió que no la necesita. Solo el 7 % habló de privacidad o seguridad. En España los motivos cambian: pesa más no saber usarla (28 %) o no saber que existía (25 %). En los dos casos, la falta de conocimiento pesa más que la prudencia.",
          "In 2025, Eurostat asked people who do not use generative AI why not. 64% said they do not need it. Only 7% mentioned privacy or security. In Spain the reasons shift: not knowing how to use it (28%) or not knowing it existed (25%) weigh more. In both cases, lack of knowledge weighs more than caution."),
        { fig: "e1-motivos-no-ia-generativa", code: "E1" },
        { see: { es: "Nota: qué frena a las empresas que se plantearon usar IA y no lo hicieron", en: "Note: what holds back companies that considered using AI and did not" }, href: { es: "/es/notas/ai-act/", en: "/en/notes/ai-act/" } },
        p("Donde sí hay una elección de fondo es en cómo se gobierna internet. Según los expertos de V-Dem, el Gobierno chino filtra internet y censura las redes sociales mucho más que cualquier país de la UE. En EE. UU., el filtrado del Gobierno aumentó en 2023 y sigue en ese nivel; la mediana de la UE filtra menos. Dentro de la Unión también hay diferencias: el gráfico muestra el país con más control en cada año.",
          "Where there is a deeper choice is in how the internet is governed. According to V-Dem's experts, the Chinese government filters the internet and censors social media far more than any EU country. In the US, government filtering increased in 2023 and has stayed at that level; the EU median filters less. There are differences within the Union too: the chart shows the most controlled member state each year."),
        { fig: "e2-control-internet", code: "E2" },
        { see: { es: "Libertades, bienestar y clima: la calidad democrática de la UE, EE. UU. y China", en: "Freedoms, well-being and climate: the quality of democracy in the EU, the US and China" }, href: { es: "/es/libertades/", en: "/en/freedoms/" } },
        p("Hay otra decisión que distingue a Europa: de sus 18 modelos destacados desde 2023, 13 se publicaron con pesos abiertos, que cualquiera puede descargar y adaptar. En China, el 64 %; en EE. UU., el 29 %, donde más de la mitad solo se ofrece a través de una API o de la web. Con tan pocos modelos, un solo laboratorio cambia mucho el porcentaje europeo.",
          "One more decision sets Europe apart: of its 18 notable models since 2023, 13 were released with open weights that anyone can download and adapt. In China, 64%; in the US, 29%, where more than half are offered only through an API or the web. With so few models, a single lab changes the European share a lot."),
        { fig: "e3-modelos-abiertos", code: "E3" },
        { see: { es: "Análisis: el AI Act, qué exige y cómo cumplirlo", en: "Analysis: the AI Act, what it requires and how to comply" }, href: { es: "/es/notas/ai-act-como-cumplirlo/", en: "/en/notes/ai-act-how-to-comply/" } },
      ],
    },
    dentro: {
      lede: { es: "Hablar de Europa en conjunto esconde distancias enormes entre sus países.", en: "Talking about Europe as a whole hides huge distances between its countries." },
      body: [
        p("En Dinamarca, el 42 % de las empresas ya usa alguna tecnología de IA. En Rumanía, el 5 %. La media de la UE se ha multiplicado por 2,6 desde 2021, hasta el 20 %, y España está justo en la media.",
          "In Denmark, 42% of enterprises already use some AI technology. In Romania, 5%. The EU average has grown 2.6 times since 2021, to 20%, and Spain sits right on the average."),
        { fig: "d1-empresas-ia", code: "D1" },
        p("Dentro de cada país, la IA se concentra en torno a la capital. Pasa en casi todos los países que publican datos por regiones. En España, la Comunidad de Madrid (27 %) multiplica por ocho a Melilla (3,5 %).",
          "Within each country, AI clusters around the capital. It happens in almost every country that publishes regional data. In Spain, the Madrid region (27%) is eight times Melilla (3.5%)."),
        { fig: "d2-mapa-regional-ia", code: "D2" },
        p("Entre las personas, el patrón se repite. Uno de cada tres europeos usó IA generativa en 2025. Entre los jóvenes de 16 a 24 años, casi dos de cada tres. España está por encima de la media, con un 38 %.",
          "Among people, the pattern repeats. One in three Europeans used generative AI in 2025. Among 16 to 24 year olds, almost two in three. Spain is above average, at 38%."),
        { fig: "d3-ia-generativa", code: "D3" },
        p("La base de todo son las competencias digitales, y ahí la UE está lejos de su objetivo: en 2025, el 60,4 % de las personas de 16 a 74 años tenía al menos competencias básicas, frente al 80 % que se ha propuesto para 2030. Entre 2021 y 2025 subió 6,5 puntos; para llegar a la meta, tendría que subir casi 20 en cinco años. España, con el 66,5 %, está por encima de la media.",
          "Digital skills are the foundation, and there the EU is far from its goal: in 2025, 60.4% of people aged 16 to 74 had at least basic skills, against the 80% it has set for 2030. Between 2021 and 2025 the share rose 6.5 points; to reach the target, it would have to rise almost 20 in five years. Spain, at 66.5%, is above the average."),
        { fig: "d4-competencias-digitales", code: "D4" },
        { h: { es: "La ficha: las metas de la Década Digital", en: "The policy card: the Digital Decade targets" }, id: "ficha-decada-digital" },
        p("El objetivo del 80 % sale de la Decisión (UE) 2022/2481, de 14 de diciembre de 2022, que fija el programa de la Década Digital. Sus metas para 2030 incluyen también 20 millones de especialistas en TIC empleados en la UE, que el 75 % de las empresas use computación en la nube, macrodatos o inteligencia artificial, y duplicar el número de unicornios. No son obligaciones para cada país: la Comisión y los Estados «cooperarán» para alcanzarlas, y la Comisión presenta cada año un informe sobre el estado de la Década Digital y, si los avances no bastan, propone medidas. La meta de las empresas se cumple con cualquiera de las tres tecnologías, así que el 20 % de empresas que usan IA de D1 no se puede comparar directamente con el 75 %.",
          "The 80% target comes from Decision (EU) 2022/2481 of 14 December 2022, which sets the Digital Decade programme. Its 2030 targets also include 20 million ICT specialists employed in the EU, 75% of companies using cloud computing, big data or artificial intelligence, and doubling the number of unicorns. They are not obligations for each country: the Commission and member states \"shall cooperate\" to reach them, and the Commission presents a yearly report on the state of the Digital Decade and proposes measures if progress falls short. The business target is met with any of the three technologies, so the 20% of companies using AI in D1 cannot be compared directly with the 75%."),
        p("Lo que no dicen estos datos. Las patentes miden inventos, no si llegan al mercado, y los últimos años están incompletos por el retraso en su publicación. La lista de modelos destacados de Epoch AI se basa en criterios propios y en lo que se hace público: puede dejar fuera modelos de empresas que publican poco. El índice de control de internet de V-Dem resume la opinión de expertos, no mediciones técnicas. El uso de IA de empresas y personas es lo que declaran en las encuestas de Eurostat, que no dicen para qué la usan ni con qué intensidad. Y ninguno de estos gráficos mide cuánto valor económico genera la IA.",
          "What these data do not say. Patents measure inventions, not whether they reach the market, and the latest years are incomplete because of publication lags. Epoch AI's list of notable models relies on its own criteria and on what is made public: it may leave out models from companies that publish little. V-Dem's internet control index summarises expert opinion, not technical measurements. AI use by companies and people is what they report in Eurostat surveys, which do not say what they use it for or how intensively. And none of these charts measures how much economic value AI creates."),
      ],
    },
  },
  sources: [
    { name: "EUR-Lex: Decisión (UE) 2022/2481, por la que se establece el programa estratégico de la Década Digital para 2030", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32022D2481" },
  ],
};

export default theme;
