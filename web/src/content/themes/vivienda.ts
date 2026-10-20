import { p, type Theme } from "../../lib/content-types";

// Cifras comprobadas contra data/charts/vi*.json (BIS, OCDE y Eurostat) y n01-vivienda-precios.json.
// Completado el 20/10/2026 (P2, ver editorial/registro/vivienda.md): ficha de la Directiva 2014/17/UE, límites
// y sin repetir la cifra de N01 (precios nominales 2015-2025), que se enlaza.
const theme: Theme = {
  id: "vivienda",
  code: "VI",
  slug: { es: "vivienda", en: "housing" },
  title: { es: "Vivienda y coste de vida", en: "Housing and the cost of living" },
  status: "published",
  order: 7,
  published: "2026-10-09",
  updated: "2026-10-20",
  dek: {
    es: "La vivienda ha subido menos en la zona del euro que en EE. UU., y los alquileres también. Casi siete de cada diez europeos viven en una casa propia, pero quien alquila a precio de mercado carga con mucho más gasto, y entre países las diferencias en coste y espacio son enormes.",
    en: "Housing has risen less in the euro area than in the US, and so have rents. Almost seven in ten Europeans live in a home they own, but those renting at market prices bear far higher costs, and the gaps between countries in cost and space are huge.",
  },
  lenses: {
    gigantes: {
      lede: { es: "Descontada la inflación, la vivienda se ha encarecido mucho más en EE. UU. que en la zona del euro. En China, se ha abaratado.", en: "After inflation, housing has become far more expensive in the US than in the euro area. In China, it has become cheaper." },
      body: [
        p("En 2025, el precio real de la vivienda en la zona del euro era un 11 % más alto que en 2010. En EE. UU., un 58,5 % más alto, y en China, un 10,5 % más bajo. Los tres bloques han seguido caminos distintos: en la zona del euro, los precios reales cayeron hasta 2013 y tocaron techo en 2021; en EE. UU. se hundieron tras la crisis de 2008, tocaron fondo en 2011 y en 2024 marcaron su máximo; en China alcanzaron su máximo en 2021 y en 2025 estaban en el nivel más bajo de toda la serie, que empieza en 2006.",
          "In 2025, real house prices in the euro area were 11% higher than in 2010. In the US, 58.5% higher, and in China, 10.5% lower. The three blocs have taken different paths: in the euro area, real prices fell until 2013 and peaked in 2021; in the US they collapsed after the 2008 crisis, bottomed out in 2011 and hit their peak in 2024; in China they peaked in 2021 and in 2025 were at the lowest level of the whole series, which starts in 2006."),
        { fig: "vig1-precio-real", code: "G1" },
        p("Son precios descontada la inflación; sin descontarla, la subida en la UE se cuenta en la nota N01. Los alquileres también se han disparado más al otro lado del Atlántico: entre 2015 y 2024 subieron un 46,9 % en EE. UU. y un 15,5 % en la zona del euro, en precios corrientes.",
          "These are prices after inflation; the rise in the EU without adjusting for it is covered in note N01. Rents have also climbed much more across the Atlantic: between 2015 and 2024 they rose 46.9% in the US and 15.5% in the euro area, at current prices."),
        { see: { es: "Nota: cuánto ha subido la vivienda en cada país de la UE desde 2015", en: "Note: how much housing has risen in each EU country since 2015" }, href: { es: "/es/notas/vivienda-desde-2015/", en: "/en/notes/housing-since-2015/" } },
        { fig: "vig2-alquileres", code: "G2" },
      ],
    },
    elige: {
      lede: { es: "Europa es, sobre todo, un continente de propietarios. Quien alquila a precio de mercado lo paga.", en: "Europe is, above all, a continent of homeowners. Those who rent at market prices pay for it." },
      body: [
        p("En 2025, el 68,5 % de la población de la UE vivía en una casa propia, algo menos que en 2010 (70,7 %). Las diferencias son de modelo. En Eslovaquia, Rumanía y Croacia son propietarios más del 91 %, y en Rumanía casi todos sin hipoteca. En el otro extremo, Alemania es el único país donde los propietarios no llegan a la mitad (47,2 %), seguida de Austria (54,2 %) y Dinamarca (58,4 %). En los Países Bajos, el 57,9 % de la población vive en una casa propia con hipoteca. España, con un 73,6 %, está por encima de la media, pero los propietarios han bajado desde el 79,8 % de 2010, y los inquilinos a precio de mercado han pasado del 11,9 % al 17,4 %.",
          "In 2025, 68.5% of the EU population lived in a home they owned, slightly fewer than in 2010 (70.7%). The differences reflect different models. In Slovakia, Romania and Croatia more than 91% are owners, and in Romania almost all of them without a mortgage. At the other end, Germany is the only country where owners are fewer than half (47.2%), followed by Austria (54.2%) and Denmark (58.4%). In the Netherlands, 57.9% of the population lives in an owned home with a mortgage. Spain, at 73.6%, is above average, but ownership has fallen from 79.8% in 2010, and tenants at market rent have risen from 11.9% to 17.4%."),
        { fig: "vie1-tenencia", code: "E1" },
        p("Ser propietario o inquilino cambia mucho lo que pesa la vivienda en el bolsillo. En 2025, el 18,6 % de los europeos que alquilan a precio de mercado vivía en un hogar que dedica más del 40 % de sus ingresos a la vivienda. Entre los propietarios con hipoteca, el 5 %, y entre los que ya no la tienen, el 3,8 %. Para los inquilinos a precio de mercado, la proporción ha bajado desde el máximo del 27,1 % en 2014, pero sigue siendo casi cuatro veces la de los propietarios con hipoteca.",
          "Owning or renting makes a big difference to how much housing weighs on household budgets. In 2025, 18.6% of Europeans renting at market prices lived in a household spending more than 40% of its income on housing. Among owners with a mortgage, 5%, and among those without one, 3.8%. For market-rent tenants the share has fallen from a peak of 27.1% in 2014, but it is still almost four times that of owners with a mortgage."),
        { fig: "vie2-sobrecarga-tenencia", code: "E2" },
        { h: { es: "La ficha: qué protege la ley europea a quien pide una hipoteca", en: "The policy card: what EU law protects for mortgage borrowers" }, id: "ficha-hipotecas" },
        p("La vivienda es sobre todo competencia de cada país, pero la hipoteca no. La Directiva 2014/17/UE, de 4 de febrero de 2014, aprobada tras la crisis financiera, obliga al banco a evaluar en profundidad la solvencia de quien pide el préstamo antes de firmarlo, y esa evaluación no puede basarse sobre todo en el valor de la casa ni en la idea de que se revalorizará. El cliente debe recibir antes una ficha europea de información normalizada (FEIN) para comparar ofertas, y tiene derecho a devolver el préstamo antes de tiempo, total o parcialmente; el banco puede cobrar una compensación, pero no una penalización. La directiva pide también que los bancos sean «razonablemente tolerantes» antes de ejecutar una hipoteca. No regula los alquileres, que dependen de cada país.",
          "Housing is mostly up to each country, but mortgages are not. Directive 2014/17/EU of 4 February 2014, adopted after the financial crisis, requires lenders to assess the borrower's creditworthiness thoroughly before signing, and that assessment cannot rely mainly on the value of the home or on the assumption that it will rise. Borrowers must first receive a European Standardised Information Sheet (ESIS) to compare offers, and they have the right to repay the loan early, in full or in part; the lender may charge compensation, but not a penalty. The directive also asks lenders to be \"reasonably forbearing\" before foreclosing. It does not regulate rents, which depend on each country."),
      ],
    },
    dentro: {
      lede: { es: "Detrás de la media europea hay países donde la vivienda ahoga y otros donde falta espacio.", en: "Behind the European average are countries where housing costs crush households and others where space runs short." },
      body: [
        p("En 2025, el 7,7 % de la población de la UE vivía en un hogar que dedica más del 40 % de sus ingresos a la vivienda, frente al 11,2 % de 2015. Grecia es el caso extremo: el 26,4 %, aunque en 2015 era el 45,5 %. Le siguen Dinamarca, con un dato afectado por un cambio de método, y Alemania (11,2 %). En Chipre es el 2,4 %, y en Croacia, el 3,2 %. España, con un 7,2 %, es el octavo país con la proporción más alta.",
          "In 2025, 7.7% of the EU population lived in a household spending more than 40% of its income on housing, down from 11.2% in 2015. Greece is the extreme case: 26.4%, although in 2015 it was 45.5%. It is followed by Denmark, whose figure is affected by a change in method, and Germany (11.2%). In Cyprus it is 2.4%, and in Croatia, 3.2%. Spain, at 7.2%, has the eighth highest share."),
        { fig: "vid1-sobrecarga", code: "D1" },
        p("El otro problema es el espacio. En 2025, el 16,8 % de los europeos vivía en una casa con menos habitaciones de las que necesita su hogar. En Rumanía era el 40,4 %, y en Letonia, el 38,9 %; en Chipre, el 2,2 %, y en los Países Bajos, el 4,1 %. Ser propietario no evita el hacinamiento: de los ocho países con más propietarios, siete tienen más hacinamiento que la media de la UE; la excepción es Hungría. En España está por debajo de la media, pero ha subido del 5 % en 2010 al 9,5 %.",
          "The other problem is space. In 2025, 16.8% of Europeans lived in a home with fewer rooms than their household needs. In Romania it was 40.4%, and in Latvia, 38.9%; in Cyprus, 2.2%, and in the Netherlands, 4.1%. Owning does not prevent overcrowding: of the eight countries with the most homeowners, seven have more overcrowding than the EU average; the exception is Hungary. In Spain it is below average but has risen from 5% in 2010 to 9.5%."),
        { fig: "vid2-hacinamiento", code: "D2" },
        p("Lo que no dicen estos datos. Los precios de G1 son de la zona del euro, no de los 27, y cada país los mide a su manera, así que la comparación vale más para la evolución que para el nivel. En la sobrecarga, el gasto de los propietarios que cuenta Eurostat son los intereses de la hipoteca, descontadas las deducciones fiscales, además de los gastos de la casa; la definición no incluye la devolución del préstamo entre esos gastos. El hacinamiento usa una regla fija de habitaciones por persona que no tiene en cuenta el tamaño de la casa. Y ninguno de estos gráficos dice cuántas viviendas faltan o sobran en cada país.",
          "What these data do not say. The prices in G1 are for the euro area, not the 27, and each country measures them in its own way, so the comparison works better for trends than for levels. In the overburden rate, the owner costs Eurostat counts are mortgage interest, net of tax relief, plus the running costs of the home; the definition does not list loan repayments among those costs. Overcrowding uses a fixed rule of rooms per person that ignores the size of the home. And none of these charts says how many homes are missing or surplus in each country."),
      ],
    },
  },
  notes: ["n01"],
  sources: [
    { name: "Eurostat, glosario: tasa de sobrecarga del coste de la vivienda", url: "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Housing_cost_overburden_rate" },
    { name: "EUR-Lex: Directiva 2014/17/UE, sobre los contratos de crédito celebrados con los consumidores para bienes inmuebles de uso residencial", url: "https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32014L0017" },
  ],
};

export default theme;
