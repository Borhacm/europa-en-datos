# Web de Europa en datos

Sitio estático en Astro con gráficos en D3. Lee los JSON que genera el pipeline (`../data`).

```bash
npm install
npm run dev     # sincroniza ../data en public/data y arranca el servidor local
npm run build   # genera dist/
```

Publicación en Vercel desde esta carpeta: `vercel build --prod && vercel deploy --prebuilt --prod`. Se construye en local porque el build necesita `../data`, que queda fuera de esta carpeta.

Más detalles en el [README principal](../README.md).
