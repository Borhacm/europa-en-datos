// N05. Cómo se dibujan los gráficos de la nota.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "n05-electricos-cuota": {
    renderer: "rank",
    controls: [{ dim: "fuel", default: "ELC" }],
    extraGeos: ["NOR"],
    usesFocus: true,
    table: { rows: "geo", cols: "fuel" },
  },
  "n05-electricos-evolucion": {
    renderer: "line",
    series: ["EU27"],
    showContext: true,
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 7 },
    domainMin: 0,
  },
};

export default charts;
