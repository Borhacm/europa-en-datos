// Cómo se dibuja cada gráfico de este tema. Ver ChartConfig en lib/charts-config.ts.
import type { ChartConfig } from "../../lib/charts-config";

const charts: Record<string, ChartConfig> = {
  "edg1-matricula-superior": {
    renderer: "line",
    series: ["EU27", "USA", "CHN"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    domainMin: 0,
  },
  "edg2-investigadores": {
    renderer: "line",
    series: ["EU27", "USA", "CHN"],
    table: { rows: "geo", cols: "time", lastCols: 6 },
    digits: 0,
    domainMin: 0,
  },
  // El renderizador «paired» lee las categorías de la dimensión «reason»: aquí son las etapas educativas
  "ede1-gasto-niveles": {
    renderer: "paired",
    usesFocus: true,
    table: { rows: "geo", cols: "reason" },
  },
  // Empleo con estudios hasta la secundaria obligatoria frente a estudios superiores
  "ede2-empleo-nivel": {
    renderer: "dumbbell",
    usesFocus: true,
    pair: { dim: "isced11", from: "ED0-2", to: "ED5-8" },
    table: { rows: "geo", cols: "isced11" },
  },
  "edd1-abandono-paises": {
    renderer: "dumbbell",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
  "edd2-ctim-paises": {
    renderer: "rank",
    usesFocus: true,
    table: { rows: "geo", cols: "time" },
  },
};

export default charts;
