import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n01-vivienda-precios.json (Eurostat, datos de 2025).
const note: Note = {
  id: "n01",
  code: "N01",
  slug: { es: "vivienda-desde-2015", en: "housing-since-2015" },
  title: {
    es: "La vivienda ha subido casi el doble que la inflación desde 2015",
    en: "Housing has risen almost twice as much as inflation since 2015",
  },
  dek: {
    es: "En la UE, comprar una casa cuesta un 62 % más que en 2015. En Hungría se ha multiplicado por 3,7; en Finlandia está algo más barata.",
    en: "In the EU, buying a home costs 62% more than in 2015. In Hungary prices have multiplied by 3.7; in Finland they are slightly lower.",
  },
  published: "2026-09-24",
  lens: "dentro",
  theme: "libertades",
  body: [
    p("Entre 2015 y 2025, el precio de la vivienda en la UE subió un 62 %. En el mismo periodo, la inflación acumulada fue del 33 %: las casas se han encarecido casi el doble que el resto de los precios.",
      "Between 2015 and 2025, house prices in the EU rose by 62%. Over the same period, cumulative inflation was 33%: homes have become almost twice as expensive as everything else."),
    { fig: "n01-vivienda-precios", code: "1" },
    p("Las diferencias entre países son enormes. En Hungría los precios se han multiplicado por 3,7, y en Portugal, Lituania o Bulgaria han subido más del 140 %. España está por encima de la media, con un 81 %. En el otro extremo, en Italia (16 %) y Francia (27 %) la vivienda ha subido menos que la inflación media europea, y en Finlandia cuesta un 1 % menos que en 2015.",
      "The differences between countries are huge. In Hungary prices have multiplied by 3.7, and in Portugal, Lithuania or Bulgaria they have risen by more than 140%. Spain is above average, at 81%. At the other end, in Italy (16%) and France (27%) housing has risen less than average European inflation, and in Finland it costs 1% less than in 2015."),
  ],
};

export default note;
