#!/usr/bin/env python3
"""Ansh Enterprises WhatsApp brochure v2 — high-res, real logo, product info."""
import os, qrcode, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT="/Users/ankush/Documents/Ansh Enterprises"
PROD=f"{ROOT}/assets/img/products"
OUTDIR=f"{ROOT}/marketing"; os.makedirs(OUTDIR,exist_ok=True)

FOREST=(23,52,4); FOREST_D=(14,32,2); LEAF=(59,109,17); GOLD=(239,159,39)
TERRA=(153,60,29); CREAM=(251,246,234); INK=(44,44,42); SAGE=(225,236,205); MUTED=(126,130,112)

SERIF="/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
SERIF_IT="/System/Library/Fonts/Supplemental/Georgia Italic.ttf"
SERIF_REG="/System/Library/Fonts/Supplemental/Georgia.ttf"
SANS="/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
SANS_B="/System/Library/Fonts/Supplemental/Arial Bold.ttf"
def F(p,s): return ImageFont.truetype(p,s)

W=2160; M=140
cv=Image.new("RGBA",(W,13000),CREAM+(255,))
d=ImageDraw.Draw(cv)

def tw(s,f): b=d.textbbox((0,0),s,font=f); return b[2]-b[0]
def th(s,f): b=d.textbbox((0,0),s,font=f); return b[3]-b[1]
def ctext(y,s,f,fill): d.text(((W-tw(s,f))//2,y),s,font=f,fill=fill)
def ltext(x,y,s,f,fill): d.text((x,y),s,font=f,fill=fill)
def tracked(cx,y,s,f,fill,tr):  # letter-spaced, centered
    total=sum(tw(c,f)+tr for c in s)-tr; x=cx-total//2
    for c in s: d.text((x,y),c,font=f,fill=fill); x+=tw(c,f)+tr

# ---- transparent logo mark (chroma-key the forest square) ----
def logo_transparent():
    im=Image.open(f"{ROOT}/source/brand/app-icon-forest-1000.png").convert("RGBA")
    a=np.asarray(im).copy()
    diff=(np.abs(a[:,:,0].astype(int)-23)+np.abs(a[:,:,1].astype(int)-52)+np.abs(a[:,:,2].astype(int)-4))
    a[diff<60,3]=0
    out=Image.fromarray(a)
    return out.crop(out.getbbox())
LOGO=logo_transparent()

def shadow_card(x,y,w,h,r=28):
    pad=46
    sh=Image.new("RGBA",(w+2*pad,h+2*pad),(0,0,0,0))
    sd=ImageDraw.Draw(sh)
    sd.rounded_rectangle([pad,pad,pad+w,pad+h],radius=r,fill=(20,40,5,70))
    sh=sh.filter(ImageFilter.GaussianBlur(16))
    cv.paste(sh,(x-pad,y-pad+10),sh)
    d.rounded_rectangle([x,y,x+w,y+h],radius=r,fill=(255,255,255,255))

def thumb(x,y,size,img,name,tag):
    shadow_card(x,y,size,size+150)
    if os.path.exists(img):
        im=Image.open(img).convert("RGB"); pad=int(size*0.09); box=size-2*pad
        iw,ih=im.size; sc=min(box/iw,box/ih)
        im=im.resize((round(iw*sc),round(ih*sc)),Image.LANCZOS)
        cv.paste(im,(x+(size-im.size[0])//2,y+(size-im.size[1])//2))
    # name (wrap up to 2 lines)
    fn=F(SERIF_REG,46); words=name.split(); lines=[]; cur=""
    for w_ in words:
        t=(cur+" "+w_).strip()
        if tw(t,fn)<=size-30: cur=t
        else: lines.append(cur); cur=w_
    if cur: lines.append(cur)
    ly=y+size+18
    for ln in lines[:2]:
        d.text((x+(size-tw(ln,fn))//2,ly),ln,font=fn,fill=FOREST); ly+=52
    # gold benefit tag
    ft=F(SANS_B,26)
    tracked(x+size//2,ly+4,tag.upper(),ft,GOLD,3)

def section(y,title,sub):
    d.rounded_rectangle([M,y+6,M+16,y+62],radius=8,fill=GOLD)
    d.text((M+40,y),title,font=F(SERIF,76),fill=FOREST)
    y+=104
    d.text((M+40,y),sub,font=F(SERIF_IT,40),fill=MUTED)
    return y+78

def grid(y,items,cols=3):
    gap=42; size=(W-2*M-(cols-1)*gap)//cols
    for i,(img,nm,tg) in enumerate(items):
        r,c=divmod(i,cols); thumb(M+c*(size+gap),y+r*(size+196),size,img,nm,tg)
    rows=(len(items)+cols-1)//cols
    return y+rows*(size+196)

# ================= HEADER =================
HDR=900
d.rectangle([0,0,W,HDR],fill=FOREST)
lg=LOGO.resize((360,int(360*LOGO.height/LOGO.width)),Image.LANCZOS)
cv.paste(lg,((W-lg.width)//2,70),lg)
ctext(470,"ANSH ENTERPRISES",F(SERIF,120),CREAM)
tracked(W//2,628,"COLD-PRESSED   ·   PURE   ·   NATURAL",F(SANS_B,40),GOLD,6)
d.rectangle([(W-300)//2,710,(W+300)//2,716],fill=GOLD)
ctext(742,"Wood-pressed oils, A2 ghee, honey & natural products",F(SANS,40),(222,230,205))

y=HDR+70
ctext(y,"Pure, the way nature intended.",F(SERIF_IT,66),TERRA); y+=110
ctext(y,"Real food, pressed slow and kept honest. No heat, no chemicals.",F(SANS,40),MUTED); y+=120

# ================= CATEGORIES =================
def P(f,n,t): return (f"{PROD}/{f}",n,t)
CATS=[
 ("Cold-Pressed Oils","Pressed slow on a wooden ghani, never heated.",[
   P("groundnut-oil.webp","Groundnut Oil","Wood-pressed"),P("mustard-oil.webp","Mustard Oil","Cold-pressed"),
   P("coconut-oil.webp","Coconut Oil","Wood-pressed"),P("sesame-oil.webp","Sesame Oil","Cold-pressed"),
   P("flaxseed-oil.webp","Flaxseed Oil","Omega-3 rich"),P("almond-oil.webp","Almond Oil","Cold-pressed"),
 ],"Also: Sunflower, Safflower, Virgin Coconut, Castor"),
 ("A2 Ghee & Sweeteners","Hand-churned ghee, raw honey and chemical-free jaggery.",[
   P("a2-ghee.webp","A2 Gir Cow Ghee","Bilona churned"),P("honey.webp","Wild Honey","Raw & unfiltered"),
   P("jaggery.webp","Jaggery","No chemicals"),
 ],"Jaggery also in powder & cube"),
 ("Natural Spices","Single-source and pure, with nothing added.",[
   P("turmeric.webp","High-Curcumin Turmeric","High curcumin"),P("rock-salt.webp","Himalayan Rock Salt","Mineral-rich"),
   P("black-salt.webp","Black Salt","Tangy & natural"),
 ],None),
 ("Health Care","Cold-pressed juices and herbal preserves, no added sugar.",[
   P("aloe-vera-juice.webp","Aloe Vera Juice","Sugar-free"),P("amla-juice.webp","Amla Juice","Vitamin C"),
   P("jamun-juice.webp","Jamun Juice","Sugar-free"),P("amla-prash.webp","Amla Prash","Daily immunity"),
   P("gulkand-prash.webp","Gulkand Prash","Cooling"),P("zankar-oil.webp","Pain Relief Oil","For aches"),
 ],None),
 ("Skin & Hair","Handmade bars and cold-pressed oils for natural care.",[
   P("kalonji-oil.webp","Kalonji Oil","Cold-pressed"),P("neem-soap.webp","Neem Citronella Bar","Handmade"),
   P("ubtan-soap.webp","Ubtan Bar","Handmade"),P("kapoor-soap.webp","Kapoor Soap","Pure camphor"),
 ],None),
 ("Pooja Essentials","Pure oils and camphor for your daily rituals.",[
   P("deepam-oil.webp","Deepam Oil","Clean burning"),P("bhimseni-kapoor.webp","Bhimseni Kapoor","Pure camphor"),
 ],None),
]
for title,sub,items,note in CATS:
    y=section(y,title,sub)
    y=grid(y,items)
    if note: d.text((M,y),f"+  {note}",font=F(SERIF_IT,38),fill=MUTED); y+=70
    y+=50

# ================= TRUST STRIP =================
d.rectangle([0,y,W,y+150],fill=SAGE)
tracked(W//2,y+52,"100% NATURAL     ·     WOOD-PRESSED     ·     NO CHEMICALS     ·     HOME DELIVERY",F(SANS_B,38),FOREST,4)
y+=150

# ================= CONTACT FOOTER =================
ft0=y
FH=880
d.rectangle([0,ft0,W,ft0+FH],fill=FOREST)
ctext(ft0+60,"Order on WhatsApp",F(SERIF,92),GOLD)
d.rectangle([(W-320)//2,ft0+185,(W+320)//2,ft0+191],fill=(90,120,50))

# QR (right)
wa="https://wa.me/918265011431?text=Namaste!%20I'd%20like%20to%20order%20from%20Ansh%20Enterprises."
qr=qrcode.QRCode(border=2,box_size=12); qr.add_data(wa); qr.make()
qimg=qr.make_image(fill_color="#173404",back_color="white").convert("RGB").resize((360,360))
qx=W-M-360-30; qy=ft0+300
d.rounded_rectangle([qx-26,qy-26,qx+360+26,qy+360+26],radius=24,fill=(255,255,255,255))
cv.paste(qimg,(qx,qy))
ctext2=qx+180
tracked(qx+180,qy+380,"SCAN TO ORDER",F(SANS_B,28),(222,230,205),3)

# details (left)
lx=M+20; ly=ft0+250
def row(label,value,ly):
    d.text((lx,ly),label.upper(),font=F(SANS_B,30),fill=GOLD)
    fy=F(SANS,42);
    # wrap value to fit left column width
    maxw=qx-80-lx; words=value.split(); lines=[]; cur=""
    for w_ in words:
        t=(cur+" "+w_).strip()
        if tw(t,fy)<=maxw: cur=t
        else: lines.append(cur); cur=w_
    if cur: lines.append(cur)
    yy=ly+44
    for ln in lines:
        d.text((lx,yy),ln,font=fy,fill=CREAM); yy+=52
    return yy+24
ly=row("Call / WhatsApp","+91 82650 11431",ly)
ly=row("Visit","31, Garud Colony, Nakane Rd, opp. Sakar Glass House, Deopur, Dhule 424002",ly)
ly=row("Hours","9 AM to 9 PM, all days  ·  Free home delivery in Dhule (orders above Rs.500, UPI in advance)",ly)
ly=row("Instagram","@ansh_cold_pressed_oil",ly)
y=ft0+FH

# ================= EXPORT =================
final=cv.crop((0,0,W,y)).convert("RGB")
jpg=f"{OUTDIR}/ansh-enterprises-brochure.jpg"; pdf=f"{OUTDIR}/ansh-enterprises-brochure.pdf"
final.save(jpg,"JPEG",quality=92); final.save(pdf,"PDF",resolution=150)
print("size",final.size); print("wrote",jpg); print("wrote",pdf)
