// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "g1-inversion-id": {
    renderer: "line",
    controls: [{ dim: "measure", default: "total" }],
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
    digits: 2,
  },
  "g2-patentes-ia": {
    renderer: "line",
    controls: [{ dim: "scale", default: "total", options: ["total", "per_million"] }],
    valueFrom: { control: "scale", map: { total: "value", per_million: "per_million" } },
    series: ["USA", "CHN", "EU27"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "g3-modelos-ia": {
    renderer: "line",
    controls: [{ dim: "rule", default: "participa" }],
    series: ["USA", "CHN", "EU27"],
    showContext: true,
    table: { rows: "geo", cols: "time", lastCols: 8 },
    domainMin: 0,
    digits: 0,
  },
  "e1-motivos-no-ia-generativa": {
    renderer: "paired",
    usesFocus: true,
    table: { rows: "geo", cols: "reason" },
  },
  "e2-control-internet": {
    renderer: "line",
    controls: [{ dim: "measure", default: "v2smgovfilprc" }],
    series: ["USA", "CHN", "EU27"],
    fixed: {},
    table: { rows: "geo", cols: "time", lastCols: 6 },
  },
  "e3-modelos-abiertos": {
    renderer: "stack",
    series: ["USA", "CHN", "EU27", "GBR"],
    table: { rows: "geo", cols: "access" },
  },
  "d1-empresas-ia": {
    renderer: "dumbbell",
    controls: [{ dim: "size", default: "GE10" }],
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "d2-mapa-regional-ia": {
    renderer: "map",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "d3-ia-generativa": {
    renderer: "rank",
    controls: [
      { dim: "age", default: "IND_TOTAL" },
      { dim: "use", default: "I_IUAI" },
    ],
    usesFocus: true,
    table: { rows: "geo", cols: "age" },
  },
  "d4-competencias-digitales": {
    renderer: "rank",
    controls: [{ dim: "time", default: "2025", options: ["2021", "2023", "2025"] }],
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
