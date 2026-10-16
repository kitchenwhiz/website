# KitchenWhiz website

Static website for Unique Steel Products / KitchenWhiz. Main address: **https://kitchenwhiz.in**.

- `public/` is the site: `index.html`, `404.html`, `images/`, `robots.txt`, `sitemap.xml`.
- `src/worker.js` serves `public/` and redirects (301) www.kitchenwhiz.in, commercialkitchens.co.in and
  www.commercialkitchens.co.in to the same page on kitchenwhiz.in.
- `wrangler.jsonc` attaches all four addresses to the Worker `website` as custom domains.

## Publish
Every push to `main` runs `.github/workflows/deploy.yml`, which runs `wrangler deploy` with the repository
secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. Check results under the **Actions** tab.

## Edit
Change `public/index.html` or replace files in `public/images/` (lowercase names, no spaces, web-sized images),
then commit to `main`.
