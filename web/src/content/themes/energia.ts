import { p, type Theme } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/en*.json (Banco Mundial con datos de la AIE, y Eurostat) y n04-luz-cambio.json.
// Completado el 20/10/2026 (P2, ver editorial/registro/energia.md): ficha de la Directiva (UE) 2023/2413, límites,
// sin cifras repetidas entre miradas y sin repetir N04 (luz de los hogares) ni AN02 (Chipre frente a Finlandia).
const theme: Theme = {
  id: "energia",
  code: "EN",
  slug: { es: "energia", en: "energy" },
  title: { es: "Energía", en: "Energy" },
  status: "published",
  order: 8,
  published: "2026-10-16",
  updated: "2026-10-20",
  dek: {
    es: "La UE consume por habitante menos de la mitad de energía que EE. UU., y China ya la ha superado. Su electricidad depende mucho menos de los combustibles fósiles, pero las renovables solo cubren una cuarta parte de toda su energía y la industria paga la luz bastante más cara que antes de la crisis de 2022.",
    en: "The EU uses less than half as much energy per person as the US, and China has now overtaken it. Its electricity relies far less on fossil fuels, but renewables cover only a quarter of all its energy, and industry pays considerably more for power than before the 2022 crisis.",
  },
  lenses: {
    gigantes: {
      lede: { es: "Un estadounidense consume más del doble de energía que un europeo, y el chino medio ya ha adelantado al europeo.", en: "An American uses more than twice as much energy as a European, and the average person in China has now overtaken the average European." },
      body: [
        p("En 2024, cada habitante de la UE consumió 2.768 kilos equivalentes de petróleo en energía primaria. En EE. UU., 6.454, 2,3 veces más. China ha pasado de 898 kilos en 2000 a 2.947 en 2024, 3,3 veces más, y desde 2023 supera a la UE. Europa y EE. UU. consumen menos que a principios de siglo: un 19,2 % menos por habitante en la UE y un 19,9 % menos en EE. UU. Dentro de la UE, 17 de los 27 países consumen ya menos por habitante que China.",
          "In 2024, each person in the EU used 2,768 kilograms of oil equivalent in primary energy. In the US, 6,454, 2.3 times as much. China has gone from 898 kilograms in 2000 to 2,947 in 2024, 3.3 times as much, and has been ahead of the EU since 2023. Europe and the US use less than at the turn of the century: 19.2% less per person in the EU and 19.9% less in the US. Within the EU, 17 of the 27 countries now use less energy per person than China."),
        { fig: "eng1-consumo-habitante", code: "G1" },
        p("La diferencia más clara está en la electricidad. En 2024, el 27,8 % de la que se produjo en la UE salió de combustibles fósiles; en EE. UU., el 58,3 %, y en China, el 61,6 %. El carbón genera el 10,5 % de la electricidad europea, cuando en 2000 era el 31,8 %; en China sigue siendo el 58,6 %. EE. UU. también ha dejado atrás el carbón (del 52,5 % al 15,7 %), pero lo ha cambiado sobre todo por gas, que ya da el 42 % de su electricidad. La UE se apoya en la nuclear (23 %) y en la eólica, la solar y otras fuentes, que han pasado del 2,6 % al 35 %.",
          "The clearest difference is in electricity. In 2024, 27.8% of the electricity produced in the EU came from fossil fuels; in the US, 58.3%, and in China, 61.6%. Coal generates 10.5% of Europe's electricity, down from 31.8% in 2000; in China it is still 58.6%. The US has also moved away from coal (from 52.5% to 15.7%), but has replaced it mainly with gas, which now provides 42% of its electricity. The EU relies on nuclear (23%) and on wind, solar and other sources, which have risen from 2.6% to 35%."),
        { fig: "eng2-mezcla-electrica", code: "G2" },
      ],
    },
    elige: {
      lede: { es: "La UE ha elegido las renovables. En la electricidad va rápido; en el resto, no tanto. Y la industria paga la luz mucho más cara que antes de la crisis.", en: "The EU has chosen renewables. In electricity it is moving fast; elsewhere, less so. And industry pays far more for power than before the crisis." },
      body: [
        p("En 2024, las renovables cubrieron el 25,2 % del consumo final de energía de la UE, frente al 9,6 % de 2004. En la electricidad llegan ya al 47,5 %; en la calefacción y la refrigeración, al 26,7 %, y en el transporte, solo al 11,2 %. El objetivo para 2030 es el 42,5 %. Para alcanzarlo, la UE tendría que sumar casi tres puntos al año hasta 2030; entre 2019 y 2024 sumó, de media, poco más de uno.",
          "In 2024, renewables covered 25.2% of the EU's final energy consumption, up from 9.6% in 2004. In electricity they have reached 47.5%; in heating and cooling, 26.7%, and in transport, just 11.2%. The 2030 target is 42.5%. To reach it, the EU would need to add almost three points a year until 2030; between 2019 and 2024 it added just over one a year on average."),
        { fig: "ene1-renovables-ue", code: "E1" },
        { h: { es: "La ficha: el objetivo de renovables para 2030", en: "The policy card: the 2030 renewables target" }, id: "ficha-renovables" },
        p("El 42,5 % sale de la Directiva (UE) 2023/2413, de 18 de octubre de 2023, que reformó la directiva de renovables. Es un objetivo del conjunto de la UE, no de cada país: los Estados «velarán conjuntamente» por alcanzarlo y «procurarán» llegar al 45 %. La directiva añade metas por sectores: en los edificios, un objetivo indicativo del 49 % de renovables, y en el transporte, los proveedores de combustible deben garantizar al menos un 29 % de renovables o reducir un 14,5 % la intensidad de gases de efecto invernadero de lo que suministran.",
          "The 42.5% comes from Directive (EU) 2023/2413 of 18 October 2023, which reformed the renewables directive. It is a target for the EU as a whole, not for each country: member states \"shall collectively ensure\" it is reached and \"shall collectively endeavour\" to reach 45%. The directive adds sector targets: in buildings, an indicative 49% renewables target, and in transport, fuel suppliers must ensure at least 29% renewables or cut the greenhouse gas intensity of what they supply by 14.5%."),
        p("La otra cara es el precio. Entre 2007 y 2020, la electricidad para la industria europea nunca pasó de 10,72 céntimos por kWh, sin IVA ni impuestos recuperables. Con la crisis energética, llegó a 20,16 céntimos en el segundo semestre de 2022. En el segundo de 2025 estaba en 15,96: un 20,8 % por debajo de ese máximo, pero un 45,8 % por encima del primer semestre de 2021. Sin impuestos, la subida es del 80,6 %. No hay una serie abierta que permita comparar este precio con el de EE. UU. y China con el mismo método.",
          "The other side is price. Between 2007 and 2020, electricity for European industry never cost more than 10.72 cents per kWh, excluding VAT and recoverable taxes. With the energy crisis, it reached 20.16 cents in the second half of 2022. In the second half of 2025 it stood at 15.96: 20.8% below that peak, but 45.8% above the first half of 2021. Excluding taxes, the rise is 80.6%. There is no open series that allows this price to be compared with the US and China using the same method."),
        { fig: "ene2-precio-industria", code: "E2" },
        { see: { es: "Análisis: el informe Draghi, dos años después, y el precio de la energía para la industria", en: "Analysis: the Draghi report two years on, and energy prices for industry" }, href: { es: "/es/notas/informe-draghi-dos-anos-despues/", en: "/en/notes/draghi-report-two-years-on/" } },
      ],
    },
    dentro: {
      lede: { es: "Entre los 27, el peso de las renovables va de casi dos tercios a una séptima parte, y la industria de unos países paga la luz a varias veces el precio de la de otros.", en: "Across the 27, the share of renewables ranges from almost two thirds to one seventh, and industry in some countries pays several times as much for power as in others." },
      body: [
        p("Cinco países superan ya el objetivo de renovables que la UE se ha fijado para 2030: Suecia (62,9 %), Finlandia (52,1 %), Dinamarca (46,5 %), Letonia (45,5 %) y Austria (43 %). En el otro extremo están Bélgica (14,3 %), Luxemburgo (14,7 %) e Irlanda (16,1 %). España, con un 25,4 %, está prácticamente en la media de la UE, y en 2004 estaba en el 8,3 %. Entre 2014 y 2024, Dinamarca es el país que más ha avanzado (17,2 puntos); Croacia, el único que ha retrocedido.",
          "Five countries already exceed the renewables target the EU has set for 2030: Sweden (62.9%), Finland (52.1%), Denmark (46.5%), Latvia (45.5%) and Austria (43%). At the other end are Belgium (14.3%), Luxembourg (14.7%) and Ireland (16.1%). Spain, at 25.4%, is practically at the EU average, up from 8.3% in 2004. Between 2014 and 2024, Denmark made the most progress (17.2 points); Croatia is the only country that went backwards."),
        { fig: "end1-renovables-paises", code: "D1" },
        p("Como contaba la nota N04 con la luz de los hogares, el precio de la electricidad cambia mucho de un país a otro. Para la industria, en el segundo semestre de 2025 iba de 6,74 céntimos por kWh en Finlandia y 8,52 en Suecia a 23,66 en Chipre y 21,87 en Irlanda. En Alemania, 19,22. Desde el primer semestre de 2021 se ha encarecido en los 27 países: en Hungría, un 119,9 %, más del doble; en Malta, solo un 0,9 %. España es el cuarto país más barato, con 11,91 céntimos, un 35,8 % más que en 2021.",
          "As note N04 showed for household electricity, power prices vary widely from country to country. For industry, in the second half of 2025 they ranged from 6.74 cents per kWh in Finland and 8.52 in Sweden to 23.66 in Cyprus and 21.87 in Ireland. In Germany, 19.22. Since the first half of 2021 they have risen in all 27 countries: in Hungary by 119.9%, more than doubling; in Malta by just 0.9%. Spain is the fourth cheapest country, at 11.91 cents, 35.8% more than in 2021."),
        { fig: "end2-precio-industria-paises", code: "D2" },
        p("Lo que no dicen estos datos. La energía primaria de G1 cuenta la energía antes de transformarla: una central térmica o nuclear pierde en forma de calor gran parte de lo que consume, y la eólica o la solar, no, así que pasar a renovables reduce la energía primaria aunque se use la misma electricidad. Las cuotas de renovables siguen las reglas de cálculo de la directiva, que no son las de G2. Los precios de E2 y D2 son medias para un tamaño de consumo, en euros corrientes: no dicen lo que paga cada empresa, que a menudo compra con contratos a largo plazo, ni lo que paga la industria de EE. UU. o China. Y ninguno de estos gráficos mide las emisiones, que se cuentan en el tema de libertades, bienestar y clima.",
          "What these data do not say. Primary energy in G1 counts energy before it is transformed: a thermal or nuclear plant loses much of what it consumes as heat, while wind and solar do not, so switching to renewables reduces primary energy even if the same electricity is used. Renewable shares follow the directive's accounting rules, which are not those of G2. The prices in E2 and D2 are averages for one consumption band, in current euros: they do not say what each company pays, often under long-term contracts, or what industry pays in the US or China. And none of these charts measures emissions, which are covered in the freedoms, well-being and climate theme."),
        { see: { es: "Libertades, bienestar y clima: las emisiones de la UE, EE. UU. y China", en: "Freedoms, well-being and climate: emissions in the EU, the US and China" }, href: { es: "/es/libertades/", en: "/en/freedoms/" } },
      ],
    },
  },
  notes: ["n04"],
  sources: [
    { name: "EUR-Lex: Directiva (UE) 2023/2413, que modifica la Directiva (UE) 2018/2001 relativa al fomento del uso de energía procedente de fuentes renovables", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32023L2413" },
  ],
};

export default theme;
