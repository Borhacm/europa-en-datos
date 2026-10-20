import { p, type Theme } from "../../lib/content-types";

// Rehecho el 20/10/2026 (ver editorial/registro/comercio.md): guion, cuatro gráficos explicativos,
// ficha de los derechos compensatorios a los eléctricos chinos y párrafo de límites. Cifras comprobadas contra data/charts/c*.json.
const theme: Theme = {
  id: "comercio",
  code: "CO",
  slug: { es: "comercio", en: "trade" },
  title: { es: "Comercio y dependencias", en: "Trade and dependencies" },
  status: "published",
  order: 2,
  published: "2026-09-24",
  updated: "2026-10-20",
  dek: {
    es: "China ha adelantado a la UE como mayor exportador del mundo. Europa compra a China mucho más de lo que le vende y vende a EE. UU. mucho más de lo que le compra: depende de un gigante para abastecerse y del otro para vender. Desde 2022 ha cambiado de proveedor de gas y ha puesto aranceles a los eléctricos chinos, con resultados distintos.",
    en: "China has overtaken the EU as the world's largest exporter. Europe buys far more from China than it sells to it and sells far more to the US than it buys: it relies on one giant for supplies and on the other to sell. Since 2022 it has switched gas suppliers and put duties on Chinese electric cars, with different results.",
  },
  lenses: {
    gigantes: {
      lede: { es: "En dos décadas, el centro del comercio mundial se ha desplazado hacia China. La UE ha quedado en medio, entre el que vende y el que compra.", en: "In two decades, the centre of world trade has shifted towards China. The EU has ended up in the middle, between the seller and the buyer." },
      body: [
        p("En 2002, la UE aportaba el 18,9 % de las exportaciones mundiales de bienes y China, el 6,5 %. China la supera desde 2015, y en 2024 exportaba el 18,7 % del total mundial; la UE, el 14,7 %. En importaciones, el primero sigue siendo EE. UU., con el 16,8 % del total en 2024.",
          "In 2002, the EU supplied 18.9% of world goods exports and China 6.5%. China has been ahead since 2015, and in 2024 it exported 18.7% of the world total; the EU, 14.7%. In imports, the US is still first, with 16.8% of the total in 2024."),
        { fig: "cg1-cuota-mundial", code: "G1" },
        p("Las balanzas muestran los papeles de cada uno. En 2024, China vendió al mundo 916.000 millones de euros más de lo que compró, y EE. UU. compró 1,19 billones más de lo que vendió. La UE tuvo un superávit de 133.000 millones, y en 2025, de 114.000 millones.",
          "Trade balances show each one's role. In 2024, China sold the world 916 billion euros more than it bought, and the US bought 1.19 trillion more than it sold. The EU had a surplus of 133 billion, and in 2025, 114 billion."),
        { fig: "cg2-saldo-comercial", code: "G2" },
        p("Ese equilibrio europeo esconde dos desequilibrios opuestos. Con China, la UE tuvo en 2025 un déficit de 371.600 millones de euros, nueve veces el de 2002 (40.900 millones); el máximo fue en 2022, con 397.800. Con EE. UU., un superávit de 198.000 millones, tres veces el de 2002. El superávit con EE. UU. cubre algo más de la mitad del déficit con China.",
          "That European balance hides two opposite imbalances. With China, the EU ran a deficit of 371.6 billion euros in 2025, nine times that of 2002 (40.9 billion); the peak was in 2022, at 397.8. With the US, a surplus of 198 billion, three times that of 2002. The surplus with the US covers just over half of the deficit with China."),
        { fig: "cg3-saldo-bilateral", code: "G3" },
      ],
    },
    elige: {
      lede: { es: "Europa ha decidido reducir algunas dependencias. Con el gas lo ha conseguido; con los coches chinos, solo en parte.", en: "Europe has decided to reduce some dependencies. With gas it has succeeded; with Chinese cars, only in part." },
      body: [
        p("China suministraba en 2002 el 7,8 % de lo que la UE compraba fuera de la Unión; en 2025, el 22,6 %. En maquinaria y equipos de transporte, donde entran la electrónica, las baterías o los paneles solares, llegó al 40,6 % en 2022 y en 2025 estaba en el 35,8 %. La parte de EE. UU. apenas ha cambiado (del 14,7 % al 14,1 %).",
          "In 2002 China supplied 7.8% of what the EU bought from outside the Union; in 2025, 22.6%. In machinery and transport equipment, which includes electronics, batteries and solar panels, it reached 40.6% in 2022 and stood at 35.8% in 2025. The US share has barely changed (from 14.7% to 14.1%)."),
        { fig: "ce1-importaciones-origen", code: "E1" },
        p("El gas es el ejemplo de una dependencia que se ha reducido. En 2021, Rusia suministraba el 46,9 % del gas que la UE importaba de fuera; en 2023, el 12,2 %, y en 2024 repuntó al 14,6 %. Su lugar lo han ocupado Noruega, que ha pasado del 18,2 % al 32,2 %, y EE. UU., con su gas licuado, del 6,2 % al 17,1 %. Europa depende menos de Rusia, pero más de EE. UU., que ya es su mayor cliente.",
          "Gas is an example of a dependency that has been reduced. In 2021, Russia supplied 46.9% of the gas the EU imported from abroad; in 2023, 12.2%, and in 2024 it edged back up to 14.6%. Its place has been taken by Norway, which went from 18.2% to 32.2%, and the US, with its liquefied gas, from 6.2% to 17.1%. Europe depends less on Russia, but more on the US, which is already its biggest customer."),
        { fig: "ce3-gas-origen", code: "E2" },
        { see: { es: "Energía: de dónde sale la electricidad y cuánto cuesta en cada país", en: "Energy: where electricity comes from and what it costs in each country" }, href: { es: "/es/energia/", en: "/en/energy/" } },
        { h: { es: "La ficha: los aranceles a los eléctricos chinos", en: "The policy card: duties on Chinese electric cars" }, id: "ficha-electricos" },
        { steps: [
          { title: { es: "Qué es.", en: "What it is." },
            text: { es: "Un derecho compensatorio: un arancel extra que la UE impone cuando concluye que un producto importado recibe subvenciones que perjudican a la industria europea. El Reglamento de Ejecución (UE) 2024/2754 lo aplica a los turismos eléctricos de batería nuevos fabricados en China. No afecta a los híbridos.",
                    en: "A countervailing duty: an extra tariff the EU imposes when it concludes that an imported product receives subsidies that harm European industry. Implementing Regulation (EU) 2024/2754 applies it to new battery electric cars made in China. It does not cover hybrids." } },
          { title: { es: "Quién y cuándo.", en: "Who and when." },
            text: { es: "La Comisión impuso derechos provisionales el 3 de julio de 2024 (Reglamento 2024/1866) y definitivos el 29 de octubre de 2024, en vigor desde el día siguiente. Van del 7,8 % para Tesla al 17,0 % para BYD, el 18,8 % para Geely y el 35,3 % para SAIC y las empresas que no cooperaron; el resto de las que cooperaron pagan el 20,7 %.",
                    en: "The Commission imposed provisional duties on 3 July 2024 (Regulation 2024/1866) and definitive ones on 29 October 2024, in force from the following day. They range from 7.8% for Tesla to 17.0% for BYD, 18.8% for Geely and 35.3% for SAIC and non-cooperating companies; other cooperating companies pay 20.7%." } },
          { title: { es: "Qué debería pasar.", en: "What should happen." },
            text: { es: "Que los eléctricos chinos se encarezcan en Europa y se importen menos, para dar margen a los fabricantes europeos.",
                    en: "Chinese electric cars should become more expensive in Europe and fewer should be imported, giving European manufacturers room." } },
          { title: { es: "Con qué lo comparamos.", en: "What we compare it with." },
            text: { es: "Con los híbridos chinos, que no pagan el derecho. No es un grupo de control perfecto: la demanda de cada tipo de coche cambia por sí sola.",
                    en: "With Chinese hybrids, which do not pay the duty. It is not a perfect control group: demand for each type of car changes on its own." } },
        ] },
        p("Las importaciones de eléctricos chinos pasaron de 11.030 millones de euros en 2023 a 6.350 millones en 2025, un 42 % menos. Pero las de híbridos enchufables chinos se triplicaron en 2025 (de 1.090 a 3.590 millones) y las de híbridos no enchufables subieron de 190 millones en 2023 a 1.810 millones. En total, la UE compró a China 11.750 millones en turismos eléctricos e híbridos en 2025, solo un 4 % menos que en 2023. El arancel ha cambiado qué coches llegan de China más que cuántos.",
          "Imports of Chinese electric cars fell from 11.03 billion euros in 2023 to 6.35 billion in 2025, 42% less. But imports of Chinese plug-in hybrids tripled in 2025 (from 1.09 to 3.59 billion) and those of non-plug-in hybrids rose from 190 million in 2023 to 1.81 billion. In total, the EU bought 11.75 billion euros of electric and hybrid cars from China in 2025, only 4% less than in 2023. The duty has changed which cars arrive from China more than how many."),
        { fig: "ce4-coches-china", code: "E3" },
        { see: { es: "Nota: qué parte de los coches nuevos ya son eléctricos en cada país", en: "Note: what share of new cars are already electric in each country" }, href: { es: "/es/notas/coche-electrico/", en: "/en/notes/electric-cars/" } },
      ],
    },
    dentro: {
      lede: { es: "El mercado único sigue siendo el primer socio de casi todos. La exposición a EE. UU. y a la energía importada, en cambio, va por países.", en: "The single market is still almost everyone's first partner. Exposure to the US and to imported energy, however, varies by country." },
      body: [
        p("De cada diez euros que exportan los países de la UE, seis van a otros países de la Unión: el 61,0 % en 2025, casi lo mismo que en 2004 (61,5 %). Chequia y Eslovaquia venden en la UE casi el 80 % de lo que exportan; Irlanda, el 33,5 %, y Chipre, el 27,6 %. España, el 61,8 %.",
          "Of every ten euros EU countries export, six go to other EU countries: 61.0% in 2025, almost the same as in 2004 (61.5%). Czechia and Slovakia sell almost 80% of their exports within the EU; Ireland, 33.5%, and Cyprus, 27.6%. Spain, 61.8%."),
        { fig: "cd1-comercio-intra", code: "D1" },
        p("La dependencia de EE. UU. tampoco es igual para todos. En 2025, la UE exportó a EE. UU. bienes por valor del 2,9 % de su PIB. Irlanda, del 18,5 %: el 82 % de lo que vende a EE. UU. son químicos orgánicos y medicamentos. Bélgica y Países Bajos, con grandes puertos, del 5,0 % y el 3,7 %; Alemania, del 3,2 %, y es el país que más vende en euros. España, del 1,0 %, la octava más baja. Son los países que más notan cualquier cambio en los aranceles estadounidenses.",
          "Dependence on the US is not the same for everyone either. In 2025, the EU exported goods to the US worth 2.9% of its GDP. Ireland, 18.5%: 82% of what it sells to the US is organic chemicals and medicines. Belgium and the Netherlands, with large ports, 5.0% and 3.7%; Germany, 3.2%, and it is the country that sells most in euros. Spain, 1.0%, the eighth lowest. These are the countries that most feel any change in US tariffs."),
        { fig: "cd3-exposicion-eeuu", code: "D2" },
        p("En energía, la UE importó en 2024 el 57,3 % de la que usa. Malta (98,4 %), Luxemburgo (91,0 %) y Chipre (87,7 %) dependen casi por completo de fuera; España, en el 68,9 %, más que la media. Solo Estonia está por debajo del 10 %, con el 4,6 %.",
          "In energy, the EU imported 57.3% of what it used in 2024. Malta (98.4%), Luxembourg (91.0%) and Cyprus (87.7%) depend almost entirely on imports; Spain, at 68.9%, more than the average. Only Estonia is below 10%, at 4.6%."),
        { fig: "cd2-dependencia-energetica", code: "D3" },
        p("Lo que no dicen estos datos. Todo es comercio de bienes: los servicios, como el software, las finanzas o el turismo, no aparecen. Los valores están en euros corrientes, así que mezclan cantidades y precios: el valor de los coches chinos baja también si bajan sus precios. Las estadísticas atribuyen cada exportación al país por el que sale y cada importación al país del que llega, que no siempre es donde se produce. Y ninguno de estos gráficos permite separar el efecto del arancel a los eléctricos de otros cambios del mercado al mismo tiempo, como la propia demanda europea de coches eléctricos.",
          "What these data do not say. Everything is trade in goods: services, such as software, finance or tourism, do not appear. Values are in current euros, so they mix quantities and prices: the value of Chinese cars also falls if their prices fall. The statistics attribute each export to the country it leaves from and each import to the country it arrives from, which is not always where it was produced. And none of these charts can separate the effect of the duty on electric cars from other market changes happening at the same time, such as European demand for electric cars itself."),
      ],
    },
  },
  sources: [
    { name: "EUR-Lex: Reglamento de Ejecución (UE) 2024/2754, derechos compensatorios definitivos sobre los vehículos eléctricos de batería de China", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R2754" },
    { name: "EUR-Lex: Reglamento de Ejecución (UE) 2024/1866, derechos compensatorios provisionales", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R1866" },
    { name: "Eurostat: Comext, comercio internacional por producto (DS-045409)", url: "https://ec.europa.eu/eurostat/comext/newxtweb/" },
  ],
};

export default theme;
