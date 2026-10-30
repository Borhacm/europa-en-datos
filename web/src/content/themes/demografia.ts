import { p, type Theme } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/dm*.json (Banco Mundial y Eurostat, descargados el 30 de octubre de 2026). Ver editorial/registro/demografia.md.
// Ficha: Pacto sobre Migración y Asilo, cotejado en la web de la Comisión Europea (DG Migración y Asuntos de Interior).
// Asilo: Eurostat migr_asyappctza (solicitantes por primera vez, 2025). Protección temporal: Eurostat migr_asytpsm (diciembre de 2025).
const theme: Theme = {
  id: "demografia",
  code: "DM",
  slug: { es: "demografia", en: "population" },
  title: { es: "Demografía y migración", en: "Population and migration" },
  status: "published",
  order: 13,
  published: "2026-10-30",
  dek: {
    es: "La UE es el más envejecido de los tres bloques: el 22 % de su población tiene 65 años o más. Desde 2012 mueren más europeos de los que nacen, y la población solo crece por la migración. Quien llega lo hace sobre todo por trabajo o por familia, y el peso de los nacidos fuera de la UE va del 1,1 % de Eslovaquia al 24,6 % de Malta.",
    en: "The EU is the oldest of the three blocs: 22% of its population is 65 or older. Since 2012, more Europeans have died than have been born, and the population only grows through migration. Newcomers arrive mainly for work or family, and the share born outside the EU ranges from 1.1% in Slovakia to 24.6% in Malta.",
  },
  lenses: {
    gigantes: {
      lede: {
        es: "La UE tiene más mayores que EE. UU. y China. China envejece más deprisa, y sus mujeres ya tienen menos hijos que las europeas.",
        en: "The EU has more older people than the US and China. China is ageing faster, and its women now have fewer children than European women.",
      },
      body: [
        p(
          "En 2024, el 22 % de la población de la UE tenía 65 años o más, frente al 15,7 % en 2000. En EE. UU., la proporción ha pasado del 12,2 % al 17,9 %. China partía de mucho más abajo, el 7 %, pero es la que más ha subido: 7,7 puntos, hasta el 14,7 %. Más mayores significa más gasto en pensiones y en sanidad, que se ve en el tema de finanzas públicas.",
          "In 2024, 22% of the EU population was 65 or older, up from 15.7% in 2000. In the US, the share has gone from 12.2% to 17.9%. China started much lower, at 7%, but has risen the most: 7.7 points, to 14.7%. More older people means more spending on pensions and health care, which the public finances topic covers.",
        ),
        { fig: "dmg1-mayores-bloques", code: "G1" },
        p(
          "El envejecimiento tiene dos causas: se vive más y nacen menos niños. En 2024, las mujeres de la UE tenían de media 1,34 hijos; en 2000, 1,44. En EE. UU., que en 2000 todavía superaba los 2 hijos por mujer, ha bajado a 1,63. En China, de 1,63 a 1,01: hasta 2017 estaba por encima de la europea y ahora es la más baja de los tres. Ninguno llega a los 2,1 hijos por mujer que mantienen una población estable sin migración.",
          "Ageing has two causes: people live longer and fewer children are born. In 2024, women in the EU had 1.34 children on average; in 2000, 1.44. In the US, where it was still above 2 births per woman in 2000, it has fallen to 1.63. In China, from 1.63 to 1.01: until 2017 it was above the European rate, and now it is the lowest of the three. None reaches the 2.1 births per woman that keep a population stable without migration.",
        ),
        { fig: "dmg2-fecundidad-bloques", code: "G2" },
        { see: { es: "Finanzas públicas: deuda, impuestos y en qué se gasta", en: "Public finances: debt, taxes and spending" }, href: { es: "/es/finanzas-publicas/", en: "/en/public-finances/" } },
      ],
    },
    elige: {
      lede: {
        es: "Sin migración, la población de la UE llevaría más de una década bajando. Quien llega de fuera viene sobre todo a trabajar o a reunirse con su familia, y desde junio de 2026 se aplican nuevas reglas de asilo.",
        en: "Without migration, the EU population would have been shrinking for more than a decade. Newcomers from outside come mainly to work or to join their families, and new asylum rules have applied since June 2026.",
      },
      body: [
        p(
          "La población cambia por dos vías: los nacimientos menos las defunciones, y los que llegan menos los que se van. En la UE, la primera es negativa todos los años desde 2012. En 2025 nacieron 3,46 millones de niños y murieron 4,81 millones de personas: 1,35 millones más. La población creció igualmente, en 705.756 personas, porque el saldo migratorio fue de 2,06 millones. Desde 2012, solo bajó en 2020, el año de la pandemia.",
          "Population changes in two ways: births minus deaths, and arrivals minus departures. In the EU, the first has been negative every year since 2012. In 2025, 3.46 million children were born and 4.81 million people died: 1.35 million more. The population still grew, by 705,756 people, because net migration was 2.06 million. Since 2012, it only fell in 2020, the year of the pandemic.",
        ),
        { fig: "dme1-crecimiento-ue", code: "E1" },
        p(
          "¿Por qué viene la gente de fuera? En 2025, los países de la UE dieron 3,86 millones de primeros permisos de residencia a ciudadanos de terceros países. El 33,6 % fue por trabajo; el 28,1 %, por familia; el 15,5 %, por estudios, y el 22,8 %, por otros motivos, entre ellos la protección internacional. Los países cambian mucho. En Croacia, el 93 % de los permisos es de trabajo, y en Rumanía, el 81,5 %. En España, el motivo más frecuente es la familia (43,4 %), como en Italia (40,8 %). En Irlanda, los estudios (47,6 %). Cómo les va a los jóvenes europeos en el mercado de trabajo se cuenta en el tema de empleo y jóvenes.",
          "Why do people come from outside? In 2025, EU countries issued 3.86 million first residence permits to non-EU citizens. 33.6% were for work, 28.1% for family, 15.5% for education and 22.8% for other reasons, including international protection. Countries differ a great deal. In Croatia, 93% of permits are for work, and in Romania 81.5%. In Spain, the most common reason is family (43.4%), as in Italy (40.8%). In Ireland, education (47.6%). The jobs and young people topic shows how young Europeans are faring in the labour market.",
        ),
        { fig: "dme2-permisos-motivo", code: "E2" },
        { see: { es: "Empleo y jóvenes: tasa de empleo, paro juvenil y emancipación", en: "Jobs and young people: employment, youth unemployment and leaving home" }, href: { es: "/es/empleo/", en: "/en/jobs/" } },
        { h: { es: "La ficha: el Pacto sobre Migración y Asilo", en: "The policy card: the Pact on Migration and Asylum" }, id: "ficha-pacto-migracion" },
        { steps: [
          { title: { es: "Qué es.", en: "What it is." },
            text: { es: "Un conjunto de diez actos legislativos que fija reglas comunes para el asilo y la gestión de la migración en la UE: control y registro en la frontera exterior, un procedimiento fronterizo obligatorio para algunos solicitantes de asilo, criterios para decidir qué país examina cada solicitud y un mecanismo de solidaridad entre países.",
                    en: "A set of ten legislative acts laying down common rules for asylum and migration management in the EU: screening and registration at the external border, a mandatory border procedure for some asylum seekers, criteria to decide which country examines each application and a solidarity mechanism between countries." } },
          { title: { es: "Quién y cuándo.", en: "Who and when." },
            text: { es: "Lo adoptaron el Parlamento Europeo y el Consejo en junio de 2024, según la Comisión Europea. Se aplica en toda la UE desde el 12 de junio de 2026.",
                    en: "The European Parliament and the Council adopted it in June 2024, according to the European Commission. It has applied across the EU since 12 June 2026." } },
          { title: { es: "Qué debería pasar.", en: "What should happen." },
            text: { es: "Que las solicitudes de asilo de nacionalidades con una tasa de reconocimiento baja (20 % o menos) se resuelvan en la frontera en un máximo de doce semanas, recurso incluido, y que los países que reciben más solicitantes no carguen solos con ellos: el reglamento fija un mínimo anual de 30.000 reubicaciones y 600 millones de euros en contribuciones financieras.",
                    en: "Asylum applications from nationalities with a low recognition rate (20% or less) should be decided at the border within twelve weeks, appeal included, and the countries receiving the most applicants should not bear them alone: the regulation sets an annual minimum of 30,000 relocations and 600 million euros in financial contributions." } },
          { title: { es: "Con qué lo comparamos.", en: "What we compare it with." },
            text: { es: "Con la escala del asilo frente al resto de la migración. En 2025 pidieron asilo por primera vez en la UE 671.895 personas, según Eurostat, frente a 3,86 millones de primeros permisos de residencia (gráfico E2). Las solicitudes de asilo, de las que se ocupa sobre todo el Pacto, equivalen a menos de una quinta parte de los permisos. Es pronto para medir sus efectos: lleva menos de cinco meses en vigor.",
                    en: "With the scale of asylum compared with other migration. In 2025, 671,895 people applied for asylum in the EU for the first time, according to Eurostat, against 3.86 million first residence permits (chart E2). Asylum applications, which are the Pact's main concern, are equivalent to less than a fifth of the permits. It is too early to measure its effects: it has been in force for less than five months." } },
        ] },
      ],
    },
    dentro: {
      lede: {
        es: "En casi todos los países de la UE, las mujeres tienen menos hijos que hace diez años. Y la parte de la población nacida fuera de la Unión va del 1,1 % al 24,6 %.",
        en: "In almost every EU country, women have fewer children than ten years ago. And the share of the population born outside the Union ranges from 1.1% to 24.6%.",
      },
      body: [
        p(
          "La fecundidad ha bajado entre 2014 y 2024 en 23 de los 27 países. Las mayores caídas son las de Finlandia, de 1,71 a 1,25 hijos por mujer; Lituania, de 1,57 a 1,11, y Suecia, de 1,88 a 1,43. Francia, que tenía 2 hijos por mujer, se ha quedado en 1,61, aunque sigue siendo la segunda más alta. España tiene la segunda más baja (1,1), solo por encima de Malta.",
          "Fertility fell between 2014 and 2024 in 23 of the 27 countries. The largest drops are in Finland, from 1.71 to 1.25 births per woman; Lithuania, from 1.57 to 1.11, and Sweden, from 1.88 to 1.43. France, which had 2 births per woman, is down to 1.61, although it is still the second highest. Spain has the second lowest (1.1), only above Malta.",
        ),
        { fig: "dmd1-fecundidad-paises", code: "D1" },
        p(
          "A 1 de enero de 2025, el 10,4 % de los residentes en la UE había nacido fuera de ella, frente al 8,5 % en 2021. Malta ha pasado del 15,6 % al 24,6 %, la mayor subida. En España, del 12 % al 16 %. En el este, la proporción sigue siendo pequeña: el 1,9 % en Polonia y el 1,1 % en Eslovaquia. En Polonia y Grecia no ha cambiado, y en Letonia ha bajado.",
          "On 1 January 2025, 10.4% of EU residents had been born outside it, against 8.5% in 2021. Malta has gone from 15.6% to 24.6%, the largest increase. In Spain, from 12% to 16%. In the east, the share remains small: 1.9% in Poland and 1.1% in Slovakia. In Poland and Greece it has not changed, and in Latvia it has fallen.",
        ),
        { fig: "dmd2-nacidos-fuera", code: "D2" },
        p(
          "Lo que no dicen estos datos. El saldo migratorio de Eurostat se calcula por diferencia y arrastra ajustes estadísticos, y las cifras de EE. UU. y China vienen de estimaciones de Naciones Unidas, no de registros comparables a los europeos. Los permisos de residencia cuentan papeles, no personas que se quedan, y los 4,35 millones de refugiados de Ucrania con protección temporal que había en la UE a finales de 2025 tienen su propia estadística. Que la migración compense la falta de nacimientos en el número de habitantes no dice si compensa el envejecimiento: eso depende de la edad de quien llega, de si encuentra empleo y de si se queda. Y estos datos no permiten atribuir los cambios de fecundidad a ninguna política concreta.",
          "What these data do not say. Eurostat's net migration is calculated as a residual and carries statistical adjustments, and the US and Chinese figures come from United Nations estimates, not from records comparable to Europe's. Residence permits count papers, not people who stay, and the 4.35 million refugees from Ukraine under temporary protection in the EU at the end of 2025 are counted in separate statistics. That migration offsets the lack of births in headcount does not say whether it offsets ageing: that depends on the age of newcomers, on whether they find work and on whether they stay. And these data do not allow fertility changes to be attributed to any specific policy.",
        ),
      ],
    },
  },
  sources: [
    { name: "Comisión Europea: Pacto sobre Migración y Asilo", url: "https://home-affairs.ec.europa.eu/policies/migration-and-asylum/pact-migration-and-asylum_en" },
    { name: "Comisión Europea: preguntas y respuestas sobre el Pacto sobre Migración y Asilo (12/06/2026)", url: "https://home-affairs.ec.europa.eu/policies/migration-and-asylum/pact-migration-and-asylum/questions-and-answers-pact-migration-and-asylum_en" },
    { name: "Eurostat: solicitantes de asilo por primera vez (migr_asyappctza)", url: "https://ec.europa.eu/eurostat/databrowser/view/migr_asyappctza/default/table" },
    { name: "Eurostat: beneficiarios de protección temporal (migr_asytpsm)", url: "https://ec.europa.eu/eurostat/databrowser/view/migr_asytpsm/default/table" },
  ],
};

export default theme;
