import { p, type Theme } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/df*.json (SIPRI vía Banco Mundial y Eurostat COFOG). Ver editorial/registro/defensa.md.
// Ficha del Reglamento (UE) 2025/1106 (SAFE) cotejada en EUR-Lex (arts. 1, 6, 7, 16, 23 y considerandos 19 y 28).
const theme: Theme = {
  id: "defensa",
  code: "DF",
  slug: { es: "defensa", en: "defence" },
  title: { es: "Defensa y seguridad", en: "Defence and security" },
  status: "published",
  order: 10,
  published: "2026-10-20",
  dek: {
    es: "La UE gasta en defensa más que China y menos de la mitad que EE. UU., y desde 2021 ha subido su gasto un 76 % en dólares. Compra fuera tres veces más armas que hace cinco años, invierte más en equipos y menos en sueldos, y entre países las diferencias son enormes: por habitante, Dinamarca gasta casi como EE. UU. y Malta, menos de 300 dólares.",
    en: "The EU spends more on defence than China and less than half as much as the US, and since 2021 its spending has risen 76% in dollars. It buys three times as many arms abroad as five years ago, invests more in equipment and less in pay, and the gaps between countries are huge: per person, Denmark spends almost as much as the US and Malta less than 300 dollars.",
  },
  lenses: {
    gigantes: {
      lede: { es: "La UE gasta en defensa más que China y bastante más que Rusia, aunque lejos de EE. UU. Rusia ha disparado su gasto, pero vende muchas menos armas.", en: "The EU spends more on defence than China and far more than Russia, although well short of the US. Russia has sent its spending soaring, but sells far fewer arms." },
      body: [
        p("En 2025, los 27 países de la UE gastaron en defensa unos 461.000 millones de dólares, según los datos del SIPRI que publica el Banco Mundial. Es menos de la mitad que EE. UU. (954.400 millones), pero más que China (335.500 millones) y 2,4 veces lo que Rusia (190.400 millones). Desde 2021, el último año antes de la invasión rusa de Ucrania, el gasto de la UE ha subido un 76 % en dólares; el de EE. UU., un 18 %, y el de China, un 17 %. El de Rusia casi se ha triplicado: un 189 % más. EE. UU. gastó en 2025 menos que en 2024, cuando superó el billón de dólares.",
          "In 2025, the 27 EU countries spent about 461 billion dollars on defence, according to SIPRI data published by the World Bank. That is less than half the US figure (954.4 billion), but more than China (335.5 billion) and 2.4 times Russia (190.4 billion). Since 2021, the last year before Russia's invasion of Ukraine, EU spending has risen 76% in dollars; US spending, 18%, and China's, 17%. Russia's has almost tripled: up 189%. The US spent less in 2025 than in 2024, when it passed a trillion dollars."),
        { fig: "dfg1-gasto-dolares", code: "G1" },
        { see: { es: "Análisis: el informe Draghi, dos años después, y el gasto en defensa en % del PIB", en: "Analysis: the Draghi report two years on, and defence spending as % of GDP" }, href: { es: "/es/notas/informe-draghi-dos-anos-despues/", en: "/en/notes/draghi-report-two-years-on/" } },
        p("Rusia gasta más, pero ya no vende como antes. Entre 2016 y 2020 exportó casi tantas armas como los 27 países de la UE juntos. Entre 2021 y 2025, un 64 % menos que en esos cinco años, y menos de la cuarta parte que la UE, cuyas exportaciones han crecido un 36 %. EE. UU., el mayor vendedor, ha aumentado las suyas un 27 %, y China, un 11 %.",
          "Russia spends more, but no longer sells as it did. Between 2016 and 2020 it exported almost as many arms as the 27 EU countries together. Between 2021 and 2025, 64% less than in those five years, and less than a quarter of the EU's, whose exports have grown 36%. The US, the largest seller, has increased its exports by 27%, and China by 11%."),
        { fig: "dfg2-exportaciones-armas", code: "G2" },
      ],
    },
    elige: {
      lede: { es: "Para rearmarse deprisa, Europa ha comprado fuera. Ahora intenta que el dinero se quede en su industria, y ya lo gasta de otra manera.", en: "To rearm quickly, Europe has bought abroad. Now it is trying to keep the money in its own industry, and it already spends it differently." },
      body: [
        p("Entre 2021 y 2025, los países de la UE importaron tres veces más armas que entre 2016 y 2020, medidas en volumen con la unidad del SIPRI. Polonia es el que más compra, casi diez veces más que en el periodo anterior, seguida de los Países Bajos y Alemania. Solo Luxemburgo, Italia, Finlandia e Irlanda importaron menos. Estos datos incluyen las compras entre países de la UE, así que no dicen cuánto viene de EE. UU. o de otros proveedores de fuera.",
          "Between 2021 and 2025, EU countries imported three times as many arms as between 2016 and 2020, measured by volume in SIPRI's unit. Poland buys the most, almost ten times as much as in the previous period, followed by the Netherlands and Germany. Only Luxembourg, Italy, Finland and Ireland imported less. These data include purchases between EU countries, so they do not say how much comes from the US or other outside suppliers."),
        { fig: "dfe1-importaciones-armas", code: "E1" },
        { h: { es: "La ficha: SAFE, los préstamos europeos para comprar defensa", en: "The policy card: SAFE, EU loans to buy defence" }, id: "ficha-safe" },
        { steps: [
          { title: { es: "Qué es.", en: "What it is." },
            text: { es: "El instrumento Acción por la Seguridad de Europa (SAFE) presta dinero a los Estados miembros para inversiones urgentes en defensa que apoyen a la industria europea, en particular las compras que hacen varios países en común. Los préstamos pueden sumar hasta 150.000 millones de euros.",
                    en: "The Security Action for Europe (SAFE) instrument lends money to member states for urgent defence investment that supports European industry, in particular purchases made jointly by several countries. The loans can total up to 150 billion euros." } },
          { title: { es: "Quién y cuándo.", en: "Who and when." },
            text: { es: "Lo aprobó el Consejo el 27 de mayo de 2025, con el artículo 122 del Tratado de Funcionamiento de la UE. Los países tenían hasta el 30 de noviembre de 2025 para pedir los préstamos, con un plan de inversión. Los préstamos pueden durar hasta 45 años, con diez de carencia.",
                    en: "The Council adopted it on 27 May 2025, under Article 122 of the Treaty on the Functioning of the EU. Countries had until 30 November 2025 to apply for the loans, with an investment plan. The loans can run for up to 45 years, with a ten-year grace period." } },
          { title: { es: "Qué debería pasar.", en: "What should happen." },
            text: { es: "Que se compre más en Europa. En las compras en común que financia, los componentes de fuera de la UE, del Espacio Económico Europeo y de Ucrania no pueden superar el 35 % del coste.",
                    en: "More should be bought in Europe. In the joint purchases it finances, components from outside the EU, the European Economic Area and Ukraine cannot exceed 35% of the cost." } },
          { title: { es: "Con qué lo comparamos.", en: "What we compare it with." },
            text: { es: "Con E1, que muestra cómo se han triplicado las importaciones. Esos datos llegan hasta 2025 y no separan lo que se compra dentro de la UE, así que todavía no permiten ver si SAFE cambia hacia dónde va el dinero.",
                    en: "With E1, which shows imports tripling. Those data run to 2025 and do not separate what is bought within the EU, so they cannot yet show whether SAFE changes where the money goes." } },
        ] },
        p("El dinero también se gasta de otra manera. En 2014, el 54 % del gasto de las administraciones europeas en defensa eran sueldos y cotizaciones; en 2024, el 39 %. Los sueldos no han bajado: han crecido menos que lo demás. La inversión en equipos e infraestructuras ha pasado del 15,5 % al 21,6 % del gasto, y las transferencias, del 2,3 % al 8,4 %, casi todo desde 2022. En euros, el gasto en defensa casi se ha duplicado: de 136.412 millones en 2014 a 266.360 millones en 2024.",
          "The money is also spent differently. In 2014, 54% of European governments' defence spending was pay and contributions; in 2024, 39%. Pay has not fallen: it has grown less than everything else. Investment in equipment and infrastructure has risen from 15.5% to 21.6% of spending, and transfers from 2.3% to 8.4%, almost all of it since 2022. In euros, defence spending has almost doubled: from 136,412 million in 2014 to 266,360 million in 2024."),
        { fig: "dfe2-composicion-gasto", code: "E2" },
        { see: { es: "Finanzas públicas: la cláusula de escape que permite a 18 países gastar más en defensa", en: "Public finances: the escape clause that lets 18 countries spend more on defence" }, href: { es: "/es/finanzas-publicas/", en: "/en/public-finances/" } },
      ],
    },
    dentro: {
      lede: { es: "Detrás de la media hay países que gastan por habitante casi como EE. UU. y otros que apenas gastan, y también cambia en qué.", en: "Behind the average are countries that spend almost as much per person as the US and others that barely spend at all, and what they spend on differs too." },
      body: [
        p("Por habitante, Dinamarca gastó en defensa 2.488 dólares en 2025, el 89 % de lo que gasta EE. UU. (2.792). Le siguen los Países Bajos (1.600), Suecia (1.555) y Finlandia (1.431). En el otro extremo, Malta (215) e Irlanda (283) no llegan a 300 dólares. Polonia, que es el país que más gasta en proporción a su PIB, es sexto por habitante, con 1.283 dólares. España gasta 815, casi como Italia (817) y Grecia (805).",
          "Per person, Denmark spent 2,488 dollars on defence in 2025, 89% of what the US spends (2,792). Next come the Netherlands (1,600), Sweden (1,555) and Finland (1,431). At the other end, Malta (215) and Ireland (283) are below 300 dollars. Poland, the country that spends most relative to its GDP, ranks sixth per person, at 1,283 dollars. Spain spends 815, almost the same as Italy (817) and Greece (805)."),
        { fig: "dfd1-gasto-habitante", code: "D1" },
        { see: { es: "Nota: el gasto en defensa de cada país, en % del PIB, frente a la pauta de la OTAN", en: "Note: each country's defence spending as % of GDP, against the NATO guideline" }, href: { es: "/es/notas/gasto-defensa-paises/", en: "/en/notes/defence-spending-by-country/" } },
        p("En qué se va el dinero cambia aún más. En 2024, Estonia dedicó a inversión el 43,6 % de su gasto en defensa, y Polonia, el 38,9 %. Les siguen Lituania (37,6 %) y Hungría (37,2 %). En el otro extremo, Irlanda (7,7 %), Bulgaria (9,3 %) y Finlandia (9,6 %) invierten menos del 10 %, y Alemania, el 14,3 %. España, el 21,5 %.",
          "What the money goes on varies even more. In 2024, Estonia put 43.6% of its defence spending into investment, and Poland 38.9%. Next come Lithuania (37.6%) and Hungary (37.2%). At the other end, Ireland (7.7%), Bulgaria (9.3%) and Finland (9.6%) invest less than 10%, and Germany 14.3%. Spain, 21.5%."),
        { fig: "dfd2-inversion-paises", code: "D2" },
        p("Lo que no dicen estos datos. El SIPRI y Eurostat miden el gasto en defensa con definiciones distintas, y ninguna es la que usa la OTAN para sus pautas del 2 % y del 3,5 % del PIB. Las cifras en dólares cambian con el tipo de cambio. Los TIV miden volumen de armas, no dinero, y no dicen de dónde vienen las que compra cada país. Y más gasto no significa más capacidad: estos datos no dicen cuántos soldados, aviones o municiones tiene cada país, ni si los ejércitos europeos pueden actuar juntos.",
          "What these data do not say. SIPRI and Eurostat measure defence spending with different definitions, and neither is the one NATO uses for its 2% and 3.5% of GDP guidelines. Dollar figures change with the exchange rate. TIVs measure the volume of arms, not money, and do not say where each country's purchases come from. And more spending does not mean more capability: these data do not say how many soldiers, aircraft or munitions each country has, or whether European armed forces can act together."),
      ],
    },
  },
  sources: [
    { name: "EUR-Lex: Reglamento (UE) 2025/1106 del Consejo, por el que se crea el instrumento SAFE", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32025R1106" },
    { name: "Consejo de la UE: cláusula de escape nacional para el gasto en defensa", url: "https://www.consilium.europa.eu/en/policies/national-escape-clause-for-defence-expenditure-nec/" },
    { name: "OTAN: Declaración de la cumbre de Gales (5/09/2014)", url: "https://www.nato.int/cps/en/natohq/official_texts_112964.htm" },
    { name: "OTAN: Declaración de la cumbre de La Haya (25/06/2025)", url: "https://www.nato.int/cps/en/natohq/official_texts_236705.htm" },
  ],
};

export default theme;
