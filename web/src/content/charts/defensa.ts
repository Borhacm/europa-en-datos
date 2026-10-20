// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "dfg1-gasto-dolares": {
    renderer: "line",
    series: ["USA", "EU27", "CHN", "RUS"],
    seriesColors: { RUS: "--context-strong" },
    digits: 0,
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "dfg2-exportaciones-armas": {
    renderer: "dumbbell",
    extraGeos: ["USA", "RUS", "CHN"],
    table: { rows: "geo", cols: "time" },
  },
  "dfe1-importaciones-armas": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "dfe2-composicion-gasto": {
    renderer: "line",
    series: ["D1", "P2", "P51G", "TRANSF"],
    seriesColors: { D1: "--context-strong", P2: "--ord-3", P51G: "--eu", TRANSF: "--ord-2" },
    table: { rows: "series", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "dfd1-gasto-habitante": {
    renderer: "rank",
    extraGeos: ["USA"],
    usesFocus: true,
    digits: 0,
    table: { rows: "geo", cols: "time" },
  },
  "dfd2-inversion-paises": {
    renderer: "rank",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
