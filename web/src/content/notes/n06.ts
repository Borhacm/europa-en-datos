import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n06-*.json (FMI, World Economic Outlook de octubre de 2026, 2001-2024; Eurostat gov_10dd_edpt1, 2025).
// Medidas de la deuda de China y valor de referencia del 60 %, cotejados en el FMI y en EUR-Lex (ver sources).
const note: Note = {
  id: "n06",
  code: "N06",
  slug: { es: "deuda-publica", en: "public-debt" },
  title: {
    es: "La deuda pública de EE. UU. supera el 120 % de su PIB; la de la UE, el 80 %",
    en: "US public debt exceeds 120% of GDP; the EU's, 80%",
  },
  dek: {
    es: "En 2001, la UE debía más que EE. UU. Hoy, EE. UU. debe el 122,3 % de su PIB y la UE, el 81,6 %. Dentro de la UE, 12 de los 27 países superan el 60 % que fija el Tratado.",
    en: "In 2001, the EU owed more than the US. Today the US owes 122.3% of its GDP and the EU 81.6%. Within the EU, 12 of the 27 countries exceed the 60% set in the Treaty.",
  },
  published: "2026-10-13",
  lens: "gigantes",
  theme: "productividad",
  body: [
    p("En 2024, las administraciones públicas de EE. UU. debían el 122,3 % de su PIB, según el FMI. Las de la UE, el 81,6 %. En 2001 era al revés: la deuda de EE. UU. era del 53,5 % y la de la UE, del 65,6 %. Desde entonces, la de EE. UU. se ha más que duplicado; la de la UE ha subido 16 puntos.",
      "In 2024, US general government debt stood at 122.3% of GDP, according to the IMF. The EU's, at 81.6%. In 2001 it was the other way round: US debt was 53.5% and the EU's 65.6%. Since then, US debt has more than doubled; the EU's has risen by 16 points."),
    p("Las dos grandes subidas llegaron con las crisis. La primera, tras 2008. La segunda, en 2020, con la pandemia: la deuda de EE. UU. pasó del 108,8 % al 132,6 % en un año, y la de la UE, del 79 % al 91,1 %. Después, la UE la ha bajado hasta el 81,6 %. EE. UU. la redujo hasta el 119,2 % en 2022 y desde entonces ha vuelto a subir.",
      "The two big increases came with the crises. The first, after 2008. The second, in 2020, with the pandemic: US debt went from 108.8% to 132.6% in a year, and the EU's from 79% to 91.1%. Since then the EU has brought it down to 81.6%. The US cut it to 119.2% in 2022 and it has been rising again since."),
    p("La de China se ha multiplicado por 3,7: en la serie del FMI, ha pasado del 24,2 % en 2001 al 90,5 % en 2024, y está por encima de la UE desde 2023. También es la cifra más discutida. En su examen anual del país, de febrero de 2026, el propio FMI la sitúa en el 60,9 % en 2024 con la definición estrecha, y en el 126,6 % en 2025 si se suma la deuda de los vehículos de financiación de los gobiernos locales.",
      "China's has multiplied by 3.7: in the IMF series, it went from 24.2% in 2001 to 90.5% in 2024, and has been above the EU since 2023. It is also the most disputed figure. In its annual review of the country, in February 2026, the IMF itself puts it at 60.9% in 2024 on the narrow definition, and at 126.6% in 2025 once the debt of local government financing vehicles is added."),
    { fig: "n06-deuda-bloques", code: "1" },
    p("Dentro de la UE, las diferencias son enormes. El Tratado fija en el 60 % del PIB el valor de referencia para la deuda pública. En 2025, 12 de los 27 países lo superaban, con Grecia (146,1 %), Italia (137,1 %) y Francia (115,6 %) a la cabeza. España, con el 100,7 %, es la quinta. En el otro extremo, Estonia debe el 24,1 % y Luxemburgo, el 26,5 %. El conjunto de la UE, el 81,7 %, según Eurostat.",
      "Within the EU, the gaps are huge. The Treaty sets 60% of GDP as the reference value for public debt. In 2025, 12 of the 27 countries were above it, led by Greece (146.1%), Italy (137.1%) and France (115.6%). Spain, at 100.7%, ranks fifth. At the other end, Estonia owes 24.1% and Luxembourg 26.5%. The EU as a whole, 81.7%, according to Eurostat."),
    { fig: "n06-deuda-paises", code: "2" },
  ],
  sources: [
    { name: "FMI (18/02/2026): conclusión de la consulta del artículo IV de 2025 con China", url: "https://www.imf.org/en/News/Articles/2026/02/18/pr-26053-china-imf-executive-board-concludes-2025-article-iv-consultation" },
    { name: "EUR-Lex: Protocolo n.º 12 sobre el procedimiento aplicable en caso de déficit excesivo", url: "https://eur-lex.europa.eu/eli/treaty/tfeu_2016/pro_12/oj/eng" },
    { name: "FMI DataMapper: deuda bruta de las administraciones públicas", url: "https://www.imf.org/external/datamapper/GGXWDG_NGDP@WEO" },
  ],
};

export default note;
