# ---------- insights ----------
e = __import__("html").escape
from articles_data import ARTICLES
BYSLUG['whatsapp-ai-agent-uae'] = dict(short='WhatsApp automation')
BIOS = {
  'Razal Mohammed': "is the founder of Ads n' Codes and leads its AI automation and WhatsApp agent work.",
  'Shabeeb Mohd': "works with Ads n' Codes on lead generation, local search and campaign performance for UAE businesses.",
  'Hafeeda': "works with Ads n' Codes on content, influencer and UGC campaigns for brands in the UAE.",
}

def _inline(t):
    t = e(t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
def _date(d):
    import datetime as _dt
    return _dt.date.fromisoformat(d).strftime('%-d %B %Y')
def article_page(a):
    parts = []
    for kind, v in a['body']:
        if kind == 'p': parts.append(f'<p>{_inline(v)}</p>')
        elif kind == 'h2': parts.append(f'<h2>{e(v)}</h2>')
        elif kind == 'img': parts.append(f'<figure class="art-fig"><img src="{v[0]}" alt="{e(v[1])}" width="1480" height="832" loading="lazy" decoding="async"><figcaption>{e(v[1])}</figcaption></figure>')
        elif kind == 'ul': parts.append('<ul>' + ''.join(f'<li>{_inline(x)}</li>' for x in v) + '</ul>')
    faq = ''.join(f'<div class="qa"><button type="button" aria-expanded="{"true" if i == 0 else "false"}" aria-controls="f{i}" id="fq{i}">{e(q)}<span class="pm" aria-hidden="true">+</span></button><div class="ans" id="f{i}" role="region" aria-labelledby="fq{i}"><div><p>{e(x)}</p></div></div></div>' for i, (q, x) in enumerate(a['faq']))
    src = ''
    if a.get('sources'):
        src = '<div class="art-src"><p>Sources</p><ul>' + ''.join(f'<li><a href="{u}" target="_blank" rel="nofollow noopener">{e(t)}</a></li>' for t, u in a['sources']) + '</ul></div>'
    rel = ''.join(f'<a href="{r}.html">{e(BYSLUG[r]["short"])}</a>' for r in a['related'])
    others = [o for o in ARTICLES if o['slug'] != a['slug']][:3]
    more = ''.join(f'<a class="icard" href="insights-{o["slug"]}.html"><span>{e(o["kicker"])}</span><h3>{e(o["h1"])}</h3><em>{o["read"]} read</em></a>' for o in others)
    body = f"""<section class="phero">
  <canvas class="silk" aria-hidden="true"></canvas><div class="veil" aria-hidden="true"></div>
  <div class="wrap">
    <p class="crumb"><a href="index.html">Home</a> / <a href="insights.html">Insights</a> / {e(a['kicker'])}</p>
    <h1 class="hl art-h1">{e(a['h1'])}</h1>
    <p class="lede">{e(a['lede'])}</p>
    <p class="art-meta">By {a.get('author','Razal Mohammed')} · {_date(a['date'])} · {a['read']} read</p>
  </div>
</section>
<section class="sec light"><div class="wrap">
  <article class="prose">{''.join(parts)}{src}<p class="art-by"><b>{a.get('author','Razal Mohammed')}</b> {BIOS.get(a.get('author','Razal Mohammed'), '')}</p></article>
</div></section>
<section class="sec stone"><div class="wrap">
  <div class="row-head"><span class="lab">Questions</span><div class="faq">{faq}</div></div>
  <div class="row-head" style="margin-top:56px"><span class="lab">Related services</span><p class="areas">{rel}</p></div>
</div></section>
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">Keep reading</span><h2 class="mid">More from Insights</h2></div>
  <div class="icards">{more}</div>
</div></section>"""
    url = DOMAIN + 'insights-' + a['slug'] + '.html'
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a['h1'], "description": a['desc'], "datePublished": a['date'], "dateModified": a['date'],
          "author": dict({"@type": "Person", "name": a.get('author','Razal Mohammed')}, **({"url": DOMAIN + "about.html"} if a.get('author','Razal Mohammed') == 'Razal Mohammed' else {})), "publisher": {"@id": DOMAIN + "#org"},
          "mainEntityOfPage": url, "inLanguage": "en-AE", "image": DOMAIN + OGMAP.get("insights-" + a["slug"], "assets/og.jpg")}
    return page('insights-' + a['slug'], 'insights', a['title'], a['desc'], "Want this done for your business? Let's talk.", body,
                [ld, faq_ld(a['faq']), crumbs_ld([("Home", ""), ("Insights", "insights.html"), (a['h1'], 'insights-' + a['slug'] + '.html')])])
def insights_index():
    cards = ''.join(f'<a class="icard" href="insights-{a["slug"]}.html"><span>{e(a["kicker"])}</span><h3>{e(a["h1"])}</h3><p>{e(a["lede"])}</p><em>{a["read"]} read</em></a>' for a in ARTICLES)
    body = f"""<section class="phero">
  <canvas class="silk" aria-hidden="true"></canvas><div class="veil" aria-hidden="true"></div>
  <div class="wrap">
    <p class="crumb"><a href="index.html">Home</a> / Insights</p>
    <h1 class="hl"><span class="ln"><span>Insights</span></span></h1>
    <p class="lede">Practical notes on marketing, search and automation for businesses in Dubai and the UAE.</p>
  </div>
</section>
<section class="sec light"><div class="wrap"><h2 class="sr-only">All articles</h2><div class="icards">{cards}</div></div></section>"""
    return page('insights', 'insights', "Marketing Insights for UAE Businesses | Ads n' Codes", "Practical guides for Dubai and UAE businesses on WhatsApp automation, local SEO, influencer marketing, UGC and growing with digital marketing.", "Have a question we haven't covered? Ask us.", body,
                [crumbs_ld([("Home", ""), ("Insights", "insights.html")])])
built.append(insights_index())
for a in ARTICLES: built.append(article_page(a))
