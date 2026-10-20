import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n07-*.json (Banco Mundial MS.MIL.XPND.GD.ZS, datos del SIPRI, 2021 y 2025).
// Pautas de la OTAN (2 % en Gales, 2014; 3,5 % en La Haya, 2025), cotejadas en nato.int (ver sources).
const note: Note = {
  id: "n07",
  code: "N07",
  slug: { es: "gasto-defensa-paises", en: "defence-spending-by-country" },
  title: {
    es: "18 de los 27 países de la UE ya dedican a defensa el 2 % de su PIB o más; en 2021 eran 4",
    en: "18 of the 27 EU countries now spend 2% of their GDP or more on defence; in 2021 it was 4",
  },
  dek: {
    es: "Polonia gasta en defensa el 4,5 % de su PIB, más que nadie en la UE. Los países bálticos y Dinamarca superan el 3 %. Irlanda, Malta, Luxemburgo y Austria siguen por debajo del 1,5 %.",
    en: "Poland spends 4.5% of its GDP on defence, more than any other EU country. The Baltic states and Denmark are above 3%. Ireland, Malta, Luxembourg and Austria remain below 1.5%.",
  },
  published: "2026-10-20",
  updated: "2026-10-20",
  lens: "dentro",
  theme: "defensa",
  body: [
    p("En 2025, Polonia dedicó a defensa el 4,5 % de su PIB, según los datos del SIPRI que publica el Banco Mundial. Es la cifra más alta de la UE y unas 20 veces la de Irlanda (0,22 %). Le siguen Letonia (3,61 %), Estonia (3,37 %), Dinamarca (3,25 %) y Lituania (3,08 %). Grecia, con el 2,99 %, completa los seis primeros.",
      "In 2025, Poland spent 4.5% of its GDP on defence, according to SIPRI data published by the World Bank. That is the highest figure in the EU and about 20 times Ireland's (0.22%). Next come Latvia (3.61%), Estonia (3.37%), Denmark (3.25%) and Lithuania (3.08%). Greece, at 2.99%, completes the top six."),
    p("En el otro extremo, nueve países siguen por debajo del 2 %, la pauta que los aliados de la OTAN se fijaron en 2014. Entre ellos, Italia (1,89 %) y Portugal (1,71 %). Los cuatro últimos son Austria, Luxemburgo, Malta e Irlanda, y tres de ellos no están en la OTAN. España, con el 2,13 %, ocupa el puesto 12.",
      "At the other end, nine countries are still below 2%, the guideline NATO allies set themselves in 2014. Among them are Italy (1.89%) and Portugal (1.71%). The bottom four are Austria, Luxembourg, Malta and Ireland, and three of them are not in NATO. Spain, at 2.13%, ranks 12th."),
    { fig: "n07-defensa-paises", code: "1" },
    p("El salto ha sido rápido. En 2021, el último año antes de la invasión rusa de Ucrania, solo cuatro países llegaban al 2 %: Grecia, Polonia, Letonia y Estonia. En 2025 son 18. Polonia ha sumado 2,28 puntos de PIB y Dinamarca, 1,95. Solo Grecia, Chipre e Irlanda gastan hoy una parte menor de su PIB que en 2021; en Malta no ha cambiado.",
      "The jump has been fast. In 2021, the last year before Russia's invasion of Ukraine, only four countries reached 2%: Greece, Poland, Latvia and Estonia. In 2025 there are 18. Poland has added 2.28 points of GDP and Denmark 1.95. Only Greece, Cyprus and Ireland now spend a smaller share of GDP than in 2021; in Malta it is unchanged."),
    { fig: "n07-defensa-cambio", code: "2" },
    { see: { es: "Defensa y seguridad: cuánto gastan la UE, EE. UU., China y Rusia, y en qué", en: "Defence and security: how much the EU, the US, China and Russia spend, and on what" }, href: { es: "/es/defensa/", en: "/en/defence/" } },
    p("El listón ya es otro. En la cumbre de La Haya, en junio de 2025, los aliados se comprometieron a dedicar al menos el 3,5 % del PIB a defensa en 2035, con la definición de la OTAN, que no coincide con la del SIPRI. Con estos datos, solo Polonia y Letonia lo superan hoy. La comparación de la UE con EE. UU. y China está en el análisis del informe Draghi.",
      "The bar has moved. At the Hague summit in June 2025, allies pledged to spend at least 3.5% of GDP on defence by 2035, on NATO's definition, which differs from SIPRI's. On these figures, only Poland and Latvia are above it today. The comparison of the EU with the US and China is in the analysis of the Draghi report."),
    { see: { es: "El informe Draghi, dos años después: qué pedía, qué se ha hecho y qué dicen hoy los datos", en: "The Draghi report, two years on: what it asked for, what has been done and what the data say today" },
      href: { es: "/es/notas/informe-draghi-dos-anos-despues/", en: "/en/notes/draghi-report-two-years-on/" } },
    p("Lo que no dicen estos datos. El gasto en proporción del PIB no dice en qué se gasta, si en personal, armamento o investigación, ni si los ejércitos europeos pueden actuar juntos.",
      "What these data do not say. Spending as a share of GDP does not say what it goes on, whether personnel, weapons or research, or whether European armies can act together."),
  ],
  sources: [
    { name: "OTAN: Declaración de la cumbre de Gales (5/09/2014), párrafo 14", url: "https://www.nato.int/cps/en/natohq/official_texts_112964.htm" },
    { name: "OTAN: Declaración de la cumbre de La Haya (25/06/2025)", url: "https://www.nato.int/cps/en/natohq/official_texts_236705.htm" },
    { name: "Banco Mundial: gasto militar en % del PIB (datos del SIPRI)", url: "https://data.worldbank.org/indicator/MS.MIL.XPND.GD.ZS" },
  ],
};

export default note;
