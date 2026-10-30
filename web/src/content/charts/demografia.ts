// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "dmg1-mayores-bloques": {
    renderer: "line",
    series: ["EU27", "USA", "CHN"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "dmg2-fecundidad-bloques": {
    renderer: "line",
    series: ["EU27", "USA", "CHN"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    digits: 2,
    domainMin: 0,
  },
  // Dos series de un mismo bloque: saldo natural (negativo desde 2012) y saldo migratorio
  "dme1-crecimiento-ue": {
    renderer: "line",
    series: ["NATGROW", "CNMIGRAT"],
    seriesColors: { NATGROW: "--context-strong", CNMIGRAT: "--eu" },
    table: { rows: "series", cols: "time", lastCols: 6 },
    digits: 0,
  },
  "dme2-permisos-motivo": {
    renderer: "paired",
    usesFocus: true,
    table: { rows: "geo", cols: "reason" },
  },
  "dmd1-fecundidad-paises": {
    renderer: "dumbbell",
    usesFocus: true,
    digits: 2,
    table: { rows: "geo", cols: "time" },
  },
  "dmd2-nacidos-fuera": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
