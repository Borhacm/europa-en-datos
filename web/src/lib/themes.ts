// Registro de temas, notas y miradas. Todas las páginas salen de aquí.
// Cada tema vive en content/themes/<id>.ts y cada nota en content/notes/<id>.ts:
// para publicar uno nuevo basta con añadir su archivo.
import type { Lang } from "./i18n";
import type { Bi, Lens, LensId, Note, Theme } from "./content-types";

export type { Bi, Block, Lens, LensId, Note, Theme, ThemeLens } from "./content-types";

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

const byDate = <T extends { published?: string; order?: number; code: string }>(a: T, b: T) =>
  (a.published ?? "").localeCompare(b.published ?? "") || (a.order ?? 0) - (b.order ?? 0) || a.code.localeCompare(b.code);

const themeModules = import.meta.glob<{ default: Theme }>("../content/themes/*.ts", { eager: true });
const noteModules = import.meta.glob<{ default: Note }>("../content/notes/*.ts", { eager: true });

/** Temas en orden de publicación (el más antiguo primero) */
export const THEMES: Theme[] = Object.values(themeModules).map((m) => m.default).sort(byDate);
/** Notas, de la más reciente a la más antigua */
export const NOTES: Note[] = Object.values(noteModules).map((m) => m.default).sort(byDate).reverse();

export const published = () => THEMES.filter((t) => t.status === "published");
export const upcoming = () => THEMES.filter((t) => t.status === "upcoming");
export const themeById = (id: string) => THEMES.find((t) => t.id === id);
/** Notas de un tema: las suyas y las que el tema declara como relacionadas */
export const notesOf = (themeId: string) => {
  const extra = themeById(themeId)?.notes ?? [];
  return NOTES.filter((n) => n.theme === themeId || extra.includes(n.id));
};

export function figuresOf(theme: Theme, lens?: LensId) {
  const ids = lens ? [lens] : LENSES.map((l) => l.id);
  return ids.flatMap((id) =>
    (theme.lenses?.[id].body ?? []).filter((b): b is { fig: string; code: string } => "fig" in b).map((b) => ({ ...b, code: `${theme.code}-${b.code}`, lens: id })),
  );
}

export function noteFigures(note: Note) {
  return note.body.filter((b): b is { fig: string; code: string } => "fig" in b).map((b) => ({ ...b, code: `${note.code}-${b.code}` }));
}

export const lensById = (id: LensId) => LENSES.find((l) => l.id === id)!;

export const tr = (b: Bi, lang: Lang) => b[lang];
