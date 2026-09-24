// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "pg1-peso-pib-mundial": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    context: ["JPN"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "pg2-productividad-hora": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    context: ["JPN"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "pe1-brecha-ee-uu": {
    renderer: "line",
    series: ["hora", "habitante"],
    seriesColors: { hora: "--eu", habitante: "--context-strong" },
    table: { rows: "series", cols: "time", lastCols: 6 },
  },
  "pe2-horas-trabajadas": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2025", options: ["2015", "2020", "2025"] }],
    extraGeos: ["USA"],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "pd1-convergencia": {
    renderer: "dumbbell",
    usesFocus: true,
    digits: 0,
    table: { rows: "geo", cols: "time" },
  },
  "pd2-mapa-renta": {
    renderer: "map",
    usesFocus: true,
    digits: 0,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
