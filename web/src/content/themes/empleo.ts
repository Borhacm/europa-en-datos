import { p, type Theme } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/em*.json (OIT y Eurostat, descargados el 25 de octubre de 2026). Ver editorial/registro/empleo.md.
// Ficha: objetivos para 2030 del Plan de Acción del Pilar Europeo de Derechos Sociales, cotejados en la web de la Comisión Europea.
// Ninis: Eurostat edat_lfse_20 (15 a 29 años, 2015 y 2025).
const theme: Theme = {
  id: "empleo",
  code: "EM",
  slug: { es: "empleo", en: "jobs" },
  title: { es: "Empleo y jóvenes", en: "Jobs and young people" },
  status: "published",
  order: 12,
  published: "2026-10-25",
  dek: {
    es: "En la UE trabaja más gente de 25 a 54 años que en EE. UU., pero muchos menos jóvenes, y el paro juvenil sigue siendo alto: el 14,9 %, frente al 8,9 % estadounidense. Dentro de la Unión, las diferencias son enormes: en Rumanía y España, uno de cada cuatro jóvenes activos está en paro, y en Croacia, Grecia o España se van de casa pasados los 30.",
    en: "More people aged 25 to 54 work in the EU than in the US, but far fewer young people, and youth unemployment remains high: 14.9%, against 8.9% in the US. Within the Union, the differences are huge: in Romania and Spain, one in four young people in the labour force is unemployed, and in Croatia, Greece or Spain they leave home after 30.",
  },
  lenses: {
    gigantes: {
      lede: {
        es: "La diferencia de empleo con EE. UU. está en los jóvenes. China, que tenía muy poco paro juvenil, ya ha alcanzado a la UE.",
        en: "The employment gap with the US is among the young. China, which had very little youth unemployment, has now caught up with the EU.",
      },
      body: [
        p(
          "El paro de los jóvenes europeos ha bajado mucho desde la crisis del euro: en 2013 llegó al 24,3 %, según las estimaciones de la OIT, y en 2024 era del 14,9 %. Aun así, sigue por encima del de EE. UU. (8,9 %), donde también se disparó en 2020 y bajó deprisa. En China ha pasado lo contrario: en 2000, el 6,8 % de los jóvenes activos estaba en paro; en 2024, el 15 %, prácticamente lo mismo que en la UE.",
          "Youth unemployment in Europe has fallen a long way since the euro crisis: it reached 24.3% in 2013, according to ILO estimates, and stood at 14.9% in 2024. Even so, it remains above the US rate (8.9%), which also soared in 2020 and fell quickly. China has gone the other way: in 2000, 6.8% of young people in the labour force were unemployed; in 2024, 15%, practically the same as in the EU.",
        ),
        { fig: "emg1-paro-juvenil", code: "G1" },
        p(
          "En conjunto, en la UE ya trabaja la misma parte de la población que en EE. UU., como se ve en el tema de productividad. Pero no en todas las edades. Entre los 25 y los 54 años, la tasa de empleo europea es más alta (82,4 % frente a 80,7 %), y entre los 55 y los 64 también (65,2 % frente a 64,1 %). La diferencia está en los jóvenes: en la UE trabaja el 34,9 % de quienes tienen entre 15 y 24 años; en EE. UU., el 50,9 %. Parte de esa diferencia depende de cuántos jóvenes estudian sin trabajar a la vez, algo que estos datos no separan.",
          "Overall, the EU now has the same share of its population in work as the US, as the productivity topic shows. But not at every age. Between 25 and 54, the European employment rate is higher (82.4% against 80.7%), and between 55 and 64 too (65.2% against 64.1%). The gap is among the young: in the EU, 34.9% of those aged 15 to 24 work; in the US, 50.9%. Part of that gap depends on how many young people study without working at the same time, which these data do not separate.",
        ),
        { fig: "emg2-empleo-edades", code: "G2" },
        { see: { es: "Productividad y crecimiento: empleo y horas trabajadas frente a EE. UU.", en: "Productivity and growth: employment and hours worked compared with the US" }, href: { es: "/es/productividad/", en: "/en/productivity/" } },
      ],
    },
    elige: {
      lede: {
        es: "La UE se ha fijado un objetivo de empleo para 2030 que ya cumplen 16 países. Y en buena parte de Europa, el contrato temporal no se elige.",
        en: "The EU has set itself a 2030 employment target that 16 countries already meet. And in much of Europe, a temporary contract is not a choice.",
      },
      body: [
        p(
          "En 2025, el 76,1 % de los europeos de 20 a 64 años tenía empleo, a dos puntos del objetivo del 78 % para 2030. Dieciséis países ya lo superan, con Malta (83,6 %) y los Países Bajos (83,4 %) a la cabeza. Los más lejos son Italia (67,6 %), Rumanía (69 %), Grecia (71 %) y España (72,4 %).",
          "In 2025, 76.1% of Europeans aged 20 to 64 were in work, two points short of the 78% target for 2030. Sixteen countries already exceed it, led by Malta (83.6%) and the Netherlands (83.4%). The furthest away are Italy (67.6%), Romania (69%), Greece (71%) and Spain (72.4%).",
        ),
        { fig: "eme1-objetivo-empleo", code: "E1" },
        { h: { es: "La ficha: el objetivo de empleo del Pilar Europeo de Derechos Sociales", en: "The policy card: the employment target of the European Pillar of Social Rights" }, id: "ficha-pilar-social" },
        { steps: [
          { title: { es: "Qué es.", en: "What it is." },
            text: { es: "El Plan de Acción del Pilar Europeo de Derechos Sociales fija tres objetivos comunes para 2030. El primero es de empleo: que trabaje al menos el 78 % de la población de 20 a 64 años. Los otros dos son de formación de adultos y de reducción de la pobreza.",
                    en: "The European Pillar of Social Rights Action Plan sets three common goals for 2030. The first is on employment: at least 78% of people aged 20 to 64 should be in work. The other two cover adult training and poverty reduction." } },
          { title: { es: "Quién y cuándo.", en: "Who and when." },
            text: { es: "Lo propuso la Comisión Europea en 2021. En la Cumbre Social de Oporto, en mayo de 2021, los líderes de la UE, las instituciones, los interlocutores sociales y la sociedad civil se comprometieron con los tres objetivos.",
                    en: "The European Commission proposed it in 2021. At the Porto Social Summit in May 2021, EU leaders, institutions, social partners and civil society committed to the three targets." } },
          { title: { es: "Qué debería pasar.", en: "What should happen." },
            text: { es: "Que la tasa de empleo de la UE llegue al 78 % en 2030. Cada país fijó su propio objetivo nacional para contribuir al común.",
                    en: "The EU employment rate should reach 78% by 2030. Each country set its own national target to contribute to the common one." } },
          { title: { es: "Con qué lo comparamos.", en: "What we compare it with." },
            text: { es: "Con la tasa de empleo de 20 a 64 años de cada país en 2025 (gráfico E1). Es un objetivo político, no una obligación legal: no hay sanción para quien no lo cumpla.",
                    en: "With each country's employment rate for ages 20 to 64 in 2025 (chart E1). It is a political target, not a legal obligation: there is no penalty for missing it." } },
        ] },
        p(
          "El objetivo cuenta cuánta gente trabaja, no con qué contrato. En la UE, el 12,7 % de los asalariados de 15 a 64 años tiene un contrato temporal; en los Países Bajos, el 25,8 %, y en España, el 15,1 %. Los motivos cambian mucho de un país a otro. En el conjunto de la UE, la mitad de los temporales dice que lo es porque no encontró un empleo fijo (26,6 %) o porque el puesto solo se ofrecía con contrato temporal (23,3 %). En España, esos dos motivos suman el 76,4 %, y en Italia, el 82,9 %. En Alemania, en cambio, el 39,9 % de los temporales se está formando (una categoría que incluye los contratos de aprendizaje), y en los Países Bajos, el 58,1 % está en periodo de prueba.",
          "The target counts how many people work, not on what contract. In the EU, 12.7% of employees aged 15 to 64 are on a temporary contract; in the Netherlands 25.8%, and in Spain 15.1%. The reasons vary widely from country to country. Across the EU, half of temporary employees say they are temporary because they could not find a permanent job (26.6%) or because the job was only offered on a temporary contract (23.3%). In Spain those two reasons add up to 76.4%, and in Italy 82.9%. In Germany, by contrast, 39.9% of temporary employees are in training (a category that includes apprenticeship contracts), and in the Netherlands 58.1% are on probation.",
        ),
        { fig: "eme2-motivos-temporales", code: "E2" },
      ],
    },
    dentro: {
      lede: {
        es: "En Alemania, el 7,1 % de los jóvenes activos está en paro; en Rumanía y España, uno de cada cuatro. Y la edad a la que se van de casa casi no ha cambiado en diez años.",
        en: "In Germany, 7.1% of young people in the labour force are unemployed; in Romania and Spain, one in four. And the age at which they leave home has barely changed in ten years.",
      },
      body: [
        p(
          "En 2025, la tasa de paro de los jóvenes de 15 a 24 años fue del 15,2 % en la UE, según Eurostat. En Rumanía llegó al 26,1 % y en España, al 24,9 %; en Alemania se quedó en el 7,1 % y en los Países Bajos, en el 8,8 %. La tasa solo cuenta a los jóvenes que trabajan o buscan empleo, así que no siempre mide lo mismo: sube donde muchos estudiantes buscan trabajo a la vez, y baja donde los aprendices, que cuentan como ocupados, son muchos.",
          "In 2025, the unemployment rate for young people aged 15 to 24 was 15.2% in the EU, according to Eurostat. In Romania it reached 26.1% and in Spain 24.9%; in Germany it stood at 7.1% and in the Netherlands at 8.8%. The rate only counts young people who work or look for work, so it does not always measure the same thing: it rises where many students look for work at the same time, and falls where apprentices, who count as employed, are numerous.",
        ),
        { fig: "emd1-paro-juvenil-paises", code: "D1" },
        p(
          "Una medida que no depende de quién busca empleo es la de los jóvenes que ni estudian ni trabajan. En 2025 eran el 11 % de los europeos de 15 a 29 años, frente al 15,2 % en 2015. En España han bajado del 19,4 % al 11,5 %. El máximo está en Rumanía (19,2 %) y el mínimo, en los Países Bajos (5,3 %).",
          "A measure that does not depend on who is looking for work is the share of young people neither in employment nor in education or training. In 2025 they were 11% of Europeans aged 15 to 29, against 15.2% in 2015. In Spain the share has fallen from 19.4% to 11.5%. The highest is in Romania (19.2%) and the lowest in the Netherlands (5.3%).",
        ),
        p(
          "Irse de casa es otra cosa. En la UE, los jóvenes dejan el hogar de sus padres de media a los 26,3 años, casi lo mismo que en 2015 (26,4). Pero en Croacia lo hacen a los 31,5; en Grecia y Eslovaquia, a los 30,9, y en España e Italia, a los 30,2. En Finlandia, a los 21,3, y en Dinamarca, a los 21,8. En España, la edad ha subido más de un año desde 2015.",
          "Leaving home is a different matter. In the EU, young people leave their parents' home at 26.3 on average, almost the same as in 2015 (26.4). But in Croatia they do so at 31.5; in Greece and Slovakia at 30.9, and in Spain and Italy at 30.2. In Finland at 21.3, and in Denmark at 21.8. In Spain, the age has risen by more than a year since 2015.",
        ),
        { fig: "emd2-edad-emancipacion", code: "D2" },
        p(
          "Lo que no dicen estos datos. Las tasas de paro juvenil se calculan sobre los jóvenes activos, que son una parte distinta de cada generación en cada país: comparar países con muchos estudiantes que trabajan y países donde casi nadie lo hace exige cuidado. El paro de EE. UU. y China viene de estimaciones de la OIT que armonizan encuestas distintas, y las cifras oficiales de China no son del todo comparables con las europeas. Los motivos de los contratos temporales los declara el propio trabajador. Y la edad de emancipación depende de muchas cosas a la vez, del precio de la vivienda a la tradición familiar o la duración de los estudios: estos datos no permiten separarlas.",
          "What these data do not say. Youth unemployment rates are calculated over young people in the labour force, who are a different share of each generation in each country: comparing countries where many students work with countries where almost none do calls for care. US and Chinese unemployment comes from ILO estimates that harmonise different surveys, and China's official figures are not fully comparable with European ones. The reasons for temporary contracts are reported by the workers themselves. And the age of leaving home depends on many things at once, from house prices to family tradition or the length of studies: these data cannot separate them.",
        ),
        { see: { es: "Vivienda y coste de vida: precios, alquileres y sobrecarga", en: "Housing and the cost of living: prices, rents and overburden" }, href: { es: "/es/vivienda/", en: "/en/housing/" } },
      ],
    },
  },
  sources: [
    { name: "Comisión Europea: Plan de Acción del Pilar Europeo de Derechos Sociales y objetivos para 2030", url: "https://ec.europa.eu/social/main.jsp?catId=1607&langId=es" },
    { name: "Eurostat: jóvenes que ni estudian ni trabajan, de 15 a 29 años (edat_lfse_20)", url: "https://ec.europa.eu/eurostat/databrowser/view/edat_lfse_20/default/table" },
  ],
};

export default theme;
