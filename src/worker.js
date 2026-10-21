// kitchenwhiz.in Worker
// 1. Other hostnames 301 to https://kitchenwhiz.in (same path).
// 2. Old Squarespace addresses that changed 301 to their new pages, so search history carries over.
// 3. Adds security and caching headers to the static files in public/.
// 4. /shop/uspessentials/ serves the USP Essentials shop (Cloudflare Pages project "uspessentials").

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

// The USP Essentials shop lives in its own Pages project; it is shown at kitchenwhiz.in/shop/uspessentials/
const SHOP_PREFIX = "/shop/uspessentials";
const SHOP_ORIGIN = "https://uspessentials.pages.dev";

async function shop(request, url) {
  // The shop uses relative links (img/…, api/…), so its address must end with "/"
  if (url.pathname === SHOP_PREFIX) {
    url.pathname = SHOP_PREFIX + "/";
    return Response.redirect(url.toString(), 301);
  }
  const upstream = new URL(url.pathname.slice(SHOP_PREFIX.length) + url.search, SHOP_ORIGIN);
  const res = await fetch(new Request(upstream.toString(), request), { redirect: "manual" });
  const out = new Response(res.body, res);
  // Keep any redirect from the shop inside /shop/uspessentials/
  const loc = res.headers.get("Location");
  if (loc) {
    const l = new URL(loc, SHOP_ORIGIN);
    if (l.origin === SHOP_ORIGIN) out.headers.set("Location", SHOP_PREFIX + l.pathname + l.search + l.hash);
  }
  for (const [k, v] of Object.entries(SECURITY_HEADERS)) out.headers.set(k, v);
  // On the shop's pages, add a KitchenWhiz breadcrumb bar at the top and a back-to-top button
  if ((out.headers.get("Content-Type") || "").includes("text/html")) {
    return new HTMLRewriter()
      .on("body", { element(el) { el.prepend(SHOP_CRUMBS, { html: true }); el.append(SHOP_TOTOP, { html: true }); } })
      .transform(out);
  }
  return out;
}

const SHOP_CRUMBS = `<nav class="kwx-crumbs" aria-label="Breadcrumb" style="background:#F8F9F9;color:#5B6166;border-bottom:1px solid #D5D9DC;font:14px/1.4 'Instrument Sans','Segoe UI',Helvetica,Arial,sans-serif">
<ol style="list-style:none;margin:0 auto;padding:9px 20px;max-width:1180px;display:flex;flex-wrap:wrap;gap:6px;align-items:center">
<li><a href="/" style="color:#1F2326;text-decoration:none;font-weight:600">← KitchenWhiz</a></li>
<li aria-hidden="true" style="color:#C3CAD0">/</li><li><a href="/equipment" style="color:inherit;text-decoration:none">Equipment</a></li>
<li aria-hidden="true" style="color:#C3CAD0">/</li><li><a href="/usp-essentials" style="color:inherit;text-decoration:none">USP Essentials + Ecoline</a></li>
<li aria-hidden="true" style="color:#C3CAD0">/</li><li aria-current="page" style="color:#1F2326">Shop</li>
</ol></nav>`;

const SHOP_TOTOP = `<a href="#" class="kwx-top" aria-label="Back to top" style="position:fixed;right:16px;bottom:96px;z-index:34;display:inline-flex;align-items:center;gap:6px;padding:11px 14px;border-radius:999px;background:#1F2326;color:#EEF0F1;text-decoration:none;font:600 13px/1 'Instrument Sans','Segoe UI',Arial,sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.2);opacity:0;pointer-events:none;transition:opacity .25s"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>Top</a>
<script>(function(){var b=document.querySelector('.kwx-top');if(!b)return;var f=function(){var s=window.scrollY>700;b.style.opacity=s?'.92':'0';b.style.pointerEvents=s?'auto':'none'};addEventListener('scroll',f,{passive:true});f();b.addEventListener('click',function(e){e.preventDefault();scrollTo({top:0,behavior:'smooth'})})})();</script>`;

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

    if (url.pathname === SHOP_PREFIX || url.pathname.startsWith(SHOP_PREFIX + "/")) return shop(request, url);

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
