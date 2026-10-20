// kitchenwhiz.in Worker
// 1. Other hostnames 301 to https://kitchenwhiz.in (same path).
// 2. Old Squarespace addresses that changed 301 to their new pages, so search history carries over.
// 3. Adds security and caching headers to the static files in public/.

const MAIN_HOST = "kitchenwhiz.in";
const REDIRECT_HOSTS = new Set([
  "www.kitchenwhiz.in",
  "commercialkitchens.co.in",
  "www.commercialkitchens.co.in",
]);

// Old kitchenwhiz.in (Squarespace) paths → new paths. Keys are lowercase, without trailing slash.
const LEGACY = {
  "/home": "/",
  "/index": "/",
  "/cart": "/",
  "/barwhiz-1": "/barwhiz",
  "/cloud-/-qsr-/-central-kitchen": "/cloud-qsr-central-kitchen",
  "/cloud-qsr-central-kitchen-1": "/cloud-qsr-central-kitchen",
  "/kw-originals/-custom-built": "/kw-originals",
  "/kw-originals-custom-built": "/kw-originals",
  "/bought-out": "/equipment#brands-we-supply",
  "/kitchen-whiz-advantage": "/about-us#advantage",
  "/test-demo": "/showroom",
  "/demo-centre": "/showroom",
  "/demo-centre-1": "/showroom",
  "/demo-center": "/showroom",
  "/about": "/about-us",
  "/contact-us": "/contact",
  "/projects": "/living-kitchens",
  "/restaurant": "/restaurants",
  "/bakeries": "/bakery",
  "/cafes": "/cafe",
  "/pizzerias": "/pizzeria",
  "/micro-brewery": "/micro-brewery-and-bar",
  "/general-2": "/",
};

const SECURITY_HEADERS = {
  "X-Content-Type-Options": "nosniff",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "X-Frame-Options": "SAMEORIGIN",
  "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
  "Strict-Transport-Security": "max-age=31536000",
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (REDIRECT_HOSTS.has(url.hostname)) {
      url.protocol = "https:";
      url.hostname = MAIN_HOST;
      url.port = "";
      return Response.redirect(url.toString(), 301);
    }

    let key = url.pathname.toLowerCase();
    try { key = decodeURIComponent(key); } catch (_) { /* keep raw path */ }
    if (key.length > 1 && key.endsWith("/")) key = key.slice(0, -1);
    // Grease trap page is hidden for now: send visitors to USP Essentials (temporary redirect).
    if (key === "/grease-trap" || key === "/grease-traps") {
      return Response.redirect(new URL("/usp-essentials", url.origin).toString(), 302);
    }
    if (Object.prototype.hasOwnProperty.call(LEGACY, key)) {
      const target = new URL(LEGACY[key], url.origin);
      target.search = url.search;
      return Response.redirect(target.toString(), 301);
    }
    // One address per page: lowercase, no trailing slash, no .html (permanent redirects).
    if (!url.pathname.startsWith("/images/") && !url.pathname.startsWith("/assets/")) {
      let clean = url.pathname.toLowerCase();
      if (clean.length > 1 && clean.endsWith("/")) clean = clean.replace(/\/+$/, "") || "/";
      if (clean === "/index.html") clean = "/";
      else if (clean.endsWith(".html") && clean !== "/404.html") clean = clean.slice(0, -5);
      if (clean !== url.pathname) {
        url.pathname = clean;
        return Response.redirect(url.toString(), 301);
      }
    }

    const res = await env.ASSETS.fetch(request);
    const out = new Response(res.body, res);
    for (const [k, v] of Object.entries(SECURITY_HEADERS)) out.headers.set(k, v);
    const p = url.pathname;
    if (res.ok && (p.startsWith("/images/") || p.startsWith("/assets/"))) {
      out.headers.set("Cache-Control", "public, max-age=2592000");
    }
    return out;
  },
};
