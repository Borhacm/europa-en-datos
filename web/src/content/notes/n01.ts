import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n01-vivienda-precios.json y n01-alquiler-compra.json (Eurostat, datos de 2025).
// Revisada el 20/10/2026 (P3, ver editorial/registro/notas-p3.md): pasa al tema de vivienda, gráfico de alquiler frente a compra y límites.
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
  updated: "2026-10-20",
  lens: "dentro",
  theme: "vivienda",
  body: [
    p("Entre 2015 y 2025, el precio de la vivienda en la UE subió un 62 %. En el mismo periodo, la inflación acumulada fue del 33 %: las casas se han encarecido casi el doble que el resto de los precios.",
      "Between 2015 and 2025, house prices in the EU rose by 62%. Over the same period, cumulative inflation was 33%: homes have become almost twice as expensive as everything else."),
    { fig: "n01-vivienda-precios", code: "1" },
    p("Las diferencias entre países son enormes. En Hungría los precios se han multiplicado por 3,7, y en Portugal, Lituania o Bulgaria han subido más del 140 %. España está por encima de la media, con un 81 %. En el otro extremo, en Italia (16 %) y Francia (27 %) la vivienda ha subido menos que la inflación media europea, y en Finlandia cuesta un 1 % menos que en 2015.",
      "The differences between countries are huge. In Hungary prices have multiplied by 3.7, and in Portugal, Lithuania or Bulgaria they have risen by more than 140%. Spain is above average, at 81%. At the other end, in Italy (16%) and France (27%) housing has risen less than average European inflation, and in Finland it costs 1% less than in 2015."),
    p("Alquilar se ha encarecido mucho menos. En el mismo periodo, los alquileres de la UE subieron un 20,5 %: comprar ha subido tres veces más. Pasa en 25 de los 26 países con datos; solo en Finlandia el alquiler ha subido más que la compra. La mayor distancia está en Hungría, donde la compra sube un 266,6 % y el alquiler un 105,4 %, y en Portugal (163,9 % frente a 36,4 %). En España, la compra ha subido un 80,6 % y el alquiler, un 13,6 %.",
      "Renting has become far less expensive. Over the same period, EU rents rose 20.5%: buying has risen three times as much. This is the case in 25 of the 26 countries with data; only in Finland have rents risen more than purchase prices. The widest gaps are in Hungary, where purchase prices rose 266.6% and rents 105.4%, and in Portugal (163.9% against 36.4%). In Spain, purchase prices rose 80.6% and rents 13.6%."),
    { fig: "n01-alquiler-compra", code: "2" },
    p("Lo que no dicen estos datos. Son precios nominales y no se comparan con los salarios, así que no dicen si la vivienda es más o menos asequible. El índice de alquileres sigue lo que pagan los hogares inquilinos, no el precio de los pisos que se anuncian. Quién compra, quién alquila y cuánto pesa la vivienda en cada hogar se cuenta en el tema de vivienda.",
      "What these data do not say. These are nominal prices and are not compared with wages, so they do not say whether housing is more or less affordable. The rent index tracks what tenant households pay, not the price of advertised flats. Who buys, who rents and how much housing weighs on each household is covered in the housing theme."),
  ],
};

export default note;
