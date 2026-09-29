import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n04-*.json (Eurostat nrg_pc_204, segundo semestre de 2025).
// Media de la UE, peso de los impuestos e impuestos negativos de Países Bajos y Luxemburgo, cotejados en Eurostat (ver sources).
const note: Note = {
  id: "n04",
  code: "N04",
  slug: { es: "precio-luz-hogares", en: "household-electricity-prices" },
  title: {
    es: "La luz de los hogares cuesta un 31,5 % más que a principios de 2021",
    en: "Household electricity costs 31.5% more than in early 2021",
  },
  dek: {
    es: "Un hogar medio de la UE paga 29 céntimos por kWh. En Irlanda, 40; en Hungría, 11. Los impuestos son el 28,9 % del precio; en Dinamarca, casi la mitad.",
    en: "An average EU household pays 29 cents per kWh. In Ireland, 40; in Hungary, 11. Taxes are 28.9% of the price; in Denmark, almost half.",
  },
  published: "2026-09-29",
  lens: "dentro",
  theme: "comercio",
  body: [
    p("En el segundo semestre de 2025, un hogar de la UE con un consumo medio pagó la electricidad a 28,96 céntimos por kWh, impuestos incluidos. Las diferencias entre países son grandes: en Irlanda, 40,42 céntimos, 3,7 veces lo que en Hungría (10,82). Alemania, Bélgica y Dinamarca completan los cuatro precios más altos. España, con 26,69 céntimos, está por debajo de la media.",
      "In the second half of 2025, an EU household with average consumption paid 28.96 cents per kWh for electricity, taxes included. The gaps between countries are wide: in Ireland, 40.42 cents, 3.7 times as much as in Hungary (10.82). Germany, Belgium and Denmark round out the four highest prices. Spain, at 26.69 cents, is below the average."),
    { fig: "n04-luz-precio", code: "1" },
    p("Parte de la diferencia la ponen los impuestos, que en la UE suponen el 28,9 % del precio. En Dinamarca son el 49,1 %: sin impuestos, su luz es más barata que la media europea; con ellos, es la cuarta más cara. En Países Bajos y Luxemburgo ocurre lo contrario: las ayudas y deducciones superan a los impuestos.",
      "Taxes account for part of the gap: in the EU they make up 28.9% of the price. In Denmark they are 49.1%: before taxes, its electricity is cheaper than the European average; after taxes, it is the fourth most expensive. The Netherlands and Luxembourg are the opposite case: allowances and support exceed taxes."),
    p("Desde el primer semestre de 2021, antes de la subida de la energía, la luz de los hogares se ha encarecido un 31,5 % en la UE, en euros corrientes. Ha subido en 26 de los 27 países; en Malta apenas ha cambiado. En Países Bajos casi se ha duplicado, y en Rumanía, Chequia, Polonia, Letonia y Estonia ha subido más de un 70 %. España está entre los que menos: un 14,9 %.",
      "Since the first half of 2021, before the energy price surge, household electricity has become 31.5% more expensive in the EU, in current euros. It has risen in 26 of the 27 countries; in Malta it has barely changed. In the Netherlands it has almost doubled, and in Romania, Czechia, Poland, Latvia and Estonia it has risen by more than 70%. Spain is among the smallest increases: 14.9%."),
    { fig: "n04-luz-cambio", code: "2" },
  ],
  sources: [
    { name: "Eurostat, Statistics Explained: Electricity price statistics", url: "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Electricity_price_statistics" },
  ],
};

export default note;
