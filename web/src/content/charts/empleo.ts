// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "emg1-paro-juvenil": {
    renderer: "line",
    series: ["EU27", "USA", "CHN"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  // Filas: grupos de edad. Punto hueco: EE. UU.; punto lleno: la UE
  "emg2-empleo-edades": {
    renderer: "dumbbell",
    pair: { dim: "bloc", from: "USA", to: "EU27" },
    extraGeos: ["Y15-24", "Y25-54", "Y55-64"],
    seriesColors: { "Y15-24": "--eu", "Y25-54": "--eu", "Y55-64": "--eu" },
    table: { rows: "geo", cols: "bloc" },
  },
  "eme1-objetivo-empleo": {
    renderer: "rank",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "eme2-motivos-temporales": {
    renderer: "paired",
    usesFocus: true,
    table: { rows: "geo", cols: "reason" },
  },
  "emd1-paro-juvenil-paises": {
    renderer: "rank",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "emd2-edad-emancipacion": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
