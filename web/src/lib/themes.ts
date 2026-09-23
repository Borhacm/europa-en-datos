// Registro de temas y miradas. Todas las páginas (temas, miradas, portada, metodología) salen de aquí.
// Las cifras de los textos están comprobadas contra data/charts.
import type { Lang } from "./i18n";

export type Bi = { es: string; en: string };
export type LensId = "gigantes" | "elige" | "dentro";
export type Block = { p: Bi } | { fig: string; code: string };

export interface Lens {
  id: LensId;
  slug: Bi;
  name: Bi;
  short: Bi;
  about: Bi;
}

export interface ThemeLens {
  lede: Bi;
  body: Block[];
}

export interface Theme {
  id: string;
  /** Prefijo de los códigos de gráfico (IA-G1, CO-G1...): identificador único y citable */
  code: string;
  slug: Bi;
  title: Bi;
  status: "published" | "upcoming";
  dek?: Bi;
  published?: string;
  lenses?: Record<LensId, ThemeLens>;
}

export const LENSES: Lens[] = [
  {
    id: "gigantes",
    slug: { es: "entre-dos-gigantes", en: "between-two-giants" },
    name: { es: "Entre dos gigantes", en: "Between two giants" },
    short: { es: "La UE frente a EE. UU. y China", en: "The EU against the US and China" },
    about: {
      es: "Cómo se compara la Unión Europea con Estados Unidos y China en cada tema.",
      en: "How the European Union compares with the United States and China on each theme.",
    },
  },
  {
    id: "elige",
    slug: { es: "pierde-o-elige", en: "losing-or-choosing" },
    name: { es: "¿Pierde Europa o elige?", en: "Is Europe losing, or choosing?" },
    short: { es: "Lo que el modelo europeo gana y lo que cede", en: "What the European model gains and what it gives up" },
    about: {
      es: "Dónde Europa se queda atrás y dónde ha decidido ir por otro camino, con el precio que eso tiene.",
      en: "Where Europe falls behind and where it has chosen a different path, and what that costs.",
    },
  },
  {
    id: "dentro",
    slug: { es: "europa-por-dentro", en: "europe-from-within" },
    name: { es: "Europa por dentro", en: "Europe from within" },
    short: { es: "Las diferencias entre los 27", en: "The differences among the 27" },
    about: {
      es: "Las diferencias entre los 27 países, y entre sus regiones, que se esconden detrás de la media europea.",
      en: "The differences between the 27 countries, and their regions, hidden behind the European average.",
    },
  },
];

const p = (es: string, en: string): Block => ({ p: { es, en } });

export const THEMES: Theme[] = [
  {
    id: "ia-digital",
    code: "IA",
    slug: { es: "ia-digital", en: "ai-digital" },
    title: { es: "IA y digital", en: "AI and digital" },
    status: "published",
    published: "2026-09-24",
    dek: {
      es: "La UE adopta la inteligencia artificial más rápido que nunca, pero casi toda la tecnología que usa se diseña fuera.",
      en: "The EU is adopting artificial intelligence faster than ever, but almost all the technology it uses is designed elsewhere.",
    },
    lenses: {
      gigantes: {
        lede: { es: "La brecha no está en el uso de la IA. Está en su producción.", en: "The gap is not in using AI. It is in making it." },
        body: [
          p("Estados Unidos dedica a la investigación el 3,4 % de su PIB. China, el 2,7 %, y sigue subiendo. La UE lleva una década en torno al 2 %, con un 2,1 % en 2024. Casi toda la diferencia está en lo que invierten las empresas: el 2,7 % del PIB en Estados Unidos, el 2,1 % en China y el 1,4 % en la UE.",
            "The United States spends 3.4% of its GDP on research. China spends 2.7%, and rising. The EU has hovered around 2% for a decade, reaching 2.1% in 2024. Almost all of the difference lies in business investment: 2.7% of GDP in the US, 2.1% in China and 1.4% in the EU."),
          { fig: "g1-inversion-id", code: "G1" },
          p("Esa inversión se nota en lo que se inventa. En solicitudes internacionales de patentes de IA, Estados Unidos y China presentan cada uno casi el triple que la UE. Por habitante, Estados Unidos patenta cuatro veces más IA que la UE, mientras que China y la UE están a la par.",
            "That investment shows up in what gets invented. In international AI patent applications, the US and China each file almost three times as many as the EU. Per person, the US patents four times more AI than the EU, while China and the EU are level."),
          { fig: "g2-patentes-ia", code: "G2" },
          p("En los modelos de IA que marcan el ritmo del sector, la distancia es todavía mayor. Desde 2023, las organizaciones de la UE han participado en 18 modelos destacados. Las de Estados Unidos, en 250. Las de China, en 120.",
            "In the AI models that set the pace of the field, the distance is even wider. Since 2023, EU organisations have taken part in 18 notable models. US organisations, in 250. Chinese ones, in 120."),
          { fig: "g3-modelos-ia", code: "G3" },
        ],
      },
      elige: {
        lede: { es: "Se suele decir que Europa va más despacio porque prefiere proteger. Los datos lo matizan.", en: "The usual story says Europe moves slower because it prefers to protect. The data adds nuance." },
        body: [
          p("En 2025, Eurostat preguntó a quienes no usan IA generativa por qué no lo hacen. El 64 % respondió que no la necesita. Solo el 7 % habló de privacidad o seguridad. En España los motivos cambian: pesa más no saber usarla (28 %) o no saber que existía (25 %). Más que una elección prudente, parece una brecha de conocimiento.",
            "In 2025, Eurostat asked people who do not use generative AI why not. 64% said they do not need it. Only 7% mentioned privacy or security. In Spain the reasons shift: not knowing how to use it (28%) or not knowing it existed (25%) weigh more. It looks less like a cautious choice and more like a knowledge gap."),
          { fig: "e1-motivos-no-ia-generativa", code: "E1" },
          p("Donde sí hay una elección de fondo es en cómo se gobierna internet. China adopta la tecnología con filtrado y censura del Estado. La UE, en conjunto, protege más la libertad en la red que Estados Unidos, que ha retrocedido desde 2023. Dentro de la Unión también hay diferencias: el gráfico muestra el país con más control en cada año.",
            "Where there is a deeper choice is in how the internet is governed. China adopts technology under state filtering and censorship. The EU as a whole protects online freedom more than the United States, which has slipped since 2023. There are differences within the Union too: the chart shows the most controlled member state each year."),
          { fig: "e2-control-internet", code: "E2" },
          p("Hay otra decisión que distingue a Europa: la mayoría de sus modelos destacados se publican con pesos abiertos, que cualquiera puede descargar y adaptar. Pero con tan pocos modelos, es más una señal que una estrategia.",
            "One more decision sets Europe apart: most of its notable models are released with open weights that anyone can download and adapt. But with so few models, it is more of a signal than a strategy."),
          { fig: "e3-modelos-abiertos", code: "E3" },
        ],
      },
      dentro: {
        lede: { es: "Hablar de Europa en conjunto esconde distancias enormes entre sus países.", en: "Talking about Europe as a whole hides huge distances between its countries." },
        body: [
          p("En Dinamarca, el 42 % de las empresas ya usa alguna tecnología de IA. En Rumanía, el 5 %. La media de la UE se ha multiplicado por 2,6 desde 2021, hasta el 20 %, y España está justo en la media.",
            "In Denmark, 42% of enterprises already use some AI technology. In Romania, 5%. The EU average has grown 2.6 times since 2021, to 20%, and Spain sits right on the average."),
          { fig: "d1-empresas-ia", code: "D1" },
          p("Dentro de cada país, la IA se concentra en torno a la capital. Pasa en casi todos los países que publican datos por regiones. En España, la Comunidad de Madrid (27 %) multiplica por ocho a Melilla (3,5 %).",
            "Within each country, AI clusters around the capital. It happens in almost every country that publishes regional data. In Spain, the Madrid region (27%) is eight times Melilla (3.5%)."),
          { fig: "d2-mapa-regional-ia", code: "D2" },
          p("Entre las personas, el patrón se repite. Uno de cada tres europeos usó IA generativa en 2025. Entre los jóvenes de 16 a 24 años, casi dos de cada tres. España está por encima de la media, con un 38 %.",
            "Among people, the pattern repeats. One in three Europeans used generative AI in 2025. Among 16 to 24 year olds, almost two in three. Spain is above average, at 38%."),
          { fig: "d3-ia-generativa", code: "D3" },
          p("La base de todo son las competencias digitales, y ahí la UE está lejos de su objetivo: el 60 % de la población tiene al menos competencias básicas, frente al 80 % que se ha propuesto para 2030.",
            "Digital skills are the foundation, and there the EU is far from its goal: 60% of people have at least basic skills, against the 80% it has set for 2030."),
          { fig: "d4-competencias-digitales", code: "D4" },
        ],
      },
    },
  },
  {
    id: "comercio",
    code: "CO",
    slug: { es: "comercio", en: "trade" },
    title: { es: "Comercio y dependencias", en: "Trade and dependencies" },
    status: "published",
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
  },
  { id: "productividad", code: "PR", slug: { es: "productividad", en: "productivity" }, title: { es: "Productividad e I+D", en: "Productivity and R&D" }, status: "upcoming" },
  { id: "libertades", code: "LI", slug: { es: "libertades", en: "freedoms" }, title: { es: "Libertades, bienestar y clima", en: "Freedoms, well-being and climate" }, status: "upcoming" },
];

export const published = () => THEMES.filter((t) => t.status === "published");
export const upcoming = () => THEMES.filter((t) => t.status === "upcoming");

export function figuresOf(theme: Theme, lens?: LensId) {
  const ids = lens ? [lens] : LENSES.map((l) => l.id);
  return ids.flatMap((id) =>
    (theme.lenses?.[id].body ?? []).filter((b): b is { fig: string; code: string } => "fig" in b).map((b) => ({ ...b, code: `${theme.code}-${b.code}`, lens: id })),
  );
}

export const lensById = (id: LensId) => LENSES.find((l) => l.id === id)!;

export const tr = (b: Bi, lang: Lang) => b[lang];
