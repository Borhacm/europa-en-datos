// N08. Cómo se dibujan los gráficos de la nota.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "n08-paro-dos-medidas": {
    renderer: "dumbbell",
    pair: { dim: "measure", from: "tasa", to: "proporcion" },
    usesFocus: true,
    table: { rows: "geo", cols: "measure" },
  },
  "n08-jovenes-activos": {
    renderer: "rank",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
