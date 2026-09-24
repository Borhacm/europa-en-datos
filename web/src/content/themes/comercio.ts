import { p, type Theme } from "../../lib/content-types";

const theme: Theme = {
  id: "comercio",
  code: "CO",
  slug: { es: "comercio", en: "trade" },
  title: { es: "Comercio y dependencias", en: "Trade and dependencies" },
  status: "published",
  order: 2,
  published: "2026-09-24",
  dek: {
    es: "La UE fue durante décadas la mayor potencia comercial del mundo. China la ha adelantado, y Europa depende cada vez más de otros para comprar y para vender.",
    en: "For decades the EU was the world's largest trading power. China has overtaken it, and Europe increasingly depends on others to buy and to sell.",
  },
  lenses: {
    gigantes: {
      lede: { es: "El comercio mundial ha cambiado de centro de gravedad en dos décadas.", en: "World trade has shifted its centre of gravity in two decades." },
      body: [
        p("En 2002, la UE aportaba el 18,9 % de las exportaciones mundiales de bienes y China, el 6,5 %. China supera a la UE desde 2015, y en 2024 ya exportaba el 18,7 % del total mundial, frente al 14,7 % de la UE. Estados Unidos es sobre todo un gran comprador: absorbe más del 16 % de las importaciones del mundo.",
          "In 2002, the EU supplied 18.9% of world goods exports and China 6.5%. China has exported more than the EU since 2015, and by 2024 it accounted for 18.7% of the world total, against the EU's 14.7%. The United States is above all a big buyer: it takes in more than 16% of the world's imports."),
        { fig: "cg1-cuota-mundial", code: "G1" },
        p("Las cuentas lo resumen. En 2024, China vendió al mundo 916.000 millones de euros más de lo que compró. Estados Unidos, al revés, compró 1,19 billones más de lo que vendió. La UE, con un superávit de 133.000 millones, queda en medio.",
          "The accounts sum it up. In 2024, China sold the world 916 billion euros more than it bought. The United States, the other way round, bought 1.19 trillion more than it sold. The EU, with a surplus of 133 billion, sits in between."),
        { fig: "cg2-saldo-comercial", code: "G2" },
      ],
    },
    elige: {
      lede: { es: "Abrirse al mundo fue una decisión europea. El precio es depender de dos socios que ya no se entienden.", en: "Opening up to the world was a European choice. The price is depending on two partners who no longer get along." },
      body: [
        p("En 2002, China suministraba el 7,8 % de lo que la UE compraba fuera de la Unión. En 2025, el 22,6 %. En maquinaria y equipos de transporte, donde entran los paneles solares, las baterías o la electrónica, llega al 35,8 %, tras un máximo del 40,6 % en 2022.",
          "In 2002, China supplied 7.8% of what the EU bought from outside the Union. In 2025, 22.6%. In machinery and transport equipment, which includes solar panels, batteries and electronics, it reaches 35.8%, after peaking at 40.6% in 2022."),
        { fig: "ce1-importaciones-origen", code: "E1" },
        p("Para vender ocurre lo contrario. Estados Unidos compra el 21 % de lo que la UE exporta fuera de la Unión, casi tres veces más que China (7,5 %). Europa compra a un gigante y vende al otro, y eso la deja expuesta a los aranceles de uno y a la competencia del otro.",
          "Selling works the other way round. The United States buys 21% of what the EU exports outside the Union, almost three times as much as China (7.5%). Europe buys from one giant and sells to the other, which leaves it exposed to the tariffs of one and the competition of the other."),
        { fig: "ce2-exportaciones-destino", code: "E2" },
      ],
    },
    dentro: {
      lede: { es: "El mercado único sigue siendo el gran socio de cada país. Las dependencias, en cambio, se reparten de forma muy desigual.", en: "The single market is still every country's main partner. Dependencies, however, are spread very unevenly." },
      body: [
        p("De cada diez euros que exportan los países de la UE, seis van a otros países de la Unión, igual que en 2004. Eslovaquia y Chequia venden en la UE casi el 80 % de lo que exportan. En el otro extremo, Irlanda y Chipre, con grandes filiales de multinacionales, miran mucho más fuera. España envía a la UE el 62 %.",
          "Of every ten euros EU countries export, six go to other EU countries, just as in 2004. Slovakia and Czechia sell almost 80% of their exports within the EU. At the other end, Ireland and Cyprus, home to large multinational subsidiaries, look much further afield. Spain sends 62% to the EU."),
        { fig: "cd1-comercio-intra", code: "D1" },
        p("La energía es la dependencia más visible. La UE importa el 57 % de la energía que usa. Malta y Luxemburgo importan más del 90 %; España, el 69 %. Solo Estonia, gracias a su esquisto bituminoso, se acerca a la autosuficiencia.",
          "Energy is the most visible dependency. The EU imports 57% of the energy it uses. Malta and Luxembourg import more than 90%; Spain, 69%. Only Estonia, thanks to its oil shale, comes close to self-sufficiency."),
        { fig: "cd2-dependencia-energetica", code: "D2" },
      ],
    },
  },
};

export default theme;
