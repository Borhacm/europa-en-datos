import { p, type Theme } from "../../lib/content-types";

const theme: Theme = {
  id: "productividad",
  code: "PR",
  slug: { es: "productividad", en: "productivity" },
  title: { es: "Productividad y crecimiento", en: "Productivity and growth" },
  status: "published",
  order: 1,
  published: "2026-09-25",
  dek: {
    es: "La UE pesa tanto en la economía mundial como Estados Unidos, pero produce menos por hora y mucho menos por habitante. La pregunta es cuánto de esa distancia es atraso y cuánto es elección.",
    en: "The EU weighs as much in the world economy as the United States, but it produces less per hour and much less per person. The question is how much of that gap is lagging behind and how much is choice.",
  },
  lenses: {
    gigantes: {
      lede: { es: "China ya es la mayor economía del mundo. La UE y EE. UU. pesan casi lo mismo, pero no producen igual.", en: "China is now the world's largest economy. The EU and the US weigh almost the same, but they do not produce the same." },
      body: [
        p("Medida en poder adquisitivo, la economía china supera a la estadounidense desde 2014 y ya aporta el 19,1 % del PIB mundial. La UE (14,4 %) y EE. UU. (14,7 %) están prácticamente empatadas, y las dos pesan mucho menos que en 1990, cuando cada una superaba el 20 %.",
          "Measured in purchasing power, China's economy has been larger than the US's since 2014 and now accounts for 19.1% of world GDP. The EU (14.4%) and the US (14.7%) are practically level, and both weigh far less than in 1990, when each was above 20%."),
        { fig: "pg1-peso-pib-mundial", code: "G1" },
        p("La diferencia está en la productividad. En 2024, cada hora trabajada en la UE produjo 69,8 dólares, frente a 80,6 en EE. UU.: un 13 % menos. En 2019 la distancia era del 7 %. China, con 19,7 dólares por hora, sigue lejos de ambos.",
          "The difference lies in productivity. In 2024, each hour worked in the EU produced 69.8 dollars, against 80.6 in the US: 13% less. In 2019 the gap was 7%. China, at 19.7 dollars per hour, is still far behind both."),
        { fig: "pg2-productividad-hora", code: "G2" },
      ],
    },
    elige: {
      lede: { es: "Europa produce menos por habitante que por hora. Parte de la diferencia es que trabaja menos horas.", en: "Europe produces less per person than per hour. Part of the difference is that it works fewer hours." },
      body: [
        p("Por hora trabajada, la UE está al 87 % del nivel de EE. UU. Por habitante, solo al 74 %. La distancia entre esas dos cifras se explica por las horas que trabaja cada persona y por la parte de la población que tiene empleo.",
          "Per hour worked, the EU is at 87% of the US level. Per person, only at 74%. The distance between those two figures comes from the hours each person works and from the share of the population in work."),
        { fig: "pe1-brecha-ee-uu", code: "E1" },
        p("Las horas no son iguales en toda Europa. Un trabajador de Países Bajos hace 31 horas a la semana; uno de Alemania, 33,5; uno de EE. UU., 37,5. En cambio, en Grecia, Polonia o Lituania se trabaja más que en EE. UU. España, con 36,4, queda algo por debajo. Trabajar menos horas es, sobre todo, un rasgo de los países más ricos del oeste y el norte.",
          "Hours are not the same across Europe. A worker in the Netherlands puts in 31 hours a week; in Germany, 33.5; in the US, 37.5. By contrast, people in Greece, Poland or Lithuania work more than in the US. Spain, at 36.4, is slightly below. Working fewer hours is above all a feature of the richest countries of the west and north."),
        { fig: "pe2-horas-trabajadas", code: "E2" },
      ],
    },
    dentro: {
      lede: { es: "Desde 2004, el este se ha acercado a la media europea. El sur se ha quedado atrás.", en: "Since 2004, the east has closed in on the European average. The south has fallen behind." },
      body: [
        p("En 2004, Rumanía tenía un PIB por habitante del 35 % de la media europea; en 2025, del 78 %. Polonia ha pasado del 52 % al 81 %, y Lituania, del 50 % al 87 %. En el sur ha ocurrido lo contrario: Grecia ha caído del 95 % al 68 %, Italia del 114 % al 96 % y España del 101 % al 92 %.",
          "In 2004, Romania's GDP per person was 35% of the European average; in 2025, 78%. Poland has gone from 52% to 81%, and Lithuania from 50% to 87%. The south has gone the other way: Greece has fallen from 95% to 68%, Italy from 114% to 96% and Spain from 101% to 92%."),
        { fig: "pd1-convergencia", code: "D1" },
        p("Por regiones, las distancias son todavía mayores. La región de Dublín (268 % de la media), Luxemburgo (245 %) y Hamburgo (196 %) encabezan la lista. En España, la Comunidad de Madrid llega al 125 % y Melilla se queda en el 59 %.",
          "By region, the gaps are even wider. The Dublin region (268% of the average), Luxembourg (245%) and Hamburg (196%) top the list. In Spain, the Madrid region reaches 125% and Melilla stays at 59%."),
        { fig: "pd2-mapa-renta", code: "D2" },
      ],
    },
  },
};

export default theme;
