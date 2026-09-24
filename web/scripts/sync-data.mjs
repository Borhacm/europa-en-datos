// Copia la salida del pipeline (../data) a public/data para que el navegador pueda leerla.
import { cpSync, mkdirSync, rmSync } from "node:fs";

const src = new URL("../../data/", import.meta.url);
const dest = new URL("../public/data/", import.meta.url);
rmSync(dest, { recursive: true, force: true });
mkdirSync(dest, { recursive: true });
for (const part of ["charts", "geo"]) {
  cpSync(new URL(part, src), new URL(part, dest), { recursive: true });
}
console.log("datos sincronizados en public/data");
