export type Lang = "es" | "en";
export const LANGS: Lang[] = ["es", "en"];

export const ui = {
  es: {
    siteName: "Europa en datos",
    siteDescription:
      "La Unión Europea frente a Estados Unidos y China, y las diferencias entre sus 27 países, contadas con datos abiertos oficiales.",
    navThemes: "Temas",
    navLenses: "Miradas",
    navMethod: "Metodología",
    otherLang: "English",
    skip: "Saltar al contenido",
    source: "Fuente",
    license: "Licencia",
    notes: "Notas",
    showTable: "Ver los datos en una tabla",
    download: "Descargar los datos (JSON)",
    retrieved: "Datos descargados el",
    yourCountry: "Destacar un país",
    none: "Ninguno",
    lens: "Mirada",
    loading: "Cargando el gráfico",
    loadError: "No se ha podido cargar el gráfico. Los datos siguen disponibles en la tabla.",
    footerIndependent:
      "Proyecto independiente de Bocal. No es una publicación oficial de la Unión Europea ni de ninguna institución.",
    footerData: "Datos abiertos de Eurostat, OCDE, Banco Mundial, la OIT, Epoch AI y V-Dem.",
    comingSoon: "En preparación",
    table: { country: "País", year: "Año", value: "Valor" },
  },
  en: {
    siteName: "Europe in data",
    siteDescription:
      "The European Union against the United States and China, and the differences between its 27 countries, told with official open data.",
    navThemes: "Themes",
    navLenses: "Lenses",
    navMethod: "Methodology",
    otherLang: "Español",
    skip: "Skip to content",
    source: "Source",
    license: "Licence",
    notes: "Notes",
    showTable: "Show the data as a table",
    download: "Download the data (JSON)",
    retrieved: "Data retrieved on",
    yourCountry: "Highlight a country",
    none: "None",
    lens: "Lens",
    loading: "Loading the chart",
    loadError: "The chart could not be loaded. The data is still available in the table.",
    footerIndependent:
      "An independent project by Bocal. Not an official publication of the European Union or any institution.",
    footerData: "Open data from Eurostat, the OECD, the World Bank, the ILO, Epoch AI and V-Dem.",
    comingSoon: "In preparation",
    table: { country: "Country", year: "Year", value: "Value" },
  },
} as const;

export type Bi = { es: string; en: string };

export const paths = {
  home: { es: "/es/", en: "/en/" },
  themes: { es: "/es/temas/", en: "/en/themes/" },
  lenses: { es: "/es/miradas/", en: "/en/lenses/" },
  method: { es: "/es/metodologia/", en: "/en/methodology/" },
} as const;

export type Section = "home" | "themes" | "lenses" | "method";

/** Rutas de un tema o de una mirada en los dos idiomas, a partir de su slug. */
export const themePath = (slug: Bi): Bi => ({ es: `/es/${slug.es}/`, en: `/en/${slug.en}/` });
export const lensPath = (slug: Bi): Bi => ({ es: `/es/miradas/${slug.es}/`, en: `/en/lenses/${slug.en}/` });

export function formatNumber(value: number, lang: Lang, digits = 1): string {
  return new Intl.NumberFormat(lang === "es" ? "es-ES" : "en-GB", {
    maximumFractionDigits: digits,
  }).format(value);
}

export function formatDate(iso: string, lang: Lang): string {
  return new Intl.DateTimeFormat(lang === "es" ? "es-ES" : "en-GB", {
    day: "numeric",
    month: "long",
    year: "numeric",
  }).format(new Date(iso));
}
