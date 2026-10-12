# KitchenWhiz website (commercialkitchens.co.in)

Plain static website (HTML, CSS, images; no build step) for Unique Steel Products / KitchenWhiz.

- `public/` is the site: `index.html`, `404.html`, `images/`.
- `wrangler.jsonc` deploys `public/` to Cloudflare Workers as static assets.

## Publish
Cloudflare → Workers & Pages → Create → Import a repository → `kitchenwhiz/website`.
Build command: none. Deploy command: `npx wrangler deploy`. Every push to `main` redeploys.
Then Settings → Domains & Routes → add `commercialkitchens.co.in` and `www.commercialkitchens.co.in`.

## Edit
Change `public/index.html` or replace files in `public/images/` (lowercase names, no spaces, web-sized images), then commit to `main`.
