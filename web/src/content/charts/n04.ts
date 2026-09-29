// N04. Cómo se dibujan los gráficos de la nota.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "n04-luz-precio": {
    renderer: "rank",
    controls: [{ dim: "tax", default: "I_TAX" }],
    usesFocus: true,
    table: { rows: "geo", cols: "tax" },
  },
  "n04-luz-cambio": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
