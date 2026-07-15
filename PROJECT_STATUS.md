# PROJECT_STATUS.md — Ansh Enterprises (project status & context)

> **Read this first if you are picking the project back up.** It captures the
> current state, the decisions already made, and what's left. The full spec is in
> `PROJECT_BRIEF.md` (source of truth for brand/colors/voice). This file records what
> has actually been built and changed since then.
>
> **Local project folder:** `/Users/ankush/Documents/Ansh Enterprises`
> **Last updated:** 2026-07-07 — **SITE IS LIVE: https://ankushpatil45.github.io/ansh-enterprises/**

## Logo decision (current)
- **The live logo on the website and brochures is the ORIGINAL अ mark** (अ + gold leaf-drop):
  `assets/img/logo-mark.svg` (header), `assets/img/logo-stacked-reversed.svg` (hero/brochure),
  `assets/img/favicon.svg`, `assets/img/og-image.png`.
- We explored a redesign (a folded-ribbon "A") and many other concepts; the owner chose to
  **revert to the original अ**. All explorations are **parked, not used**, in:
  `source/brand/logo-alternates/` (A-based) and `source/brand/logo-concepts/` (sheets +
  non-letter ideas). Nothing there is referenced by the site or brochures.
- Asset links in `index.html` are cache-busted with `?v=` (css `?v=11`, js `?v=11`, logos `?v=9`;
  product images via `assetVersion` in main.js CONFIG) — bump when a file changes.

## Sync status
- Repo: **github.com/AnkushPatil45/ansh-enterprises** (private). Commits are kept clean / AI-free.
- Local and remote are **in sync**; every push to main auto-deploys the LIVE site in ~1 min.
- **Marketing kit (`marketing/`):** EN + Marathi brochures (JPG + tappable PDF), A6 review card,
  4 review sticker designs (all QRs machine-verified to g.page/r/CT4JK8Ze2bKzEBE/review).
- **Review link** is wired on the site ("Leave a review") and in both brochure PDFs.
- **About section** now has a custom wooden-ghani illustration (assets/img/ghani-illustration.webp);
  Clay Utensils uses a custom terracotta illustration — every product has an image.
- **35 products**, sizes synced to the owner's Vyapar inventory export (2026-06-30); Zankar has
  no size by design; prices remain hidden everywhere.

---

## 1. What this is
A static, free-to-host (GitHub Pages) showcase site for **Ansh Enterprises** — a Dhule
cold-pressed oil & natural products store. Ordering is via **pre-filled WhatsApp links**
(no server, no payment gateway). **Prices are never shown** on the site. Brand is **Ansh
Enterprises**; "Orgatma" is only a supplier (mentioned once in About, never as the brand).

Stack: plain HTML + CSS + vanilla JS, no build step. Catalog driven by `products.json`.

**The site is LIVE** at https://ankushpatil45.github.io/ansh-enterprises/ (public repo, GitHub Pages from main). Every push to main auto-deploys in ~1 minute. A custom domain (e.g. anshenterprises.in) can be added later via a CNAME file + registrar DNS.

---

## 2. Current status — DONE
- **Full single-page site built** (`index.html`): header, hero, sticky search + category
  chips, product grid, trust strip, about, reviews, contact (with Google map), footer.
- **Brand system** in `assets/css/styles.css` (CSS variables for the locked colors/fonts
  from the brief; Playfair Display + Poppins + Noto Serif Devanagari).
- **Logos** (real, from the owner's design) in `assets/img/`:
  - `logo-mark.svg` — the अ mark only → used in the **header**
  - `logo-stacked-reversed.svg` — full stacked lockup on forest → **hero**
  - `logo.svg` / `logo-reversed.svg` — horizontal lockups (spare, not wired)
  - `favicon.svg`, `og-image.png` (1200×630 social share image, generated)
- **products.json** — 31 products with `sizes` arrays (multi-size → dropdown on card).
- **main.js** — renders products, search, category filter, **size selection**, a
  client-side **order basket** (localStorage) that builds ONE combined WhatsApp message,
  injects per-product `Product` JSON-LD, and loads GA4.
- **WhatsApp / multi-product ordering:** "Add to order" collects items in a floating
  "Your order" basket → "Send order on WhatsApp" opens one pre-filled message.
- **SEO:** title/meta, `LocalBusiness` JSON-LD, per-product `ItemList`/`Product` JSON-LD
  (built in main.js), Open Graph + Twitter tags, `sitemap.xml`, `robots.txt`.
- **Analytics:** GA4 live — `CONFIG.ga4Id = 'G-YXW401W2XD'` in `main.js`.
- **Cache-busting:** CSS/JS are included as `styles.css?v=2` / `main.js?v=2`. **Bump the
  `v` number whenever you edit those files** so returning visitors get the update.
- **Product photos:** 30 of 31 products have optimized WebP images (~1.2 MB total).
- **Product descriptions:** all 31 rewritten as original Ansh Enterprises copy (referencing
  supplier facts from orgatma.com, but our own wording, supplier-neutral, no em dashes).
- **Catalog freshness:** `main.js` fetches `products.json?t=<timestamp>` so product edits show
  immediately for returning visitors (no stale cache). Asset links are at `?v=4`.
- **34 products.** Groundnut, Mustard, Sesame each split into **Gold** + **Premium** grades
  (separate cards). Gold = lighter/clearer; Premium = denser/wood-pressed. Real photos for
  both Groundnut grades + all Gold grades; Mustard & Premium and Sesame Premium use a
  `premium-coming-soon.webp` placeholder until the owner sends those two photos.
- **Image backgrounds:** every product is a **transparent cutout** (rembg, `scripts`/scratch) so
  there's no rectangle behind it — EXCEPT the 3 soaps, which keep their original decorative photo
  (owner's choice). product-card image bg is white. Hours now **9 AM to 10 PM, all 7 days**.
- **Brochures (in `marketing/`):** high-res JPG + clickable PDF, English **and Marathi**,
  rendered from HTML via headless Chromium (real Playfair/Poppins/Mukta fonts, all products,
  Gold/Premium, QR + tappable order link). Generator: `scripts/make_brochure_html.py`
  (needs `.venv` with playwright+qrcode and `playwright install chromium`).

---

## 3. Key decisions already made (don't re-litigate)
- **Prices hidden** everywhere; orders/quotes happen on WhatsApp. No `price` field in JSON.
- **Phone/WhatsApp number: `8265011431`** (intl `918265011431`, display `+91 82650 11431`).
  This is the WhatsApp Business number. The old `9890581346` (owner's father's personal
  number) was removed everywhere — do not reintroduce it.
- **Payment: prepaid.** "Home delivery in Dhule on orders above ₹500, confirmed with UPI
  payment in advance." (NOT cash-on-delivery.)
- **Category named "Health Care"** (renamed from "Health Juices") — it holds the juices,
  the prash products, and Zankar pain-relief oil.
- **Logo tagline** reads **"शुद्ध · The Old Way"** (that's what the owner's final logo says).
- **No em dashes** in user-facing copy (owner prefers natural, human wording). Keep it that way.
- **Reviews** are realistic placeholders (Marathi + English, with names) until real Google
  reviews are dropped in.
- **Soap photos kept as-is** (decorative template background: rings/leaves/pedestal). An
  auto white-cutout was tried and reverted — it cropped the boxes and looked improper. If
  perfect consistency is wanted later, the owner should reshoot the 3 soaps on plain white.
- **Instagram:** `https://www.instagram.com/ansh_cold_pressed_oil`
  **Google profile:** `https://share.google/uxPhYZIj9RsNsyaWk`
  **Map:** exact embed pin is wired in the contact section.
- **Address:** 31, Garud Colony, Nakane Rd, opp. Sakar Glass House, Deopur, Dhule, MH 424002.

---

## 4. Remaining work / next steps
1. **Pending photos:** only Clay Utensils (shows 🌿 placeholder) — wire as `clay-utensils.webp`.
   Mustard/Sesame Premium photos are IN, plus a new product: **Black Sesame Oil (Premium)**
   (35 products now). Brochure text sizes were increased for mobile readability and the banner
   got a gold keyline frame. Soaps still use original photos (owner's choice).
2. **Automation scripts (`/scripts`)** — NOT built yet. From `PROJECT_BRIEF.md §6`, in
   priority order: `reorder_list.py` (highest ROI), `update_products.py`, `weekly_summary.py`,
   optional `caption_helper.py`. These read Vyapar exports from `./data/` (git-ignored).
   `scripts/optimize_images.py` already exists (image helper, not a Vyapar script).
3. ~~Deploy to GitHub Pages~~ — DONE (live). Next: optional custom domain; submit sitemap to Google Search Console; add the live URL to the Google Business Profile website field.
4. Optional polish: reshoot the 3 soaps on white; replace placeholder reviews with real
   Google reviews; consider FSSAI licence number display; back-to-top button.

---

## 5. How to run / preview locally
Static site — serve the folder and open it. Example:
```
cd "/Users/ankush/Documents/Ansh Enterprises"
python3 -m http.server 4321
# open http://localhost:4321
```
(A preview config named `ansh-site` serves it on port 4321.)

## 6. Adding / optimizing product images
Originals live in `source/product-photos/<category>/` (renamed to match products).
Optimized WebP go in `assets/img/products/` and must be named to match the `image`
field in `products.json`. (Logo/brand source files live in `source/brand/`.)
Use the helper (needs a venv with Pillow; numpy only for `--whiten`):
```
python3 -m venv .venv && .venv/bin/pip install Pillow numpy
.venv/bin/python scripts/optimize_images.py "Product Images/SOURCE.jpg" assets/img/products/NAME.webp
# add --whiten if the source has a single light/grey backdrop to turn white
```

## 7. File map
```
index.html              single-page site (cache-busted asset links ?v=N)
products.json           catalog: store info, categories[], products[] (sizes[], no price)
sitemap.xml, robots.txt
assets/css/styles.css   brand styles + CSS variables
assets/js/main.js       render, search, filter, sizes, basket, schema, GA4 (CONFIG at top)
assets/img/             logos, favicon, og-image, products/ (WebP)
scripts/                optimize_images.py (+ future Vyapar automation scripts)
data/                   git-ignored; Vyapar exports go here (never commit customer data)
source/                 originals (NOT deployed): see source/README.md
  product-photos/       renamed source photos grouped by category
  brand/                logo source set + app icons + designer master-set
PROJECT_BRIEF.md        the spec / source of truth
PROJECT_STATUS.md       this file
README.md               how to update products / deploy
```
