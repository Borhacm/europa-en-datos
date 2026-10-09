// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "vig1-precio-real": {
    renderer: "line",
    series: ["EA", "USA", "CHN"],
    seriesColors: { EA: "--eu" },
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "vig2-alquileres": {
    renderer: "line",
    series: ["EA", "USA"],
    seriesColors: { EA: "--eu" },
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "vie1-tenencia": {
    renderer: "rank",
    controls: [
      { dim: "tenure", default: "OWN", options: ["OWN", "OWN_L", "OWN_NL", "RENT_MKT", "RENT_FR"] },
      { dim: "time", default: "2025", options: ["2010", "2015", "2025"] },
    ],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "vie2-sobrecarga-tenencia": {
    renderer: "line",
    series: ["RENT_MKT", "RENT_FR", "OWN_L", "OWN_NL"],
    seriesColors: { RENT_MKT: "--eu", RENT_FR: "--ord-1", OWN_L: "--ord-2", OWN_NL: "--ord-3" },
    table: { rows: "series", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "vid1-sobrecarga": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2025", options: ["2015", "2020", "2025"] }],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "vid2-hacinamiento": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2025", options: ["2010", "2015", "2025"] }],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
};

export default charts;
