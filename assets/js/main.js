/* ============================================================
   ANSH ENTERPRISES — main.js
   Renders products, search, category filter, size selection,
   a client-side order basket, and one combined WhatsApp order.
   No prices, ever. No server.
   ============================================================ */

// --------------- Config ---------------
const CONFIG = {
  baseUrl: 'https://ankushpatil45.github.io/ansh-enterprises',
  ga4Id: 'G-YXW401W2XD', // Google Analytics 4 Measurement ID
  assetVersion: '6',     // bump when product images change, to bust browser cache
};

// --------------- State ---------------
let STORE = null;
let activeCategory = 'All';
let searchTerm = '';
// cart: { "id|size": { id, name, size, qty } }
let cart = loadCart();

// --------------- Bootstrap ---------------
document.addEventListener('DOMContentLoaded', () => {
  fetch('products.json?t=' + Date.now())
    .then(r => r.json())
    .then(data => {
      STORE = data;
      initCategoryFilter(data);
      initSearch();
      renderProducts();
      initMobileNav();
      initCartUI();
      applyGeneralLinks();
      renderCart();
      injectProductSchema(data);
    })
    .catch(err => console.error('Could not load products.json:', err));
});

// --------------- WhatsApp links ---------------
function waGeneral() {
  const msg = `Namaste! I'd like to see your products and prices. (from Ansh Enterprises website)`;
  return `https://wa.me/${STORE.store.whatsapp}?text=${encodeURIComponent(msg)}`;
}

function waOrderFromCart() {
  const items = Object.values(cart);
  if (items.length === 0) return waGeneral();
  const lines = items.map(i => `• ${i.name}${i.size ? ` (${i.size})` : ''} x${i.qty}`).join('\n');
  const msg =
    `Namaste! I'd like to order from Ansh Enterprises:\n${lines}\n\n` +
    `My name is ____ and my area is ____.\n` +
    `(I understand home delivery is for orders above ₹500, paid by UPI in advance.)`;
  return `https://wa.me/${STORE.store.whatsapp}?text=${encodeURIComponent(msg)}`;
}

function applyGeneralLinks() {
  document.querySelectorAll('.js-wa-general').forEach(el => { el.href = waGeneral(); });
}

// --------------- Product schema (SEO) ---------------
// Builds an ItemList of Product JSON-LD from products.json so search engines
// can index each item. No price (prices are hidden), so no Offer is emitted.
function injectProductSchema(data) {
  const base = CONFIG.baseUrl.replace(/\/$/, '');
  const items = data.products
    .filter(p => p.available)
    .map((p, i) => ({
      "@type": "ListItem",
      "position": i + 1,
      "item": {
        "@type": "Product",
        "name": p.name,
        "description": p.description,
        "image": `${base}/${p.image}`,
        "category": p.category,
        "brand": { "@type": "Brand", "name": "Ansh Enterprises" }
      }
    }));
  const schema = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Ansh Enterprises Products",
    "itemListElement": items
  };
  const el = document.createElement('script');
  el.type = 'application/ld+json';
  el.textContent = JSON.stringify(schema);
  document.head.appendChild(el);
}

// --------------- Search ---------------
function initSearch() {
  const input = document.getElementById('product-search');
  if (!input) return;
  input.addEventListener('input', () => {
    searchTerm = input.value.trim().toLowerCase();
    renderProducts();
  });
}

// --------------- Category filter ---------------
function initCategoryFilter(data) {
  const bar = document.getElementById('category-chips');
  if (!bar) return;
  bar.appendChild(makeChip('All', true));
  data.categories.forEach(cat => bar.appendChild(makeChip(cat, false)));
}

function makeChip(label, active) {
  const btn = document.createElement('button');
  btn.className = 'chip' + (active ? ' active' : '');
  btn.textContent = label;
  btn.type = 'button';
  btn.addEventListener('click', () => {
    activeCategory = label;
    document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    renderProducts();
  });
  return btn;
}

// --------------- Product rendering ---------------
function getVisibleProducts() {
  return STORE.products.filter(p => {
    const inCat = activeCategory === 'All' || p.category === activeCategory;
    const inSearch = !searchTerm ||
      p.name.toLowerCase().includes(searchTerm) ||
      p.category.toLowerCase().includes(searchTerm) ||
      (p.tags || []).some(t => t.toLowerCase().includes(searchTerm));
    return inCat && inSearch;
  });
}

function renderProducts() {
  const grid = document.getElementById('product-grid');
  if (!grid) return;
  const products = getVisibleProducts();
  grid.innerHTML = '';

  if (products.length === 0) {
    grid.innerHTML = `<p class="text-muted text-center" style="grid-column:1/-1;padding:2rem;">No products match your search. Try another word, or ask us on WhatsApp.</p>`;
    return;
  }
  products.forEach(p => grid.appendChild(productCard(p)));
}

function productCard(p) {
  const card = document.createElement('article');
  card.className = 'product-card' + (p.available ? '' : ' product-card--oos');
  card.setAttribute('role', 'listitem');

  const imgAlt = `${p.name} from Ansh Enterprises Dhule`;

  const sizeControl = p.sizes.length > 1
    ? `<select class="product-card__size-select" aria-label="Choose size for ${escHtml(p.name)}">
         ${p.sizes.map(s => `<option value="${escHtml(s)}">${escHtml(s)}</option>`).join('')}
       </select>`
    : (p.sizes.length === 1 ? `<span class="product-card__size">${escHtml(p.sizes[0])}</span>` : '');

  card.innerHTML = `
    <div class="product-card__image">
      <img src="${p.image}?v=${CONFIG.assetVersion}" alt="${imgAlt}" loading="lazy"
           onerror="this.parentNode.innerHTML='<span class=\\'product-card__image--placeholder\\' aria-hidden=\\'true\\'>🌿</span>'">
    </div>
    <div class="product-card__body">
      <div class="product-card__name">${escHtml(p.name)}</div>
      <div class="product-card__desc">${escHtml(p.description)}</div>
      <div class="product-card__size-row">${sizeControl}</div>
      ${!p.available ? '<span class="badge-oos">Out of stock</span>' : ''}
    </div>
    <div class="product-card__footer"></div>
  `;

  const footer = card.querySelector('.product-card__footer');
  if (p.available) {
    const btn = document.createElement('button');
    btn.className = 'btn btn-add';
    btn.type = 'button';
    btn.innerHTML = `<span aria-hidden="true">+</span> Add to order`;
    btn.addEventListener('click', () => {
      const select = card.querySelector('.product-card__size-select');
      const size = select ? select.value : (p.sizes[0] || '');
      addToCart(p, size);
      flashAdded(btn);
    });
    footer.appendChild(btn);
  } else {
    footer.innerHTML = `<button class="btn btn-secondary" disabled aria-disabled="true">Currently unavailable</button>`;
  }
  return card;
}

function flashAdded(btn) {
  const original = btn.innerHTML;
  btn.innerHTML = `<span aria-hidden="true">✓</span> Added`;
  btn.classList.add('btn-add--done');
  setTimeout(() => { btn.innerHTML = original; btn.classList.remove('btn-add--done'); }, 1000);
}

function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// --------------- Cart ---------------
function cartKey(id, size) { return `${id}|${size}`; }

function loadCart() {
  try { return JSON.parse(localStorage.getItem('ansh_cart')) || {}; }
  catch { return {}; }
}
function saveCart() {
  try { localStorage.setItem('ansh_cart', JSON.stringify(cart)); } catch {}
}

function addToCart(p, size) {
  const key = cartKey(p.id, size);
  if (cart[key]) cart[key].qty += 1;
  else cart[key] = { id: p.id, name: p.name, size, qty: 1 };
  saveCart();
  renderCart();
}

function changeQty(key, delta) {
  if (!cart[key]) return;
  cart[key].qty += delta;
  if (cart[key].qty <= 0) delete cart[key];
  saveCart();
  renderCart();
}

function clearCart() {
  cart = {};
  saveCart();
  renderCart();
}

function cartCount() {
  return Object.values(cart).reduce((n, i) => n + i.qty, 0);
}

// --------------- Cart UI ---------------
function initCartUI() {
  const fab = document.getElementById('cart-fab');
  const drawer = document.getElementById('cart-drawer');
  const overlay = document.getElementById('cart-overlay');
  const closeBtn = document.getElementById('cart-close');
  if (!fab) return;

  const open = () => { drawer.classList.add('open'); overlay.classList.add('open'); drawer.setAttribute('aria-hidden', 'false'); };
  const close = () => { drawer.classList.remove('open'); overlay.classList.remove('open'); drawer.setAttribute('aria-hidden', 'true'); };

  fab.addEventListener('click', open);
  closeBtn.addEventListener('click', close);
  overlay.addEventListener('click', close);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });

  document.getElementById('cart-clear').addEventListener('click', clearCart);
}

function renderCart() {
  const count = cartCount();
  const badge = document.getElementById('cart-count');
  const fab = document.getElementById('cart-fab');
  if (badge) badge.textContent = count;
  if (fab) fab.classList.toggle('has-items', count > 0);

  const list = document.getElementById('cart-items');
  const empty = document.getElementById('cart-empty');
  const footer = document.getElementById('cart-footer');
  if (!list) return;

  const items = Object.entries(cart);
  list.innerHTML = '';

  if (items.length === 0) {
    if (empty) empty.style.display = 'block';
    if (footer) footer.style.display = 'none';
    return;
  }
  if (empty) empty.style.display = 'none';
  if (footer) footer.style.display = 'block';

  items.forEach(([key, item]) => {
    const row = document.createElement('div');
    row.className = 'cart-item';
    row.innerHTML = `
      <div class="cart-item__info">
        <div class="cart-item__name">${escHtml(item.name)}</div>
        <div class="cart-item__size">${escHtml(item.size)}</div>
      </div>
      <div class="cart-item__qty">
        <button type="button" class="qty-btn" data-act="dec" aria-label="Decrease quantity">−</button>
        <span class="qty-num">${item.qty}</span>
        <button type="button" class="qty-btn" data-act="inc" aria-label="Increase quantity">+</button>
      </div>
    `;
    row.querySelector('[data-act="dec"]').addEventListener('click', () => changeQty(key, -1));
    row.querySelector('[data-act="inc"]').addEventListener('click', () => changeQty(key, +1));
    list.appendChild(row);
  });

  const sendBtn = document.getElementById('cart-send');
  if (sendBtn) sendBtn.href = waOrderFromCart();
}

// --------------- Mobile nav ---------------
function initMobileNav() {
  const hamburger = document.getElementById('hamburger');
  const navLinks  = document.getElementById('nav-links');
  const navCta    = document.getElementById('nav-cta');
  if (!hamburger) return;

  hamburger.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    navCta.classList.toggle('open', open);
    hamburger.setAttribute('aria-expanded', String(open));
  });
  navLinks.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      navLinks.classList.remove('open');
      navCta.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
    });
  });
}

// --------------- GA4 (opt-in) ---------------
if (CONFIG.ga4Id) {
  const s = document.createElement('script');
  s.src = `https://www.googletagmanager.com/gtag/js?id=${CONFIG.ga4Id}`;
  s.async = true;
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  function gtag(){ dataLayer.push(arguments); }
  gtag('js', new Date());
  gtag('config', CONFIG.ga4Id);
}
