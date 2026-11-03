// N11. Cómo se dibujan los gráficos de la nota.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "n11-frio-cambio": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "n11-frio-pobreza": {
    renderer: "dumbbell",
    pair: { dim: "rskpovth", from: "A_60", to: "B_60" },
    usesFocus: true,
    table: { rows: "geo", cols: "rskpovth" },
  },
};

export default charts;
