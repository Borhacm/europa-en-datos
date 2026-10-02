import { p, type Theme } from "../../lib/content-types";

const theme: Theme = {
  id: "dinero",
  code: "DI",
  slug: { es: "dinero", en: "money" },
  title: { es: "Dinero y pagos", en: "Money and payments" },
  status: "published",
  order: 6,
  published: "2026-10-02",
  dek: {
    es: "La zona del euro guarda más efectivo que EE. UU. y China en relación con su economía, pero cada vez paga menos con él. El hueco lo llenan las tarjetas, en buena parte de redes no europeas. El euro digital es la apuesta de la UE para que el dinero público siga presente en los pagos electrónicos.",
    en: "The euro area holds more cash relative to its economy than the US and China, but uses it less and less to pay. Cards are filling the gap, largely through non-European networks. The digital euro is the EU's bet to keep public money present in electronic payments.",
  },
  lenses: {
    gigantes: {
      lede: {
        es: "La zona del euro tiene más efectivo que EE. UU. y China en relación con su PIB. En pagos electrónicos, EE. UU. va por delante y China es la que más ha crecido.",
        en: "The euro area has more cash than the US and China relative to its GDP. In electronic payments, the US is ahead and China has grown the fastest.",
      },
      body: [
        p("En 2024, los billetes y monedas en euros equivalían al 10,7 % del PIB de la zona del euro. En China, al 9,9 %, y en EE. UU., al 7,9 %. Los tres subieron en 2020, con la pandemia, y la zona del euro llegó al 12,6 %. Desde entonces el efectivo pesa menos en la zona del euro y en EE. UU., mientras que en China ha vuelto a crecer desde 2021.",
          "In 2024, euro banknotes and coins were worth 10.7% of euro area GDP. In China, 9.9%, and in the US, 7.9%. All three rose in 2020, with the pandemic, and the euro area reached 12.6%. Since then cash has weighed less in the euro area and the US, while in China it has grown again since 2021."),
        { fig: "dig1-efectivo-pib", code: "G1" },
        p("Tener mucho efectivo no significa usarlo para pagar: una parte se guarda como ahorro y otra circula fuera. Los pagos electrónicos cuentan otra historia. En 2024, en EE. UU. se hicieron 644 pagos sin efectivo por habitante, y en China, 402, casi 28 veces más que en 2012. El BIS no publica el dato de la UE, pero sí el de siete de sus países. Suecia (685) supera a EE. UU.; Bélgica, Francia y Alemania quedan entre EE. UU. y China, y España (364) e Italia (247), por debajo de China.",
          "Holding a lot of cash does not mean using it to pay: part of it is kept as savings and part circulates abroad. Electronic payments tell a different story. In 2024, the US made 644 cashless payments per person, and China 402, almost 28 times as many as in 2012. The BIS does not publish an EU figure, but it does for seven EU countries. Sweden (685) is ahead of the US; Belgium, France and Germany sit between the US and China, and Spain (364) and Italy (247) are below China."),
        { fig: "dig2-pagos-sin-efectivo", code: "G2" },
        p("Los dos gigantes han elegido caminos opuestos para el dinero digital. China prueba su yuan digital, el e-CNY, emitido por su banco central, desde finales de 2019. EE. UU. ha ido en la dirección contraria: en enero de 2025, una orden ejecutiva prohibió a las agencias federales crear o promover un dólar digital, y en julio de 2025 la ley GENIUS reguló las stablecoins, monedas digitales privadas respaldadas por activos en dólares.",
          "The two giants have chosen opposite paths for digital money. China has been testing its digital yuan, the e-CNY, issued by its central bank, since the end of 2019. The US has gone the other way: in January 2025 an executive order barred federal agencies from creating or promoting a digital dollar, and in July 2025 the GENIUS Act regulated stablecoins, private digital coins backed by dollar assets."),
      ],
    },
    elige: {
      lede: {
        es: "Los europeos pagan cada vez menos con efectivo, pero no quieren perderlo. El euro digital es la respuesta de la UE: dinero público para pagar con el móvil.",
        en: "Europeans pay less and less in cash, but do not want to lose it. The digital euro is the EU's answer: public money to pay with a phone.",
      },
      body: [
        p("En 2016, el 79 % de los pagos en tiendas, bares y otros comercios de la zona del euro se hacía con efectivo. En 2024, el 52 %. El 55 % de los consumidores ya prefiere pagar con tarjeta u otro medio sin efectivo, frente al 22 % que prefiere los billetes. Aun así, el 62 % considera importante poder seguir pagando con efectivo.",
          "In 2016, 79% of payments in shops, bars and other businesses in the euro area were made in cash. In 2024, 52%. 55% of consumers now prefer to pay by card or another cashless method, against 22% who prefer notes and coins. Even so, 62% consider it important to keep being able to pay in cash."),
        { fig: "die1-pago-en-tienda", code: "E1" },
        p("El hueco del efectivo lo llenan sobre todo las tarjetas. En 2025 se hicieron en la zona del euro casi 92.000 millones de pagos con tarjeta, el 57 % de todos los pagos sin efectivo y un 36 % más que en 2022. Ahí está lo que preocupa al BCE: en 2022, el 61 % de los pagos con tarjeta de la zona del euro pasó por redes internacionales como Visa o Mastercard, y 13 países de la zona dependen por completo de ellas.",
          "Cards are filling most of the gap left by cash. In 2025, the euro area made almost 92 billion card payments, 57% of all cashless payments and 36% more than in 2022. That is what worries the ECB: in 2022, 61% of euro area card payments went through international networks such as Visa or Mastercard, and 13 euro area countries rely on them entirely."),
        { fig: "die2-pagos-zona-euro", code: "E2" },
        p("El euro digital busca ser una alternativa europea y pública: dinero emitido por el BCE, como los billetes, pero para pagar en tiendas, en internet y también sin conexión. Los servicios básicos serían gratuitos y habría un límite de cuánto puede guardar cada persona. Lo que falta es la ley. Parlamento y Consejo negocian sobre todo cómo se compensa a los bancos y entidades que lo distribuyan, cómo se reparte y cuál es ese límite. La privacidad es la otra gran duda: el 60 % de los consumidores de la zona del euro dice preocuparse por su privacidad en los pagos digitales.",
          "The digital euro aims to be a European, public alternative: money issued by the ECB, like banknotes, but for paying in shops, online and offline too. Basic services would be free and there would be a cap on how much each person can hold. What is missing is the law. Parliament and Council are negotiating mainly how banks and payment firms that distribute it are compensated, how distribution works and where that cap lies. Privacy is the other big question: 60% of euro area consumers say they are concerned about their privacy in digital payments."),
        {
          timeline: [
            { date: { es: "Junio de 2023", en: "June 2023" }, text: { es: "La Comisión Europea propone el reglamento del euro digital.", en: "The European Commission proposes the digital euro regulation." } },
            { date: { es: "Octubre de 2025", en: "October 2025" }, text: { es: "El BCE pasa a la siguiente fase del proyecto para estar listo técnicamente.", en: "The ECB moves the project to its next phase to be technically ready." } },
            { date: { es: "Diciembre de 2025", en: "December 2025" }, text: { es: "Los gobiernos de la UE, en el Consejo, fijan su posición: límites de tenencia, servicios básicos gratuitos y comisiones reguladas.", en: "EU governments, in the Council, agree their position: holding limits, free basic services and regulated fees." } },
            { date: { es: "Junio y julio de 2026", en: "June and July 2026" }, text: { es: "La comisión de Asuntos Económicos del Parlamento Europeo aprueba su informe (43 votos a favor, 14 en contra y 1 abstención) y el pleno da luz verde a negociar con el Consejo.", en: "The European Parliament's Economic Affairs Committee adopts its report (43 votes in favour, 14 against and 1 abstention) and the plenary gives the go-ahead to negotiate with the Council." } },
            { date: { es: "Segunda mitad de 2027", en: "Second half of 2027" }, text: { es: "Piloto de 12 meses con entidades de pago, si la ley se aprueba en 2026.", en: "12-month pilot with payment providers, if the law is adopted in 2026." } },
            { date: { es: "2029", en: "2029" }, text: { es: "Primera emisión posible. El BCE decidirá si lo emite, y cuándo, cuando la ley esté aprobada.", en: "Earliest possible issuance. The ECB will decide whether and when to issue it once the law is adopted." } },
          ],
        },
      ],
    },
    dentro: {
      lede: {
        es: "La tarjeta gana terreno en todos los países, pero a ritmos muy distintos. El efectivo retrocede más despacio.",
        en: "Cards are gaining ground in every country, but at very different speeds. Cash is retreating more slowly.",
      },
      body: [
        p("En 2025, en Finlandia se hicieron 456 pagos con tarjeta por habitante; en los Países Bajos, 376, y en Francia, 320. En Alemania, 174, y en Italia, 162, entre los más bajos junto a Rumanía (172) y Bulgaria (105). España, con 265, está justo en la mediana de los 25 países con datos. Lituania, Luxemburgo e Irlanda superan a todos, pero sus cifras pueden reflejar entidades de pago con sede allí y clientes en otros países. Entre 2022 y 2025, los pagos con tarjeta por habitante aumentaron en los 24 países con datos de ambos años, desde el 13 % de los Países Bajos hasta el 92 % de Rumanía.",
          "In 2025, Finland made 456 card payments per person; the Netherlands, 376, and France, 320. Germany made 174, and Italy 162, among the lowest along with Romania (172) and Bulgaria (105). Spain, with 265, is exactly at the median of the 25 countries with data. Lithuania, Luxembourg and Ireland are above everyone, but their figures may reflect payment institutions based there with customers in other countries. Between 2022 and 2025, card payments per person rose in all 24 countries with data for both years, from 13% in the Netherlands to 92% in Romania."),
        { fig: "did1-pagos-tarjeta", code: "D1" },
        p("Las retiradas de efectivo con tarjeta bajaron en 20 de los 21 países con datos de 2022 y 2025; en Rumanía apenas cambiaron. La mayor caída fue la de Estonia, un 28 %. Donde más se saca dinero con tarjeta es en Portugal, 30,6 veces por habitante al año, y donde menos, en Hungría (8,6), Finlandia (9,1) y los Países Bajos (9,3). En España, 13,5 veces, casi igual que en 2022 (13,6).",
          "Cash withdrawals with cards fell in 20 of the 21 countries with data for 2022 and 2025; in Romania they barely changed. The biggest drop was in Estonia, 28%. People withdraw cash with cards most often in Portugal, 30.6 times per person a year, and least often in Hungary (8.6), Finland (9.1) and the Netherlands (9.3). In Spain, 13.5 times, almost the same as in 2022 (13.6)."),
        { fig: "did2-retiradas-efectivo", code: "D2" },
      ],
    },
  },
  sources: [
    { name: "Parlamento Europeo, Legislative Train: Digital euro (actualizado el 20 de septiembre de 2026)", url: "https://www.europarl.europa.eu/legislative-train/theme-a-new-plan-for-europe-s-sustainable-prosperity-and-competitiveness/file-digital-euro" },
    { name: "BCE, El Eurosistema pasa a la siguiente fase del proyecto del euro digital (30 de octubre de 2025)", url: "https://www.ecb.europa.eu/press/pr/date/2025/html/ecb.pr251030~8c5b5beef0.en.html" },
    { name: "Consejo de la UE, posición sobre el euro digital y el papel del efectivo (diciembre de 2025)", url: "https://www.consilium.europa.eu/en/press/press-releases/2025/12/19/single-currency-council-agrees-position-on-the-digital-euro-and-on-strengthening-the-role-of-cash/" },
    { name: "BCE, informe sobre sistemas y procesadores de tarjetas (28 de febrero de 2025)", url: "https://www.ecb.europa.eu/press/pr/date/2025/html/ecb.pr250228_1~7f0697af45.en.html" },
    { name: "BCE, estadísticas de pagos del segundo semestre de 2025", url: "https://www.ecb.europa.eu/press/stats/paysec/html/ecb.pis2025h2~23986fb4a6.en.html" },
    { name: "BCE, estudio SPACE 2024 sobre las actitudes de pago de los consumidores", url: "https://www.ecb.europa.eu/stats/ecb_surveys/space/html/ecb.space2024~19d46f0f17.en.html" },
    { name: "Banco Popular de China, Progress of Research and Development of E-CNY in China (julio de 2021)", url: "https://www.pbc.gov.cn/en/3688110/3688172/4157443/4293696/2021072014364791207.pdf" },
    { name: "Casa Blanca, orden ejecutiva 14178 sobre tecnología financiera digital (23 de enero de 2025)", url: "https://www.whitehouse.gov/presidential-actions/2025/01/strengthening-american-leadership-in-digital-financial-technology/" },
    { name: "Congreso de EE. UU., ley GENIUS sobre stablecoins (S. 1582, firmada el 18 de julio de 2025)", url: "https://www.congress.gov/bill/119th-congress/senate-bill/1582" },
  ],
};

export default theme;
