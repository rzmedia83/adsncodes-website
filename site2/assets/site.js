(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  var $ = function(s, r){ return (r || document).querySelector(s); };
  var $$ = function(s, r){ return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var hasGsap = !!(window.gsap && window.ScrollTrigger);

  /* video posters load only when the video is near the screen */
  (function(){ var lp = $$('video[data-lposter]'); if (!lp.length) return;
    var set = function(v){ if (v.dataset.lposter) { v.poster = v.dataset.lposter; v.removeAttribute('data-lposter'); } };
    if (!('IntersectionObserver' in window)) { lp.forEach(set); return; }
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { set(e.target); io.unobserve(e.target); } }); }, { rootMargin: '700px 0px' });
    lp.forEach(function(v){ io.observe(v); }); })();
  /* videos play only on screen */
  $$('video').forEach(function(v){
    v.muted = true;
    if (reduce) { v.pause(); return; }
    if ('IntersectionObserver' in window) new IntersectionObserver(function(es){
      es.forEach(function(e){ if (e.isIntersecting) { if (v.classList.contains('sv') && !v.classList.contains('on')) return; var p = v.play(); if (p && p.catch) p.catch(function(){}); } else v.pause(); });
    }, { threshold: .05 }).observe(v);
  });

  /* smooth scroll */
  var lenis = null;
  if (false && !reduce && window.Lenis) {  /* native scrolling: smoother on every device */
    try {
      lenis = new Lenis({ lerp: .09, smoothWheel: true });
      if (hasGsap) { lenis.on('scroll', ScrollTrigger.update); gsap.ticker.add(function(t){ lenis.raf(t * 1000); }); gsap.ticker.lagSmoothing(0); }
      else (function raf(t){ lenis.raf(t); requestAnimationFrame(raf); })(0);
    } catch (e) { lenis = null; }
  }
  $$('a[href^="#"]').forEach(function(a){
    a.addEventListener('click', function(e){
      var id = a.getAttribute('href'); var el = id.length > 1 && $(id);
      if (!el) return; e.preventDefault();
      if (lenis) lenis.scrollTo(el, { offset: -90 }); else el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
    });
  });

  /* nav + drawer */
  var nav = $('#nav');
  function onScroll(){ if (nav) nav.classList.toggle('scrolled', window.scrollY > 40); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  var mb = $('#menuBtn'), dr = $('#drawer');
  if (mb && dr) mb.addEventListener('click', function(){
    var open = !dr.classList.contains('open'); dr.classList.toggle('open', open); mb.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (mb.firstChild && mb.firstChild.nodeType === 3) mb.firstChild.nodeValue = open ? 'Close' : 'Menu';
    dr.setAttribute('aria-hidden', open ? 'false' : 'true'); document.documentElement.style.overflow = open ? 'hidden' : '';
    if (lenis) open ? lenis.stop() : lenis.start();
    if (open && window.innerHeight > (screen.height || 900) * 1.4) { dr.classList.add('tall'); try { dr.scrollIntoView({ block: 'start' }); } catch (e) {} }
  });

  if (mb && dr) document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && dr.classList.contains('open')) mb.click(); });

  /* live Dubai card */
  (function(){ var t = $('#lcTime'), n = $('#lcNote'); if (!t) return;
    function tick(){ try { var d = new Date(), f = new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', hour12: true, timeZone: 'Asia/Dubai' });
      t.textContent = f.format(d).toUpperCase();
      var parts = new Intl.DateTimeFormat('en-GB', { weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false, timeZone: 'Asia/Dubai' }).formatToParts(d), P = {};
      parts.forEach(function(p){ P[p.type] = p.value; });
      var days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'], wd = days.indexOf(P.weekday), m = (+P.hour % 24) * 60 + (+P.minute);
      var HRS = [null, [9,18], [9,18], [9,18], [9,18], [9,18], [9,14]];
      var names = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
      function fmt(x){ return (x > 12 ? x - 12 : x) + ':00 ' + (x >= 12 ? 'PM' : 'AM'); }
      var today = HRS[wd], open = !!today && m >= today[0] * 60 && m < today[1] * 60, st = $('#lcStatus');
      if (st) { st.textContent = open ? 'Open now' : 'Closed now'; st.parentNode.classList.toggle('closed', !open); }
      if (open) { n.textContent = 'Open until ' + fmt(today[1]) + ', Dubai time. Message us on WhatsApp for a quick reply.'; }
      else {
        var k = 0, nd = wd;
        if (today && m < today[0] * 60) { k = 0; } else { do { nd = (nd + 1) % 7; k++; } while (!HRS[nd]); }
        var when = k === 0 ? 'today' : (k === 1 ? 'tomorrow' : 'on ' + names[nd]);
        n.textContent = 'Opens ' + when + ' at ' + fmt(HRS[k === 0 ? wd : nd][0]) + ', Dubai time. Message us any time and we will reply then.';
      }
    } catch (e) {} }
    tick(); setInterval(tick, 20000);
  })();

  /* live UAE clock */
  $$('[data-clock]').forEach(function(c){
    function tick(){ try { c.textContent = 'UAE ' + new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', timeZone: 'Asia/Dubai' }).format(new Date()) + ', open for new projects'; } catch (e) {} }
    tick(); setInterval(tick, 15000);
  });

  /* copy buttons */
  $$('[data-copy]').forEach(function(b){
    b.addEventListener('click', function(){
      var t = b.getAttribute('data-copy'), old = b.textContent;
      function done(ok){ b.textContent = ok ? 'Copied' : 'Select and copy'; setTimeout(function(){ b.textContent = old; }, 1600); }
      try { navigator.clipboard.writeText(t).then(function(){ done(true); }, function(){ done(false); }); } catch (e) { done(false); }
    });
  });

  /* liquid silk shader, used on any canvas.silk */
  window.ANCsilk = function(cv, opts){
    opts = opts || {};
    var gl = cv && (cv.getContext('webgl', { antialias: false }) || cv.getContext('experimental-webgl'));
    if (!gl) return;
    try { var dbg = gl.getExtension('WEBGL_debug_renderer_info'); var rn = dbg ? String(gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL)) : ''; if (/swiftshader|llvmpipe|software|basic render/i.test(rn)) { cv.classList.add('silk-static'); return; } } catch (e) {}
    var vs = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    var fs = ['precision highp float;uniform vec2 R;uniform float T;uniform vec2 M;uniform float S;',
      'float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}',
      'float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}',
      'float fbm(vec2 p){float v=0.,a=.5;mat2 r=mat2(.8,.6,-.6,.8);for(int i=0;i<4;i++){v+=a*n(p);p=r*p*2.02;a*=.5;}return v;}',
      'float H(vec2 p){vec2 m=(M-.5)*vec2(R.x/R.y,1.);float d=length(p-m*.95);',
      'p+=normalize(p-m*.95+.0001)*.16*exp(-d*d*3.)*sin(d*10.-T*2.2);',
      'vec2 q=vec2(fbm(p*.9+vec2(0.,T*.05)),fbm(p*.9+vec2(5.2,1.3)-T*.04));',
      'vec2 r=vec2(fbm(p+2.2*q+vec2(1.7,9.2)+T*.06),fbm(p+2.2*q+vec2(8.3,2.8)-T*.05));',
      'return fbm(p*.7+2.6*r+S*.6);}',
      'void main(){vec2 uv=gl_FragCoord.xy/R;vec2 p=(gl_FragCoord.xy-.5*R)/R.y*.95;',
      'float e=2./R.y;float c=H(p);float dx=H(p+vec2(e,0))-c;float dy=H(p+vec2(0,e))-c;',
      'vec3 N=normalize(vec3(-dx/e*.35,-dy/e*.35,1.));vec3 L=normalize(vec3(.6+(M.x-.5)*.8,.7+(M.y-.5)*.8,.9));',
      'float di=clamp(dot(N,L),0.,1.);float sp=pow(clamp(dot(reflect(-L,N),vec3(0,0,1)),0.,1.),28.);float fr=pow(1.-N.z,2.);',
      'vec3 ink=vec3(.255,.251,.259);vec3 col=ink*(.55+.75*di)+vec3(1.)*(sp*.95+fr*.35);',
      'col=mix(col,ink*.75,smoothstep(.4,1.2,length(uv-vec2(.7,.55))));col+=(h(gl_FragCoord.xy+T)-.5)*.035;',
      'gl_FragColor=vec4(clamp(col,0.,1.),1.);}'].join('\n');
    function sh(t, s){ var o = gl.createShader(t); gl.shaderSource(o, s); gl.compileShader(o); return o; }
    var pr = gl.createProgram(); gl.attachShader(pr, sh(gl.VERTEX_SHADER, vs)); gl.attachShader(pr, sh(gl.FRAGMENT_SHADER, fs)); gl.linkProgram(pr);
    if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) return;
    gl.useProgram(pr);
    gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1,3,-1,-1,3]), gl.STATIC_DRAW);
    var loc = gl.getAttribLocation(pr, 'p'); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
    var uR = gl.getUniformLocation(pr, 'R'), uT = gl.getUniformLocation(pr, 'T'), uM = gl.getUniformLocation(pr, 'M'), uS = gl.getUniformLocation(pr, 'S');
    var lite = matchMedia('(max-width:760px)').matches || (navigator.hardwareConcurrency || 8) <= 4, skip = 0;
    var scale = opts.scale || (lite ? .32 : .5), mx = .62, my = .55, tx = .62, ty = .55, vis = true, t0 = performance.now();
    function fit(){ cv.width = Math.max(1, Math.round(cv.clientWidth * scale)); cv.height = Math.max(1, Math.round(cv.clientHeight * scale)); gl.viewport(0, 0, cv.width, cv.height); }
    fit(); window.addEventListener('resize', fit);
    window.addEventListener('pointermove', function(e){ var r = cv.getBoundingClientRect(); tx = (e.clientX - r.left) / r.width; ty = 1 - (e.clientY - r.top) / r.height; }, { passive: true });
    if ('IntersectionObserver' in window) new IntersectionObserver(function(es){ vis = es[0].isIntersecting; }).observe(cv);
    function draw(now){
      mx += (tx - mx) * .06; my += (ty - my) * .06;
      gl.uniform2f(uR, cv.width, cv.height); gl.uniform1f(uT, reduce ? 8 : (now - t0) / 1000); gl.uniform2f(uM, mx, my);
      gl.uniform1f(uS, Math.min(window.scrollY / Math.max(window.innerHeight, 1), 1.5));
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      if (opts.onFrame) opts.onFrame(mx, my);
    }
    if (reduce) draw(performance.now());
    else (function loop(now){ if (vis && !document.hidden && (skip ^= 1)) draw(now || performance.now()); requestAnimationFrame(loop); })();
  };
  (function(){ function start(){ $$('canvas.silk').forEach(function(c){ if (c.offsetParent === null && getComputedStyle(c).position !== 'fixed') return; window.ANCsilk(c); }); }
    var go = false; function start2(){ if (go) return; go = true; start(); }
    function idle(){ if ('requestIdleCallback' in window) requestIdleCallback(start2, { timeout: 1500 }); else setTimeout(start2, 300); }
    /* phones: the shader waits until the first touch or scroll, or a few seconds after load, so it never competes with the first view */
    var phone = matchMedia('(max-width: 900px)').matches;
    function onLoad(){ if (phone) { setTimeout(idle, 4000); ['pointerdown','touchstart','scroll'].forEach(function(ev){ window.addEventListener(ev, idle, { once: true, passive: true }); }); } else idle(); }
    if (document.readyState === 'complete') onLoad(); else window.addEventListener('load', onLoad); })();

  /* industry panels */
  var panels = $$('.panel');
  function openPanel(p){ panels.forEach(function(x){ var on = x === p; x.classList.toggle('on', on); x.setAttribute('aria-expanded', on ? 'true' : 'false'); }); }
  if (!$('#industries')) panels.forEach(function(p){ p.addEventListener('click', function(){ openPanel(p); }); if (fine) p.addEventListener('pointerenter', function(){ openPanel(p); }); });

  /* industries: hover or tap to open; phones swipe; gently rotates while on screen */
  var ind = $('#industries');
  if (ind && panels.length) {
    var row = ind.querySelector('.panels'), ibar = ind.querySelector('.ind-prog i');
    var phoneQ = window.matchMedia('(max-width: 820px)');
    var curI = Math.max(0, panels.findIndex ? panels.findIndex(function(p){ return p.classList.contains('on'); }) : 0);
    var paused = false, inView = false, timer = null, userTouched = false;
    var setBar = function(){ if (ibar) ibar.style.width = ((curI + 1) / panels.length * 100) + '%'; };
    var show = function(i, fromUser){ curI = (i + panels.length) % panels.length; openPanel(panels[curI]); setBar();
      if (fromUser) userTouched = true;
      if (phoneQ.matches && row && fromUser !== 'swipe') { var p = panels[curI]; row.scrollTo({ left: p.offsetLeft - (row.clientWidth - p.offsetWidth) / 2, behavior: reduce ? 'auto' : 'smooth' }); } };
    panels.forEach(function(p, i){ p.addEventListener('click', function(){ show(i, true); }); if (fine) p.addEventListener('pointerenter', function(){ show(i, true); }); });
    if (fine) { row.addEventListener('pointerenter', function(){ paused = true; }); row.addEventListener('pointerleave', function(){ paused = false; }); }
    var mode = function(){ ind.classList.toggle('ind-swipe', phoneQ.matches); ind.classList.add('ind-auto'); };
    mode(); if (phoneQ.addEventListener) phoneQ.addEventListener('change', mode);
    if (row) { var pt = false; row.addEventListener('scroll', function(){ if (!phoneQ.matches || pt) return; pt = true; requestAnimationFrame(function(){ pt = false;
      var c = row.scrollLeft + row.clientWidth / 2, best = 0, bd = 1e9;
      panels.forEach(function(p, i){ var d = Math.abs(p.offsetLeft + p.offsetWidth / 2 - c); if (d < bd) { bd = d; best = i; } });
      if (best !== curI) show(best, 'swipe'); }); }, { passive: true });
      row.addEventListener('touchstart', function(){ userTouched = true; }, { passive: true }); }
    var tick = function(){ if (inView && !paused && !userTouched && !document.hidden && !reduce) show(curI + 1); };
    if ('IntersectionObserver' in window) new IntersectionObserver(function(es){ inView = es[0].isIntersecting;
      if (inView && !timer) timer = setInterval(tick, 4200); if (!inView && timer) { clearInterval(timer); timer = null; } }, { threshold: .45 }).observe(ind);
    setBar();
  }

  /* sections ease in as they arrive */
  if (!reduce && 'IntersectionObserver' in window) {
    document.documentElement.classList.add('rv-on');
    var rio = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('in'); rio.unobserve(e.target); } }); }, { rootMargin: '0px 0px -8% 0px', threshold: .06 });
    $$('main .row-head, .sg, .wk > .wk-item, .stories article, .gsteps li, .qa, .case-row, .icard, .uae-in, .ai-in > *, .founder, .places .place').forEach(function(el){
      if (el.closest('#split') || el.closest('#industries')) return;
      var sib = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
      el.style.setProperty('--d', Math.min(sib, 4) * .08 + 's'); el.classList.add('rvl'); rio.observe(el);
    });
  }

  /* FAQ */
  $$('.qa button').forEach(function(b){
    b.addEventListener('click', function(){
      var open = b.getAttribute('aria-expanded') === 'true', grp = b.closest('.faq-list') || document;
      $$('.qa button', grp).forEach(function(x){ x.setAttribute('aria-expanded', 'false'); });
      b.setAttribute('aria-expanded', open ? 'false' : 'true');
    });
  });

  /* WhatsApp demo */
  var msgs = $('#msgs');
  if (msgs) {
    var convos = {
      clinic: { name: 'Dental Clinic', done: 'Booked and synced to the clinic software', m: [['u','Hi, I want to book a cleaning this week.'],['a','Of course. Dr. Sara has Thursday at 4:30 pm or Saturday at 11:00 am. Which suits you?'],['u','Thursday works.'],['a','Booked for Thursday at 4:30 pm with Dr. Sara. You’ll get a reminder the day before.']] },
      food: { name: 'Grill Restaurant', done: 'Order sent to the POS and kitchen screen', m: [['u','2 chicken shawarma and a mint lemonade'],['a','Added both. Deliver to your saved address in JLT, cash on delivery?'],['u','Yes please'],['a','Confirmed and sent to the kitchen. It should reach you in about 35 minutes.']] },
      home: { name: 'Smart Home Company', done: 'Lead saved to the CRM, specialist notified', m: [['u','What does a smart home setup cost for a 3 bedroom villa?'],['a','It depends on what you want automated. Lighting, curtains, security, or all of it?'],['u','Lighting and security.'],['a','Got it. I’ll share a starting package and book a site visit with our specialist. What day suits you?']] },
      realty: { name: 'Property Agency', done: 'Qualified lead sent to the sales team', m: [['u','Looking for a 2 bed apartment in Abu Dhabi, around AED 120k a year.'],['a','Great. Al Reem Island or Saadiyat? And are you moving in this month or later?'],['u','Al Reem, next month.'],['a','I have three matching units. An agent will call you within the hour with viewing times.']] }
    };
    var biz = $('#bizName'), timers = [];
    var el = function(cls, txt){ var d = document.createElement('div'); d.className = cls; if (txt) d.textContent = txt; return d; };
    var play = function(k){
      timers.forEach(clearTimeout); timers = [];
      var c = convos[k]; biz.textContent = c.name; msgs.textContent = ''; var t = 0;
      c.m.forEach(function(row){
        if (row[0] === 'a' && !reduce) { timers.push(setTimeout(function(){ var ty = el('typing'); ty.innerHTML = '<i></i><i></i><i></i>'; msgs.appendChild(ty); }, t)); t += 700; }
        timers.push(setTimeout(function(){ var ty = $('.typing', msgs); if (ty) ty.remove(); msgs.appendChild(el('m ' + row[0], row[1])); }, t));
        t += reduce ? 0 : 650;
      });
      timers.push(setTimeout(function(){ var s = el('synced'); s.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12l5 5L20 6" fill="none" stroke="#414042" stroke-width="2.6" stroke-linecap="round"/></svg>'; s.appendChild(document.createTextNode(c.done)); msgs.appendChild(s); }, t + 200));
    };
    $$('.tab').forEach(function(b){ b.addEventListener('click', function(){ $$('.tab').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); play(b.dataset.k); }); });
  }

  /* work filter */
  var fbtns = $$('[data-filter]');
  fbtns.forEach(function(b){
    b.addEventListener('click', function(){
      var f = b.dataset.filter;
      fbtns.forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      $$('.wcard').forEach(function(c){ c.hidden = !(f === 'all' || (c.dataset.cat || '').indexOf(f) > -1); });
      if (window.ScrollTrigger) ScrollTrigger.refresh();
    });
  });
  var hf = (location.hash.match(/^#(brand|pack|campaign|photo|digital|results)$/) || [])[1];
  if (hf) { var hb = $('[data-filter="' + hf + '"]'); if (hb) { hb.click(); setTimeout(function(){ var g = hb.closest('section') || hb; g.scrollIntoView({behavior: 'smooth'}); }, 300); } }

  /* contact form: composes a WhatsApp or email message */
  var form = $('#enquiry');
  if (form) {
    var waBtn = $('#sendWa'), mlBtn = $('#sendMail');
    var compose = function(){
      var d = new FormData(form), svc = d.getAll('svc').join(', ');
      var body = 'Hi Ads n’ Codes, I’d like to discuss a project.\n\nName: ' + (d.get('name') || '') + '\nBusiness: ' + (d.get('biz') || '') + '\nPhone or email: ' + (d.get('reach') || '') + '\nInterested in: ' + (svc || 'Not sure yet') + '\nMonthly budget: ' + (d.get('budget') || 'Not decided') + '\n\n' + (d.get('msg') || '');
      waBtn.href = 'https://wa.me/971565440310?text=' + encodeURIComponent(body);
      mlBtn.href = 'mailto:bd@adsncodes.com?subject=' + encodeURIComponent('Project enquiry from ' + (d.get('biz') || d.get('name') || 'website')) + '&body=' + encodeURIComponent(body);
    };
    form.addEventListener('input', compose); form.addEventListener('change', compose); compose();
    form.addEventListener('submit', function(e){ e.preventDefault(); });
  }

  /* footer: fold the service list on phones */
  var fd = $('.fsvc-d'); if (fd && window.matchMedia('(max-width: 900px)').matches) fd.removeAttribute('open');

  /* home: Ads n' Codes split hero */
  var split = $('#split');
  if (split) {
    var codes = $('#codesLayer'), handle = $('#splitHandle'), world = $('.ads-layer .world'), stage = $('.ads-layer .stage');
    var mq = window.matchMedia('(max-width: 900px)');
    var cur = 1, target = 1, dragging = false, lastUser = -1e9, box = { W: 1, H: 1, t: 0, b: 0, rest: .5 };
    var measure = function(){ var r = split.getBoundingClientRect(), q = stage.getBoundingClientRect(), w = world.getBoundingClientRect();
      box = { W: r.width || 1, H: r.height || 1, t: w.top - r.top, b: w.bottom - r.top, rest: mq.matches ? .5 : Math.min(.85, Math.max(.5, ((q.left + q.width / 2) - r.left) / (r.width || 1))) }; };
    var set = function(v){ cur = v; var x = v * 100;
      if (mq.matches) { codes.style.clipPath = 'inset(0 0 ' + Math.max(0, box.H - box.b) + 'px ' + x + '%)'; handle.style.top = box.t + 'px'; handle.style.height = (box.b - box.t) + 'px'; handle.style.bottom = 'auto'; }
      else { codes.style.clipPath = 'inset(0 0 0 ' + x + '%)'; handle.style.top = '0'; handle.style.height = ''; handle.style.bottom = '0'; }
      handle.style.left = '0'; handle.style.transform = 'translate3d(' + (v * box.W).toFixed(1) + 'px,0,0)'; handle.setAttribute('aria-valuenow', Math.round(x));
      split.classList.toggle('hmid', v > .14 && v < .9); };
    var from = function(x){ var r = split.getBoundingClientRect(); return Math.min(.96, Math.max(.06, (x - r.left) / r.width)); };
    var touch = function(){ lastUser = performance.now(); split.classList.add('touched'); };
    if (fine) {
      split.addEventListener('pointermove', function(e){ if (!dragging) { target = from(e.clientX); touch(); } });
      split.addEventListener('pointerleave', function(){ if (!dragging) { target = box.rest; } });
    }
    handle.addEventListener('pointerdown', function(e){ dragging = true; touch(); handle.setPointerCapture(e.pointerId); e.preventDefault(); });
    handle.addEventListener('pointermove', function(e){ if (dragging) { target = from(e.clientX); touch(); } });
    handle.addEventListener('pointerup', function(){ dragging = false; });
    handle.addEventListener('pointercancel', function(){ dragging = false; });
    handle.addEventListener('keydown', function(e){ if (e.key === 'ArrowLeft') { target = Math.max(.06, target - .06); touch(); e.preventDefault(); } if (e.key === 'ArrowRight') { target = Math.min(.96, target + .06); touch(); e.preventDefault(); } });
    window.addEventListener('resize', measure); window.addEventListener('load', measure);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);
    measure();
    if (reduce) { set(box.rest); window.addEventListener('resize', function(){ set(box.rest); }); }
    else {
      set(mq.matches ? .9 : .98);
      var t0 = performance.now(), n = 0, heroOn = true;
      /* phones: hold the opening frame until the page has settled, then sweep */
      var armed = !mq.matches, arm = function(){ if (armed) return; armed = true; measure(); set(cur); split.classList.add('armed'); t0 = performance.now(); try { split.dispatchEvent(new Event('armed')); } catch (e) {} }; if (armed) split.classList.add('armed');
      if (!armed) { var armLater = function(){ setTimeout(arm, 2500); }; if (document.readyState === 'complete') armLater(); else window.addEventListener('load', armLater); ['pointerdown','touchstart','scroll'].forEach(function(ev){ window.addEventListener(ev, arm, { once: true, passive: true }); }); }
      if ('IntersectionObserver' in window) new IntersectionObserver(function(es){ var was = heroOn; heroOn = es[0].isIntersecting; if (heroOn && !was) requestAnimationFrame(loop); }).observe(split);
      var loop = function(now){
        if (!heroOn || document.hidden) { if (document.hidden) setTimeout(function(){ requestAnimationFrame(loop); }, 500); return; }
        if (!armed) { requestAnimationFrame(loop); return; }
        now = now || performance.now(); var e = now - t0;
        if (++n % 180 === 0) measure();
        if (now - lastUser > 3500 && !dragging) {
          if (e < 1400) target = mq.matches ? .9 : .98;       /* open on the Ads side, a strip of Codes showing on phones */
          else if (e < 3200) target = mq.matches ? .08 : .3;  /* sweep: the Codes side takes over */
          else if (!fine && e > 5000) target = .5 + Math.sin((e - 5000) / 2400) * .3;  /* phones: keep breathing */
          else target = box.rest;                              /* settle */
        }
        if (Math.abs(target - cur) > .0004) set(cur + (target - cur) * .07);
        requestAnimationFrame(loop);
      };
      loop();
    }
  }

  /* home: journey chapters swap the sticky visual */
  var chapters = $$('.chap');
  if (chapters.length) {
    var shots = $$('.jv-shot'), dots = $$('.jv-dot'), curK = -1, ticking = false;
    var pick = function(){
      ticking = false;
      var mid = window.innerHeight * 0.5, best = 0, bestD = Infinity;
      chapters.forEach(function(c, i){
        var t = c.querySelector('h3') || c, r = t.getBoundingClientRect();
        var d = Math.abs((r.top + r.bottom) / 2 - mid);
        if (d < bestD) { bestD = d; best = i; }
      });
      if (best === curK) return; curK = best;
      shots.forEach(function(s, i){ s.classList.toggle('on', i === best); }); dots.forEach(function(d, i){ d.classList.toggle('on', i <= best); });
      chapters.forEach(function(c, i){ c.classList.toggle('on', i === best); });
    };
    window.addEventListener('scroll', function(){ if (!ticking) { ticking = true; requestAnimationFrame(pick); } }, { passive: true });
    window.addEventListener('resize', pick); pick();
  }

  /* service peek */
  var peek = $('#peek');
  if (peek && fine) {
    var px = 0, py = 0, cx = 0, cy = 0, imgs = peek.children;
    $$('[data-peek]').forEach(function(row){
      row.addEventListener('pointerenter', function(){ var k = +row.dataset.peek; for (var i = 0; i < imgs.length; i++) imgs[i].classList.toggle('show', i === k); peek.classList.add('on'); });
      row.addEventListener('pointerleave', function(){ peek.classList.remove('on'); });
    });
    window.addEventListener('pointermove', function(e){ px = e.clientX + 170; py = e.clientY; }, { passive: true });
    (function loop(){ if (Math.abs(px - cx) + Math.abs(py - cy) > .3) { cx += (px - cx) * .14; cy += (py - cy) * .14; peek.style.left = cx + 'px'; peek.style.top = cy + 'px'; } requestAnimationFrame(loop); })();
  }

  /* cursor, magnetic buttons, phone tilt */
  var cu = $('.cur');
  if (fine && cu && !reduce) {
    var ux = -100, uy = -100, vx = -100, vy = -100;
    window.addEventListener('pointermove', function(e){ ux = e.clientX; uy = e.clientY; }, { passive: true });
    (function loop(){ if (Math.abs(ux - vx) + Math.abs(uy - vy) > .2) { vx += (ux - vx) * .2; vy += (uy - vy) * .2; cu.style.transform = 'translate(' + vx + 'px,' + vy + 'px)'; } requestAnimationFrame(loop); })();
    $$('a, button').forEach(function(el){
      if (el.closest('.case,.wcard,.wk-item')) return;
      el.addEventListener('pointerenter', function(){ cu.classList.add('big'); }); el.addEventListener('pointerleave', function(){ cu.classList.remove('big'); });
    });
    $$('.case, .wcard, .wk-item').forEach(function(el){ if (el.querySelector('.reel')) return; el.addEventListener('pointerenter', function(){ cu.classList.add('view'); }); el.addEventListener('pointerleave', function(){ cu.classList.remove('view'); }); });
    $$('.mag').forEach(function(b){
      b.addEventListener('pointermove', function(e){ var r = b.getBoundingClientRect(); b.style.transform = 'translate(' + (e.clientX - r.left - r.width / 2) * .25 + 'px,' + (e.clientY - r.top - r.height / 2) * .35 + 'px)'; });
      b.addEventListener('pointerleave', function(){ b.style.transition = 'transform .5s cubic-bezier(.2,.7,.2,1)'; b.style.transform = ''; setTimeout(function(){ b.style.transition = ''; }, 500); });
    });
    var ph = $('.phone');
    if (ph) { ph.addEventListener('pointermove', function(e){ var r = ph.getBoundingClientRect(); var x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; ph.style.transform = 'perspective(1200px) rotateY(' + x * 10 + 'deg) rotateX(' + (-y * 10) + 'deg)'; }); ph.addEventListener('pointerleave', function(){ ph.style.transform = ''; }); }
  }

  /* GSAP choreography: the library loads after the page, so it never delays the first view */
  function choreo() {
    if (!(window.gsap && window.ScrollTrigger)) return;
    gsap.registerPlugin(ScrollTrigger);
    var mf = $('#manifesto');
    if (mf) {
      mf.innerHTML = mf.textContent.split(' ').map(function(w){ return '<span>' + w + '</span>'; }).join(' ');
      gsap.fromTo('#manifesto span', { opacity: .28 }, { opacity: 1, stagger: .05, ease: 'none', scrollTrigger: { trigger: mf, start: 'top 80%', end: 'bottom 50%', scrub: true } });
    }
    $$('[data-parallax]').forEach(function(img){ gsap.fromTo(img, { yPercent: -7 }, { yPercent: 7, ease: 'none', scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } }); });
    var film = $('#filmBox');
    if (film) gsap.fromTo(film.querySelector('video'), { scale: 1.18 }, { scale: 1, ease: 'none', scrollTrigger: { trigger: film, start: 'top bottom', end: 'bottom top', scrub: true } });
    var reel = $('#reel');
    if (reel) {
      gsap.matchMedia().add('(min-width: 900px)', function(){
        reel.classList.add('pinned');
        var dist = function(){ return Math.max(0, reel.scrollWidth - window.innerWidth); };
        var tw = gsap.to(reel, { x: function(){ return -dist(); }, ease: 'none', scrollTrigger: { trigger: '#reelOuter', start: 'top 12%', end: function(){ return '+=' + dist(); }, pin: true, scrub: 1, invalidateOnRefresh: true } });
        return function(){ reel.classList.remove('pinned'); tw.kill(); gsap.set(reel, { clearProps: 'x' }); };
      });
    }
    var gi = $('.giant img');
    if (gi) gsap.fromTo(gi, { yPercent: 18, scale: .94 }, { yPercent: 0, scale: 1, ease: 'none', scrollTrigger: { trigger: '.giant', start: 'top bottom', end: 'bottom bottom', scrub: true } });
    ScrollTrigger.refresh();
  }
  if (!reduce) {
    var gsapStarted = false;
    var loadGsap = function(){
      if (gsapStarted) return; gsapStarted = true;
      var add = function(src, cb){ var s = document.createElement('script'); s.src = src; s.async = false; s.onload = cb; document.head.appendChild(s); };
      add('https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js');
      add('https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js', choreo);
    };
    var whenLoaded = function(){ setTimeout(function(){ ('requestIdleCallback' in window) ? requestIdleCallback(loadGsap, { timeout: 2000 }) : loadGsap(); }, 1200); };
    /* phones: only once the visitor starts scrolling or touching; larger screens: shortly after load */
    if (!window.matchMedia('(max-width: 900px)').matches) { if (document.readyState === 'complete') whenLoaded(); else window.addEventListener('load', whenLoaded); }
    ['scroll','touchstart','pointerdown'].forEach(function(ev){ window.addEventListener(ev, loadGsap, { once: true, passive: true }); });
  }
})();

/* hero sculpture follows the pointer */
(function(){
  const sc=document.querySelector('.sculpt'); if(!sc||matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const hero=sc.closest('section')||document.body;
  hero.addEventListener('pointermove',e=>{
    const r=hero.getBoundingClientRect(); const x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
    sc.style.setProperty('--ty',(x*22).toFixed(2)+'deg'); sc.style.setProperty('--tx',(-y*16).toFixed(2)+'deg');
  });
  hero.addEventListener('pointerleave',()=>{sc.style.setProperty('--ty','0deg');sc.style.setProperty('--tx','0deg');});
})();

/* load the film only when it comes near the screen */
(function(){
  var vs = document.querySelectorAll('video[data-src]:not(.sr-v)'); if (!vs.length) return;
  function go(v){ if (v.src) return; v.src = v.dataset.src; v.load(); var p = v.play(); if (p && p.catch) p.catch(function(){}); }
  if (!('IntersectionObserver' in window)) { vs.forEach(go); return; }
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { go(e.target); io.unobserve(e.target); } }); }, { rootMargin: '150px 0px' });
  vs.forEach(function(v){ io.observe(v); });
})();

/* hero stages: one frame per side, cycling through real work in sync */
(function(){
  var stages = Array.prototype.slice.call(document.querySelectorAll('.stage')); if (!stages.length) return;
  /* phones open on the people behind the work: BTS first, then the tech expo film */
  if (window.matchMedia('(max-width: 900px)').matches) {
    var ast = document.querySelector('.ads-layer .stage');
    if (ast) { var bts = ast.querySelector('[data-name="Behind the scenes"]'), rg = ast.querySelector('[data-name="Tech expo"]');
      if (rg) ast.insertBefore(rg, ast.firstChild); if (bts) ast.insertBefore(bts, ast.firstChild);
      Array.prototype.forEach.call(ast.querySelectorAll(':scope > img:not(.m-poster), :scope > video.sv'), function(m){ m.classList.remove('on'); }); }
  }
  var pageReady = document.readyState === 'complete'; window.addEventListener('load', function(){ setTimeout(function(){ pageReady = true; }, 900); });
  var DUR = 5200, k = 0, SEL = ':scope > img:not(.m-poster), :scope > video.sv, :scope > .live';
  var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function hyd(m){ if (!m) return; if (m.classList && m.classList.contains('live')) { Array.prototype.forEach.call(m.querySelectorAll('img[data-ssrc]'), function(i){ i.src = i.dataset.ssrc; i.removeAttribute('data-ssrc'); }); return; } if (m.dataset.ssrc) { if (m.dataset.ssrcset) { m.srcset = m.dataset.ssrcset; m.removeAttribute('data-ssrcset'); } m.src = m.dataset.ssrc; m.removeAttribute('data-ssrc'); } if (m.dataset.poster && !m.getAttribute('poster')) m.poster = m.dataset.poster; if (m.tagName === 'VIDEO' && !m.src && m.dataset.vsrc && pageReady && !(navigator.connection && navigator.connection.saveData)) { m.preload = 'auto'; m.src = m.dataset.vsrc; } }
  function liveGo(m){ var run = function(){ Array.prototype.forEach.call(m.querySelectorAll('.lv-win'), function(w){ var im = w.querySelector('.lv-img'); var d = im.offsetHeight - w.clientHeight; if (d < 0) d = 0; d = Math.min(d, w.clientHeight * 3.4); w.style.setProperty('--dist', (-d) + 'px'); w.style.setProperty('--dur', ((+m.dataset.dur || 9000) / 1000 - .6) + 's'); }); void m.offsetWidth; m.classList.add('go'); };
    var ims = m.querySelectorAll('.lv-img'), left = 0; Array.prototype.forEach.call(ims, function(im){ if (!(im.complete && im.naturalHeight)) { left++; im.addEventListener('load', function(){ if (--left === 0) run(); }, { once: true }); } }); if (!left) run(); }
  function durFor(i){ var d = DUR; stages.forEach(function(st){ var it = st.querySelectorAll(SEL), m = it[i % it.length]; if (m && m.dataset.dur) d = Math.max(d, +m.dataset.dur); }); return d; }
  function show(i){
    stages.forEach(function(st){
      var imgs = st.querySelectorAll(SEL), img = imgs[i % imgs.length];
      /* phones: the Codes side waits until the split starts moving, so it never competes with the first view */
      var sp = document.getElementById('split'), held = sp && st.closest('.codes-layer') && !sp.classList.contains('armed');
      if (held) { if (!st._wait) { st._wait = true; sp.addEventListener('armed', function(){ var cur = st.querySelector('.on'); if (cur) { hyd(cur); if (cur.classList.contains('live')) liveGo(cur); } }, { once: true }); } }
      else { hyd(img); (function(n){ setTimeout(function(){ hyd(n); }, 2600); })(imgs[(i + 1) % imgs.length]); }
      imgs.forEach(function(m){ if (m.classList.contains('live')) { m.classList.remove('go'); if (m === img && !held) liveGo(m); } });
      imgs.forEach(function(m){ m.classList.toggle('on', m === img);
        if (m.tagName === 'VIDEO') { if (m === img) { if (!m.src && m.dataset.vsrc) { if (pageReady || i === 0) m.src = m.dataset.vsrc; else (function(v){ window.addEventListener('load', function(){ setTimeout(function(){ if (!v.src) { v.src = v.dataset.vsrc; if (v.classList.contains('on')) { var q = v.play(); if (q && q.catch) q.catch(function(){}); } } }, 900); }, { once: true }); })(m); } var pp = m.play(); if (pp && pp.catch) pp.catch(function(){}); } else { m.pause(); } } });
      var cap = st.querySelector('.stage-cap'); if (cap) { cap.querySelector('b').textContent = img.dataset.name; cap.querySelector('span').textContent = img.dataset.cat; cap.querySelector('em').textContent = String(i % imgs.length + 1).padStart(2,'0') + ' / ' + String(imgs.length).padStart(2,'0'); }
      var bar = st.querySelector('.stage-bar'); if (bar && !still) { bar.style.setProperty('--dur', durFor(i) + 'ms'); bar.classList.remove('run'); void bar.offsetWidth; bar.classList.add('run'); }
    });
  }
  show(0); if (still) return;
  var t; function sched(){ clearTimeout(t); t = setTimeout(function(){ if (!document.hidden) show(++k); sched(); }, durFor(k)); }
  sched();
  stages.forEach(function(st){ st.addEventListener('click', function(){ show(++k); sched(); }); });
})();

/* testimonials: switch voices, rotate slowly */
(function(){
  var qs = document.querySelectorAll('.quote'), bs = document.querySelectorAll('.qnav button'); if (!qs.length || !bs.length) return;
  var i = 0, t;
  function go(k){ i = k % qs.length; qs.forEach(function(q, j){ q.classList.toggle('on', j === i); }); bs.forEach(function(b, j){ b.setAttribute('aria-pressed', j === i ? 'true' : 'false'); }); }
  bs.forEach(function(b, j){ b.addEventListener('click', function(){ clearInterval(t); go(j); }); });
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) t = setInterval(function(){ if (!document.hidden) go(i + 1); }, 7000);
})();

/* agent showcase: tabs + self-scrolling chat */
(function(){
  var shows = document.querySelectorAll('.agent-show'); if (!shows.length) return;
  function setup(win){
    var img = win.querySelector('.lp-chat'); if (!img) return;
    function go(){ var d = img.offsetHeight - win.clientHeight; if (d <= 0) return; win.style.setProperty('--dist', (-d) + 'px'); win.style.setProperty('--dur', Math.max(18, d / 38) + 's'); win.classList.add('run'); }
    if (img.complete && img.naturalHeight) go(); else img.addEventListener('load', go);
    window.addEventListener('resize', function(){ win.classList.remove('run'); void win.offsetWidth; go(); });
  }
  shows.forEach(function(s){
    s.querySelectorAll('.lp-win').forEach(function(w){ var im = w.querySelector('img'); if (im) im.loading = 'lazy'; });
    var tabs = s.querySelectorAll('.ag-tabs button'), panels = s.querySelectorAll('.ag-panel');
    tabs.forEach(function(t){ t.addEventListener('click', function(){
      tabs.forEach(function(x){ x.setAttribute('aria-selected', x === t ? 'true' : 'false'); });
      panels.forEach(function(p){ var on = p.dataset.ag === t.dataset.ag; p.classList.toggle('on', on); if (on) p.querySelectorAll('.lp-win').forEach(function(w){ w.classList.remove('run'); setup(w); }); });
    }); });
    s.querySelectorAll('.ag-panel.on .lp-win').forEach(setup);
  });
})();

/* sound toggle on ad films */
(function(){
  document.querySelectorAll('.reel-sound').forEach(function(b){
    b.addEventListener('click', function(e){
      e.preventDefault(); e.stopPropagation();
      var v = b.parentElement.querySelector('video'); if (!v) return;
      if (!v.src && v.dataset.src) { v.src = v.dataset.src; }
      var on = v.muted;
      document.querySelectorAll('.reel video').forEach(function(o){ if (o !== v) o.muted = true; });
      document.querySelectorAll('.reel-sound').forEach(function(o){ if (o !== b) { o.setAttribute('aria-pressed','false'); o.setAttribute('aria-label','Turn sound on'); } });
      v.muted = !on; b.setAttribute('aria-pressed', on ? 'true' : 'false'); b.setAttribute('aria-label', on ? 'Turn sound off' : 'Turn sound on');
      var p = v.play(); if (p && p.catch) p.catch(function(){});
    });
  });
})();

/* open work videos full size with sound */
(function(){
  var reels = document.querySelectorAll('.wk .reel video, .onset .reel video'); if (!reels.length) return;
  var box = document.createElement('div'); box.className = 'vbox'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-modal', 'true'); box.setAttribute('aria-label', 'Video');
  box.innerHTML = '<button type="button" class="vbox-x" aria-label="Close video">\u00d7</button><video controls playsinline></video>';
  document.body.appendChild(box);
  var bv = box.querySelector('video');
  function close(){ box.classList.remove('open'); bv.pause(); bv.removeAttribute('src'); bv.load(); document.documentElement.style.overflow = ''; }
  box.addEventListener('click', function(e){ if (e.target === box || e.target.classList.contains('vbox-x')) close(); });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && box.classList.contains('open')) close(); });
  reels.forEach(function(v){
    var wrap = v.closest('.reel'); if (!wrap) return;
    var play = document.createElement('button'); play.type = 'button'; play.className = 'reel-open'; play.setAttribute('aria-label', 'Play video with sound');
    play.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M8 5v14l11-7z"/></svg><span>Watch</span>';
    wrap.appendChild(play);
    play.addEventListener('click', function(e){ e.stopPropagation(); bv.src = v.dataset.src || v.currentSrc; bv.poster = v.poster || ''; box.classList.add('open'); document.documentElement.style.overflow = 'hidden'; bv.muted = false; var p = bv.play(); if (p && p.catch) p.catch(function(){}); });
  });
})();

/* ---- custom: showreel ---- */
(function(){
  document.querySelectorAll('[data-sreel]').forEach(function(root){
    var vids = [].slice.call(root.querySelectorAll('.sr-v')), tabs = [].slice.call(root.querySelectorAll('.sreel-tabs button'));
    var capB = root.querySelector('.sreel-cap b'), capS = root.querySelector('.sreel-cap span'), snd = root.querySelector('.sreel-sound');
    var cur = -1, inView = false, muted = true, CAP = 9.5, t0 = 0, raf = 0;
    function load(v){ if (!v.getAttribute('src')) { var big = v.dataset.hd && root.clientWidth * (window.devicePixelRatio || 1) > 1500 && !(navigator.connection && navigator.connection.saveData); v.src = big ? v.dataset.hd : v.dataset.src; v.preload = 'auto'; } }
    function bar(){ var v = vids[cur], b = tabs[cur] && tabs[cur].querySelector('i'); if (!v || !b) return;
      var d = Math.min(CAP, (v.duration || CAP) - (+v.dataset.start || 0)); var p = Math.max(0, Math.min(1, (v.currentTime - (+v.dataset.start || 0)) / d));
      b.style.width = (p * 100) + '%'; if (p >= .999 || v.ended) { next(); return; } raf = requestAnimationFrame(bar); }
    function go(i){
      if (i === cur) return; cancelAnimationFrame(raf);
      vids.forEach(function(v, k){ if (k !== i) { v.classList.remove('on'); try { v.pause(); } catch(e){} } });
      tabs.forEach(function(t, k){ t.setAttribute('aria-selected', k === i ? 'true' : 'false'); var b = t.querySelector('i'); if (b) b.style.width = k < i ? '100%' : '0'; });
      cur = i; var v = vids[i]; load(v); v.muted = muted; v.classList.add('on');
      capB.textContent = v.dataset.name; capS.textContent = v.dataset.cat;
      var st = +v.dataset.start || 0;
      function start(){ try { v.currentTime = st; } catch(e){} if (inView) { var p = v.play(); if (p && p.catch) p.catch(function(){}); } raf = requestAnimationFrame(bar); }
      if (v.readyState >= 1) start(); else v.addEventListener('loadedmetadata', start, {once:true});
      var n = vids[(i + 1) % vids.length]; setTimeout(function(){ if (cur === i) { n.preload = 'metadata'; } }, 2500);
      var tb = tabs[i]; if (tb && tb.parentNode.scrollWidth > tb.parentNode.clientWidth) tb.parentNode.scrollTo({left: tb.offsetLeft - 4, behavior: 'smooth'});
    }
    function next(){ go((cur + 1) % vids.length); }
    tabs.forEach(function(t, k){ t.addEventListener('click', function(){ cur === k ? null : go(k); }); });
    snd.addEventListener('click', function(){ muted = !muted; snd.setAttribute('aria-pressed', muted ? 'false' : 'true'); snd.setAttribute('aria-label', muted ? 'Turn sound on' : 'Turn sound off'); if (vids[cur]) { vids[cur].muted = muted; if (!muted && vids[cur].paused) vids[cur].play().catch(function(){}); } });
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ inView = e.isIntersecting;
      if (cur < 0 && inView) go(0); else if (vids[cur]) { if (inView) { var p = vids[cur].play(); if (p && p.catch) p.catch(function(){}); } else vids[cur].pause(); } }); }, {threshold: .35});
    io.observe(root);
  });
})();

/* ---- custom: logo vs brand slider ---- */
(function(){
  document.querySelectorAll('[data-ba]').forEach(function(ba){
    var r = ba.querySelector('.ba-range'), sec = ba.closest('section'), tabs = sec ? [].slice.call(sec.querySelectorAll('.ba-tabs button')) : [];
    function set(v){ ba.style.setProperty('--v', v + '%'); }
    r.addEventListener('input', function(){ ba.classList.remove('hint'); set(r.value); });
    tabs.forEach(function(t){ t.addEventListener('click', function(){
      tabs.forEach(function(x){ x.setAttribute('aria-selected', x === t ? 'true' : 'false'); });
      ba.querySelectorAll('.ba-case').forEach(function(c){ c.classList.toggle('on', c.dataset.case === t.dataset.case); });
      ba.classList.add('hint'); r.value = 50; set(50);
    }); });
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
      var io = new IntersectionObserver(function(es){ if (!es[0].isIntersecting) return; io.disconnect();
        ba.classList.add('hint'); set(78); setTimeout(function(){ set(22); }, 900); setTimeout(function(){ set(50); r.value = 50; }, 1800); setTimeout(function(){ ba.classList.remove('hint'); }, 2800);
      }, {threshold: .5});
      io.observe(ba);
    }
  });
})();

/* ---- custom: whatsapp agent demo (real WhatsApp look) ---- */
(function(){
  var root = document.querySelector('[data-chat]'); if (!root) return;
  var log = root.querySelector('.wa-log'), body = root.querySelector('.wa-body'), typed = root.querySelector('.wa-typed'), mic = root.querySelector('.wa-mic');
  var asks = document.querySelector('.wa-asks'), sheet = root.querySelector('.wa-sheet'), sb = root.querySelector('.wa-sb'), go = root.querySelector('.wa-sheet .go');
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, busy = false, D = 'assets/agent/demo/';
  function el(h){ var d = document.createElement('div'); d.innerHTML = h.trim(); return d.firstChild; }
  function now(){ var d = new Date(), h = d.getHours(), m = ('0' + d.getMinutes()).slice(-2); return ((h % 12) || 12) + ':' + m + ' ' + (h < 12 ? 'AM' : 'PM'); }
  function add(node){ log.appendChild(node); body.scrollTo({top: body.scrollHeight, behavior: reduce ? 'auto' : 'smooth'}); return node; }
  function me(t){ add(el('<div class="wm me"><p></p><small>' + now() + ' <i class="tk"></i></small></div>')).querySelector('p').textContent = t; }
  function bot(html){ return add(el('<div class="wm"><p>' + html + '</p><small>' + now() + '</small></div>')); }
  function typing(on){ var x = log.querySelector('.wtyp'); if (on && !x) add(el('<div class="wm wtyp"><i></i><i></i><i></i></div>')); else if (!on && x) x.remove(); }
  function wait(ms){ return new Promise(function(r){ setTimeout(r, reduce ? 0 : ms); }); }
  function typeIn(t){ return new Promise(function(r){ typed.classList.add('on'); typed.textContent = ''; mic.classList.add('send'); var i = 0;
    (function n(){ if (i > t.length) { setTimeout(function(){ typed.textContent = ''; typed.classList.remove('on'); mic.classList.remove('send'); r(); }, reduce ? 0 : 250); return; } typed.textContent = t.slice(0, i++); setTimeout(n, reduce ? 0 : 28); })(); }); }
  function think(ms){ typing(true); return wait(ms || 900).then(function(){ typing(false); }); }
  var SVC = [
    {k:'gm', t:'General Medicine', d:'Everyday care for the whole family', s:'Check ups · Fever and infections · Blood pressure', p:'From AED 250', img:'svc-gm.webp', b:'Book General', c:'#1f4e79', ic:'<path d="M7 4v6a4 4 0 0 0 8 0V4M11 14v2a4 4 0 0 0 8 0v-2"/><circle cx="19" cy="12" r="2"/>'},
    {k:'derm', t:'Dermatology', d:'Skin and hair, treated with care', s:'Acne · Pigmentation · Hair loss', p:'From AED 350', img:'svc-derm.webp', b:'Book Dermatology', c:'#1d6b72', ic:'<path d="M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z"/>'},
    {k:'gyn', t:'Gynecology', d:"Women's health, every stage", s:'Antenatal care · Health checks', p:'From AED 350', img:'', b:'Book Gynecology', c:'#7a2f57', ic:'<path d="M12 20s-7-4.3-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.7-7 10-7 10z"/>'}];
  var DOC = [
    {n:'Dr. Rashid Khan', r:'General Medicine · 15+ years', a:'Preventive care, chronic conditions', l:'English, Arabic, Hindi', x:'Next: Tomorrow, 9:00 AM', img:'doc-rashid.webp', b:'Book Dr. Rashid'},
    {n:'Dr. Hana Yusuf', r:'General Medicine · 8+ years', a:'Check ups, fever, infections', l:'English, Arabic', x:'Next: Tomorrow, 12:30 PM', img:'doc-hana.webp', b:'Book Dr. Hana'}];
  function cards(title, sub, list){
    var h = '<div class="wcar"><div class="wcar-h"><b>' + title + '</b><span>' + sub + '</span></div><div class="wcar-t">';
    list.forEach(function(c, i){ h += '<div class="wcard">' + (c.img ? '<img src="' + D + c.img + '" alt="" loading="lazy">' : '<div class="wph" style="background:' + c.c + '"><svg viewBox="0 0 24 24">' + c.ic + '</svg><span>' + c.t + '</span></div>') +
      '<div class="wcb"><b>' + (c.t || c.n) + '</b><p>' + (c.d || c.r) + '</p><p>' + (c.s || c.a) + '</p>' + (c.l ? '<p>' + c.l + '</p>' : '') + '<em>' + (c.p || c.x) + '</em></div><button type="button" data-i="' + i + '"><svg viewBox="0 0 24 24"><path d="M10 8L5 12l5 4M5 12h9a5 5 0 0 1 5 5v1"/></svg>' + c.b + '</button></div>'; });
    var n = add(el(h + '</div></div>'));
    n.querySelectorAll('button').forEach(function(btn){ btn.addEventListener('click', function(){ if (busy) return; me(btn.textContent.trim()); openFlow(list === SVC ? +btn.dataset.i : 0, list === DOC ? +btn.dataset.i : -1); }); });
  }
  var FLOW = {svc: 0, doc: 0, slot: 1, step: 1};
  var SLOTS = ['9:00 AM', '10:30 AM', '12:30 PM', '4:00 PM', '6:15 PM'];
  function renderStep(){
    if (FLOW.step === 1) {
      sb.innerHTML = '<img class="wbn" src="' + D + 'flow-banner.webp" alt=""><small class="st">Step 1 of 3</small><h4>Let\'s find the right appointment</h4><p class="sd">Choose a service.</p>' +
        SVC.map(function(c, i){ return '<label class="wopt' + (i === FLOW.svc ? ' on' : '') + '"><span class="oi" style="background:' + c.c + '"><svg viewBox="0 0 24 24">' + c.ic + '</svg></span><span class="ot"><b>' + c.t + '</b><span>' + c.d + '</span><span>' + c.p + '</span></span><input type="radio" name="wsvc" ' + (i === FLOW.svc ? 'checked' : '') + ' data-i="' + i + '"><i class="rd"></i></label>'; }).join('');
      go.textContent = 'Continue';
    } else if (FLOW.step === 2) {
      sb.innerHTML = '<small class="st">Step 2 of 3</small><h4>Pick a doctor and time</h4><p class="sd">' + SVC[FLOW.svc].t + ', tomorrow.</p>' +
        DOC.map(function(d, i){ return '<label class="wopt' + (i === FLOW.doc ? ' on' : '') + '"><img class="oa" src="' + D + d.img + '" alt=""><span class="ot"><b>' + d.n + '</b><span>' + d.r + '</span></span><input type="radio" name="wdoc" ' + (i === FLOW.doc ? 'checked' : '') + ' data-i="' + i + '"><i class="rd"></i></label>'; }).join('') +
        '<div class="wslots">' + SLOTS.map(function(s, i){ return '<button type="button" class="' + (i === FLOW.slot ? 'on' : '') + '" data-i="' + i + '">' + s + '</button>'; }).join('') + '</div>';
      go.textContent = 'Continue';
    } else {
      sb.innerHTML = '<small class="st">Step 3 of 3</small><h4>Confirm your visit</h4><div class="wsum"><div><span>Service</span><b>' + SVC[FLOW.svc].t + '</b></div><div><span>Doctor</span><b>' + DOC[FLOW.doc].n + '</b></div><div><span>When</span><b>Tomorrow, ' + SLOTS[FLOW.slot] + '</b></div><div><span>Fee</span><b>' + SVC[FLOW.svc].p + '</b></div><div><span>Insurance</span><b>Card photo can be sent in chat</b></div></div>';
      go.textContent = 'Confirm booking';
    }
    sb.scrollTop = 0;
    sb.querySelectorAll('input[name=wsvc]').forEach(function(r){ r.addEventListener('change', function(){ FLOW.svc = +r.dataset.i; renderStep(); }); });
    sb.querySelectorAll('input[name=wdoc]').forEach(function(r){ r.addEventListener('change', function(){ FLOW.doc = +r.dataset.i; renderStep(); }); });
    sb.querySelectorAll('.wslots button').forEach(function(b){ b.addEventListener('click', function(){ FLOW.slot = +b.dataset.i; renderStep(); }); });
  }
  function openFlow(svc, doc){ busy = true; FLOW = {svc: svc || 0, doc: doc >= 0 ? doc : 0, slot: 1, step: doc >= 0 ? 1 : 1}; renderStep(); setTimeout(function(){ sheet.classList.add('open'); sheet.setAttribute('aria-hidden', 'false'); sheet.inert = false; }, reduce ? 0 : 450); }
  function closeFlow(){ sheet.classList.remove('open'); sheet.setAttribute('aria-hidden', 'true'); sheet.inert = true; }
  root.querySelector('.wa-sheet .x').addEventListener('click', function(){ closeFlow(); busy = false; });
  go.addEventListener('click', function(){
    if (FLOW.step < 3) { FLOW.step++; renderStep(); return; }
    closeFlow(); var s = SVC[FLOW.svc], d = DOC[FLOW.doc], t = SLOTS[FLOW.slot];
    add(el('<div class="wm me wflow"><p><b>Book your visit</b>Form submitted</p><small>' + now() + ' <i class="tk"></i></small></div>'));
    think(1100).then(function(){ bot('<b>Booked ✅</b><br>' + s.t + ' with ' + d.n + '<br>Tomorrow at ' + t + '<br><br>Please arrive 10 minutes early with your Emirates ID. I\'ll send a reminder 2 hours before.'); }).then(function(){ busy = false; });
  });
  var ASK = [
    {q:'What are your prices?', run:function(){ return think().then(function(){ cards('Services and prices', 'Swipe to see what we treat. Prices are consultation fees, the final bill is confirmed at the clinic.', SVC); }); }},
    {q:'Can I see your doctors?', run:function(){ return think().then(function(){ cards('Meet our doctors', 'Swipe to meet the team, then tap Book.', DOC); }); }},
    {q:'Do you accept insurance?', run:function(){ return think().then(function(){ bot('Yes, we work with most major UAE insurers. Send a photo of your insurance card here and the front desk will confirm your cover before the visit.'); }); }},
    {q:'I want to book an appointment', run:function(){ return think(700).then(function(){ var n = bot('Sure. Book in about a minute below 👇'); var b = el('<button type="button" class="wcta"><svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h10"/></svg>Book your visit</button>'); n.appendChild(b); b.addEventListener('click', function(){ if (!busy) openFlow(0, -1); }); openFlow(0, -1); }); }}
  ];
  ASK.forEach(function(a){ var b = document.createElement('button'); b.type = 'button'; b.textContent = a.q; asks.appendChild(b);
    b.addEventListener('click', function(){ if (busy) return; busy = true; closeFlow(); typeIn(a.q).then(function(){ me(a.q); return a.run(); }).then(function(){ if (!sheet.classList.contains('open')) busy = false; }); }); });
  function start(){ log.innerHTML = '<div class="wday">Today</div><div class="wnote">🔒 This business uses a secure service from Meta to manage this chat. Tap to learn more.</div>';
    think(700).then(function(){ bot('Hi, welcome to Medicare Health Clinic 👋<br>Ask about services, prices, doctors, insurance or book a visit.'); }); }
  var io = new IntersectionObserver(function(es){ if (es[0].isIntersecting) { io.disconnect(); start(); } }, {threshold: .3}); io.observe(root);
})();

/* hero asterisk: slow drift with the pointer */
(function(){
  var d = document.querySelector('.ads-deco'); if (!d || matchMedia('(prefers-reduced-motion: reduce)').matches || matchMedia('(max-width:900px)').matches) return;
  var tx = 0, ty = 0, x = 0, y = 0, run = false;
  window.addEventListener('pointermove', function(e){ tx = (e.clientX / innerWidth - .5) * -28; ty = (e.clientY / innerHeight - .5) * -20; if (!run) { run = true; requestAnimationFrame(step); } }, { passive: true });
  function step(){ x += (tx - x) * .05; y += (ty - y) * .05; d.style.setProperty('--dx', x.toFixed(1) + 'px'); d.style.setProperty('--dy', y.toFixed(1) + 'px'); if (Math.abs(tx - x) > .1 || Math.abs(ty - y) > .1) requestAnimationFrame(step); else run = false; }
})();

/* banner videos: show the poster first, start the film once the page has loaded */
(function(){
  var hv = document.querySelectorAll('video[data-hsrc]'); if (!hv.length) return;
  function go(){ setTimeout(function(){ hv.forEach(function(v){ v.src = (v.dataset.hd && innerWidth * (window.devicePixelRatio || 1) > 1700 && !(navigator.connection && navigator.connection.saveData)) ? v.dataset.hd : v.dataset.hsrc; var p = v.play(); if (p && p.catch) p.catch(function(){}); }); }, 700); }
  if (document.readyState === 'complete') go(); else window.addEventListener('load', go);
})();

/* Meta Pixel: loaded after the page is ready so it never slows the first view */
(function(){
  var ID='2532781190404772', started=false;
  function boot(){
    if(started) return; started=true;
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init',ID); fbq('track','PageView');
  }
  function later(){ setTimeout(boot, 6000); }
  if(document.readyState==='complete') later(); else window.addEventListener('load', later);
  ['pointerdown','keydown','scroll'].forEach(function(ev){ window.addEventListener(ev, boot, {once:true, passive:true}); });
  document.addEventListener('click', function(e){
    var a=e.target.closest && e.target.closest('a'); if(!a) return;
    var h=a.getAttribute('href')||'';
    var ev = (a.id==='sendWa'||a.id==='sendMail') ? 'Lead' : (/wa\.me|^tel:|^mailto:/.test(h) ? 'Contact' : null);
    if(!ev) return; boot();
    try{ fbq('track', ev, {content_name: ev==='Lead' ? 'Project brief form' : (/wa\.me/.test(h)?'WhatsApp':/^tel:/.test(h)?'Phone':'Email'), page: location.pathname}); }catch(_){}
  }, true);
})();

/* Google Analytics 4: page views queue at once, the library loads after the page so speed is untouched */
(function(){
  var GA='G-P5X3FL8DLN', loaded=false;
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function(){ dataLayer.push(arguments); };
  gtag('js', new Date()); gtag('config', GA);
  function load(){ if(loaded) return; loaded=true; var s=document.createElement('script'); s.async=true; s.src='https://www.googletagmanager.com/gtag/js?id='+GA; document.head.appendChild(s); }
  function later(){ setTimeout(load, 6000); }
  if(document.readyState==='complete') later(); else window.addEventListener('load', later);
  ['pointerdown','keydown','scroll'].forEach(function(ev){ window.addEventListener(ev, load, {once:true, passive:true}); });
  document.addEventListener('click', function(e){
    var a=e.target.closest && e.target.closest('a'); if(!a) return;
    var h=a.getAttribute('href')||'', name=null, p={page_path: location.pathname, link_text: (a.textContent||'').trim().slice(0,60)};
    if(a.id==='sendWa'||a.id==='sendMail'){ name='generate_lead'; p.method = a.id==='sendWa' ? 'whatsapp' : 'email'; }
    else if(/wa\.me|api\.whatsapp\.com/.test(h)) name='whatsapp_click';
    else if(/^tel:/.test(h)) name='phone_click';
    else if(/^mailto:/.test(h)) name='email_click';
    else if(/\/\/(realestate|medicare|grillhouse|inventa|backtoroots)\.adsncodes\.com/.test(h)){ name='demo_click'; p.demo = h.split('//')[1].split('.')[0]; }
    if(!name) return; load(); p.transport_type='beacon';
    try{ gtag('event', name, p); }catch(_){}
  }, true);
})();
