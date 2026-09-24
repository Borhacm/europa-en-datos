# Web de Europa en datos

Sitio estático en Astro con gráficos en D3. Lee los JSON que genera el pipeline (`../data`).

```bash
npm install
npm run dev     # sincroniza ../data en public/data y arranca el servidor local
npm run build   # genera dist/
```

El build lee `../data`, fuera de esta carpeta: Vercel lo permite porque el proyecto tiene `web` como directorio raíz y acceso a los archivos de fuera.

Más detalles en el [README principal](../README.md).
