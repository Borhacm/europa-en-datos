// N02. Cómo se dibujan los gráficos de la nota.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "n02-ia-frenos": {
    renderer: "paired",
    usesFocus: true,
    table: { rows: "geo", cols: "reason" },
  },
  "n02-ia-incertidumbre-legal": {
    renderer: "dumbbell",
    usesFocus: true,
    digits: 0,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
