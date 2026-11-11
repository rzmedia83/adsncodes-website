# One section per key page that only that page has.

def _clip(src, name, cat, vert=False, start=0, poster=None):
    poster = poster or src.replace('.mp4', '.jpg')
    bg = f' style="background-image:url({src.replace(".mp4", "-bg.jpg")})"' if vert else ''
    cls = 'sr-v vert' if vert else 'sr-v'
    hd = ' data-hd="assets/video/ragam-home.mp4"' if src.endswith('ragam-720.mp4') else ''
    return (f'<video class="{cls}"{hd} data-src="{src}" data-start="{start}" data-name="{name}" data-cat="{cat}" '
            f'poster="{poster}" muted playsinline preload="none"{bg}></video>')

_CLIPS = [
    ('assets/video/ragam-hd.mp4', "Ragam '23", 'Event film', False, 0),
    ('assets/video/auto-brand-reel-hd.mp4', 'Brand reel', 'Vehicle testing centre, shoot and edit', True, 0),
    ('assets/video/event-tech-expo-hd.mp4', 'Tech expo', 'Event film for an exhibitor', False, 0),
    ('assets/video/portrait-film-hd.mp4', 'Fashion film', 'Concept, styling, shoot and edit', True, 12),
    ('assets/video/ad-clinic-hd.mp4', 'Clinic video ad', 'Script, shoot and edit', True, 0),
    ('assets/video/social-package-hd.mp4', 'Social media ad', 'Presenter led video ad', True, 0),
]

SHOWREEL = ('<section class="sec reel-sec"><div class="wrap">'
  '<div class="row-head"><span class="lab">Showreel</span><div><h2 class="big" style="max-width:14ch">Our work, in motion</h2>'
  '<p class="lede dim" style="margin-top:22px;max-width:52ch">Event films, brand reels, fashion and video ads. Each one planned, shot and edited by us.</p></div></div>'
  '<div class="sreel" data-sreel><div class="sreel-stage">'
  + ''.join(_clip(*c) for c in _CLIPS) +
  '<div class="sreel-cap"><b></b><span></span></div>'
  '<button type="button" class="sreel-sound" aria-pressed="false" aria-label="Turn sound on"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 9h4l5-4v14l-5-4H4z"/><path class="w1" d="M16.5 8.5a5 5 0 0 1 0 7"/><path class="x1" d="M16 9l5 6M21 9l-5 6"/></svg><span>Sound</span></button>'
  '</div><div class="sreel-tabs" role="tablist">'
  + ''.join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}"><i></i><b>{c[1]}</b><span>{c[2]}</span></button>' for i, c in enumerate(_CLIPS)) +
  '</div><div class="sreel-foot"><span>Selected cuts from recent shoots. Events, fashion, founders, clinics and brands.</span><a class="tlink" href="work.html#campaign">See more video work</a></div></div></div></section>\n')

_MORE_BA = [('assets/work/cloants-bag.webp', 'Cloants', 'Apparel'), ('assets/work/iedc-tote.webp', 'IEDC', 'Anniversary identity'), ('assets/work/velt-logistics.webp', 'Velt Logistics', 'Logistics'), ('assets/work/auditorium-cards.webp', 'Auditorium Booking', 'Digital product')]
_CASES = [
    ('carbar', 'Carbar', 'assets/work/carbar-logo-cut.webp', '#EDDBC8', 'assets/work/carbar-facade.webp', 'Carbar identity on a building facade', 'Car care brand'),
    ('orula', 'Orula', 'assets/work/orula-logo.png', '#f3f0e8', 'assets/work/orula-store.webp', 'Orula identity on a storefront', 'Meal management brand'),
]
BEFORE_AFTER = ('<section class="sec stone ba-sec"><div class="wrap">'
  '<div class="row-head"><span class="lab">Logo vs brand</span><div><h2 class="big" style="max-width:15ch">A logo is the start. The brand is everything around it.</h2>'
  '<p class="lede dim" style="margin-top:22px;max-width:52ch">Drag across to see one mark become a full identity: signage, colour, type and the places customers meet it.</p></div></div>'
  '<div class="ba-tabs" role="tablist">'
  + ''.join(f'<button type="button" role="tab" data-case="{k}" aria-selected="{"true" if i == 0 else "false"}">{n}<span>{t}</span></button>' for i, (k, n, _, _, _, _, t) in enumerate(_CASES)) +
  '</div><div class="ba" data-ba style="--v:50%">'
  + ''.join(f'<div class="ba-case{" on" if i == 0 else ""}" data-case="{k}"><img class="ba-after" src="{after}" alt="{alt}" loading="lazy"><div class="ba-before" style="background:{bg}"><img src="{logo}" alt="{n} logo" loading="lazy"></div></div>' for i, (k, n, logo, bg, after, alt, _) in enumerate(_CASES)) +
  '<span class="ba-lab l">The logo</span><span class="ba-lab r">The brand</span>'
  '<span class="ba-line" aria-hidden="true"><span class="ba-knob"><img src="assets/mark-white.png" alt=""></span></span>'
  '<input class="ba-range" type="range" min="0" max="100" value="50" aria-label="Compare the logo with the full brand identity">'
  '</div>'
  + '<div class="more-row"><span class="lab">More identities we built</span><div class="more-grid">'
  + ''.join(f'<a href="work.html#brand"><img src="{s}" alt="{n} brand identity" loading="lazy"><b>{n}</b><span>{k}</span></a>' for s, n, k in _MORE_BA) +
  '</div><a class="tlink" href="work.html#brand">See all branding work</a></div>' +
  '</div></section>\n')


RE_DEMO = ('<section class="sec stone re-demo"><div class="wrap">'
  '<style>.re-demo .redm{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:6vw;align-items:center}'
  '.re-demo .redm-ph{display:flex;justify-content:center}.re-demo .redm-ph img{width:min(100%,300px);height:auto;filter:drop-shadow(0 30px 50px rgba(0,0,0,.25))}'
  '.re-demo .redm{margin-top:56px}.re-demo ol{list-style:none;margin:0;padding:0;counter-reset:r}.re-demo li{counter-increment:r;display:grid;grid-template-columns:44px 1fr;padding:16px 0;border-top:1px solid var(--line,rgba(20,20,22,.12))}'
  '.re-demo li:before{content:counter(r,decimal-leading-zero);font-size:13px;color:#8a7a5a;padding-top:3px}.re-demo li b,.re-demo li span{grid-column:2}.re-demo li b{display:block;font-weight:500}.re-demo li span{color:var(--ink-70)}'
  '@media (max-width:860px){.re-demo .redm{grid-template-columns:minmax(0,1fr)}.re-demo .redm-ph{order:2}.re-demo .redm-ph img{width:min(66%,250px)}}</style>'
  '<div class="row-head"><span class="lab">Live demo</span><div><h2 class="big" style="max-width:15ch">Pick a lead. Watch it turn into a viewing.</h2>'
  '<p class="lede dim" style="margin-top:22px;max-width:52ch">Try our real estate agent as an Instagram ad lead, a portal enquiry, a tenant, an owner or an overseas investor messaging at 11:40 PM. Then open Behind the scenes to see the lead record, routing and CRM updates your team receives.</p></div></div>'
  '<div class="redm"><div class="redm-ph"><a href="https://realestate.adsncodes.com"><img src="assets/img/demo-re-match.webp" alt="WhatsApp agent for a Dubai brokerage matching a typed request to Dubai Marina listings with prices" loading="lazy" width="831" height="1742"></a></div>'
  '<div><ol><li><b>Replies in seconds, in the lead\'s language</b><span>Ad, portal and website leads get an answer day or night, in English, Arabic, Russian and more, on your own number.</span></li>'
  '<li><b>Qualifies and matches from your listings</b><span>Budget, area, bedrooms, ready or off plan and finance, then matching homes from your live feed with price, permit and floor plan.</span></li>'
  '<li><b>Books the viewing with the right agent</b><span>In person, at the sales gallery or by video, from your agents\' calendars, routed by area and language.</span></li>'
  '<li><b>Hands over and follows up</b><span>Your agent joins the same chat with the full brief. Quiet leads hear back when a new listing fits.</span></li></ol>'
  '<div class="acts" style="margin-top:34px;display:flex;gap:26px;align-items:center;flex-wrap:wrap"><a class="btn btn-i mag" href="https://realestate.adsncodes.com">Try the demo</a><a class="tlink" href="whatsapp-ai-agent-real-estate-dubai.html" style="color:var(--ink)">How the real estate agent works</a></div>'
  '</div></div>'
  '</div></section>')

RE_AGENT = ('<section class="sec light re-demo" style="border-top:1px solid rgba(65,64,66,.1)"><div class="wrap">'
  '<style>.re-demo .redm{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:6vw;align-items:center}'
  '.re-demo .redm-ph{display:flex;justify-content:center}.re-demo .redm-ph img{width:min(100%,300px);height:auto;filter:drop-shadow(0 30px 50px rgba(0,0,0,.25))}'
  '.re-demo .redm{margin-top:56px}.re-demo ol{list-style:none;margin:0;padding:0;counter-reset:r}.re-demo li{counter-increment:r;display:grid;grid-template-columns:44px 1fr;padding:16px 0;border-top:1px solid var(--line,rgba(20,20,22,.12))}'
  '.re-demo li:before{content:counter(r,decimal-leading-zero);font-size:13px;color:#8a7a5a;padding-top:3px}.re-demo li b,.re-demo li span{grid-column:2}.re-demo li b{display:block;font-weight:500}.re-demo li span{color:var(--ink-70)}'
  '@media (max-width:860px){.re-demo .redm{grid-template-columns:minmax(0,1fr)}.re-demo .redm-ph{order:2}.re-demo .redm-ph img{width:min(66%,250px)}}</style>'
  '<div class="row-head"><span class="lab">After the click</span><div><h2 class="big" style="max-width:15ch">Every enquiry answered, qualified and booked.</h2>'
  '<p class="lede dim" style="margin-top:22px;max-width:52ch">Your campaigns bring the leads. Our WhatsApp AI agent makes sure none go cold: it replies in seconds, day or night, shares matching listings, and books the viewing with the right agent. Try it as a buyer, a tenant or an overseas investor.</p></div></div>'
  '<div class="redm"><div class="redm-ph"><a href="https://realestate.adsncodes.com"><img src="assets/img/demo-re-match.webp" alt="WhatsApp agent for a Dubai brokerage matching a typed request to Dubai Marina listings with prices" loading="lazy" width="831" height="1742"></a></div>'
  '<div><ol><li><b>Replies in seconds, in the lead\'s language</b><span>Ad, portal and website leads get an answer day or night, in English, Arabic, Russian and more, on your own number.</span></li>'
  '<li><b>Qualifies and matches from your listings</b><span>Budget, area, bedrooms, ready or off plan and finance, then matching homes from your live feed with price, permit and floor plan.</span></li>'
  '<li><b>Books the viewing with the right agent</b><span>In person, at the sales gallery or by video, from your agents\' calendars, routed by area and language.</span></li>'
  '<li><b>Hands over and follows up</b><span>Your agent joins the same chat with the full brief. Quiet leads hear back when a new listing fits.</span></li></ol>'
  '<div class="acts" style="margin-top:34px;display:flex;gap:26px;align-items:center;flex-wrap:wrap"><a class="btn btn-i mag" href="https://realestate.adsncodes.com">Try the demo</a><a class="tlink" href="whatsapp-ai-agent-real-estate-dubai.html" style="color:var(--ink)">How the real estate agent works</a></div>'
  '</div></div>'
  '</div></section>')


def _agent_sec(h2, lede, url, img, alt, steps, more_href, more_txt):
    head = RE_AGENT[:RE_AGENT.index('<div class="row-head">')]
    li = ''.join(f'<li><b>{b}</b><span>{t}</span></li>' for b, t in steps)
    return (head + '<div class="row-head"><span class="lab">After the click</span><div><h2 class="big" style="max-width:15ch">' + h2 + '</h2>'
      '<p class="lede dim" style="margin-top:22px;max-width:52ch">' + lede + '</p></div></div>'
      '<div class="redm"><div class="redm-ph"><a href="' + url + '"><img src="' + img + '" alt="' + alt + '" loading="lazy" width="831" height="1742"></a></div>'
      '<div><ol>' + li + '</ol>'
      '<div class="acts" style="margin-top:34px;display:flex;gap:26px;align-items:center;flex-wrap:wrap"><a class="btn btn-i mag" href="' + url + '">Try the demo</a><a class="tlink" href="' + more_href + '" style="color:var(--ink)">' + more_txt + '</a></div>'
      '</div></div></div></section>')

CLINIC_AGENT = _agent_sec("Every patient enquiry answered and booked.",
  "Your campaigns bring the enquiries. Our WhatsApp AI agent makes sure none of them wait: it answers questions about treatments, prices and doctors in seconds, day or night, and books the appointment inside WhatsApp. Try it as a patient.",
  'https://medicare.adsncodes.com', 'assets/img/demo-clinic-wa.webp', 'WhatsApp agent for a Dubai clinic showing treatments and a booking form inside the chat',
  [("Replies in seconds, in the patient\'s language", "Ad, Google profile and website enquiries get an answer at any hour, in English, Arabic and more, on your clinic\'s own number."),
   ("Answers the usual questions", "Treatments, prices, insurance, doctors and branches, using only information your clinic approves."),
   ("Books with the right doctor", "Patients choose the doctor, branch, date and time in one form inside the chat."),
   ("Confirms and reminds", "A clear confirmation, a reminder before the visit, and the booking lands in the system your team already uses.")],
  'whatsapp-ai-agent-clinics-dubai.html', 'How the clinic agent works')

RESTO_AGENT = _agent_sec("Every order taken, even in the rush.",
  "Your ads and Instagram bring hungry customers. Our WhatsApp ordering agent takes the order in seconds: menu cards, typed orders understood, delivery or pickup, and the order sent straight to your kitchen, without aggregator commission. Try it as a customer.",
  'https://grillhouse.adsncodes.com', 'assets/img/demo-grillhouse.webp', 'WhatsApp ordering agent for a Dubai restaurant showing menu cards and an order summary',
  [("Shows the menu as cards", "Dish photos, prices and today\'s offers, right inside WhatsApp."),
   ("Understands typed orders", "A message like 2 chicken shawarma, 1 large fries, no garlic becomes a priced summary."),
   ("Checkout in one form", "Delivery or pickup, address and payment on a single screen."),
   ("Straight to the kitchen", "The order reaches your POS or kitchen screen and the customer gets updates until it arrives.")],
  'whatsapp-ordering-restaurants-dubai.html', 'How WhatsApp ordering works')

CUSTOM_AFTER = {'real-estate-marketing-agency-dubai': RE_AGENT, 'healthcare-marketing-agency-dubai': CLINIC_AGENT, 'restaurant-marketing-agency-dubai': RESTO_AGENT}

CUSTOM = {'video-production-dubai': SHOWREEL, 'branding-agency-dubai': BEFORE_AFTER}

CHAT_DEMO = '''<section class="sec stone chat-sec" id="try"><div class="wrap chat-in">
  <div class="chat-copy">
    <div class="row-head" style="display:block;margin:0"><span class="lab">Try it</span></div>
    <h2 class="big" style="max-width:12ch;margin-top:18px">See it answer on WhatsApp</h2>
    <p class="lede dim" style="margin-top:22px;max-width:40ch">This is how the agent looks to your customer: real WhatsApp, with service cards, doctor profiles and a booking form that opens inside the chat. Tap a message to send it.</p>
    <div class="wa-asks" aria-label="Messages to send"></div>
    <p class="dim" style="margin-top:20px;font-size:14px">Demo clinic with sample data. Yours is built on your own services, prices and team.</p>
  </div>
  <div class="wa" data-chat>
    <div class="wa-phone lp-frame"><div class="wa-scr lp-screen">
      <img class="lp-head" src="assets/agent/clinic-head.webp" alt="Medicare Health Clinic, verified business account on WhatsApp">
      <div class="wa-body" aria-live="polite"><div class="wa-log"></div></div>
      <div class="wa-barw"><img src="assets/agent/clinic-bar.webp" alt=""><span class="wa-typed"></span><span class="wa-mic" aria-hidden="true"></span></div>
      <div class="wa-sheet" aria-hidden="true" inert><div class="wa-sh"><button type="button" class="x" aria-label="Close">✕</button><b>Book your visit</b></div><div class="wa-sb"></div><div class="wa-sf"><button type="button" class="go">Continue</button><small>Managed by the business. Learn more</small></div></div>
    </div></div>
  </div>
</div></section>
'''
