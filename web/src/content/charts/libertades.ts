// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "lg1-democracia": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
    digits: 2,
  },
  "lg2-esperanza-vida": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "lg3-co2-habitante": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "le1-emisiones-1990": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
    digits: 0,
  },
  "le2-gasto-social": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2022", options: ["2012", "2017", "2022"] }],
    extraGeos: ["USA"],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "ld1-democracia-ue": {
    renderer: "dumbbell",
    usesFocus: true,
    digits: 2,
    table: { rows: "geo", cols: "time" },
  },
  "ld2-pobreza": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2025", options: ["2015", "2020", "2025"] }],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "ld3-renovables": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2025", options: ["2005", "2015", "2025"] }],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
};

export default charts;
