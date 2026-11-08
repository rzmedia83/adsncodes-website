# ---------- Arabic pages (/ar/) ----------
# Live and indexed (approved by Razal, Nov 2026). Set AR_LIVE to False to noindex them again.
AR_LIVE = True
AR_PAIRS = []
_ae = __import__("html").escape
(R / 'ar').mkdir(exist_ok=True)

AR_CSS = """<style>
html[dir=rtl]{--display:'IBM Plex Sans Arabic','Outfit',system-ui,sans-serif;--body:'IBM Plex Sans Arabic','Outfit',system-ui,sans-serif}
html[dir=rtl] body{font-weight:400;line-height:1.85}
html[dir=rtl] h1,html[dir=rtl] h2,html[dir=rtl] h3,html[dir=rtl] h4,html[dir=rtl] .results b,html[dir=rtl] .drawer>a,html[dir=rtl] .foot h2{letter-spacing:0!important}
html[dir=rtl] .hl{line-height:1.22}
html[dir=rtl] .hl .ln{padding-bottom:.16em;padding-top:.04em}
html[dir=rtl] .qa button{text-align:right}
html[dir=rtl] .wa-fab{right:auto;left:calc(18px + env(safe-area-inset-left,0px))}
html[dir=rtl] .tlink svg{transform:scaleX(-1)}
html[dir=rtl] .tlink:hover svg{transform:scaleX(-1) translateX(4px)}
html[dir=rtl] .facts li{padding:28px 0 28px 28px}
html[dir=rtl] .lab,html[dir=rtl] .tagl{letter-spacing:0;text-transform:none}
html[dir=rtl] .lede{line-height:1.8}
.ar-note{font-size:14px;color:var(--ink-45);margin-top:26px}
.lang-sw{font:500 14px var(--body);text-decoration:none;opacity:.85}
</style>"""

AR_NAV = """<div class="cur" aria-hidden="true"></div>
<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="brand" href="ar/" aria-label="Ads n' Codes"><img src="assets/logo-white-sm.webp" alt="Ads n' Codes" width="320" height="188"></a>
    <nav class="nav-links" aria-label="القائمة الرئيسية">
      <a href="ar/">الرئيسية</a>
      <a href="ar/abu-dhabi.html">أبوظبي</a>
      <a href="case-studies.html">أعمالنا</a>
      <a href="contact.html">تواصل معنا</a>
      <a class="lang-sw" href="{EN}" hreflang="en" lang="en">English</a>
      <a class="btn btn-w mag" href="https://wa.me/971565440310">ابدأ مشروعك</a>
      <button class="menu-btn" id="menuBtn" type="button" aria-expanded="false" aria-controls="drawer">القائمة</button>
    </nav>
  </div>
</header>
<div class="drawer" id="drawer" aria-hidden="true">
  <a href="ar/">الرئيسية</a>
  <a href="ar/abu-dhabi.html">أبوظبي</a>
  <a href="ar/ppc-abu-dhabi.html">إعلانات جوجل</a>
  <a href="ar/seo-abu-dhabi.html">تحسين محركات البحث</a>
  <a href="ar/web-design-abu-dhabi.html">تصميم المواقع</a>
  <a href="ar/app-development-abu-dhabi.html">تطوير التطبيقات</a>
  <a href="{EN}" lang="en">English</a>
  <div class="d-c">
    <span>للمشاريع <a href="mailto:bd@adsncodes.com">bd@adsncodes.com</a></span>
    <span>اتصال أو واتساب <a href="https://wa.me/971565440310" dir="ltr">+971 56 544 0310</a></span>
  </div>
</div>"""

AR_FOOT = """<footer class="foot">
  <canvas class="silk" aria-hidden="true"></canvas>
  <div class="veil" aria-hidden="true"></div>
  <div class="wrap">
    <h2>{FT}</h2>
    <div class="acts">
      <a class="btn btn-w mag" href="https://wa.me/971565440310">راسلنا على واتساب</a>
      <a class="tlink" href="contact.html">أرسل تفاصيل مشروعك <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </div>
    <div class="fcols">
      <div><p class="fh">المشاريع الجديدة</p><span class="v"><a href="mailto:bd@adsncodes.com">bd@adsncodes.com</a></span></div>
      <div><p class="fh">الاستفسارات العامة</p><span class="v"><a href="mailto:hello@adsncodes.com">hello@adsncodes.com</a></span></div>
      <div><p class="fh">اتصال أو واتساب</p><span class="v"><a href="tel:+971565440310" dir="ltr">+971 56 544 0310</a></span><span class="sub"><a href="https://wa.me/971565440310">واتساب</a><a href="tel:+971565440310">اتصال</a></span></div>
      <div><p class="fh">دبي</p><span class="v">بي هايف، الطابق الثالث، برج برجمان للأعمال</span><span class="sub">دبي، الإمارات<a href="https://www.google.com/maps/search/?api=1&amp;query=Ads+n%27+Codes+BurJuman+Dubai&amp;query_place_id=ChIJL8srqlxzh2kRtCTl_DkPRDY">الاتجاهات</a></span></div>
    </div>
    <nav class="fareas" aria-label="صفحات أبوظبي"><span>أبوظبي</span><a href="ar/abu-dhabi.html">وكالة تسويق في أبوظبي</a><a href="ar/ppc-abu-dhabi.html">إعلانات جوجل</a><a href="ar/seo-abu-dhabi.html">تحسين محركات البحث</a><a href="ar/web-design-abu-dhabi.html">تصميم المواقع</a><a href="ar/app-development-abu-dhabi.html">تطوير التطبيقات</a></nav>
    <div class="giant"><img src="assets/logo-white-lg.png" alt="" width="1400" height="823" loading="lazy"></div>
    <div class="foot-bar">
      <span>© Ads n' Codes FZE LLC. وكالة تسويق وتقنية في دبي، نخدم أبوظبي والشارقة وعجمان وجميع إمارات الدولة.</span>
      <nav aria-label="روابط"><a href="ar/">الرئيسية</a><a href="contact.html">تواصل معنا</a><a href="privacy.html" lang="en">Privacy</a></nav>
    </div>
  </div>
</footer>
<a class="wa-fab" href="https://wa.me/971565440310" aria-label="تحدث معنا على واتساب"><svg width="26" height="26" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.6-.3Z"/></svg></a>"""

def ar_page(slug, en, title, desc, ftitle, body, lds=(), region=('AE-DU', 'Dubai')):
    path = 'ar/' if slug == 'index' else f'ar/{slug}.html'
    AR_PAIRS.append((path, en))
    url = DOMAIN + path
    enurl = DOMAIN + ('' if en == 'index' else en + '.html')
    robots = 'index, follow, max-image-preview:large' if AR_LIVE else 'noindex, follow'
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in [ORG] + list(lds))
    head = f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<base href="/">
<title>{_ae(title)}</title>
<meta name="description" content="{_ae(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ar-ae" href="{url}"><link rel="alternate" hreflang="en-ae" href="{enurl}">
<meta name="robots" content="{robots}">
<meta name="geo.region" content="{region[0]}"><meta name="geo.placename" content="{region[1]}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Ads n' Codes"><meta property="og:locale" content="ar_AE">
<meta property="og:title" content="{_ae(title)}"><meta property="og:description" content="{_ae(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{DOMAIN}assets/og.jpg">
<meta name="theme-color" content="#414042">
<link rel="icon" href="assets/mark-white.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600&family=Outfit:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/site.css">
{AR_CSS}
{ld}</head>
<body>
"""
    out = head + AR_NAV.replace('{EN}', ('' if en == 'index' else en + '.html') or './') + '\n<main id="top">\n' + body + '\n</main>\n' + AR_FOOT.replace('{FT}', _ae(ftitle)) + '\n' + SCRIPTS + '\n</body>\n</html>\n'
    (R / path.replace('ar/', 'ar/index.html') if slug == 'index' else R / path).write_text(out)
    return path

def ar_faq(faq):
    return ''.join(f'<div class="qa"><button type="button" aria-expanded="{"true" if i == 0 else "false"}" aria-controls="f{i}" id="fq{i}">{_ae(q)}<span class="pm" aria-hidden="true">+</span></button><div class="ans" id="f{i}" role="region" aria-labelledby="fq{i}"><div><p>{_ae(a)}</p></div></div></div>' for i, (q, a) in enumerate(faq))

def ar_hero(img, alt, crumb, h1, lede, pos='center'):
    pic = PIC(img, f'<img src="{img}" fetchpriority="high" alt="{_ae(alt)}" style="object-position:{pos}">')
    lines = ''.join(f'<span class="ln"><span>{_ae(x)}</span></span>' for x in h1)
    return f"""<section class="phero photo"><div class="ph-img">{pic}</div><div class="veil" aria-hidden="true" style="background:linear-gradient(270deg,rgba(65,64,66,.92),rgba(65,64,66,.5) 60%,rgba(65,64,66,.25)),linear-gradient(180deg,rgba(65,64,66,0) 55%,#414042)"></div>
  <div class="wrap">
    <p class="crumb">{crumb}</p>
    <h1 class="hl">{lines}</h1>
    <p class="lede">{_ae(lede)}</p>
    <div class="acts" style="margin-top:36px"><a class="btn btn-w mag" href="https://wa.me/971565440310">احصل على عرض</a><a class="tlink" href="contact.html">أرسل تفاصيل مشروعك</a></div>
  </div>
</section>"""

def ar_subs(items):
    return '<ul class="subs">' + ''.join(f'<li><h3>{_ae(a)}</h3><p>{_ae(b)}</p></li>' for a, b in items) + '</ul>'

AR_CRUMB_AD = '<a href="ar/">الرئيسية</a> / <a href="ar/abu-dhabi.html">أبوظبي</a> / '

# ---------- service pages for Abu Dhabi ----------
AR_SVC = [
dict(slug='ppc-abu-dhabi', en='ppc-agency-abu-dhabi', img='assets/img/ad-palace.webp', pos='30% center', alt='أفق أبوظبي عند الغروب مع أبراج الاتحاد',
  title="إدارة إعلانات جوجل في أبوظبي | Ads n' Codes",
  desc="إدارة حملات جوجل والإعلانات المدفوعة في أبوظبي والعين: إعلانات البحث وبيرفورمانس ماكس ويوتيوب بالعربية والإنجليزية، مع تتبع كل مكالمة ومحادثة واتساب.",
  short='إعلانات جوجل', h1=['إدارة إعلانات جوجل', 'في أبوظبي'],
  lede="حملات جوجل مصممة لطريقة البحث في أبوظبي: ميزانيات منفصلة للجزيرة والبر الرئيسي والعين، وإعلانات بالعربية والإنجليزية، وتتبع كل عميل محتمل حتى المكالمة أو محادثة واتساب أو الحجز.",
  intro_h="البحث في أبوظبي يختلف عن دبي.",
  intro=["حجم البحث في العاصمة أصغر، والعميل يقارن لفترة أطول، لذلك تهدر الحملات العامة المنسوخة من دبي الميزانية بسرعة. عيادة في مدينة خليفة، ومقاول في مصفح، وفندق في جزيرة ياس، يحتاج كل منهم إلى كلمات مفتاحية وإعلانات ومناطق خاصة به، والعين تحتاج إلى حملة مستقلة تماماً.",
         "نبدأ بإعداد تتبع التحويلات، ثم نبني حملات دقيقة حسب الخدمة والمنطقة، مع إعلانات عربية حيث يبحث عملاؤك بالعربية. كل أسبوع نراجع عبارات البحث ونوقف النقرات التي لا تتحول إلى عملاء. حساب إعلانات جوجل باسمك، وترى كل درهم يُصرف."],
  subs_h='خدمات الإعلانات المدفوعة في أبوظبي',
  subs=[('إعلانات بحث جوجل حسب المنطقة','حملات مقسمة بين جزيرة أبوظبي والريم وياس والسعديات ومدينة خليفة ومدينة محمد بن زايد والعين، لتتبع الميزانية الطلب الفعلي.'),
        ('إعلانات بالعربية والإنجليزية','إعلانات وكلمات مفتاحية مكتوبة أصلاً باللغتين وليست مترجمة، لأن كثيراً من العملاء في أبوظبي يبحثون بالعربية أولاً.'),
        ('بيرفورمانس ماكس','البحث والخرائط ويوتيوب والشبكة الإعلانية في حملة واحدة، تتغذى على بيانات تحويل حقيقية من عملائك في أبوظبي.'),
        ('حملات للشركات والجهات','حملات بحث ولينكدإن للشركات التي تبيع للمؤسسات والشركات في المناطق الحرة والجهات شبه الحكومية في أبوظبي.'),
        ('مراجعة حساب جوجل الحالي','مراجعة كاملة للحساب: الإنفاق المهدر، والتتبع المعطل، والمواقع الخاطئة، والإصلاحات السريعة التي تخفض تكلفة العميل المحتمل.'),
        ('تتبع التحويلات','إعداد GA4 وتتبع المكالمات ونقرات واتساب، ليتعلم جوجل من الاستفسارات الحقيقية لا من زيارات الصفحات.')],
  process=[('المراجعة','ندرس سوقك في أبوظبي ومنافسيك وحملاتك السابقة، ونجهز التتبع قبل صرف أي مبلغ.'),('البناء','حملات حسب المنطقة واللغة، مع الكلمات المفتاحية والكلمات السلبية والإعلانات وصفحات الهبوط، وكلها بموافقتك قبل الإطلاق.'),('التحسين','مراجعة أسبوعية لعبارات البحث، وتعديل العروض والميزانيات بين المناطق، واختبار إعلانات جديدة.'),('التقرير','تقرير شهري بعدد العملاء المحتملين وتكلفة كل عميل والمبيعات لكل منطقة، مع خطة الشهر التالي.')],
  faq=[("هل تديرون إعلانات جوجل لشركات في أبوظبي؟","نعم. ندير حملات الإعلانات المدفوعة لشركات في أبوظبي والعين. تتم الاجتماعات والتقارير عبر الإنترنت، ونلتقي بك في أبوظبي عندما يكون ذلك مفيداً."),
       ("هل يجب فصل حملات أبوظبي عن العين؟","غالباً نعم. للعين عادات بحث ومنافسون وتكاليف مختلفة، والحملة المشتركة تصرف معظم الميزانية على الجزيرة. الحملات المنفصلة تبقي الاثنتين تحت السيطرة."),
       ("هل نحتاج إلى إعلانات عربية في أبوظبي؟","لمعظم الشركات التي تخدم الأفراد أو الجهات الحكومية، نعم. جزء كبير من البحث في أبوظبي يتم بالعربية، وغالباً ما تكون المنافسة على الإعلانات العربية أقل."),
       ("هل الحساب الإعلاني ملك لنا؟","نعم. الحساب باسمك ويبقى لك، ونعمل داخله بصلاحيات يمكنك إلغاؤها في أي وقت.")],
  related=[('seo-abu-dhabi','تحسين محركات البحث في أبوظبي'),('web-design-abu-dhabi','تصميم المواقع في أبوظبي')]),

dict(slug='seo-abu-dhabi', en='seo-agency-abu-dhabi', img='assets/img/ad-corniche.webp', pos='center', alt='أفق أبوظبي ليلاً من الكورنيش',
  title="شركة SEO وتحسين محركات البحث في أبوظبي | Ads n' Codes",
  desc="شركة تحسين محركات البحث في أبوظبي: SEO محلي، ونشاطك التجاري على جوجل، وصفحات عربية وإنجليزية، وإصلاحات تقنية ومحتوى يتصدر نتائج البحث في العاصمة.",
  short='تحسين محركات البحث', h1=['شركة تحسين محركات البحث', 'في أبوظبي'],
  lede="تحسين محلي لمحركات البحث، وملف نشاطك التجاري على جوجل، ومحتوى باللغتين، لتظهر شركتك أمام من يبحث عنها في أبوظبي، من الجزيرة حتى العين.",
  intro_h="الظهور في أبوظبي يبدأ محلياً.",
  intro=["معظم عمليات البحث بنية الشراء في أبوظبي محلية: خدمة قرب مدينة خليفة، أو عيادة في الريم، أو مورد في مصفح. يجيب جوجل عنها بالخريطة وبالصفحات التي توضح بوضوح أين تعمل. وما زالت شركات كثيرة في العاصمة تملك صفحة عامة واحدة وملفاً غير مُدار على جوجل، فتبقى المراكز الأولى متاحة.",
         "نصلح الأساسيات التقنية، ونبني صفحات للخدمات والمناطق التي تخدمها فعلاً بالعربية والإنجليزية، ونضبط ملف نشاطك التجاري على جوجل، ونكسب لك إشارات من مصادر يثق بها جوجل في الإمارات. ثم نرسل لك كل شهر الترتيب والمكالمات والاستفسارات القادمة من البحث."],
  subs_h='خدمات تحسين محركات البحث في أبوظبي',
  subs=[('SEO محلي وملف جوجل التجاري','إعداد الملف والفئات والصور والمنشورات والتقييمات، لتظهر في نتائج الخريطة في أبوظبي.'),
        ('صفحات للمناطق والخدمات','صفحة لكل خدمة ومنطقة تغطيها، من جزيرة أبوظبي حتى العين، مكتوبة للناس أولاً.'),
        ('SEO باللغة العربية','صفحات وكلمات مفتاحية عربية مبنية على بحث فعلي بالعربية، لتظهر في عمليات البحث التي لا يصل إليها موقعك الإنجليزي.'),
        ('SEO تقني','السرعة والفهرسة والبنية والبيانات المنظمة، ليقرأ جوجل كل صفحة ويثق بها.'),
        ('محتوى يتصدر البحث','مقالات وأدلة تجيب عن الأسئلة التي يطرحها العملاء في أبوظبي قبل الشراء.'),
        ('الظهور في بحث الذكاء الاصطناعي','إجابات واضحة ومنظمة تساعد ChatGPT وGemini ونتائج جوجل الذكية على ذكر شركتك.')],
  process=[('المراجعة','مراجعة تقنية وتحليل للمنافسين ولعمليات البحث المهمة لك في أبوظبي.'),('الإصلاح','نصلح السرعة والفهرسة والبنية وملف جوجل التجاري أولاً.'),('البناء','صفحات خدمات ومناطق باللغتين، ومحتوى وروابط تضاف كل شهر.'),('التقرير','الترتيب والمكالمات والاستفسارات من البحث، مع خطة الشهر التالي.')],
  faq=[("كم يستغرق تحسين محركات البحث في أبوظبي؟","تلاحظ معظم الشركات تحسناً في نتائج الخريطة خلال شهر إلى ثلاثة أشهر، وترتيباً أقوى في عمليات البحث التنافسية خلال أربعة إلى ستة أشهر، بحسب موقعك ومنافسيك وحجم المحتوى."),
       ("هل نحتاج إلى صفحات عربية؟","إذا كان عملاؤك يبحثون بالعربية، نعم. للبحث العربي كلمات ومنافسون مختلفون عن البحث الإنجليزي، والموقع الإنجليزي وحده يفوّت جزءاً من السوق."),
       ("هل يمكنكم تحسين ظهورنا في العين أيضاً؟","نعم. تحصل العين على صفحات وعمل خاص على ملف جوجل، لأن جوجل يعاملها مدينة مستقلة بنتائج خاصة بها."),
       ("هل تضمنون المركز الأول في جوجل؟","لا. لا أحد يتحكم في ترتيب جوجل، ومن يضمن مركزاً معيناً يخمّن. نلتزم بالعمل والتقارير والتقدم المستمر في عمليات البحث التي تجلب لك العملاء.")],
  related=[('ppc-abu-dhabi','إعلانات جوجل في أبوظبي'),('web-design-abu-dhabi','تصميم المواقع في أبوظبي')]),

dict(slug='web-design-abu-dhabi', en='web-design-abu-dhabi', img='assets/img/ad-louvre.webp', pos='55% center', alt='قبة متحف اللوفر أبوظبي في جزيرة السعديات',
  title="شركة تصميم وتطوير مواقع في أبوظبي | Ads n' Codes",
  desc="تصميم وتطوير المواقع في أبوظبي: مواقع شركات ثنائية اللغة، ومتاجر إلكترونية، ومواقع حجز سريعة، مبنية لتتصدر البحث وتحول الزيارات إلى استفسارات.",
  short='تصميم المواقع', h1=['تصميم وتطوير المواقع', 'في أبوظبي'],
  lede="مواقع شركات ومتاجر إلكترونية ومواقع حجز للشركات في أبوظبي، مصممة بالعربية والإنجليزية، سريعة على أي هاتف، ومبنية لتجلب الاستفسارات.",
  intro_h="في العاصمة، موقعك هو اجتماعك الأول.",
  intro=["العملاء في أبوظبي، من العائلات إلى فرق المشتريات، يتفقدون موقع الشركة قبل الاتصال. الموقع البطيء، أو النسخة العربية المعطلة، أو الصفحة التي تبدو غير مكتملة، تكلفك الاجتماع قبل أن يحدث. ويزداد ذلك أهمية عندما تبيع للشركات أو للجهات الحكومية التي تقارن الموردين بعناية.",
         "نصمم ونبني مواقع تبدو راسخة، وتفتح بسرعة، وتعمل بشكل صحيح باللغتين، مع تصميم عربي من اليمين إلى اليسار مبني بعناية لا مجرد نسخة معكوسة. كل موقع مهيأ لمحركات البحث من اليوم الأول، مع صفحات خدمات واضحة، وأزرار واتساب واتصال، وتتبع يوضح مصدر كل استفسار."],
  subs_h='خدمات تصميم المواقع في أبوظبي',
  subs=[('مواقع الشركات','مواقع للشركات والخدمات تشرح ما تقدمه بوضوح وتسهّل التواصل.'),
        ('مواقع ثنائية اللغة','تصميم عربي صحيح من اليمين إلى اليسار، ومحتوى مكتوب للقارئ العربي لا مترجم آلياً.'),
        ('المتاجر الإلكترونية','متاجر مع بوابات دفع إماراتية وخيارات توصيل وصفحات منتجات تبيع.'),
        ('مواقع الحجز والاستفسارات','مواقع للعيادات والفنادق والمدارس والخدمات، مع نماذج حجز وواتساب مربوطة بفريقك.'),
        ('إعادة تصميم الموقع','نسخة أسرع وأوضح من موقعك الحالي تحافظ على ترتيبك في جوجل.'),
        ('الاستضافة والصيانة','التحديثات والنسخ الاحتياطية والحماية والتعديلات الصغيرة كل شهر.')],
  process=[('الموجز','نفهم نشاطك وعملاءك والصفحات التي تحتاجها، ونتفق على النطاق والجدول الزمني.'),('التصميم','تصاميم بالعربية والإنجليزية للكمبيوتر والهاتف، بموافقتك قبل البناء.'),('البناء','موقع سريع مع النماذج وواتساب والتتبع وأساسيات SEO.'),('الإطلاق والمتابعة','اختبار على أجهزة حقيقية، ثم الإطلاق، ثم صيانة وتحسينات شهرية.')],
  faq=[("كم يستغرق بناء الموقع؟","يستغرق موقع الشركة عادة من ثلاثة إلى ستة أسابيع من الموجز حتى الإطلاق. المتاجر والمواقع ذات الحجوزات أو المزايا الخاصة تحتاج وقتاً أطول، ونتفق على الجدول قبل البدء."),
       ("هل تبنون مواقع باللغة العربية؟","نعم. نبني مواقع ثنائية اللغة بتصميم صحيح من اليمين إلى اليسار وخطوط عربية ومحتوى مكتوب للقارئ العربي."),
       ("هل يمكن إعادة تصميم موقعنا دون خسارة ترتيبنا في جوجل؟","نعم. نرسم خريطة لصفحاتك الحالية، ونحافظ على كل رابط له ترتيب أو نعيد توجيهه، ونتحقق من الفهرسة بعد الإطلاق."),
       ("هل تعملون مع شركات أبوظبي من دبي؟","نعم. مكتبنا في دبي في بي هايف، برجمان. يمكن عقد ورش العمل والمراجعات في أبوظبي، ويتم الباقي عبر الإنترنت.")],
  related=[('app-development-abu-dhabi','تطوير التطبيقات في أبوظبي'),('seo-abu-dhabi','تحسين محركات البحث في أبوظبي')]),

dict(slug='app-development-abu-dhabi', en='app-development-abu-dhabi', img='assets/img/ad-marina.webp', pos='center', alt='برج على واجهة أبوظبي البحرية عند الغروب',
  title="شركة تطوير تطبيقات الجوال في أبوظبي | Ads n' Codes",
  desc="تطوير تطبيقات الجوال في أبوظبي: تطبيقات آيفون وأندرويد، وتطبيقات ويب، وأنظمة أعمال بالعربية والإنجليزية، مصممة ومبنية حول طريقة عملك.",
  short='تطوير التطبيقات', h1=['تطوير تطبيقات الجوال', 'في أبوظبي'],
  lede="تطبيقات آيفون وأندرويد وتطبيقات ويب وأنظمة داخلية لشركات أبوظبي، بالعربية والإنجليزية، مبنية ليستخدمها الناس كل يوم لا لتُحمّل مرة واحدة.",
  intro_h="معظم التطبيقات تفشل في الاستخدام، لا في البرمجة.",
  intro=["التطبيق لا يحقق عائداً إلا إذا استمر العملاء أو الموظفون في استخدامه. لذلك نبدأ من المهمة التي يؤديها: حجز خدمة، أو إعادة طلب منتج، أو تسجيل زيارة موقع في مصفح، أو الموافقة على طلب أثناء التنقل. نرسم هذه المهمة أولاً، ثم نصمم أقصر طريق لإنجازها باللغتين.",
         "نبني تطبيقات لآيفون وأندرويد، وتطبيقات ويب ولوحات تحكم، مربوطة بالأدوات التي تستخدمها، من بوابات الدفع إلى نظام إدارة العملاء. الكود وحسابات المتاجر ملكك، ونبقى معك بعد الإطلاق للإصلاح والتحديث والتطوير."],
  subs_h='خدمات تطوير التطبيقات في أبوظبي',
  subs=[('تطبيقات آيفون وأندرويد','تطبيقات للعملاء على المنصتين بأداء سلس وإحساس أصلي.'),
        ('تطبيقات الويب والبوابات','بوابات عملاء وأنظمة حجز ولوحات تحكم تعمل في أي متصفح.'),
        ('تطبيقات الأعمال الداخلية','أدوات للفرق الميدانية والموافقات والتفتيش والمخزون، مبنية حول طريقة عملك.'),
        ('واجهات عربية وإنجليزية','تصميم من اليمين إلى اليسار ومحتوى ثنائي اللغة من البداية.'),
        ('الدفع والربط','بوابات الدفع الإماراتية والخرائط وأنظمة العملاء وواتساب وأنظمتك الحالية.'),
        ('الدعم والتحديثات','إصلاح الأخطاء وتحديثات أنظمة التشغيل ومزايا جديدة بعد الإطلاق.')],
  process=[('الاكتشاف','نحدد المستخدمين والمهام والأنظمة المرتبطة، ثم نتفق على النطاق.'),('النموذج الأولي','تصميم تفاعلي بالعربية والإنجليزية يُختبر قبل بدء البرمجة.'),('البناء','تطوير على مراحل قصيرة مع نسخة تعمل تجربها كل أسبوعين.'),('الإطلاق والنمو','النشر على المتاجر، ثم التحديث والتحسين بناءً على الاستخدام الفعلي.')],
  faq=[("كم يستغرق بناء التطبيق؟","تستغرق النسخة الأولى المركزة عادة من شهرين إلى أربعة أشهر. التطبيقات الأكبر ذات الربط الكثير تحتاج وقتاً أطول، ونتفق على نطاق يضع نسخة مفيدة في أيدي المستخدمين مبكراً."),
       ("هل تبنون لآيفون وأندرويد معاً؟","نعم. تحتاج معظم الشركات في أبوظبي إلى المنصتين، لذلك نبني عادة كوداً واحداً يعمل جيداً على الاثنين، ونلجأ إلى التطوير الأصلي الكامل عندما يحتاجه التطبيق."),
       ("هل يمكن أن يكون التطبيق بالعربية والإنجليزية؟","نعم. نصمم اللغتين من البداية، بما في ذلك التصميم من اليمين إلى اليسار."),
       ("من يملك التطبيق والكود؟","أنت. الكود والتصاميم وحسابات App Store وGoogle Play باسمك.")],
  related=[('web-design-abu-dhabi','تصميم المواقع في أبوظبي'),('ppc-abu-dhabi','إعلانات جوجل في أبوظبي')]),
]

def ar_service(s):
    steps = ''.join(f'<li><h3>{i}. {_ae(a)}</h3><p>{_ae(b)}</p></li>' for i, (a, b) in enumerate(s['process'], 1))
    rel = ''.join(f'<a href="ar/{u}.html">{_ae(n)}</a>' for u, n in s['related']) + '<a href="ar/abu-dhabi.html">كل خدماتنا في أبوظبي</a>'
    body = ar_hero(s['img'], s['alt'], AR_CRUMB_AD + _ae(s['short']), s['h1'], s['lede'], s['pos']) + f"""
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">نظرة عامة</span><div><h2 class="mid" style="max-width:18ch">{_ae(s['intro_h'])}</h2><div class="two" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:24px 4vw;margin-top:30px"><p class="lede">{_ae(s['intro'][0])}</p><p class="dim">{_ae(s['intro'][1])}</p></div></div></div>
</div></section>
<section class="sec light" style="padding-top:0"><div class="wrap">
  <div class="row-head"><span class="lab">ما نقدمه</span><h2 class="big" style="max-width:16ch">{_ae(s['subs_h'])}</h2></div>
  {ar_subs(s['subs'])}
</div></section>
<section class="sec stone"><div class="wrap">
  <div class="row-head"><span class="lab">طريقة العمل</span><div><h2 class="mid" style="max-width:20ch">كيف نعمل معك</h2><ol class="subs how-steps">{steps}</ol></div></div>
</div></section>
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">أسئلة شائعة</span><div class="faq faq-list">{ar_faq(s['faq'])}</div></div>
  <div class="row-head" style="margin:56px 0 0"><span class="lab">خدمات ذات صلة</span><nav class="related" aria-label="خدمات ذات صلة">{rel}</nav></div>
</div></section>"""
    url = DOMAIN + 'ar/' + s['slug'] + '.html'
    svc = {"@context": "https://schema.org", "@type": "Service", "name": s['h1'][0] + ' ' + s['h1'][1], "provider": {"@id": DOMAIN + "#org"}, "areaServed": {"@type": "City", "name": "Abu Dhabi"}, "url": url, "description": s['desc'], "inLanguage": "ar-AE"}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "الرئيسية", "item": DOMAIN + 'ar/'}, {"@type": "ListItem", "position": 2, "name": "أبوظبي", "item": DOMAIN + 'ar/abu-dhabi.html'}, {"@type": "ListItem", "position": 3, "name": s['short'], "item": url}]}
    return ar_page(s['slug'], s['en'], s['title'], s['desc'], 'هل أنت جاهز للنمو في أبوظبي؟ لنتحدث.', body, [svc, faq_ld(s['faq']), crumbs], ('AE-AZ', 'Abu Dhabi'))

# ---------- Abu Dhabi hub ----------
def ar_abu_dhabi():
    focus = [('التواصل الاجتماعي والإعلانات المدفوعة','حملات ميتا وجوجل وتيك توك ولينكدإن موجهة لمناطق أبوظبي والعين، مع إدارة كاملة لحساباتك على إنستغرام وفيسبوك وتيك توك.'),
             ('تحسين محركات البحث في أبوظبي','صفحات للمناطق، وملف نشاطك التجاري على جوجل، وSEO محلي لعمليات البحث القريبة منك.'),
             ('الهوية التجارية والموقع','هوية تجارية ومواقع سريعة ثنائية اللغة تليق بعميل يدقق قبل أن يقرر.'),
             ('الرد على كل استفسار','وكيل واتساب بالذكاء الاصطناعي يرد على كل رسالة خلال ثوانٍ، ليلاً ونهاراً، ويحجز الخطوة التالية.')]
    cards = [('ar/ppc-abu-dhabi.html','assets/img/ad-palace.webp','إعلانات جوجل','حملات بحث ويوتيوب بالعربية والإنجليزية، لكل منطقة ميزانيتها.'),
             ('ar/seo-abu-dhabi.html','assets/img/ad-corniche.webp','تحسين محركات البحث','SEO محلي وصفحات عربية وملف جوجل التجاري.'),
             ('ar/web-design-abu-dhabi.html','assets/img/ad-louvre.webp','تصميم المواقع','مواقع شركات ومتاجر ثنائية اللغة وسريعة.'),
             ('ar/app-development-abu-dhabi.html','assets/img/ad-marina.webp','تطوير التطبيقات','تطبيقات آيفون وأندرويد وأنظمة أعمال.')]
    groups = ''.join(f'<a class="group" href="{u}"><div class="media"><img src="{i.replace(".webp", "-p.webp")}" alt="" loading="lazy" style="object-position:center 40%"></div><h2>{_ae(t)}</h2><p>{_ae(d)}</p></a>' for u, i, t, d in cards)
    faq = [("هل لديكم مكتب في أبوظبي؟","مكتبنا في دبي في بي هايف، برجمان. تتم الاجتماعات والتقارير عبر الإنترنت، ونأتي إليك في أبوظبي للتصوير وورش العمل والاجتماعات المهمة."),
           ("هل تعملون كوكالة إعلانات أم وكالة تسويق رقمي؟","الاثنان معاً. نخطط الحملات وننتج المحتوى من تصوير وفيديو وتصاميم، وندير الإعلانات على ميتا وجوجل وتيك توك، ونبني المواقع وأنظمة واتساب التي تحوّل الاهتمام إلى عملاء."),
           ("هل تديرون حملات للعملاء المحتملين في أبوظبي؟","نعم. ندير حملات ميتا وجوجل موجهة لأبوظبي والعين، مع صفحات هبوط ومتابعة فورية على واتساب."),
           ("هل يمكن استهداف العين بشكل منفصل؟","نعم. تختلف العين كثيراً عن جزيرة أبوظبي، لذلك نخصص لها حملات ومحتوى وميزانية مستقلة."),
           ("متى يمكن أن تبدأ الحملة؟","عادة خلال أسبوع إلى أسبوعين من التوقيع، بعد تجهيز الموجز والمواد والحسابات الإعلانية.")]
    body = ar_hero('assets/img/abudhabi.webp', 'جامع الشيخ زايد الكبير في أبوظبي', '<a href="ar/">الرئيسية</a> / أبوظبي', ['وكالة إعلان وتسويق', 'في أبوظبي'],
                   'إدارة التواصل الاجتماعي، والإعلانات المدفوعة، وتحسين محركات البحث، والهوية التجارية، والمحتوى والمواقع للشركات في أبوظبي والعين.') + f"""
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">أبوظبي</span><div><h2 class="mid" style="max-width:18ch">تسويق لعاصمة تشتري بثقة.</h2><div class="two" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:24px 4vw;margin-top:30px"><p class="lede">العملاء في أبوظبي يأخذون وقتاً أطول في القرار، ويتوقعون أن تبدو العلامة التجارية راسخة قبل التواصل معها. وهذا يغيّر طريقة العمل: حضور أقوى للعلامة، وأدلة أكثر، ومواقع أوضح، ومتابعة لا تترك العميل المحتمل يفقد اهتمامه.</p><p class="dim">نوجه الحملات إلى جزيرة أبوظبي وياس والسعديات ومدينة خليفة ومدينة محمد بن زايد والعين كلاً على حدة، لتذهب ميزانيتك إلى المناطق التي يعيش ويعمل فيها عملاؤك. ونرتب التصوير في موقعه داخل أبوظبي.</p></div></div></div>
</div></section>
<section class="sec light" style="padding-top:0"><div class="wrap">
  <div class="row-head"><span class="lab">ما نقدمه</span><h2 class="big" style="max-width:16ch">ما نقدمه لشركات أبوظبي</h2></div>
  {ar_subs(focus)}
  <p class="dim" style="margin-top:36px;max-width:60ch">القطاعات التي نعمل معها: العقارات، والعيادات والرعاية الصحية، والضيافة، والمطاعم، والتعليم، والشركات والخدمات المهنية.</p>
</div></section>
<section class="sec stone"><div class="wrap">
  <div class="row-head"><span class="lab">خدمات متخصصة</span><h2 class="mid" style="max-width:20ch">خدماتنا المتخصصة في أبوظبي</h2></div>
  <div class="groups" style="margin-top:40px">{groups}</div>
</div></section>
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">أسئلة شائعة</span><div class="faq faq-list">{ar_faq(faq)}</div></div>
</div></section>"""
    url = DOMAIN + 'ar/abu-dhabi.html'
    svc = {"@context": "https://schema.org", "@type": "Service", "name": "وكالة إعلان وتسويق في أبوظبي", "provider": {"@id": DOMAIN + "#org"}, "areaServed": {"@type": "City", "name": "Abu Dhabi"}, "url": url, "inLanguage": "ar-AE"}
    return ar_page('abu-dhabi', 'digital-marketing-agency-abu-dhabi', "وكالة إعلان وتسويق في أبوظبي | Ads n' Codes",
                   "وكالة إعلان وتسويق رقمي لأبوظبي والعين: إدارة التواصل الاجتماعي، وإعلانات ميتا وجوجل، وتحسين محركات البحث، والهوية التجارية، والفيديو، والمواقع، وواتساب بالذكاء الاصطناعي.",
                   'هل تريد أن تنمو في أبوظبي؟ لنتحدث.', body, [svc, faq_ld(faq)], ('AE-AZ', 'Abu Dhabi'))

# ---------- Arabic homepage ----------
def ar_home():
    svc = [('social-media-agency-dubai.html','assets/img/social-card.webp','التسويق الرقمي','إدارة التواصل الاجتماعي وإعلانات ميتا وجوجل وتيك توك وسناب شات، بخطة واحدة وتقرير شهري واضح.'),
           ('ppc-google-ads-agency-dubai.html','assets/img/ppc-card.webp','إعلانات جوجل','حملات البحث وبيرفورمانس ماكس ويوتيوب، مع تتبع كل مكالمة ومحادثة واتساب.'),
           ('seo-agency-dubai.html','assets/img/seo-card.webp','تحسين محركات البحث','SEO محلي وتقني ومحتوى يجعل عملاءك يجدونك على جوجل وفي بحث الذكاء الاصطناعي.'),
           ('branding-agency-dubai.html','assets/work/orula-billboard.webp','الهوية التجارية','هوية بصرية وتغليف ورسائل تجعل علامتك تبدو بالمستوى الذي تستحقه.'),
           ('video-production-dubai.html','assets/video/reel-poster.jpg','التصوير والفيديو','تصوير المنتجات والفعاليات والأفلام الإعلانية والريلز، من الفكرة حتى المونتاج.'),
           ('web-development-dubai.html','assets/work/app-ui-2.webp','المواقع والتطبيقات','مواقع سريعة ومتاجر إلكترونية وتطبيقات بالعربية والإنجليزية.')]
    import os
    svc = [(u, i if os.path.exists(R / i) else 'assets/img/dm-card.webp', t, d) for u, i, t, d in svc]
    groups = ''.join(f'<a class="group" href="{u}"><div class="media"><img src="{i}" alt="" loading="lazy"></div><h2>{_ae(t)}</h2><p>{_ae(d)}</p></a>' for u, i, t, d in svc)
    results = [('3,735','عميلاً محتملاً مؤهلاً خلال ثلاثة أشهر من إعلانات ميتا، بمعدل تحويل 13.86%','معهد تدريب'),
               ('1,696','عميلاً محتملاً وأكثر من 70 تسجيلاً عالي القيمة خلال ثلاثة أشهر من إعلانات ميتا','معهد تعليم إبداعي'),
               ('+1M','مشاهدة على إنستغرام وأكثر من 40 ألف إعجاب لخمسة فيديوهات خلال شهرين','معهد تدريب، محتوى غير مدفوع'),
               ('834','تحويلاً من 8,100 نقرة على إعلانات جوجل','أكاديمية مهارات رقمية')]
    res = ''.join(f'<li><b dir="ltr">{a}</b><span>{_ae(b)}</span><em>{_ae(c)}</em></li>' for a, b, c in results)
    facts = [('شركة مرخصة في الإمارات','Ads n\' Codes FZE LLC، ومكتبنا في دبي في بي هايف، الطابق الثالث، برجمان.'),
             ('النطاق والسعر مكتوبان','تحصل على خطة مكتوبة بالمخرجات والجدول الزمني والتكلفة قبل بدء أي عمل.'),
             ('حساباتك تبقى لك','الحسابات الإعلانية والصفحات والنطاقات والملفات باسمك. نحن نعمل عليها وأنت تملكها.'),
             ('تقارير من بيانات حقيقية','تقارير شهرية من حساباتك الإعلانية والتحليلات، بما نجح وما سنغيّره.'),
             ('فريق واحد وجهة تواصل واحدة','الاستراتيجية والمحتوى والإعلانات والتقنية تُدار معاً، مع شخص واحد مسؤول عن حسابك.'),
             ('ردود سريعة','نرد على الرسائل في يوم العمل نفسه عبر واتساب أو الهاتف أو البريد.')]
    fl = ''.join(f'<li><h3>{_ae(a)}</h3><p>{_ae(b)}</p></li>' for a, b in facts)
    faq = [("ما الذي تقدمه Ads n' Codes؟","نحن وكالة تسويق وتقنية في دبي. نقدم إدارة التواصل الاجتماعي، وإعلانات ميتا وجوجل، وتحسين محركات البحث، والهوية التجارية، والتصوير والفيديو، والمواقع والتطبيقات، ووكلاء واتساب بالذكاء الاصطناعي، لشركات في جميع إمارات الدولة."),
           ("هل تعملون مع شركات خارج دبي؟","نعم. نعمل مع شركات في أبوظبي والشارقة وعجمان وباقي الإمارات. الاجتماعات والتقارير عبر الإنترنت، والتصوير وورش العمل في موقعك."),
           ("ما هو وكيل واتساب بالذكاء الاصطناعي؟","هو مساعد على رقم واتساب الخاص بشركتك يفهم ما يكتبه العميل بالعربية أو الإنجليزية، ويجيب عن الأسعار والمواعيد والخدمات، ويحجز الموعد أو يأخذ الطلب، ثم يحوّل المحادثة إلى فريقك عند الحاجة."),
           ("هل نملك الحسابات الإعلانية والموقع؟","نعم. كل الحسابات والنطاقات والملفات باسمك، ونعمل عليها بصلاحيات يمكنك إلغاؤها في أي وقت.")]
    body = f"""<section class="phero">
  <canvas class="silk" aria-hidden="true"></canvas><div class="veil" aria-hidden="true"></div>
  <div class="wrap">
    <p class="crumb">Ads n' Codes · دبي، الإمارات</p>
    <h1 class="hl"><span class="ln"><span>وكالة تسويق وتقنية</span></span><span class="ln"><span>في دبي والإمارات</span></span></h1>
    <p class="lede">نساعد الشركات في الإمارات على النمو: محتوى يلفت الانتباه، وإعلانات تجلب عملاء حقيقيين، ومواقع وتطبيقات سريعة، ووكلاء واتساب بالذكاء الاصطناعي يردون على كل استفسار خلال ثوانٍ.</p>
    <div class="acts" style="margin-top:36px"><a class="btn btn-w mag" href="https://wa.me/971565440310">احصل على عرض</a><a class="tlink" href="case-studies.html">شاهد أعمالنا</a></div>
  </div>
</section>
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">الخدمات</span><div><h2 class="big" style="max-width:16ch">كل ما تحتاجه للنمو، من فريق واحد</h2><p class="ar-note">صفحات الخدمات التفصيلية متاحة حالياً باللغة الإنجليزية.</p></div></div>
  <div class="groups" style="margin-top:48px">{groups}</div>
</div></section>
<section class="sec stone"><div class="wrap">
  <div class="row-head"><span class="lab">واتساب بالذكاء الاصطناعي</span><div><h2 class="mid" style="max-width:18ch">استفسارات أكثر مما تستطيع الرد عليه؟</h2>
  <p class="lede dim" style="margin-top:24px">نحن نضمن أن يحصل كل استفسار على رد. تصلك الرسائل من خرائط جوجل وإنستغرام والتوصيات والعملاء الدائمين والإعلانات، وغالباً وأنت مشغول بإدارة عملك. وكلاء واتساب لدينا يردون خلال ثوانٍ، بالعربية والإنجليزية، ويفهمون طلب العميل ويحجزون الخطوة التالية، للعقارات والعيادات والمطاعم والتجزئة وغيرها.</p>
  <p style="margin-top:24px"><a class="tlink" href="whatsapp-ai-agent-uae.html">اعرف المزيد (بالإنجليزية)</a></p></div></div>
</div></section>
<section class="sec" id="results"><div class="wrap">
  <div class="row-head"><span class="lab">النتائج</span><div><h2 class="big" style="max-width:14ch">أرقام من حملات أدرناها</h2><p class="lede dim" style="margin-top:22px">من حسابات إعلانية وتحليلات حقيقية. أسماء العملاء محفوظة.</p></div></div>
  <ul class="results">{res}</ul>
  <p style="margin-top:36px"><a class="tlink" href="case-studies.html" style="color:var(--paper)">اقرأ دراسات الحالة (بالإنجليزية)</a></p>
</div></section>
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">أبوظبي</span><div><h2 class="mid" style="max-width:20ch">نعمل في أبوظبي أيضاً</h2><p class="lede dim" style="margin-top:20px">حملات ومحتوى ومواقع مصممة لعملاء العاصمة والعين.</p>
  <nav class="related" aria-label="أبوظبي" style="margin-top:28px"><a href="ar/abu-dhabi.html">وكالة تسويق في أبوظبي</a><a href="ar/ppc-abu-dhabi.html">إعلانات جوجل</a><a href="ar/seo-abu-dhabi.html">تحسين محركات البحث</a><a href="ar/web-design-abu-dhabi.html">تصميم المواقع</a><a href="ar/app-development-abu-dhabi.html">تطوير التطبيقات</a></nav></div></div>
</div></section>
<section class="sec stone"><div class="wrap">
  <div class="row-head"><span class="lab">العمل معنا</span><h2 class="big" style="max-width:15ch">ما يمكنك الاعتماد عليه</h2></div>
  <ul class="facts">{fl}</ul>
</div></section>
<section class="sec light"><div class="wrap">
  <div class="row-head"><span class="lab">أسئلة شائعة</span><div class="faq faq-list">{ar_faq(faq)}</div></div>
</div></section>"""
    site = {"@context": "https://schema.org", "@type": "WebPage", "name": "Ads n' Codes | وكالة تسويق وتقنية في دبي", "url": DOMAIN + 'ar/', "inLanguage": "ar-AE", "publisher": {"@id": DOMAIN + "#org"}}
    return ar_page('index', 'index', "Ads n' Codes | وكالة تسويق وتقنية في دبي والإمارات",
                   "وكالة تسويق رقمي وتقنية في دبي: إدارة التواصل الاجتماعي، وإعلانات ميتا وجوجل، وتحسين محركات البحث، والهوية التجارية، والتصوير، والمواقع، ووكلاء واتساب بالذكاء الاصطناعي.",
                   'ما الذي يبطئ نمو شركتك؟ لنتحدث.', body, [site, faq_ld(faq)])

AR_BUILT = [ar_home(), ar_abu_dhabi()] + [ar_service(s) for s in AR_SVC]

# hreflang from the English pages to their Arabic versions
if AR_LIVE:
    for _arp, _en in AR_PAIRS:
        _f = R / (_en + '.html')
        if not _f.exists(): continue
        _s = _f.read_text()
        _tag = f'<link rel="alternate" hreflang="ar-ae" href="{DOMAIN + _arp}">'
        if _tag not in _s:
            _s = _s.replace('<link rel="alternate" hreflang="en-ae"', _tag + '\n<link rel="alternate" hreflang="x-default" href="' + DOMAIN + ('' if _en == 'index' else _en + '.html') + '">\n<link rel="alternate" hreflang="en-ae"', 1)
            _f.write_text(_s)
