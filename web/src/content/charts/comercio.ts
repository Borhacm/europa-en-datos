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

export default charts;
