// N03. Cómo se dibujan los gráficos de la nota.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "n03-crecimiento": {
    renderer: "line",
    series: ["USA", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    digits: 0,
  },
  "n03-inversion": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
};

export default charts;
