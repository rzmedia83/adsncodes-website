"""Honest proof block for service pages: one named client quote, one Google review, plain facts.
No figures. Quotes and reviews are the real ones already on the homepage (src/_voices.html)."""
import os
QUOTES = {
    'mss': ("The campaign really worked for us. We saw a big jump in admission enquiries, and you could feel the message connecting with people.", "Mother MSS Group", "Nursing and education institutes"),
    'lk': ("They understood our vision from day one and brought our brand story to life with real creativity and heart.", "LaryKlean", "D2C clothing brand"),
    'carbar': ("They got what we had in mind straight away and turned it into something even better. The branding just feels like us.", "Carbar", "Car detailing and accessories"),
}
REVIEWS = {
    'clinic': ("Contacted them to get more enquiries for my wife's clinic. The content and lead generation worked really well and we started getting better enquiries. Happy with the work 👍", "Clinic"),
    'setup': ("They built our website and also helped us with our digital marketing. They understood our UAE business setup and PRO services and delivered exactly what we needed. Good experience working with them.", "Business setup and PRO services"),
    'garage': ("They did our garage website and also set up the lead automation for us. Everything was smooth and the website is much better now. Good work...", "Auto garage"),
}
# keyword in slug -> (quote, review); first match wins
MAP = [
    ('whatsapp', 'mss', 'garage'), ('ai-', 'mss', 'garage'), ('automation', 'carbar', 'garage'), ('chatbot', 'mss', 'garage'),
    ('clinic', 'mss', 'clinic'), ('healthcare', 'mss', 'clinic'), ('education', 'mss', 'clinic'), ('lead-generation', 'mss', 'clinic'),
    ('meta-ads', 'mss', 'clinic'), ('ppc', 'mss', 'setup'), ('real-estate', 'mss', 'clinic'),
    ('ecommerce', 'lk', 'setup'), ('fashion', 'lk', 'setup'), ('web', 'carbar', 'setup'), ('app-', 'carbar', 'setup'),
    ('seo', 'mss', 'setup'), ('email', 'lk', 'setup'),
    ('brand', 'carbar', 'setup'), ('automotive', 'carbar', 'garage'),
    ('social', 'lk', 'clinic'), ('instagram', 'lk', 'clinic'), ('content', 'lk', 'clinic'), ('ugc', 'lk', 'clinic'), ('influencer', 'lk', 'clinic'),
    ('photo', 'carbar', 'setup'), ('video', 'lk', 'clinic'), ('restaurant', 'lk', 'clinic'), ('hotel', 'lk', 'setup'),
]
REVIEW_URL = 'https://www.google.com/maps/place/?q=place_id:ChIJL8srqlxzh2kRtCTl_DkPRDY'
STAR = '<svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true"><path fill="#F5B400" d="M10 1.5l2.6 5.6 6.1.6-4.6 4.1 1.3 6-5.4-3.1-5.4 3.1 1.3-6L.3 7.7l6.1-.6z"/></svg>'
PREVIEW = set(filter(None, os.environ.get('PROOF_PREVIEW', '').split(',')))

def proof(slug, e):
    if slug not in PREVIEW: return ''
    q, r = 'lk', 'setup'
    for k, a, b in MAP:
        if k in slug: q, r = a, b; break
    qt, qn, qr = QUOTES[q]; rt, rr = REVIEWS[r]
    ai = any(k in slug for k in ('whatsapp', 'ai-', 'chatbot', 'automation'))
    third = ('<li><b>Try it before you buy</b><span>Our WhatsApp AI agents are live. <a href="ai-automation.html#demos">Open a demo</a> and talk to one.</span></li>' if ai else
             '<li><b>Free audit first</b><span>We look at what you have now and tell you what to fix, before any proposal. <a href="free-marketing-audit.html">Get the audit</a></span></li>')
    return f'''<section class="sec light pfb"><div class="wrap">
  <div class="row-head"><span class="lab">Clients</span><h2 class="mid" style="max-width:20ch">What it is like to work with us</h2></div>
  <div class="pf-grid">
    <figure class="pf-quote"><blockquote>&ldquo;{e(qt)}&rdquo;</blockquote><figcaption><b>{e(qn)}</b>{e(qr)}</figcaption></figure>
    <div class="pf-side">
      <div class="pf-review"><div class="gstars" role="img" aria-label="5 out of 5 stars">{STAR * 5}</div><p>{e(rt)}</p><span><b>{e(rr)}</b>Google review</span></div>
      <a class="tlink pf-g" href="{REVIEW_URL}" target="_blank" rel="noopener">Rated 5 stars on Google. Read the reviews</a>
    </div>
  </div>
  <ul class="pf-facts">
    <li><b>You deal with the founder</b><span>No account managers in between. The person you brief is the person doing the work.</span></li>
    <li><b>Marketing and tech in one place</b><span>Ads, content, websites and AI from one team, so nothing gets lost between agencies.</span></li>
    {third}
  </ul>
</div></section>
'''
