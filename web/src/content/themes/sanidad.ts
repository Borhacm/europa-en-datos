import { p, type Theme } from "../../lib/content-types";

const theme: Theme = {
  id: "sanidad",
  code: "SA",
  slug: { es: "sanidad", en: "health" },
  title: { es: "Sanidad", en: "Health" },
  status: "published",
  order: 5,
  published: "2026-09-25",
  dek: {
    es: "La UE gasta en sanidad mucho menos que EE. UU. y se vive más años. La paga sobre todo con dinero público, pero cada país reparte de forma distinta los médicos y lo que sale del bolsillo del paciente.",
    en: "The EU spends far less on health than the US, and people live longer. Most of it is paid with public money, but each country differs in how many doctors it has and how much patients pay themselves.",
  },
  lenses: {
    gigantes: {
      lede: { es: "EE. UU. gasta en sanidad mucho más que nadie. La UE gasta menos y vive más.", en: "The US spends far more on health than anyone else. The EU spends less and lives longer." },
      body: [
        p("En 2023, EE. UU. dedicó a la sanidad el 16,7 % de su PIB; la UE, el 10 %, y China, el 5,9 %. En 2000 eran el 12,5 %, el 8,4 % y el 4,5 %. La pandemia elevó el gasto en 2020 y 2021, y después volvió a bajar.",
          "In 2023, the US spent 16.7% of its GDP on health; the EU, 10%, and China, 5.9%. In 2000 the figures were 12.5%, 8.4% and 4.5%. The pandemic pushed spending up in 2020 and 2021, and it fell back afterwards."),
        { fig: "sag1-gasto-pib", code: "G1" },
        p("Por habitante, la distancia es aún mayor. EE. UU. gastó 13.473 dólares por persona, 2,3 veces más que la UE (5.806), medidos en paridad de poder adquisitivo. China, 1.487. Y, sin embargo, en la UE se vive tres años más que en EE. UU.: 81,4 años frente a 78,4 en 2023, como se ve en el tema de libertades, bienestar y clima.",
          "Per person, the gap is even wider. The US spent $13,473 per person, 2.3 times as much as the EU ($5,806), measured at purchasing power parity. China spent $1,487. And yet people in the EU live three years longer than in the US: 81.4 years against 78.4 in 2023, as shown in the freedoms, well-being and climate theme."),
        { fig: "sag2-gasto-habitante", code: "G2" },
      ],
    },
    elige: {
      lede: { es: "Europa eligió una sanidad pagada sobre todo con dinero público. Eso no la hace gratis para el paciente.", en: "Europe chose healthcare paid mostly with public money. That does not make it free for patients." },
      body: [
        p("En la UE, el 74,4 % del gasto sanitario lo pagan las administraciones y la seguridad social. En EE. UU., el 54 %, y en China, el 57,1 %. La distancia se ha acortado: en 2000, el gasto público era el 44,4 % del total en EE. UU. y el 22 % en China, mientras que en la UE apenas ha cambiado (74,8 %).",
          "In the EU, government and social security pay 74.4% of health spending. In the US, 54%, and in China, 57.1%. The gap has narrowed: in 2000, public spending was 44.4% of the total in the US and 22% in China, while in the EU it has barely changed (74.8%)."),
        { fig: "sae1-gasto-publico", code: "E1" },
        p("Pero lo público no siempre libra al paciente de pagar. En 2023, los hogares de EE. UU. pagaron de su bolsillo el 10,9 % del gasto sanitario; los de la UE, el 14,9 %. Solo en Luxemburgo, Francia y Croacia la proporción era menor que en EE. UU. En Bulgaria, Letonia y Grecia supera el 34 %; en España, el 20,9 %. Es una proporción: como EE. UU. gasta mucho más, sus hogares pagan más dinero, 1.472 dólares por habitante frente a 898 en la UE. Malta y Bélgica superan a EE. UU. incluso en esa cifra.",
          "But public funding does not always spare patients from paying. In 2023, US households paid 10.9% of health spending out of pocket; EU households, 14.9%. Only in Luxembourg, France and Croatia was the share lower than in the US. In Bulgaria, Latvia and Greece it is above 34%; in Spain, 20.9%. This is a share: since the US spends so much more, its households pay more money, $1,472 per person against $898 in the EU. Malta and Belgium exceed the US even on that measure."),
        { fig: "sae2-pago-bolsillo", code: "E2" },
      ],
    },
    dentro: {
      lede: { es: "Detrás de la media europea hay sistemas muy distintos, en médicos y en quién se queda sin atención.", en: "Behind the European average lie very different systems, in doctors and in who goes without care." },
      body: [
        p("En 2024, Grecia, Italia y Austria tenían más de 560 médicos en ejercicio por cada 100.000 habitantes. Letonia y Bélgica, unos 340. España, con 464, está por encima de la mediana de los 27 (410). Las series no siempre son comparables en el tiempo, y por eso el gráfico muestra solo el último año.",
          "In 2024, Greece, Italy and Austria had more than 560 practising doctors per 100,000 people. Latvia and Belgium, about 340. Spain, with 464, is above the median of the 27 (410). The series are not always comparable over time, which is why the chart shows only the latest year."),
        { fig: "sad1-medicos", code: "D1" },
        p("El número de médicos no lo explica todo. En 2025, el 2,4 % de los europeos de 16 años o más dijo haberse quedado sin un examen o tratamiento que necesitaba por el precio, la distancia o la lista de espera. En Grecia, que encabeza la lista de médicos, fue el 11,5 %, sobre todo por el precio (8,8 %). En Finlandia (7,8 %) y Estonia (7,7 %), sobre todo por las listas de espera. Desde 2023, en el conjunto de la UE las listas de espera pesan más que el precio. En España, el 1,6 %, casi todo por esperas, que han pasado del 0,4 % en 2015 al 1,5 %.",
          "The number of doctors does not tell the whole story. In 2025, 2.4% of Europeans aged 16 and over said they had gone without an examination or treatment they needed because of cost, distance or a waiting list. In Greece, which tops the ranking for doctors, it was 11.5%, mainly because of cost (8.8%). In Finland (7.8%) and Estonia (7.7%), mainly because of waiting lists. Since 2023, waiting lists have weighed more than cost across the EU as a whole. In Spain, 1.6%, almost all because of waiting, up from 0.4% in 2015 to 1.5%."),
        { fig: "sad2-necesidades-no-cubiertas", code: "D2" },
      ],
    },
  },
};

export default theme;
