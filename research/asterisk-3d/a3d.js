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
  var VS = 'attribute vec3 p;attribute vec3 q;uniform mat4 M;uniform mat4 R;varying vec3 N;varying vec3 X;void main(){vec4 w=R*vec4(p,1.);N=mat3(R)*q;X=w.xyz;gl_Position=M*w;}';
  var FS = 'precision mediump float;varying vec3 N;varying vec3 X;uniform vec3 C;uniform float K;uniform float A;uniform float L;' +
    'void main(){vec3 n=normalize(N);if(!gl_FrontFacing)n=-n;vec3 v=normalize(-X);vec3 r=reflect(-v,n);' +
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
    var m = mesh(o.depth || .12, o.bevel || .03);
    function buf(data, name) { var b = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW); var l = gl.getAttribLocation(pr, name); gl.enableVertexAttribArray(l); gl.vertexAttribPointer(l, 3, gl.FLOAT, false, 0, 0); }
    buf(m.v, 'p'); buf(m.n, 'q');
    var uM = gl.getUniformLocation(pr, 'M'), uR = gl.getUniformLocation(pr, 'R'), uC = gl.getUniformLocation(pr, 'C'), uK = gl.getUniformLocation(pr, 'K'), uA = gl.getUniformLocation(pr, 'A'), uL = gl.getUniformLocation(pr, 'L');
    gl.uniform3fv(uC, hex(o.color || '#e8e6e3')); gl.uniform1f(uK, o.metal == null ? .6 : o.metal); gl.uniform1f(uL, o.light || 1);
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
      gl.drawArrays(gl.TRIANGLES, 0, m.v.length / 3);
      if (S.onframe) S.onframe(project, S);
    }
    function project(x, y, z) { // object space -> css px within canvas
      var X = R[0]*x + R[4]*y + R[8]*z + R[12], Y = R[1]*x + R[5]*y + R[9]*z + R[13], Z = R[2]*x + R[6]*y + R[10]*z + R[14];
      var cx = MP[0]*X / -Z, cy = MP[5]*Y / -Z, r = cv.getBoundingClientRect();
      return [(cx * .5 + .5) * r.width, (.5 - cy * .5) * r.height, Z];
    }
    function tick(t) {
      S.raf = 0; var dt = Math.min(.05, (t - (S.last || t)) / 1000); S.last = t;
      S.vy *= Math.pow(.04, dt); S.yaw += (S.auto + S.vy) * dt;
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
