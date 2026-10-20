"""Page text for kitchenwhiz.in. Edit here, then run: python3 tools/build.py"""
import html, os

e = lambda s: html.escape(s, quote=True)
SITE = "https://kitchenwhiz.in"
HERE = os.path.dirname(os.path.abspath(__file__))
WA = "https://wa.me/919902014700"
# Grease trap page and links are hidden for now. Set to True to bring them back.
SHOW_GREASE_TRAP = False
MAPS = "https://www.google.com/maps/place/?q=place_id:ChIJFfickwVtrjsRtKl4_SAreX4"

BUSINESS = {
    "@context": "https://schema.org",
    "@type": "Store",
    "@id": SITE + "/#business",
    "name": "KitchenWhiz – Unique Steel Products",
    "alternateName": ["KitchenWhiz", "Unique Steel Products", "Kitchen Whiz"],
    "description": "Commercial kitchen equipment manufacturer and supplier in Bangalore. Kitchen design, stainless steel fabrication, installation and service for restaurants, hotels, bakeries, cafés, bars, breweries and cloud kitchens.",
    "url": SITE + "/",
    "logo": SITE + "/images/logo.png",
    "image": [SITE + "/images/showroom.jpg", SITE + "/images/p-geist.jpg"],
    "telephone": "+91-99020-14700",
    "email": "info@kitchenwhiz.in",
    "foundingDate": "1977",
    "address": {"@type": "PostalAddress", "streetAddress": "235/E, Bommasandra Industrial Area, Phase 3",
                "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "postalCode": "560099", "addressCountry": "IN"},
    "geo": {"@type": "GeoCoordinates", "latitude": 12.8158287, "longitude": 77.6942781},
    "hasMap": MAPS,
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                   "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                                   "opens": "09:00", "closes": "17:30"}],
    "areaServed": ["Bengaluru", "Karnataka", "India"],
    "brand": ["KitchenWhiz", "Barwhiz", "HeatKO", "USP Essentials", "USP Ecoline"],
    "sameAs": ["https://www.instagram.com/kitchenwhiz.in/", "https://www.facebook.com/KitchenWhiz.in/",
               "https://www.linkedin.com/company/kitchenwhiz"],
}
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/",
           "name": "KitchenWhiz", "alternateName": "Kitchen Whiz", "publisher": {"@id": SITE + "/#business"}}

STORES = {
    "Taj West End": "store-restaurants-8", "DoubleTree by Hilton": "store-restaurants-4",
    "Four Points by Sheraton": "store-sheraton", "MTR – Mavalli Tiffin Rooms": "store-mtr",
    "ITC Master Chef": "store-itc-master-chef", "China Pearl": "store-restaurants-3", "Badmaash": "store-restaurants-2",
    "Plan B": "store-restaurants-7", "Café Noir": "store-cafe-1", "Coffee Tales": "store-coffee-tales",
    "Lavonne": "store-lavonne", "Glen's Bakehouse": "store-glens-bakehouse", "Milano": "store-milano",
    "Thom's Bakery": "store-thoms-bakery", "White Caps": "store-white-caps", "Go Pizza": "store-go-pizza",
    "Thin Tony's": "store-thin-tony", "Paper & Pie": "store-paper-and-pie", "Imperio": "store-imperio",
    "India Chai": "store-india-chai", "Khan Saheb": "store-khan-saheb", "Leon Grill": "store-leon-grill",
    "Nagarjuna": "store-nagarjuna", "Sharief Bhai": "store-sharief-bhai", "Juice Junction": "store-juice-junction",
    "Geist Brewing Co.": "store-geist", "BYG Brewsky": "store-byg-brewsky", "The 13th Floor": "store-13th-floor",
    "Bob's Bar": "store-bobs-bar", "Tipsy Bull": "store-tipsy-bull",
}


def stores(names, cls="stores s4"):
    figs = "".join(f'<figure><img src="/images/{STORES[n]}.jpg" alt="{e(n)}" width="480" height="360" loading="lazy">'
                   f'<figcaption>{e(n)}</figcaption></figure>' for n in names)
    return f'<div class="{cls}">{figs}</div>'


def photo(src, alt, w, h, cap=None, cls="photo", lazy=False):
    c = f"<figcaption>{e(cap)}</figcaption>" if cap else ""
    ld = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    return f'<figure class="{cls}"><img src="/images/{src}" alt="{e(alt)}" width="{w}" height="{h}"{ld}>{c}</figure>'


def faq_html(faqs, title, eyebrow="Questions"):
    items = "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in faqs)
    return f'''<section><div class="wrap"><p class="eyebrow">{eyebrow}</p><h2>{title}</h2><div class="faq">{items}</div></div></section>'''


def cards(items, eyebrow, title, extra=""):
    cs = "".join(f'<a href="{h}"><b>{e(t)}</b><span>{e(d)}</span><span class="go">Read more →</span></a>' for h, t, d in items)
    return f'<section style="padding-top:0"><div class="wrap"><p class="eyebrow">{eyebrow}</p><h2>{title}</h2>{extra}<div class="cards">{cs}</div></div></section>'


def ul(items, cls="list-cols"):
    return f'<ul class="{cls}">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def pills(label, items):
    links = "".join(f'<a href="{h}">{e(t)}</a>' for h, t in items)
    return f'<nav class="pills" aria-label="{e(label)}"><span>{e(label)}</span>{links}</nav>'


def hero(eyebrow, h1, lede, fig, ctas=None, extra=""):
    ctas = ctas or [("/contact", "Plan my kitchen", "btn-rose"), (WA, "WhatsApp us", "btn-line")]
    ext = ' target="_blank" rel="noopener"'
    b = "".join(f'<a class="btn {c}" href="{h}"{ext if h.startswith("http") else ""}>{t}</a>' for h, t, c in ctas)
    return f'''<section class="page-hero"><div class="wrap"><div class="hero-grid">
<div><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lede">{lede}</p>{extra}<div class="cta">{b}</div></div>
{fig}
</div></div></section>'''


STEPS = '''<div class="steps">
      <div class="step"><h3>Consult</h3><p>Site visit, menu and volume study, and a budget that suits your format.</p></div>
      <div class="step"><h3>Design &amp; MEP</h3><p>Kitchen layout, 3D line renders, and gas, water, power and exhaust points.</p></div>
      <div class="step"><h3>Fabricate</h3><p>Custom SS202 and SS304 equipment built to your exact sizes in our factory.</p></div>
      <div class="step"><h3>Install</h3><p>Delivery, placement, exhaust hoods, ducting and fire suppression, commissioned on site.</p></div>
      <div class="step"><h3>Train &amp; service</h3><p>Equipment training for your chefs, then maintenance and spares.</p></div>
    </div>'''

RENDERS = '''<div class="renders">
      <figure><img src="/images/line-render-1.jpg" alt="3D render of a cooking line with burner ranges, sink and work tables" width="1150" height="594" loading="lazy"><figcaption>Every line is drawn in 3D before it is built.</figcaption></figure>
      <figure><img src="/images/line-render-2.jpg" alt="3D render of a Chinese and continental cooking line" width="1064" height="513" loading="lazy"><figcaption>Sizes are matched to your site, down to the millimetre.</figcaption></figure>
    </div>'''

COMMON_FAQ = [
    ("Do you make equipment to custom sizes?",
     "Yes. Work tables, burner ranges, sinks, racks, hoods and counters are fabricated in our Bommasandra factory in SS202 or SS304, to the exact sizes of your site."),
    ("Can we see the equipment before we buy?",
     'Yes. Our 20,000 sq ft <a href="/showroom">showroom and demo centre</a> in Bommasandra has Indian and imported equipment on display, and your chef can try it in a live demo. Call ahead for a demo slot.'),
    ("Do you install exhaust and fire suppression too?",
     "Yes. Installation covers placement, exhaust hoods, ducting and fire suppression, and we commission the kitchen on site before handing over."),
    ("What should I send to get a quote?",
     'Your floor plan or site photos, the cuisine, and the number of covers or orders per day. Email <a href="mailto:info@kitchenwhiz.in">info@kitchenwhiz.in</a> or <a href="' + WA + '">WhatsApp 99020 14700</a>.'),
]

# ---------------------------------------------------------------- sectors
SECTORS = [
    dict(slug="restaurants", short="Restaurants & hotels", og="p-restaurant.jpg",
         title="Restaurant & Hotel Kitchen Equipment in Bangalore | KitchenWhiz",
         desc="Restaurant and hotel kitchen design, custom stainless steel equipment and installation in Bangalore. Pan Asian, continental, Indian and Mediterranean lines. Since 1977.",
         eyebrow="Restaurant & hotel kitchens · Bangalore",
         h1="Restaurant &amp; hotel <em>kitchen</em> equipment",
         lede="Our kitchens cover a variety of cuisines: Pan Asian, continental, Indian, Mediterranean and more. From compact to large spaces, they are designed for high efficiency with an eye on aesthetics, and our designs are modular and tailor-made to any space.",
         img=("p-restaurant.jpg", "Restaurant kitchen with a stainless-steel cooking line", 1300, 975),
         eq_lede="Cooking lines and back-of-house equipment for à la carte restaurants, hotel kitchens, banqueting and club kitchens.",
         equipment=["Burner ranges and Chinese ranges", "Tandoors", "Vegetable cutters", "Meat mincers", "Refrigeration and cold rooms",
                    "Combi and convection ovens", "Work tables", "Sinks and dishwash tables", "Racks and storage", "Dishwashers",
                    "Exhaust hoods and fresh air", "Fire suppression"],
         original=("Robata grill", "A KitchenWhiz original born out of the Japanese idea of fireside cooking. It grills all kinds of food, and diners get to watch what is being made."),
         stores=["Taj West End", "DoubleTree by Hilton", "Four Points by Sheraton", "China Pearl", "Badmaash", "Plan B", "Café Noir", "ITC Master Chef"],
         clients="Taj West End, Sheraton, DoubleTree by Hilton, Holiday Inn, Bangalore Club, Karnataka Golf Association, The Oterra, China Pearl, Monkey Bar, Badmaash, Plan B, Prequel, Taki Taki, Yuki, Café Noir",
         faqs=[("Do you set up hotel kitchens as well as restaurants?",
                "Yes. We have equipped hotel and club kitchens including Taj West End, Four Points by Sheraton, DoubleTree by Hilton, Holiday Inn, Bangalore Club and the Karnataka Golf Association, as well as stand-alone restaurants.")] + COMMON_FAQ),
    dict(slug="bakery", short="Bakeries", og="p-bakery-oven.jpg",
         title="Bakery Equipment & Bakery Kitchen Setup in Bangalore | KitchenWhiz",
         desc="Bakery equipment in Bangalore: ovens, mixers, sheeters, proofers, slicers, racks and trolleys, with complete bakery kitchen design and installation. For production, artisanal and home bakers.",
         eyebrow="Bakery kitchens · Bangalore",
         h1="Bakery <em>equipment</em> &amp; bakery kitchens",
         lede="We have set up bakeries for mass production, high-end restaurants and microbreweries, artisanal bakers with specific needs, and home bakers. Combi ovens now keep every batch consistent, and we help you choose the right one.",
         img=("p-bakery-oven.jpg", "Bakery with racks of trays next to an oven", 975, 1300), tall=True,
         eq_lede="Everything from the mixer to the display counter, in standard models or built to your space.",
         equipment=["Deck, convection and combi ovens", "Planetary and spiral mixers", "Dough sheeters", "Bread slicers", "Proofers",
                    "Refrigeration and freezers", "Bakery tables (granite or SS top)", "Racks and tray trolleys", "SS and aluminium bakery trays",
                    "Display counters"],
         original=("Bakery trolley", "A KitchenWhiz original for stacking trays, which makes moving product before and after baking easier."),
         stores=["Glen's Bakehouse", "Milano", "Thom's Bakery", "Lavonne", "White Caps"],
         clients="ITC Sunfeast, Lavonne, Thom's Bakery, Glen's Bakehouse, Milano, Loafer &amp; Co., White Caps, Samie's Cake Art, The Flour Girl, Deepali's Academy",
         faqs=[("Do you supply equipment for home bakers and baking academies?",
                "Yes. Besides production bakeries we work with home bakers and teaching kitchens such as Deepali's Academy and The Flour Girl, and size the equipment to the batch you actually bake.")] + COMMON_FAQ),
    dict(slug="pizzeria", short="Pizzerias", og="p-pizzeria.jpg",
         title="Pizzeria Kitchen Equipment & Pizza Ovens in Bangalore | KitchenWhiz",
         desc="Pizzeria kitchen equipment in Bangalore: customised wood-fired ovens, conventional pizza ovens, dough kneaders, prep counters and refrigeration, designed and installed by KitchenWhiz.",
         eyebrow="Pizzeria kitchens · Bangalore",
         h1="Pizzeria kitchens &amp; <em>pizza ovens</em>",
         lede="Equipment that gives a warm appeal, like our customised wood-fired ovens, supported by prep counters and coffee machines that complete the Italian feel.",
         img=("p-pizzeria.jpg", "Pizzeria kitchen with a wood-fired oven", 1300, 975),
         eq_lede="From the dough room to the pass, with the oven as the centrepiece.",
         equipment=["Customised wood-fired ovens", "Conventional pizza ovens", "Kneaders and dough rollers", "Pizza prep counters",
                    "Refrigeration", "Coffee machines", "Mixers and blenders", "Tables, racks and sinks", "Display counters", "Wine chillers"],
         original=("Prep counter", "A KitchenWhiz original that keeps everything needed for pizzas and sandwiches in one organised station, so the chef can assemble quickly."),
         stores=["Go Pizza", "Thin Tony's", "Paper & Pie", "Milano"],
         clients="Brik Oven, Holy Doh, Thin Tony's, Go Pizza",
         faqs=[("Can you build a wood-fired oven for our space?",
                "Yes. We customise wood-fired ovens to your kitchen and dining layout, and plan the prep counter, refrigeration and exhaust around them. Brik Oven and Holy Doh are among the pizzerias we have equipped.")] + COMMON_FAQ),
    dict(slug="cafe", short="Cafés", og="p-cafe-display.jpg",
         title="Café Kitchen Equipment in Bangalore | Coffee Shop Setup | KitchenWhiz",
         desc="Café and coffee shop equipment in Bangalore: display counters, coffee machines, speed ovens, ice machines, blenders, grillers, waffle and crepe makers, designed and installed by KitchenWhiz.",
         eyebrow="Café kitchens · Bangalore",
         h1="Café &amp; coffee shop <em>equipment</em>",
         lede="Front-of-house food display with tabletop cooking and dispensing equipment that is functional, looks good, and is easy to use and keep hygienic. Most cafés now use speed ovens, which turn orders around fast without losing the texture of the product.",
         img=("p-cafe-display.jpg", "Cake display counter in a café", 975, 1300), tall=True,
         eq_lede="Counter and back-kitchen equipment for cafés, coffee bars and patisseries.",
         equipment=["Display counters", "Coffee machines", "Speed and convection ovens", "Refrigerators", "Ice machines", "Blenders",
                    "Cold beverage dispensers", "Fryers", "Sandwich grillers", "Waffle makers", "Crepe makers", "Tables, racks and sinks"],
         original=("Six burner range", "A KitchenWhiz original and the workhorse of any commercial kitchen: one versatile range that handles a wide variety of tasks."),
         stores=["Café Noir", "Coffee Tales", "Lavonne", "Paper & Pie", "Milano", "Glen's Bakehouse", "India Chai", "Juice Junction"],
         clients="Coffee Tales, Café Noir, Lavonne Café, Glen's Bakehouse, Milano, Paper and Pie",
         faqs=[("Which oven suits a small café?",
                "It depends on your menu and volume. Many cafés now choose a speed oven for fast turnaround; for baking on site a convection or combi oven may suit better. You can try UNOX ovens in a live demo at our showroom before deciding.")] + COMMON_FAQ),
    dict(slug="micro-brewery-and-bar", short="Micro-breweries & bars", og="p-toit.jpg",
         title="Bar & Microbrewery Equipment in Bangalore | Cocktail Stations | KitchenWhiz",
         desc="Bar and microbrewery equipment in Bangalore: cocktail stations, cold rooms, beer towers and taps, flash chillers, kegerators and glass washers. Bars designed for tight spaces by KitchenWhiz and Barwhiz.",
         eyebrow="Micro-brewery & bar · Bangalore",
         h1="Bars &amp; <em>micro-breweries</em>",
         lede="Many bars have space constraints, so ours are designed ergonomically for ease of use and access. The bar is the showcase, and we take special care to make it eye-catching. Cocktail stations bring everything a bartender needs into one unit, so drinks go out fast.",
         img=("p-toit.jpg", "Bar counter at Toit, Bengaluru", 1300, 975),
         eq_lede="Bar counters, back bars and brewery kitchens, including Barwhiz cocktail stations from our own factory.",
         equipment=["Cocktail stations (Barwhiz)", "Bar cabinets and back bars", "Cold rooms", "Beer towers and taps", "Beer lines",
                    "Flash chillers", "Kegerators", "Ice cube machines", "Glass washers", "Ice crushers and blenders", "Bottle coolers", "Wine chillers"],
         original=("Cocktail station", 'A KitchenWhiz original that keeps every supply for mixed drinks in one organised station, so bartenders serve faster. The full range is sold as <a href="/barwhiz">Barwhiz</a>.'),
         stores=["Geist Brewing Co.", "BYG Brewsky", "The 13th Floor", "Bob's Bar", "Tipsy Bull", "Badmaash", "Plan B", "Leon Grill"],
         clients="Toit, Geist, BYG Brewsky, The Bier Library, Bier Garten, BLR Brewing Co., Jamming Goat, Yuki, The 13th Floor, Bob's Bar, Juliet, Kaze, Mirage, Mynx, Tipsy Bull",
         faqs=[("Do you design the bar and the brewery kitchen together?",
                "Yes. We plan the bar counter, back bar, cold room and the kitchen as one project, so the bar and kitchen teams don't get in each other's way. Toit, Geist and BYG Brewsky are among the breweries we have equipped.")] + COMMON_FAQ),
    dict(slug="cloud-qsr-central-kitchen", short="Cloud, QSR & central kitchens", og="p-imperio.jpg",
         title="Cloud Kitchen, QSR & Central Kitchen Equipment in Bangalore | KitchenWhiz",
         desc="Cloud kitchen, QSR and central kitchen setup in Bangalore: hub-and-spoke kitchen design, high-volume cooking, prep, storage and dishwash equipment. Clients include MTR, ITC and Akshaya Patra.",
         eyebrow="Cloud, QSR & central kitchens · Bangalore",
         h1="Cloud, QSR &amp; <em>central</em> kitchens",
         lede="A central kitchen lets a brand scale up without building a full kitchen at every outlet, whether those outlets serve dine-in or delivery. We provide a complete solution for this hub-and-spoke model.",
         img=("p-imperio.jpg", "Imperio QSR kitchen", 1300, 986),
         eq_lede="High-volume prep, cooking, holding and cleaning, laid out for speed and hygiene.",
         equipment=["Work tables", "Sinks", "Racks", "Dishwashers", "Exhaust and fresh air", "Burner ranges", "Vegetable cutters",
                    "Meat mincers", "Refrigeration and cold rooms", "Ovens", "Bain maries and hot holding", "Trolleys and storage bins"],
         original=("Bain marie", "A KitchenWhiz original that works like a traditional water bath or double boiler, keeping food at the right serving temperature."),
         stores=["MTR – Mavalli Tiffin Rooms", "ITC Master Chef", "Imperio", "Khan Saheb", "Nagarjuna", "Sharief Bhai", "Leon Grill", "India Chai"],
         clients="Akshaya Patra, ITC Aashirvaad, ITC Master Chef, MTR, GRB, Imperio, India Chai, Juice Junction, Khan Saheb, Leon Grill, Nagarjuna, Potful Biryani, Sharief Bhai, Square Meal",
         faqs=[("Can you plan a central kitchen that supplies several outlets?",
                "Yes. We design the hub kitchen for volume and the outlets for finishing and holding, so each outlet needs only a small footprint. Our central kitchen clients include Akshaya Patra, MTR and ITC.")] + COMMON_FAQ),
]

# ---------------------------------------------------------------- brands
BRANDS = [
    dict(slug="barwhiz", name="Barwhiz", cls="b-bw", logo=("barwhiz.png", 124, 142), tag="Where precision meets mixology",
         title="Barwhiz Cocktail Stations & Bar Equipment | Bangalore",
         desc="Barwhiz makes cocktail stations and bar equipment in SS304 in Bangalore: speed rails, sink tables, dispensing tables, liquor cabinets and POS counters, with bar design and installation.",
         h1="Barwhiz <em>cocktail stations</em> &amp; bar equipment",
         lede="Barwhiz builds high-performance cocktail stations for speed, style and durability, combining international design with rugged construction for busy bars.",
         about=["Engineered with premium materials and a fine finish, Barwhiz's self-contained units lift any bar setup and are built to last.",
                "Our showroom has more than 10 cocktail station designs on display, so you can stand behind the bar and try them before you choose.",
                "Beyond equipment, Barwhiz offers complete bar projects: bar design consulting, MEP planning, manufacturing, installation and service, plus bar furniture and tools. We also work with the hospitality community through collaborations and events."],
         range_title="The Barwhiz range",
         products=["Game Changer", "Game Changer Pro", "Starter", "The Socialite", "The Maverick", "The Elevate", "The Elevate Max",
                   "The Catalyst", "The Catalyst Mini", "The Alchemist", "The Conductor", "The Disruptor", "The Curator",
                   "Speed rail", "Drip tray", "Sink table with glass rack", "Dispensing table", "Liquor cabinet", "POS counter"],
         photos=[("bar-studio.jpg", "Barwhiz bar studio with cocktail stations", 507, 900, "Barwhiz bar studio"),
                 ("orbit-station.jpg", "The Orbit, a curved custom cocktail station", 703, 420, "Custom curved station")],
         clients="Toit, BYG Ventures, Jamming Goat, The Bier Library, BLR Brewing Co., Bier Garten, Yuki",
         email="barwhizindia@gmail.com", related="micro-brewery-and-bar"),
    dict(slug="heatko", name="HeatKO", cls="b-hk", logo=("heatko.png", 400, 147), tag="Where innovation meets culinary precision",
         title="HeatKO Dimsum Steamers, Robata Grills & IR Heaters | Bangalore",
         desc="HeatKO commercial kitchen equipment, made in Bangalore: dimsum steamers, cheung fun steamers, pasta blanchers, robata (sigadi) charcoal grills, hot bain maries and IR strip heaters.",
         h1="HeatKO <em>steamers, grills</em> &amp; heaters",
         lede="HeatKO makes heavy-duty commercial kitchen equipment that bridges industrial power and culinary finesse, with precise heat control and energy efficiency.",
         about=["From dimsum steamers and robata grills to IR strip heaters, HeatKO equipment is built for the demands of professional kitchens.",
                "Each unit is designed to keep the electrical load low while staying safe and durable, with a clean, functional finish that looks good on an open line.",
                "HeatKO IR heaters also fit the overhead shelves of our USP Ecoline work tables, to keep food warm at the pass."],
         range_title="The HeatKO range",
         products=["Dimsum steamer", "Cheung fun steamer", "Pasta blancher", "Robatayaki / sigadi charcoal griller", "Hot bain marie", "IR strip heaters (IR500, IR800)"],
         photos=[],
         clients="BYG Ventures, Helen's Place, Yuki, Telangana Spice Kitchen, Jamming Goat, Yazu Supper Club, Destini, Rainbow Children's Hospital",
         email="heatko.india@gmail.com", related="restaurants"),
    dict(slug="usp-essentials", name="USP Essentials", cls="b-ec", logo=("usp-ecoline.png", 300, 157), tag="Affordable. Durable. Essential.",
         title="USP Essentials: Drain Gratings, Grease Traps, Trolleys & Bins | Bangalore",
         desc="USP Essentials stainless steel kitchen infrastructure in standard sizes: drain gratings, grease traps, corner guards, wall shelves, trolleys, storage bins, bakery and oven tables. Made in Bangalore.",
         h1="USP Essentials <em>kitchen infrastructure</em>",
         lede="USP Essentials is a range of high-utility kitchen infrastructure in stainless steel, built for heavy-duty commercial kitchens, in standard sizes that are ready to deploy.",
         about=["The range covers everything from drainage and protective corner guards to heavy-duty tables, specialised trolleys and storage.",
                "Standard dimensions make ordering simple, and each item arrives ready to use. The engineering is rugged and no-nonsense, so the products last and need little maintenance."],
         range_title="The USP Essentials range",
         products=["Drain gratings", "Grease traps", "Wall corner guards", "Wall-mounted shelves", "Wall-mounted pipe shelves", "MS storage racks",
                   "Soak sink trolleys", "Platform trolleys", "Utility trolleys", "Masala trolleys", "Batter trolleys", "Skewer soaking trolleys",
                   "Vegetable crate trolleys", "SS bakery / GN / cooling trolleys", "Vegetable storage bins", "Atta bins", "Charcoal bins",
                   "Nacho bins", "Dust bins", "Deck oven tables", "Bakery tables with granite top and socket", "SS / aluminium bakery trays",
                   "SS pallets", "Attachment holding racks"],
         photos=[("grease-trap-open.jpg", "USP stainless steel grease trap with the lid off, showing basket and baffles", 1200, 780, "USP grease trap")] if SHOW_GREASE_TRAP else [],
         clients="", email="info@kitchenwhiz.in", related="cloud-qsr-central-kitchen"),
    dict(slug="usp-ecoline", name="USP Ecoline", cls="b-ec", logo=("usp-ecoline.png", 300, 157), tag="Affordable. Durable. Essential.",
         title="USP Ecoline Flat-Pack SS Work Tables, Racks & Burners | Bangalore",
         desc="USP Ecoline flat-packed stainless steel kitchen furniture in standard sizes: work tables, overhead shelves, 5-tier storage racks and single burner ranges. Easy to assemble, for new outlets on a budget.",
         h1="USP Ecoline <em>flat-pack</em> kitchen furniture",
         lede="USP Ecoline is sturdy, no-frills stainless steel kitchen furniture in standard sizes, priced for cost-conscious businesses and new outlets.",
         about=["Ecoline ships flat-packed to cut transport costs. Allen-screw fittings make it simple to assemble, and to dismantle again if you move.",
                "Tops and shelves are SS430 with stiffener supports, on 38 mm pipe legs with nylon bushes. Standard lengths are 900, 1150 and 1500 mm, 600 mm deep and 850 mm high.",
                "Every item carries a 12-month warranty against manufacturing defects. Ecoline is sold in standard sizes only; for custom sizes see <a href=\"/kw-originals\">KW Originals</a>."],
         range_title="The USP Ecoline range",
         products=["Work table with cross support", "Work table with one undershelf", "Work table with two undershelves",
                   "Options: 100 mm back splash, two detachable overhead shelves", "SS overhead shelves (mount for HeatKO IR500 / IR800 heaters)",
                   "SS 5-tier storage rack (900 or 1150 mm)", "Single burner range with T35 high-pressure burner"],
         photos=[], clients="", email="uspecoline@gmail.com", related="restaurants"),
]

# The four brands of Unique Steel Products, as shown in menus and brand cards
BRAND_MENU = [("/kw-originals", "KitchenWhiz"), ("/barwhiz", "Barwhiz"), ("/heatko", "HeatKO"),
              ("/usp-essentials", "USP Essentials + Ecoline")]
BRAND_CARDS = [("/kw-originals", "KitchenWhiz", "Engineering culinary spaces, from concept to completion"),
               ("/barwhiz", "Barwhiz", "Where precision meets mixology"),
               ("/heatko", "HeatKO", "Where innovation meets culinary precision"),
               ("/usp-essentials", "USP Essentials + Ecoline", "Affordable. Durable. Essential.")]
BRAND_PATHS = {"/kw-originals", "/barwhiz", "/heatko", "/usp-essentials", "/usp-ecoline"}

SECTION_OF = {f'/{s["slug"]}': "/commercial-kitchens" for s in SECTORS}
SECTION_OF.update({f'/{b["slug"]}': "/equipment" for b in BRANDS})
SECTION_OF.update({"/kw-originals": "/equipment", "/grease-trap": "/equipment"})


def sector_page(s):
    path = "/" + s["slug"]
    img = s["img"]
    fig = photo(img[0], img[1], img[2], img[3], cls="photo tall" if s.get("tall") else "photo")
    others = [(f'/{o["slug"]}', o["short"], o["eq_lede"]) for o in SECTORS if o is not s]
    body = hero(s["eyebrow"], s["h1"], s["lede"], fig)
    body += f'''<section class="band"><div class="wrap">
  <div class="two"><div><p class="eyebrow">What goes into it</p><h2>Equipment we supply</h2><p class="lede">{s["eq_lede"]} Custom pieces are built in our own factory; the rest comes from 100+ Indian and international brands.</p></div>
  <div>{ul(s["equipment"])}</div></div>
  <div class="feature"><div class="badge">KW</div><div><p class="eyebrow">KitchenWhiz original</p><h3>{s["original"][0]}</h3><p>{s["original"][1]}</p></div></div>
</div></section>
<section><div class="wrap"><p class="eyebrow">Our living kitchens</p><h2>Kitchens we've equipped</h2>
  {stores(s["stores"])}
  <p class="clients-line"><b>Clients include:</b> {s["clients"]}</p>
  <p class="clients-line"><a href="/living-kitchens">See more projects →</a></p>
</div></section>
<section class="band"><div class="wrap"><p class="eyebrow">How we work</p><h2>One team from drawing to first service</h2>
<p class="lede">You work with one partner from the first site visit to after-sales service. <a href="/commercial-kitchens">How we plan a kitchen →</a></p>{STEPS}</div></section>
'''
    body += faq_html(s["faqs"], f'{s["short"]}: common questions')
    body += cards(others, "Other kitchens", "Every format, every cuisine")
    ld = [{"@context": "https://schema.org", "@type": "Service", "name": s["title"].split(" | ")[0],
           "serviceType": "Commercial kitchen design, equipment supply and installation", "description": s["desc"],
           "provider": {"@id": SITE + "/#business"}, "areaServed": [{"@type": "City", "name": "Bengaluru"}, {"@type": "State", "name": "Karnataka"}],
           "url": SITE + path}]
    return dict(path=path, file=s["slug"] + ".html", title=s["title"], desc=s["desc"], og=s["og"], body=body,
                crumbs=[("/", "Home"), ("/commercial-kitchens", "Commercial kitchens"), (None, s["short"])],
                faqs=s["faqs"], ld=ld)


def brand_page(b):
    path = "/" + b["slug"]
    lw, lh = b["logo"][1], b["logo"][2]
    block = (f'<article class="brand {b["cls"]}" style="min-height:320px;justify-content:center">'
             f'<img src="/images/{b["logo"][0]}" alt="{e(b["name"])}" width="{lw}" height="{lh}" style="height:80px">'
             f'<div class="tag">{e(b["tag"])}</div><p>A brand of Unique Steel Products, made in Bengaluru.</p></article>')
    body = hero(f'{e(b["name"])} · Unique Steel Products · Bengaluru', b["h1"], b["lede"], block,
                [("/contact", "Ask for a quote", "btn-rose"), (WA, "WhatsApp us", "btn-line")])
    about = "".join(f"<p>{p}</p>" for p in b["about"])
    pics = ""
    if b["photos"]:
        pics = '<div class="duo">' + "".join(photo(p[0], p[1], p[2], p[3], p[4], lazy=True) for p in b["photos"]) + "</div>"
    body += f'''<section class="band"><div class="wrap two">
  <div><p class="eyebrow">About {e(b["name"])}</p><h2>What we make</h2><div class="prose" style="margin-top:18px">{about}</div></div>
  <div><h3>{b["range_title"]}</h3>{ul(b["products"])}<p class="clients-line">Ask us for the catalogue and technical specifications: <a href="mailto:{b["email"]}">{b["email"]}</a> · <a href="tel:+919902014700">99020 14700</a></p></div>
</div>{f'<div class="wrap">{pics}</div>' if pics else ""}</section>
'''
    if b["clients"]:
        body += f'<section><div class="wrap"><p class="eyebrow">Clients</p><h2>Where you will find {e(b["name"])}</h2><p class="clients-line"><b>Clients include:</b> {b["clients"]}</p></div></section>'
    if b["slug"] == "usp-essentials" and SHOW_GREASE_TRAP:
        body += '<section><div class="wrap"><p class="eyebrow">Featured</p><h2>Stainless steel grease traps</h2><p class="lede">Our USP grease trap keeps fats, oils and grease out of your drains. <a href="/grease-trap">Sizes, parts and specifications →</a></p></div></section>'
    usp = b["slug"] in ("usp-essentials", "usp-ecoline")
    if usp:
        sib = next(o for o in BRANDS if o["slug"] in ("usp-essentials", "usp-ecoline") and o is not b)
        body += (f'<section style="padding-top:0"><div class="wrap"><div class="feature"><div class="badge">USP</div><div>'
                 f'<p class="eyebrow">Also from USP</p><h3>{e(sib["name"])}</h3><p>{e(sib["lede"])} '
                 f'<a href="/{sib["slug"]}">See the {e(sib["name"])} range →</a></p></div></div></div></section>')
    own = "/usp-essentials" if usp else path
    others = [c for c in BRAND_CARDS if c[0] != own]
    rel = next(s for s in SECTORS if s["slug"] == b["related"])
    others.append((f'/{rel["slug"]}', rel["short"], rel["eq_lede"]))
    body += cards(others, "Brands by Unique Steel Products", "Four brands, one factory")
    trail = [("/", "Home"), ("/equipment", "Equipment")]
    if b["slug"] == "usp-ecoline":
        trail.append(("/usp-essentials", "USP Essentials + Ecoline"))
    trail.append((None, b["name"]))
    return dict(path=path, file=b["slug"] + ".html", title=b["title"], desc=b["desc"], og=b["photos"][0][0] if b["photos"] else "showroom.jpg",
                body=body, crumbs=trail)


def read(name):
    return open(os.path.join(HERE, "pages", name)).read()


def pages():
    out = []
    home_faqs = [
        ("Where is KitchenWhiz located?",
         'Our showroom, factory and warehouse are at 235/E Bommasandra Industrial Area, Phase 3, Bengaluru 560099. We are open Monday to Saturday, 9:00 am to 5:30 pm. <a href="' + MAPS + '">Directions on Google Maps</a>.'),
        ("Do you manufacture commercial kitchen equipment or only supply it?",
         "Both. We build custom stainless steel equipment in our own factory in Bommasandra, and supply 100+ Indian and international brands such as UNOX, Hoshizaki, Winterhalter and Trufrost."),
        ("Can you design the whole kitchen, not just supply equipment?",
         'Yes. We consult, design the layout and MEP points, draw the line in 3D, fabricate, install, train your team and service the kitchen afterwards. <a href="/commercial-kitchens">How we plan a kitchen</a>.'),
        ("What kinds of businesses do you work with?",
         'Restaurants, hotels and clubs, bakeries, pizzerias, cafés, bars and microbreweries, cloud kitchens, QSR chains, central kitchens and institutional kitchens such as hospitals.'),
        ("How big is your showroom?",
         'Our showroom in Bommasandra has been expanded to 20,000 sq ft. It has Indian and imported equipment for every kind of kitchen, a demo centre, the UNOX Lounge and the Barwhiz bar studio. <a href="/showroom">Plan your visit</a>.'),
        ("Can I see and try equipment before buying?",
         'Yes. Our 20,000 sq ft <a href="/showroom">showroom</a> has a demo centre and the UNOX Lounge, where chefs can cook on the equipment before they buy. Call ahead for a demo slot.'),
        ("Which stainless steel grades do you use?",
         'Custom equipment is built in SS202 or SS304 depending on the use and budget. Our budget <a href="/usp-ecoline">USP Ecoline</a> range uses SS430.'),
    ]
    home = read("home.html")
    home += faq_html(home_faqs, "Commercial kitchens: common questions").replace("<section>", '<section id="faq" style="padding-top:0">', 1)
    # move FAQ before the contact section
    i = home.find('<section class="contact"')
    j = home.find('<section id="faq"')
    if i != -1 and j > i:
        home = home[:i] + home[j:] + "\n" + home[i:j]
    out.append(dict(path="/", file="index.html",
                    title="Commercial Kitchen Equipment Manufacturer in Bangalore | KitchenWhiz",
                    desc="KitchenWhiz (Unique Steel Products) designs, manufactures and installs commercial kitchen equipment in Bangalore since 1977: stainless steel kitchens for restaurants, hotels, bakeries, cafés, bars and cloud kitchens. Showroom in Bommasandra.",
                    og_title="KitchenWhiz – Commercial kitchen equipment, Bangalore, since 1977",
                    body=home, ld=[BUSINESS, WEBSITE], faqs=home_faqs, no_cta=True))
    out += [sector_page(s) for s in SECTORS]
    out += [brand_page(b) for b in BRANDS]
    out += [read_page(n) for n in ("about", "contact", "showroom", "living", "kitchens", "equipment", "originals") + (("greasetrap",) if SHOW_GREASE_TRAP else ())]
    out.append(dict(path="/404", file="404.html", title="Page not found | KitchenWhiz",
                    desc="This page has moved. Find commercial kitchen equipment, kitchen design and our showroom at KitchenWhiz, Bangalore.",
                    robots="noindex", canonical=False, sitemap=False,
                    body='''<section class="notfound"><div class="wrap"><p class="eyebrow">404</p><h1 style="font-size:clamp(36px,5vw,60px);font-weight:900;font-stretch:72%;text-transform:uppercase;line-height:.95">This page has moved</h1>
<p class="lede">Our website has a new layout. The page you were looking for may be under one of these:</p></div></section>''' +
                    cards([("/commercial-kitchens", "Commercial kitchens", "Design and setup for every format"),
                           ("/equipment", "Equipment", "What we make and supply"),
                           ("/showroom", "Showroom", "Visit and try the equipment"),
                           ("/living-kitchens", "Projects", "Kitchens we've built"),
                           ("/about-us", "About us", "Since 1977"),
                           ("/contact", "Contact", "Call, email or visit")], "Popular pages", "Where to next")))
    return out


# --------------------------------------------------------------- one-off pages
def read_page(name):
    return globals()["p_" + name]()


def p_about():
    adv = ["Over 45 years of building and looking after commercial kitchens of every format.",
           "Full service, from planning and design to building and maintaining the kitchen.",
           "In-house manufacturing of custom equipment, so a kitchen can be designed to fit any space.",
           "We represent many major Indian and international equipment makers.",
           "If something isn't available here, we source it from anywhere in the world, as we have for several clients.",
           "A 20,000 sq ft showroom where you can compare choices first-hand.",
           "A demo centre with product trials across a variety of cuisines."]
    body = hero("About us · Since 1977", "From an SJP Road shop to <em>living kitchens</em>",
                "KitchenWhiz is the commercial kitchen brand of Unique Steel Products, a Bengaluru family business now in its second generation. Close to 100 people cover design, projects, sales, manufacturing and service.",
                photo("showroom.jpg", "KitchenWhiz showroom in Bommasandra", 1400, 933, "Our showroom, Bommasandra"))
    body += '''<section class="manifesto"><div class="wrap">
<div><p class="eyebrow">We live kitchens</p><h2>Kitchens are in our blood</h2></div>
<div><blockquote>Ever since we started in 1977, we have been helping restaurants and other commercial establishments build and maintain their kitchens, and been an active part of their growth. We also know that for this industry, <em>downtime is perilous</em>. So we make sure our kitchens don't just evolve: they stay living, breathing ones. Each of our kitchens is a living entity which we nurture with all our heart.</blockquote><cite>Be a part of our living kitchens</cite></div>
</div></section>
<section class="story"><div class="wrap split">
<div><p class="eyebrow">Our story</p><h2>A Bengaluru family business</h2>
<div class="prose" style="margin-top:18px"><p>Shabbir Madraswala started Trade Links Corporation in 1977 from a small shop on SJP Road, trading hardware, tools and safety products. Shireen Madraswala later took charge of sales and customer relationships, and built the trust the business still runs on.</p>
<p>Today the company is led by Huzefa Madraswala. Our aim is simple: to stay at the forefront of commercial kitchens, and be an invaluable part of our clients' living kitchens.</p></div>
<p class="facility-note">Factory, 20,000 sq ft showroom and warehouse together on one campus in Bommasandra.</p></div>
<div><ul class="timeline">
<li><b>1977</b><span><strong>Trade Links Corporation</strong>A small trading shop on SJP Road, Bengaluru.</span></li>
<li><b>1988</b><span><strong>Into manufacturing</strong>A move to an industrial shed in Bommasandra to build stainless-steel stoves, then commercial kitchen equipment. KitchenWhiz is born.</span></li>
<li><b>2003</b><span><strong>The next generation</strong>Huzefa Madraswala joins with an industrial engineering background and brings in new systems. He leads the company today.</span></li>
<li><b>Today</b><span><strong>Four brands and the UNOX Lounge</strong>KitchenWhiz, Barwhiz, HeatKO and USP, plus Bengaluru's UNOX Lounge, all under one roof.</span></li>
</ul></div></div></section>
<section id="advantage"><div class="wrap two">
<div><p class="eyebrow">The KitchenWhiz advantage</p><h2>Why kitchens choose us</h2><p class="lede">One partner who designs, builds, supplies and services, with a factory and showroom in the same place.</p></div>
<div>''' + ul(adv, "list-cols\" style=\"columns:1") + '''</div>
</div></section>
<section class="trusted"><div class="wrap"><p class="eyebrow">Trusted by</p><h2 class="trusted-title">Hotels, clubs, chains and neighbourhood favourites</h2>''' + _logos() + '''</div></section>
'''
    body += cards([("/commercial-kitchens", "Commercial kitchens", "How we plan and build a kitchen"),
                   ("/showroom", "Showroom", "20,000 sq ft and a demo centre"),
                   ("/living-kitchens", "Projects", "Kitchens we've built")], "Next", "See our work").replace('style="padding-top:0"', "", 1)
    return dict(path="/about-us", file="about-us.html", title="About KitchenWhiz | Commercial Kitchen Makers in Bangalore since 1977",
                desc="KitchenWhiz (Unique Steel Products) has built commercial kitchens in Bengaluru since 1977: a family business with its own factory, a 20,000 sq ft showroom and a warehouse in Bommasandra and close to 100 people.",
                body=body, crumbs=[("/", "Home"), (None, "About us")],
                ld=[{"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + "/about-us", "about": {"@id": SITE + "/#business"}}])


def _logos():
    home = read("home.html")
    a = home.find('<ul class="logos">')
    b = home.find("</ul>", a) + 5
    return home[a:b].replace('src="images/', 'src="/images/')


def p_contact():
    body = '''<section class="page-hero"><div class="wrap"><p class="eyebrow">Contact</p><h1>Tell us what you're <em>building</em></h1>
<p class="lede">Call, write or visit. Share your floor plan, cuisine and covers per day, and we'll come back with a layout and next steps.</p>
<div class="contact-grid">
<div><span class="label">Call or WhatsApp</span><div class="big"><span class="phone"><a href="tel:+919902014700" style="text-decoration:none">99020 14700</a><a class="wa" href="https://wa.me/919902014700" target="_blank" rel="noopener" aria-label="WhatsApp 99020 14700"><svg viewBox="0 0 32 32" width="34" height="34" aria-hidden="true"><circle cx="16" cy="16" r="16" fill="#25D366"/><path d="M16 7.5a8.5 8.5 0 0 0-7.3 12.8L7.5 24.5l4.3-1.1A8.5 8.5 0 1 0 16 7.5z" fill="none" stroke="#fff" stroke-width="1.8" stroke-linejoin="round"/><path d="M13.2 12.2c.3-.3.7-.3.9 0l.8 1.4c.2.3.1.6-.1.9l-.5.5c.5 1.1 1.4 2 2.5 2.5l.5-.5c.3-.2.6-.3.9-.1l1.4.8c.3.2.3.6 0 .9l-.6.7c-.5.5-1.3.6-2 .3a8 8 0 0 1-4.3-4.3c-.3-.7-.2-1.5.3-2z" fill="#fff"/></svg></a></span><span class="phone"><a href="tel:+919902014702" style="text-decoration:none">99020 14702</a></span></div><p class="wa-text"><a href="https://wa.me/919902014700" target="_blank" rel="noopener">Message us on WhatsApp</a></p></div>
<div><span class="label">Email</span><div class="big"><a href="mailto:info@kitchenwhiz.in" style="text-decoration:none">info@kitchenwhiz.in</a></div><p>Send drawings, photos of your site or an equipment list.</p></div>
<div><span class="label">Showroom &amp; factory</span><div class="big">235/E Bommasandra Industrial Area, Phase 3</div><p>Bengaluru, Karnataka 560099 · <a href="''' + MAPS + '''" target="_blank" rel="noopener">Directions on Google Maps</a></p></div>
<div><span class="label">Opening hours</span><div class="big">Mon – Sat<br>9:00 am – 5:30 pm</div><p>Closed on Sundays. Call ahead for a demo slot.</p></div>
</div>
<iframe class="map" title="Map to KitchenWhiz, Bommasandra" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=12.8158287,77.6942781&amp;z=15&amp;output=embed"></iframe>
</div></section>
<section class="band"><div class="wrap two">
<div><p class="eyebrow">Getting a quote</p><h2>What to send us</h2><p class="lede">The more we know up front, the faster we can come back with a layout and an equipment list.</p></div>
<div>''' + ul(["Floor plan or a sketch with dimensions", "Photos or a video of the site", "Cuisine and menu style",
               "Covers per day, or orders per hour for delivery", "Gas, power and water points if already fixed",
               "Your budget range and opening date"], 'list-cols" style="columns:1') + '''
<p class="clients-line">Brand enquiries: Barwhiz <a href="mailto:barwhizindia@gmail.com">barwhizindia@gmail.com</a> · HeatKO <a href="mailto:heatko.india@gmail.com">heatko.india@gmail.com</a> · USP Ecoline <a href="mailto:uspecoline@gmail.com">uspecoline@gmail.com</a></p></div>
</div></section>'''
    return dict(path="/contact", file="contact.html", title="Contact KitchenWhiz | Commercial Kitchen Equipment, Bommasandra, Bangalore",
                desc="Contact KitchenWhiz: call or WhatsApp 99020 14700, email info@kitchenwhiz.in, or visit our showroom and factory at 235/E Bommasandra Industrial Area, Phase 3, Bengaluru 560099. Mon–Sat 9–5:30.",
                body=body, crumbs=[("/", "Home"), (None, "Contact")], no_cta=True,
                ld=[{"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/contact", "about": {"@id": SITE + "/#business"}}])


def p_showroom():
    body = hero("Showroom & demo centre · Bommasandra, Bengaluru", "Cook on it <em>before</em> you buy it",
                "20,000 sq ft of Indian and international commercial kitchen equipment for any cuisine and any kind of food service, with a demo centre for live trials. Bring your chef and test the line.",
                photo("showroom.jpg", "KitchenWhiz showroom with burner ranges and cooking lines", 1400, 933, "KitchenWhiz showroom, Bommasandra"),
                [("/contact", "Book a visit", "btn-rose"), (MAPS, "Get directions", "btn-line")])
    body += '''<section class="band"><div class="wrap">
<div class="facts" style="margin-top:0">
<div><h3>Demo centre</h3><p>Product trials across a variety of cuisines, plus UNOX oven demos.</p></div>
<div><h3>100+ brands</h3><p>Indian and imported equipment, plus global sourcing for anything we don't stock.</p></div>
<div><h3>Factory on site</h3><p>See your custom equipment being built.</p></div>
</div></div></section>
<section><div class="wrap partners">
<div><p class="eyebrow">What you'll find</p><h2>The best of India and the world</h2><p class="lede">We represent major Indian and global equipment makers alongside our own brands.</p>
<div class="marks"><span>UNOX</span><span>Hoshizaki</span><span>Winterhalter</span><span>Butler</span><span>Trufrost</span><span>Aluids</span><span class="more">+ 100 more</span></div></div>
<div class="unox"><p class="eyebrow">At our Bommasandra showroom</p><h3>The UNOX Lounge, Bengaluru</h3><p>Built with UNOX, the lounge lets chefs try combi, convection and speed ovens in live demonstrations before they buy.</p><p><a href="/contact" style="color:var(--on-band)">Book a demo →</a></p></div>
</div></section>
<section style="padding-top:0"><div class="wrap"><p class="eyebrow">Barwhiz bar studio</p><h2>Stand behind the bar</h2><p class="lede">More than 10 <a href="/barwhiz">Barwhiz cocktail station</a> designs, set up as working bars.</p>
<div class="duo">''' + photo("bar-studio.jpg", "Barwhiz bar studio with cocktail stations", 507, 900, "Barwhiz bar studio", lazy=True) + \
        photo("orbit-station.jpg", "The Orbit, a curved custom cocktail station", 703, 420, "Custom curved station", "photo plate", lazy=True) + '''</div></div></section>
<section class="band"><div class="wrap two">
<div><p class="eyebrow">Visit</p><h2>Plan your visit</h2></div>
<div class="prose"><p><strong>Address:</strong> 235/E Bommasandra Industrial Area, Phase 3, Bengaluru, Karnataka 560099. <a href="''' + MAPS + '''" target="_blank" rel="noopener">Google Maps</a></p>
<p><strong>Hours:</strong> Monday to Saturday, 9:00 am to 5:30 pm. Closed on Sundays.</p>
<p><strong>Demos:</strong> call <a href="tel:+919902014700">99020 14700</a> to book a slot, so the right equipment is set up and a specialist is free.</p></div>
</div></section>'''
    faqs = [("How big is the KitchenWhiz showroom?",
             "20,000 sq ft, after our recent expansion, with our factory and warehouse on the same campus."),
            ("What can I see there?",
             "Indian and imported equipment for every kind of kitchen, our own KitchenWhiz, Barwhiz, HeatKO and USP ranges, the UNOX Lounge for oven demos, and the Barwhiz bar studio with more than 10 cocktail station designs."),
            ("Can my chef cook on the equipment?",
             'Yes. The demo centre is set up for live trials across a variety of cuisines. Call <a href="tel:+919902014700">99020 14700</a> to book a slot so the right equipment is ready.'),
            ("When is the showroom open?",
             'Monday to Saturday, 9:00 am to 5:30 pm, at 235/E Bommasandra Industrial Area, Phase 3, Bengaluru 560099. Closed on Sundays.')]
    body += faq_html(faqs, "Showroom: common questions")
    return dict(path="/showroom", file="showroom.html", og="showroom.jpg",
                title="Commercial Kitchen Equipment Showroom in Bangalore | KitchenWhiz",
                desc="Visit KitchenWhiz's 20,000 sq ft commercial kitchen equipment showroom and demo centre in Bommasandra, Bangalore. Try UNOX ovens in the UNOX Lounge and Barwhiz cocktail stations before you buy.",
                body=body, crumbs=[("/", "Home"), (None, "Showroom")], faqs=faqs)


def p_living():
    home = read("home.html")
    a = home.find('<div class="gallery">')
    b = home.find("</div>", a) + 6
    gallery = home[a:b].replace('src="images/', 'src="/images/')
    body = f'''<section class="page-hero" style="padding-bottom:0"><div class="wrap"><p class="eyebrow">Our living kitchens · Projects</p>
<h1>Kitchens we've <em>built</em></h1>
<p class="lede">A few of the kitchens and bars we have designed, built and installed across Bengaluru, from five-star hotels and microbreweries to pizzerias, bakeries and QSR chains.</p>
{gallery}</div></section>
<section><div class="wrap"><p class="eyebrow">Clients</p><h2>Kitchens we've equipped</h2>
{stores(list(STORES), "stores")}</div></section>
<section class="trusted"><div class="wrap"><p class="eyebrow">Trusted by</p><h2 class="trusted-title">Hotels, clubs, chains and neighbourhood favourites</h2>{_logos()}</div></section>
'''
    body += cards([(f'/{s["slug"]}', s["short"], s["eq_lede"]) for s in SECTORS], "By format", "Find your kind of kitchen").replace('style="padding-top:0"', "", 1)
    return dict(path="/living-kitchens", file="living-kitchens.html", og="p-geist.jpg",
                title="Our Projects: Commercial Kitchens We've Built in Bangalore | KitchenWhiz",
                desc="Commercial kitchens and bars built by KitchenWhiz in Bengaluru: Taj West End, Sheraton, DoubleTree by Hilton, MTR, Toit, Geist, Glen's Bakehouse, Brik Oven, Milano and more.",
                body=body, crumbs=[("/", "Home"), (None, "Projects")])


def p_kitchens():
    home = read("home.html")
    a = home.find('<div class="kitchens">')
    b = home.find("</div>\n  </div>\n</section>", a) + 6
    grid = home[a:b].replace('src="images/', 'src="/images/')
    body = hero("Commercial kitchen design & setup · Bangalore", "Commercial kitchens, <em>built</em> to your layout",
                "We plan, design, build and maintain commercial kitchens and bars across Bengaluru. You work with one partner from the first site visit to after-sales service, instead of coordinating a designer, a fabricator and a dozen suppliers.",
                photo("p-geist.jpg", "Geist Brewing Co. kitchen line built by KitchenWhiz", 1300, 975, "Geist Brewing Co."),
                extra=pills("Choose your kitchen", [(f'/{s["slug"]}', s["short"]) for s in SECTORS]))
    body += f'''<section class="sectors" id="formats"><div class="wrap"><p class="eyebrow">Commercial kitchen solutions</p><h2>Every format, every cuisine</h2>
<p class="lede">Pick your kind of kitchen to see the equipment we supply, a KitchenWhiz original built for it, and the clients we've set up.</p>
{grid}</div></section>
<section class="band"><div class="wrap"><p class="eyebrow">How we work</p><h2>One team from drawing to first service</h2>{STEPS}{RENDERS}</div></section>
'''
    body += faq_html(COMMON_FAQ, "Planning a kitchen: common questions")
    return dict(path="/commercial-kitchens", file="commercial-kitchens.html", og="p-geist.jpg",
                title="Commercial Kitchen Design & Setup in Bangalore | KitchenWhiz",
                desc="Commercial kitchen design and turnkey setup in Bangalore: consulting, layout and MEP, 3D drawings, stainless steel fabrication, installation, training and service. For restaurants, hotels, bakeries, cafés, bars and cloud kitchens.",
                body=body, crumbs=[("/", "Home"), (None, "Commercial kitchens")], faqs=COMMON_FAQ,
                ld=[{"@context": "https://schema.org", "@type": "Service", "name": "Commercial kitchen design and setup",
                     "serviceType": "Commercial kitchen design, equipment supply and installation",
                     "provider": {"@id": SITE + "/#business"}, "areaServed": [{"@type": "City", "name": "Bengaluru"}], "url": SITE + "/commercial-kitchens"}])


GT_FEATURE = '''<div class="feature"><div class="badge">GT</div><div><p class="eyebrow">Featured</p><h3>Stainless steel grease traps</h3><p>Keep fats, oils and grease out of your drains. <a href="/grease-trap">Specifications →</a></p></div></div>'''


def p_equipment():
    make = ["Stainless steel work tables", "Commercial burner ranges", "Chinese cooking ranges", "Tandoors", "Hot plates and griddles",
            "Kitchen sinks and dishwash tables", "Storage racks and cabinets", "Exhaust hoods and ducting", "Fire suppression systems",
            "Grease traps and drain gratings", "Commercial refrigeration", "Combi and convection ovens", "Dishwashers",
            "Bain maries and food display", "Bakery equipment", "Bar and cocktail stations"]
    home = read("home.html")
    a = home.find('<div class="brands">') + len('<div class="brands">')
    brands = home[a:home.find("</div>\n  </div>\n</section>", a)].strip()
    body = hero("Commercial kitchen equipment · Bangalore", "Commercial kitchen <em>equipment</em>",
                "Stainless steel equipment made in our Bommasandra factory, our own brands for bars, steamers and standard furniture, and 100+ Indian and imported brands, for restaurants, hotels and food businesses across Bengaluru and Karnataka.",
                photo("p-line.jpg", "Stainless steel cooking line in a commercial kitchen", 975, 1300, cls="photo tall"),
                [("/contact", "Ask for a quote", "btn-rose"), ("/showroom", "Visit the showroom", "btn-line")],
                extra=pills("Explore", [("/kw-originals", "KitchenWhiz (custom built)")] + BRAND_MENU[1:] +
                                       ([("/grease-trap", "Grease traps")] if SHOW_GREASE_TRAP else []) + [("/showroom", "Showroom & demo centre")]))
    body += f'''<section class="band"><div class="wrap two">
<div><p class="eyebrow">What we make and supply</p><h2>For every station</h2><p class="lede">Custom pieces are built to your sizes in SS202 or SS304. <a href="/kw-originals">See KW Originals →</a></p>
{GT_FEATURE if SHOW_GREASE_TRAP else ""}</div>
<div>{ul(make)}</div></div></section>
<section id="brands"><div class="wrap"><p class="eyebrow">Brands by Unique Steel Products</p><h2>Four brands, one factory</h2><div class="brands">{brands}</div></div></section>
<section id="brands-we-supply" style="padding-top:0"><div class="wrap partners">
<div><p class="eyebrow">Brands we bring in</p><h2>The best of India and the world</h2><p class="lede">We represent major Indian and global equipment makers, and source anything we don't stock from anywhere in the world.</p>
<div class="marks"><span>UNOX</span><span>Hoshizaki</span><span>Winterhalter</span><span>Butler</span><span>Trufrost</span><span>Aluids</span><span class="more">+ 100 more</span></div></div>
<div class="unox"><p class="eyebrow">At our Bommasandra showroom</p><h3>The UNOX Lounge, Bengaluru</h3><p>Try combi, convection and speed ovens in a live demonstration before you buy.</p><p><a href="/showroom" style="color:var(--on-band)">About the showroom →</a></p></div>
</div></section>
'''
    return dict(path="/equipment", file="equipment.html", og="p-line.jpg",
                title="Commercial Kitchen Equipment Supplier in Bangalore | KitchenWhiz",
                desc="Commercial kitchen equipment in Bangalore: SS work tables, burner ranges, tandoors, sinks, exhaust hoods, grease traps, refrigeration, ovens and dishwashers. Made in our factory or supplied from 100+ brands.",
                body=body, crumbs=[("/", "Home"), (None, "Equipment")])


def p_originals():
    items = [("Robata grill", "Born out of the Japanese idea of fireside cooking. It grills all kinds of food, and diners get to watch what is being made.", "/restaurants"),
             ("Six burner range", "The workhorse of any commercial kitchen: one versatile range that handles a wide variety of tasks.", "/cafe"),
             ("Bain marie", "Works like a traditional water bath or double boiler, keeping food at the right serving temperature.", "/cloud-qsr-central-kitchen"),
             ("Prep counter", "Keeps everything needed for pizzas and sandwiches in one organised station, so the chef can assemble quickly.", "/pizzeria"),
             ("Cocktail station", "Keeps every supply for mixed drinks in one organised station, so bartenders serve faster.", "/barwhiz"),
             ("Bakery trolley", "Stacks trays so product moves easily before and after baking.", "/bakery")]
    cs = "".join(f'<a href="{h}"><b>{t}</b><span>{d}</span><span class="go">Where it\'s used →</span></a>' for t, d, h in items)
    body = hero("KitchenWhiz · KW Originals · Custom built", "KitchenWhiz <em>custom-built</em> kitchen equipment",
                "Our in-house design team studies the ergonomics, aesthetics, function and pain points of each kitchen to build equipment that performs. We keep improving the designs from client feedback and current trends.",
                photo("p-prep.jpg", "Custom stainless steel prep station built by KitchenWhiz", 975, 1300, cls="photo tall"),
                [("/contact", "Discuss a custom build", "btn-rose"), ("/showroom", "See it in the showroom", "btn-line")])
    body += f'''<section class="band"><div class="wrap"><p class="eyebrow">KW Originals</p><h2>Designs we're known for</h2><div class="cards">{cs}</div></div></section>
<section><div class="wrap"><p class="eyebrow">Built to your site</p><h2>Drawn in 3D, built to the millimetre</h2>
<p class="lede">Every custom line is drawn in 3D and matched to your site before fabrication starts in our factory, in SS202 or SS304.</p>{RENDERS}</div></section>
'''
    return dict(path="/kw-originals", file="kw-originals.html", og="line-render-1.jpg",
                title="KitchenWhiz Custom-Built Stainless Steel Kitchen Equipment | KW Originals",
                desc="KW Originals: custom-built stainless steel commercial kitchen equipment made in Bangalore: robata grills, six burner ranges, bain maries, prep counters, cocktail stations and bakery trolleys, built to your exact sizes.",
                body=body, crumbs=[("/", "Home"), ("/equipment", "Equipment"), (None, "KitchenWhiz – KW Originals")])


def p_greasetrap():
    spec = [("Model", "GT53H3"), ("Overall size", "500 × 350 × 300 mm"), ("Holding volume", "35 litres"),
            ("Flow capacity", "550 litres per hour"), ("Inlet coupling", '1½" CPVC'), ("Outlet coupling", '1½" CPVC'),
            ("Grease exit coupling", '⅜" CPVC'), ("Material", "Stainless steel")]
    rows = "".join(f"<tr><th>{e(a)}</th><td>{e(b)}</td></tr>" for a, b in spec)
    parts = ul(["Top stainless steel lid with handles", "SS perforated basket with handle, catches food solids",
                "SS baffle plate, slows the flow so grease separates", 'Grease collecting tray with ⅜" exit coupling',
                '1½" inlet and outlet couplings'], 'list-cols" style="columns:1')
    faqs = [("What does a grease trap do?",
             "It slows down the wastewater from sinks and dishwash areas so that fats, oils and grease float and separate before the water reaches the drain. That prevents blocked drains, bad smells and overflowing sewer lines."),
            ("Where is a grease trap installed?",
             "Usually under or next to the pot wash and dishwash sinks, before the line joins the main drain, where it can be opened easily for cleaning."),
            ("How often should it be cleaned?",
             "Empty the solids basket daily, and drain the collected grease regularly; a busy kitchen needs it more often. Clean the whole unit when grease builds up on the baffles."),
            ("Do you make other sizes?",
             'Ask us. Call <a href="tel:+919902014700">99020 14700</a> or email <a href="mailto:info@kitchenwhiz.in">info@kitchenwhiz.in</a> with your sink layout and daily volume and we will suggest the right size.')]
    body = hero("USP Essentials · Grease traps", "Stainless steel <em>grease traps</em>",
                "A stainless steel grease trap for commercial kitchens that stops fats, oils and grease before they reach your drains. It has a removable solids basket, a baffle plate and its own grease collecting tray, and is made in our Bengaluru factory.",
                photo("grease-trap-open.jpg", "USP stainless steel grease trap with the lid removed, showing the perforated basket and baffle plates", 1200, 780),
                [("/contact", "Ask for a quote", "btn-rose"), (WA, "WhatsApp us", "btn-line")])
    body += f'''<section class="band"><div class="wrap two">
<div><p class="eyebrow">Specifications</p><h2>GT53H3 grease trap</h2><table class="spec">{rows}</table></div>
<div><p class="eyebrow">How it's built</p><h2>Parts</h2>{parts}
<div class="duo" style="grid-template-columns:1fr">{photo("grease-trap-closed.jpg", "USP stainless steel grease trap with lid closed", 1200, 790, lazy=True)}</div></div>
</div></section>
'''
    body += faq_html(faqs, "Grease traps: common questions")
    body += cards([("/usp-essentials", "USP Essentials", "Drain gratings, trolleys, bins and more"),
                   ("/equipment", "All equipment", "What we make and supply"),
                   ("/cloud-qsr-central-kitchen", "Cloud & central kitchens", "High-volume kitchens")], "Related", "More for your kitchen")
    return dict(path="/grease-trap", file="grease-trap.html", og="grease-trap-open.jpg",
                title="Stainless Steel Grease Trap for Commercial Kitchens | Bangalore | KitchenWhiz",
                desc="Stainless steel grease trap for restaurant and commercial kitchens, made in Bangalore: 35 litre, 550 LPH, 500×350×300 mm with solids basket, baffle plate and grease tray. Ask KitchenWhiz for a quote.",
                body=body, crumbs=[("/", "Home"), ("/equipment", "Equipment"), (None, "Grease traps")], faqs=faqs)
