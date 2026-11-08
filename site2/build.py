import re, json, pathlib, html as H
from services_data import SERVICES
from custom_sections import CUSTOM, CHAT_DEMO, CUSTOM_AFTER
from process_data import PROCESS, AREA_NOTE
from locations_data import LOCATIONS, AREAS as LOC_AREAS
R = pathlib.Path(__file__).parent
S = R / 'src'
DOMAIN = 'https://adsncodes.com/'
OGMAP = json.loads((pathlib.Path(__file__).parent / 'og_map.json').read_text())
SOCIAL = [
  ('Instagram', 'https://www.instagram.com/adsncodes/', '<path fill="currentColor" d="M12 7.3A4.7 4.7 0 1 0 16.7 12 4.7 4.7 0 0 0 12 7.3Zm0 7.7a3 3 0 1 1 3-3 3 3 0 0 1-3 3Zm4.9-8.9a1.1 1.1 0 1 0 1.1 1.1 1.1 1.1 0 0 0-1.1-1.1ZM20 4H4v16h16Zm-1.6 14.4H5.6V5.6h12.8Z"/>'),
  ('Facebook', 'https://www.facebook.com/adsncodes', '<path fill="currentColor" d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.5V4.4a20 20 0 0 0-2.2-.1c-2.2 0-3.7 1.3-3.7 3.8v2.4H8v3h2.6V21Z"/>'),
  ('YouTube', 'https://www.youtube.com/@AdsnCodes', '<path fill="currentColor" d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 0 0 2.4 7.2 26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8A26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8ZM10 15V9l5.2 3Z"/>'),
  ('LinkedIn', 'https://www.linkedin.com/company/adsncodes/', '<path fill="currentColor" d="M6.9 8.9H3.6V20h3.3ZM5.2 3.5a1.9 1.9 0 1 0 0 3.8 1.9 1.9 0 0 0 0-3.8ZM20.4 13.6c0-3-1.6-4.9-4.3-4.9a3.7 3.7 0 0 0-3.3 1.8V8.9H9.6V20h3.3v-5.8c0-1.6.6-2.8 2.1-2.8s1.9 1.2 1.9 2.9V20h3.4Z"/>'),
  ('TikTok', 'https://www.tiktok.com/@adsncodes', '<path fill="currentColor" d="M16.6 3h-3.2v11.9a2.6 2.6 0 1 1-2.6-2.6c.3 0 .5 0 .8.1V9.1a5.9 5.9 0 1 0 5 5.8V8.9a7.3 7.3 0 0 0 4.2 1.3V7a4.2 4.2 0 0 1-4.2-4Z"/>'),
]
socials_html = '<div class="socials">' + ''.join(f'<a href="{u}" aria-label="{n}"><svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true">{p}</svg></a>' for n, u, p in SOCIAL) + '</div>'
ORG = {
  "@context": "https://schema.org", "@type": ["ProfessionalService", "LocalBusiness"], "@id": DOMAIN + "#org",
  "name": "Ads n' Codes", "alternateName": ["Ads n Codes", "AdsnCodes", "Ads and Codes", "Ads Codes", "Ads N Codes FZE LLC"], "legalName": "Ads N Codes FZE LLC", "url": DOMAIN, "logo": DOMAIN + "assets/logo-ink.png", "image": DOMAIN + "assets/logo-ink.png",
  "description": "Marketing and technology agency in Dubai offering digital marketing, social media marketing, paid ads, SEO, branding, photography, video production, web and app development, and AI automation across the UAE.",
  "telephone": "+971565440310", "email": "hello@adsncodes.com", "priceRange": "AED",
  "address": {"@type": "PostalAddress", "streetAddress": "B Hive, Level 3, BurJuman Business Tower", "addressLocality": "Dubai", "addressRegion": "Dubai", "addressCountry": "AE"},
  "areaServed": [{"@type": "Country", "name": "United Arab Emirates"}] + [{"@type": "City", "name": c} for c in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Umm Al Quwain"]],
  "founder": {"@type": "Person", "name": "Razal Mohammed", "sameAs": "https://www.linkedin.com/in/razalmhd/"},
  "sameAs": [u for _, u, _ in SOCIAL] + ["https://www.google.com/search?kgmid=/g/11nvs5lhb9"],
  "geo": {"@type": "GeoCoordinates", "latitude": 25.2541, "longitude": 55.3036},
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "14:00"}],
  "hasMap": "https://www.google.com/maps/search/?api=1&query=Ads+n%27+Codes+BurJuman+Dubai&query_place_id=ChIJL8srqlxzh2kRtCTl_DkPRDY",
  "foundingDate": "2024-05",
  "knowsAbout": ["Digital marketing", "Social media marketing", "Meta ads", "Google ads", "SEO", "Local SEO", "Generative engine optimization", "AI SEO", "AI search optimisation", "Branding", "Personal branding", "Influencer marketing", "Email marketing", "UGC content", "Content creation", "Photography", "Video production", "Event coverage", "Web development", "E-commerce", "App development", "WhatsApp automation", "AI agents"],
  "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "email": "bd@adsncodes.com", "telephone": "+971565440310", "areaServed": "AE", "availableLanguage": ["English"]}],
}
nav = (S / '_nav.html').read_text()
foot = (S / '_foot.html').read_text().replace('{{SOCIALS}}', socials_html)
SCRIPTS = '''<script defer src="assets/site.js"></script>'''

def head(title, desc, path, extra_ld=(), region=('AE-DU','Dubai')):
    url = DOMAIN + ('' if path == 'index' else path + '.html')
    lds = [ORG] + list(extra_ld)
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in lds)
    return f'''<title>{H.escape(title)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{H.escape(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-ae" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="{region[0]}"><meta name="geo.placename" content="{region[1]}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Ads n' Codes"><meta property="og:locale" content="en_AE">
<meta property="og:title" content="{H.escape(title)}"><meta property="og:description" content="{H.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{DOMAIN}{OGMAP.get(path, 'assets/og.jpg')}"><meta property="og:image:alt" content="{H.escape(title)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{DOMAIN}{OGMAP.get(path, 'assets/og.jpg')}">
<meta name="theme-color" content="#414042">
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/assets/icon-192.png" type="image/png" sizes="192x192"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&family=Outfit:wght@300;400;500;600&display=swap"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&family=Outfit:wght@300;400;500;600&display=swap" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&family=Outfit:wght@300;400;500;600&display=swap"></noscript>
<link rel="preload" as="image" href="assets/logo-white-sm.webp"><link rel="stylesheet" href="assets/site.css">
{ld}'''

def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u} for i, (n, u) in enumerate(items)]}

def _mdl(t):
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
def _mdt(t):
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', t)
def faq_ld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": _mdt(a)}} for q, a in faq]}

def page(name, cur, title, desc, ftitle, body, extra_ld=(), region=('AE-DU','Dubai')):
    style = ''
    m = re.match(r'\s*(<style>.*?</style>)(.*)', body, re.S)
    if m: style, body = m.group(1), m.group(2)
    n = nav
    if cur: n = n.replace(f'data-nav="{cur}"', f'data-nav="{cur}" aria-current="page"')
    f = foot.replace('{{FOOT_TITLE}}', ftitle)
    hd = head(title, desc, name, extra_ld, region) + style
    inner = n + '\n<main id="top">\n' + body + '\n</main>\n' + f + '\n' + SCRIPTS
    if name == 'index': out = hd + '\n' + inner
    else: out = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + hd + '\n</head>\n<body>\n' + inner + '\n</body>\n</html>\n'
    (R / f'{name}.html').write_text(out)
    return name

RESULTS = (R / 'src' / '_results.html').read_text()
VOICES = (R / 'src' / '_voices.html').read_text()
LANDING = (R / 'src' / '_landing.html').read_text()
AGENTSHOW = (R / 'src' / '_agentshow.html').read_text()
from seo_data import SEO
for _s in SERVICES:
    if _s['slug'] in SEO: _s['title'], _s['desc'] = SEO[_s['slug']]
import seo_boost; seo_boost.apply(SERVICES)
BYSLUG = {s['slug']: s for s in SERVICES}
BYSLUG['ai-automation'] = dict(short='AI and automation')
BYSLUG['whatsapp-ai-agent-uae'] = dict(short='WhatsApp AI agents')
from industries_data import INDUSTRIES as _IND
seo_boost.apply(_IND)
for _x in _IND: BYSLUG[_x['slug']] = dict(short=_x['short'])
# drop links to pages that are scheduled but not live yet
for _x in list(SERVICES) + list(_IND):
    if 'related' in _x: _x['related'] = [r for r in _x['related'] if r in BYSLUG]
AREAS = '<p class="areas" style="margin-top:26px"><a href="index.html">Dubai</a><a href="digital-marketing-agency-abu-dhabi.html">Abu Dhabi</a><a href="digital-marketing-agency-sharjah.html">Sharjah</a><a href="digital-marketing-agency-ajman.html">Ajman</a><a href="digital-marketing-agency-ras-al-khaimah.html">Ras Al Khaimah</a><a href="digital-marketing-agency-ras-al-khaimah.html">Fujairah</a><a href="digital-marketing-agency-ras-al-khaimah.html">Umm Al Quwain</a></p>'
ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

READS_MAP = {'influencer-marketing-dubai':[('influencer-campaign-uae-how-it-works','How an influencer campaign works in the UAE'),('uae-advertiser-permit-brands','The UAE Advertiser Permit: what brands must check'),('influencer-vs-ugc-uae','Influencer marketing or UGC?')],
 'ugc-content-dubai':[('influencer-vs-ugc-uae','Influencer marketing or UGC?'),('uae-advertiser-permit-brands','The UAE Advertiser Permit explained')],
 'seo-agency-dubai':[('google-business-profile-dubai','A Google Business Profile checklist for Dubai'),('best-seo-agencies-dubai','The best SEO agencies in Dubai, and who each one suits'),('how-long-does-seo-take-dubai','How long does SEO take in Dubai?')],
 'seo-agency-abu-dhabi':[('best-seo-agencies-dubai','The best SEO agencies in Dubai, and who each one suits'),('how-long-does-seo-take-dubai','How long does SEO take in Dubai?')],
 'real-estate-marketing-agency-dubai':[('real-estate-lead-generation-dubai','Real estate lead generation in Dubai: what works')],
 'whatsapp-ai-agent-real-estate-dubai':[('real-estate-lead-generation-dubai','Real estate lead generation in Dubai: what works')],
 'lead-generation-agency-dubai':[('whatsapp-auto-reply-business-uae','WhatsApp auto reply for business: setup guide'),('real-estate-lead-generation-dubai','Real estate lead generation in Dubai: what works'),('whatsapp-lead-response-uae','Why UAE businesses lose leads on WhatsApp'),('whatsapp-ai-agent-industries-uae','Which UAE businesses gain most from a WhatsApp AI agent')],
 'ppc-google-ads-agency-dubai':[('how-long-does-seo-take-dubai','How long does SEO take, and should you run ads meanwhile?')],
 'workflow-automation-dubai':[('whatsapp-chatbot-vs-ai-agent-uae','WhatsApp chatbot or AI agent?'),('whatsapp-api-charges-uae','WhatsApp API charges from October 2026'),('whatsapp-ai-agent-industries-uae','Which UAE businesses gain most from a WhatsApp AI agent')],
 'digital-marketing-dubai':[('best-digital-marketing-agencies-dubai','The best digital marketing agencies in Dubai, and who each one suits'),('whatsapp-lead-response-uae','Why UAE businesses lose leads on WhatsApp'),('google-business-profile-dubai','Google Business Profile checklist')],
 'content-creation-dubai':[('choose-content-creation-agency-dubai','How to choose a content creation agency in Dubai'),('influencer-vs-ugc-uae','Influencer marketing or UGC?')],
 'social-media-agency-dubai':[('choose-social-media-agency-dubai','How to choose a social media management agency in Dubai'),('best-social-media-agencies-dubai','The best social media marketing companies in Dubai')],
 'instagram-marketing-agency-dubai':[('choose-social-media-agency-dubai','How to choose a social media management agency in Dubai')]}
def SRCSET(a):
    return ''

def PIC(a, img):
    """Hero art direction: phones get a portrait crop (-p) made from the original, larger screens the landscape file."""
    import os
    p = re.sub(r'\.(webp|jpg)$', r'-p.\1', a)
    if p == a or not os.path.exists(R / p): return img
    return f'<picture><source media="(max-width:760px)" srcset="{p}">{img}</picture>'

def service_page(s):
    e = H.escape
    if s.get('video'):
        media = f'<div class="ph-img"><video data-hsrc="{s["video"]}"{(' data-hd="' + s["video_hd"] + '"') if s.get("video_hd") else ''} poster="{s["img"]}" muted loop playsinline preload="none" aria-hidden="true" style="width:100%;height:100%;object-fit:cover;object-position:{s.get('img_pos','center')}"></video></div>'
    else:
        media = '<div class="ph-img">' + PIC(s["img"], f'<img src="{s["img"]}" fetchpriority="high" alt="{e(s["alt"])}"' + ((' style="object-position:' + s["img_pos"] + '"') if s.get("img_pos") else '') + '>') + '</div>'
    subs = ''.join(f'<li><h3>{e(a)}</h3><p>{e(b)}</p></li>' for a, b in s['subs'])
    def _fig(a, b):
        if a.endswith('.mp4'):
            poster = a[:-4] + '.jpg'
            wide = ' wide' if ('ragam-event' in a or 'event-tech-expo' in a) else ''
            return f'<figure><div class="media reel-media{wide}"><div class="reel{wide}"><video data-src="{a}" poster="{poster}" muted loop playsinline preload="none" aria-label="{e(b)}"></video><button type="button" class="reel-sound" aria-label="Turn sound on" aria-pressed="false"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 9h4l5-4v14l-5-4H4z"/><path class="w1" d="M16.5 8.5a5 5 0 0 1 0 7"/><path class="x1" d="M16 9l5 6M21 9l-5 6"/></svg></button></div></div><figcaption>{e(b)}</figcaption></figure>'
        illus = (a.startswith('assets/img/') and not a.startswith('assets/img/demo-')) or a == 'assets/video/reel-poster.jpg'
        tag = ''
        post = ' post' if any(k in a for k in ('foundation-day',)) else ''
        return f'<figure><div class="media{post}"><img src="{a}" alt="{e(b)}" loading="lazy"></div><figcaption>{e(b)}{tag}</figcaption></figure>'
    STEPS = ''.join(f'<li><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in s.get('process') or PROCESS.get(s['slug'], [('Look','We review where you are today.'),('Plan','A written plan with scope and timeline.'),('Make','We produce and build with you.'),('Improve','We measure and refine every month.')]))
    strip = ''.join(_fig(a, b) for a, b in s['work'])
    allreal = not any((a.startswith('assets/img/') and not a.startswith('assets/img/demo-')) or a == 'assets/video/reel-poster.jpg' for a, _ in s['work'])
    note = f'<p class="dim" style="margin-top:18px;font-size:14px">{e(s["work_note"])}</p>' if s.get('work_note') else ''
    faq = ''.join(f'<div class="qa"><button type="button" aria-expanded="{"true" if i == 0 else "false"}" aria-controls="f{i}" id="fq{i}">{e(q)}<span class="pm" aria-hidden="true">+</span></button><div class="ans" id="f{i}" role="region" aria-labelledby="fq{i}"><div><p>{_mdl(e(a))}</p></div></div></div>' for i, (q, a) in enumerate(s['faq']))
    rel = ''.join(f'<a href="{r}.html">{e(BYSLUG[r]["short"])}</a>' for r in s['related'])
    READS = ''.join(f'<a href="insights-{k}.html">{e(t)}</a>' for k, t in READS_MAP.get(s['slug'], []))
    READS = f'<div class="row-head" style="margin:28px 0 0"><span class="lab">Further reading</span><nav class="related" aria-label="Further reading">{READS}</nav></div>' if READS else ''
    body = f'''<section class="phero photo">
  {media}<div class="veil" aria-hidden="true" style="background:linear-gradient(90deg,rgba(65,64,66,.9),rgba(65,64,66,.45) 60%,rgba(65,64,66,.2)),linear-gradient(180deg,rgba(65,64,66,0) 55%,#414042)"></div>
  <div class="wrap">
    <p class="crumb"><a href="index.html">Home</a> / <a href="{s.get('crumb_url','services.html')}">{s.get('crumb','Services')}</a> / {e(s['short'])}</p>
    <h1 class="hl"><span class="ln"><span>{e(s['h1'][0])}</span></span><span class="ln"><span>{e(s['h1'][1])}</span></span></h1>
    <p class="lede">{e(s['lede'])}</p>
    <div class="acts" style="margin-top:36px"><a class="btn btn-w mag" href="contact.html">Get a proposal</a><a class="tlink" href="free-marketing-audit.html">Get a free audit</a></div>
  </div>
</section>
{CUSTOM.get(s['slug'],'')}<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">Overview</span><div><h2 class="mid" style="max-width:18ch">{e(s['intro_h'])}</h2><div class="two" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:24px 4vw;margin-top:30px"><p class="lede">{e(s['intro'][0])}</p><p class="dim">{e(s['intro'][1])}</p></div></div></div>
</div></section>
<section class="sec light" style="padding-top:0"><div class="wrap">
  <div class="row-head"><span class="lab">What's included</span><h2 class="big" style="max-width:16ch">{e(s.get('subs_h', s['short'] + ' services'))}</h2></div>
  <ul class="subs">{subs}</ul>
</div></section>
<section class="sec stone"><div class="wrap">
  <div class="row-head"><span class="lab">Work</span><h2 class="mid">{"Related work" if allreal else "Our work, and what it looks like"}</h2></div>
  <div class="strip">{strip}</div>{note}
  <p style="margin-top:36px"><a class="tlink" href="work.html" style="color:var(--ink)">See all work {ARROW}</a></p>
</div></section>
{CUSTOM_AFTER.get(s['slug'],'')}{RESULTS if s.get('results') else ''}
<section class="sec"><div class="wrap">
  <div class="row-head"><span class="lab">Process</span><h2 class="big">How we work</h2></div>
  <ol class="steps" style="margin:0;padding:0;list-style:none">{STEPS}</ol>
</div></section>
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">Where we work</span><div><h2 class="mid" style="max-width:20ch">{e(s.get('area_h', s['short'] + ' for businesses across the UAE'))}</h2>{AREAS}<p class="dim" style="margin-top:18px">{e(AREA_NOTE.get(s['slug'], 'From our Dubai office at B Hive, BurJuman, we work in person across Dubai and Sharjah and online with businesses in every emirate.'))}</p></div></div>
</div></section>
<section class="sec light" style="padding-top:0"><div class="wrap">
  <div class="row-head"><span class="lab">Questions</span><div class="faq faq-list">{faq}</div></div>
  <div class="row-head" style="margin:56px 0 0"><span class="lab">Related services</span><nav class="related" aria-label="Related services">{rel}<a href="services.html">All services</a></nav></div>{READS}
</div></section>'''
    title = s['title']
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": s['short'] + (" in " + s['city'] if s.get('city') else " in Dubai and the UAE"), "serviceType": s.get('stype', s['short']), "provider": {"@id": DOMAIN + "#org"}, "areaServed": ({"@type": "City", "name": s['city']} if s.get('city') else {"@type": "Country", "name": "United Arab Emirates"}), "url": DOMAIN + s['slug'] + '.html', "description": s['desc'],
              "hasOfferCatalog": {"@type": "OfferCatalog", "name": s['short'], "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": a, "description": b}} for a, b in s['subs']]}}
    return page(s['slug'], s.get('cur', 'services'), title, s['desc'], s.get('ftitle', "Let's talk about " + s['short'].lower() + "."), body,
                [svc_ld, faq_ld(s['faq']), crumbs_ld([("Home", ""), (s.get('crumb','Services'), s.get('crumb_url','services.html')), (s['short'], s['slug'] + '.html')])] + video_ld(s), {'Abu Dhabi': ('AE-AZ','Abu Dhabi'), 'Sharjah': ('AE-SH','Sharjah')}.get(s.get('city'), ('AE-DU','Dubai')))


def video_ld(s):
    names = {}
    for src, nm, cat, poster in re.findall(r'data-src="(assets/video/[^"]+\.mp4)"[^>]*?data-name="([^"]+)" data-cat="([^"]+)"[^>]*?poster="([^"]+)"', CUSTOM.get(s['slug'], '')):
        names[src] = H.unescape(nm) + ', ' + cat.lower()
    vids = [(m[0], m[3]) for m in re.findall(r'data-src="(assets/video/[^"]+\.mp4)"[^>]*?data-name="([^"]+)" data-cat="([^"]+)"[^>]*?poster="([^"]+)"', CUSTOM.get(s['slug'], ''))]
    vids += [(a, a.replace('.mp4', '.jpg')) for a, _ in s.get('work', []) if a.endswith('.mp4')]
    seen, out = set(), []
    for src, poster in vids:
        if src in seen: continue
        seen.add(src)
        nm = names.get(src) or dict((a, b) for a, b in s.get('work', [])).get(src) or src.split('/')[-1].replace('.mp4', '').replace('-', ' ').capitalize()
        out.append({"@context": "https://schema.org", "@type": "VideoObject", "name": nm + " | Ads n' Codes", "description": nm + ", produced by Ads n' Codes in the UAE.", "thumbnailUrl": DOMAIN + poster, "contentUrl": DOMAIN + src, "uploadDate": "2026-11-01T10:00:00+04:00", "publisher": {"@id": DOMAIN + "#org"}})
    return out


def location_page(L):
    e = H.escape
    if L['hero_img']:
        hero = f"""<section class="phero photo"><div class="ph-img">{PIC(L['hero_img'], '<img src="' + L['hero_img'] + '" fetchpriority="high" alt="' + e(L.get('hero_alt', L['city'])) + '">')}</div><div class="veil" aria-hidden="true" style="background:linear-gradient(90deg,rgba(65,64,66,.92),rgba(65,64,66,.5) 60%,rgba(65,64,66,.25)),linear-gradient(180deg,rgba(65,64,66,0) 55%,#414042)"></div>"""
    else:
        hero = '<section class="phero"><canvas class="silk" aria-hidden="true"></canvas><div class="veil" aria-hidden="true"></div>'
    focus = ''.join(f'<li><h3>{e(a)}</h3><p>{e(b)}</p></li>' for a, b in L['focus'])
    svc = ''.join(f'<a href="{x["slug"]}.html">{e(x["short"])}</a>' for x in SERVICES if not x.get('city') and not x.get('sub')) + '<a href="ai-automation.html">AI and automation</a>'
    local = [x for x in SERVICES if x.get('city') == L['city']]
    localnav = (f'<div class="row-head" style="margin:0 0 56px"><span class="lab">In {e(L["city"])}</span><div><h2 class="mid" style="max-width:22ch">Specialist services for {e(L["city"])}</h2><nav class="related" aria-label="{e(L["city"])} services" style="margin-top:28px">' + ''.join(f'<a href="{x["slug"]}.html">{e(x["short"])}</a>' for x in local) + '</nav></div></div>') if local else ''
    others = ''.join(f'<a href="{o["slug"]}.html">{e(o["city"] if o["city"] != "UAE" else "All of the UAE")}</a>' for o in LOCATIONS if o['slug'] != L['slug'])
    faq = ''.join(f'<div class="qa"><button type="button" aria-expanded="{"true" if i == 0 else "false"}" aria-controls="f{i}" id="fq{i}">{e(q)}<span class="pm" aria-hidden="true">+</span></button><div class="ans" id="f{i}" role="region" aria-labelledby="fq{i}"><div><p>{_mdl(e(a))}</p></div></div></div>' for i, (q, a) in enumerate(L['faq']))
    body = f"""{hero}
  <div class="wrap">
    <p class="crumb"><a href="index.html">Home</a> / {e(L['short'])}</p>
    <h1 class="hl"><span class="ln"><span>{e(L['h1'][0])}</span></span><span class="ln"><span>{e(L['h1'][1])}</span></span></h1>
    <p class="lede">{e(L['lede'])}</p>
    <div class="acts" style="margin-top:36px"><a class="btn btn-w mag" href="contact.html">Get a proposal</a><a class="tlink" href="free-marketing-audit.html">Get a free audit</a></div>
  </div>
</section>
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">{e(L['city'])}</span><div><h2 class="mid" style="max-width:18ch">{e(L['intro_h'])}</h2><div class="two" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:24px 4vw;margin-top:30px"><p class="lede">{e(L['intro'][0])}</p><p class="dim">{e(L['intro'][1])}</p></div></div></div>
</div></section>
<section class="sec light" style="padding-top:0"><div class="wrap">
  <div class="row-head"><span class="lab">Focus</span><h2 class="big" style="max-width:16ch">What we do for {e(L['city'])} businesses</h2></div>
  <ul class="subs">{focus}</ul>
  <p class="dim" style="margin-top:36px;max-width:60ch">Industries we work with here: {e(L['industries'])}</p>
</div></section>
<section class="sec stone"><div class="wrap">
  <div class="row-head"><span class="lab">How it works</span><div><h2 class="mid" style="max-width:20ch">Working with us from {e('anywhere in the UAE' if L['city'] == 'UAE' else L['city'])}</h2>
  <ol class="subs how-steps"><li><h3>1. A call, then a plan</h3><p>We start online: your goals, your customers and what is working now. You get a written plan and a fixed quote within a few days.</p></li><li><h3>2. On site when it matters</h3><p>Shoots, workshops and key meetings happen in person{'' if L['city'] == 'UAE' else ' in ' + e(L['city'])}. Everything else runs online so nothing waits on travel.</p></li><li><h3>3. One report a month</h3><p>Leads, cost per lead, rankings and what changes next month, in plain language, with one person to call.</p></li></ol>
  <p class="dim" style="margin-top:30px">Areas we cover{'' if L['city'] == 'UAE' else ' in and around ' + e(L['city'])}: {e(', '.join(LOC_AREAS.get(L["slug"], [])))}.</p></div></div>
</div></section>
{RESULTS}
<section class="sec stone"><div class="wrap">{localnav}
  <div class="row-head"><span class="lab">All services</span><div><h2 class="mid" style="max-width:20ch">Everything you need to grow, from one team</h2><nav class="related" aria-label="Services" style="margin-top:28px">{svc}</nav></div></div>
</div></section>
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">Questions</span><div class="faq faq-list">{faq}</div></div>
  <div class="row-head" style="margin:56px 0 0"><span class="lab">Other areas</span><nav class="related" aria-label="Other areas">{others}</nav></div>
</div></section>"""
    lb = {"@context": "https://schema.org", "@type": "Service", "name": "Digital marketing in " + L['city'], "serviceType": "Digital marketing", "provider": {"@id": DOMAIN + "#org"},
          "areaServed": {"@type": "Country" if L['city'] == 'UAE' else "City", "name": "United Arab Emirates" if L['city'] == 'UAE' else L['city']}, "url": DOMAIN + L['slug'] + '.html', "description": L['desc']}
    return page(L['slug'], None, L['title'], L['desc'], "Growing a business in " + ("the UAE" if L['city'] == 'UAE' else L['city']) + "? Let's talk.", body,
                [lb, faq_ld(L['faq']), crumbs_ld([("Home", ""), (L['short'], L['slug'] + '.html')])], (L['region'], L['city']))

STATIC = [
  ('index', None, "Ads n' Codes | Digital Marketing & Technology Agency in Dubai, UAE", "Digital marketing and technology agency in Dubai. Social media, paid ads, SEO, branding, photography, video, websites, apps and AI automation for businesses across the UAE.", "Tell us what's slowing your growth."),
  ('services', 'services', "Marketing, Branding & Tech Services in Dubai | Ads n' Codes", "All Ads n' Codes services in Dubai: digital marketing, SEO, branding, content, photography, video production, websites, e-commerce, apps, software and AI automation.", 'Pick a service. Or let us run all of it.'),
  ('ai-automation', 'ai', "AI Automation, WhatsApp Automation & AI Agents in Dubai | Ads n' Codes", "AI agents, WhatsApp automation, WhatsApp Business API setup, lead qualification, CRM automation and business process automation for businesses in Dubai and the UAE.", 'Show us the work your team repeats.'),
  ('work', 'work', "Our Work | Branding, Campaigns & AI Systems | Ads n' Codes Dubai", "Selected branding, packaging, campaign and AI automation work by Ads n' Codes, a digital marketing agency in Dubai.", 'Your brand could be the next one here.'),
  ('about', 'about', "About Ads n' Codes | Marketing & Technology Agency in Dubai", "The story behind Ads n' Codes, a marketing and technology agency based at B Hive, BurJuman, Dubai, working with businesses across the UAE.", "Let's build something people remember."),
  ('whatsapp-ai-agent-uae', 'ai', "WhatsApp Automation & AI Agent in Dubai, UAE | Lead Response | Ads n' Codes", "WhatsApp automation and AI agents on the official WhatsApp Business API for UAE businesses. Reply to every lead in seconds, qualify enquiries, take bookings and orders, and sync with your CRM or POS, 24/7.", 'Stop losing customers to slow replies.'),
  ('missed-enquiry-cost-calculator', 'ai', "Missed Enquiry Cost Calculator (UAE) | Ads n' Codes", "Free calculator for UAE businesses: see what slow WhatsApp and phone replies cost you each month, from your enquiries, reply time and customer value.", 'Want every enquiry answered in seconds? Talk to us.'),
  ('free-marketing-audit', None, "Free Marketing Audit for UAE Businesses | Ads n' Codes", "A free marketing audit for UAE businesses: social media, ads, Google and SEO, your website and WhatsApp reply speed, with the three fixes that matter most.", 'Prefer to talk it through? Message us.'),
  ('privacy', None, "Privacy Policy and Terms | Ads n' Codes", "How Ads n' Codes FZE LLC collects, uses and protects personal data under UAE law, and the terms for using this website.", 'Questions? Talk to us.'),
  ('contact', 'contact', "Contact Ads n' Codes | Digital Marketing Agency in Dubai", "Contact Ads n' Codes in Dubai. Email bd@adsncodes.com for projects, hello@adsncodes.com for general questions, or call and WhatsApp +971 56 544 0310.", 'Prefer to talk? We answer fast.'),
]
built = []
for name, cur, title, desc, ftitle in STATIC:
    if name in SEO: title, desc = SEO[name]
    body = (S / f'{name}.html').read_text().replace('{{VOICES}}', VOICES).replace('{{LANDING}}', LANDING).replace('{{AGENTSHOW}}', AGENTSHOW).replace('{{RESULTS}}', RESULTS).replace('{{CHATDEMO}}', CHAT_DEMO)
    extra = [crumbs_ld([("Home", ""), (title.split(' | ')[0], name + '.html')])] if name != 'index' else []
    if name == 'index':
        extra.append({"@context": "https://schema.org", "@type": "WebSite", "@id": DOMAIN + "#website", "name": "Ads n' Codes", "alternateName": ["Ads n Codes", "AdsnCodes", "Ads and Codes"], "url": DOMAIN, "publisher": {"@id": DOMAIN + "#org"}, "inLanguage": "en-AE"})
    if name in ('index', 'ai-automation'):
        qs = re.findall(r'id="[qp]\d+">([^<]+)<', body); ans = re.findall(r'aria-labelledby="[qp]\d+"><div><p>(.*?)</p>', body)
        if qs and len(qs) == len(ans): extra.append(faq_ld([(q, re.sub('<[^>]+>', '', a)) for q, a in zip(qs, ans)]))
    if name == 'whatsapp-ai-agent-uae':
        qa = re.findall(r'aria-labelledby="(wq\d)">[^<]*</button>|<button[^>]*id="wq\d">([^<]+)<span', body)
        qs = re.findall(r'id="wq\d+">([^<]+)<span', body); ans = [re.sub('<[^>]+>', '', a) for a in re.findall(r'aria-labelledby="wq\d+"><div><p>(.*?)</p>', body)]
        extra.append(faq_ld(list(zip(qs, ans))))
        extra.append({"@context": "https://schema.org", "@type": "Service", "name": "WhatsApp automation and AI agent for lead response", "serviceType": "WhatsApp automation", "provider": {"@id": DOMAIN + "#org"}, "areaServed": {"@type": "Country", "name": "United Arab Emirates"}, "url": DOMAIN + name + ".html"})
    if name in ('free-marketing-audit', 'missed-enquiry-cost-calculator'):
        qs = re.findall(r'id="[ac]qb\d+">([^<]+)<span', body); ans = [re.sub('<[^>]+>', '', x) for x in re.findall(r'aria-labelledby="[ac]qb\d+"><div><p>(.*?)</p>', body)]
        if qs and len(qs) == len(ans): extra.append(faq_ld(list(zip(qs, ans))))
    built.append(page(name, cur, title, desc, ftitle, body, extra))
for s in SERVICES:
    built.append(service_page(s))
for L in LOCATIONS:
    if L['slug'] in SEO: L['title'], L['desc'] = SEO[L['slug']]
    seo_boost.apply([L])
    built.append(location_page(L))
exec(open(R / 'agents_build.py').read(), globals())
exec(open(R / 'insights_build.py').read(), globals())
exec(open(R / 'case_build.py').read(), globals())
exec(open(R / 'ar_build.py').read(), globals())
exec(open(R / 'industries_build.py').read(), globals())
# llms.txt lines for scheduled pages, added the day they go live
from extra_services import LLMS_LINES
_ANCH = {'food-photography-dubai': 'corporate-photography-dubai.html', 'corporate-video-production-dubai': 'video-production-dubai.html',
         'micro-influencer-agency-dubai': 'influencer-marketing-dubai.html', 'insights-how-to-use-whatsapp-business-web': 'insights-whatsapp-business-multiple-users-uae.html'}
_lp = R / 'llms.txt'; _ll = _lp.read_text().split('\n')
for _slug, _line in LLMS_LINES.items():
    if _slug in built and _line not in _ll:
        _i = next((i for i, l in enumerate(_ll) if _ANCH[_slug] in l), len(_ll) - 1)
        _ll.insert(_i + 1, _line)
_lp.write_text('\n'.join(_ll))
# sitemap + robots
import datetime as _dt
_today = _dt.date.today().isoformat()
# lastmod only moves when a page's visible text changes, so Google keeps trusting it
import hashlib as _hl, json as _js
_lmf = R / 'lastmod.json'
_lm = _js.loads(_lmf.read_text()) if _lmf.exists() else {}
for n in built:
    _t = (R / (n + '.html')).read_text()
    _m = re.search(r'<main.*?</main>', _t, re.S)
    _v = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<script.*?</script>|<style.*?</style>', '', _m.group(0) if _m else _t, flags=re.S)))
    _h = _hl.md5((_v + re.search(r'<title>(.*?)</title>', _t).group(1)).encode()).hexdigest()
    if _lm.get(n, {}).get('h') != _h: _lm[n] = {'h': _h, 'd': _today}
_lmf.write_text(_js.dumps(_lm, indent=0))
urls = ''.join(f'<url><loc>{DOMAIN}{"" if n == "index" else n + ".html"}</loc><lastmod>{_lm[n]["d"]}</lastmod><changefreq>monthly</changefreq><priority>{"1.0" if n == "index" else "0.8"}</priority></url>' for n in built)
if AR_LIVE: urls += ''.join(f'<url><loc>{DOMAIN}{p}</loc><lastmod>{_today}</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>' for p, _ in AR_PAIRS)
(R / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
_bots = ['OAI-SearchBot', 'ChatGPT-User', 'GPTBot', 'Claude-SearchBot', 'Claude-User', 'ClaudeBot', 'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot-Extended', 'Bingbot', 'meta-externalagent', 'DeepSeekBot', 'CCBot']
(R / 'robots.txt').write_text('# Search engines and AI assistants are welcome to read and cite this site.\nUser-agent: *\nAllow: /\n\n' + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in _bots) + f'Sitemap: {DOMAIN}sitemap.xml\n')
print(len(built), 'pages:', ', '.join(built))
