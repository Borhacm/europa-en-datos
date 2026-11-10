import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n12-*.json (Eurostat edat_lfse_03, 2025). Ver editorial/registro/n12.md.
const note: Note = {
  id: "n12",
  code: "N12",
  slug: { es: "estudios-superiores-objetivo-2030", en: "tertiary-education-2030-target" },
  title: {
    es: "11 de los 27 países ya superan el objetivo europeo de estudios superiores para 2030; la UE en conjunto, todavía no",
    en: "11 of the 27 countries already exceed the EU's 2030 tertiary education target; the EU as a whole does not yet",
  },
  dek: {
    es: "En 2025, el 44,8 % de las personas de 25 a 34 años de la UE tenía estudios superiores, por debajo del 47 % fijado para 2030. Irlanda llega al 66,8 % y Rumanía se queda en el 23 %. Las mujeres van por delante de los hombres en todos los países.",
    en: "In 2025, 44.8% of 25 to 34-year-olds in the EU had tertiary education, below the 47% set for 2030. Ireland reaches 66.8% and Romania stays at 23%. Women are ahead of men in every country.",
  },
  published: "2026-11-10",
  updated: "2026-11-10",
  lens: "dentro",
  theme: "educacion",
  body: [
    p("En 2026, el Consejo de la UE subió del 45 % al 47 % la parte de las personas de 25 a 34 años que deberían tener estudios superiores en 2030. Es un objetivo para la media de la UE, no para cada país. En 2025, la UE estaba en el 44,8 %: por debajo de los dos.",
      "In 2026, the Council of the EU raised from 45% to 47% the share of 25 to 34-year-olds who should have tertiary education by 2030. It is a target for the EU average, not for each country. In 2025 the EU stood at 44.8%: below both."),
    p("Once países ya pasan del 47 %. Irlanda (66,8 %) y Luxemburgo (65,2 %) encabezan la lista, seguidos de Lituania (60,8 %) y Chipre (60 %). España, con el 52,5 %, está empatada con Dinamarca, y Malta (47,7 %) lo supera por poco. Polonia (45,2 %) está entre el objetivo antiguo y el nuevo. Los otros 15 países no llegan al 45 %. Alemania está en el 40,9 %, Hungría en el 32,6 % e Italia en el 31,1 %. Rumanía, con el 23 %, no llega a la mitad del objetivo.",
      "Eleven countries are already above 47%. Ireland (66.8%) and Luxembourg (65.2%) top the list, followed by Lithuania (60.8%) and Cyprus (60%). Spain, at 52.5%, is level with Denmark, and Malta (47.7%) is just above. Poland (45.2%) sits between the old and the new target. The other 15 countries are below 45%. Germany is at 40.9%, Hungary at 32.6% and Italy at 31.1%. Romania, at 23%, is below half of the target."),
    { fig: "n12-universitarios-paises", code: "1" },
    p("La distancia está sobre todo en los hombres. En la UE, el 50,5 % de las mujeres de 25 a 34 años tiene estudios superiores, frente al 39,3 % de los hombres: 11,2 puntos más. Ellas van por delante en los 27 países, y en 20 pasan del 47 %; ellos, solo en seis. Las mayores diferencias son las de Eslovenia (23,8 puntos) y Estonia (23); las menores, las de Rumanía (4,1) y Luxemburgo (4,5). En España, el 58,7 % de las mujeres y el 46,6 % de los hombres.",
      "The gap lies mostly with men. In the EU, 50.5% of women aged 25 to 34 have tertiary education, against 39.3% of men: 11.2 points more. Women are ahead in all 27 countries, and in 20 they are above 47%; men, in only six. The largest gaps are in Slovenia (23.8 points) and Estonia (23); the smallest, in Romania (4.1) and Luxembourg (4.5). In Spain, 58.7% of women and 46.6% of men."),
    { fig: "n12-universitarios-sexo", code: "2" },
    p("Lo que no dicen estos datos. Cuentan títulos, no lo que se aprende, y meten en el mismo grupo un ciclo corto de formación profesional superior y un doctorado. Miden dónde vive cada persona y no dónde estudió, así que la emigración y la inmigración de titulados mueven las cifras. Y como la encuesta cambió en 2021, no sirven para decir cuánto se ha avanzado en cada país.",
      "What these data do not say. They count qualifications, not learning, and put a short higher vocational course and a doctorate in the same group. They measure where each person lives, not where they studied, so emigration and immigration of graduates move the figures. And because the survey changed in 2021, they cannot show how much each country has progressed."),
    { see: { es: "Educación y talento: abandono escolar, gasto y los objetivos europeos para 2030", en: "Education and talent: early school leaving, spending and the EU's 2030 targets" }, href: { es: "/es/educacion/", en: "/en/education/" } },
  ],
  sources: [
    { name: "Eurostat: población de 25 a 34 años con estudios superiores (edat_lfse_03)", url: "https://ec.europa.eu/eurostat/databrowser/view/edat_lfse_03/default/table" },
    { name: "Consejo de la UE: Resolución relativa al segundo ciclo del marco estratégico del Espacio Europeo de Educación (2026-2030), C/2026/3720", url: "https://op.europa.eu/es/publication-detail/-/publication/cd806b9d-7bf7-11f1-bf5e-01aa75ed71a1" },
  ],
};

export default note;
