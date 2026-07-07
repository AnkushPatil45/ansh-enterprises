#!/usr/bin/env python3
"""Ansh Enterprises brochure (HTML -> high-res JPG + clickable PDF), EN + Marathi.
Transparent cutouts matted to cream (small PDFs), subtle ghani motif, brand copy.
Setup: .venv/bin/pip install playwright qrcode pillow && .venv/bin/python -m playwright install chromium
Run:   .venv/bin/python scripts/make_brochure_html.py
"""
import os, shutil, qrcode
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROD=f"{ROOT}/assets/img/products"
OUT=f"{ROOT}/marketing"; os.makedirs(OUT,exist_ok=True)
TMP=f"{OUT}/_imgs"; os.makedirs(TMP,exist_ok=True)
CREAM=(251,246,234)
def fileurl(p): return "file://"+p

WA="https://wa.me/918265011431?text=Namaste!%20I'd%20like%20to%20order%20from%20Ansh%20Enterprises."
qrcode.make(WA).save(f"{OUT}/qr.png")

SAGE=(233,241,217)  # alternating section tint
def matte(name, bg=CREAM):
    key=f"{os.path.splitext(name)[0]}_{bg[0]}{bg[1]}{bg[2]}.jpg"
    out=f"{TMP}/{key}"
    im=Image.open(f"{PROD}/{name}").convert("RGBA")
    canvas=Image.new("RGB",im.size,bg); canvas.paste(im,(0,0),im); canvas.save(out,"JPEG",quality=90)
    return out

# traditional लाकडी घाणा (kolhu) silhouette — subtle, relatable background motif
GHANI='<svg class="ghani" viewBox="0 0 300 230" fill="currentColor"><path d="M30,210 Q150,236 270,210" fill="none" stroke="currentColor" stroke-width="3"/><path d="M120,120 Q150,108 180,120 L173,188 Q150,200 127,188 Z"/><ellipse cx="150" cy="118" rx="30" ry="8"/><rect x="144" y="52" width="12" height="68" rx="3"/><circle cx="150" cy="52" r="7"/><path d="M150,56 L36,30 L42,46 L150,70 Z"/><path d="M150,120 L196,150 L190,158 L150,132 Z"/></svg>'

# (image, name_en, name_mr, tag_en, tag_mr)
CATS=[
("Cold-Pressed Oils","तेल","Every oil is cold-pressed on a wooden ghani, never heated.","प्रत्येक तेल लाकडी घाण्यावर, उष्णतेशिवाय काढलेलं.",[
 ("groundnut-oil-gold.webp","Groundnut Oil (Gold)","शेंगदाणा तेल (गोल्ड)","Rich in Vitamin E","व्हिटॅमिन E युक्त"),
 ("groundnut-oil-premium.webp","Groundnut Oil (Premium)","शेंगदाणा तेल (प्रीमियम)","Rich in Vitamin E","व्हिटॅमिन E युक्त"),
 ("mustard-oil-gold.webp","Mustard Oil (Gold)","मोहरी तेल (गोल्ड)","Good for the heart","हृदयासाठी उत्तम"),
 ("mustard-oil-premium.webp","Mustard Oil (Premium)","मोहरी तेल (प्रीमियम)","Good for the heart","हृदयासाठी उत्तम"),
 ("sesame-oil-gold.webp","Sesame Oil (Gold)","तीळ तेल (गोल्ड)","Good for bones","हाडांसाठी उत्तम"),
 ("sesame-oil-premium.webp","Sesame Oil (Premium)","तीळ तेल (प्रीमियम)","Good for bones","हाडांसाठी उत्तम"),
 ("black-sesame-oil-premium.webp","Black Sesame Oil (Premium)","काळे तीळ तेल (प्रीमियम)","Rich in calcium","कॅल्शियमयुक्त"),
 ("sunflower-oil.webp","Sunflower Oil","सूर्यफूल तेल","Light & heart-friendly","हलकं, हृदयासाठी"),
 ("safflower-oil.webp","Safflower Oil","करडई तेल","Good for cholesterol","कोलेस्ट्रॉलसाठी उत्तम"),
 ("coconut-oil.webp","Coconut Oil","खोबरेल तेल","Cooking, skin & hair","स्वयंपाक व केसांसाठी"),
 ("virgin-coconut-oil.webp","Virgin Coconut Oil","व्हर्जिन खोबरेल तेल","For skin & immunity","त्वचा व प्रतिकारशक्तीसाठी"),
 ("flaxseed-oil.webp","Flaxseed Oil","जवस तेल","Omega-3 rich","ओमेगा-३ युक्त"),
 ("castor-oil.webp","Castor Oil","एरंडेल तेल","Hair & skin care","केस व त्वचेसाठी"),
 ("almond-oil.webp","Almond Oil","बदाम तेल","For skin & hair","त्वचा व केसांसाठी"),
]),
("A2 Ghee","तूप","Hand-churned from A2 Gir cow milk, the bilona way.","A2 गीर गायीच्या दुधाचं, बिलोना पद्धतीचं तूप.",[
 ("a2-ghee.webp","A2 Gir Cow Ghee","A2 गीर गाय तूप","Good for digestion","पचनासाठी उत्तम"),
]),
("Honey & Sweeteners","मध व गूळ","Raw honey and chemical-free jaggery.","नैसर्गिक मध आणि रसायनमुक्त गूळ.",[
 ("honey.webp","Wild Honey","रानमध","Boosts immunity","प्रतिकारशक्तीसाठी"),
 ("jaggery.webp","Jaggery","गूळ","Rich in iron","लोहयुक्त"),
 ("jaggery-powder.webp","Jaggery Powder","गूळ पावडर","Dissolves easily","पटकन विरघळतो"),
 ("jaggery-cube.webp","Jaggery Cube","गूळ क्यूब","Handy pieces","सोयीस्कर तुकडे"),
]),
("Natural Spices","मसाले","Pure spices, nothing added.","अस्सल मसाले, कोणतीही भेसळ नाही.",[
 ("turmeric.webp","High-Curcumin Turmeric","हळद (जास्त कर्क्युमिन)","High curcumin","जास्त कर्क्युमिन"),
 ("rock-salt.webp","Himalayan Rock Salt","सैंधव मीठ","Mineral-rich","खनिजयुक्त"),
 ("black-salt.webp","Black Salt","काळं मीठ","Good for digestion","पचनासाठी उत्तम"),
]),
("Health Care","आरोग्य","Cold-pressed juices and herbal preserves, no added sugar.","विनासाखर ज्यूस आणि आयुर्वेदिक प्राश.",[
 ("aloe-vera-juice.webp","Aloe Vera Juice","कोरफड ज्यूस","Skin & digestion","त्वचा व पचनासाठी"),
 ("amla-juice.webp","Amla Juice","आवळा ज्यूस","Rich in Vitamin C","व्हिटॅमिन C युक्त"),
 ("jamun-juice.webp","Jamun Juice","जांभूळ ज्यूस","Blood-sugar support","रक्तशर्करेसाठी"),
 ("amla-prash.webp","Amla Prash","आवळा प्राश","Daily immunity","रोगप्रतिकारक शक्ती"),
 ("gulkand-prash.webp","Gulkand Prash","गुलकंद प्राश","Cooling for summer","उन्हाळ्यात थंडावा"),
 ("zankar-oil.webp","Pain Relief Oil","झंकार वेदनाशामक तेल","For joint pain","सांधेदुखीसाठी"),
]),
("Skin & Hair","त्वचा व केस","Handmade bars and cold-pressed oils for natural care.","हाताने बनवलेले साबण आणि कोल्ड प्रेस्ड तेल.",[
 ("kalonji-oil.webp","Kalonji Oil","कलौंजी तेल","Hair & scalp","केस व टाळूसाठी"),
 ("neem-soap.webp","Neem Citronella Bar","नीम सिट्रोनेला साबण","Antibacterial care","जंतुनाशक"),
 ("ubtan-soap.webp","Ubtan Bar","उटणे साबण","For glowing skin","त्वचेच्या तेजासाठी"),
 ("kapoor-soap.webp","Kapoor Soap","कापूर साबण","Cooling & cleansing","थंडगार व स्वच्छ"),
]),
("Pooja Essentials","पूजा साहित्य","Pure oils and camphor for your daily rituals.","रोजच्या पूजेसाठी शुद्ध तेल आणि कापूर.",[
 ("deepam-oil.webp","Deepam Oil","दिवा तेल","Clean burning","धूरविरहित"),
 ("bhimseni-kapoor.webp","Bhimseni Kapoor","भीमसेनी कापूर","Pure camphor","शुद्ध कापूर"),
]),
("Clay Utensils","मातीची भांडी","Handcrafted clay cookware. Ask us for the current range.","हाताने घडवलेली मातीची भांडी. उपलब्ध प्रकारांसाठी विचारा.",[
 ("clay-utensils.webp","Clay Utensils","मातीची भांडी","Traditional cookware","पारंपरिक स्वयंपाक"),
]),
]

STR={
 "en":{"sub":"Cold-pressed oils, A2 ghee, honey &amp; natural foods",
   "hero":"Healthy food you can trust.",
   "trust":"NO CHEMICALS &nbsp;·&nbsp; NO ARTIFICIAL COLOUR &nbsp;·&nbsp; NO PRESERVATIVES",
   "cta":"Order on WhatsApp","scan":"Scan to order","tapnote":"Reading on your phone? Tap the green button below 👇","link":"Order Now on WhatsApp","review":"⭐ Loved our products? Rate us on Google",
   "l_call":"Call / WhatsApp","l_visit":"Visit","l_hours":"Hours","l_ig":"Instagram",
   "hours":"9 AM to 10 PM, all 7 days","addr":"31, Garud Colony, Nakane Rd, opp. Sakar Glass House, Deopur, Dhule 424002"},
 "mr":{"sub":"लाकडी घाण्याचे तेल, A2 तूप, मध आणि नैसर्गिक उत्पादने",
   "hero":"आरोग्यदायी आणि विश्वासार्ह अन्न.",
   "trust":"रसायनमुक्त &nbsp;·&nbsp; कृत्रिम रंग नाही &nbsp;·&nbsp; प्रिझर्वेटिव्ह नाही",
   "cta":"WhatsApp वर ऑर्डर करा","scan":"ऑर्डरसाठी स्कॅन करा","tapnote":"मोबाईलवर पाहत आहात? खालील हिरव्या बटणावर टॅप करा 👇","link":"आत्ताच ऑर्डर करा","review":"⭐ उत्पादनं आवडली? Google वर रेटिंग द्या",
   "l_call":"कॉल / WhatsApp","l_visit":"पत्ता","l_hours":"वेळ","l_ig":"इंस्टाग्राम",
   "hours":"सकाळी ९ ते रात्री १०, आठवड्याचे सातही दिवस","addr":"31, गरुड कॉलनी, नकाणे रोड, साकर ग्लास हाऊससमोर, देवपूर, धुळे 424002"},
}

CSS="""
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;background:#FBF6EA;color:#2C2C2A;font-family:'Poppins',sans-serif}
.serif{font-family:'Playfair Display',serif}
.lang-mr{font-family:'Mukta',sans-serif}
.lang-mr .serif{font-family:'Noto Serif Devanagari',serif}
.ghani{position:absolute;pointer-events:none}
.header::after{content:"";position:absolute;inset:18px;border:1.5px solid rgba(239,159,39,.35);border-radius:10px;pointer-events:none}
.header{position:relative;overflow:hidden;text-align:center;padding:66px 40px 56px;
  background:radial-gradient(120% 90% at 50% -10%, #1d4607 0%, #173404 62%)}
.header .ghani{right:14px;top:50%;transform:translateY(-50%);width:230px;color:#c0dd97;opacity:.12}
.header img.logo{position:relative;width:390px;height:auto;margin:0 auto 16px;display:block}
.rule{width:300px;height:3px;background:#EF9F27;margin:6px auto 18px;border-radius:3px}
.hsub{position:relative;color:#e7eed8;font-size:30px;letter-spacing:.01em}
.hero{text-align:center;padding:44px 40px 6px}
.hero .h{font-style:italic;color:#993C1D;font-size:48px}
.section{padding:60px 70px 56px;border-top:1px solid rgba(23,52,4,.08)}
.snum{display:block;color:#EF9F27;font-weight:700;letter-spacing:.24em;font-size:20px;margin-bottom:12px}
.shead{display:flex;align-items:center;gap:22px}
.bar{width:14px;height:54px;background:#EF9F27;border-radius:7px;flex:none}
.shead h2{font-size:54px;color:#173404;font-weight:700;line-height:1}
.ssub{font-style:italic;color:#7e826e;font-size:28px;margin:14px 0 30px 36px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:34px 30px}
.grid.single{display:flex;justify-content:center}
.grid.single .card{width:33.3%}
.card{text-align:center;padding:6px}
.card .imgwrap{height:300px;display:flex;align-items:center;justify-content:center}
.card img{max-width:84%;max-height:300px;object-fit:contain}
.card .nm{font-size:33px;color:#173404;font-weight:600;margin-top:16px;line-height:1.2}
.card .tag{color:#b07a16;font-weight:700;font-size:19px;letter-spacing:.08em;text-transform:uppercase;margin-top:7px}
.trust{background:#EAF3DE;text-align:center;color:#173404;font-weight:700;font-size:26px;letter-spacing:.07em;padding:34px 40px}
.contact{position:relative;overflow:hidden;background:#173404;color:#dde6cd;padding:52px 70px 58px}
.contact .ghani{left:6px;bottom:18px;width:230px;color:#EF9F27;opacity:.12;transform:scaleX(-1)}
.cta{position:relative;color:#EF9F27;font-size:56px;font-weight:700;text-align:center}
.cline{width:300px;height:3px;background:#5a7832;margin:18px auto 6px;border-radius:3px}
.cwrap{position:relative;display:flex;gap:48px;align-items:center;margin-top:30px}
.details{flex:1}
.row{margin-bottom:22px}
.row .lab{color:#EF9F27;font-weight:700;font-size:22px;letter-spacing:.08em;text-transform:uppercase}
.row .val{color:#FBF6EA;font-size:30px;margin-top:4px;line-height:1.35}
.qr{flex:none;text-align:center}
.qr .qrbox{background:#fff;border-radius:18px;padding:18px;display:inline-block}
.qr img{width:270px;height:270px;display:block}
.qr .scan{color:#dde6cd;font-size:22px;letter-spacing:.1em;text-transform:uppercase;margin-top:14px}
.orderlink{position:relative;display:block;text-align:center;margin-top:36px}
.tapnote{color:#dde6cd;font-size:26px;margin-bottom:18px}
.orderlink a{display:inline-flex;align-items:center;gap:16px;background:#25D366;color:#fff;font-weight:700;font-size:36px;
  text-decoration:none;padding:24px 56px;border-radius:999px;border-bottom:6px solid #17963f}
.orderlink svg{width:44px;height:44px;flex:none}
.reviewlink{position:relative;text-align:center;margin-top:26px}
.reviewlink a{display:inline-flex;align-items:center;gap:12px;background:transparent;color:#EF9F27;font-weight:600;font-size:27px;
  text-decoration:none;padding:16px 40px;border-radius:999px;border:2.5px solid #EF9F27}
.lang-mr .trust,.lang-mr .tag,.lang-mr .scan,.lang-mr .row .lab{letter-spacing:normal}
.lang-mr .card .nm{font-family:'Noto Serif Devanagari',serif;font-weight:600}
"""

def card(img,nm,tag,bg):
    return f'<div class="card"><div class="imgwrap"><img src="{fileurl(matte(img,bg))}"></div><div class="nm serif">{nm}</div><div class="tag">{tag}</div></div>'

def build(lang):
    s=STR[lang]; ni=1 if lang=="mr" else 0; ti=3 if lang=="mr" else 2
    secs=""
    for i,(cat_en,cat_mr,sub_en,sub_mr,items) in enumerate(CATS):
        title=cat_mr if lang=="mr" else cat_en
        sub=sub_mr if lang=="mr" else sub_en
        even=(i%2==0); bg=CREAM if even else SAGE; bg_hex="#FBF6EA" if even else "#E9F1D9"
        cards="".join(card(it[0], it[ni+1], it[ti+1], bg) for it in items)
        gcls="grid single" if len(items)==1 else "grid"
        secs+=f'<div class="section" style="background:{bg_hex}"><span class="snum">{i+1:02d} / {len(CATS):02d}</span><div class="shead"><div class="bar"></div><h2 class="serif">{title}</h2></div><div class="ssub">{sub}</div><div class="{gcls}">{cards}</div></div>'
    body_cls="lang-mr" if lang=="mr" else "lang-en"
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,500&family=Poppins:wght@400;500;600;700&family=Mukta:wght@400;600;700&family=Noto+Serif+Devanagari:wght@500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head>
<body class="{body_cls}">
<div class="header">
  {GHANI}
  <img class="logo" src="{fileurl(ROOT)}/assets/img/logo-stacked-reversed.svg">
  <div class="rule"></div>
  <div class="hsub">{s['sub']}</div>
</div>
<div class="hero"><div class="h serif">{s['hero']}</div></div>
{secs}
<div class="trust">{s['trust']}</div>
<div class="contact">
  {GHANI}
  <div class="cta serif">{s['cta']}</div><div class="cline"></div>
  <div class="cwrap">
    <div class="details">
      <div class="row"><div class="lab">{s['l_call']}</div><div class="val">+91 82650 11431</div></div>
      <div class="row"><div class="lab">{s['l_visit']}</div><div class="val">{s['addr']}</div></div>
      <div class="row"><div class="lab">{s['l_hours']}</div><div class="val">{s['hours']}</div></div>
      <div class="row"><div class="lab">{s['l_ig']}</div><div class="val">@ansh_cold_pressed_oil</div></div>
    </div>
    <div class="qr"><div class="qrbox"><img src="{fileurl(OUT)}/qr.png"></div><div class="scan">{s['scan']}</div></div>
  </div>
  <div class="orderlink"><div class="tapnote">{s['tapnote']}</div><a href="{WA}"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>{s['link']}</a></div>
  <div class="reviewlink"><a href="https://share.google/uxPhYZIj9RsNsyaWk">{s['review']}</a></div>
</div>
</body></html>"""

def render(lang, jpg, pdf):
    htmlpath=f"{OUT}/_brochure_{lang}.html"
    open(htmlpath,"w",encoding="utf-8").write(build(lang))
    with sync_playwright() as p:
        b=p.chromium.launch()
        pg=b.new_page(viewport={"width":1080,"height":1400}, device_scale_factor=2)
        pg.goto(fileurl(htmlpath), wait_until="networkidle")
        pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1500)
        pg.screenshot(path=jpg, full_page=True, type="jpeg", quality=92)
        h=pg.evaluate("document.body.scrollHeight")
        pg.pdf(path=pdf, width="1080px", height=f"{h}px", print_background=True)
        b.close()
    os.remove(htmlpath); print("wrote",os.path.basename(jpg),"+ pdf")

render("en", f"{OUT}/ansh-enterprises-brochure.jpg", f"{OUT}/ansh-enterprises-brochure.pdf")
render("mr", f"{OUT}/ansh-enterprises-brochure-marathi.jpg", f"{OUT}/ansh-enterprises-brochure-marathi.pdf")
os.remove(f"{OUT}/qr.png"); shutil.rmtree(TMP)
print("DONE")
