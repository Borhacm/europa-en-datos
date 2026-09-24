// Tipos de los contenidos (temas y notas). Los archivos de content/ importan de aquí.

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
  /** Desempate si dos temas se publican el mismo día (menor = antes) */
  order?: number;
  /** Gráfico de apertura propio del tema, bajo el titular (ver OPENERS en views/Theme.astro) */
  opener?: "models-units";
  lenses?: Record<LensId, ThemeLens>;
  /** Notas de otros temas que adelantaron este (se listan en la página del tema) */
  notes?: string[];
}

export interface Note {
  /** Identificador del calendario editorial, en minúsculas: "n01" */
  id: string;
  /** Código visible y citable: "N01". Los gráficos se numeran N01-1, N01-2... */
  code: string;
  slug: Bi;
  title: Bi;
  dek: Bi;
  published: string;
  /** Mirada desde la que se cuenta */
  lens: LensId;
  /** Tema al que pertenece (id de un tema publicado) */
  theme: string;
  body: Block[];
}

/** Atajo para párrafos bilingües */
export const p = (es: string, en: string): Block => ({ p: { es, en } });
