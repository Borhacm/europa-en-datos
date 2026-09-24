import { p, type Note } from "../../lib/content-types";

// Cifras de los gráficos comprobadas contra data/charts/n03-*.json (Banco Mundial).
// Cifras del informe y de su aplicación comprobadas en la Comisión Europea y en el JEDI Draghi Tracker (ver sources).
const note: Note = {
  id: "n03",
  code: "N03",
  slug: { es: "informe-draghi", en: "draghi-report" },
  title: {
    es: "El informe Draghi, en dos gráficos: Europa crece menos y necesita invertir mucho más",
    en: "The Draghi report in two charts: Europe grows less and needs to invest much more",
  },
  dek: {
    es: "Desde 2000, la economía de EE. UU. ha crecido un 69 % y la de la UE, un 41 %. Draghi calculó que cerrar la brecha exige entre 750.000 y 800.000 millones de euros más de inversión al año. Dos años después, se ha aplicado una cuarta parte de sus recomendaciones.",
    en: "Since 2000, the US economy has grown 69% and the EU's 41%. Draghi estimated that closing the gap requires an extra 750 to 800 billion euros of investment a year. Two years on, a quarter of his recommendations have been implemented.",
  },
  published: "2026-09-24",
  lens: "gigantes",
  theme: "productividad",
  body: [
    p("En septiembre de 2024, Mario Draghi, expresidente del Banco Central Europeo, entregó a la Comisión Europea un informe sobre el futuro de la competitividad europea. Su diagnóstico parte de un dato: desde principios de siglo, Europa crece menos que Estados Unidos. Entre 2000 y 2025, el PIB real de EE. UU. aumentó un 69 %; el de la UE, un 41 %. China, en el mismo periodo, lo multiplicó por 6,9.",
      "In September 2024, Mario Draghi, former president of the European Central Bank, handed the European Commission a report on the future of European competitiveness. His diagnosis starts from one fact: since the turn of the century, Europe has grown less than the United States. Between 2000 and 2025, US real GDP rose 69%; the EU's, 41%. China multiplied its GDP by 6.9 over the same period."),
    { fig: "n03-crecimiento", code: "1" },
    p("Su respuesta es invertir mucho más, y a la vez en tres frentes: innovación, descarbonización, y seguridad y defensa. Calculó que la UE necesita entre 750.000 y 800.000 millones de euros más al año, entre el 4,4 % y el 4,7 % del PIB, lo que llevaría la inversión del 22 % al 27 % del PIB. Hoy la UE invierte en proporción lo mismo que EE. UU., en torno al 21 % del PIB; China, casi el doble.",
      "His answer is to invest much more, on three fronts at once: innovation, decarbonisation, and security and defence. He estimated the EU needs an extra 750 to 800 billion euros a year, 4.4% to 4.7% of GDP, which would lift investment from 22% to 27% of GDP. Today the EU invests the same share as the US, around 21% of GDP; China, almost twice as much."),
    { fig: "n03-inversion", code: "2" },
    p("Dos años después, el seguimiento del JEDI Draghi Tracker, publicado el 10 de septiembre de 2026, calcula que se ha aplicado el 26 % de sus recomendaciones y que ninguna de las 30 clave se ha ejecutado por completo. El avance es desigual: un 35 % en energía y materias primas, un 13 % en salud. El informe sigue marcando la agenda europea, pero la inversión que pedía todavía no ha llegado.",
      "Two years on, the JEDI Draghi Tracker assessment published on 10 September 2026 finds that 26% of his recommendations have been implemented and that none of the 30 key ones has been fully executed. Progress is uneven: 35% in energy and raw materials, 13% in health. The report still sets the European agenda, but the investment it called for has not yet arrived."),
  ],
  sources: [
    { name: "Comisión Europea: el informe Draghi sobre la competitividad de la UE", url: "https://commission.europa.eu/topics/competitiveness/draghi-report_en" },
    { name: "Euronews (10/09/2026): EU falls short on Draghi reform agenda", url: "https://www.euronews.com/my-europe/2026/09/10/eu-falls-short-on-draghi-reform-agenda-new-report-shows" },
    { name: "JEDI Draghi Tracker", url: "https://draghitracker.org/" },
  ],
};

export default note;
