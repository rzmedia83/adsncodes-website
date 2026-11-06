# ---------- case studies ----------
from case_data import CASES, SHORT_CASES
_e = __import__("html").escape

def _cinline(t):
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', _e(t))

def case_page(c):
    parts = []
    for kind, v in c['body']:
        if kind == 'p': parts.append(f'<p>{_cinline(v)}</p>')
        elif kind == 'h2': parts.append(f'<h2>{_e(v)}</h2>')
        elif kind == 'ul': parts.append('<ul>' + ''.join(f'<li>{_cinline(x)}</li>' for x in v) + '</ul>')
    stats = ''.join(f'<li><b>{_e(a)}</b><span>{_e(b)}</span></li>' for a, b in c['stats'])
    proof = ''
    if c.get('proof'):
        figs = ''.join(f'<figure><div class="shot-frame"><img src="{src}" alt="{_e(alt)}" loading="lazy" width="{w}" height="{h}"></div><figcaption><b>{_e(t1)}</b>{_e(t2)}</figcaption></figure>' for src, alt, w, h, t1, t2 in c['proof'])
        proof = f'<div class="proof proof-2">{figs}</div><p class="proof-note">Screenshots from the client\'s live ad accounts. Client details removed.</p>'
    faq = ''.join(f'<div class="qa"><button type="button" aria-expanded="{"true" if i == 0 else "false"}" aria-controls="f{i}" id="fq{i}">{_e(q)}<span class="pm" aria-hidden="true">+</span></button><div class="ans" id="f{i}" role="region" aria-labelledby="fq{i}"><div><p>{_cinline(x)}</p></div></div></div>' for i, (q, x) in enumerate(c['faq']))
    svc = ''.join(f'<a href="{u}.html">{_e(n)}</a>' for n, u in c['services'])
    others = ''.join(f'<a class="icard" href="case-study-{o["slug"]}.html"><span>{_e(o["kicker"])}</span><h3>{_e(o["h1"])}</h3><em>Case study</em></a>' for o in CASES if o['slug'] != c['slug'])
    body = f"""<section class="phero">
  <canvas class="silk" aria-hidden="true"></canvas><div class="veil" aria-hidden="true"></div>
  <div class="wrap">
    <p class="crumb"><a href="index.html">Home</a> / <a href="case-studies.html">Case studies</a> / {_e(c['short'])}</p>
    <h1 class="hl art-h1">{_e(c['h1'])}</h1>
    <p class="lede">{_e(c['lede'])}</p>
    <p class="art-meta">{_e(c['kicker'])} · Client name kept private</p>
  </div>
</section>
<section class="sec" id="results"><div class="wrap">
  <div class="row-head"><span class="lab">Results</span><h2 class="mid" style="max-width:18ch">The numbers</h2></div>
  <ul class="results">{stats}</ul>{proof}
</div></section>
<section class="sec light"><div class="wrap">
  <article class="prose">{''.join(parts)}</article>
</div></section>
<section class="sec stone"><div class="wrap">
  <div class="row-head"><span class="lab">Questions</span><div class="faq">{faq}</div></div>
  <div class="row-head" style="margin-top:56px"><span class="lab">Services used</span><p class="areas">{svc}</p></div>
</div></section>
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">More results</span><h2 class="mid">Other case studies</h2></div>
  <div class="icards">{others}</div>
  <p style="margin-top:36px"><a class="tlink" href="case-studies.html">All case studies</a></p>
</div></section>"""
    url = DOMAIN + 'case-study-' + c['slug'] + '.html'
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": c['h1'], "description": c['desc'], "about": c['kicker'],
          "author": {"@id": DOMAIN + "#org"}, "publisher": {"@id": DOMAIN + "#org"}, "mainEntityOfPage": url, "inLanguage": "en-AE",
          "datePublished": "2026-11-05", "dateModified": "2026-11-05", "image": DOMAIN + (c['proof'][0][0] if c.get('proof') else "assets/og.jpg")}
    return page('case-study-' + c['slug'], 'work', c['title'], c['desc'], "Want results like these? Let's talk.", body,
                [ld, faq_ld(c['faq']), crumbs_ld([("Home", ""), ("Case studies", "case-studies.html"), (c['short'], 'case-study-' + c['slug'] + '.html')])])

def _row(tag, name, text, num, numtxt, link=None, ext=None):
    extra = ''
    if link: extra = f'<p style="margin-top:14px"><a class="tlink" href="{link}" style="color:var(--ink)">Read the case study</a></p>'
    elif ext: extra = f'<p style="margin-top:14px"><a class="tlink" href="{ext}" target="_blank" rel="noopener" style="color:var(--ink)">Visit the store</a></p>'
    return f'<article class="case-row"><div><span class="tagl">{_e(tag)}</span><h3>{_e(name)}</h3>{extra}</div><div><p>{_e(text)}</p></div><div><div class="num">{_e(num)}</div><p>{_e(numtxt)}</p></div></article>'

def cases_hub():
    rows = ''.join(_row(c['kicker'], c['short'], c['lede'], c['stats'][0][0], c['stats'][0][1], 'case-study-' + c['slug'] + '.html') for c in CASES)
    rows += ''.join(_row(t, n, x, num, nt, None, ext) for t, n, x, num, nt, ext in SHORT_CASES)
    body = f"""<section class="phero">
  <canvas class="silk" aria-hidden="true"></canvas><div class="veil" aria-hidden="true"></div>
  <div class="wrap">
    <p class="crumb"><a href="index.html">Home</a> / <a href="work.html">Work</a> / Case studies</p>
    <h1 class="hl"><span class="ln"><span>Case studies</span></span></h1>
    <p class="lede">What we did for businesses in the UAE and the region, and what changed. Client names are kept private. The numbers come from their ad accounts and analytics.</p>
  </div>
</section>
<section class="sec light"><div class="wrap">
  <h2 class="sr-only">All case studies</h2>
  <div class="cases">{rows}</div>
</div></section>
{RESULTS.replace('<p style="margin-top:28px"><a class="tlink" href="case-studies.html" style="color:var(--paper)">Read the case studies</a></p>', '')}"""
    ld = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": DOMAIN + 'case-study-' + c['slug'] + '.html', "name": c['h1']} for i, c in enumerate(CASES)]}
    return page('case-studies', 'work', "Marketing Case Studies & Results, UAE | Ads n' Codes", "Case studies from Ads n' Codes: lead generation, Google Ads, Meta ads, SEO and branding results for UAE businesses, with numbers from live ad accounts.",
                "Want to be the next case study? Let's talk.", body, [ld, crumbs_ld([("Home", ""), ("Work", "work.html"), ("Case studies", "case-studies.html")])])

built.append(cases_hub())
for c in CASES: built.append(case_page(c))
