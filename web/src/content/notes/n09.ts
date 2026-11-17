import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n09-*.json (Eurostat demo_pjanind, 2005 y 2025). Ver editorial/registro/n09.md.
// La comparación de la UE con EE. UU. y China ya está en el tema Demografía (DM-G1): esta nota cuenta el envejecimiento país por país.
const note: Note = {
  id: "n09",
  code: "N09",
  slug: { es: "envejecimiento-pais-por-pais", en: "ageing-country-by-country" },
  title: {
    es: "Polonia, uno de los países más jóvenes de la UE en 2005, es el que más ha envejecido desde entonces",
    en: "Poland, one of the youngest EU countries in 2005, has aged the most since then",
  },
  dek: {
    es: "En 2005, ningún país de la UE tenía a uno de cada cinco habitantes con 65 años o más. En 2025, 22 de los 27 lo superan. Los que más han envejecido son Polonia, Finlandia y Eslovaquia, que en 2005 estaban por debajo de la media.",
    en: "In 2005, no EU country had one in five residents aged 65 or older. In 2025, 22 of the 27 are above that mark. Those that have aged most are Poland, Finland and Slovakia, which in 2005 were below the average.",
  },
  published: "2026-11-17",
  updated: "2026-11-17",
  lens: "dentro",
  theme: "demografia",
  body: [
    p("A 1 de enero de 2025, el 21,9 % de los habitantes de la UE tenía 65 años o más, frente al 16,7 % en 2005. La proporción ha subido en los 27 países, pero no al mismo ritmo. En 2005, ningún país llegaba al 20 %; ahora lo superan 22.",
      "On 1 January 2025, 21.9% of EU residents were 65 or older, up from 16.7% in 2005. The share has risen in all 27 countries, but not at the same pace. In 2005, no country reached 20%; now 22 are above it."),
    p("Polonia es el caso más claro. En 2005 era el cuarto país más joven, con el 13,1 % de mayores; ahora tiene el 21 %, 7,9 puntos más, y ya supera a España, Suecia y los Países Bajos. Le siguen Finlandia (7,7 puntos, hasta el 23,6 %) y Eslovaquia (7,1 puntos). En 16 países, los mayores han ganado más peso que en el conjunto de la UE (5,2 puntos). En Alemania y en España han ganado 4,1 puntos, y en Luxemburgo, solo 1,1: con el 15,2 %, es el país más joven, seguido de Irlanda (15,7 %). Italia es el más envejecido, con el 24,7 %.",
      "Poland is the clearest case. In 2005 it was the fourth-youngest country, with 13.1% of its population aged 65 or older; now it has 21%, 7.9 points more, and it is ahead of Spain, Sweden and the Netherlands. It is followed by Finland (7.7 points, to 23.6%) and Slovakia (7.1 points). In 16 countries, older people have gained more weight than in the EU as a whole (5.2 points). In Germany and Spain they have gained 4.1 points, and in Luxembourg only 1.1: at 15.2%, it is the youngest country, followed by Ireland (15.7%). Italy is the oldest, at 24.7%."),
    { fig: "n09-mayores-cambio", code: "1" },
    p("En la UE, el 6,2 % de la población tiene 80 años o más, lo mismo que en España. Italia vuelve a estar arriba, con el 7,8 %, seguida de Alemania (7,2 %) y Grecia (7,1 %). Eslovaquia (3,7 %) e Irlanda (3,8 %) no llegan a la mitad que Italia.",
      "In the EU, 6.2% of the population is 80 or older, the same as in Spain. Italy is again at the top, at 7.8%, followed by Germany (7.2%) and Greece (7.1%). Slovakia (3.7%) and Ireland (3.8%) have less than half Italy's share."),
    { fig: "n09-mayores-80", code: "2" },
    p("Lo que no dicen estos datos. El porcentaje de mayores sube si se vive más, si nacen menos niños o si se van los jóvenes, y estos gráficos no separan las tres causas. Tampoco dicen cuántos mayores necesitan ayuda. La comparación de la UE con EE. UU. y China, y la caída de la natalidad, están en el tema de demografía.",
      "What these data do not say. The share of older people rises if people live longer, if fewer children are born or if young people leave, and these charts do not separate the three causes. Nor do they say how many older people need help. The comparison of the EU with the US and China, and the fall in birth rates, are in the population topic."),
    { see: { es: "Demografía y migración: envejecimiento, natalidad y migración", en: "Population and migration: ageing, birth rates and migration" }, href: { es: "/es/demografia/", en: "/en/population/" } },
  ],
  sources: [
    { name: "Eurostat: indicadores de estructura de la población (demo_pjanind)", url: "https://ec.europa.eu/eurostat/databrowser/view/demo_pjanind/default/table" },
  ],
};

export default note;
