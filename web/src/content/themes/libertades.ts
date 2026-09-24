import { p, type Theme } from "../../lib/content-types";

const theme: Theme = {
  id: "libertades",
  code: "LI",
  slug: { es: "libertades", en: "freedoms" },
  title: { es: "Libertades, bienestar y clima", en: "Freedoms, well-being and climate" },
  status: "published",
  order: 2,
  published: "2026-09-25",
  dek: {
    es: "Europa vive más años, contamina menos y protege más las libertades que Estados Unidos o China. Pero esas ventajas no son iguales en todos sus países, y algunas se están erosionando.",
    en: "Europe lives longer, pollutes less and protects freedoms more than the United States or China. But those advantages are not equal across its countries, and some are eroding.",
  },
  lenses: {
    gigantes: {
      lede: { es: "En democracia, salud y clima, la UE sale mejor parada que los dos gigantes.", en: "On democracy, health and climate, the EU fares better than both giants." },
      body: [
        p("Según V-Dem, la democracia estadounidense cayó en 2025 hasta 0,57 sobre 1, su nivel más bajo del siglo y ya por debajo de la mediana de la UE (0,74). China sigue en el extremo opuesto, con 0,04.",
          "According to V-Dem, US democracy fell in 2025 to 0.57 out of 1, its lowest level this century and now below the EU median (0.74). China remains at the opposite end, at 0.04."),
        { fig: "lg1-democracia", code: "G1" },
        p("En la UE se vive de media 81,6 años, casi tres más que en EE. UU. (78,9), donde la esperanza de vida apenas ha cambiado desde 2010. China, con 78,0, casi ha alcanzado a EE. UU.",
          "People in the EU live 81.6 years on average, almost three more than in the US (78.9), where life expectancy has barely changed since 2010. China, at 78.0, has nearly caught up with the US."),
        { fig: "lg2-esperanza-vida", code: "G2" },
        p("En clima, cada estadounidense emite 13,6 toneladas de CO₂ al año, más del doble que un europeo (5,5). Un chino emite ya 9,3 toneladas: más que un europeo desde 2012.",
          "On climate, each American emits 13.6 tonnes of CO₂ a year, more than twice as much as a European (5.5). A Chinese person now emits 9.3 tonnes: more than a European since 2012."),
        { fig: "lg3-co2-habitante", code: "G3" },
      ],
    },
    elige: {
      lede: { es: "Europa ha elegido recortar emisiones y proteger más a su población. Son decisiones con costes.", en: "Europe has chosen to cut emissions and protect its population more. Those are choices with costs." },
      body: [
        p("La UE emite hoy un 35 % menos de CO₂ que en 1990. Estados Unidos, un 7 % menos. China, más de cinco veces más. Parte del recorte europeo se explica porque fabrica fuera muchos de los bienes que consume.",
          "The EU now emits 35% less CO₂ than in 1990. The United States, 7% less. China, more than five times as much. Part of Europe's cut comes from producing abroad many of the goods it consumes."),
        { fig: "le1-emisiones-1990", code: "E1" },
        p("El gasto social público es la otra gran diferencia. En 2022, Francia le dedicaba el 31,4 % de su PIB; Italia, el 28,2 %; Alemania, el 27,7 %; España, el 26,0 %. EE. UU., el 19,0 %. Pero no es un rasgo de toda la UE: Irlanda, Países Bajos o varios países del este gastan menos que EE. UU.",
          "Public social spending is the other big difference. In 2022, France devoted 31.4% of its GDP to it; Italy, 28.2%; Germany, 27.7%; Spain, 26.0%. The US, 19.0%. But it is not a feature of the whole EU: Ireland, the Netherlands and several eastern countries spend less than the US."),
        { fig: "le2-gasto-social", code: "E2" },
      ],
    },
    dentro: {
      lede: { es: "La media europea esconde países que retroceden en democracia, con mucha más pobreza o muy por detrás en renovables.", en: "The European average hides countries sliding back on democracy, with far more poverty or far behind on renewables." },
      body: [
        p("Desde 2010, la calidad democrática ha bajado en 24 de los 27 países de la UE. Hungría es el caso más grave, seguida de Grecia, Eslovenia y Polonia. España ha pasado de 0,83 a 0,74.",
          "Since 2010, democratic quality has fallen in 24 of the 27 EU countries. Hungary is the most severe case, followed by Greece, Slovenia and Poland. Spain has gone from 0.83 to 0.74."),
        { fig: "ld1-democracia-ue", code: "D1" },
        p("El 20,9 % de los europeos está en riesgo de pobreza o exclusión social. En Chequia, el 11,5 %; en Bulgaria, el 29,0 %. España, con un 25,7 %, es el quinto país con más riesgo.",
          "20.9% of Europeans are at risk of poverty or social exclusion. In Czechia, 11.5%; in Bulgaria, 29.0%. Spain, at 25.7%, has the fifth highest risk."),
        { fig: "ld2-pobreza", code: "D2" },
        p("En renovables, Suecia (65 %) y Finlandia (53 %) ya superan de largo el objetivo europeo del 42,5 % para 2030. La UE en conjunto está en el 26 %, como España, y Bélgica no llega al 15 %.",
          "On renewables, Sweden (65%) and Finland (53%) are already well past the EU's 42.5% target for 2030. The EU as a whole is at 26%, like Spain, and Belgium does not reach 15%."),
        { fig: "ld3-renovables", code: "D3" },
      ],
    },
  },
};

export default theme;
