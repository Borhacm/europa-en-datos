// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "fpg1-deficit": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "fpg2-intereses": {
    renderer: "dumbbell",
    pair: { dim: "measure", from: "primario", to: "total" },
    extraGeos: ["USA", "CHN"],
    table: { rows: "geo", cols: "measure" },
  },
  "fpe1-impuestos": {
    renderer: "dumbbell",
    pair: { dim: "bloc", from: "EU27", to: "USA" },
    extraGeos: ["T_1000", "T_2000", "T_5000", "T_4000", "T_OTH"],
    seriesColors: { T_1000: "--usa", T_2000: "--usa", T_5000: "--usa", T_4000: "--usa", T_OTH: "--usa" },
    table: { rows: "geo", cols: "bloc" },
  },
  "fpe2-gasto-funciones": {
    renderer: "dumbbell",
    pair: { dim: "bloc", from: "EU27", to: "USA" },
    extraGeos: ["GF10", "GF07", "GF01", "GF09", "GF04", "GF02", "GF03", "GF_OTH"],
    seriesColors: { GF10: "--usa", GF07: "--usa", GF01: "--usa", GF09: "--usa", GF04: "--usa", GF02: "--usa", GF03: "--usa", GF_OTH: "--usa" },
    table: { rows: "geo", cols: "bloc" },
  },
  "fpd1-deficit-paises": {
    renderer: "rank",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "fpd2-intereses-paises": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
