// N07. Cómo se dibujan los gráficos de la nota.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "n07-defensa-paises": {
    renderer: "rank",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "n07-defensa-cambio": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
