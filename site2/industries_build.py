# Industry landing pages and the industries hub. Exec'd from build.py with its globals.
from industries_data import INDUSTRIES, IND_COMMON
e = __import__("html").escape
for _i in INDUSTRIES:
    for k, v in IND_COMMON.items(): _i.setdefault(k, v)
    _i.setdefault('subs_h', 'What we do for ' + _i['ind'].lower())
    BYSLUG[_i['slug']] = _i
for _i in INDUSTRIES:
    built.append(service_page(_i))

_cards = ''.join(f'''<a class="indc" href="{i['slug']}.html"><span class="indc-m"><img src="{i['img']}" alt="{e(i['alt'])}" loading="lazy"></span><span class="indc-t"><b>{e(i['ind'])}</b><span>{e(i['lede'].split('. ')[0])}.</span><em>{e(i['short'])} {ARROW}</em></span></a>''' for i in INDUSTRIES)
_body = f'''<style>
.indgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));gap:clamp(16px,2vw,26px)}}
.indc{{display:flex;flex-direction:column;text-decoration:none;color:inherit;border-radius:var(--rad);overflow:hidden;background:linear-gradient(180deg,#fff,#fbfaf8);box-shadow:0 5px 0 #e7e4de,0 22px 40px rgba(20,20,22,.07)}}
.indc-m{{aspect-ratio:4/3;overflow:hidden;display:block}}
.indc-m img{{width:100%;height:100%;object-fit:cover;transition:transform 1.2s var(--ease)}}
.indc:hover .indc-m img{{transform:scale(1.05)}}
.indc-t{{display:flex;flex-direction:column;gap:8px;padding:22px 22px 24px}}
.indc-t b{{font:500 clamp(22px,1.9vw,28px)/1.1 var(--display);letter-spacing:-.03em}}
.indc-t span{{color:var(--ink-70);font-size:15px;line-height:1.5}}
.indc-t em{{font-style:normal;font-size:14px;display:inline-flex;gap:8px;align-items:center;margin-top:6px}}
</style>
<section class="phero">
  <canvas class="silk" aria-hidden="true"></canvas><div class="veil" aria-hidden="true"></div>
  <div class="wrap">
    <p class="crumb"><a href="index.html">Home</a> / Industries</p>
    <h1 class="hl"><span class="ln"><span>Marketing by</span></span><span class="ln"><span>industry, UAE</span></span></h1>
    <p class="lede">Every sector buys differently. Property buyers message three agents in one evening, diners decide on a reel, patients choose the doctor they already trust. Here is how we work in each one.</p>
  </div>
</section>
<section class="sec light"><div class="wrap">
  <div class="indgrid">{_cards}</div>
  <p class="dim" style="margin-top:36px;max-width:62ch">Also construction and contracting, beauty and wellness, trading, B2B and professional services. If your customers search, scroll or message before they buy, <a href="contact.html">we can help</a>.</p>
</div></section>'''
_ild = {"@context": "https://schema.org", "@type": "ItemList", "name": "Industries we market in the UAE", "itemListElement": [{"@type": "ListItem", "position": n + 1, "url": DOMAIN + i['slug'] + '.html', "name": i['short']} for n, i in enumerate(INDUSTRIES)]}
built.append(page('industries', None, "Marketing Agency by Industry in Dubai & UAE | Ads n' Codes",
                  "Industry marketing in Dubai and the UAE for real estate, automotive, clinics, restaurants, hotels, e-commerce, education and fashion brands.",
                  "Tell us about your industry.", _body, [_ild, crumbs_ld([("Home", ""), ("Industries", "industries.html")])]))
