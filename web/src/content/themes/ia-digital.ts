import { p, type Theme } from "../../lib/content-types";

const theme: Theme = {
  id: "ia-digital",
  code: "IA",
  slug: { es: "ia-digital", en: "ai-digital" },
  title: { es: "IA y digital", en: "AI and digital" },
  status: "published",
  order: 1,
  published: "2026-09-24",
  opener: "models-units",
  dek: {
    es: "La UE adopta la inteligencia artificial más rápido que nunca, pero casi toda la tecnología que usa se diseña fuera.",
    en: "The EU is adopting artificial intelligence faster than ever, but almost all the technology it uses is designed elsewhere.",
  },
  lenses: {
    gigantes: {
      lede: { es: "La brecha no está en el uso de la IA. Está en su producción.", en: "The gap is not in using AI. It is in making it." },
      body: [
        p("Estados Unidos dedica a la investigación el 3,4 % de su PIB. China, el 2,7 %, y sigue subiendo. La UE lleva una década en torno al 2 %, con un 2,1 % en 2024. Casi toda la diferencia está en lo que invierten las empresas: el 2,7 % del PIB en Estados Unidos, el 2,1 % en China y el 1,4 % en la UE.",
          "The United States spends 3.4% of its GDP on research. China spends 2.7%, and rising. The EU has hovered around 2% for a decade, reaching 2.1% in 2024. Almost all of the difference lies in business investment: 2.7% of GDP in the US, 2.1% in China and 1.4% in the EU."),
        { fig: "g1-inversion-id", code: "G1" },
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
        p("En 2025, Eurostat preguntó a quienes no usan IA generativa por qué no lo hacen. El 64 % respondió que no la necesita. Solo el 7 % habló de privacidad o seguridad. En España los motivos cambian: pesa más no saber usarla (28 %) o no saber que existía (25 %). Más que una elección prudente, parece una brecha de conocimiento.",
          "In 2025, Eurostat asked people who do not use generative AI why not. 64% said they do not need it. Only 7% mentioned privacy or security. In Spain the reasons shift: not knowing how to use it (28%) or not knowing it existed (25%) weigh more. It looks less like a cautious choice and more like a knowledge gap."),
        { fig: "e1-motivos-no-ia-generativa", code: "E1" },
        p("Donde sí hay una elección de fondo es en cómo se gobierna internet. China adopta la tecnología con filtrado y censura del Estado. La UE, en conjunto, protege más la libertad en la red que Estados Unidos, que ha retrocedido desde 2023. Dentro de la Unión también hay diferencias: el gráfico muestra el país con más control en cada año.",
          "Where there is a deeper choice is in how the internet is governed. China adopts technology under state filtering and censorship. The EU as a whole protects online freedom more than the United States, which has slipped since 2023. There are differences within the Union too: the chart shows the most controlled member state each year."),
        { fig: "e2-control-internet", code: "E2" },
        p("Hay otra decisión que distingue a Europa: la mayoría de sus modelos destacados se publican con pesos abiertos, que cualquiera puede descargar y adaptar. Pero con tan pocos modelos, es más una señal que una estrategia.",
          "One more decision sets Europe apart: most of its notable models are released with open weights that anyone can download and adapt. But with so few models, it is more of a signal than a strategy."),
        { fig: "e3-modelos-abiertos", code: "E3" },
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
        p("La base de todo son las competencias digitales, y ahí la UE está lejos de su objetivo: el 60 % de la población tiene al menos competencias básicas, frente al 80 % que se ha propuesto para 2030.",
          "Digital skills are the foundation, and there the EU is far from its goal: 60% of people have at least basic skills, against the 80% it has set for 2030."),
        { fig: "d4-competencias-digitales", code: "D4" },
      ],
    },
  },
};

export default theme;
