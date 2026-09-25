// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "sag1-gasto-pib": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "sag2-gasto-habitante": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
    digits: 0,
  },
  "sae1-gasto-publico": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "sae2-pago-bolsillo": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2023", options: ["2003", "2013", "2023"] }],
    fixed: { measure: "share" },
    extraGeos: ["USA", "CHN"],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "sad1-medicos": {
    renderer: "rank",
    usesFocus: true,
    digits: 0,
    table: { rows: "geo", cols: "time" },
  },
  "sad2-necesidades-no-cubiertas": {
    renderer: "rank",
    controls: [
      { dim: "reason", default: "TXP_TFAR_WLIST" },
      { dim: "time", default: "2025", options: ["2015", "2020", "2025"] },
    ],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
};

export default charts;
