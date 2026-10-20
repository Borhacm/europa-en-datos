import { p, type Theme } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/tr*.json (EDGAR del JRC y Eurostat). Ver editorial/registro/transporte.md.
// Ficha del Reglamento (UE) 2023/851 cotejada en EUR-Lex (art. 1); estado de la propuesta de 2025, en el Parlamento Europeo.
const theme: Theme = {
  id: "transporte",
  code: "TR",
  slug: { es: "transporte", en: "transport" },
  title: { es: "Transporte y transición verde", en: "Transport and the green transition" },
  status: "published",
  order: 11,
  published: "2026-10-20",
  dek: {
    es: "El transporte es el único sector en el que la UE emite más gases que en 1990, y ya es el que más emite. El coche sigue moviendo a más de ocho de cada diez viajeros, los compradores eligen híbridos y solo el 2,9 % de los coches que circulan son eléctricos, a nueve años de 2035, cuando la ley actual exige que todos los coches nuevos dejen de emitir CO2.",
    en: "Transport is the only sector in which the EU emits more greenhouse gases than in 1990, and it is now the largest emitter. Cars still carry more than eight in ten passengers, buyers are choosing hybrids and only 2.9% of the cars on the road are electric, nine years before 2035, when current law requires all new cars to stop emitting CO2.",
  },
  lenses: {
    gigantes: {
      lede: { es: "Mientras la electricidad, la industria y los edificios recortan emisiones, el transporte apenas se mueve, en la UE y en EE. UU.", en: "While electricity, industry and buildings cut emissions, transport barely moves, in the EU and in the US." },
      body: [
        p("En 2024, el transporte de la UE emitió 791 millones de toneladas de gases de efecto invernadero, un 21 % más que en 1990. Es el único sector que no ha bajado: la electricidad, la industria, los edificios o la agricultura emiten hoy menos que entonces. Las emisiones del transporte tocaron techo en 2007, con 853,8 millones de toneladas, y desde entonces han bajado poco: en 2024 seguían por encima de las de 2000. EE. UU. emite más del doble (1.702,8 millones), un 17 % más que en 1990. En China se han multiplicado por diez, hasta 957,4 millones.",
          "In 2024, EU transport emitted 791 million tonnes of greenhouse gases, 21% more than in 1990. It is the only sector that has not fallen: electricity, industry, buildings and agriculture all emit less than then. Transport emissions peaked in 2007, at 853.8 million tonnes, and have fallen little since: in 2024 they were still above their 2000 level. The US emits more than twice as much (1,702.8 million), 17% more than in 1990. In China they have increased tenfold, to 957.4 million."),
        { fig: "trg1-emisiones", code: "G1" },
        p("Como los demás sectores sí han recortado, el transporte pesa cada vez más. En 1990 suponía el 13,5 % de las emisiones de la UE; en 2024, el 25 %, y ya es el sector que más emite, por delante de la generación de electricidad y calor. En EE. UU. ha pasado del 23,4 % al 28,8 %. En China es solo el 6,2 %, porque el resto de su economía emite mucho más.",
          "Because other sectors have made cuts, transport weighs more and more. In 1990 it was 13.5% of EU emissions; in 2024, 25%, and it is now the largest emitting sector, ahead of power and heat generation. In the US it has gone from 23.4% to 28.8%. In China it is only 6.2%, because the rest of its economy emits far more."),
        { fig: "trg2-peso-transporte", code: "G2" },
        { see: { es: "Libertades, bienestar y clima: las emisiones totales de la UE, EE. UU. y China", en: "Freedoms, well-being and climate: total emissions in the EU, the US and China" }, href: { es: "/es/libertades/", en: "/en/freedoms/" } },
      ],
    },
    elige: {
      lede: { es: "La UE ha fijado el fin de las emisiones de los coches nuevos para 2035, pero el coche sigue dominando y los compradores eligen híbridos.", en: "The EU has set 2035 as the end of emissions from new cars, but cars still dominate and buyers are choosing hybrids." },
      body: [
        p("En 2024, el coche movió el 82,5 % de los pasajeros-kilómetro del transporte terrestre de la UE; en 2000, el 82 %. El tren ha subido poco, del 7,5 % al 8,9 %, y el autobús ha bajado del 10,5 % al 8,6 %. La pandemia hundió el transporte público en 2020 y 2021, pero el tren ya ha recuperado lo perdido: en 2019 movía el 7,9 %.",
          "In 2024, cars accounted for 82.5% of inland passenger-kilometres in the EU; in 2000, 82%. Rail has risen little, from 7.5% to 8.9%, and buses have fallen from 10.5% to 8.6%. The pandemic hit public transport in 2020 and 2021, but rail has already recovered: in 2019 it carried 7.9%."),
        { fig: "tre1-reparto-viajeros", code: "E1" },
        p("En los coches nuevos, los europeos han elegido sobre todo el híbrido. En 2025, los híbridos sin enchufe fueron el 33,1 % de las matriculaciones, frente al 25,2 % de 2023, y ya superan a los de gasolina, que han bajado del 35,6 % al 27,3 %. El diésel ha caído del 14,1 % al 9,8 %, y los híbridos enchufables han subido al 9,4 %. Cuántos coches nuevos son eléctricos en cada país se cuenta en la nota N05.",
          "Among new cars, Europeans have mostly chosen hybrids. In 2025, non-plug-in hybrids made up 33.1% of registrations, up from 25.2% in 2023, and they now outsell petrol cars, which have fallen from 35.6% to 27.3%. Diesel has dropped from 14.1% to 9.8%, and plug-in hybrids have risen to 9.4%. How many new cars are electric in each country is covered in note N05."),
        { fig: "tre2-combustible-nuevos", code: "E2" },
        { see: { es: "Nota: qué parte de los coches nuevos ya son eléctricos en cada país", en: "Note: what share of new cars are already electric in each country" }, href: { es: "/es/notas/coche-electrico/", en: "/en/notes/electric-cars/" } },
        { h: { es: "La ficha: el fin de las emisiones de los coches nuevos en 2035", en: "The policy card: the end of emissions from new cars in 2035" }, id: "ficha-coches-2035" },
        { steps: [
          { title: { es: "Qué es.", en: "What it is." },
            text: { es: "El Reglamento (UE) 2023/851 endurece el Reglamento (UE) 2019/631, que fija cuánto CO2 pueden emitir de media los coches nuevos que vende cada fabricante en la UE. Si se pasan, pagan una prima por exceso de emisiones.",
                    en: "Regulation (EU) 2023/851 tightens Regulation (EU) 2019/631, which sets how much CO2 the new cars each manufacturer sells in the EU may emit on average. Those who exceed it pay an excess emissions premium." } },
          { title: { es: "Quién y cuándo.", en: "Who and when." },
            text: { es: "Lo aprobaron el Parlamento Europeo y el Consejo el 19 de abril de 2023.",
                    en: "The European Parliament and the Council adopted it on 19 April 2023." } },
          { title: { es: "Qué debería pasar.", en: "What should happen." },
            text: { es: "Desde 2025, los coches nuevos deben emitir de media un 15 % menos que el objetivo de 2021; desde 2030, un 55 % menos, y desde 2035, un 100 % menos. En la práctica, desde 2035 solo se podrán matricular coches nuevos que no emitan CO2 por el tubo de escape.",
                    en: "From 2025, new cars must emit on average 15% less than the 2021 target; from 2030, 55% less, and from 2035, 100% less. In practice, from 2035 only new cars that emit no CO2 from the exhaust can be registered." } },
          { title: { es: "Con qué lo comparamos.", en: "What we compare it with." },
            text: { es: "Con E2: en 2025, casi ocho de cada diez coches nuevos seguían llevando un motor de combustión, solo o como híbrido. Y la norma puede cambiar. En diciembre de 2025, la Comisión propuso rebajar el objetivo de 2035 al 90 % y compensar el resto con acero bajo en carbono fabricado en la UE y combustibles renovables. El Parlamento Europeo prevé votarlo el 23 de noviembre de 2026, y el Consejo, fijar su posición el 11 de diciembre.",
                    en: "With E2: in 2025, almost eight in ten new cars still had a combustion engine, alone or as a hybrid. And the rule may change. In December 2025, the Commission proposed lowering the 2035 target to 90% and offsetting the rest with low-carbon steel made in the EU and renewable fuels. The European Parliament is expected to vote on it on 23 November 2026, and the Council to set its position on 11 December." } },
        ] },
      ],
    },
    dentro: {
      lede: { es: "Entre países, el peso del tren y del coche eléctrico cambia mucho: en algunos ya es una parte visible del tráfico; en otros, casi nada.", en: "Between countries, the weight of rail and of electric cars varies widely: in some they are a visible part of traffic; in others, almost nothing." },
      body: [
        p("En 2024, el tren movió el 14 % de los viajeros en Hungría y el 13,7 % en Austria. Les siguen Francia (11,6 %), Suecia (11,3 %) y los Países Bajos (11 %). En el otro extremo están Grecia (0,6 %), Lituania (1,1 %) y Bulgaria (2,2 %). España, con un 8,8 %, está casi en la media de la UE.",
          "In 2024, rail carried 14% of passengers in Hungary and 13.7% in Austria. Next come France (11.6%), Sweden (11.3%) and the Netherlands (11%). At the other end are Greece (0.6%), Lithuania (1.1%) and Bulgaria (2.2%). Spain, at 8.8%, is close to the EU average."),
        { fig: "trd1-tren-paises", code: "D1" },
        p("El coche eléctrico avanza en las ventas, pero el parque cambia despacio. A finales de 2025, solo el 2,9 % de los coches que circulaban por la UE eran eléctricos de batería, frente al 0,4 % de 2020. Dinamarca es la gran excepción, con el 17,9 %. Le siguen Luxemburgo (8,7 %) y Suecia (8,6 %). En Polonia, Grecia y Croacia no llegan al 1 %, y en España, a poco más del 1 %.",
          "Electric cars are gaining in sales, but the fleet changes slowly. At the end of 2025, only 2.9% of the cars on EU roads were battery electric, up from 0.4% in 2020. Denmark is the big exception, at 17.9%. Next come Luxembourg (8.7%) and Sweden (8.6%). In Poland, Greece and Croatia they are below 1%, and in Spain just over 1%."),
        { fig: "trd2-electricos-parque", code: "D2" },
        { see: { es: "Energía: cuánta energía renovable usa ya el transporte", en: "Energy: how much renewable energy transport already uses" }, href: { es: "/es/energia/", en: "/en/energy/" } },
        p("Lo que no dicen estos datos. Las emisiones de EDGAR no incluyen la aviación ni la navegación internacionales, que se cuentan aparte y no se asignan a ningún país. El reparto entre coche, autobús y tren solo cubre el transporte terrestre: deja fuera el avión, la bicicleta y los desplazamientos a pie, y sus datos de 2010 a 2012 tienen problemas. Estos gráficos no dicen cuánto contamina cada coche en carretera, ni si los híbridos reducen tanto las emisiones como prometen. Tampoco permiten atribuir los cambios a una política concreta.",
          "What these data do not say. EDGAR emissions exclude international aviation and shipping, which are counted separately and not assigned to any country. The split between car, bus and train covers only inland transport: it leaves out air travel, cycling and walking, and its 2010-2012 data have problems. These charts do not say how much each car pollutes on the road, or whether hybrids cut emissions as much as promised. Nor can they attribute changes to a particular policy."),
      ],
    },
  },
  sources: [
    { name: "EUR-Lex: Reglamento (UE) 2023/851, que refuerza las normas de emisiones de CO2 de los turismos y furgonetas nuevos", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32023R0851" },
    { name: "Parlamento Europeo, Legislative Train: propuesta de 2025 de modificación de las normas de CO2 de los turismos y furgonetas (2025/0420(COD))", url: "https://www.europarl.europa.eu/legislative-train/package-automotive-package/file-co2-emission-standards-for-new-light-duty-vehicles-and-labelling" },
    { name: "Comisión Europea: paquete de automoción (16/12/2025)", url: "https://transport.ec.europa.eu/transport-themes/action-plan-future-automotive-sector/automotive-package_en" },
  ],
};

export default theme;
