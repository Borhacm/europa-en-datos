import type { ChartData } from "./data";
import { CHARTS, EXTRA_DIMENSIONS } from "./charts-config";
import { formatNumber, type Lang } from "./i18n";

export interface Pivot {
  rowHeader: string;
  cols: { key: string; label: string }[];
  rows: { key: string; label: string; cells: (string | null)[] }[];
}

function label(chart: ChartData, dim: string, key: string, lang: Lang): string {
  if (dim === "geo") return chart.geos[key]?.[lang] ?? chart.rows.find((r) => r.geo === key)?.name ?? key;
  return chart.dimensions?.[dim]?.[key]?.[lang] ?? EXTRA_DIMENSIONS[dim]?.[key]?.[lang] ?? key;
}

/** Tabla accesible con el estado por defecto de los controles. */
export function pivot(chart: ChartData, lang: Lang, headers: { country: string; year: string }): Pivot {
  const cfg = CHARTS[chart.id];
  const { rows: rowDim, cols: colDim, lastCols } = cfg.table;
  const filter: Record<string, string> = { ...(cfg.fixed ?? {}) };
  for (const c of cfg.controls ?? []) if (c.dim !== rowDim && c.dim !== colDim && c.dim !== "scale") filter[c.dim] = c.default;

  let data = chart.rows.filter((r) => Object.entries(filter).every(([k, v]) => r[k] === undefined || r[k] === v));
  if (chart.best_level) data = data.filter((r) => r.level === chart.best_level[r.country]);
  if (chart.id === "e2-control-internet") data = data.filter((r) => r.stat !== "min");

  let colKeys = [...new Set(data.map((r) => String(r[colDim])))].sort();
  if (colDim === "reason" || colDim === "access") colKeys = Object.keys(chart.dimensions?.[colDim] ?? {}).filter((k) => colKeys.includes(k));
  if (lastCols) colKeys = colKeys.slice(-lastCols);

  const rowKeys = [...new Set(data.map((r) => String(r[rowDim])))];
  const rowLabel = (k: string) => label(chart, rowDim, k, lang);
  rowKeys.sort((a, b) => (a === "EU27" ? -1 : b === "EU27" ? 1 : rowLabel(a).localeCompare(rowLabel(b), lang)));

  const index = new Map(data.map((r) => [`${r[rowDim]}|${r[colDim]}`, r.value as number]));
  return {
    rowHeader: rowDim === "geo" ? headers.country : rowDim,
    cols: colKeys.map((k) => ({ key: k, label: colDim === "time" ? k : label(chart, colDim, k, lang) })),
    rows: rowKeys.map((k) => ({
      key: k,
      label: rowLabel(k),
      cells: colKeys.map((c) => {
        const v = index.get(`${k}|${c}`);
        return v === undefined ? null : formatNumber(v, lang, 2);
      }),
    })),
  };
}
