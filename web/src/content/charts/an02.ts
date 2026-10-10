// AN02. Gráficos nuevos del análisis; el resto se reutiliza de N03, productividad e IA.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "an02-luz-industria": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2025-S2", options: ["2019-S2", "2025-S2"] }],
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "an02-defensa": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
};

export default charts;
