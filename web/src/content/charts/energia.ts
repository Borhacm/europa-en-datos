// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "eng1-consumo-habitante": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    showContext: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
    digits: 0,
  },
  "eng2-mezcla-electrica": {
    renderer: "line",
    controls: [{ dim: "source", default: "fossil" }],
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "ene1-renovables-ue": {
    renderer: "line",
    series: ["REN", "REN_ELC", "REN_HEAT_CL", "REN_TRA"],
    seriesColors: { REN: "--eu", REN_ELC: "--ord-1", REN_HEAT_CL: "--ord-2", REN_TRA: "--ord-3" },
    table: { rows: "series", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "ene2-precio-industria": {
    renderer: "line",
    series: ["X_VAT", "X_TAX"],
    seriesColors: { X_VAT: "--eu", X_TAX: "--ord-2" },
    table: { rows: "series", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "end1-renovables-paises": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2024", options: ["2004", "2014", "2024"] }],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "end2-precio-industria-paises": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
