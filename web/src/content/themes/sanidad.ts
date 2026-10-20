import { p, type Theme } from "../../lib/content-types";

// Rehecho el 20/10/2026 (ver editorial/registro/sanidad.md): guion, dos gráficos explicativos nuevos (SA-G3 y SA-E3),
// ficha de la Directiva 2011/24/UE, párrafo de límites y enlace a Libertades en lugar de repetir la esperanza de vida.
// Cifras comprobadas contra data/charts/sa*.json y las fuentes de `sources`.
const theme: Theme = {
  id: "sanidad",
  code: "SA",
  slug: { es: "sanidad", en: "health" },
  title: { es: "Sanidad", en: "Health" },
  status: "published",
  order: 5,
  published: "2026-09-25",
  updated: "2026-10-20",
  dek: {
    es: "EE. UU. gasta en sanidad más del doble por habitante que la UE, sobre todo en atención curativa, y aun así tiene más muertes por causas tratables que la mayoría de los países europeos. Dentro de la UE, lo que más separa a unos países de otros es quién se queda sin atención y por qué.",
    en: "The US spends more than twice as much per person on health as the EU, mostly on curative care, and still has more deaths from treatable causes than most European countries. Within the EU, what most separates countries is who goes without care and why.",
  },
  lenses: {
    gigantes: {
      lede: { es: "EE. UU. gasta en sanidad mucho más que nadie. La UE gasta menos y vive más.", en: "The US spends far more on health than anyone else. The EU spends less and lives longer." },
      body: [
        p("En 2023, EE. UU. dedicó a la sanidad el 16,7 % de su PIB; la UE, el 10 %, y China, el 5,9 %. En 2000 eran el 12,5 %, el 8,4 % y el 4,5 %. La pandemia elevó el gasto en 2020 y 2021, y después volvió a bajar.",
          "In 2023, the US spent 16.7% of its GDP on health; the EU, 10%, and China, 5.9%. In 2000 the figures were 12.5%, 8.4% and 4.5%. The pandemic pushed spending up in 2020 and 2021, and it fell back afterwards."),
        { fig: "sag1-gasto-pib", code: "G1" },
        p("Por habitante, la distancia es aún mayor. En 2023, EE. UU. gastó 13.473 dólares por persona, 2,3 veces más que la UE (5.806), medidos en paridad de poder adquisitivo. China, 1.487. En 2000, EE. UU. gastaba 4.549 dólares por persona y la UE, 1.814.",
          "Per person, the gap is even wider. In 2023, the US spent $13,473 per person, 2.3 times as much as the EU ($5,806), measured at purchasing power parity. China spent $1,487. In 2000, the US spent $4,549 per person and the EU $1,814."),
        { fig: "sag2-gasto-habitante", code: "G2" },
        { see: { es: "Libertades, bienestar y clima: cuánto se vive en la UE, EE. UU. y China", en: "Freedoms, well-being and climate: how long people live in the EU, the US and China" }, href: { es: "/es/libertades/", en: "/en/freedoms/" } },
        p("¿En qué se va la diferencia? Las cuentas de salud de la OCDE separan el gasto por destino. En 2023, EE. UU. gastó 13.933 dólares por habitante y la UE, de media, 6.138 en las mismas partidas. De los 7.795 dólares de diferencia, 5.765, tres de cada cuatro, corresponden a la atención curativa y la rehabilitación: consultas, hospitales y pruebas. La administración del sistema y de los seguros suma otros 886: EE. UU. gasta en ella 1.102 dólares por habitante, cinco veces más que la UE (216). Los medicamentos, 793. En cuidados de larga duración, los dos gastan casi lo mismo.",
          "Where does the difference go? The OECD health accounts split spending by function. In 2023, the US spent $13,933 per person and the EU, on average, $6,138 on the same items. Of the $7,795 difference, $5,765, three in every four, goes on curative and rehabilitative care: consultations, hospitals and tests. Administration of the system and of insurance adds another $886: the US spends $1,102 per person on it, five times as much as the EU ($216). Medicines, $793. On long-term care, both spend almost the same."),
        { fig: "sag3-gasto-funciones", code: "G3" },
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
        p("Gastar más no garantiza mejores resultados. En 2022, en EE. UU. murieron antes de los 75 años por causas tratables, que una atención a tiempo y eficaz podría haber evitado, 95 personas por cada 100.000 habitantes, en tasa ajustada por edad. En 16 de los 24 países de la UE con datos murieron menos: 45 en Luxemburgo; 48 en Francia, Países Bajos y Suecia; 51 en España. Los ocho con tasas más altas son todos del este, con Rumanía (179) a la cabeza. En las muertes prevenibles, las que se evitan con prevención y salud pública, EE. UU. (217) supera a 18 de los 24.",
          "Spending more does not guarantee better results. In 2022, 95 people per 100,000 died before age 75 in the US from treatable causes, which timely and effective care could have avoided, in age-adjusted terms. Fewer died in 16 of the 24 EU countries with data: 45 in Luxembourg; 48 in France, the Netherlands and Sweden; 51 in Spain. The eight with higher rates are all in the east, led by Romania (179). On preventable deaths, those avoided through prevention and public health, the US (217) exceeds 18 of the 24."),
        { fig: "sae3-mortalidad-evitable", code: "E3" },
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
        { h: { es: "La ficha: atenderse en otro país de la UE", en: "The policy card: getting treatment in another EU country" }, id: "ficha-asistencia-transfronteriza" },
        p("Cada país sigue siendo responsable de su sanidad, pero la Directiva 2011/24/UE, de 9 de marzo de 2011, da a los pacientes un derecho que conecta con las listas de espera de D2: recibir en otro país de la UE un tratamiento que su sistema cubre y que este se lo reembolse, hasta lo que habría costado en casa y sin superar el coste real. Para tratamientos que exigen pasar al menos una noche en el hospital o equipos muy especializados y caros, el país puede pedir una autorización previa, pero no puede negarla si no es capaz de dar ese tratamiento en un plazo médicamente justificado. Cada país debe tener puntos nacionales de contacto que informen a los pacientes. La propia directiva advierte de que no debe servir para animar a los pacientes a tratarse fuera.",
          "Each country remains responsible for its healthcare, but Directive 2011/24/EU of 9 March 2011 gives patients a right linked to the waiting lists in D2: to receive in another EU country a treatment their system covers and have it reimbursed, up to what it would have cost at home and not above the actual cost. For treatments requiring at least one night in hospital or highly specialised and costly equipment, a country may require prior authorisation, but it cannot refuse it if it cannot provide the treatment within a medically justifiable time. Each country must have national contact points to inform patients. The directive itself warns that it should not be used to encourage patients to seek treatment abroad."),
        p("Lo que no dicen estos datos. Las cifras de gasto de G1 y G2 son de la Organización Mundial de la Salud y las de G3, de la OCDE, que las calcula de otra forma; por eso no coinciden del todo. Ninguno de estos gráficos separa precios de cantidades: no dice si EE. UU. gasta más porque paga más caro cada servicio o porque usa más. La mortalidad evitable depende también de la renta, la dieta, el tabaco o la violencia, no solo de los hospitales. Las necesidades no cubiertas de D2 son lo que declaran los encuestados. Y no hay datos de cuántos pacientes usan la directiva de asistencia transfronteriza.",
          "What these data do not say. The spending figures in G1 and G2 come from the World Health Organization and those in G3 from the OECD, which computes them differently, so they do not fully match. None of these charts separates prices from quantities: they do not say whether the US spends more because it pays more for each service or because it uses more. Avoidable mortality also depends on income, diet, tobacco or violence, not only on hospitals. The unmet needs in D2 are what respondents report. And there are no data here on how many patients use the cross-border healthcare directive."),
      ],
    },
  },
  sources: [
    { name: "EUR-Lex: Directiva 2011/24/UE, relativa a la aplicación de los derechos de los pacientes en la asistencia sanitaria transfronteriza", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32011L0024" },
    { name: "OCDE, System of Health Accounts: gasto sanitario por función", url: "https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_SHA%40DF_SHA&df[ag]=OECD.ELS.HD" },
    { name: "OCDE, Health Status: mortalidad evitable (tratable y prevenible)", url: "https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_HEALTH_STAT%40DF_AM&df[ag]=OECD.ELS.HD" },
  ],
};

export default theme;
