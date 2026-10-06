import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n05-*.json (Eurostat road_eqr_carpda, matriculaciones de 2013 a 2025).
// Objetivo de 2035, propuesta de 2025 y fin de la ayuda alemana, cotejados en las fuentes oficiales (ver sources).
const note: Note = {
  id: "n05",
  code: "N05",
  slug: { es: "coche-electrico", en: "electric-cars" },
  title: {
    es: "Uno de cada seis coches nuevos de la UE ya es eléctrico, pero el ritmo va por países",
    en: "One in six new cars in the EU is now electric, but the pace depends on the country",
  },
  dek: {
    es: "En 2025, el 17,3 % de los turismos nuevos de la UE fueron eléctricos de batería, frente al 1,9 % de 2019. En Dinamarca, el 67,8 %; en España, el 8,7 %; en Croacia, el 1,9 %.",
    en: "In 2025, 17.3% of new cars in the EU were battery electric, up from 1.9% in 2019. In Denmark, 67.8%; in Spain, 8.7%; in Croatia, 1.9%.",
  },
  published: "2026-10-06",
  lens: "elige",
  theme: "libertades",
  body: [
    p("La UE ya ha elegido hacia dónde va el coche. La norma aprobada en 2023 fija para 2035 una reducción del 100 % de las emisiones de CO2 de los turismos nuevos, lo que en la práctica deja fuera a los de combustión. En diciembre de 2025, la Comisión propuso rebajar ese objetivo al 90 % y compensar el resto; la propuesta está en manos del Parlamento y del Consejo.",
      "The EU has already chosen where cars are heading. The rules adopted in 2023 set a 100% cut in CO2 emissions from new cars by 2035, which in practice rules out combustion engines. In December 2025 the Commission proposed lowering that target to 90% and offsetting the rest; the proposal is now with Parliament and the Council."),
    p("Los compradores van más despacio que la norma, y a velocidades muy distintas. En 2025, el 17,3 % de los turismos nuevos de la UE fueron eléctricos de batería. En Dinamarca, más de dos de cada tres; en Países Bajos, Malta, Finlandia, Suecia y Bélgica, más de un tercio. En 13 de los 27 países no llegan al 10 %: España se queda en el 8,7 %, Italia en el 6,1 % y Croacia en el 1,9 %. Fuera de la UE, en Noruega son el 95,1 %.",
      "Buyers are moving more slowly than the rules, and at very different speeds. In 2025, 17.3% of new cars in the EU were battery electric. In Denmark, more than two in three; in the Netherlands, Malta, Finland, Sweden and Belgium, more than a third. In 13 of the 27 countries they are below 10%: Spain stands at 8.7%, Italy at 6.1% and Croatia at 1.9%. Outside the EU, in Norway, the figure is 95.1%."),
    { fig: "n05-electricos-cuota", code: "1" },
    p("Si se suman los híbridos enchufables, la cuota de la UE sube al 26,7 %, y la de España al 19,2 %, más del doble que con los eléctricos puros.",
      "Adding plug-in hybrids lifts the EU share to 26.7%, and Spain's to 19.2%, more than double the battery electric figure."),
    p("El salto ha sido rápido: en 2019 eran el 1,9 % en la UE. Pero no ha sido lineal. En 2024 la cuota bajó por primera vez, del 14,5 % al 13,5 %, arrastrada sobre todo por Alemania, el mayor mercado, que cerró su ayuda a la compra en diciembre de 2023 y pasó del 18,4 % al 13,5 %. En 2025 se recuperó: subió en 22 de los 27 países, y Alemania llegó al 19,1 %.",
      "The jump has been fast: in 2019 they were 1.9% in the EU. But it has not been a straight line. In 2024 the share fell for the first time, from 14.5% to 13.5%, dragged down mainly by Germany, the largest market, which closed its purchase subsidy in December 2023 and went from 18.4% to 13.5%. In 2025 it recovered: it rose in 22 of the 27 countries, and Germany reached 19.1%."),
    { fig: "n05-electricos-evolucion", code: "2" },
  ],
  sources: [
    { name: "Comisión Europea: normas de CO2 para turismos y furgonetas (Reglamento (UE) 2023/851 y propuesta de diciembre de 2025)", url: "https://climate.ec.europa.eu/areas-action/transport-decarbonisation/road-transport/cars-and-vans_en" },
    { name: "EUR-Lex: Reglamento (UE) 2023/851", url: "https://eur-lex.europa.eu/eli/reg/2023/851/oj" },
    { name: "Gobierno alemán: fin del Umweltbonus (solicitudes hasta el 17 de diciembre de 2023)", url: "https://verwaltung.bund.de/leistungsverzeichnis/DE/leistung/99148026017000/herausgeber/LeiKa-101301682/region/000000000000" },
  ],
};

export default note;
