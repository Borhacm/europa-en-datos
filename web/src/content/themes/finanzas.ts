import { p, type Theme } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/fp*.json (FMI, OCDE y Eurostat). Ver editorial/registro/finanzas.md.
// Ficha del Reglamento (UE) 2024/1263 cotejada en EUR-Lex (arts. 2, 6, 7 y 8); procedimientos abiertos, en la Comisión;
// cláusula de escape para defensa, en el Consejo (ver sources).
const theme: Theme = {
  id: "finanzas",
  code: "FP",
  slug: { es: "finanzas-publicas", en: "public-finances" },
  title: { es: "Finanzas públicas", en: "Public finances" },
  status: "published",
  order: 9,
  published: "2026-10-20",
  dek: {
    es: "EE. UU. gasta mucho más de lo que ingresa: en 2024, su déficit fue del 7,8 % del PIB y el de la UE, del 3,1 %. Los europeos pagan más impuestos, sobre todo cotizaciones sociales e impuestos sobre el consumo, y sus gobiernos gastan más en protección social. Dentro de la UE, diez países superan el límite del 3 %.",
    en: "The US spends far more than it takes in: in 2024 its deficit was 7.8% of GDP and the EU's 3.1%. Europeans pay more tax, above all social contributions and consumption taxes, and their governments spend more on social protection. Within the EU, ten countries are above the 3% limit.",
  },
  lenses: {
    gigantes: {
      lede: { es: "EE. UU. lleva dos décadas con déficits que la UE solo ha tenido en las crisis. China se ha sumado desde 2016.", en: "The US has run for two decades deficits the EU has only had in crises. China has joined it since 2016." },
      body: [
        p("Desde 2001, EE. UU. ha gastado casi siempre bastante más de lo que ingresa. Su déficit público superó el 3 % del PIB en 21 de los 24 años hasta 2024; solo quedó por debajo en 2001, 2006 y 2007. La UE lo superó en 10 de esos años, y en 9 de ellos estaba en una de las dos grandes crisis: de 2009 a 2012 y desde 2020. En 2020, con la pandemia, el déficit de EE. UU. llegó al 14,1 % del PIB y el de la UE, al 6,7 %. En 2024, EE. UU. seguía en el 7,8 %; la UE, en el 3,1 %.",
          "Since 2001, the US has almost always spent well beyond its revenue. Its public deficit exceeded 3% of GDP in 21 of the 24 years up to 2024; it stayed below only in 2001, 2006 and 2007. The EU exceeded it in 10 of those years, and in 9 of them it was in one of the two big crises: from 2009 to 2012 and since 2020. In 2020, with the pandemic, the US deficit reached 14.1% of GDP and the EU's 6.7%. In 2024, the US was still at 7.8%; the EU, at 3.1%."),
        p("China ha cambiado de grupo. Hasta 2015, su déficit no pasó del 3 % ningún año. Desde 2016 lo supera todos, y en 2024 fue del 7,2 %, casi como el de EE. UU.",
          "China has changed groups. Until 2015, its deficit never exceeded 3%. Since 2016 it has done so every year, and in 2024 it was 7.2%, almost as high as the US."),
        { fig: "fpg1-deficit", code: "G1" },
        p("Una parte de la diferencia son los intereses de la deuda acumulada. En 2024, EE. UU. dedicó a pagar intereses netos el 3,2 % de su PIB, más del doble que la UE (1,5 %) y más del triple que China (0,9 %). Pero los intereses no lo explican todo: sin contarlos, el déficit de EE. UU. habría sido del 4,6 %, casi el triple que el de la UE (1,6 %). El de China, del 6,3 %.",
          "Part of the difference is interest on accumulated debt. In 2024, the US spent 3.2% of its GDP on net interest, more than twice the EU (1.5%) and more than three times China (0.9%). But interest does not explain it all: excluding it, the US deficit would have been 4.6%, almost three times the EU's (1.6%). China's, 6.3%."),
        { fig: "fpg2-intereses", code: "G2" },
        { see: { es: "Nota: la deuda pública de la UE, EE. UU. y China, y la de cada país de la UE", en: "Note: public debt in the EU, the US and China, and in each EU country" }, href: { es: "/es/notas/deuda-publica/", en: "/en/notes/public-debt/" } },
      ],
    },
    elige: {
      lede: { es: "Los gobiernos europeos recaudan y gastan mucho más que el estadounidense. Lo que separa a los dos modelos son las pensiones y el resto de la protección social.", en: "European governments collect and spend far more than the US government. What separates the two models is pensions and the rest of social protection." },
      body: [
        p("En 2023, las administraciones públicas de la UE recaudaron en impuestos el 38,6 % del PIB; las de EE. UU., el 25,6 %. En impuestos sobre la renta y los beneficios recaudan lo mismo: el 12,4 % del PIB. Los 13 puntos de diferencia están en dos partidas. Las cotizaciones sociales suponen el 12,6 % del PIB en la UE y el 6 % en EE. UU.; los impuestos sobre el consumo, el 11 % y el 4,2 %. EE. UU. solo recauda más en impuestos sobre la propiedad: el 2,9 % del PIB, frente al 1,7 %.",
          "In 2023, EU governments collected 38.6% of GDP in taxes; US governments, 25.6%. On income and profits they collect the same: 12.4% of GDP. The 13-point gap lies in two items. Social contributions amount to 12.6% of GDP in the EU and 6% in the US; consumption taxes, 11% and 4.2%. The US collects more only in property taxes: 2.9% of GDP, against 1.7%."),
        { fig: "fpe1-impuestos", code: "E1" },
        p("Ese dinero va sobre todo a la protección social. En 2024, las administraciones de la UE gastaron el 48,9 % del PIB y las de EE. UU., el 39,6 %. Solo en protección social (pensiones, desempleo, familia, invalidez), la UE gasta el 19,6 % del PIB y EE. UU., el 7,8 %: 11,8 puntos más, por encima de toda la diferencia. EE. UU. gasta más en cinco de las otras siete partidas. En sanidad, el 10,3 % del PIB frente al 7,3 %: aunque buena parte de su sanidad es privada, el gasto público en salud ya supera al europeo. También en defensa (3,1 % frente a 1,5 %) y en educación (5,6 % frente a 4,7 %).",
          "That money goes mainly to social protection. In 2024, EU governments spent 48.9% of GDP and US governments 39.6%. On social protection alone (pensions, unemployment, family, disability), the EU spends 19.6% of GDP and the US 7.8%: 11.8 points more, above the whole gap. The US spends more on five of the other seven items. On health, 10.3% of GDP against 7.3%: although much of its health care is private, its public health spending already exceeds Europe's. Also on defence (3.1% against 1.5%) and education (5.6% against 4.7%)."),
        { fig: "fpe2-gasto-funciones", code: "E2" },
        { see: { es: "Libertades, bienestar y clima: el gasto social de cada país de la UE frente a EE. UU.", en: "Freedoms, well-being and climate: social spending in each EU country compared with the US" }, href: { es: "/es/libertades/", en: "/en/freedoms/" } },
      ],
    },
    dentro: {
      lede: { es: "Diez países superan el déficit del 3 % que fija el Tratado, y los intereses pesan más que hace cuatro años en casi todos.", en: "Ten countries exceed the 3% deficit set by the Treaty, and interest weighs more than four years ago in almost all of them." },
      body: [
        p("En 2025, 10 de los 27 países de la UE tuvieron un déficit superior al 3 % del PIB. Los mayores fueron los de Rumanía (7,9 %) y Polonia (7,3 %), seguidos de Bélgica (5,2 %) y Francia (5,1 %). Cinco cerraron el año con superávit: Chipre (3,4 %), Dinamarca (2,9 %), Irlanda (1,8 %), Grecia (1,7 %) y Portugal (0,7 %). Grecia, el país más endeudado de la UE, ingresó más de lo que gastó. España, con un déficit del 2,4 %, quedó por debajo del límite.",
          "In 2025, 10 of the 27 EU countries ran a deficit above 3% of GDP. The largest were Romania's (7.9%) and Poland's (7.3%), followed by Belgium (5.2%) and France (5.1%). Five ended the year in surplus: Cyprus (3.4%), Denmark (2.9%), Ireland (1.8%), Greece (1.7%) and Portugal (0.7%). Greece, the most indebted EU country, took in more than it spent. Spain, with a deficit of 2.4%, stayed below the limit."),
        { fig: "fpd1-deficit-paises", code: "D1" },
        { h: { es: "La ficha: las nuevas reglas fiscales de la UE", en: "The policy card: the EU's new fiscal rules" }, id: "ficha-reglas-fiscales" },
        { steps: [
          { title: { es: "Qué es.", en: "What it is." },
            text: { es: "El Reglamento (UE) 2024/1263 es el centro de la reforma de las reglas fiscales europeas. Mantiene los límites del Tratado, el 3 % del PIB para el déficit y el 60 % para la deuda, pero cambia la forma de vigilarlos. Cada país presenta un plan fiscal-estructural a medio plazo con una senda de gasto neto: el gasto público sin contar los intereses, los programas pagados con fondos europeos, la parte cíclica del gasto en desempleo y las medidas puntuales, y descontando las subidas o bajadas de impuestos que decida el gobierno.",
                    en: "Regulation (EU) 2024/1263 is the core of the reform of the EU fiscal rules. It keeps the Treaty limits, 3% of GDP for the deficit and 60% for debt, but changes how they are monitored. Each country submits a medium-term fiscal-structural plan with a net expenditure path: public spending excluding interest, programmes paid for with EU funds, the cyclical part of unemployment spending and one-off measures, and net of tax rises or cuts decided by the government." } },
          { title: { es: "Quién y cuándo.", en: "Who and when." },
            text: { es: "Lo aprobaron el Parlamento Europeo y el Consejo el 29 de abril de 2024, y entró en vigor al publicarse, el 30 de abril. El periodo de ajuste es de cuatro años y puede ampliarse hasta tres más.",
                    en: "The European Parliament and the Council adopted it on 29 April 2024, and it entered into force on publication, on 30 April. The adjustment period is four years and can be extended by up to three more." } },
          { title: { es: "Qué debería pasar.", en: "What should happen." },
            text: { es: "Que la deuda baje en los países que más deben: al menos un punto del PIB al año de media si supera el 90 %, y medio punto si está entre el 60 % y el 90 %. El ajuste sigue hasta que el déficit estructural quede 1,5 puntos por debajo del 3 %. Desde julio de 2025, el Consejo ha activado en 18 países una cláusula de escape que les permite gastar más en defensa, hasta un 1,5 % del PIB al año, entre 2025 y 2028.",
                    en: "Debt should fall in the countries that owe most: by at least one point of GDP a year on average if it exceeds 90%, and half a point if it is between 60% and 90%. Adjustment continues until the structural deficit is 1.5 points below 3%. Since July 2025, the Council has activated in 18 countries an escape clause that lets them spend more on defence, up to 1.5% of GDP a year, between 2025 and 2028." } },
          { title: { es: "Con qué lo comparamos.", en: "What we compare it with." },
            text: { es: "Con D1. Los diez países con un procedimiento de déficit excesivo abierto, según la Comisión, son Austria, Bélgica, Bulgaria, Finlandia, Francia, Hungría, Italia, Polonia, Rumanía y Eslovaquia: los mismos diez que superaron el 3 % en 2025. Con datos hasta 2025, todavía no se puede saber si las nuevas reglas reducen la deuda.",
                    en: "With D1. The ten countries with an open excessive deficit procedure, according to the Commission, are Austria, Belgium, Bulgaria, Finland, France, Hungary, Italy, Poland, Romania and Slovakia: the same ten that exceeded 3% in 2025. With data up to 2025, it is too early to tell whether the new rules reduce debt." } },
        ] },
        p("El otro frente son los intereses. Desde 2021, el último año antes de que el BCE empezara a subir los tipos, el pago de intereses ha subido en 23 de los 27 países. Italia (3,9 % del PIB) y Hungría (3,8 %) son los que más dedican a ello, y Hungría es donde más ha crecido: 1,6 puntos. En el otro extremo están Luxemburgo (0,3 %), Estonia e Irlanda (0,5 %). España paga el 2,4 %, tres décimas más que en 2021. Solo en Portugal, Chipre, Irlanda y Croacia ha bajado.",
          "The other front is interest. Since 2021, the last year before the ECB began raising rates, interest payments have risen in 23 of the 27 countries. Italy (3.9% of GDP) and Hungary (3.8%) spend the most on it, and Hungary is where it has grown most: 1.6 points. At the other end are Luxembourg (0.3%), Estonia and Ireland (0.5%). Spain pays 2.4%, three tenths more than in 2021. It has fallen only in Portugal, Cyprus, Ireland and Croatia."),
        { fig: "fpd2-intereses-paises", code: "D2" },
        p("Lo que no dicen estos datos. El déficit y los intereses son flujos de un año: no dicen cuánto deben los países, que se cuenta en la nota N06, ni cuánto tienen en activos. Las cifras de China son las del FMI con la definición estrecha; el propio FMI publica otras más amplias, que suman la deuda de los vehículos de financiación de los gobiernos locales. La comparación de impuestos deja fuera lo que en EE. UU. se paga a seguros y planes de pensiones privados, que en Europa suelen cubrir las cotizaciones. Y ninguno de estos gráficos dice si un gobierno gasta bien o mal.",
          "What these data do not say. Deficits and interest are flows over one year: they do not say how much countries owe, which is covered in note N06, nor how much they hold in assets. China's figures are the IMF's on the narrow definition; the IMF itself publishes broader ones that add the debt of local government financing vehicles. The tax comparison leaves out what Americans pay to private insurance and pension plans, which in Europe contributions usually cover. And none of these charts says whether a government spends well or badly."),
      ],
    },
  },
  sources: [
    { name: "EUR-Lex: Reglamento (UE) 2024/1263, relativo a la coordinación eficaz de las políticas económicas y a la supervisión presupuestaria multilateral", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R1263" },
    { name: "Comisión Europea: procedimientos de déficit excesivo abiertos y cerrados", url: "https://economy-finance.ec.europa.eu/economic-governance-framework/stability-and-growth-pact/corrective-arm-excessive-deficit-procedure/excessive-deficit-procedures-overview_en" },
    { name: "Consejo de la UE: cláusula de escape nacional para el gasto en defensa", url: "https://www.consilium.europa.eu/en/policies/national-escape-clause-for-defence-expenditure-nec/" },
    { name: "BCE (21/07/2022): decisiones de política monetaria (primera subida de tipos del ciclo)", url: "https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp220721~53e5bdd317.en.html" },
  ],
};

export default theme;
