# KitchenWhiz website

Static website for Unique Steel Products / KitchenWhiz. Main address: **https://kitchenwhiz.in**.

- `public/` is the published site: one `.html` file per page, `assets/site.css`, `images/`, `robots.txt`, `sitemap.xml`.
  Pages are served without `.html` (for example `public/bakery.html` is https://kitchenwhiz.in/bakery).
- `tools/` builds the pages: `content.py` holds the page text, `pages/home.html` the home page body,
  `build.py` the shared header, footer, meta tags, structured data and sitemap.
- `src/worker.js`:
  - 301-redirects www.kitchenwhiz.in, commercialkitchens.co.in and www.commercialkitchens.co.in to kitchenwhiz.in;
  - 301-redirects old Squarespace addresses that changed (for example `/barwhiz-1`, `/kw-originals/-custom-built`,
    `/cloud-/-qsr-/-central-kitchen`) so their search history carries over. Add more to `LEGACY`;
  - forces one address per page (lowercase, no trailing slash, no `.html`);
  - adds security headers and 30-day caching for images and CSS.
- `wrangler.jsonc` attaches all four addresses to the Worker `website` as custom domains.

## Edit
1. Change text in `tools/content.py` or `tools/pages/home.html`, or styles in `public/assets/site.css`.
2. Run `python3 tools/build.py` (rebuilds every page and the sitemap).
3. Commit everything in `public/` and `tools/` to `main`.

Images go in `public/images/` (lowercase names, no spaces, under ~250 KB).

## Publish
Every push to `main` runs `.github/workflows/deploy.yml`, which runs `wrangler deploy` with the repository
secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. Check results under the **Actions** tab.
