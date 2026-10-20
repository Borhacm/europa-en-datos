// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
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
  "cg3-saldo-bilateral": {
    renderer: "line",
    series: ["USA", "CHN"],
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
  "ce3-gas-origen": {
    renderer: "line",
    series: ["RU", "NO", "US", "DZ", "QA", "OTH"],
    seriesColors: { RU: "--ink", NO: "--ord-2", US: "--usa", DZ: "--focus", QA: "--ord-1", OTH: "--context-strong" },
    table: { rows: "series", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "ce4-coches-china": {
    renderer: "line",
    series: ["870380", "870360", "870340"],
    seriesColors: { "870380": "--chn", "870360": "--focus", "870340": "--context-strong" },
    table: { rows: "series", cols: "time", lastCols: 7 },
    domainMin: 0,
    digits: 2,
  },
  "cd1-comercio-intra": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "cd3-exposicion-eeuu": {
    renderer: "rank",
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

export default charts;
