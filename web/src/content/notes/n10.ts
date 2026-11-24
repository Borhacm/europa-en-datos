import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n10-*.json (Eurostat migr_pop3ctb, 2021 y 2025). Ver editorial/registro/n10.md.
// La parte nacida fuera de la UE por país y su subida desde 2021 ya está en el tema Demografía (DM-D2):
// esta nota la compara con la nacida en otro país de la Unión.
const note: Note = {
  id: "n10",
  code: "N10",
  slug: { es: "nacidos-en-otro-pais-de-la-ue", en: "born-in-another-eu-country" },
  title: {
    es: "Solo en Luxemburgo, Hungría y Eslovaquia viven más personas nacidas en otro país de la UE que fuera de ella",
    en: "Only in Luxembourg, Hungary and Slovakia do more residents come from another EU country than from outside the EU",
  },
  dek: {
    es: "El 4 % de los residentes en la UE nació en otro país de la Unión, y el 10,6 %, fuera de ella. Desde 2021, los primeros han aumentado en medio millón y los segundos, en 9,9 millones.",
    en: "4% of EU residents were born in another EU country, and 10.6% outside the EU. Since 2021, the first group has grown by half a million and the second by 9.9 million.",
  },
  published: "2026-11-24",
  updated: "2026-11-24",
  lens: "dentro",
  theme: "demografia",
  body: [
    p("Cualquier ciudadano de la UE puede vivir y trabajar en otro país de la Unión. A 1 de enero de 2025, 18 millones de residentes en la UE habían nacido en un país de la Unión distinto de aquel en el que viven: el 4 % de la población. Los nacidos fuera de la UE eran 47,7 millones, el 10,6 %.",
      "Any EU citizen can live and work in another EU country. On 1 January 2025, 18 million EU residents had been born in an EU country other than the one they live in: 4% of the population. Those born outside the EU numbered 47.7 million, or 10.6%."),
    p("En 24 de los 27 países pesan más los nacidos fuera de la Unión. Las excepciones son Luxemburgo, donde el 32,5 % de los habitantes nació en otro país de la UE y el 19 % fuera de ella; Eslovaquia (2,9 % y 1,1 %) y Hungría, donde las dos partes casi coinciden (3,7 % y 3,6 %). Después de Luxemburgo, los que tienen más residentes de otros países de la UE son Austria (9,7 %) y Chipre (9,1 %). En España, el 3,3 % nació en otro país de la UE y el 16 %, fuera de ella. Polonia y Lituania tienen la parte más pequeña: el 0,7 %.",
      "In 24 of the 27 countries, people born outside the EU outnumber those born elsewhere in the EU. The exceptions are Luxembourg, where 32.5% of residents were born in another EU country and 19% outside the EU; Slovakia (2.9% and 1.1%) and Hungary, where the two shares are almost the same (3.7% and 3.6%). After Luxembourg, the countries with the most residents from other EU countries are Austria (9.7%) and Cyprus (9.1%). In Spain, 3.3% were born in another EU country and 16% outside the EU. Poland and Lithuania have the smallest share: 0.7%."),
    { fig: "n10-nacidos-ue-fuera", code: "1" },
    p("La diferencia se ha ensanchado. Entre 2021 y 2025, los residentes nacidos en otro país de la UE pasaron de 17,6 a 18 millones. Los nacidos fuera, de 37,9 a 47,7 millones. El tema Demografía cuenta cómo ha crecido esa parte en cada país.",
      "The gap has widened. Between 2021 and 2025, residents born in another EU country went from 17.6 to 18 million. Those born outside the EU rose from 37.9 to 47.7 million. The Population theme shows how that share has grown in each country."),
    { fig: "n10-nacidos-ue-evolucion", code: "2" },
    p("Lo que no dicen estos datos. Cuentan dónde nació cada persona, no su nacionalidad ni cuánto tiempo lleva en el país, y no recogen a quien trabaja en otro país sin empadronarse en él, como los trabajadores transfronterizos. Tampoco dicen por qué se mudó cada uno.",
      "What these data do not say. They count where each person was born, not their nationality or how long they have lived in the country, and they leave out people who work in another country without registering as residents there, such as cross-border workers. Nor do they say why each person moved."),
    { see: { es: "Demografía y migración: envejecimiento, natalidad y migración", en: "Population and migration: ageing, birth rates and migration" }, href: { es: "/es/demografia/", en: "/en/population/" } },
  ],
  sources: [
    { name: "Eurostat: población a 1 de enero por país de nacimiento (migr_pop3ctb)", url: "https://ec.europa.eu/eurostat/databrowser/view/migr_pop3ctb/default/table" },
  ],
};

export default note;
