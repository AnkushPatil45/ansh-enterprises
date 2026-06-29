# PROJECT_BRIEF.md — ANSH ENTERPRISES

> **For developers:** Read this whole file first. It is the single source of truth for the Ansh Enterprises website and automation project. Build to this spec. Confirm before any destructive action (force-push, deleting files), before installing paid services, and before publishing anything live. Everything here is free/low-cost by design.
>
> **Local project folder:** `/Users/ankush/Documents/Ansh Enterprises`

> **BRAND NAME — READ CAREFULLY:** The brand, the store, the face, the logo, the voice, and all socials are **ANSH ENTERPRISES**. "Orgatma" is a *supplier* whose products the store resells — it is NOT the brand and must NEVER be used as the store/brand name. The owner may add or change suppliers in future, so the identity must stay supplier-independent. Orgatma may be mentioned only as a product line we stock (e.g. a small "Brands we carry: Orgatma" note), never in the logo, title, or headline branding.

---

## 0. TL;DR — what we are building

1. A **static showcase website** for Ansh Enterprises — a cold-pressed oil & natural products retail store — hosted **free on GitHub Pages**.
2. Ordering happens via **pre-filled WhatsApp links** (no cart, no payment gateway, no server). This is intentional — it is free, reliable, and matches how local customers buy.
3. A set of **local automation scripts** that bridge the store's inventory app (Vyapar) to the website and to marketing tasks, since Vyapar has **no API** (export-based workflow only).

Build the website first. Then the automation scripts.

---

## 1. The business (facts)

- **Brand name (public-facing):** ANSH ENTERPRISES
- **Tagline options:** "शुद्ध · Cold-Pressed Oils & Natural" / "Pure, the way nature intended"
- **What it is:** A retail store selling cold-pressed oils and natural/organic products. The store currently sources many products from **Orgatma** (orgatma.com, Wai, Satara) and resells them, and may add other suppliers over time. IMPORTANT: Orgatma is a supplier only — do NOT brand the site as Orgatma, do NOT link to orgatma.com as if it's ours. Mention Orgatma only as a stocked product line. The brand is Ansh Enterprises.
- **Location:** 31, Garud Colony, Nakane Rd, opposite Sakar Glass House, Deopur, Dhule, Maharashtra 424002, India
- **Phone / WhatsApp:** +91 82650 11431  (WhatsApp orders go here)
- **Hours:** Opens 9:00 AM (confirm full hours from owner; placeholder: 9 AM – 9 PM)
- **Google Business:** Claimed & verified. Current Google listing name: "ORGATMA | ANSH ENTERPRISES - Cold Pressed Oil (लाकडी घाण्याचे शुद्ध तेल) and Organic Products" (4.3★, 6 reviews). NOTE: owner is repositioning the brand to lead with ANSH ENTERPRISES; the Google name may be updated to put Ansh Enterprises first. Treat Ansh Enterprises as the brand regardless of the current listing string.
- **Run by:** Owner's parents on-site in Dhule. Owner (project lead) is remote in Canada and does all the digital/dev work.
- **Delivery:** Home delivery within Dhule on orders above ₹500. Cash or UPI on delivery.

### Audience
Mix of walk-in locals, repeat regulars, and word-of-mouth. Health-conscious families, traditional buyers, some younger urban buyers. **Most web traffic will be mobile.** Languages: English, Marathi (मराठी), Hindi. Use Marathi/Hindi touches for warmth and local SEO.

---

## 2. Products (full catalog)

Build the product grid from a `products.json` file (spec in §5). Categories and items:

**Cold-Pressed Oils:** Groundnut Oil, Sunflower Oil, Mustard Oil, Safflower Oil, Coconut Oil, Virgin Coconut Oil, Flaxseed Oil, Sesame Oil, Walnut Oil, Castor Oil, Almond Oil

**Natural Spices:** High-Curcumin Turmeric, Himalayan Rock Salt

**Natural Sweeteners:** Honey, Chemical-Free Jaggery

**A2 Ghee:** A2 Gir Cow Ghee

**Health Care:** Sugar-Free Aloe Vera Juice, Sugar-Free Amla Juice, Sugar-Free Jamun Juice, Zankar Pain Relief Oil, Dant Pankti Tooth Powder, Amla Prash, Gulkand Prash

**Hair Care:** Cold-Pressed Kalonji Oil

**Skin Care:** Neem Citronella Gomay Bar (100g), Ubtan Gomay Bar (100g bath soap), Bhimseni Kapoor Soap (100g)

**Pooja Essentials:** Deepam Oil, Bhimseni Kapoor

**Clay Utensils:** (range — confirm specific items with owner)

> **Prices: HIDDEN on the website.** Do not display prices. Order buttons ask the customer to enquire on WhatsApp. (Owner wants pricing flexibility and to drive the WhatsApp conversation.)

---

## 3. Brand system (LOCKED — use exactly)

### Colors
| Role | Name | Hex |
|---|---|---|
| Primary | Forest Green | `#173404` |
| Support | Leaf Green | `#3B6D11` |
| Accent | Gold | `#EF9F27` |
| Warm pop | Terracotta | `#D85A30` |
| Base / background | Cream | `#FBF6EA` |
| Deep text/terracotta-dark | | `#993C1D` |
| Sage (light fills) | | `#C0DD97` / `#EAF3DE` |
| Ink (body text) | | `#2C2C2A` |
| Muted text | | `#888780` |

### Typography
- **Headings / logo / product names:** "Playfair Display" (elegant serif — the "traditional" half). Load from Google Fonts.
- **Body / buttons / captions / UI:** "Inter" or "Poppins" (clean sans — the "modern" half). Load from Google Fonts.
- Sentence case for UI; product names can use Title Case as proper nouns.

### Logo rules (CRITICAL — contrast bugs to avoid)
The mark is a **leaf that doubles as an oil-drop**, with a central stem + small rib veins. The wordmark reads **ANSH ENTERPRISES** (Playfair Display), with a smaller tagline line below.
- **On light (cream) backgrounds:** circle = forest `#173404`, drop = gold `#EF9F27`, veins = **forest at full strength, thick** (stem ~2.4px, ribs ~1.8px). **Wordmark = FOREST GREEN `#173404`** (NEVER white/cream on cream — that was a bug). Tagline = terracotta `#993C1D`.
- **On dark (forest) backgrounds:** circle/leaf = cream `#FBF6EA`, drop = forest `#173404`, veins = **GOLD `#EF9F27`** (NOT forest — forest-on-forest is invisible). Wordmark = cream `#FBF6EA`, tagline = gold.
- **Tiny sizes (favicon, WhatsApp DP):** drop the wordmark, use the leaf-drop mark (preferred) or an "AE" seal only.
- **Contrast rules:** Never white/gold text on cream. Never forest veins on a forest element. Never terracotta on green. Never light text on a light background. Always verify legibility in both modes.
- The actual logo file will be provided as SVG/PNG by the owner. For now, scaffold with placeholder `logo.svg` / `logo-reversed.svg` and an `AE` `favicon.svg` using these rules so they're swappable.

### Voice
Warm but confident. Short, punchy sentences. Trust the reader. No hype, no "best in the world." Emphasize: purity, cold-pressed process, single-source sourcing, family-run, Dhule roots, no chemicals.

---

## 4. Website spec

### Stack & hosting
- **Plain HTML + CSS + vanilla JS.** No framework, no build step (keep it dead-simple and free to host).
- Host on **GitHub Pages**. Assume repo/username **`anshenterprises`** → site at `https://anshenterprises.github.io` (owner will confirm exact username at repo creation — `ansh-enterprises` or `anshenterprisesdhule` are fallbacks if taken; make this easy to change — put the base URL in one config spot). This maps cleanly to a future domain like `anshenterprises.in`.
- Mobile-first, fully responsive. Fast: optimize images (WebP, lazy-load), minimal JS.
- Works perfectly as a static site — no server, no database.

### Pages / sections (single-page is fine, with anchor nav)
1. **Header:** logo (left), nav (Products, About, Contact), a sticky "Order on WhatsApp" button.
2. **Hero:** logo/brand, tagline ("शुद्ध · Cold-Pressed · Natural"), one line of value, primary CTA "Shop on WhatsApp", secondary "Browse Products". Forest or cream background with gold accents.
3. **Category nav:** chips/tabs — Oils · Ghee · Honey & Sweeteners · Spices · Health Juices · Skin & Hair · Pooja · Clay.
4. **Product grid:** card per product from `products.json`. Card = image, name (Playfair), short description, size, and a button **"Order on WhatsApp"** (no price). Filter by category.
5. **About:** the family story, sourcing (single-source, cold-pressed process, what makes it pure), Dhule roots. Warm, human, first-person-plural.
6. **Trust strip:** "100% Natural · Family-Run · No Chemicals · Home Delivery ₹500+".
7. **Reviews:** show a few Google reviews (manual/static for now; link to the Google profile to leave a review). Include the review QR/link.
8. **Contact / footer:** address, embedded Google Map, hours, WhatsApp button, Instagram link, phone. `LocalBusiness` schema here.

### The "ordering backend" (free, no server)
Every order button is a WhatsApp deep link:
```
https://wa.me/918265011431?text=<url-encoded message>
```
Message template (no price, since prices are hidden):
```
Namaste! I'd like to order / enquire:
• Product: {{name}} ({{size}})
From the Ansh Enterprises website. My name is ____ and my area is ____.
```
A general "Shop on WhatsApp" button uses a generic message:
```
Namaste! I'd like to see your products and prices. (from Ansh Enterprises website)
```
Phone number must be in international format without `+` or spaces: `918265011431`.

### SEO (important for local discovery)
- `<title>`: "Ansh Enterprises Dhule | Cold-Pressed Oil & Natural Products | लाकडी घाणी तेल"
- Meta description with Dhule + key products + Marathi keyword.
- `schema.org` **LocalBusiness** JSON-LD: name, address, geo, phone, hours, priceRange, url, sameAs (Instagram, Google profile).
- Open Graph + Twitter card tags (so WhatsApp/FB share previews look good — use the reversed logo on forest as the OG image).
- `sitemap.xml` + `robots.txt`.
- Semantic headings; alt text on every product image (e.g. "Cold-pressed groundnut oil 1L — Ansh Enterprises Dhule").
- Target keywords: "cold pressed oil Dhule", "लाकडी घाणी तेल धुळे", "A2 gir cow ghee Dhule", "organic store Dhule", "wood pressed oil Maharashtra".

### Analytics
- Add **Google Analytics 4** (free) OR Cloudflare Web Analytics (privacy-friendly, free). Put the snippet behind a single config flag so it's easy to add the real ID later.

### Accessibility & quality bar
- Color contrast must pass (use the brand contrast rules in §3).
- Keyboard navigable, alt text everywhere, semantic HTML.
- Lighthouse target: 90+ on mobile for Performance/SEO/Accessibility.

### Repo structure (suggested)
```
/ (root)
  index.html
  /assets
    /css/styles.css
    /js/main.js            (renders products from products.json, filters, builds wa.me links)
    /img/products/...      (WebP product photos)
    logo.svg, logo-reversed.svg, favicon.svg, og-image.png
  products.json            (the catalog — edited via export, not by hand ideally)
  sitemap.xml, robots.txt
  README.md                (how to update products, how to deploy)
  CNAME                    (only when a custom domain is added later)
```

---

## 5. products.json schema

```json
{
  "store": {
    "name": "Ansh Enterprises",
    "whatsapp": "918265011431",
    "delivery_min": 500
  },
  "categories": ["Oils","Ghee","Honey & Sweeteners","Spices","Health Juices","Skin & Hair","Pooja","Clay"],
  "products": [
    {
      "id": "groundnut-oil-1l",
      "name": "Groundnut Oil",
      "category": "Oils",
      "size": "1 L",
      "description": "Wood-pressed, never heated. Keeps every nutrient where it belongs.",
      "image": "assets/img/products/groundnut-oil.webp",
      "available": true,
      "tags": ["cold-pressed","cooking"]
    }
  ]
}
```
- No `price` field (prices hidden). `main.js` builds each card + the wa.me link from this.
- Keep `id` stable and URL-safe. `available:false` → show "Currently out of stock", disable order button.
- Descriptions are supplier-neutral (describe the product, not the supplier). A "Brands we carry: Orgatma" note may appear once in the footer/about, not per-product.

---

## 6. Vyapar automation (export-based — Vyapar has NO API)

**Constraint:** Vyapar offers no public API and no Zapier. It DOES export to Excel/PDF and can sync to Google Drive / Google Sheets. So all automation is **export → script → output**. Owner will place exports in a known folder (e.g. `./data/vyapar_export.xlsx`) or a synced Google Sheet.

Build these as small, well-documented Python scripts in a `/scripts` folder (use `openpyxl`/`pandas`). Each script: read-only on the export, prints/writes clearly, never edits Vyapar.

### Script 1 — `update_products.py`
- Input: Vyapar item export (Excel/CSV) with item names, categories, stock qty, sizes.
- Output: regenerate `products.json` (preserve descriptions/images already written; only update availability/sizes/new items). Flag items in the export not yet in the site and items on the site missing from the export.
- Never writes prices into the JSON (prices stay hidden).

### Script 2 — `reorder_list.py`
- Input: Vyapar sales export (date, customer, item, qty) + a refill-cycle map (oils ~30d, A2 ghee ~45d, juices ~25d, honey/jaggery ~40d, etc. — see the existing Reorder Tracker the owner has).
- Output: a "DUE NOW / DUE SOON" list of customers to message, each with a ready WhatsApp reorder message and a clickable `wa.me` link. Print to console and optionally write a CSV.
- This operationalizes repeat purchases (the biggest untapped revenue lever for a consumables store).

### Script 3 — `weekly_summary.py`
- Input: Vyapar sales export.
- Output: a short weekly report — top sellers, slow movers, low-stock alerts, total sales, week-over-week change. Plain text/markdown the owner can read on mobile.

### Script 4 (optional) — `caption_helper.py`
- For products needing a push (low sales / new stock), generate on-brand Instagram captions (voice rules in §3) + hashtag sets. Pull product facts from `products.json`.

> If/when the owner wants these scripts to run on a schedule without a laptop, suggest GitHub Actions (free tier) reading a synced Google Sheet — but confirm before setting up any scheduled automation or new accounts.

---

## 7. Order of work (build sequence)

1. Scaffold repo + brand CSS (colors, fonts, placeholder logos) + responsive shell.
2. Build `index.html` sections (hero → categories → product grid → about → trust → reviews → contact).
3. Build `products.json` from the §2 catalog (descriptions in the brand voice, placeholder images).
4. Wire `main.js`: render products, category filter, WhatsApp deep links (no prices).
5. SEO + schema + OG tags + sitemap/robots + analytics flag.
6. README with deploy steps (GitHub Pages: Settings → Pages → deploy from main branch) and "how to update products".
7. Then the `/scripts` automations (§6), starting with `reorder_list.py` (highest ROI) and `update_products.py`.

## 8. Guardrails
- Confirm before: force-push, deleting files, publishing live, registering/buying anything, adding paid services, or setting up scheduled automation.
- Never hardcode secrets. Never commit Vyapar exports with customer personal data to a public repo — keep `./data/` git-ignored.
- Keep everything within free tiers unless the owner explicitly approves a cost.
- The WhatsApp number `918265011431` and the Dhule address are the only "live" contact details — keep them consistent everywhere.
```
