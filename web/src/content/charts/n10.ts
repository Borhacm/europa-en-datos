// N10. Cómo se dibujan los gráficos de la nota.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "n10-nacidos-ue-fuera": {
    renderer: "dumbbell",
    pair: { dim: "c_birth", from: "EU27_2020_FOR", to: "NEU27_2020_FOR" },
    usesFocus: true,
    table: { rows: "geo", cols: "c_birth" },
  },
  // Dos series de un mismo bloque: nacidos en otro país de la UE y nacidos fuera de la UE
  "n10-nacidos-ue-evolucion": {
    renderer: "line",
    series: ["EU27_2020_FOR", "NEU27_2020_FOR"],
    seriesColors: { EU27_2020_FOR: "--context-strong", NEU27_2020_FOR: "--eu" },
    table: { rows: "series", cols: "time" },
    domainMin: 0,
  },
};

export default charts;
