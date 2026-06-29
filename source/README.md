# source/ — working & original files (not part of the deployed site)

These are the **original, full-resolution source files**. The live website only uses the
optimized copies in `../assets/`. Nothing in here is served by the website; keep it for
re-editing, reshoots, and reference. Do not delete.

## product-photos/
Original product photos, renamed to match the products and grouped by category. Each is the
source for the optimized WebP of the same name in `../assets/img/products/`.

| Folder | Files |
|---|---|
| `oils/` | groundnut-oil, groundnut-oil-2 (alt angle), sunflower-oil, mustard-oil, safflower-oil, coconut-oil, virgin-coconut-oil, flaxseed-oil, sesame-oil, castor-oil, almond-oil |
| `ghee/` | a2-gir-cow-ghee |
| `sweeteners/` | honey, chemical-free-jaggery, jaggery-powder, jaggery-cube |
| `spices/` | turmeric, turmeric-2 (500g alt), himalayan-rock-salt, black-salt |
| `health-care/` | aloe-vera-juice, amla-juice, jamun-juice, zankar-pain-relief-oil, amla-prash, gulkand-prash |
| `skin-hair/` | kalonji-oil, neem-citronella-soap, ubtan-soap, bhimseni-kapoor-soap |
| `pooja/` | bhimseni-kapoor (camphor flakes), deepam-oil |

To re-optimize one for the site:
```
.venv/bin/python scripts/optimize_images.py source/product-photos/oils/groundnut-oil.jpg assets/img/products/groundnut-oil.webp
```

## brand/
The full logo source set (from the designer) and the high-res app icon.

| File | What it is |
|---|---|
| `logo-primary-horizontal-cream.svg` | Full horizontal lockup on cream |
| `logo-reversed-horizontal-forest.svg` | Full horizontal lockup on forest |
| `logo-stacked-cream.svg` | Stacked lockup on cream (square/social) |
| `app-icon-forest.svg` / `app-icon-cream.svg` | Mark-only app icons |
| `app-icon-forest-1000.png` | High-res (1000px) forest app icon |
| `logo-master-set.html` + `support.js` | Designer's interactive master-set export |
| `logo-concepts-backup.zip` | Backup of the original logo concepts export |

## Which logos the LIVE website actually uses (in ../assets/img/)
These were derived/cleaned from the brand source above. They are wired into `index.html`:

| Website file | Where it's used |
|---|---|
| `assets/img/logo-mark.svg` | Header (the अ mark only) |
| `assets/img/logo-stacked-reversed.svg` | Hero (अ + "Ansh Enterprises" + "शुद्ध · The Old Way" tagline, on forest) |
| `assets/img/favicon.svg` | Browser tab icon |
| `assets/img/og-image.png` | Social share preview (WhatsApp/Facebook) |
| `assets/img/logo.svg`, `assets/img/logo-reversed.svg` | Spare horizontal lockups, not currently wired |
