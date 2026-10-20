// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "trg1-emisiones": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    digits: 0,
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "trg2-peso-transporte": {
    renderer: "dumbbell",
    extraGeos: ["USA", "CHN"],
    table: { rows: "geo", cols: "time" },
  },
  "tre1-reparto-viajeros": {
    renderer: "line",
    series: ["CAR", "BUS_TOT", "TRN"],
    seriesColors: { CAR: "--context-strong", BUS_TOT: "--ord-3", TRN: "--eu" },
    table: { rows: "series", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "tre2-combustible-nuevos": {
    renderer: "dumbbell",
    extraGeos: ["HYB", "PET", "ELC", "DIE", "PHEV"],
    seriesColors: { HYB: "--eu", PET: "--eu", ELC: "--eu", DIE: "--eu", PHEV: "--eu" },
    table: { rows: "geo", cols: "time" },
  },
  "trd1-tren-paises": {
    renderer: "rank",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "trd2-electricos-parque": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
