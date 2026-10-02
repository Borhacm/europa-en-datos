// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "dig1-efectivo-pib": {
    renderer: "line",
    series: ["EA", "USA", "CHN"],
    seriesColors: { EA: "--eu" },
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "dig2-pagos-sin-efectivo": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2024", options: ["2014", "2019", "2024"] }],
    extraGeos: ["USA", "CHN"],
    usesFocus: true,
    digits: 0,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "die1-pago-en-tienda": {
    renderer: "line",
    series: ["efectivo", "prefiere_tarjeta", "prefiere_efectivo"],
    seriesColors: { efectivo: "--eu", prefiere_tarjeta: "--context-strong", prefiere_efectivo: "--context" },
    table: { rows: "series", cols: "time" },
    domainMin: 0,
    digits: 0,
  },
  "die2-pagos-zona-euro": {
    renderer: "line",
    series: ["TOTL1", "CP0", "CT0", "DD"],
    seriesColors: { TOTL1: "--context-strong", CP0: "--eu", CT0: "--ord-2", DD: "--ord-1" },
    table: { rows: "series", cols: "time" },
    domainMin: 0,
  },
  "did1-pagos-tarjeta": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2025", options: ["2022", "2025"] }],
    usesFocus: true,
    digits: 0,
    table: { rows: "geo", cols: "time" },
  },
  "did2-retiradas-efectivo": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
