# WhatsApp AI agent pages by industry. Exec'd from build.py with its globals, before industries.
from agents_data import AGENTS, AG_COMMON, DEMOS
_e = __import__("html").escape
def _demo_sec(d):
    return ('<section class="sec stone re-demo"><div class="wrap">'
      '<style>.re-demo .redm{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:6vw;align-items:center;margin-top:56px}'
      '.re-demo .redm-ph{display:flex;justify-content:center}.re-demo .redm-ph img{width:min(100%,300px);height:auto;filter:drop-shadow(0 30px 50px rgba(0,0,0,.25))}'
      '.re-demo ol{list-style:none;margin:0;padding:0;counter-reset:r}.re-demo li{counter-increment:r;display:grid;grid-template-columns:44px 1fr;padding:16px 0;border-top:1px solid rgba(20,20,22,.12)}.re-demo li:before{content:counter(r,decimal-leading-zero);font-size:13px;color:#8a7a5a;padding-top:3px}.re-demo li b,.re-demo li span{grid-column:2}.re-demo li b{display:block;font-weight:500}.re-demo li span{color:var(--ink-70)}'
      '@media (max-width:860px){.re-demo .redm{grid-template-columns:minmax(0,1fr)}.re-demo .redm-ph{order:2}.re-demo .redm-ph img{width:min(66%,250px)}}</style>'
      f'<div class="row-head"><span class="lab">Live demo</span><div><h2 class="big" style="max-width:15ch">{_e(d["h"])}</h2>'
      f'<p class="lede dim" style="margin-top:22px;max-width:52ch">{_e(d["p"])}</p>'
      f'<div class="acts" style="margin-top:34px;display:flex;gap:26px;align-items:center;flex-wrap:wrap"><a class="btn btn-i mag" href="{d["url"]}">Try the demo</a>'
      '<a class="tlink" style="color:var(--ink)" href="https://wa.me/971565440310?text=Hi%2C%20I%27d%20like%20a%20free%20WhatsApp%20agent%20demo%20built%20for%20my%20business.">Ask for a demo built on your business</a></div></div></div>'
      f'<div class="redm"><div class="redm-ph"><a href="{d["url"]}"><img src="{d["img"]}" alt="{_e(d["alt"])}" loading="lazy" width="831" height="1742"></a></div>'
      '<div><ol class="ag-steps">' + ''.join(f'<li><b>{_e(t)}</b><span>{_e(x)}</span></li>' for t, x in d['steps']) + '</ol></div></div>'
      '</div></section>')
for _a in AGENTS:
    for k, v in AG_COMMON.items(): _a.setdefault(k, v)
    BYSLUG[_a['slug']] = _a
    CUSTOM[_a['slug']] = _demo_sec(DEMOS[_a['demo']])
    seo_boost.apply([_a])
for _a in AGENTS:
    built.append(service_page(_a))
