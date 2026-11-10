/* Ads n' Codes 3D asterisk. No libraries. A3D.mount(canvas, opts) -> controller | null (no WebGL) */
(function (W) {
  var P = [24.1,30.5,11.1,51.8,2.8,69.5,35.5,86.9,82.4,108.2,4.0,148.1,10.1,161.4,24.4,185.0,103.4,139.6,100.1,213.9,144.4,213.9,141.4,141.5,213.2,183.6,228.6,160.1,234.4,146.2,159.8,109.2,236.5,70.2,228.8,52.2,215.6,30.9,185.8,48.1,141.8,75.9,143.6,6.2,127.5,4.1,100.9,5.8,100.1,20.5,103.2,76.5];
  var TIPS = [[122,5],[14,58],[14,160],[122,213],[230,160],[230,58]];
  function shape() {
    var o = [], i, n = P.length / 2;
    for (i = 0; i < n; i++) o.push([(P[2*i] - 119.6) / 105, -(P[2*i+1] - 109) / 105]);
    var a = 0; for (i = 0; i < n; i++) { var p = o[i], q = o[(i+1)%n]; a += p[0]*q[1] - q[0]*p[1]; }
    if (a < 0) o.reverse();
    return o;
  }
  function inset(o, b) {
    var n = o.length, r = [];
    for (var i = 0; i < n; i++) {
      var p = o[(i+n-1)%n], c = o[i], q = o[(i+1)%n];
      var e1 = norm([c[0]-p[0], c[1]-p[1]]), e2 = norm([q[0]-c[0], q[1]-c[1]]);
      var n1 = [-e1[1], e1[0]], n2 = [-e2[1], e2[0]]; // inward normals for CCW
      var m = norm([n1[0]+n2[0], n1[1]+n2[1]]), k = b / Math.max(.35, m[0]*n1[0] + m[1]*n1[1]);
      r.push([c[0] + m[0]*k, c[1] + m[1]*k]);
    }
    return r;
  }
  function norm(v) { var l = Math.hypot(v[0], v[1]) || 1; return [v[0]/l, v[1]/l]; }
  function ear(o) {
    var idx = o.map(function (_, i) { return i; }), t = [], g = 0;
    function cross(a, b, c) { return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]); }
    function inside(p, a, b, c) { return cross(a,b,p) >= 0 && cross(b,c,p) >= 0 && cross(c,a,p) >= 0; }
    while (idx.length > 3 && g++ < 5000) {
      for (var i = 0; i < idx.length; i++) {
        var ia = idx[(i+idx.length-1)%idx.length], ib = idx[i], ic = idx[(i+1)%idx.length];
        var a = o[ia], b = o[ib], c = o[ic];
        if (cross(a, b, c) <= 1e-9) continue;
        var ok = true;
        for (var j = 0; j < idx.length && ok; j++) { var k = idx[j]; if (k !== ia && k !== ib && k !== ic && inside(o[k], a, b, c)) ok = false; }
        if (ok) { t.push(ia, ib, ic); idx.splice(i, 1); break; }
      }
    }
    t.push(idx[0], idx[1], idx[2]);
    return t;
  }
  function mesh(d, b) {
    var O = shape(), I = inset(O, b), T = ear(I), n = O.length, v = [], nm = [];
    function tri(a, b2, c, flip) {
      var u = [b2[0]-a[0], b2[1]-a[1], b2[2]-a[2]], w = [c[0]-a[0], c[1]-a[1], c[2]-a[2]];
      var N = [u[1]*w[2]-u[2]*w[1], u[2]*w[0]-u[0]*w[2], u[0]*w[1]-u[1]*w[0]], l = Math.hypot(N[0], N[1], N[2]) || 1;
      if (flip) { var s = b2; b2 = c; c = s; N = [-N[0], -N[1], -N[2]]; }
      [a, b2, c].forEach(function (p) { v.push(p[0], p[1], p[2]); nm.push(N[0]/l, N[1]/l, N[2]/l); });
    }
    for (var s = 0; s < 2; s++) {
      var z = s ? -d : d, f = !!s;
      for (var i = 0; i < T.length; i += 3) tri([I[T[i]][0], I[T[i]][1], z], [I[T[i+1]][0], I[T[i+1]][1], z], [I[T[i+2]][0], I[T[i+2]][1], z], f);
      var zo = s ? -(d-b) : d-b;
      for (i = 0; i < n; i++) {
        var j = (i+1)%n, a = [O[i][0], O[i][1], zo], c = [O[j][0], O[j][1], zo], e = [I[j][0], I[j][1], z], g = [I[i][0], I[i][1], z];
        tri(a, c, e, f); tri(a, e, g, f);
      }
    }
    for (i = 0; i < n; i++) {
      j = (i+1)%n;
      var p0 = [O[i][0], O[i][1], d-b], p1 = [O[j][0], O[j][1], d-b], p2 = [O[j][0], O[j][1], -(d-b)], p3 = [O[i][0], O[i][1], -(d-b)];
      tri(p0, p3, p2); tri(p0, p2, p1);
    }
    return { v: new Float32Array(v), n: new Float32Array(nm) };
  }
  function wire(d) {
    var O = shape(), n = O.length, v = [], i, j, k;
    for (k = 0; k < 3; k++) { var z = [d, -d, 0][k]; if (k === 2) continue;
      for (i = 0; i < n; i++) { j = (i+1)%n; v.push(O[i][0], O[i][1], z, O[j][0], O[j][1], z); } }
    for (i = 0; i < n; i++) { var p = O[(i+n-1)%n], c = O[i], q = O[(i+1)%n];
      if ((c[0]-p[0])*(q[1]-c[1]) - (c[1]-p[1])*(q[0]-c[0]) > 0) v.push(c[0], c[1], d, c[0], c[1], -d); }
    return { v: new Float32Array(v), n: new Float32Array(v.length) };
  }
  var VS = 'attribute vec3 p;attribute vec3 q;uniform mat4 M;uniform mat4 R;varying vec3 N;varying vec3 X;void main(){vec4 w=R*vec4(p,1.);N=mat3(R)*q;X=w.xyz;gl_Position=M*w;}';
  var FS = 'precision mediump float;varying vec3 N;varying vec3 X;uniform vec3 C;uniform float K;uniform float A;uniform float L;uniform float F;' +
    'void main(){if(F>.5){float k=.35+.65*smoothstep(-5.6,-3.8,X.z);gl_FragColor=vec4(C*L*k*A,k*A);return;}vec3 n=normalize(N);if(!gl_FrontFacing)n=-n;vec3 v=normalize(-X);vec3 r=reflect(-v,n);' +
    'vec3 l1=normalize(vec3(-.5,.8,.9)),l2=normalize(vec3(.9,-.2,.5));' +
    'float d=max(dot(n,l1),0.)*.75+max(dot(n,l2),0.)*.25;' +
    'float s=pow(max(dot(n,normalize(l1+v)),0.),70.)*1.1+pow(max(dot(n,normalize(l2+v)),0.),30.)*.35;' +
    'float env=.42+smoothstep(-.4,.9,r.y)*.45+smoothstep(.5,.95,r.x)*.3+exp(-pow((r.y-.3)*5.,2.))*.35-smoothstep(.2,-.8,r.y)*.25;' +
    'float fr=pow(1.-max(dot(n,v),0.),2.5);float g=(.92+X.y*.1)*L;' +
    'vec3 col=(C*(.3+d*.75)*(1.-K)+C*env*K)*g+vec3(1.)*s*(.35+K*.5)+vec3(1.)*fr*.28;' +
    'gl_FragColor=vec4(col*A,A);}';
  function persp(f, a, n, fa) { var t = 1/Math.tan(f/2); return [t/a,0,0,0, 0,t,0,0, 0,0,(fa+n)/(n-fa),-1, 0,0,2*fa*n/(n-fa),0]; }
  function mul(a, b) { var r = [], i, j, k; for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) { var x = 0; for (k = 0; k < 4; k++) x += a[k*4+j] * b[i*4+k]; r[i*4+j] = x; } return r; }
  function rot(yaw, pitch, roll, z) {
    var c = Math.cos, s = Math.sin;
    var Ry = [c(yaw),0,-s(yaw),0, 0,1,0,0, s(yaw),0,c(yaw),0, 0,0,0,1];
    var Rx = [1,0,0,0, 0,c(pitch),s(pitch),0, 0,-s(pitch),c(pitch),0, 0,0,0,1];
    var Rz = [c(roll),s(roll),0,0, -s(roll),c(roll),0,0, 0,0,1,0, 0,0,0,1];
    var T = [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,z,1];
    return mul(T, mul(Rx, mul(Ry, Rz)));
  }
  function hex(h) { h = h.replace('#', ''); return [0,2,4].map(function (i) { return parseInt(h.substr(i, 2), 16) / 255; }); }

  function mount(cv, o) {
    o = o || {};
    var reduce = W.matchMedia && W.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var coarse = W.matchMedia && W.matchMedia('(pointer: coarse)').matches;
    var gl = cv.getContext('webgl', { antialias: true, alpha: true, premultipliedAlpha: true });
    if (!gl) return null;
    function sh(t, s) { var x = gl.createShader(t); gl.shaderSource(x, s); gl.compileShader(x); return x; }
    var pr = gl.createProgram(); gl.attachShader(pr, sh(gl.VERTEX_SHADER, VS)); gl.attachShader(pr, sh(gl.FRAGMENT_SHADER, FS)); gl.linkProgram(pr);
    if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) return null;
    gl.useProgram(pr);
    var m = o.wire ? wire(o.depth || .12) : mesh(o.depth || .12, o.bevel || .03), mode = o.wire ? gl.LINES : gl.TRIANGLES;
    function buf(data, name) { var b = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW); var l = gl.getAttribLocation(pr, name); gl.enableVertexAttribArray(l); gl.vertexAttribPointer(l, 3, gl.FLOAT, false, 0, 0); }
    buf(m.v, 'p'); buf(m.n, 'q');
    var uM = gl.getUniformLocation(pr, 'M'), uR = gl.getUniformLocation(pr, 'R'), uC = gl.getUniformLocation(pr, 'C'), uK = gl.getUniformLocation(pr, 'K'), uA = gl.getUniformLocation(pr, 'A'), uL = gl.getUniformLocation(pr, 'L');
    gl.uniform3fv(uC, hex(o.color || '#e8e6e3')); gl.uniform1f(uK, o.metal == null ? .6 : o.metal); gl.uniform1f(uL, o.light || 1); gl.uniform1f(gl.getUniformLocation(pr, 'F'), o.wire ? 1 : 0); if (o.wire) { gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA); }
    gl.enable(gl.DEPTH_TEST); gl.clearColor(0, 0, 0, 0);
    var S = { yaw: o.yaw || -.5, vy: 0, auto: o.spin == null ? .35 : o.spin, tx: 0, ty: 0, px: 0, py: 0, roll: o.roll || 0, a: 0, vis: true, last: 0, raf: 0, onframe: o.onframe };
    var dprCap = coarse ? 1.5 : 2, w = 0, h = 0, R, MP;
    function size() {
      var r = cv.getBoundingClientRect(), d = Math.min(W.devicePixelRatio || 1, dprCap);
      w = Math.max(1, Math.round(r.width * d)); h = Math.max(1, Math.round(r.height * d));
      if (cv.width !== w || cv.height !== h) { cv.width = w; cv.height = h; }
      gl.viewport(0, 0, w, h);
      MP = persp(.52, w / h, .1, 20); gl.uniformMatrix4fv(uM, false, MP);
    }
    function draw() {
      R = rot(S.yaw, S.py + (o.pitch || 0), S.roll + S.px * .15, -(o.dist || 4.4));
      gl.uniformMatrix4fv(uR, false, R); gl.uniform1f(uA, S.a);
      gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
      if (o.wire) gl.clear(gl.DEPTH_BUFFER_BIT), gl.disable(gl.DEPTH_TEST); gl.drawArrays(mode, 0, m.v.length / 3);
      if (S.onframe) S.onframe(project, S);
    }
    function project(x, y, z) { // object space -> css px within canvas
      var X = R[0]*x + R[4]*y + R[8]*z + R[12], Y = R[1]*x + R[5]*y + R[9]*z + R[13], Z = R[2]*x + R[6]*y + R[10]*z + R[14];
      var cx = MP[0]*X / -Z, cy = MP[5]*Y / -Z, r = cv.getBoundingClientRect();
      return [(cx * .5 + .5) * r.width, (.5 - cy * .5) * r.height, Z];
    }
    function tick(t) {
      S.raf = 0; var dt = Math.min(.05, (t - (S.last || t)) / 1000); S.last = t;
      S.vy *= Math.pow(.04, dt); if (o.home) S.vy -= Math.sin(2 * S.yaw) * o.home * dt; S.yaw += (S.auto + S.vy) * dt;
      S.px += (S.tx - S.px) * Math.min(1, dt * 5); S.py += (S.ty - S.py) * Math.min(1, dt * 5);
      S.a = Math.min(1, S.a + dt * 2.2);
      draw();
      if (S.vis && !reduce) S.raf = requestAnimationFrame(tick);
    }
    function start() { if (!S.raf) { S.last = 0; S.raf = requestAnimationFrame(tick); } }
    size(); if (reduce) { S.a = 1; draw(); } else start();
    if (W.ResizeObserver) new ResizeObserver(function () { size(); if (reduce || !S.vis) draw(); }).observe(cv);
    if (W.IntersectionObserver) new IntersectionObserver(function (e) { S.vis = e[0].isIntersecting; if (S.vis && !reduce) start(); }).observe(cv);
    document.addEventListener('visibilitychange', function () { S.vis = !document.hidden; if (S.vis && !reduce) start(); });
    return {
      state: S, project: project, tips: TIPS.map(function (p) { return [(p[0] - 119.6) / 105, -(p[1] - 109) / 105]; }),
      tilt: function (x, y) { S.tx = x; S.ty = y; if (reduce) { S.px = x; S.py = y; draw(); } },
      kick: function (v) { S.vy = Math.max(-14, Math.min(14, S.vy + v)); if (reduce) { S.yaw += v * .05; draw(); } else start(); },
      reduce: reduce
    };
  }
  W.A3D = { mount: mount };
})(window);
/* Auto setup for the three site placements: [data-a3d="knob|hero|wire"] */
(function (W, D) {
  function tilt(el, c, k) { el.addEventListener('pointermove', function (e) { var r = el.getBoundingClientRect(); c.tilt(((e.clientX - r.left) / r.width - .5) * k, ((e.clientY - r.top) / r.height - .5) * k); }); el.addEventListener('pointerleave', function () { c.tilt(0, 0); }); }
  function net(cv, ctl, gcv) {
    var x = cv.getContext('2d'), dpr = Math.min(W.devicePixelRatio || 1, 2);
    var nodes = ctl.tips.map(function (t, i) { return { a: Math.atan2(t[1], t[0]), r: .92 + (i % 2) * .12, ph: i * 1.7, p: (i * .37) % 1 }; });
    return function (project) {
      var b = cv.getBoundingClientRect(), g = gcv.getBoundingClientRect();
      if (cv.width !== Math.round(b.width * dpr)) { cv.width = Math.round(b.width * dpr); cv.height = Math.round(b.height * dpr); }
      x.setTransform(dpr, 0, 0, dpr, 0, 0); x.clearRect(0, 0, b.width, b.height);
      var ox = g.left - b.left, oy = g.top - b.top, t = performance.now() / 1000, cx = ox + g.width / 2, cy = oy + g.height / 2, sc = g.width * .34;
      nodes.forEach(function (n, i) {
        var tp = project(ctl.tips[i][0], ctl.tips[i][1], 0), x1 = tp[0] + ox, y1 = tp[1] + oy;
        var an = n.a + Math.sin(t * .25 + n.ph) * .08, rr = (n.r + Math.sin(t * .6 + n.ph) * .03) * 1.9;
        var x2 = cx + Math.cos(an) * sc * rr, y2 = cy - Math.sin(an) * sc * rr;
        var gr = x.createLinearGradient(x1, y1, x2, y2); gr.addColorStop(0, 'rgba(255,255,255,.3)'); gr.addColorStop(1, 'rgba(255,255,255,.03)');
        x.strokeStyle = gr; x.lineWidth = 1; x.beginPath(); x.moveTo(x1, y1); x.lineTo(x2, y2); x.stroke();
        x.fillStyle = 'rgba(255,255,255,.48)'; x.beginPath(); x.arc(x2, y2, 2.6, 0, 7); x.fill();
        x.strokeStyle = 'rgba(255,255,255,.24)'; x.beginPath(); x.arc(x2, y2, 6 + Math.sin(t * 1.6 + n.ph) * 1.5, 0, 7); x.stroke();
        if (!ctl.reduce) { var p = (t * .35 + n.p) % 1; x.fillStyle = 'rgba(37,211,102,' + (.9 * Math.sin(p * Math.PI)) + ')'; x.beginPath(); x.arc(x2 + (x1 - x2) * p, y2 + (y1 - y2) * p, 2.2, 0, 7); x.fill(); }
      });
    };
  }
  function init() {
    Array.prototype.forEach.call(D.querySelectorAll('[data-a3d]'), function (el) {
      var k = el.getAttribute('data-a3d'), cv = el.querySelector('canvas.gl');
      if (!cv || getComputedStyle(el).display === 'none') return;
      if (k === 'knob') {
        var c = A3D.mount(cv, { color: '#f1efec', metal: .55, light: 1.45, spin: .5, dist: 7.4, pitch: .18, yaw: -.4 });
        if (!c) return; el.classList.add('a3d-on');
        var h = el.closest('[aria-valuenow]'), last = h ? +h.getAttribute('aria-valuenow') : 0;
        if (h && W.MutationObserver) new MutationObserver(function () { var v = +h.getAttribute('aria-valuenow'); c.kick((v - last) * .35); last = v; }).observe(h, { attributes: true, attributeFilter: ['aria-valuenow'] });
      } else if (k === 'hero') {
        var nc = el.querySelector('canvas.net'), draw = null;
        var c2 = A3D.mount(cv, { color: '#ecebe8', metal: .65, light: 1.35, spin: .28, dist: 5.2, pitch: .22, yaw: -.9, onframe: function (p) { if (draw) draw(p); } });
        if (!c2) { el.style.display = 'none'; return; }
        if (nc) draw = net(nc, c2, cv);
        tilt(el.closest('section') || el, c2, .8); el.classList.add('a3d-on');
      } else if (k === 'wire') {
        var c3 = A3D.mount(cv, { wire: true, color: '#ffffff', light: .95, spin: 0, home: 6, dist: 4.4, pitch: .22, yaw: .35, depth: .16 });
        if (!c3) { el.style.display = 'none'; return; }
        var down = false, lx = 0, lt = 0;
        el.addEventListener('pointerdown', function (e) { down = true; lx = e.clientX; lt = performance.now(); });
        W.addEventListener('pointermove', function (e) { if (!down) return; var t = performance.now(); c3.kick((e.clientX - lx) / Math.max(8, t - lt) * 2.2); lx = e.clientX; lt = t; });
        W.addEventListener('pointerup', function () { down = false; });
        tilt(el, c3, .6); el.classList.add('a3d-on');
      }
    });
  }
  // Start on the first sign of a real visitor (or after 8s) so the 3D never competes with page load
  var done = false, ev = ['pointermove', 'pointerdown', 'touchstart', 'scroll', 'keydown', 'wheel'];
  function go() { if (done) return; done = true; ev.forEach(function (e) { W.removeEventListener(e, go, true); }); init(); }
  ev.forEach(function (e) { W.addEventListener(e, go, { capture: true, passive: true }); });
  setTimeout(go, 8000);
})(window, document);
