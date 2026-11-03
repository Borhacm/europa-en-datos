import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n11-*.json (Eurostat ilc_mdes01, 2021 y 2025). Ver editorial/registro/n11.md.
const note: Note = {
  id: "n11",
  code: "N11",
  slug: { es: "no-poder-calentar-la-casa", en: "unable-to-keep-home-warm" },
  title: {
    es: "No poder calentar la casa es más frecuente que en 2021 en 19 de los 27 países",
    en: "Being unable to keep the home warm is more common than in 2021 in 19 of the 27 countries",
  },
  dek: {
    es: "En 2025, el 8,8 % de los residentes en la UE no podía permitirse mantener su casa a una temperatura adecuada, frente al 6,9 % de 2021. Ha subido sobre todo en Francia y los Países Bajos, y ha bajado en Chipre, Bulgaria y Lituania.",
    en: "In 2025, 8.8% of EU residents could not afford to keep their home adequately warm, against 6.9% in 2021. It has risen most in France and the Netherlands, and fallen in Cyprus, Bulgaria and Lithuania.",
  },
  published: "2026-11-03",
  updated: "2026-11-03",
  lens: "dentro",
  theme: "energia",
  body: [
    p("La encuesta de condiciones de vida de Eurostat pregunta a cada hogar si puede permitirse mantener su casa a una temperatura adecuada. En 2021, el 6,9 % de los residentes en la UE respondía que no. En 2025 eran el 8,8 %. En ese tiempo subió también el precio de la luz para los hogares, como cuenta la nota sobre la factura eléctrica.",
      "Eurostat's survey on living conditions asks each household whether it can afford to keep its home adequately warm. In 2021, 6.9% of EU residents said no. In 2025 it was 8.8%. Household electricity prices also rose over that period, as the note on electricity bills shows."),
    p("Entre 2021 y 2025, la proporción ha subido en 19 países, ha bajado en 7 y no ha cambiado en Polonia. Las mayores subidas son las de Francia, del 6 % al 11,5 %, aunque parte puede deberse a un cambio en su encuesta; los Países Bajos, del 2,4 % al 6,6 %, y Suecia, del 1,7 % al 4,7 %. Las mayores bajadas, las de Chipre (del 19,2 % al 11,3 %), Bulgaria (del 23,7 % al 16,1 %) y Lituania (del 22,5 % al 16,7 %). En 2025, las proporciones más altas son las de Grecia (18,1 %), Lituania, Bulgaria y España (15,9 %); las más bajas, las de Finlandia (2,6 %) y Estonia (3,1 %).",
      "Between 2021 and 2025, the share rose in 19 countries, fell in 7 and did not change in Poland. The largest increases were in France, from 6% to 11.5%, although part of this may be due to a change in its survey; the Netherlands, from 2.4% to 6.6%, and Sweden, from 1.7% to 4.7%. The largest falls were in Cyprus (from 19.2% to 11.3%), Bulgaria (from 23.7% to 16.1%) and Lithuania (from 22.5% to 16.7%). In 2025, the highest shares are in Greece (18.1%), Lithuania, Bulgaria and Spain (15.9%); the lowest, in Finland (2.6%) and Estonia (3.1%)."),
    { fig: "n11-frio-cambio", code: "1" },
    p("La renta pesa mucho. En la UE, el 19,6 % de las personas en riesgo de pobreza no puede calentar su casa, casi el triple que el resto (6,7 %). En Grecia son el 36,1 %; en Chipre, el 34,6 %, y en Bulgaria, el 33,1 %. En España, el 28,3 %, frente al 12,9 % de quienes están por encima del umbral.",
      "Income matters a great deal. In the EU, 19.6% of people at risk of poverty cannot keep their home warm, almost three times the rate for everyone else (6.7%). In Greece it is 36.1%; in Cyprus, 34.6%, and in Bulgaria, 33.1%. In Spain, 28.3%, against 12.9% of those above the threshold."),
    { fig: "n11-frio-pobreza", code: "2" },
    p("Lo que no dicen estos datos. Es lo que declaran los hogares, no una medida de la temperatura de las casas ni de lo que gastan en energía, y lo que cada uno considera adecuado cambia con el clima y la vivienda. Tampoco permiten atribuir los cambios a los precios de la energía ni a las ayudas que cada Gobierno dio en la crisis.",
      "What these data do not say. This is what households report, not a measure of how warm homes are or of what they spend on energy, and what each considers adequate varies with climate and housing. Nor do they allow changes to be attributed to energy prices or to the support each government gave during the crisis."),
    { see: { es: "Nota: cuánto pagan por la luz los hogares de cada país", en: "Note: what households pay for electricity in each country" }, href: { es: "/es/notas/precio-luz-hogares/", en: "/en/notes/household-electricity-prices/" } },
    { see: { es: "Energía: de dónde sale la electricidad y cuánto cuesta en cada país", en: "Energy: where electricity comes from and what it costs in each country" }, href: { es: "/es/energia/", en: "/en/energy/" } },
  ],
  sources: [
    { name: "Eurostat: imposibilidad de mantener la vivienda a una temperatura adecuada (ilc_mdes01)", url: "https://ec.europa.eu/eurostat/databrowser/view/ilc_mdes01/default/table" },
  ],
};

export default note;
