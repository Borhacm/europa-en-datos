import { p, type Note } from "../../lib/content-types";

// Cifras de los gráficos comprobadas contra data/charts/n02-*.json (Eurostat, encuestas de 2023 y 2025).
// Fechas del AI Act comprobadas en EUR-Lex y en análisis jurídicos (ver sources).
const note: Note = {
  id: "n02",
  code: "N02",
  slug: { es: "ai-act", en: "ai-act" },
  title: {
    es: "El AI Act y las empresas: la incertidumbre legal ya es el segundo freno a la IA",
    en: "The AI Act and business: legal uncertainty is now the second barrier to AI",
  },
  dek: {
    es: "Europa eligió ser la primera en regular la inteligencia artificial. Entre las empresas que se plantean usarla y no lo hacen, el 54 % señala ya que no tiene claras las consecuencias legales, frente al 46 % de 2023.",
    en: "Europe chose to be first to regulate artificial intelligence. Among companies that consider using it but do not, 54% now say the legal consequences are unclear, up from 46% in 2023.",
  },
  published: "2026-09-24",
  lens: "elige",
  theme: "ia-digital",
  body: [
    p("El AI Act es la primera ley general sobre inteligencia artificial del mundo. Entró en vigor el 1 de agosto de 2024 y se aplica por fases: las prácticas prohibidas, desde febrero de 2025, y las obligaciones de los grandes modelos de propósito general, desde agosto de 2025. Las obligaciones para los sistemas de alto riesgo se han aplazado: un reglamento en vigor desde el 27 de julio de 2026 las retrasa de agosto de 2026 a diciembre de 2027 y, para la IA integrada en productos regulados, de agosto de 2027 a agosto de 2028, porque las normas técnicas y las autoridades nacionales no estaban listas.",
      "The AI Act is the world's first general law on artificial intelligence. It entered into force on 1 August 2024 and applies in stages: prohibited practices since February 2025, and obligations for large general-purpose models since August 2025. The obligations for high-risk systems have been postponed: a regulation in force since 27 July 2026 moves them from August 2026 to December 2027 and, for AI built into regulated products, from August 2027 to August 2028, because technical standards and national authorities were not ready."),
    p("¿Frena la regulación a las empresas? Eurostat pregunta a las que se plantearon usar IA y no lo hicieron por qué. El primer motivo sigue siendo la falta de conocimientos (70 %). Pero la falta de claridad sobre las consecuencias legales ha pasado del 46 % al 54 % en dos años y ya es el segundo, casi empatado con la protección de datos (53 %).",
      "Is regulation holding companies back? Eurostat asks those that considered using AI but did not why. Lack of expertise is still the main reason (70%). But unclear legal consequences have risen from 46% to 54% in two years and are now the second reason, almost level with data protection (53%)."),
    { fig: "n02-ia-frenos", code: "1" },
    p("La subida es general: la incertidumbre legal pesa más que en 2023 en 17 de los 18 países con datos de ambos años. En España llega al 51 %, y en Alemania, que no tiene dato de 2023, al 62 %. La encuesta no distingue entre leyes, así que no todo es atribuible al AI Act: también cuentan el reglamento de protección de datos y la propiedad intelectual. Pero el aplazamiento de 2026 reconoce el problema: cumplir la ley sin normas técnicas terminadas era difícil.",
      "The rise is widespread: legal uncertainty weighs more than in 2023 in 17 of the 18 countries with data for both years. In Spain it reaches 51%, and in Germany, which has no 2023 figure, 62%. The survey does not distinguish between laws, so not all of it can be attributed to the AI Act: data protection rules and intellectual property also count. But the 2026 postponement acknowledges the problem: complying with the law without finished technical standards was hard."),
    { fig: "n02-ia-incertidumbre-legal", code: "2" },
  ],
  sources: [
    { name: "EUR-Lex: Reglamento (UE) 2024/1689 (AI Act)", url: "https://eur-lex.europa.eu/eli/reg/2024/1689/oj" },
    { name: "EUR-Lex: Reglamento (UE) 2026/1744 (Digital Omnibus on AI)", url: "https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng" },
    { name: "Gibson Dunn: EU AI Act Omnibus Agreement, postponed high-risk deadlines", url: "https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/" },
  ],
};

export default note;
