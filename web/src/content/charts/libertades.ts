// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

// Componentes del índice de V-Dem: las filas del gráfico de pesas no son países
const COMPONENTS = ["v2xlg_legcon", "v2x_freexp_altinf", "v2xcl_rol", "v2x_jucon", "v2x_frassoc_thick", "v2xel_frefair"];

const charts: Record<string, ChartConfig> = {
  "lg1-democracia": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
    digits: 2,
  },
  "lg4-componentes-democracia": {
    renderer: "dumbbell",
    extraGeos: COMPONENTS,
    seriesColors: Object.fromEntries(COMPONENTS.map((c) => [c, "--usa"])),
    digits: 2,
    table: { rows: "geo", cols: "time" },
  },
  "lg2-esperanza-vida": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "le1-emisiones-1990": {
    renderer: "line",
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
    digits: 0,
  },
  "le3-huella-emisiones": {
    renderer: "line",
    controls: [{ dim: "bloc", default: "EU27", options: ["EU27", "USA", "CHN"] }],
    series: ["FD_GHG", "PROD_GHG"],
    seriesColors: { FD_GHG: "--eu", PROD_GHG: "--context-strong" },
    table: { rows: "series", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "le2-gasto-social": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2022", options: ["2012", "2017", "2022"] }],
    extraGeos: ["USA"],
    usesFocus: true,
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "ld1-democracia-ue": {
    renderer: "dumbbell",
    usesFocus: true,
    digits: 2,
    table: { rows: "geo", cols: "time" },
  },
  "ld4-trayectorias-democracia": {
    renderer: "line",
    series: ["EU27", "POL", "SVK", "HUN"],
    seriesColors: { HUN: "--ink", POL: "--focus", SVK: "--context-strong" },
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
    digits: 2,
  },
  "ld5-pobreza-transferencias": {
    renderer: "dumbbell",
    pair: { dim: "transfers", from: "before", to: "after" },
    usesFocus: true,
    table: { rows: "geo", cols: "transfers" },
  },
};

export default charts;
