// Cómo se dibuja cada gráfico. Lo comparten el servidor (tabla accesible) y el navegador (gráfico).

export type Renderer = "line" | "rank" | "paired" | "dumbbell" | "stack" | "map";

export interface Control {
  dim: string;
  default: string;
  /** Solo estas opciones, en este orden (por defecto: todas las de `dimensions`) */
  options?: string[];
}

export interface ChartConfig {
  renderer: Renderer;
  controls?: Control[];
  /** Filtro fijo, además de los controles */
  fixed?: Record<string, string>;
  /** Series en color, en orden fijo. El resto se dibuja como contexto gris (o se oculta). */
  series?: string[];
  showContext?: boolean;
  /** Usa el país elegido por el lector ("Destacar un país") */
  usesFocus?: boolean;
  /** Tabla accesible: pivot de filas x columnas */
  table: { rows: string; cols: string; lastCols?: number };
  /** Dimensión alternativa del valor (p. ej. per_million) según un control */
  valueFrom?: { control: string; map: Record<string, string> };
  yLabel?: { es: string; en: string };
  /** Decimales en etiquetas y tooltips (por defecto: 1) */
  digits?: number;
  domainMin?: number;
}

export const CHARTS: Record<string, ChartConfig> = {
  "g1-inversion-id": {
    renderer: "line",
    controls: [{ dim: "measure", default: "total" }],
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
    digits: 2,
  },
  "g2-patentes-ia": {
    renderer: "line",
    controls: [{ dim: "scale", default: "total", options: ["total", "per_million"] }],
    valueFrom: { control: "scale", map: { total: "value", per_million: "per_million" } },
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "g3-modelos-ia": {
    renderer: "line",
    controls: [{ dim: "rule", default: "participa" }],
    series: ["USA", "CHN", "EU27"],
    showContext: true,
    table: { rows: "geo", cols: "time", lastCols: 8 },
    domainMin: 0,
    digits: 0,
  },
  "e1-motivos-no-ia-generativa": {
    renderer: "paired",
    usesFocus: true,
    table: { rows: "geo", cols: "reason" },
  },
  "e2-control-internet": {
    renderer: "line",
    controls: [{ dim: "measure", default: "v2smgovfilprc" }],
    series: ["USA", "CHN", "EU27"],
    fixed: {},
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "e3-modelos-abiertos": {
    renderer: "stack",
    series: ["USA", "CHN", "EU27", "GBR"],
    table: { rows: "geo", cols: "access" },
  },
  "d1-empresas-ia": {
    renderer: "dumbbell",
    controls: [{ dim: "size", default: "GE10" }],
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "d2-mapa-regional-ia": {
    renderer: "map",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "d3-ia-generativa": {
    renderer: "rank",
    controls: [
      { dim: "age", default: "IND_TOTAL" },
      { dim: "use", default: "I_IUAI" },
    ],
    usesFocus: true,
    table: { rows: "geo", cols: "age" },
  },
  "d4-competencias-digitales": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2025", options: ["2021", "2023", "2025"] }],
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },

  // ---------- Comercio y dependencias ----------
  "cg1-cuota-mundial": {
    renderer: "line",
    controls: [{ dim: "flow", default: "exportaciones" }],
    series: ["USA", "CHN", "EU27"],
    showContext: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "cg2-saldo-comercial": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    showContext: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
    digits: 0,
  },
  "ce1-importaciones-origen": {
    renderer: "line",
    controls: [{ dim: "product", default: "TOTAL" }],
    series: ["USA", "CHN"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "ce2-exportaciones-destino": {
    renderer: "line",
    controls: [{ dim: "product", default: "TOTAL" }],
    series: ["USA", "CHN"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "cd1-comercio-intra": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "cd2-dependencia-energetica": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2024", options: ["2004", "2014", "2024"] }],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
};

/** Etiquetas de los controles que no vienen en el JSON */
export const EXTRA_DIMENSIONS: Record<string, Record<string, { es: string; en: string }>> = {
  scale: {
    total: { es: "Total", en: "Total" },
    per_million: { es: "Por millón de habitantes", en: "Per million people" },
  },
  time: {
    "2021": { es: "2021", en: "2021" },
    "2023": { es: "2023", en: "2023" },
    "2025": { es: "2025", en: "2025" },
  },
};
