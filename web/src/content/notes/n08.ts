import { p, type Note } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/n08-*.json (Eurostat une_rt_a y lfsi_emp_a, 15 a 24 años, 2025). Ver editorial/registro/n08.md.
// La tasa sobre los activos por país ya está en el tema Empleo (EM-D1): esta nota cuenta el paro sobre todos los jóvenes.
const note: Note = {
  id: "n08",
  code: "N08",
  slug: { es: "paro-juvenil-todos-los-jovenes", en: "youth-unemployment-all-young-people" },
  title: {
    es: "Contados sobre todos los jóvenes, en Suecia hay más parados que en España o Rumanía",
    en: "Counted over all young people, Sweden has more unemployed than Spain or Romania",
  },
  dek: {
    es: "Rumanía y España tienen las tasas de paro juvenil más altas de la UE. Pero si los parados se cuentan sobre todos los jóvenes de 15 a 24 años, y no solo sobre los que trabajan o buscan empleo, Suecia, Finlandia y Dinamarca pasan delante.",
    en: "Romania and Spain have the highest youth unemployment rates in the EU. But if the unemployed are counted over all young people aged 15 to 24, and not only over those who work or look for work, Sweden, Finland and Denmark move ahead.",
  },
  published: "2026-10-27",
  updated: "2026-10-27",
  lens: "dentro",
  theme: "empleo",
  body: [
    p("La tasa de paro juvenil divide a los jóvenes en paro entre los jóvenes activos, los que trabajan o buscan empleo. Con esa medida, en 2025 Rumanía (26,1 %) y España (24,9 %) encabezan la UE, como se ve en el tema de empleo. Pero hay otra forma de contarlo: dividir a los mismos parados entre todos los jóvenes de 15 a 24 años, estudien o no. Eurostat la llama proporción de paro.",
      "The youth unemployment rate divides unemployed young people by young people in the labour force, those who work or look for work. On that measure, in 2025 Romania (26.1%) and Spain (24.9%) top the EU, as the jobs topic shows. But there is another way to count: divide the same unemployed by all young people aged 15 to 24, whether studying or not. Eurostat calls it the unemployment ratio."),
    p("Con ella, el orden cambia. Suecia queda primera: el 13,9 % de sus jóvenes está en paro. Le siguen Finlandia (11,7 %) y Dinamarca (9,6 %), que con la tasa ocupaba el puesto 17. España baja al sexto lugar (8,4 %) y Rumanía, al 6,2 %, lo mismo que la media de la UE. Italia, con la sexta tasa más alta (20,6 %), tiene el 4,6 % de sus jóvenes en paro. Alemania tiene la tasa más baja (7,1 %); con la proporción (3,9 %), Bulgaria (2,5 %), Chequia (2,9 %) y Polonia (3,8 %) quedan por debajo.",
      "On this measure, the order changes. Sweden comes first: 13.9% of its young people are unemployed. It is followed by Finland (11.7%) and Denmark (9.6%), which ranked 17th on the rate. Spain drops to sixth (8.4%) and Romania to 6.2%, the same as the EU average. Italy, with the sixth-highest rate (20.6%), has 4.6% of its young people unemployed. Germany has the lowest rate (7.1%); on the ratio (3.9%), Bulgaria (2.5%), Czechia (2.9%) and Poland (3.8%) are lower."),
    { fig: "n08-paro-dos-medidas", code: "1" },
    p("La diferencia está en cuántos jóvenes trabajan o buscan empleo. En la UE es el 40,7 %. En los Países Bajos, el 83,3 %; en Dinamarca, el 69,9 %, y en Suecia, el 57,2 %: allí muchos estudiantes trabajan o buscan trabajo a la vez, y si no lo encuentran cuentan como parados. En Bulgaria es el 19,1 %; en Italia, el 22,6 %, y en Rumanía, el 23,8 %. Con tan pocos jóvenes activos, unos pocos parados bastan para que la tasa sea alta. En España, el 33,7 %, por debajo de la media.",
      "The difference lies in how many young people work or look for work. In the EU it is 40.7%. In the Netherlands it is 83.3%; in Denmark 69.9%, and in Sweden 57.2%: there, many students work or look for work at the same time, and if they do not find it they count as unemployed. In Bulgaria it is 19.1%; in Italy 22.6%, and in Romania 23.8%. With so few young people in the labour force, a small number of unemployed is enough to push the rate up. In Spain it is 33.7%, below the average."),
    { fig: "n08-jovenes-activos", code: "2" },
    p("Lo que no dicen estos datos. Ninguna de las dos medidas dice si un joven inactivo está estudiando o ni estudia ni trabaja, ni si un parado es un estudiante que busca unas horas o alguien que ya ha dejado los estudios. Los jóvenes que ni estudian ni trabajan están en el tema de empleo.",
      "What these data do not say. Neither measure says whether an inactive young person is studying or neither in work nor in education, nor whether an unemployed person is a student looking for a few hours' work or someone who has already left education. Young people neither in work nor in education are covered in the jobs topic."),
    { see: { es: "Empleo y jóvenes: paro juvenil, contratos temporales y edad de emancipación", en: "Jobs and young people: youth unemployment, temporary contracts and the age of leaving home" }, href: { es: "/es/empleo/", en: "/en/jobs/" } },
  ],
  sources: [
    { name: "Eurostat: paro por sexo y edad, tasa y proporción (une_rt_a)", url: "https://ec.europa.eu/eurostat/databrowser/view/une_rt_a/default/table" },
    { name: "Eurostat: tasa de actividad por sexo y edad (lfsi_emp_a)", url: "https://ec.europa.eu/eurostat/databrowser/view/lfsi_emp_a/default/table" },
  ],
};

export default note;
