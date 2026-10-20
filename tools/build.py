#!/usr/bin/env python3
"""Builds every page in public/ from one shared layout.

Edit page text in tools/content.py (or tools/pages/home.html for the home page),
then run:  python3 tools/build.py
Commit the changed files in public/ and push; GitHub Actions deploys them.
"""
import hashlib, html, json, os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, "public")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C  # noqa: E402

SITE = "https://kitchenwhiz.in"
e = lambda s: html.escape(s, quote=True)

css_hash = hashlib.md5(open(os.path.join(PUB, "assets/site.css"), "rb").read()).hexdigest()[:8]



def header(path):
    sec = C.SECTION_OF.get(path, path)
    cur = lambda h: ' aria-current="page"' if h in (path, sec) else ""
    kitchens = [("/commercial-kitchens", "Kitchen design & setup")] + [(f'/{s["slug"]}', s["short"]) for s in C.SECTORS]
    equipment = [("/equipment", "All equipment"), ("/kw-originals", "KW Originals (custom built)")] + ([("/grease-trap", "Grease traps")] if C.SHOW_GREASE_TRAP else []) + [
                 ("/showroom", "Showroom & demo centre")]
    brands = C.BRAND_MENU
    def drop(label, href, items, active):
        links = "".join(f'<a href="{h}"{cur(h) if h == path else ""}>{e(t)}</a>' for h, t in items)
        ac = ' aria-current="page"' if active else ""
        return f'<div class="dd"><a href="{href}" class="dd-top"{ac}>{label}<span aria-hidden="true">▾</span></a><div class="dd-panel">{links}</div></div>'
    is_brand = path in C.BRAND_PATHS
    nav = (drop("Kitchens", "/commercial-kitchens", kitchens, sec == "/commercial-kitchens")
           + drop("Equipment", "/equipment", equipment, sec == "/equipment" and not is_brand)
           + drop("Brands", "/equipment#brands", brands, is_brand)
           + "".join(f'<a href="{h}"{cur(h)}>{t}</a>' for h, t in
                     [("/living-kitchens", "Projects"), ("/showroom", "Showroom"), ("/about-us", "About"), ("/contact", "Contact")]))
    menu = ['<a href="/">Home</a>']
    for title, items in [("Kitchens", kitchens), ("Equipment", equipment), ("Our brands", brands),
                         ("Company", [("/living-kitchens", "Projects"), ("/about-us", "About us"), ("/contact", "Contact")])]:
        menu += [f'<span class="sub">{title}</span>'] + [f'<a href="{h}">{e(t)}</a>' for h, t in items]
    return f'''<header class="nav">
  <div class="wrap">
    <a href="/" aria-label="KitchenWhiz home"><img class="logo-light" src="/images/logo.png" alt="KitchenWhiz, since 1977, living kitchens" width="182" height="90"><img class="logo-dark" src="/images/logo-light.png" alt="KitchenWhiz, since 1977, living kitchens" width="400" height="197"></a>
    <nav aria-label="Main">{nav}</nav>
    <details class="menu"><summary aria-label="Open menu">Menu</summary><div class="panel">{"".join(menu)}</div></details>
    <a class="btn btn-rose" href="/contact">Talk to us</a>
  </div>
</header>'''


def footer():
    col = lambda title, links: f'<div><b>{title}</b>' + "".join(f'<a href="{h}">{e(t)}</a>' for h, t in links) + "</div>"
    kitchens = [(f'/{s["slug"]}', s["short"]) for s in C.SECTORS]
    equip = [("/equipment", "All equipment"), ("/kw-originals", "KW Originals (custom built)")] + ([("/grease-trap", "Grease traps")] if C.SHOW_GREASE_TRAP else []) + [
             ("/commercial-kitchens", "Kitchen design & setup"), ("/showroom", "Showroom & demo centre")]
    brands = C.BRAND_MENU
    company = [("/about-us", "About us"), ("/living-kitchens", "Projects"), ("/contact", "Contact"),
               ("https://wa.me/919902014700", "WhatsApp 99020 14700")]
    return f'''<footer>
  <div class="wrap">
    <div class="foot-links">{col("Kitchens", kitchens)}{col("Equipment", equip)}{col("Our brands", brands)}{col("Company", company)}</div>
    <img class="logo-light" src="/images/logo.png" alt="KitchenWhiz" width="182" height="90" loading="lazy"><img class="logo-dark" src="/images/logo-light.png" alt="KitchenWhiz" width="400" height="197" loading="lazy">
    <span>KitchenWhiz is a brand of Unique Steel Products · 235/E Bommasandra Industrial Area, Phase 3, Bengaluru 560099 · <a href="tel:+919902014700">99020 14700</a></span>
    <span><a href="https://www.instagram.com/kitchenwhiz.in/" target="_blank" rel="noopener">Instagram</a> · <a href="https://www.facebook.com/KitchenWhiz.in/" target="_blank" rel="noopener">Facebook</a> · <a href="https://www.linkedin.com/company/kitchenwhiz" target="_blank" rel="noopener">LinkedIn</a></span>
  </div>
</footer>'''


CTA = '''<section class="cta-band">
  <div class="wrap">
    <div><h2>Planning a kitchen?</h2><p>Share your floor plan, cuisine and covers per day. We'll come back with a layout, an equipment list and next steps.</p></div>
    <div class="cta" style="margin-top:0"><a class="btn btn-rose" href="/contact">Talk to us</a><a class="btn btn-line" href="https://wa.me/919902014700" target="_blank" rel="noopener">WhatsApp us</a></div>
  </div>
</section>'''


def crumbs(trail):
    items = "".join(f'<li><a href="{h}">{e(t)}</a></li>' if h else f'<li aria-current="page">{e(t)}</li>' for h, t in trail)
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{items}</ol></nav>'


def crumb_ld(trail, path):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t, "item": SITE + (h or path)} for i, (h, t) in enumerate(trail)]}


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]}


def page(p):
    path = p["path"]
    url = SITE + path
    lds = list(p.get("ld", []))
    trail = p.get("crumbs")
    if trail:
        lds.append(crumb_ld(trail, path))
    if p.get("faqs"):
        lds.append(faq_ld(p["faqs"]))
    ld = "\n".join(f'<script type="application/ld+json">\n{json.dumps(x, ensure_ascii=False, indent=1)}\n</script>' for x in lds)
    img = SITE + "/images/" + p.get("og", "showroom.jpg")
    body = p["body"]
    robots = p.get("robots", "index, follow, max-image-preview:large")
    canonical = f'<link rel="canonical" href="{url}">\n' if p.get("canonical", True) else ""
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["desc"])}">
{canonical}<meta name="robots" content="{robots}">
<meta name="theme-color" content="#A3706F">
<meta property="og:type" content="website">
<meta property="og:site_name" content="KitchenWhiz">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="{e(p.get("og_title", p["title"]))}">
<meta property="og:description" content="{e(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/images/logo.png" type="image/png">
<link rel="apple-touch-icon" href="/images/logo.png">
{ld}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
<link rel="stylesheet" href="/assets/site.css?v={css_hash}">
</head>
<body>
{header(path)}
<main id="top">
{crumbs(trail) if trail else ""}
{body}
</main>
{"" if p.get("no_cta") else CTA}
{footer()}
</body>
</html>
'''


def main():
    pages = C.pages()
    seen = set()
    for p in pages:
        out = p["file"]
        assert out not in seen, out
        seen.add(out)
        with open(os.path.join(PUB, out), "w") as f:
            f.write(page(p))
    today = datetime.date.today().isoformat()
    urls = "".join(f'  <url><loc>{SITE}{p["path"]}</loc><lastmod>{today}</lastmod></url>\n'
                   for p in pages if p.get("sitemap", True))
    with open(os.path.join(PUB, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    print(f"built {len(pages)} pages")


if __name__ == "__main__":
    main()
