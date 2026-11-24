// N12. Cómo se dibujan los gráficos de la nota.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "n12-universitarios-paises": {
    renderer: "rank",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "n12-universitarios-sexo": {
    renderer: "dumbbell",
    pair: { dim: "sex", from: "M", to: "F" },
    usesFocus: true,
    table: { rows: "geo", cols: "sex" },
  },
};

export default charts;
