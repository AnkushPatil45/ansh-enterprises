# Ansh Enterprises Website

Static showcase website for **Ansh Enterprises**, Dhule — cold-pressed oils and natural products.
Hosted free on GitHub Pages. Orders happen via WhatsApp links — no cart, no server, no payment gateway.

---

## Repo structure

```
/
  index.html              — single-page site
  products.json           — product catalog (edit this to update products)
  sitemap.xml / robots.txt
  assets/
    css/styles.css        — all brand styles + CSS variables
    js/main.js            — renders products, filter, WhatsApp links
    img/
      logo.svg            — light-background logo
      logo-reversed.svg   — dark-background logo (hero, OG image)
      favicon.svg         — leaf-drop mark
      products/           — product photos (WebP, named by product id)
  scripts/                — local Python automations (Vyapar export → site)
  data/                   — Vyapar exports go here (git-ignored — never commit)
```

---

## How to update products

1. Open `products.json` in any text editor.
2. Find the product by `"id"` or `"name"`.
3. Edit `"description"`, `"size"`, or set `"available": false` to mark out-of-stock.
4. To add a new product, copy an existing block and give it a unique `"id"` (lowercase, hyphens only).
5. To change the sizes a product is sold in, edit its `"sizes"` array (e.g. `["250 ml","500 ml","1 L"]`). One size shows as plain text; multiple sizes render a dropdown the customer picks from before adding to their order.
6. **Never add a `"price"` field.** Prices are intentionally hidden on the site.
7. Save the file and commit + push (see deploy steps below).

---

## How to add a product photo

1. Save the image as **WebP** (use squoosh.app or similar — keep under 150 KB).
2. Name it to match the product `"id"` — e.g. `groundnut-oil.webp`.
3. Drop it in `assets/img/products/`.
4. The `"image"` path in `products.json` should already match: `"assets/img/products/groundnut-oil.webp"`.

---

## Deploy to GitHub Pages

1. Create a GitHub account / repo named `anshenterprises` (or the username confirmed by owner).
2. Push this folder to the `main` branch.
3. Go to **Settings → Pages → Source → Deploy from branch → main → / (root)**.
4. Site goes live at `https://anshenterprises.github.io` within ~2 minutes.
5. To use a custom domain (e.g. `anshenterprises.in`): add a `CNAME` file containing just the domain, then configure DNS at your registrar.

**To update the site:** edit files locally → `git add` → `git commit` → `git push`. GitHub Pages rebuilds automatically.

---

## Config

Two things to update when the live site is ready:

| What | Where |
|---|---|
| GitHub Pages base URL | `assets/js/main.js` → `CONFIG.baseUrl` |
| Google Analytics 4 ID | `assets/js/main.js` → `CONFIG.ga4Id` (leave blank to disable) |
| Google Maps embed | `index.html` → a working address-based map iframe is wired. For the exact verified-listing pin, replace its `src` with the one from Google Maps → Share → Embed a map |
| Social share image | `assets/img/og-image.png` (1200×630) is in place and referenced by the OG/Twitter meta tags |
| Instagram / Google links | `index.html` footer + `sameAs` in the LocalBusiness schema use placeholder URLs — replace with the real handles |

---

## Logo & image assets

Active logo files (swap these if the design changes):
- `assets/img/logo-mark.svg` — the अ mark only, used in the header
- `assets/img/logo-stacked-reversed.svg` — full stacked lockup on forest, used in the hero
- `assets/img/logo.svg` / `assets/img/logo-reversed.svg` — full horizontal lockups (spare, not currently wired)
- `assets/img/favicon.svg` — the small leaf-drop mark
- `assets/img/og-image.png` — 1200×630 social share image (regenerate with `scripts`-style tooling if branding changes)

Logo contrast rules (from brand brief):
- Light backgrounds: wordmark = `#173404`, veins = forest (thick), tagline = `#993C1D`
- Dark backgrounds: wordmark = cream `#FBF6EA`, veins = gold `#EF9F27`, tagline = gold
- Never white/gold text on cream. Never forest veins on forest element.

---

## Automation scripts (`/scripts`)

See `scripts/` folder. Each script reads Vyapar exports from `data/` — **never edit Vyapar directly**.

| Script | What it does |
|---|---|
| `update_products.py` | Vyapar item export → updates `products.json` (availability, sizes) |
| `reorder_list.py` | Sales export → WhatsApp reorder messages for repeat customers |
| `weekly_summary.py` | Sales export → weekly top sellers / slow movers report |

Run with: `python3 scripts/update_products.py`

---

## Contact details (keep consistent everywhere)

- **WhatsApp / Phone:** +91 82650 11431 (international format for wa.me: `918265011431`)
- **Address:** 31, Garud Colony, Nakane Rd, opp. Sakar Glass House, Deopur, Dhule, MH 424002
- **Hours:** 9 AM to 10 PM, all 7 days
- **Delivery & payment:** Home delivery in Dhule on orders above ₹500, confirmed with UPI payment in advance.

## How customers order (multi-product basket)

The site has no cart-and-checkout in the usual sense and still needs no server. Customers tap **Add to order** on any products (choosing a size first). Items collect in a floating **Your order** basket (saved in their browser via localStorage). When ready, **Send order on WhatsApp** opens one pre-filled WhatsApp message listing every item with its size and quantity, so they never have to message product-by-product.
