import { p, type Theme } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/ed*.json (Banco Mundial y Eurostat, descargados el 6 de noviembre de 2026). Ver editorial/registro/educacion.md.
// Ficha: Resolución del Consejo C/2026/3720 (DO de 10/07/2026) y Resolución 2021/C 66/01, leídas en el Diario Oficial (Cellar de la Oficina de Publicaciones).
// Universitarios de 25 a 34 años en la UE: Eurostat edat_lfse_03 (ED5-8, Y25-34, 2025).
const theme: Theme = {
  id: "educacion",
  code: "ED",
  slug: { es: "educacion", en: "education" },
  title: { es: "Educación y talento", en: "Education and talent" },
  status: "published",
  order: 14,
  published: "2026-11-06",
  dek: {
    es: "China ha multiplicado por diez su matrícula en estudios superiores desde 2000 y ya tiene más investigadores que la UE, aunque menos por habitante. Dentro de la UE, el abandono temprano de los estudios ha bajado en 20 de los 27 países, pero la Unión aún no llega a los objetivos para 2030, que el Consejo endureció en 2026.",
    en: "China has increased its higher-education enrolment tenfold since 2000 and now has more researchers than the EU, although fewer per person. Within the EU, early school leaving has fallen in 20 of the 27 countries, but the Union has not yet reached the 2030 targets, which the Council tightened in 2026.",
  },
  lenses: {
    gigantes: {
      lede: {
        es: "La UE ya matricula en estudios superiores a una parte de su población tan grande como EE. UU., y China está a punto de alcanzarlas. En investigadores por habitante, la UE se ha acercado a EE. UU.",
        en: "The EU now enrols as large a share of its population in higher education as the US, and China is about to catch up with both. In researchers per person, the EU has closed in on the US.",
      },
      body: [
        p(
          "En 2000, la tasa bruta de matrícula en estudios superiores de China era del 7,6 %; en 2024, del 76,9 %, diez veces más. En el mismo tiempo, la de la UE ha pasado del 50,9 % al 79,5 %. EE. UU. estuvo entre el 87,6 % y el 88,9 % de 2013 a 2020 y bajó al 79,4 % en 2022, su último año con dato. Ese año, la UE (79,6 %) lo superó por primera vez en los años con dato de los dos. La tasa bruta cuenta a los estudiantes de cualquier edad, así que no es la parte de los jóvenes que estudia.",
          "In 2000, China's gross enrolment ratio in higher education was 7.6%; in 2024, 76.9%, ten times higher. Over the same period, the EU's went from 50.9% to 79.5%. The US stood between 87.6% and 88.9% from 2013 to 2020 and fell to 79.4% in 2022, its latest year with data. That year, the EU (79.6%) overtook it for the first time in the years with data for both. The gross ratio counts students of any age, so it is not the share of young people who study.",
        ),
        { fig: "edg1-matricula-superior", code: "G1" },
        p(
          "La UE tenía 2.117 investigadores por millón de habitantes en 2000 y 4.741 en 2023: más del doble. EE. UU. ha pasado de 3.556 a 4.937, en 2022. China, de 550 a 2.107. Por habitante sigue muy por detrás, pero con su población eso son unos 3 millones de investigadores, frente a 2,1 millones en la UE y 1,6 millones en EE. UU. Lo que dedica cada bloque a investigar, en dinero, se cuenta en el tema de IA y digital.",
          "The EU had 2,117 researchers per million people in 2000 and 4,741 in 2023: more than twice as many. The US went from 3,556 to 4,937, in 2022. China, from 550 to 2,107. Per person it is still far behind, but with its population that comes to about 3 million researchers, against 2.1 million in the EU and 1.6 million in the US. How much each bloc spends on research is covered in the AI and digital topic.",
        ),
        { fig: "edg2-investigadores", code: "G2" },
        { see: { es: "IA y digital: gasto en I+D, modelos de IA y empresas", en: "AI and digital: R&D spending, AI models and businesses" }, href: { es: "/es/ia-digital/", en: "/en/ai-digital/" } },
      ],
    },
    elige: {
      lede: {
        es: "La mayor parte del dinero público de educación va a la escuela, no a la universidad. Y quien estudia más tiene más empleo, aunque la distancia cambia mucho de un país a otro.",
        en: "Most public education money goes to schools, not universities. And people with more education are more likely to have a job, although the gap varies a great deal from country to country.",
      },
      body: [
        p(
          "En 2024, las administraciones públicas de la UE gastaron en educación el 4,7 % del PIB. El 71,9 % fue a infantil, primaria y secundaria; el 16 %, a la educación superior, y el 12,2 %, a servicios como el transporte escolar y los comedores, a investigación y a otros gastos. Grecia es el país que más parte dedica a la educación superior (32,9 %), seguida de Hungría (28,4 %) y Finlandia (27,5 %). La más baja es la de Francia (8,3 %), y en Italia y Eslovaquia es del 10,3 %. En España, el 13,4 %. El reparto no dice cuánto se gasta por alumno: un país con más jóvenes en edad escolar o con más universitarios reparte el dinero de otra forma.",
          "In 2024, EU governments spent 4.7% of GDP on education. 71.9% went to pre-primary, primary and secondary education; 16% to tertiary education, and 12.2% to services such as school transport and meals, to research and to other spending. Greece devotes the largest share to tertiary education (32.9%), followed by Hungary (28.4%) and Finland (27.5%). The lowest is France's (8.3%), and in Italy and Slovakia it is 10.3%. In Spain, 13.4%. The split does not say how much is spent per student: a country with more school-age children or more university students divides the money differently.",
        ),
        { fig: "ede1-gasto-niveles", code: "E1" },
        p(
          "¿Compensa estudiar? En 2025, en la UE tenía empleo el 88,4 % de los jóvenes de 20 a 34 años con estudios superiores que ya no estudiaban, el 80,6 % de los que tenían bachillerato o FP y el 56,5 % de los que no pasaron de la secundaria obligatoria: 31,9 puntos entre los dos extremos. En Eslovaquia, la distancia es de 58 puntos, y en Finlandia, de 56,4. En Chipre, de 11,9. España es el quinto país con menos distancia (19,7 puntos): quienes solo tienen la secundaria obligatoria trabajan más que en la media de la UE (67,1 %) y los titulados superiores, algo menos (86,8 %). En Chequia, los titulados superiores tienen menos empleo que los de bachillerato o FP. Cómo les va a los jóvenes en el mercado de trabajo, con el paro juvenil y los que ni estudian ni trabajan, se cuenta en el tema de empleo.",
          "Does studying pay off? In 2025, 88.4% of EU 20 to 34-year-olds with tertiary education who were no longer studying had a job, against 80.6% of those with upper secondary or vocational education and 56.5% of those with lower secondary at most: 31.9 points between the two ends. In Slovakia, the gap is 58 points, and in Finland, 56.4. In Cyprus, 11.9. Spain has the fifth-smallest gap (19.7 points): people with lower secondary at most are more likely to work than the EU average (67.1%) and tertiary graduates somewhat less (86.8%). In Czechia, tertiary graduates have a lower employment rate than those with upper secondary or vocational education. The jobs topic shows how young people fare in the labour market, with youth unemployment and those neither in work nor in education.",
        ),
        { fig: "ede2-empleo-nivel", code: "E2" },
        { see: { es: "Empleo y jóvenes: tasa de empleo, paro juvenil y emancipación", en: "Jobs and young people: employment, youth unemployment and leaving home" }, href: { es: "/es/empleo/", en: "/en/jobs/" } },
      ],
    },
    dentro: {
      lede: {
        es: "Cada vez menos jóvenes dejan pronto los estudios, pero en Alemania y otros seis países la tasa es más alta que en 2015. Y ningún país tiene en ciencias e ingenierías tantas mujeres como pide la UE.",
        en: "Fewer and fewer young people leave education early, but in Germany and six other countries the rate is higher than in 2015. And no country has as many women in science and engineering as the EU is asking for.",
      },
      body: [
        p(
          "En 2025, el 9,1 % de los europeos de 18 a 24 años había dejado los estudios sin pasar de la secundaria obligatoria, frente al 11 % de 2015. Ha bajado en 20 de los 27 países. Las mayores caídas son las de Malta (del 16,3 % al 8,6 %), Portugal (del 13,5 % al 6,1 %) y España (del 20 % al 12,8 %). Pero ha subido en siete. Entre ellos, Alemania, del 10,1 % al 13,1 %, que ahora tiene la segunda tasa más alta, tras Rumanía (15,5 %), y Chipre, del 5,2 % al 9,8 %. Catorce países están ya por debajo del 8 %. Croacia tiene la tasa más baja (2,1 %), aunque Eurostat marca su dato como poco fiable.",
          "In 2025, 9.1% of Europeans aged 18 to 24 had left education with lower secondary at most, against 11% in 2015. It has fallen in 20 of the 27 countries. The largest drops are in Malta (from 16.3% to 8.6%), Portugal (from 13.5% to 6.1%) and Spain (from 20% to 12.8%). But it has risen in seven. Among them, Germany, from 10.1% to 13.1%, which now has the second-highest rate after Romania (15.5%), and Cyprus, from 5.2% to 9.8%. Fourteen countries are already below 8%. Croatia has the lowest rate (2.1%), although Eurostat flags its figure as unreliable.",
        ),
        { fig: "edd1-abandono-paises", code: "D1" },
        p(
          "En 2024, el 27,1 % de los estudiantes de educación superior de la UE estaba matriculado en ciencias, matemáticas, informática o ingenierías (CTIM). Solo cuatro países superan el 32 % que la UE se ha fijado para 2030: Irlanda (36,4 %), Finlandia (35,8 %), Alemania (35,4 %) y Grecia (34,4 %). El dato irlandés hay que tomarlo con cautela: sus estudiantes de ingeniería se duplican en un año. España se queda en el 25,3 %. Las mujeres son el 32,2 % de los estudiantes CTIM de la UE. Suecia es el país que más se acerca a dos de cada cinco (38,5 %); en Alemania son el 29,8 %, y en Irlanda, el 25,6 %.",
          "In 2024, 27.1% of EU tertiary students were enrolled in science, mathematics, computing or engineering (STEM). Only four countries exceed the 32% the EU has set for 2030: Ireland (36.4%), Finland (35.8%), Germany (35.4%) and Greece (34.4%). The Irish figure should be read with caution: its engineering students doubled in one year. Spain stands at 25.3%. Women make up 32.2% of STEM students in the EU. Sweden comes closest to two in five (38.5%); in Germany the figure is 29.8%, and in Ireland, 25.6%.",
        ),
        { fig: "edd2-ctim-paises", code: "D2" },
        { h: { es: "La ficha: los objetivos europeos de educación para 2030", en: "The policy card: the EU's education targets for 2030" }, id: "ficha-espacio-europeo-educacion" },
        { steps: [
          { title: { es: "Qué es.", en: "What it is." },
            text: { es: "Una resolución del Consejo de la UE que fija el segundo ciclo, de 2026 a 2030, del Espacio Europeo de Educación: prioridades comunes y nueve ámbitos con objetivos medibles. No es una ley: la educación es competencia de cada país, y los objetivos son «niveles de referencia del rendimiento medio europeo» que los Estados deben alcanzar en conjunto, no cada uno por separado.",
                    en: "A resolution of the Council of the EU setting the second cycle, from 2026 to 2030, of the European Education Area: common priorities and nine areas with measurable targets. It is not a law: education is a national competence, and the targets are «reference levels of European average performance» that member states should reach together, not each one separately." } },
          { title: { es: "Quién y cuándo.", en: "Who and when." },
            text: { es: "Los ministros de los 27, en el Consejo. Se publicó en el Diario Oficial el 10 de julio de 2026 y revisa los objetivos del primer ciclo, que el Consejo publicó en febrero de 2021.",
                    en: "The ministers of the 27, in the Council. It was published in the Official Journal on 10 July 2026 and revises the first-cycle targets, which the Council published in February 2021." } },
          { title: { es: "Qué debería pasar.", en: "What should happen." },
            text: { es: "Que para 2030 menos del 8 % de los jóvenes de 18 a 24 años deje pronto los estudios (el objetivo de 2021 era menos del 9 %), que al menos el 47 % de las personas de 25 a 34 años tenga estudios superiores (antes, el 45 %) y que al menos el 32 % de los estudiantes de educación superior esté en carreras CTIM, con al menos dos mujeres de cada cinco.",
                    en: "By 2030, fewer than 8% of 18 to 24-year-olds should leave education early (the 2021 target was below 9%), at least 47% of 25 to 34-year-olds should have tertiary education (previously 45%) and at least 32% of tertiary students should be in STEM, with at least two women in every five." } },
          { title: { es: "Con qué lo comparamos.", en: "What we compare it with." },
            text: { es: "Con los datos de Eurostat. En 2025, el abandono temprano de la UE era del 9,1 % (gráfico D1): todavía por encima del objetivo antiguo. El 44,8 % de las personas de 25 a 34 años tenía estudios superiores, por debajo tanto del 45 % como del 47 %. Y en 2024, los estudiantes CTIM eran el 27,1 %, y las mujeres, el 32,2 % de ellos (gráfico D2).",
                    en: "With Eurostat data. In 2025, early school leaving in the EU stood at 9.1% (chart D1): still above the old target. 44.8% of 25 to 34-year-olds had tertiary education, below both 45% and 47%. And in 2024, STEM students made up 27.1%, and women 32.2% of them (chart D2)." } },
        ] },
        p(
          "Lo que no dicen estos datos. No miden lo que se aprende: el primer objetivo europeo, que menos del 15 % de los alumnos de 15 años tenga un rendimiento bajo en lectura, matemáticas y ciencias, depende de PISA, que no está en este artículo. Las cifras de EE. UU. y China vienen de la UNESCO y no tienen el detalle de las encuestas europeas, y la tasa bruta de matrícula no dice cuántos terminan. El reparto del gasto público depende de cómo clasifica cada país sus centros, no incluye lo que pagan las familias y no dice cuánto se gasta por alumno. Que quien estudia más tenga más empleo no permite atribuir esa diferencia a los estudios. Y estos datos no permiten saber qué políticas explican que el abandono baje en unos países y suba en otros.",
          "What these data do not say. They do not measure learning: the first EU target, that fewer than 15% of 15-year-olds should be low achievers in reading, mathematics and science, depends on PISA, which is not in this article. The US and Chinese figures come from UNESCO and lack the detail of the European surveys, and the gross enrolment ratio does not say how many graduate. The split of public spending depends on how each country classifies its institutions, excludes what households pay and does not show spending per student. That people with more education are more likely to work does not allow the difference to be attributed to education. And these data cannot tell which policies explain why early school leaving falls in some countries and rises in others.",
        ),
      ],
    },
  },
  sources: [
    { name: "Consejo de la UE: Resolución relativa al segundo ciclo del marco estratégico del Espacio Europeo de Educación (2026-2030), C/2026/3720", url: "https://op.europa.eu/es/publication-detail/-/publication/cd806b9d-7bf7-11f1-bf5e-01aa75ed71a1" },
    { name: "Consejo de la UE: Resolución relativa a un marco estratégico para la cooperación europea en el ámbito de la educación y la formación (2021-2030), 2021/C 66/01", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32021G0226(01)" },
    { name: "Comisión Europea: marco estratégico del Espacio Europeo de Educación y objetivos para 2030", url: "https://education.ec.europa.eu/about-eea/strategic-framework" },
    { name: "Eurostat: población de 25 a 34 años con estudios superiores (edat_lfse_03)", url: "https://ec.europa.eu/eurostat/databrowser/view/edat_lfse_03/default/table" },
  ],
};

export default theme;
