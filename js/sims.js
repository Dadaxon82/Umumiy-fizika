/* Umumiy fizika — interaktiv modellar (simulyatorlar).
   Har bir model HTML'da <div class="sim-box" data-sim="KALIT"></div> ko'rinishida chaqiriladi.
   Grafik va boshqaruv freymvorki "Yarimo'tkazgich asboblar fizikasi" darsligidan olingan.
   Modellar o'quv maqsadida soddalashtirilgan; barcha kattaliklar SI birliklarida hisoblanadi. */
(() => {
  'use strict';
  const g0 = 9.81, kB = 1.380649e-23, Rg = 8.314, hP = 6.62607015e-34, c0 = 2.99792458e8, qe = 1.602176634e-19, kC = 8.988e9, mu0 = 4e-7 * Math.PI, sSB = 5.670e-8, NA = 6.02214076e23;
  const deg = Math.PI / 180;
  const A = s => (window.YAF_ALIF ? window.YAF_ALIF.A(s) : String(s));
  const C = { cyan: '#22d3ee', green: '#34d399', amber: '#fbbf24', rose: '#fb7185', violet: '#a78bfa', blue: '#60a5fa', grid: '#1e2c44', axis: '#64748b', text: '#cbd5e1' };
  const SUP = { '-': '⁻', '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹' };
  const sci = (v, d = 2) => {
    if (!isFinite(v)) return '—';
    if (v === 0) return '0';
    const e = Math.floor(Math.log10(Math.abs(v)));
    if (e >= -2 && e <= 3) return v.toFixed(Math.max(0, d - (e > 0 ? e : 0))).replace('.', ',');
    const m = v / 10 ** e;
    return `${m.toFixed(d).replace('.', ',')}·10${String(e).split('').map(ch => SUP[ch]).join('')}`;
  };
  const dc = (v, d) => Number(v).toFixed(d).replace('.', ',');
  const fx = (v, d = 3) => (isFinite(v) ? Number(v).toFixed(d).replace('.', ',') : '—');

  function ctx2d(canvas) {
    const r = canvas.getBoundingClientRect();
    const zoom = parseFloat(getComputedStyle(document.documentElement).zoom) || 1;
    const dpr = Math.min((window.devicePixelRatio || 1) * zoom, 4);
    const w = Math.max(1, Math.floor(canvas.clientWidth || r.width)), h = Math.max(1, Math.floor(canvas.clientHeight || r.height));
    if (canvas.width !== w * dpr || canvas.height !== h * dpr) { canvas.width = w * dpr; canvas.height = h * dpr; }
    const c = canvas.getContext('2d'); c.setTransform(dpr, 0, 0, dpr, 0, 0); c.clearRect(0, 0, w, h);
    return { c, w, h };
  }
  function niceTicks(a, b, n = 5) {
    const span = b - a; if (span <= 0) return [a];
    const raw = span / n, mag = 10 ** Math.floor(Math.log10(raw));
    const step = [1, 2, 2.5, 5, 10].map(s => s * mag).find(s => span / s <= n + .5) || mag * 10;
    const out = []; for (let t = Math.ceil(a / step) * step; t <= b + step * 1e-6; t += step) out.push(+t.toPrecision(10));
    return out;
  }
  const fmtTick = t => (Math.abs(t) >= 1000 || (Math.abs(t) < .01 && t !== 0) ? sci(t, 1) : String(+t.toFixed(3)).replace('.', ','));
  const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
  const lin = (a, b, n) => Array.from({ length: n }, (_, i) => a + (b - a) * i / (n - 1));
  const label = (c, t, x, y, col = C.text, al = 'left', size = 12) => { c.fillStyle = col; c.font = `${size}px Inter, sans-serif`; c.textAlign = al; c.fillText(A(t), x, y); };

  /* Umumiy grafik chizuvchi */
  function plot(c, box, o) {
    const [X0, Y0, W, H] = box, L = 54, R = 12, T = 22, B = 36;
    const px = X0 + L, py = Y0 + T, pw = W - L - R, ph = H - T - B;
    const tx = v => (o.logx ? Math.log10(v) : v), ty = v => (o.logy ? Math.log10(Math.max(v, 1e-300)) : v);
    const [xa, xb] = o.xr.map(tx), [ya, yb] = o.yr.map(ty);
    const X = v => px + (tx(v) - xa) / (xb - xa) * pw;
    const Y = v => py + ph - (ty(v) - ya) / (yb - ya) * ph;
    c.save(); c.font = '11px JetBrains Mono, monospace'; c.lineWidth = 1;
    const xt = o.logx ? range(Math.ceil(xa), Math.floor(xb)).map(e => 10 ** e) : niceTicks(o.xr[0], o.xr[1], o.nx || 6);
    const yt = o.logy ? range(Math.ceil(ya), Math.floor(yb)).filter((e, i, arr) => arr.length < 9 || i % 2 === 0).map(e => 10 ** e) : niceTicks(o.yr[0], o.yr[1], o.ny || 5);
    c.strokeStyle = C.grid; c.fillStyle = C.axis; c.textAlign = 'center';
    xt.forEach(t => { const x = X(t); c.beginPath(); c.moveTo(x, py); c.lineTo(x, py + ph); c.stroke(); c.fillText(o.logx ? sci(t, 0) : fmtTick(t), x, py + ph + 15); });
    c.textAlign = 'right';
    yt.forEach(t => { const y = Y(t); c.beginPath(); c.moveTo(px, y); c.lineTo(px + pw, y); c.stroke(); c.fillText(o.logy ? sci(t, 0) : fmtTick(t), px - 6, y + 4); });
    c.strokeStyle = C.axis; c.strokeRect(px, py, pw, ph);
    if (!o.logy && o.yr[0] < 0 && o.yr[1] > 0) { c.strokeStyle = '#475569'; c.beginPath(); c.moveTo(px, Y(0)); c.lineTo(px + pw, Y(0)); c.stroke(); }
    if (!o.logx && o.xr[0] < 0 && o.xr[1] > 0) { c.strokeStyle = '#475569'; c.beginPath(); c.moveTo(X(0), py); c.lineTo(X(0), py + ph); c.stroke(); }
    c.fillStyle = C.text; c.textAlign = 'center'; c.fillText(A(o.xl || ''), px + pw / 2, py + ph + 30);
    c.textAlign = 'left'; c.fillText(A(o.yl || ''), px, py - 8);
    c.beginPath(); c.rect(px, py, pw, ph); c.clip();
    (o.fill || []).forEach(f => { c.fillStyle = f.c; c.beginPath(); f.pts.forEach(([x, y], i) => (i ? c.lineTo(X(x), Y(y)) : c.moveTo(X(x), Y(y)))); c.closePath(); c.fill(); });
    (o.series || []).forEach(s => {
      c.strokeStyle = s.c || C.cyan; c.lineWidth = s.w || 2; c.setLineDash(s.dash || []); c.beginPath(); let started = false;
      s.pts.forEach(([x, y]) => { if (!isFinite(y) || !isFinite(x) || (o.logy && y <= 0) || (o.logx && x <= 0)) { started = false; return; } const xx = X(x), yy = Y(y); if (!started) { c.moveTo(xx, yy); started = true; } else c.lineTo(xx, yy); });
      c.stroke(); c.setLineDash([]);
    });
    (o.vl || []).forEach(v => { c.strokeStyle = v.c || C.amber; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(X(v.x), py); c.lineTo(X(v.x), py + ph); c.stroke(); c.setLineDash([]); if (v.l) { c.fillStyle = v.c || C.amber; c.fillText(A(v.l), X(v.x) + 4, py + 12 + (v.dy || 0)); } });
    (o.hl || []).forEach(v => { c.strokeStyle = v.c || C.amber; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(px, Y(v.y)); c.lineTo(px + pw, Y(v.y)); c.stroke(); c.setLineDash([]); if (v.l) { c.fillStyle = v.c || C.amber; c.fillText(A(v.l), px + 6, Y(v.y) - 5); } });
    (o.marks || []).forEach(m => { c.fillStyle = m.c || '#fff'; c.beginPath(); c.arc(X(m.x), Y(m.y), m.r || 5, 0, 7); c.fill(); if (m.l) { c.fillText(A(m.l), X(m.x) + 8, Y(m.y) - 8); } });
    c.restore();
    if ((o.legend || []).length) { c.fillStyle = 'rgba(3,7,18,.82)'; c.fillRect(px + pw - 166, py + 2, 162, o.legend.length * 16 + 8); }
    (o.legend || []).forEach((g, i) => { c.font = '11px Inter, sans-serif'; c.fillStyle = g.c; c.fillRect(px + pw - 160, py + 8 + i * 16, 12, 3); c.fillStyle = C.text; c.textAlign = 'left'; c.fillText(A(g.l), px + pw - 143, py + 13 + i * 16); });
    return { X, Y, px, py, pw, ph };
  }

  /* Qo'shimcha chizish yordamchilari */
  const ST = new WeakMap();
  const st = (cv, init) => { let s = ST.get(cv); if (!s) { s = init(); ST.set(cv, s); } return s; };
  const line = (c, x1, y1, x2, y2, col = C.text, w = 2, dash = []) => { c.strokeStyle = col; c.lineWidth = w; c.setLineDash(dash); c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2, y2); c.stroke(); c.setLineDash([]); };
  const arrow = (c, x1, y1, x2, y2, col = C.amber, w = 2.2, hd = 9) => {
    const a = Math.atan2(y2 - y1, x2 - x1), L = Math.hypot(x2 - x1, y2 - y1); if (L < 2) return;
    line(c, x1, y1, x2, y2, col, w); c.fillStyle = col; c.beginPath(); c.moveTo(x2, y2);
    c.lineTo(x2 - hd * Math.cos(a - .4), y2 - hd * Math.sin(a - .4)); c.lineTo(x2 - hd * Math.cos(a + .4), y2 - hd * Math.sin(a + .4)); c.closePath(); c.fill();
  };
  const dot = (c, x, y, r, col) => { c.fillStyle = col; c.beginPath(); c.arc(x, y, r, 0, 7); c.fill(); };
  const rect = (c, x, y, w, h, fill, stroke) => { if (fill) { c.fillStyle = fill; c.fillRect(x, y, w, h); } if (stroke) { c.strokeStyle = stroke; c.lineWidth = 1.5; c.strokeRect(x, y, w, h); } };
  const num = (s, re) => { const m = String(s).match(re); return m ? parseFloat(m[1].replace(',', '.')) : NaN; };
  function wl2rgb(l, al = 1) {
    let r = 0, g = 0, b = 0;
    if (l >= 380 && l < 440) { r = -(l - 440) / 60; b = 1; } else if (l < 490) { g = (l - 440) / 50; b = 1; } else if (l < 510) { g = 1; b = -(l - 510) / 20; }
    else if (l < 580) { r = (l - 510) / 70; g = 1; } else if (l < 645) { r = 1; g = -(l - 645) / 65; } else if (l <= 780) { r = 1; }
    let f = l < 420 ? .3 + .7 * (l - 380) / 40 : l > 700 ? .3 + .7 * (780 - l) / 80 : 1; if (l < 380 || l > 780) f = 0;
    const k = v => Math.round(255 * (v * f) ** .8);
    return `rgba(${k(r)},${k(g)},${k(b)},${al})`;
  }
  function resistor(c, x1, y1, x2, y2, col = C.text, lab = '') {
    const L = Math.hypot(x2 - x1, y2 - y1), a = Math.atan2(y2 - y1, x2 - x1), bw = Math.min(46, L * .5);
    const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
    line(c, x1, y1, mx - bw / 2 * Math.cos(a), my - bw / 2 * Math.sin(a), col, 2); line(c, mx + bw / 2 * Math.cos(a), my + bw / 2 * Math.sin(a), x2, y2, col, 2);
    c.save(); c.translate(mx, my); c.rotate(a); c.strokeStyle = col; c.lineWidth = 2; c.strokeRect(-bw / 2, -8, bw, 16); c.restore();
    if (lab) label(c, lab, mx + 12 * Math.sin(a) + (Math.abs(Math.cos(a)) < .5 ? 16 : 0), my - 14 * Math.cos(a) + (Math.abs(Math.cos(a)) < .5 ? 4 : 0), col, Math.abs(Math.cos(a)) < .5 ? 'left' : 'center');
  }
  function battery(c, x, y1, y2, col = C.text, lab = '') { // vertikal manba: yuqorida musbat qutb
    const my = (y1 + y2) / 2; line(c, x, y1, x, my - 6, col, 2); line(c, x, my + 6, x, y2, col, 2);
    line(c, x - 16, my - 6, x + 16, my - 6, col, 2.5); line(c, x - 9, my + 6, x + 9, my + 6, col, 4);
    if (lab) label(c, lab, x - 22, my + 4, col, 'right');
  }

  const S = {};

  /* L1–L2 — Shtangensirkul */
  S.vernier = {
    title: 'Shtangensirkul: nonius bo‘yicha o‘qish', stat: 'nonius · mm',
    params: [
      { k: 'L', l: 'Jismning haqiqiy uzunligi, mm', min: 0, max: 80, step: .01, v: 23.47 },
      { k: 'res', l: 'Nonius aniqligi', type: 'sel', opts: ['0,1 mm (10 bo‘lim)', '0,05 mm (20 bo‘lim)'], v: '0,1 mm (10 bo‘lim)' }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), n = P.res.startsWith('0,1') ? 10 : 20, dl = 1 / n, dv = 1 - dl;
      const rd = Math.round(P.L / dl) * dl, N = Math.floor(rd + 1e-9), k = Math.round((rd - N) / dl);
      const x0 = Math.max(0, P.L - 6), span = 34, s = (w - 40) / span, X = v => 20 + (v - x0) * s, yM = h * .45;
      rect(c, 10, yM - 78, w - 20, 78, '#16233a'); rect(c, X(P.L) - 6, yM + 2, (n * dv) * s + 12, 64, '#0f3b4a');
      label(c, 'Asosiy shkala (mm)', 16, yM - 62, '#94a3b8', 'left', 11); label(c, 'Nonius', X(P.L) - 2, yM + 78, C.cyan, 'left', 11);
      for (let m = Math.ceil(x0); m <= x0 + span; m++) {
        const L = m % 10 === 0 ? 34 : m % 5 === 0 ? 24 : 15;
        line(c, X(m), yM, X(m), yM - L, m === N + k ? C.amber : '#e2e8f0', m === N + k ? 2.4 : 1.2);
        if (m % 10 === 0) label(c, String(m / 10), X(m), yM - 42, '#e2e8f0', 'center', 13);
      }
      for (let j = 0; j <= n; j++) {
        const x = P.L + j * dv, big = n === 10 ? j % 5 === 0 : j % 2 === 0, col = j === k ? C.amber : C.cyan;
        line(c, X(x), yM + 2, X(x), yM + 2 + (big ? 26 : 15), col, j === k ? 2.4 : 1.2);
        if (n === 10 || j % 2 === 0) label(c, String(n === 10 ? j : j / 2), X(x), yM + 44, col, 'center', 11);
      }
      label(c, `O‘qish: ${N} mm + ${k} × ${String(dl).replace('.', ',')} mm = ${rd.toFixed(n === 10 ? 1 : 2).replace('.', ',')} mm`, 20, h - 16, C.green, 'left', 14);
      return { 'Asosiy shkala (nonius noligigacha), mm': String(N), 'Mos tushgan nonius chizig‘i k': String(k), 'O‘qish N + k·Δ, mm': rd.toFixed(n === 10 ? 1 : 2).replace('.', ','), 'Asbob xatoligi Δ, mm': String(dl).replace('.', ','), 'Haqiqiy qiymatdan farq, mm': fx(rd - P.L, 2) };
    }
  };

  /* M1 — To'g'ri chiziqli harakat */
  S.kinem = {
    title: 'x(t) va v(t) grafiklari', stat: 'tekis o‘zgaruvchan harakat',
    params: [
      { k: 'x0', l: 'Boshlang‘ich koordinata x₀, m', min: -20, max: 20, step: 1, v: 0 },
      { k: 'v0', l: 'Boshlang‘ich tezlik v₀, m/s', min: -10, max: 10, step: .5, v: 8 },
      { k: 'a', l: 'Tezlanish a, m/s²', min: -4, max: 4, step: .1, v: -2 },
      { k: 't', l: 'Vaqt t, s', min: 0, max: 10, step: .1, v: 6 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), T = lin(0, 10, 201), x = t => P.x0 + P.v0 * t + P.a * t * t / 2, v = t => P.v0 + P.a * t;
      const xs = T.map(x), lo = Math.min(...xs, 0), hi = Math.max(...xs, 1), pad = (hi - lo) * .1 + 1;
      plot(c, [0, 0, w * .5, h], { xr: [0, 10], yr: [lo - pad, hi + pad], xl: 't, s', yl: 'x, m', series: [{ pts: T.map(t => [t, x(t)]), c: C.cyan, w: 2.5 }], marks: [{ x: P.t, y: x(P.t), c: C.amber }] });
      const vm = Math.max(Math.abs(P.v0), Math.abs(v(10)), 1) * 1.15;
      plot(c, [w * .5, 0, w * .5, h], { xr: [0, 10], yr: [-vm, vm], xl: 't, s', yl: 'v, m/s (yuza = ko‘chish)', fill: [{ c: '#34d39933', pts: [[0, 0], ...lin(0, P.t, 60).map(t => [t, v(t)]), [P.t, 0]] }], series: [{ pts: T.map(t => [t, v(t)]), c: C.green, w: 2.5 }], marks: [{ x: P.t, y: v(P.t), c: C.amber }] });
      let s = 0; const K = 400; for (let i = 0; i < K; i++) s += Math.abs(v(P.t * (i + .5) / K)) * P.t / K;
      const ts = P.a !== 0 ? -P.v0 / P.a : NaN;
      return { 'x(t), m': fx(x(P.t), 2), 'v(t), m/s': fx(v(P.t), 2), 'Ko‘chish Δx, m': fx(x(P.t) - P.x0, 2), 'Bosib o‘tilgan yo‘l s, m': fx(s, 2), 'To‘xtash (burilish) vaqti, s': ts > 0 && ts <= 10 ? fx(ts, 2) : '—' };
    }
  };

  /* M2 — Otilgan jism */
  S.projectile = {
    title: 'Gorizontga burchak ostida otilgan jism (3D)', stat: 'havo qarshiligisiz · 3D', anim: true,
    params: [
      { k: 'v0', l: 'Boshlang‘ich tezlik v₀, m/s', min: 5, max: 40, step: .5, v: 20 },
      { k: 'al', l: 'Otish burchagi α, °', min: 0, max: 90, step: 1, v: 45 },
      { k: 'ph', l: 'Otish yo‘nalishi (azimut) φ, °', min: -60, max: 60, step: 1, v: 0 },
      { k: 'h0', l: 'Boshlang‘ich balandlik h₀, m', min: 0, max: 30, step: .5, v: 0 },
      { k: 'pl', l: 'Sayyora', type: 'sel', opts: ['Yer (g = 9,81 m/s²)', 'Mars (g = 3,71 m/s²)', 'Oy (g = 1,62 m/s²)'], v: 'Yer (g = 9,81 m/s²)' }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), g = num(P.pl, /g = ([\d,]+)/), a = P.al * deg, ph = (P.ph || 0) * deg;
      const vh = P.v0 * Math.cos(a), vy = P.v0 * Math.sin(a), ex = Math.cos(ph), ez = Math.sin(ph);
      const T = (vy + Math.sqrt(vy * vy + 2 * g * P.h0)) / g, L = vh * T, H = P.h0 + vy * vy / (2 * g), tH = vy / g;
      /* Holat: animatsiya vaqti va kamera (sichqoncha/barmoq bilan aylantiriladi) */
      const s0 = st(cv, () => ({ t: 0, yaw: -.62, pitch: .38, zoom: 1, drag: null, auto: true, bound: false }));
      if (!s0.bound) {
        s0.bound = true; cv.style.touchAction = 'none'; cv.style.cursor = 'grab';
        cv.addEventListener('pointerdown', e => { s0.drag = { x: e.clientX, y: e.clientY }; s0.auto = false; cv.setPointerCapture(e.pointerId); cv.style.cursor = 'grabbing'; });
        cv.addEventListener('pointermove', e => {
          if (!s0.drag) return;
          s0.yaw += (e.clientX - s0.drag.x) * .008; s0.pitch = Math.min(1.45, Math.max(.04, s0.pitch + (e.clientY - s0.drag.y) * .006));
          s0.drag = { x: e.clientX, y: e.clientY };
        });
        const up = () => { s0.drag = null; cv.style.cursor = 'grab'; };
        cv.addEventListener('pointerup', up); cv.addEventListener('pointercancel', up);
        cv.addEventListener('wheel', e => { e.preventDefault(); s0.auto = false; s0.zoom = Math.min(3, Math.max(.5, s0.zoom * Math.exp(-e.deltaY * .0012))); }, { passive: false });
        cv.addEventListener('dblclick', () => { s0.yaw = -.62; s0.pitch = .38; s0.zoom = 1; s0.auto = true; });
      }
      if (s0.auto) s0.yaw += dt * .12;
      s0.t += dt * Math.max(1, T / 4); if (s0.t > T * 1.25 + .5) s0.t = 0;
      const t = Math.min(s0.t, T), r = vh * t, py = P.h0 + vy * t - g * t * t / 2, vyt = vy - g * t;
      const pos = tt => { const rr = vh * tt; return [rr * ex, P.h0 + vy * tt - g * tt * tt / 2, rr * ez]; };

      /* Sahna o'lchami va perspektiv proyeksiya */
      const span = Math.max(L, H * 1.25, 10), k = 1 / span;
      const cx0 = L / 2 * ex, cz0 = L / 2 * ez, cy0 = Math.min(H, span * .5) * .35;
      const cyw = Math.cos(s0.yaw), syw = Math.sin(s0.yaw), cp = Math.cos(s0.pitch), sp = Math.sin(s0.pitch);
      const D = 2 / s0.zoom, F = Math.min(w * 1.15, h * 2);
      const pr = (x, y, z) => {
        const X = (x - cx0) * k, Y = (y - cy0) * k, Z = (z - cz0) * k;
        const x1 = X * cyw - Z * syw, z1 = X * syw + Z * cyw;
        const y2 = Y * cp - z1 * sp, z2 = Y * sp + z1 * cp, d = z2 + D;
        if (d < .08) return null;
        return [w / 2 + F * x1 / d, h * .56 - F * y2 / d, d];
      };
      const seg = (p, q, col, wd = 1, dash = []) => { const A1 = pr(...p), B1 = pr(...q); if (A1 && B1) line(c, A1[0], A1[1], B1[0], B1[1], col, wd, dash); };
      const poly = (pts, fill, stroke) => {
        const pp = pts.map(p => pr(...p)); if (pp.some(p => !p)) return;
        c.beginPath(); pp.forEach((p, i) => (i ? c.lineTo(p[0], p[1]) : c.moveTo(p[0], p[1]))); c.closePath();
        if (fill) { c.fillStyle = fill; c.fill(); } if (stroke) { c.strokeStyle = stroke; c.lineWidth = 1; c.stroke(); }
      };
      const path = (pts, col, wd, dash = []) => {
        c.strokeStyle = col; c.lineWidth = wd; c.setLineDash(dash); c.beginPath(); let on = false;
        pts.forEach(p => { const q = pr(...p); if (!q) { on = false; return; } if (on) c.lineTo(q[0], q[1]); else { c.moveTo(q[0], q[1]); on = true; } });
        c.stroke(); c.setLineDash([]);
      };
      const txt = (p, s, col, al = 'left', size = 12) => { const q = pr(...p); if (q) label(c, s, q[0], q[1], col, al, size); };

      /* Osmon foni */
      const sky = c.createLinearGradient(0, 0, 0, h); sky.addColorStop(0, '#0b1730'); sky.addColorStop(1, '#030712');
      c.fillStyle = sky; c.fillRect(0, 0, w, h);

      /* Yer tekisligi va to'r */
      const step = niceTicks(0, span, 6); const st1 = step.length > 1 ? step[1] - step[0] : span / 5;
      const gx0 = -Math.ceil(span * .25 / st1) * st1, gx1 = Math.ceil(span * 1.12 / st1) * st1, gz = Math.ceil(span * .6 / st1) * st1;
      poly([[gx0, 0, -gz], [gx1, 0, -gz], [gx1, 0, gz], [gx0, 0, gz]], 'rgba(22,48,40,.55)', '#1f3b33');
      for (let x = gx0; x <= gx1 + 1e-9; x += st1) seg([x, 0, -gz], [x, 0, gz], C.grid, 1);
      for (let z = -gz; z <= gz + 1e-9; z += st1) seg([gx0, 0, z], [gx1, 0, z], C.grid, 1);
      for (let x = st1; x <= gx1 + 1e-9; x += st1) txt([x, 0, -gz - st1 * .35], fmtTick(x), C.axis, 'center', 10);

      /* Koordinata o'qlari */
      const ax = span * .18;
      const axis3 = (q, col, lab) => { const o = pr(0, 0, 0), e = pr(...q); if (o && e) { arrow(c, o[0], o[1], e[0], e[1], col, 1.6, 7); label(c, lab, e[0] + 5, e[1] - 4, col, 'left', 12); } };
      axis3([gx1, 0, 0], '#64748b', 'x, m'); axis3([0, Math.max(H, ax) * 1.15, 0], '#64748b', 'y, m'); axis3([0, 0, gz], '#64748b', 'z, m');

      /* Boshlang'ich balandlik — minora */
      if (P.h0 > 0) {
        const b = span * .02;
        poly([[-b, 0, -b], [-b, P.h0, -b], [b, P.h0, -b], [b, 0, -b]], '#334155', '#475569');
        poly([[-b, 0, b], [-b, P.h0, b], [b, P.h0, b], [b, 0, b]], '#334155', '#475569');
        poly([[b, 0, -b], [b, P.h0, -b], [b, P.h0, b], [b, 0, b]], '#3f4f66', '#475569');
        poly([[-b, P.h0, -b], [b, P.h0, -b], [b, P.h0, b], [-b, P.h0, b]], '#64748b', '#94a3b8');
        txt([0, P.h0 / 2, -b * 3], `h₀ = ${dc(P.h0, 1)} m`, C.text, 'right', 11);
      }

      /* Trayektoriya: soya, to'liq yo'l va o'tilgan qism */
      const all = lin(0, T, 160).map(pos), done = lin(0, t, 100).map(pos);
      path(all.map(([x, , z]) => [x, 0, z]), 'rgba(148,163,184,.35)', 2, [5, 5]);
      path(all, 'rgba(34,211,238,.35)', 1.6, [6, 5]);
      if (t > 0) path(done, C.cyan, 3);

      /* Otish burchagi yoyi */
      const ra = span * .09;
      path(lin(0, a, 24).map(u => [ra * Math.cos(u) * ex, P.h0 + ra * Math.sin(u), ra * Math.cos(u) * ez]), C.amber, 1.5);
      seg([0, P.h0, 0], [ra * 1.4 * ex, P.h0, ra * 1.4 * ez], 'rgba(251,191,36,.6)', 1, [3, 3]);
      txt([ra * 1.15 * Math.cos(a / 2) * ex, P.h0 + ra * 1.15 * Math.sin(a / 2), ra * 1.15 * Math.cos(a / 2) * ez], `α = ${P.al}°`, C.amber, 'left', 11);

      /* L va H belgilari */
      seg([0, 0, 0], [L * ex, 0, L * ez], C.green, 2.2);
      { const q = pr(L / 2 * ex, 0, L / 2 * ez); if (q) label(c, `L = ${dc(L, 1)} m`, q[0], q[1] + 18, C.green, 'center', 12); }
      if (tH > 0) { const pa = pos(tH); seg([pa[0], 0, pa[2]], pa, C.violet, 1.4, [5, 4]); txt([pa[0], pa[1] + span * .03, pa[2]], `H = ${dc(H, 1)} m`, C.violet, 'center', 12); }

      /* Jism: soya, vertikal chiziq, shar va tezlik vektorlari */
      const bx = r * ex, bz = r * ez, B = pr(bx, py, bz), Bs = pr(bx, 0, bz);
      if (Bs) { c.fillStyle = 'rgba(0,0,0,.45)'; c.beginPath(); c.ellipse(Bs[0], Bs[1], 9 * 2.3 / Bs[2] * .6, 3.5 * 2.3 / Bs[2] * .6, 0, 0, 7); c.fill(); }
      seg([bx, 0, bz], [bx, py, bz], 'rgba(203,213,225,.35)', 1, [2, 3]);
      if (B) {
        const sc = span * .2 / Math.max(P.v0, 1);
        const vec = (dx, dyy, dz, col, lab) => { const E = pr(bx + dx * sc, py + dyy * sc, bz + dz * sc); if (E) { arrow(c, B[0], B[1], E[0], E[1], col, 2.2, 8); label(c, lab, E[0] + 5, E[1] + 4, col, 'left', 12); } };
        vec(vh * ex, 0, vh * ez, C.rose, 'vₓ'); vec(0, vyt, 0, C.green, 'vᵧ'); vec(vh * ex, vyt, vh * ez, C.amber, 'v');
        const R = Math.max(4, 7 * 2.3 / B[2]);
        const gr = c.createRadialGradient(B[0] - R * .35, B[1] - R * .35, R * .1, B[0], B[1], R);
        gr.addColorStop(0, '#ffffff'); gr.addColorStop(.55, '#cbd5e1'); gr.addColorStop(1, '#475569');
        c.fillStyle = gr; c.beginPath(); c.arc(B[0], B[1], R, 0, 7); c.fill();
      }
      label(c, 'Aylantirish: sichqoncha / barmoq · g‘ildirak — masshtab · 2× bosish — tiklash', 12, h - 10, '#64748b', 'left', 11);
      return { 'Uchish vaqti T, s': fx(T, 2), 'Uchish uzoqligi L, m': fx(L, 1), 'Maksimal balandlik H, m': fx(H, 2), 'Yerga tushish tezligi, m/s': fx(Math.hypot(vh, vy - g * T), 1), 'vₓ = v₀cos α (o‘zgarmas), m/s': fx(vh, 2), 'Tushish nuqtasi (x; z), m': `${fx(L * ex, 1)}; ${fx(L * ez, 1)}` };
    }
  };

  /* M3, M4, L5 — Qiya tekislik */
  S.newton = {
    title: 'Qiya tekislikdagi jism', stat: 'Nyuton qonunlari', anim: true,
    params: [
      { k: 'al', l: 'Qiyalik burchagi α, °', min: 0, max: 60, step: 1, v: 30 },
      { k: 'mu', l: 'Sirpanish ishqalanish koeffitsiyenti μ', min: 0, max: .8, step: .01, v: .2 },
      { k: 'm', l: 'Jism massasi m, kg', min: .1, max: 5, step: .1, v: 1 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), a = P.al * deg, N = P.m * g0 * Math.cos(a), Fs = P.m * g0 * Math.sin(a), Fmax = P.mu * N, slides = Fs > Fmax + 1e-9;
      const acc = slides ? g0 * (Math.sin(a) - P.mu * Math.cos(a)) : 0, Ftr = slides ? Fmax : Fs, Lp = 2;
      const s0 = st(cv, () => ({ s: 0, v: 0, hold: 0, key: '' })); const key = [P.al, P.mu].join();
      if (s0.key !== key) { s0.key = key; s0.s = 0; s0.v = 0; s0.hold = 0; }
      if (slides) { if (s0.s < Lp) { s0.v += acc * dt; s0.s = Math.min(Lp, s0.s + s0.v * dt); } else { s0.hold += dt; if (s0.hold > .8) { s0.s = 0; s0.v = 0; s0.hold = 0; } } }
      const len = Math.min(w * .62 / Math.max(Math.cos(a), .3), (h * .72) / Math.max(Math.sin(a), .05), w * .7);
      const Bx = w * .08 + len * Math.cos(a) + 30, By = h * .88, Tx = Bx - len * Math.cos(a), Ty = By - len * Math.sin(a);
      c.fillStyle = '#1e293b'; c.beginPath(); c.moveTo(Tx, Ty); c.lineTo(Bx, By); c.lineTo(Tx, By); c.closePath(); c.fill(); line(c, Tx, Ty, Bx, By, '#94a3b8', 2);
      label(c, `α = ${P.al}°`, Bx - 70, By - 8, C.text);
      const u = .1 + .8 * s0.s / Lp, dx = Math.cos(a), dy = Math.sin(a), nx = Math.sin(a), ny = -Math.cos(a), bs = 34;
      const cx = Tx + u * (Bx - Tx) + nx * bs / 2, cy = Ty + u * (By - Ty) + ny * bs / 2;
      c.save(); c.translate(cx, cy); c.rotate(a); rect(c, -bs / 2, -bs / 2, bs, bs, '#38bdf8', '#e0f2fe'); c.restore();
      const k = 70 / (P.m * g0);
      arrow(c, cx, cy, cx, cy + P.m * g0 * k, C.rose); label(c, 'mg', cx + 6, cy + P.m * g0 * k, C.rose);
      arrow(c, cx, cy, cx + nx * N * k, cy + ny * N * k, C.green); label(c, 'N', cx + nx * N * k + 4, cy + ny * N * k, C.green);
      if (Ftr > 1e-6) { arrow(c, cx, cy, cx - dx * Ftr * k, cy - dy * Ftr * k, C.amber); label(c, 'F_ishq', cx - dx * Ftr * k - 50, cy - dy * Ftr * k - 4, C.amber); }
      label(c, slides ? `a = g(sin α − μcos α) = ${dc(acc, 2)} m/s²` : 'Jism tinch turibdi: F_ishq = mg·sin α ≤ μN', 16, 24, slides ? C.cyan : C.green, 'left', 13);
      return { 'Tayanch reaksiyasi N = mg·cos α, N': fx(N, 2), 'Qiya bo‘ylab kuch mg·sin α, N': fx(Fs, 2), 'Ishqalanish kuchi, N': fx(Ftr, 2), 'Tezlanish a, m/s²': fx(acc, 2), 'Kritik burchak α_kr = arctg μ, °': fx(Math.atan(P.mu) / deg, 1), 'Pastga yetish vaqti (2 m), s': slides && acc > 0 ? fx(Math.sqrt(2 * Lp / acc), 2) : '—' };
    }
  };

  /* M4 — Guk qonuni */
  S.spring = {
    title: 'Simning cho‘zilishi: Guk qonuni', stat: 'σ = Eε',
    params: [
      { k: 'F', l: 'Cho‘zuvchi kuch F, N', min: 0, max: 400, step: 5, v: 100 },
      { k: 'L0', l: 'Sim uzunligi L₀, m', min: .5, max: 3, step: .1, v: 1.5 },
      { k: 'd', l: 'Sim diametri d, mm', min: .2, max: 2, step: .05, v: .5 },
      { k: 'mat', l: 'Material', type: 'sel', opts: ['Po‘lat (E = 200 GPa)', 'Mis (E = 120 GPa)', 'Alyuminiy (E = 70 GPa)', 'Qo‘rg‘oshin (E = 16 GPa)'], v: 'Po‘lat (E = 200 GPa)' }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), E = num(P.mat, /= (\d+)/) * 1e9, Sx = Math.PI * (P.d * 1e-3) ** 2 / 4, sg = P.F / Sx, eps = sg / E, dL = eps * P.L0, kk = E * Sx / P.L0;
      const Fs = lin(0, 400, 50), ymax = 400 / kk * 1e3 * 1.1;
      plot(c, [w * .32, 0, w * .68, h], { xr: [0, 400], yr: [0, ymax], xl: 'F, N', yl: 'ΔL, mm', series: [{ pts: Fs.map(F => [F, F / kk * 1e3]), c: C.cyan, w: 2.5 }], marks: [{ x: P.F, y: dL * 1e3, c: C.amber }], legend: [{ c: C.cyan, l: 'F = kΔL (Guk qonuni)' }] });
      const x = w * .14, top = 24, Lpx = h * .5, ext = Math.min(h * .3, dL / (P.L0 * 4e-3) * h * .3);
      rect(c, x - 50, top - 10, 100, 10, '#475569'); line(c, x, top, x, top + Lpx + ext, '#e2e8f0', Math.max(1.5, P.d * 3));
      rect(c, x - 22, top + Lpx + ext, 44, 30, '#f59e0b'); label(c, `F = ${P.F} N`, x, top + Lpx + ext + 48, C.amber, 'center');
      line(c, x + 40, top + Lpx, x + 60, top + Lpx, '#64748b', 1); line(c, x + 40, top + Lpx + ext, x + 60, top + Lpx + ext, C.green, 1.5); label(c, 'ΔL', x + 64, top + Lpx + ext / 2 + 4, C.green);
      return { 'Kesim yuzasi S, mm²': fx(Sx * 1e6, 3), 'Mexanik kuchlanish σ = F/S, MPa': fx(sg / 1e6, 1), 'Nisbiy deformatsiya ε': sci(eps, 2), 'Absolyut uzayish ΔL, mm': fx(dL * 1e3, 3), 'Bikrlik k = ES/L₀, kN/m': fx(kk / 1e3, 1), 'Holat': eps > 1e-3 ? A('ε > 0,1 %: plastik deformatsiya boshlanishi mumkin') : A('elastik deformatsiya') };
    }
  };

  /* L6–L7 — Sterjenning egilishi */
  S.beam = {
    title: 'Ikki tayanchdagi sterjenning egilishi', stat: 'f = Fl³/(48EI)',
    params: [
      { k: 'F', l: 'Yuk og‘irligi F, N', min: 0, max: 50, step: .5, v: 10 },
      { k: 'l', l: 'Tayanchlar orasidagi masofa l, m', min: .3, max: 1, step: .01, v: .6 },
      { k: 'b', l: 'Sterjen kengligi b, mm', min: 5, max: 30, step: .5, v: 15 },
      { k: 'hh', l: 'Sterjen qalinligi h, mm', min: 1, max: 10, step: .1, v: 3 },
      { k: 'mat', l: 'Material', type: 'sel', opts: ['Po‘lat (E = 200 GPa)', 'Mis (E = 120 GPa)', 'Latun (E = 100 GPa)', 'Alyuminiy (E = 70 GPa)'], v: 'Po‘lat (E = 200 GPa)' }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), E = num(P.mat, /= (\d+)/) * 1e9, I = P.b * 1e-3 * (P.hh * 1e-3) ** 3 / 12, f = P.F * P.l ** 3 / (48 * E * I);
      const x1 = w * .05, x2 = w * .5, y0 = h * .35, amp = Math.min(70, f * 1e3 * 25), Fs = lin(0, 50, 30);
      c.strokeStyle = '#e2e8f0'; c.lineWidth = 6; c.beginPath();
      lin(0, 1, 60).forEach((u, i) => { const xx = u <= .5 ? u : 1 - u, yv = xx * (3 - 4 * xx * xx) / 1; const Y = y0 + amp * yv; const X = x1 + u * (x2 - x1); i ? c.lineTo(X, Y) : c.moveTo(X, Y); }); c.stroke();
      [x1, x2].forEach(xx => { c.fillStyle = '#64748b'; c.beginPath(); c.moveTo(xx, y0 + 4); c.lineTo(xx - 12, y0 + 26); c.lineTo(xx + 12, y0 + 26); c.closePath(); c.fill(); });
      const xm = (x1 + x2) / 2; arrow(c, xm, y0 + amp - 60, xm, y0 + amp - 6, C.amber); label(c, `F = ${P.F} N`, xm + 8, y0 + amp - 44, C.amber);
      line(c, xm + 30, y0, xm + 70, y0, '#64748b', 1, [4, 3]); line(c, xm + 30, y0 + amp, xm + 70, y0 + amp, C.green, 1.5); label(c, `f = ${dc((f * 1e3), 3)} mm`, xm + 74, y0 + amp / 2 + 4, C.green);
      label(c, 'Egilish ko‘rinishi kattalashtirilgan', x1, h - 14, '#64748b', 'left', 11);
      plot(c, [w * .52, 0, w * .48, h], { xr: [0, 50], yr: [0, Math.max(50 * P.l ** 3 / (48 * E * I) * 1e3 * 1.1, .01)], xl: 'F, N', yl: 'f, mm', series: [{ pts: Fs.map(F => [F, F * P.l ** 3 / (48 * E * I) * 1e3]), c: C.cyan, w: 2.5 }], marks: [{ x: P.F, y: f * 1e3, c: C.amber }] });
      return { 'Inersiya momenti I = bh³/12, mm⁴': fx(I * 1e12, 2), 'Egilish strelasi f, mm': fx(f * 1e3, 3), 'Yung moduli E = Fl³/(48fI), GPa': fx(P.F > 0 ? P.F * P.l ** 3 / (48 * f * I) / 1e9 : E / 1e9, 0), 'Bikrlik F/f, N/mm': f > 0 ? fx(P.F / (f * 1e3), 2) : '—' };
    }
  };

  /* M5 — To'qnashuv */
  S.collision = {
    title: 'Markaziy to‘qnashuv', stat: 'impuls va energiya', anim: true,
    params: [
      { k: 'm1', l: '1-jism massasi m₁, kg', min: .2, max: 5, step: .1, v: 1 },
      { k: 'm2', l: '2-jism massasi m₂, kg', min: .2, max: 5, step: .1, v: 2 },
      { k: 'v1', l: '1-jism tezligi v₁, m/s', min: -4, max: 4, step: .1, v: 3 },
      { k: 'v2', l: '2-jism tezligi v₂, m/s', min: -4, max: 4, step: .1, v: -1 },
      { k: 'k', l: 'Tiklanish koeffitsiyenti k (1 — elastik, 0 — noelastik)', min: 0, max: 1, step: .05, v: 1 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), M = P.m1 + P.m2, p = P.m1 * P.v1 + P.m2 * P.v2;
      const u1 = (p - P.m2 * P.k * (P.v1 - P.v2)) / M, u2 = (p + P.m1 * P.k * (P.v1 - P.v2)) / M;
      const K0 = (P.m1 * P.v1 ** 2 + P.m2 * P.v2 ** 2) / 2, K1 = (P.m1 * u1 ** 2 + P.m2 * u2 ** 2) / 2;
      const b1 = .25 + .2 * Math.cbrt(P.m1), b2 = .25 + .2 * Math.cbrt(P.m2), key = [P.m1, P.m2, P.v1, P.v2, P.k].join();
      const s0 = st(cv, () => ({}));
      if (s0.key !== key || s0.t > 5) Object.assign(s0, { key, t: 0, x1: 3, x2: 7, w1: P.v1, w2: P.v2, hit: false });
      s0.t += dt; s0.x1 += s0.w1 * dt; s0.x2 += s0.w2 * dt;
      if (!s0.hit && s0.x2 - s0.x1 <= b1 + b2) { s0.hit = true; s0.w1 = u1; s0.w2 = u2; s0.x1 = Math.min(s0.x1, s0.x2 - b1 - b2); }
      const X = x => 20 + x / 10 * (w - 40), yT = h * .5;
      line(c, 10, yT, w - 10, yT, '#475569', 3);
      [[s0.x1, b1, P.m1, '#38bdf8', s0.w1, 'm₁'], [s0.x2, b2, P.m2, '#f472b6', s0.w2, 'm₂']].forEach(([x, b, m, col, v, lb]) => {
        const hh = 30 + 18 * Math.cbrt(m); rect(c, X(x - b), yT - hh, X(x + b) - X(x - b), hh, col, '#f8fafc'); label(c, lb, X(x), yT - hh / 2 + 4, '#0f172a', 'center', 13);
        if (Math.abs(v) > .02) arrow(c, X(x), yT - hh - 12, X(x) + v * 26, yT - hh - 12, C.amber); label(c, `${dc(v, 2)} m/s`, X(x), yT - hh - 22, C.amber, 'center', 11);
      });
      const bars = [['p oldin', p, C.cyan], ['p keyin', P.m1 * u1 + P.m2 * u2, C.cyan], ['K oldin', K0, C.green], ['K keyin', K1, C.green]], mx = Math.max(...bars.map(b => Math.abs(b[1])), 1);
      bars.forEach(([t, v, col], i) => { const bx = w * .2 + i * w * .16, bh = Math.abs(v) / mx * h * .22; rect(c, bx, h * .95 - bh, w * .1, bh, col + '99'); label(c, t, bx + w * .05, h * .95 + 0, '#94a3b8', 'center', 10); });
      return { 'To‘qnashuvdan keyin u₁, m/s': fx(u1, 2), 'To‘qnashuvdan keyin u₂, m/s': fx(u2, 2), 'Impuls p (saqlanadi), kg·m/s': fx(p, 2), 'Kinetik energiya: oldin, J': fx(K0, 2), 'Kinetik energiya: keyin, J': fx(K1, 2), 'Ichki energiyaga o‘tgan, J': fx(K0 - K1, 2) };
    }
  };

  /* M6 — Dumalash va inersiya momenti */
  const SHAPE = { 'Halqa (I = mR²)': 1, 'Disk / silindr (I = mR²/2)': .5, 'Shar (I = 2mR²/5)': .4, 'Sferik qobiq (I = 2mR²/3)': 2 / 3 };
  S.rotation = {
    title: 'Qiya tekislikdan dumalash', stat: 'I = k·mR²', anim: true,
    params: [
      { k: 'hgt', l: 'Balandlik h, m', min: .1, max: 2, step: .05, v: 1 },
      { k: 'al', l: 'Qiyalik burchagi α, °', min: 5, max: 60, step: 1, v: 20 },
      { k: 'sh', l: 'Jism shakli', type: 'sel', opts: Object.keys(SHAPE), v: 'Disk / silindr (I = mR²/2)' }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), k = SHAPE[P.sh], a = P.al * deg, sLen = P.hgt / Math.sin(a);
      const tOf = kk => Math.sqrt(2 * sLen / (g0 * Math.sin(a) / (1 + kk))), acc = g0 * Math.sin(a) / (1 + k), v = Math.sqrt(2 * g0 * P.hgt / (1 + k));
      const s0 = st(cv, () => ({ t: 0, key: '' })); const key = [P.hgt, P.al, P.sh].join(); if (s0.key !== key) { s0.key = key; s0.t = 0; }
      const T = tOf(k); s0.t += dt; if (s0.t > T + .8) s0.t = 0; const tt = Math.min(s0.t, T), sNow = acc * tt * tt / 2;
      const W = w * .56, len = Math.min(W / Math.cos(a), h * .75 / Math.sin(a)), Bx = 16 + len * Math.cos(a), By = h * .9, Tx = Bx - len * Math.cos(a), Ty = By - len * Math.sin(a), R = 16;
      c.fillStyle = '#1e293b'; c.beginPath(); c.moveTo(Tx, Ty); c.lineTo(Bx, By); c.lineTo(Tx, By); c.closePath(); c.fill();
      const u = sNow / sLen, cx = Tx + u * (Bx - Tx) + Math.sin(a) * R, cy = Ty + u * (By - Ty) - Math.cos(a) * R, ang = sNow / sLen * len / R;
      dot(c, cx, cy, R, k === 1 ? '#0000' : '#38bdf8'); c.strokeStyle = '#e0f2fe'; c.lineWidth = k === 1 ? 4 : 1.5; c.beginPath(); c.arc(cx, cy, R, 0, 7); c.stroke();
      line(c, cx, cy, cx + R * Math.cos(ang), cy + R * Math.sin(ang), '#0f172a', 2.5);
      const names = [['Sirpanish (ishq.siz)', 0], ['Shar', .4], ['Disk', .5], ['Qobiq', 2 / 3], ['Halqa', 1]], tmax = tOf(1) * 1.1;
      names.forEach(([nm, kk], i) => { const y = 24 + i * 26, bw = (w * .36) * tOf(kk) / tmax, on = Math.abs(kk - k) < 1e-9; rect(c, w * .6, y, bw, 16, on ? C.amber : '#334155'); label(c, `${nm}: ${dc(tOf(kk), 2)} s`, w * .6 + 4, y + 12, on ? '#0f172a' : C.text, 'left', 11); });
      return { 'Tezlanish a = g·sin α/(1 + k), m/s²': fx(acc, 3), 'Pastdagi tezlik v = √(2gh/(1 + k)), m/s': fx(v, 2), 'Tushish vaqti, s': fx(T, 2), 'Aylanma energiya ulushi k/(1 + k)': fx(k / (1 + k), 3), 'I_c (m = 1 kg, R = 0,1 m), kg·m²': fx(k * .01, 4), 'Shteyner: chetdagi o‘q, kg·m²': fx((k + 1) * .01, 4) };
    }
  };

  /* M7, L8, L9 — Tebrangichlar */
  S.oscill = {
    title: 'Mayatnik va prujinali tebrangich', stat: 'garmonik tebranish', anim: true,
    params: [
      { k: 'type', l: 'Tebrangich turi', type: 'sel', opts: ['Matematik mayatnik', 'Fizik mayatnik (uchidan osilgan sterjen)', 'Prujinali tebrangich'], v: 'Matematik mayatnik' },
      { k: 'L', l: 'Uzunlik l, m (mayatniklar uchun)', min: .1, max: 2.5, step: .01, v: 1 },
      { k: 'm', l: 'Yuk massasi m, kg (prujinali)', min: .05, max: 2, step: .05, v: .5 },
      { k: 'kk', l: 'Prujina bikrligi k, N/m', min: 2, max: 200, step: 1, v: 20 },
      { k: 'A0', l: 'Amplituda (burchak °, prujinada sm)', min: 1, max: 60, step: 1, v: 10 },
      { k: 'b', l: 'So‘nish koeffitsiyenti β, 1/s', min: 0, max: .5, step: .01, v: 0 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), ty = P.type[0], th0 = P.A0 * deg;
      let w0, Lred = P.L;
      if (ty === 'M') w0 = Math.sqrt(g0 / P.L); else if (ty === 'F') { Lred = 2 * P.L / 3; w0 = Math.sqrt(g0 / Lred); } else w0 = Math.sqrt(P.kk / P.m);
      const T0 = 2 * Math.PI / w0, Tc = ty !== 'P' ? T0 * (1 + th0 * th0 / 16) : T0, wd = Math.sqrt(Math.max((2 * Math.PI / Tc) ** 2 - P.b * P.b, 1e-9));
      const s0 = st(cv, () => ({ t: 0, key: '' })); const key = [P.type, P.L, P.m, P.kk, P.A0, P.b].join(); if (s0.key !== key) { s0.key = key; s0.t = 0; }
      s0.t += dt; const x = t => Math.exp(-P.b * t) * Math.cos(wd * t), xn = x(s0.t);
      const cx = w * .2, top = 22;
      if (ty !== 'P') {
        const Lpx = Math.min(h * .72, 70 + 120 * Math.sqrt(P.L)), ang = th0 * xn;
        rect(c, cx - 50, top - 8, 100, 8, '#475569');
        if (ty === 'M') { const bx = cx + Lpx * Math.sin(ang), by = top + Lpx * Math.cos(ang); line(c, cx, top, bx, by, '#e2e8f0', 1.5); dot(c, bx, by, 13, '#38bdf8'); }
        else { c.save(); c.translate(cx, top); c.rotate(-ang); rect(c, -7, 0, 14, Lpx, '#38bdf8', '#e0f2fe'); c.restore(); dot(c, cx, top, 4, '#f8fafc'); }
        line(c, cx, top, cx, top + Lpx + 10, '#334155', 1, [4, 4]);
      } else {
        const yEq = h * .5, amp = Math.min(h * .3, P.A0 * 3), y = yEq + amp * xn, coils = 14;
        rect(c, cx - 50, top - 8, 100, 8, '#475569'); c.strokeStyle = '#e2e8f0'; c.lineWidth = 1.6; c.beginPath(); c.moveTo(cx, top);
        for (let i = 1; i <= coils; i++) c.lineTo(cx + (i % 2 ? 14 : -14), top + (y - 20 - top) * i / coils); c.lineTo(cx, y - 20); c.stroke();
        rect(c, cx - 22, y - 20, 44, 40, '#f59e0b'); line(c, cx - 60, yEq, cx + 60, yEq, '#334155', 1, [4, 4]);
      }
      const win = Math.max(4 * Tc, 6), t1 = Math.max(0, s0.t - win), ts = lin(t1, t1 + win, 300);
      plot(c, [w * .4, 0, w * .6, h], { xr: [t1, t1 + win], yr: [-1.15, 1.15], xl: 't, s', yl: ty === 'P' ? 'x / A' : 'φ / φ₀', series: [{ pts: ts.filter(t => t <= s0.t).map(t => [t, x(t)]), c: C.cyan, w: 2.2 }, ...(P.b > 0 ? [{ pts: ts.map(t => [t, Math.exp(-P.b * t)]), c: '#64748b', dash: [5, 4] }] : [])], marks: [{ x: s0.t, y: xn, c: C.amber }] });
      const out = { 'Davr T₀ (kichik amplituda), s': fx(T0, 3), 'Chastota ν = 1/T₀, Hz': fx(1 / T0, 3), 'Siklik chastota ω₀, rad/s': fx(w0, 3) };
      if (ty !== 'P') { out['T (amplituda tuzatmasi bilan), s'] = fx(Tc, 3); out['Keltirilgan uzunlik, m'] = fx(Lred, 3); out['g = 4π²l/T₀², m/s²'] = fx(4 * Math.PI ** 2 * Lred / T0 ** 2, 2); }
      else out['To‘liq energiya kA²/2, mJ'] = fx(P.kk * (P.A0 / 100) ** 2 / 2 * 1e3, 1);
      if (P.b > 0) out['Relaksatsiya vaqti τ = 1/β, s'] = fx(1 / P.b, 1);
      return out;
    }
  };

  /* M8 — Maksvell taqsimoti */
  S.maxwell = {
    title: 'Molekulalarning tezliklar bo‘yicha taqsimoti', stat: 'Maksvell taqsimoti',
    params: [
      { k: 'T', l: 'Temperatura T, K', min: 100, max: 2000, step: 10, v: 300 },
      { k: 'gas', l: 'Gaz', type: 'sel', opts: ['H₂ (M = 2 g/mol)', 'He (M = 4 g/mol)', 'N₂ (M = 28 g/mol)', 'O₂ (M = 32 g/mol)', 'CO₂ (M = 44 g/mol)', 'Xe (M = 131 g/mol)'], v: 'N₂ (M = 28 g/mol)' }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), M = num(P.gas, /M = (\d+)/) * 1e-3;
      const f = (v, T) => 4 * Math.PI * (M / (2 * Math.PI * Rg * T)) ** 1.5 * v * v * Math.exp(-M * v * v / (2 * Rg * T));
      const vp = Math.sqrt(2 * Rg * P.T / M), vm = Math.sqrt(8 * Rg * P.T / (Math.PI * M)), vq = Math.sqrt(3 * Rg * P.T / M), vp3 = Math.sqrt(2 * Rg * 300 / M);
      const vmax = Math.max(vp, vp3) * 3.2, V = lin(0, vmax, 300), fm = Math.max(f(vp, P.T), f(vp3, 300));
      plot(c, [0, 0, w, h], { xr: [0, vmax], yr: [0, fm * 1.15], xl: 'v, m/s', yl: 'f(v), s/m', fill: [{ c: '#22d3ee22', pts: [[0, 0], ...V.map(v => [v, f(v, P.T)]), [vmax, 0]] }], series: [{ pts: V.map(v => [v, f(v, 300)]), c: '#64748b', dash: [6, 4] }, { pts: V.map(v => [v, f(v, P.T)]), c: C.cyan, w: 2.5 }], vl: [{ x: vp, l: 'v_eh', c: C.green }, { x: vm, l: '⟨v⟩', c: C.amber, dy: 14 }, { x: vq, l: 'v_kv', c: C.rose, dy: 28 }], legend: [{ c: C.cyan, l: `T = ${P.T} K` }, { c: '#64748b', l: 'T = 300 K' }] });
      return { 'Eng ehtimolli tezlik √(2RT/M), m/s': fx(vp, 0), 'O‘rtacha tezlik √(8RT/πM), m/s': fx(vm, 0), 'O‘rtacha kvadratik √(3RT/M), m/s': fx(vq, 0), '⟨E_k⟩ = 3kT/2, J': sci(1.5 * kB * P.T), '⟨E_k⟩, meV': fx(1.5 * kB * P.T / qe * 1e3, 1) };
    }
  };

  /* M9, M10, L15–L16 — Ideal gaz jarayonlari */
  S.gas = {
    title: 'Ideal gaz jarayonlari (p–V diagramma)', stat: 'pV = νRT',
    params: [
      { k: 'pr', l: 'Jarayon', type: 'sel', opts: ['Izotermik (T = const)', 'Izobarik (p = const)', 'Izoxorik (V = const)', 'Adiabatik (Q = 0)'], v: 'Izotermik (T = const)' },
      { k: 'x', l: 'Nisbat x = V₂/V₁ (izoxorada T₂/T₁)', min: .3, max: 3, step: .05, v: 2 },
      { k: 'i', l: 'Gaz molekulasi', type: 'sel', opts: ['Bir atomli (i = 3)', 'Ikki atomli (i = 5)', 'Ko‘p atomli (i = 6)'], v: 'Ikki atomli (i = 5)' },
      { k: 'n', l: 'Modda miqdori ν, mol', min: .1, max: 2, step: .05, v: .5 },
      { k: 'T1', l: 'Boshlang‘ich temperatura T₁, K', min: 200, max: 600, step: 5, v: 300 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), i = num(P.i, /i = (\d)/), Cv = i / 2 * Rg, Cp = Cv + Rg, gm = Cp / Cv, V1 = .01, p1 = P.n * Rg * P.T1 / V1, pr = P.pr.slice(0, 5);
      let V2 = V1, p2 = p1, T2 = P.T1, Aw = 0, pts;
      if (pr === 'Izote') { V2 = P.x * V1; p2 = p1 / P.x; Aw = P.n * Rg * P.T1 * Math.log(P.x); pts = lin(V1, V2, 80).map(V => [V, P.n * Rg * P.T1 / V]); }
      else if (pr === 'Izoba') { V2 = P.x * V1; T2 = P.x * P.T1; Aw = p1 * (V2 - V1); pts = [[V1, p1], [V2, p1]]; }
      else if (pr === 'Izoxo') { T2 = P.x * P.T1; p2 = P.x * p1; pts = [[V1, p1], [V1, p2]]; }
      else { V2 = P.x * V1; p2 = p1 * P.x ** -gm; T2 = P.T1 * P.x ** (1 - gm); Aw = P.n * Cv * (P.T1 - T2); pts = lin(V1, V2, 80).map(V => [V, p1 * (V1 / V) ** gm]); }
      const dU = P.n * Cv * (T2 - P.T1), Q = dU + Aw, Vm = Math.max(V1, V2) * 1.25e3, pm = Math.max(p1, p2) * 1.25e-3;
      const iso = T => lin(Vm * .06, Vm, 80).map(V => [V, P.n * Rg * T / (V * 1e-3) * 1e-3]);
      plot(c, [0, 0, w, h], { xr: [0, Vm], yr: [0, pm], xl: 'V, L', yl: 'p, kPa', fill: pr !== 'Izoxo' ? [{ c: Aw >= 0 ? '#34d39933' : '#fb718533', pts: [[V1 * 1e3, 0], ...pts.map(([V, p]) => [V * 1e3, p * 1e-3]), [V2 * 1e3, 0]] }] : [], series: [{ pts: iso(P.T1), c: '#334155', dash: [4, 4], w: 1 }, { pts: iso(T2), c: '#475569', dash: [4, 4], w: 1 }, { pts: pts.map(([V, p]) => [V * 1e3, p * 1e-3]), c: C.cyan, w: 3 }], marks: [{ x: V1 * 1e3, y: p1 * 1e-3, c: C.green, l: '1' }, { x: V2 * 1e3, y: p2 * 1e-3, c: C.amber, l: '2' }], legend: [{ c: C.cyan, l: P.pr.split(' (')[0] + ' jarayon' }, { c: '#475569', l: 'izotermalar T₁, T₂' }] });
      return { 'p₁, kPa': fx(p1 / 1e3, 1), 'V₂, L': fx(V2 * 1e3, 2), 'p₂, kPa': fx(p2 / 1e3, 1), 'T₂, K': fx(T2, 1), 'Gaz bajargan ish A, J': fx(Aw, 1), 'Ichki energiya o‘zgarishi ΔU, J': fx(dU, 1), 'Issiqlik miqdori Q = ΔU + A, J': fx(Q, 1), 'γ = C_p/C_V': fx(gm, 3) };
    }
  };

  /* M10, L12–L14 — Kalorimetr */
  S.calorimeter = {
    title: 'Kalorimetrda issiqlik balansi', stat: 'Q_berilgan = Q_olingan',
    params: [
      { k: 'm1', l: 'Kalorimetrdagi suv massasi m₁, g', min: 50, max: 500, step: 5, v: 200 },
      { k: 't1', l: 'Suvning boshlang‘ich temperaturasi t₁, °C', min: 0, max: 60, step: .5, v: 20 },
      { k: 'mat', l: 'Tushirilgan jism', type: 'sel', opts: ['Alyuminiy (c = 900)', 'Temir (c = 460)', 'Mis (c = 385)', 'Qo‘rg‘oshin (c = 130)', 'Issiq suv (c = 4186)'], v: 'Alyuminiy (c = 900)' },
      { k: 'm2', l: 'Jism massasi m₂, g', min: 20, max: 500, step: 5, v: 100 },
      { k: 't2', l: 'Jismning temperaturasi t₂, °C', min: 20, max: 100, step: .5, v: 100 },
      { k: 'Ck', l: 'Kalorimetrning issiqlik sig‘imi C_k, J/K', min: 0, max: 200, step: 5, v: 40 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), cw = 4186, c2 = num(P.mat, /c = (\d+)/), a1 = cw * P.m1 * 1e-3 + P.Ck, a2 = c2 * P.m2 * 1e-3, th = (a1 * P.t1 + a2 * P.t2) / (a1 + a2);
      const tau = 18, ts = lin(0, 120, 200), lo = Math.min(P.t1, P.t2) - 5, hi = Math.max(P.t1, P.t2) + 5;
      plot(c, [0, 0, w, h], { xr: [0, 120], yr: [lo, hi], xl: 'vaqt, s (sxematik)', yl: 't, °C', series: [{ pts: ts.map(t => [t, th + (P.t1 - th) * Math.exp(-t / tau)]), c: C.cyan, w: 2.5 }, { pts: ts.map(t => [t, th + (P.t2 - th) * Math.exp(-t / tau)]), c: C.rose, w: 2.5 }], hl: [{ y: th, l: `θ = ${dc(th, 1)} °C`, c: C.green }], legend: [{ c: C.cyan, l: 'suv + kalorimetr' }, { c: C.rose, l: 'tushirilgan jism' }] });
      const Q = a2 * (P.t2 - th);
      return { 'Muvozanat temperaturasi θ, °C': fx(th, 2), 'Jism bergan issiqlik Q, J': fx(Q, 0), 'Suv olgan issiqlik, J': fx(cw * P.m1 * 1e-3 * (th - P.t1), 0), 'Kalorimetr olgan issiqlik, J': fx(P.Ck * (th - P.t1), 0), 'c = (c_s m₁ + C_k)(θ − t₁) / (m₂(t₂ − θ)), J/(kg·K)': fx(a1 * (th - P.t1) / (P.m2 * 1e-3 * (P.t2 - th)), 0) };
    }
  };

  /* M11, L17 — Sirt taranglik va kapillyarlik */
  const LIQ = { 'Suv (σ = 0,073 N/m; θ = 0°)': [.0728, 998, 0], 'Etil spirti (σ = 0,022 N/m; θ = 0°)': [.0223, 789, 0], 'Glitserin (σ = 0,063 N/m; θ = 0°)': [.0634, 1261, 0], 'Simob (σ = 0,47 N/m; θ = 140°)': [.47, 13534, 140] };
  S.capillary = {
    title: 'Kapillyar hodisalar va tomchi', stat: 'h = 2σcos θ/(ρgr)',
    params: [
      { k: 'liq', l: 'Suyuqlik', type: 'sel', opts: Object.keys(LIQ), v: 'Suv (σ = 0,073 N/m; θ = 0°)' },
      { k: 'r', l: 'Kapillyar radiusi r, mm', min: .1, max: 2, step: .05, v: .5 },
      { k: 'd', l: 'Tomizgich bo‘yni diametri d, mm', min: .5, max: 4, step: .1, v: 2 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), [sg, rho, th] = LIQ[P.liq], r = P.r * 1e-3, hc = 2 * sg * Math.cos(th * deg) / (rho * g0 * r);
      const bx = w * .05, bw = w * .38, lvl = h * .62, scale = Math.min(h * .45 / 0.03, 5000);
      rect(c, bx, lvl, bw, h * .33, th > 90 ? '#94a3b8aa' : '#38bdf866'); line(c, bx, h * .95, bx + bw, h * .95, '#94a3b8', 2); line(c, bx, lvl - 40, bx, h * .95, '#94a3b8', 2); line(c, bx + bw, lvl - 40, bx + bw, h * .95, '#94a3b8', 2);
      const tx = bx + bw / 2, tw = Math.max(4, P.r * 9), top = lvl - h * .5, hp = Math.max(-h * .3, Math.min(h * .5, hc * scale));
      rect(c, tx - tw / 2, lvl - hp, tw, h * .95 - (lvl - hp) - 4, th > 90 ? '#94a3b8' : '#38bdf8');
      c.strokeStyle = '#e2e8f0'; c.lineWidth = 1.5; c.strokeRect(tx - tw / 2 - 2, top, tw + 4, h * .95 - top - 8);
      label(c, `h = ${dc((hc * 1e3), 1)} mm`, tx + tw + 8, lvl - hp / 2, hc >= 0 ? C.green : C.rose);
      const rs = lin(.1, 2, 100);
      plot(c, [w * .46, 0, w * .54, h], { xr: [.1, 2], yr: Math.cos(th * deg) > 0 ? [0, 2 * sg * Math.cos(th * deg) / (rho * g0 * 1e-4) * 1e3 * 1.05] : [2 * sg * Math.cos(th * deg) / (rho * g0 * 1e-4) * 1e3 * 1.05, 1], xl: 'r, mm', yl: 'h, mm', series: [{ pts: rs.map(x => [x, 2 * sg * Math.cos(th * deg) / (rho * g0 * x * 1e-3) * 1e3]), c: C.cyan, w: 2.5 }], marks: [{ x: P.r, y: hc * 1e3, c: C.amber }] });
      const mDrop = Math.PI * P.d * 1e-3 * sg / g0;
      return { 'Ko‘tarilish balandligi h, mm': fx(hc * 1e3, 2), 'Laplas bosimi Δp = 2σ/r, Pa': fx(2 * sg / r, 0), 'Tomchi massasi m = πdσ/g, mg': fx(mDrop * 1e6, 1), 'Ho‘llash': th < 90 ? A('ho‘llaydi (botiq menisk)') : A('ho‘llamaydi (qavariq menisk)') };
    }
  };

  /* L3, L4, M11 — Gidrostatik tortish */
  S.archimedes = {
    title: 'Gidrostatik tortish usuli', stat: 'F_A = ρ_s gV',
    params: [
      { k: 'body', l: 'Jism materiali', type: 'sel', opts: ['Alyuminiy (ρ = 2700)', 'Shisha (ρ = 2500)', 'Temir (ρ = 7870)', 'Mis (ρ = 8960)', 'Qo‘rg‘oshin (ρ = 11340)'], v: 'Alyuminiy (ρ = 2700)' },
      { k: 'V', l: 'Jism hajmi V, sm³', min: 5, max: 100, step: 1, v: 40 },
      { k: 'liq', l: 'Suyuqlik', type: 'sel', opts: ['Suv (ρ = 1000)', 'Kerosin (ρ = 800)', 'Sho‘r suv (ρ = 1030)', 'Glitserin (ρ = 1260)'], v: 'Suv (ρ = 1000)' },
      { k: 'dip', l: 'Botirilgan qism, %', min: 0, max: 100, step: 1, v: 100 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), rb = num(P.body, /ρ = (\d+)/), rl = num(P.liq, /ρ = (\d+)/), V = P.V * 1e-6;
      const P1 = rb * V * g0, FA = rl * V * g0 * P.dip / 100, P2 = P1 - FA, full = P.dip >= 100;
      const cx = w * .3, bw = 50, liqTop = h * .55, bodyH = 50, bodyTop = liqTop - bodyH * (1 - P.dip / 100);
      rect(c, cx - 120, liqTop, 240, h * .4, '#38bdf855'); line(c, cx - 120, liqTop - 30, cx - 120, h * .95, '#94a3b8', 2); line(c, cx + 120, liqTop - 30, cx + 120, h * .95, '#94a3b8', 2); line(c, cx - 120, h * .95, cx + 120, h * .95, '#94a3b8', 2);
      rect(c, cx - 14, 14, 28, 60, '#334155', '#94a3b8'); const fr = Math.min(1, P2 / Math.max(P1, 1e-9));
      line(c, cx - 10, 24 + 40 * fr, cx + 10, 24 + 40 * fr, C.amber, 3); line(c, cx, 74, cx, bodyTop, '#e2e8f0', 1.2);
      rect(c, cx - bw / 2, bodyTop, bw, bodyH, '#cbd5e1', '#f8fafc');
      arrow(c, cx + 40, bodyTop + bodyH, cx + 40, bodyTop + bodyH - Math.min(80, FA / Math.max(P1, 1e-9) * 80), C.green); label(c, 'F_A', cx + 46, bodyTop + bodyH - 30, C.green);
      label(c, `Dinamometr: ${dc(P2, 3)} N`, 16, h - 12, C.amber, 'left', 13);
      return { 'Havodagi og‘irlik P₁ = ρ_j Vg, N': fx(P1, 3), 'Arximed kuchi F_A, N': fx(FA, 3), 'Suyuqlikdagi og‘irlik P₂, N': fx(P2, 3), 'ρ_j = ρ_s·P₁/(P₁ − P₂), kg/m³': full ? fx(rl * P1 / (P1 - P2), 0) : A('— (to‘liq botiring)'), 'Jism cho‘kadimi?': rb > rl ? A('ha') : A('yo‘q, suzadi') };
    }
  };

  /* M12 — Nuqtaviy zaryadlar maydoni */
  S.coulomb = {
    title: 'Ikki nuqtaviy zaryadning maydoni', stat: 'Kulon qonuni',
    params: [
      { k: 'q1', l: '1-zaryad q₁, nC', min: -10, max: 10, step: .5, v: 5 },
      { k: 'q2', l: '2-zaryad q₂, nC', min: -10, max: 10, step: .5, v: -5 },
      { k: 'd', l: 'Zaryadlar orasidagi masofa d, sm', min: 2, max: 20, step: .5, v: 10 },
      { k: 'eps', l: 'Muhitning dielektrik singdiruvchanligi ε', min: 1, max: 81, step: 1, v: 1 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), q1 = P.q1 * 1e-9, q2 = P.q2 * 1e-9, d = P.d * 1e-2, W = w * .55, Wm = 2.6 * d, sc = W / Wm, cx = W / 2, cy = h / 2;
      const E = (x, y) => { let ex = 0, ey = 0; [[q1, -d / 2], [q2, d / 2]].forEach(([q, xq]) => { const rx = x - xq, ry = y, r2 = rx * rx + ry * ry, r = Math.sqrt(r2); if (r < 1e-6) return; const k = kC * q / (P.eps * r2 * r); ex += k * rx; ey += k * ry; }); return [ex, ey]; };
      const step = 26;
      for (let X = step / 2; X < W; X += step) for (let Y = step / 2; Y < h; Y += step) {
        const x = (X - cx) / sc, y = (cy - Y) / sc, [ex, ey] = E(x, y), m = Math.hypot(ex, ey); if (!m) continue;
        const near = Math.min(Math.hypot(x + d / 2, y), Math.hypot(x - d / 2, y)); if (near < d * .12) continue;
        const al = Math.min(1, .25 + .15 * Math.log10(m / 1e3 + 1)), ux = ex / m, uy = -ey / m;
        arrow(c, X - ux * 8, Y - uy * 8, X + ux * 8, Y + uy * 8, `rgba(34,211,238,${al})`, 1.2, 5);
      }
      [[P.q1, -d / 2], [P.q2, d / 2]].forEach(([q, xq]) => { dot(c, cx + xq * sc, cy, 11, q > 0 ? '#f43f5e' : q < 0 ? '#3b82f6' : '#64748b'); label(c, q > 0 ? '+' : q < 0 ? '−' : '0', cx + xq * sc, cy + 5, '#fff', 'center', 15); });
      const xs = lin(-1.3 * d, 1.3 * d, 400), phi = x => { let v = 0; [[q1, -d / 2], [q2, d / 2]].forEach(([q, xq]) => { const r = Math.max(Math.abs(x - xq), d * .03); v += kC * q / (P.eps * r); }); return v; };
      const pv = xs.map(x => [x * 100, phi(x) / 1e3]), lim = Math.max(...pv.map(p => Math.abs(p[1]))) * .35 || 1;
      plot(c, [W, 0, w - W, h], { xr: [-1.3 * P.d, 1.3 * P.d], yr: [-lim, lim], xl: 'x, sm (zaryadlar o‘qi)', yl: 'φ, kV', series: [{ pts: pv, c: C.amber, w: 2 }] });
      const F = kC * Math.abs(q1 * q2) / (P.eps * d * d), [emx] = E(0, 0);
      return { 'Kulon kuchi F, mN': fx(F * 1e3, 3), 'Ta’sir turi': q1 * q2 > 0 ? A('itarish') : q1 * q2 < 0 ? A('tortishish') : '—', 'O‘rtadagi maydon E, kV/m': fx(Math.abs(emx) / 1e3, 2), 'O‘rtadagi potensial φ, V': fx(phi(0), 1), 'O‘zaro ta’sir energiyasi W, mJ': fx(kC * q1 * q2 / (P.eps * d) * 1e3, 4) };
    }
  };

  /* M12, L19 — Kondensator (RC zanjir) */
  S.capacitor = {
    title: 'Kondensatorning zaryadlanishi va razryadlanishi', stat: 'τ = RC',
    params: [
      { k: 'C', l: 'Sig‘im C, mkF', min: 0, max: 3, step: .05, v: 2, log: true },
      { k: 'R', l: 'Qarshilik R, kΩ', min: -1, max: 2, step: .05, v: 1, log: true },
      { k: 'U0', l: 'Manba EYuK ε, V', min: 1, max: 24, step: .5, v: 12 },
      { k: 'mode', l: 'Jarayon', type: 'sel', opts: ['Zaryadlanish', 'Razryadlanish'], v: 'Zaryadlanish' }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), Cf = P.C * 1e-6, R = P.R * 1e3, tau = R * Cf, ch = P.mode === 'Zaryadlanish', ts = lin(0, 5 * tau, 200);
      const u = t => ch ? P.U0 * (1 - Math.exp(-t / tau)) : P.U0 * Math.exp(-t / tau), i = t => P.U0 / R * Math.exp(-t / tau) * 1e3;
      plot(c, [0, 0, w * .5, h], { xr: [0, 5 * tau], yr: [0, P.U0 * 1.1], xl: 't, s', yl: 'u_C, V', series: [{ pts: ts.map(t => [t, u(t)]), c: C.cyan, w: 2.5 }], vl: [{ x: tau, l: 'τ', c: C.amber }], hl: [{ y: P.U0 * (ch ? .632 : .368), l: ch ? '0,63ε' : '0,37ε', c: '#64748b' }] });
      plot(c, [w * .5, 0, w * .5, h], { xr: [0, 5 * tau], yr: [0, P.U0 / R * 1e3 * 1.1], xl: 't, s', yl: 'i, mA', series: [{ pts: ts.map(t => [t, i(t)]), c: C.rose, w: 2.5 }], vl: [{ x: tau, l: 'τ', c: C.amber }] });
      return { 'Vaqt doimiysi τ = RC, s': sci(tau, 3), 'Zaryad q = Cε, mC': fx(Cf * P.U0 * 1e3, 3), 'Energiya W = Cε²/2, mJ': fx(Cf * P.U0 ** 2 / 2 * 1e3, 2), 'Boshlang‘ich tok ε/R, mA': fx(P.U0 / R * 1e3, 3), 'Ikkita C ketma-ket / parallel, mkF': `${fx(P.C / 2, 1)} / ${fx(2 * P.C, 1)}` };
    }
  };

  /* M13, L20 — To'la zanjir uchun Om qonuni */
  S.circuit = {
    title: 'To‘la zanjir uchun Om qonuni', stat: 'I = ε/(R + r)',
    params: [
      { k: 'E', l: 'Manba EYuK ε, V', min: 1, max: 24, step: .5, v: 12 },
      { k: 'r', l: 'Ichki qarshilik r, Ω', min: .1, max: 5, step: .1, v: 1 },
      { k: 'R', l: 'Tashqi qarshilik R, Ω', min: .1, max: 30, step: .1, v: 5 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), I = P.E / (P.R + P.r), U = I * P.R, Pw = I * I * P.R, Pm = P.E ** 2 / (4 * P.r), Rs = lin(.1, 30, 200);
      const x1 = w * .06, x2 = w * .42, y1 = h * .2, y2 = h * .8;
      line(c, x1, y1, x2, y1, C.text, 2); line(c, x2, y2, x1, y2, C.text, 2); battery(c, x1, y1, y2, C.amber, 'ε, r'); resistor(c, x2, y1, x2, y2, C.cyan, 'R');
      dot(c, (x1 + x2) / 2, y1, 14, '#0f172a'); c.strokeStyle = C.green; c.lineWidth = 2; c.beginPath(); c.arc((x1 + x2) / 2, y1, 14, 0, 7); c.stroke(); label(c, 'A', (x1 + x2) / 2, y1 + 5, C.green, 'center', 13);
      label(c, `I = ${dc(I, 2)} A`, (x1 + x2) / 2, y1 - 22, C.green, 'center', 13); label(c, `U = ${dc(U, 2)} V`, x2 - 60, (y1 + y2) / 2 + 40, C.cyan, 'right', 13);
      plot(c, [w * .5, 0, w * .5, h], { xr: [0, 30], yr: [0, Pm * 1.15], xl: 'R, Ω', yl: 'P_tashqi, W', series: [{ pts: Rs.map(R => [R, (P.E / (R + P.r)) ** 2 * R]), c: C.cyan, w: 2.5 }], vl: [{ x: P.r, l: 'R = r', c: C.green }], marks: [{ x: P.R, y: Pw, c: C.amber }] });
      return { 'Tok kuchi I = ε/(R + r), A': fx(I, 3), 'Tashqi kuchlanish U = IR, V': fx(U, 2), 'Tashqi quvvat P = I²R, W': fx(Pw, 2), 'Maksimal quvvat ε²/4r, W': fx(Pm, 2), 'FIK η = R/(R + r)': fx(P.R / (P.R + P.r), 3), 'Qisqa tutashuv toki ε/r, A': fx(P.E / P.r, 1) };
    }
  };

  /* L22 — Kirxgof qoidalari */
  S.kirchhoff = {
    title: 'Ikki konturli zanjir', stat: 'Kirxgof qoidalari',
    params: [
      { k: 'E1', l: 'ε₁, V', min: 0, max: 12, step: .5, v: 6 },
      { k: 'E2', l: 'ε₂, V', min: 0, max: 12, step: .5, v: 6 },
      { k: 'R1', l: 'R₁, Ω', min: 1, max: 100, step: 1, v: 10 },
      { k: 'R2', l: 'R₂, Ω', min: 1, max: 100, step: 1, v: 20 },
      { k: 'R3', l: 'R₃ (o‘rta tarmoq), Ω', min: 1, max: 100, step: 1, v: 10 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), I3 = (P.E1 / P.R1 + P.E2 / P.R2) / (1 + P.R3 * (1 / P.R1 + 1 / P.R2)), I1 = (P.E1 - I3 * P.R3) / P.R1, I2 = (P.E2 - I3 * P.R3) / P.R2;
      const xa = w * .15, xb = w * .5, xc = w * .85, yt = h * .18, yb = h * .85;
      line(c, xa, yt, xc, yt, C.text, 2); line(c, xa, yb, xc, yb, C.text, 2); dot(c, xb, yt, 5, '#fff'); dot(c, xb, yb, 5, '#fff');
      battery(c, xa, yt + (yb - yt) * .55, yb, C.amber, 'ε₁'); resistor(c, xa, yt, xa, yt + (yb - yt) * .55, C.cyan, 'R₁');
      battery(c, xc, yt + (yb - yt) * .55, yb, C.amber, ''); label(c, 'ε₂', xc + 22, yt + (yb - yt) * .78, C.amber); resistor(c, xc, yt, xc, yt + (yb - yt) * .55, C.cyan, 'R₂');
      resistor(c, xb, yt, xb, yb, C.cyan, 'R₃');
      const cur = (x, I, nm, down) => { const s = (down ? 1 : -1) * Math.sign(I || 1), ym = yt + (yb - yt) * (down ? .5 : .3); arrow(c, x - 26, ym - s * 14, x - 26, ym + s * 14, C.green, 2, 7); label(c, `${nm} = ${dc((I * 1e3), 1)} mA`, x - 34, ym + 4, C.green, 'right', 12); };
      cur(xa, I1, 'I₁', false); cur(xc, I2, 'I₂', false); cur(xb, I3, 'I₃', true);
      label(c, 'Tugun: I₁ + I₂ = I₃', w * .5, h - 6, '#94a3b8', 'center', 12);
      return { 'I₁, mA': fx(I1 * 1e3, 2), 'I₂, mA': fx(I2 * 1e3, 2), 'I₃, mA': fx(I3 * 1e3, 2), '1-qoida: I₁ + I₂ − I₃, mA': fx((I1 + I2 - I3) * 1e3, 6), '2-qoida (chap kontur) ε₁ − I₁R₁ − I₃R₃, V': fx(P.E1 - I1 * P.R1 - I3 * P.R3, 6), 'Quvvat balansi ε₁I₁ + ε₂I₂ − ΣI²R, W': fx(P.E1 * I1 + P.E2 * I2 - (I1 * I1 * P.R1 + I2 * I2 * P.R2 + I3 * I3 * P.R3), 6) };
    }
  };

  /* L21 — Uitston ko'prigi (reoxordli) */
  S.wheatstone = {
    title: 'Uitston ko‘prigi (reoxord)', stat: 'R_x = R₀·l₁/l₂',
    params: [
      { k: 'Rx', l: 'Noma’lum qarshilik R_x (haqiqiy), Ω', min: 10, max: 500, step: 1, v: 120 },
      { k: 'R0', l: 'Namunaviy qarshilik R₀, Ω', min: 10, max: 500, step: 10, v: 100 },
      { k: 'l1', l: 'Sirpang‘ich holati l₁, sm (L = 100 sm)', min: 5, max: 95, step: .1, v: 50 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), Ee = 2, Rw = 5, Rg = 100, L = 100, l1 = P.l1, l2 = L - l1, r1 = Rw * l1 / L, r2 = Rw * l2 / L;
      const VD = Ee * P.R0 / (P.Rx + P.R0), VB = Ee * r2 / (r1 + r2), Rth = P.Rx * P.R0 / (P.Rx + P.R0) + r1 * r2 / (r1 + r2), Ig = (VD - VB) / (Rth + Rg);
      const xA = w * .1, xC = w * .9, yW = h * .78, yD = h * .22, xD = w * .5, xB = xA + (xC - xA) * l1 / L;
      line(c, xA, yW, xC, yW, '#f59e0b', 4); label(c, 'reoxord (L = 100 sm)', (xA + xC) / 2, yW + 22, '#94a3b8', 'center', 11);
      resistor(c, xA, yW, xD, yD, C.cyan, 'R_x'); resistor(c, xD, yD, xC, yW, C.cyan, 'R₀');
      line(c, xD, yD, xD, h * .45, C.text, 2); line(c, xD, h * .45 + 36, xB, yW, C.text, 2); dot(c, xB, yW, 6, C.green);
      c.strokeStyle = C.text; c.lineWidth = 2; c.beginPath(); c.arc(xD, h * .45 + 18, 18, 0, 7); c.stroke(); const nd = Math.max(-1, Math.min(1, Ig * 1e3 / .5)); line(c, xD, h * .45 + 28, xD + 14 * Math.sin(nd), h * .45 + 28 - 16 * Math.cos(nd), C.rose, 2.5); label(c, 'G', xD - 26, h * .45 + 22, C.text);
      line(c, xA, yW, xA, h * .95, C.text, 2); line(c, xC, yW, xC, h * .95, C.text, 2); line(c, xA, h * .95, w * .45, h * .95, C.text, 2); line(c, w * .55, h * .95, xC, h * .95, C.text, 2); line(c, w * .45, h * .95 - 10, w * .45, h * .95 + 10, C.amber, 2.5); line(c, w * .55, h * .95 - 6, w * .55, h * .95 + 6, C.amber, 4);
      label(c, `l₁ = ${dc(l1, 1)} sm`, (xA + xB) / 2, yW - 8, C.green, 'center', 11);
      const bal = Math.abs(Ig) < 1e-6;
      return { 'Galvanometr toki I_g, mkA': fx(Ig * 1e6, 2), 'l₁/l₂': fx(l1 / l2, 3), 'R_x = R₀·l₁/l₂ (o‘lchangan), Ω': fx(P.R0 * l1 / l2, 1), 'Muvozanat': bal ? A('bor ✓') : A('yo‘q — sirpang‘ichni suring'), 'Muvozanat nuqtasi l₁*, sm': fx(L * P.Rx / (P.Rx + P.R0), 1) };
    }
  };

  /* M14, L23 — Vakuum diod */
  S.vacdiode = {
    title: 'Vakuum diodning volt-amper xarakteristikasi', stat: 'I = BU^{3/2}, Richardson',
    params: [
      { k: 'U', l: 'Anod kuchlanishi U_a, V', min: 0, max: 200, step: 1, v: 80 },
      { k: 'T', l: 'Katod temperaturasi T, K', min: 1900, max: 2600, step: 10, v: 2300 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), W = 4.5, Ar = 6e5, Sk = 1e-5, B = 2e-5;
      const Is = T => Ar * T * T * Math.exp(-W / (8.617e-5 * T)) * Sk, Icl = U => B * Math.max(U, 0) ** 1.5, I = (U, T) => { const a = Icl(U), b = Is(T); return a <= 0 ? 0 : 1 / (1 / a ** 4 + 1 / b ** 4) ** .25; };
      const Us = lin(0, 200, 250), Ts = [P.T, P.T - 120, P.T - 240], cols = [C.cyan, C.violet, '#64748b'], ym = Math.max(Is(P.T), Icl(60)) * 1.15e3;
      plot(c, [0, 0, w, h], { xr: [0, 200], yr: [0, Math.min(ym, Icl(200) * 1.1e3)], xl: 'U_a, V', yl: 'I_a, mA', series: Ts.map((T, k) => ({ pts: Us.map(U => [U, I(U, T) * 1e3]), c: cols[k], w: k ? 1.6 : 2.6, dash: k ? [5, 4] : [] })).concat([{ pts: Us.map(U => [U, Icl(U) * 1e3]), c: '#334155', dash: [2, 4], w: 1 }]), marks: [{ x: P.U, y: I(P.U, P.T) * 1e3, c: C.amber }], legend: Ts.map((T, k) => ({ c: cols[k], l: `T = ${T} K` })) });
      return { 'Anod toki I_a, mA': fx(I(P.U, P.T) * 1e3, 3), 'To‘yinish toki I_to‘y, mA': fx(Is(P.T) * 1e3, 3), 'Richardson: j = AT²e^(−W/kT), A/m²': sci(Is(P.T) / Sk, 2), '“3/2” qonuni bo‘yicha tok, mA': fx(Icl(P.U) * 1e3, 3), 'Chiqish ishi W (volfram), eV': '4,5' };
    }
  };

  /* M15, L24 — Tokning magnit maydoni */
  S.bfield = {
    title: 'Tokning magnit maydoni', stat: 'Bio–Savar–Laplas',
    params: [
      { k: 'mode', l: 'Tajriba', type: 'sel', opts: ['To‘g‘ri o‘tkazgich', 'Doiraviy o‘ram markazi', 'Tangens-galvanometr'], v: 'Tangens-galvanometr' },
      { k: 'I', l: 'Tok kuchi I, A', min: 0, max: 2, step: .01, v: .3 },
      { k: 'r', l: 'Masofa / o‘ram radiusi r, sm', min: 1, max: 20, step: .5, v: 10 },
      { k: 'N', l: 'O‘ramlar soni N', min: 1, max: 100, step: 1, v: 20 },
      { k: 'Bh', l: 'Yer maydonining gorizontal tashkil etuvchisi B_g, mkT', min: 15, max: 40, step: .5, v: 26 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), r = P.r * 1e-2;
      const B = P.mode.startsWith('To‘') ? mu0 * P.I / (2 * Math.PI * r) : mu0 * P.N * P.I / (2 * r);
      const tg = P.mode.startsWith('Tangens'), phi = tg ? Math.atan(B / (P.Bh * 1e-6)) : 0, cx = w * .25, cy = h * .5;
      if (P.mode.startsWith('To‘')) {
        dot(c, cx, cy, 8, '#f59e0b'); label(c, '⊙ I', cx + 10, cy - 10, C.amber);
        [30, 60, 95, 135].forEach((R, k) => { c.strokeStyle = `rgba(34,211,238,${.9 - k * .18})`; c.lineWidth = 1.6; c.beginPath(); c.arc(cx, cy, R, 0, 7); c.stroke(); arrow(c, cx + R, cy + 2, cx + R, cy - 6, `rgba(34,211,238,${.9 - k * .18})`, 1.5, 6); });
        const rs = lin(1, 20, 120);
        plot(c, [w * .5, 0, w * .5, h], { xr: [1, 20], yr: [0, mu0 * Math.max(P.I, .01) / (2 * Math.PI * .01) * 1e6 * 1.1], xl: 'r, sm', yl: 'B, mkT', series: [{ pts: rs.map(x => [x, mu0 * P.I / (2 * Math.PI * x * 1e-2) * 1e6]), c: C.cyan, w: 2.5 }], marks: [{ x: P.r, y: B * 1e6, c: C.amber }] });
      } else {
        c.strokeStyle = '#f59e0b'; c.lineWidth = 5; c.beginPath(); c.ellipse(cx, cy, 22, Math.min(h * .42, 40 + P.r * 6), 0, 0, 7); c.stroke();
        if (tg) {
          const L = 46; c.strokeStyle = '#475569'; c.lineWidth = 1.5; c.beginPath(); c.arc(cx, cy, L + 8, 0, 7); c.stroke();
          line(c, cx, cy, cx, cy - L - 14, '#64748b', 1, [4, 4]); label(c, 'Shimol (B_g)', cx + 6, cy - L - 16, '#94a3b8', 'left', 11);
          c.save(); c.translate(cx, cy); c.rotate(phi); c.fillStyle = '#ef4444'; c.beginPath(); c.moveTo(0, -L); c.lineTo(6, 0); c.lineTo(-6, 0); c.closePath(); c.fill(); c.fillStyle = '#e2e8f0'; c.beginPath(); c.moveTo(0, L); c.lineTo(6, 0); c.lineTo(-6, 0); c.closePath(); c.fill(); c.restore();
          label(c, `φ = ${dc((phi / deg), 1)}°`, cx + L + 14, cy + 4, C.amber, 'left', 13);
        }
        const Is = lin(0, 2, 100);
        plot(c, [w * .5, 0, w * .5, h], { xr: [0, 2], yr: [0, tg ? 90 : mu0 * P.N * 2 / (2 * r) * 1e6 * 1.1], xl: 'I, A', yl: tg ? 'φ, °' : 'B, mkT', series: [{ pts: Is.map(I => [I, tg ? Math.atan(mu0 * P.N * I / (2 * r) / (P.Bh * 1e-6)) / deg : mu0 * P.N * I / (2 * r) * 1e6]), c: C.cyan, w: 2.5 }], marks: [{ x: P.I, y: tg ? phi / deg : B * 1e6, c: C.amber }] });
      }
      const out = { 'Magnit induksiya B, mkT': fx(B * 1e6, 2) };
      if (tg) { out['Strelka og‘ishi φ, °'] = fx(phi / deg, 1); out['B_g = μ₀NI/(2r·tg φ), mkT'] = P.I > 0 ? fx(mu0 * P.N * P.I / (2 * r * Math.tan(phi)) * 1e6, 2) : '—'; out['Optimal o‘lchash: φ ≈ 45°, I, A'] = fx(P.Bh * 1e-6 * 2 * r / (mu0 * P.N), 3); }
      out['Elektron uchun Lorens kuchi (v = 10⁶ m/s), N'] = sci(qe * 1e6 * B, 2);
      return out;
    }
  };

  /* M16, L25 — Elektromagnit induksiya */
  S.induction = {
    title: 'G‘altakdan o‘tayotgan magnit', stat: 'ε = −N·dΦ/dt', anim: true,
    params: [
      { k: 'v', l: 'Magnit tezligi v, m/s', min: .1, max: 3, step: .05, v: 1 },
      { k: 'N', l: 'G‘altak o‘ramlari soni N', min: 50, max: 1000, step: 10, v: 300 },
      { k: 'B0', l: 'Magnit kuchi (markazdagi B₀), T', min: .05, max: .5, step: .01, v: .2 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), a = .02, xR = 5 * a, Tpass = 2 * xR / P.v;
      const Phi = x => P.B0 * Math.PI * a * a / (1 + (x / a) ** 2) ** 1.5, emf = x => 3 * P.N * P.v * P.B0 * Math.PI * x * (1 + (x / a) ** 2) ** -2.5;
      const s0 = st(cv, () => ({ t: 0 })); s0.t += dt * Math.min(1, .6 / P.v + .3); if (s0.t > Tpass + .4) s0.t = 0;
      const xm = -xR + P.v * Math.min(s0.t, Tpass), em = emf(xm), emax = 2.70 * P.N * P.v * P.B0 * a;
      const cx = w * .22, cy = h * .45, scx = (w * .36) / (2 * xR);
      for (let k = -4; k <= 4; k++) { c.strokeStyle = '#f59e0b'; c.lineWidth = 2; c.beginPath(); c.ellipse(cx + k * 7, cy, 6, 38, 0, 0, 7); c.stroke(); }
      const mx = cx + xm * scx; rect(c, mx - 34, cy - 12, 34, 24, '#ef4444'); rect(c, mx, cy - 12, 34, 24, '#3b82f6'); label(c, 'N', mx - 17, cy + 5, '#fff', 'center', 13); label(c, 'S', mx + 17, cy + 5, '#fff', 'center', 13);
      const gx = cx, gy = h * .82; c.strokeStyle = C.text; c.lineWidth = 2; c.beginPath(); c.arc(gx, gy, 26, Math.PI, 0); c.stroke();
      const ang = Math.max(-1.2, Math.min(1.2, em / emax * 1.2)); line(c, gx, gy, gx + 24 * Math.sin(ang), gy - 24 * Math.cos(ang), C.rose, 2.5); label(c, 'G', gx, gy + 16, C.text, 'center');
      const ts = lin(0, Tpass, 200);
      plot(c, [w * .45, 0, w * .55, h * .5], { xr: [0, Tpass], yr: [0, Phi(0) * 1e3 * 1.15], xl: '', yl: 'Φ, mWb', series: [{ pts: ts.map(t => [t, Phi(-xR + P.v * t) * 1e3]), c: C.cyan, w: 2 }], marks: [{ x: Math.min(s0.t, Tpass), y: Phi(xm) * 1e3, c: C.amber }] });
      plot(c, [w * .45, h * .5, w * .55, h * .5], { xr: [0, Tpass], yr: [-emax * 1.2, emax * 1.2], xl: 't, s', yl: 'ε, V', series: [{ pts: ts.map(t => [t, emf(-xR + P.v * t)]), c: C.rose, w: 2 }], marks: [{ x: Math.min(s0.t, Tpass), y: em, c: C.amber }] });
      return { 'Oniy EYuK ε, V': fx(em, 3), 'Maksimal EYuK ε_max, V': fx(emax, 3), 'Maksimal oqim Φ_max, mWb': fx(Phi(0) * 1e3, 4), 'O‘tish vaqti, s': fx(Tpass, 3), 'Lens qoidasi': A('induksion tok magnit harakatiga qarshilik qiladi') };
    }
  };

  /* M17 — Tebranish konturi va rezonans */
  S.rlc = {
    title: 'Tebranish konturi: erkin tebranish va rezonans', stat: 'T = 2π√(LC)',
    params: [
      { k: 'L', l: 'Induktivlik L, mH', min: 0, max: 2, step: .05, v: 1, log: true },
      { k: 'C', l: 'Sig‘im C, mkF', min: -1, max: 2, step: .05, v: 0, log: true },
      { k: 'R', l: 'Aktiv qarshilik R, Ω', min: 0, max: 100, step: .5, v: 2 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), L = P.L * 1e-3, Cf = P.C * 1e-6, w0 = 1 / Math.sqrt(L * Cf), be = P.R / (2 * L), T0 = 2 * Math.PI / w0, under = w0 > be;
      const g = Math.sqrt(Math.abs(be * be - w0 * w0)), wd = Math.sqrt(Math.max(w0 * w0 - be * be, 0));
      const q = t => under ? Math.exp(-be * t) * (Math.cos(wd * t) + be / wd * Math.sin(wd * t)) : g < 1e-9 ? (1 + be * t) * Math.exp(-be * t) : Math.exp(-be * t) * (Math.cosh(g * t) + be / g * Math.sinh(g * t));
      const ts = lin(0, 6 * T0, 400);
      plot(c, [0, 0, w * .5, h], { xr: [0, 6 * T0 * 1e3], yr: [-1.15, 1.15], xl: 't, ms', yl: 'q / q₀', series: [{ pts: ts.map(t => [t * 1e3, q(t)]), c: C.cyan, w: 2 }, ...(be > 0 ? [{ pts: ts.map(t => [t * 1e3, Math.exp(-be * t)]), c: '#64748b', dash: [5, 4] }] : [])] });
      const Re = Math.max(P.R, .2), fr = lin(.05, 2.5, 400), Ir = x => { const om = x * w0; return Re / Math.sqrt(Re * Re + (om * L - 1 / (om * Cf)) ** 2); };
      plot(c, [w * .5, 0, w * .5, h], { xr: [0, 2.5], yr: [0, 1.1], xl: 'ω / ω₀', yl: 'I / I_max (majburiy tebranish)', series: [{ pts: fr.map(x => [x, Ir(x)]), c: C.rose, w: 2.5 }], vl: [{ x: 1, l: 'rezonans', c: C.green }] });
      return { 'Tomson formulasi T = 2π√(LC), ms': fx(T0 * 1e3, 3), 'Xususiy chastota f₀, Hz': fx(1 / T0, 1), 'So‘nish koeffitsiyenti β = R/2L, 1/s': fx(be, 1), 'Asllik Q = (1/R)√(L/C)': P.R > 0 ? fx(Math.sqrt(L / Cf) / P.R, 1) : '∞', 'To‘lqin qarshiligi √(L/C), Ω': fx(Math.sqrt(L / Cf), 1), 'Rejim': under ? A('so‘nuvchi tebranish') : A('aperiodik (tebranishsiz)') };
    }
  };

  /* M18 — O'zgaruvchan tok zanjiri */
  S.ac = {
    title: 'Ketma-ket RLC zanjiri: faza va quvvat', stat: 'Z = √(R² + (X_L − X_C)²)',
    params: [
      { k: 'f', l: 'Chastota f, Hz', min: 10, max: 500, step: 1, v: 50 },
      { k: 'R', l: 'Aktiv qarshilik R, Ω', min: 1, max: 200, step: 1, v: 40 },
      { k: 'L', l: 'Induktivlik L, mH', min: 0, max: 500, step: 5, v: 200 },
      { k: 'C', l: 'Sig‘im C, mkF', min: 5, max: 500, step: 5, v: 100 },
      { k: 'U', l: 'Kuchlanishning ta’sir etuvchi qiymati U, V', min: 1, max: 230, step: 1, v: 220 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), om = 2 * Math.PI * P.f, XL = om * P.L * 1e-3, XC = 1 / (om * P.C * 1e-6), Z = Math.hypot(P.R, XL - XC), I = P.U / Z, ph = Math.atan2(XL - XC, P.R);
      const T = 1 / P.f, ts = lin(0, 2 * T, 300);
      plot(c, [0, 0, w * .58, h], { xr: [0, 2 * T * 1e3], yr: [-1.2, 1.2], xl: 't, ms', yl: 'u / U_m, i / I_m', series: [{ pts: ts.map(t => [t * 1e3, Math.sin(om * t)]), c: C.cyan, w: 2.2 }, { pts: ts.map(t => [t * 1e3, Math.sin(om * t - ph)]), c: C.rose, w: 2.2 }], legend: [{ c: C.cyan, l: 'kuchlanish u(t)' }, { c: C.rose, l: 'tok i(t)' }] });
      const ox = w * .66, oy = h * .55, UR = I * P.R, UL = I * XL, UC = I * XC, m = Math.max(UR, UL, UC, P.U) || 1, s = Math.min(w * .3, h * .4) / m;
      line(c, ox - 10, oy, w - 10, oy, '#334155', 1); arrow(c, ox, oy, ox + UR * s, oy, C.green); label(c, 'U_R', ox + UR * s - 10, oy + 16, C.green);
      arrow(c, ox + UR * s, oy, ox + UR * s, oy - UL * s, C.amber); label(c, 'U_L', ox + UR * s + 6, oy - UL * s + 10, C.amber);
      arrow(c, ox + UR * s, oy - UL * s, ox + UR * s, oy - (UL - UC) * s, C.violet); label(c, 'U_C', ox + UR * s + 6, oy - (UL - UC / 2) * s, C.violet);
      arrow(c, ox, oy, ox + UR * s, oy - (UL - UC) * s, C.cyan, 2.6); label(c, `U, φ = ${dc((ph / deg), 1)}°`, ox + 4, oy + 32, C.cyan);
      return { 'X_L = ωL, Ω': fx(XL, 1), 'X_C = 1/(ωC), Ω': fx(XC, 1), 'To‘la qarshilik Z, Ω': fx(Z, 1), 'Tok I = U/Z, A': fx(I, 3), 'Faza siljishi φ, °': fx(ph / deg, 1), 'Quvvat koeffitsiyenti cos φ': fx(Math.cos(ph), 3), 'Aktiv quvvat P = UIcos φ, W': fx(P.U * I * Math.cos(ph), 1), 'Rezonans chastotasi f₀, Hz': fx(1 / (2 * Math.PI * Math.sqrt(P.L * 1e-3 * P.C * 1e-6)), 1) };
    }
  };

  /* M19 — Yung tajribasi */
  S.young = {
    title: 'Ikki tirqishdan interferensiya (Yung tajribasi)', stat: 'Δy = λL/d',
    params: [
      { k: 'lam', l: 'To‘lqin uzunligi λ, nm', min: 380, max: 750, step: 1, v: 600 },
      { k: 'd', l: 'Tirqishlar orasidagi masofa d, mm', min: .1, max: 1, step: .01, v: .5 },
      { k: 'L', l: 'Ekrangacha masofa L, m', min: .5, max: 3, step: .05, v: 1 },
      { k: 'b', l: 'Tirqish kengligi b, mm', min: .02, max: .1, step: .005, v: .05 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), lam = P.lam * 1e-9, d = P.d * 1e-3, b = P.b * 1e-3, Y = 15e-3;
      const I = y => { const s = y / Math.hypot(y, P.L), a = Math.PI * d * s / lam, be = Math.PI * b * s / lam; const sinc = Math.abs(be) < 1e-9 ? 1 : Math.sin(be) / be; return Math.cos(a) ** 2 * sinc * sinc; };
      const N = Math.floor(w), top = 10, hb = h * .28;
      for (let i = 0; i < N; i++) { const y = -Y + 2 * Y * i / N; c.fillStyle = wl2rgb(P.lam, Math.min(1, I(y) * 1.1)); c.fillRect(i, top, 1, hb); }
      const ys = lin(-Y, Y, 1200);
      plot(c, [0, top + hb, w, h - top - hb], { xr: [-15, 15], yr: [0, 1.05], xl: 'y, mm (ekranda)', yl: 'I / I₀', series: [{ pts: ys.map(y => [y * 1e3, I(y)]), c: wl2rgb(P.lam), w: 2 }, { pts: ys.map(y => { const s = y / Math.hypot(y, P.L), be = Math.PI * b * s / lam; return [y * 1e3, Math.abs(be) < 1e-9 ? 1 : (Math.sin(be) / be) ** 2]; }), c: '#64748b', dash: [5, 4], w: 1 }] });
      const dy = lam * P.L / d;
      return { 'Polosalar kengligi Δy = λL/d, mm': fx(dy * 1e3, 3), 'Markaziy difraksion maksimum kengligi 2λL/b, mm': fx(2 * lam * P.L / b * 1e3, 2), 'Undagi polosalar soni ≈ 2d/b': fx(2 * d / b, 0), 'Rang': P.lam < 450 ? A('binafsha') : P.lam < 495 ? A('ko‘k') : P.lam < 570 ? A('yashil') : P.lam < 590 ? A('sariq') : P.lam < 620 ? A('to‘q sariq') : A('qizil') };
    }
  };

  /* M20, L30 — Difraksion panjara */
  S.grating = {
    title: 'Difraksion panjara', stat: 'd·sin θ = kλ',
    params: [
      { k: 'lam', l: 'To‘lqin uzunligi λ, nm', min: 380, max: 750, step: 1, v: 532 },
      { k: 'n', l: '1 mm dagi shtrixlar soni', min: 50, max: 1200, step: 10, v: 300 },
      { k: 'N', l: 'Yoritilgan shtrixlar soni (namoyish uchun)', min: 2, max: 40, step: 1, v: 12 },
      { k: 'L', l: 'Panjaradan ekrangacha L, m', min: .2, max: 1.5, step: .05, v: .5 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), lam = P.lam * 1e-9, d = 1e-3 / P.n, b = d / 3, N = P.N;
      const I = s => { const ph = Math.PI * d * s / lam, be = Math.PI * b * s / lam, sinc = Math.abs(be) < 1e-9 ? 1 : Math.sin(be) / be, den = Math.sin(ph); const grt = Math.abs(den) < 1e-9 ? N * N : (Math.sin(N * ph) / den) ** 2; return sinc * sinc * grt / (N * N); };
      const ss = lin(-1, 1, 4000);
      plot(c, [0, 0, w, h * .72], { xr: [-1, 1], yr: [0, 1.05], xl: 'sin θ', yl: 'I / I₀', series: [{ pts: ss.map(s => [s, I(s)]), c: wl2rgb(P.lam), w: 1.6 }] });
      const kmax = Math.floor(d / lam), th = k => Math.asin(k * lam / d);
      const y0 = h * .8, X = s => 54 + (s + 1) / 2 * (w - 66);
      rect(c, 54, y0, w - 66, h * .14, '#020617');
      for (let k = -kmax; k <= kmax; k++) { const s = k * lam / d; line(c, X(s), y0, X(s), y0 + h * .14, wl2rgb(P.lam), 3); if (Math.abs(k) <= 6) label(c, String(k), X(s), y0 - 4, '#94a3b8', 'center', 10); }
      return { 'Panjara davri d, mkm': fx(d * 1e6, 3), '1-tartib burchagi θ₁, °': kmax >= 1 ? fx(th(1) / deg, 2) : '—', '2-tartib burchagi θ₂, °': kmax >= 2 ? fx(th(2) / deg, 2) : '—', 'Eng katta tartib k_max = [d/λ]': String(kmax), 'Ekranda 1-tartib x₁ = L·tg θ₁, sm': kmax >= 1 ? fx(P.L * Math.tan(th(1)) * 100, 2) : '—', 'Ajrata olish R = kN (k = 1, N = 10⁴)': '10000' };
    }
  };

  /* M21 — Qutblanish */
  S.malus = {
    title: 'Malyus qonuni va Bryuster burchagi', stat: 'I = I₀cos²φ',
    params: [
      { k: 'phi', l: 'Qutblagich va analizator orasidagi burchak φ, °', min: 0, max: 180, step: 1, v: 30 },
      { k: 'n', l: 'Ikkinchi muhit sindirish ko‘rsatkichi n', min: 1.1, max: 2.5, step: .01, v: 1.5 },
      { k: 'th', l: 'Tushish burchagi θ, °', min: 0, max: 89, step: 1, v: 56 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), ps = lin(0, 180, 181);
      plot(c, [0, 0, w * .5, h], { xr: [0, 180], yr: [0, 1.05], xl: 'φ, °', yl: 'I / I₀', series: [{ pts: ps.map(p => [p, Math.cos(p * deg) ** 2]), c: C.cyan, w: 2.5 }], marks: [{ x: P.phi, y: Math.cos(P.phi * deg) ** 2, c: C.amber }] });
      const F = th => { const t = th * deg, ct = Math.sqrt(Math.max(0, 1 - (Math.sin(t) / P.n) ** 2)), ci = Math.cos(t), rs = (ci - P.n * ct) / (ci + P.n * ct), rp = (P.n * ci - ct) / (P.n * ci + ct); return [rs * rs, rp * rp]; };
      const ts = lin(0, 89.9, 300), thB = Math.atan(P.n) / deg, [Rs, Rp] = F(P.th);
      plot(c, [w * .5, 0, w * .5, h], { xr: [0, 90], yr: [0, 1.02], xl: 'θ, °', yl: 'Qaytish koeffitsiyenti R', series: [{ pts: ts.map(t => [t, F(t)[0]]), c: C.rose, w: 2.2 }, { pts: ts.map(t => [t, F(t)[1]]), c: C.green, w: 2.2 }], vl: [{ x: thB, l: `θ_B = ${dc(thB, 1)}°`, c: C.amber }], marks: [{ x: P.th, y: Rs, c: C.rose }, { x: P.th, y: Rp, c: C.green }], legend: [{ c: C.rose, l: 'R_s (⊥ tebranish)' }, { c: C.green, l: 'R_p (∥ tebranish)' }] });
      return { 'I / I₀ = cos²φ': fx(Math.cos(P.phi * deg) ** 2, 3), 'Tabiiy yorug‘lik: I = (I₀/2)cos²φ': fx(Math.cos(P.phi * deg) ** 2 / 2, 3), 'Bryuster burchagi θ_B = arctg n, °': fx(thB, 2), 'R_s(θ)': fx(Rs, 4), 'R_p(θ)': fx(Rp, 4), 'Qaytgan nur qutblanish darajasi': fx(Math.abs(Rs - Rp) / (Rs + Rp || 1), 3) };
    }
  };

  /* M22, L27, L29 — Yupqa linza */
  S.lens = {
    title: 'Yupqa linzada tasvir yasash', stat: '1/d + 1/d′ = 1/f',
    params: [
      { k: 'f', l: 'Fokus masofasi f, sm (manfiy — sochuvchi)', min: -30, max: 30, step: 1, v: 15 },
      { k: 'd', l: 'Buyumdan linzagacha d, sm', min: 4, max: 80, step: 1, v: 40 },
      { k: 'hb', l: 'Buyum balandligi h, sm', min: 1, max: 5, step: .5, v: 3 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), f = Math.abs(P.f) < 2 ? (P.f < 0 ? -2 : 2) : P.f, d = P.d, hb = P.hb;
      const dp = Math.abs(d - f) < 1e-9 ? Infinity : f * d / (d - f), Gm = -dp / d, hp = Gm * hb;
      const span = 90, cx = w * .5, cy = h * .52, sx = w / (2 * span), sy = Math.min(h * .38 / Math.max(hb, Math.min(Math.abs(hp), 12), 4), 18);
      const X = x => cx + x * sx, Y = y => cy - y * sy;
      line(c, 0, cy, w, cy, '#475569', 1);
      [[-f, 'F'], [f, 'F′'], [-2 * f, '2F'], [2 * f, '2F′']].forEach(([x, t]) => { if (Math.abs(x) < span) { dot(c, X(x), cy, 3.5, '#94a3b8'); label(c, t, X(x), cy + 16, '#94a3b8', 'center', 11); } });
      line(c, cx, Y(-h * .45 / sy), cx, Y(h * .45 / sy), '#93c5fd', 3);
      const tip = f > 0 ? 1 : -1, ly = h * .45; [[cy - ly, -1], [cy + ly, 1]].forEach(([yy, s]) => { line(c, cx, yy, cx - 8, yy - s * tip * 10, '#93c5fd', 3); line(c, cx, yy, cx + 8, yy - s * tip * 10, '#93c5fd', 3); });
      arrow(c, X(-d), cy, X(-d), Y(hb), C.green, 3);
      const xEnd = span, rays = [[Y(hb), -hb / f, C.amber], [cy, -hb / d, C.cyan], [Y(-hb * f / (d - f)), 0, C.rose]];
      rays.forEach(([yL, slope, col], k) => {
        const yLens = (cy - yL) / sy;
        if (k === 0) line(c, X(-d), Y(hb), cx, Y(hb), col, 1.6); else if (k === 1) line(c, X(-d), Y(hb), cx, cy, col, 1.6); else line(c, X(-d), Y(hb), cx, yL, col, 1.6);
        const yAt = x => yLens + slope * x; line(c, cx, yL, X(xEnd), Y(yAt(xEnd)), col, 1.6);
        if (!(dp > 0) && isFinite(dp)) line(c, cx, yL, X(dp), Y(yAt(dp)), col, 1, [5, 4]);
      });
      if (isFinite(dp) && Math.abs(dp) < span) arrow(c, X(dp), cy, X(dp), Y(hp), C.amber, dp > 0 ? 3 : 2, 9);
      const kind = !isFinite(dp) ? A('tasvir hosil bo‘lmaydi (cheksizlikda)') : A(`${dp > 0 ? 'haqiqiy' : 'mavhum'}, ${hp * hb < 0 ? 'teskari' : 'to‘g‘ri'}, ${Math.abs(Gm) > 1 ? 'kattalashgan' : Math.abs(Gm) < 1 ? 'kichiklashgan' : 'teng'}`);
      return { 'Tasvirgacha masofa d′, sm': isFinite(dp) ? fx(dp, 1) : '∞', 'Chiziqli kattalashtirish Γ = −d′/d': isFinite(Gm) ? fx(Gm, 2) : '∞', 'Tasvir balandligi h′, sm': isFinite(hp) ? fx(hp, 2) : '∞', 'Tasvir': kind, 'Optik kuch D = 1/f, dptr': fx(100 / f, 2) };
    }
  };

  /* M22, L26, L28 — Yorug'likning sinishi */
  S.snell = {
    title: 'Sinish qonuni va to‘la ichki qaytish', stat: 'n₁sin θ₁ = n₂sin θ₂',
    params: [
      { k: 'n1', l: '1-muhit sindirish ko‘rsatkichi n₁', min: 1, max: 2.4, step: .01, v: 1 },
      { k: 'n2', l: '2-muhit sindirish ko‘rsatkichi n₂', min: 1, max: 2.4, step: .01, v: 1.5 },
      { k: 'th', l: 'Tushish burchagi θ₁, °', min: 0, max: 89, step: .5, v: 40 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), t1 = P.th * deg, s2 = P.n1 * Math.sin(t1) / P.n2, tir = s2 > 1, t2 = tir ? NaN : Math.asin(s2);
      const ct = tir ? 0 : Math.cos(t2), ci = Math.cos(t1), rs = tir ? 1 : ((P.n1 * ci - P.n2 * ct) / (P.n1 * ci + P.n2 * ct)) ** 2, rp = tir ? 1 : ((P.n2 * ci - P.n1 * ct) / (P.n2 * ci + P.n1 * ct)) ** 2, Rr = (rs + rp) / 2;
      const ox = w * .5, oy = h * .5, L = Math.min(w, h) * .45;
      rect(c, 0, 0, w, oy, `rgba(56,189,248,${(P.n1 - 1) * .25})`); rect(c, 0, oy, w, h - oy, `rgba(56,189,248,${(P.n2 - 1) * .25 + .03})`); line(c, 0, oy, w, oy, '#94a3b8', 1.5); line(c, ox, 10, ox, h - 10, '#64748b', 1, [5, 4]);
      label(c, `n₁ = ${dc(P.n1, 2)}`, 14, 22, C.text); label(c, `n₂ = ${dc(P.n2, 2)}`, 14, h - 14, C.text);
      arrow(c, ox - L * Math.sin(t1), oy - L * Math.cos(t1), ox, oy, C.amber, 2.6); line(c, ox, oy, ox + L * Math.sin(t1), oy - L * Math.cos(t1), `rgba(251,191,36,${Math.max(.15, Rr)})`, 2.2);
      if (!tir) arrow(c, ox, oy, ox + L * Math.sin(t2), oy + L * Math.cos(t2), C.cyan, 2.6);
      label(c, `θ₁ = ${dc(P.th, 1)}°`, ox - 70, oy - 18, C.amber); if (!tir) label(c, `θ₂ = ${dc((t2 / deg), 1)}°`, ox + 12, oy + 34, C.cyan); else label(c, 'TO‘LA ICHKI QAYTISH', ox + 14, oy + 30, C.rose, 'left', 13);
      const crit = P.n1 > P.n2 ? Math.asin(P.n2 / P.n1) / deg : NaN;
      return { 'Sinish burchagi θ₂, °': tir ? '—' : fx(t2 / deg, 2), 'Nisbiy sindirish ko‘rsatkichi n₂₁ = n₂/n₁': fx(P.n2 / P.n1, 3), 'Kritik burchak θ_kr, °': isFinite(crit) ? fx(crit, 2) : A('— (n₁ < n₂)'), 'Qaytish koeffitsiyenti R (tabiiy yorug‘lik)': fx(Rr, 4), 'Ko‘rinma chuqurlik nisbati h/h′ ≈ n₂/n₁': fx(P.n2 / P.n1, 3), 'Yorug‘lik tezligi 2-muhitda, 10⁸ m/s': fx(c0 / P.n2 / 1e8, 3) };
    }
  };

  /* M23 — Issiqlik nurlanishi */
  S.planck = {
    title: 'Absolyut qora jism nurlanish spektri', stat: 'Plank formulasi',
    params: [{ k: 'T', l: 'Temperatura T, K', min: 1000, max: 10000, step: 50, v: 5800 }],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), B = (l, T) => 2 * hP * c0 * c0 / l ** 5 / (Math.exp(hP * c0 / (l * kB * T)) - 1) * 1e-9 * 1e-12;
      const ls = lin(100, 3000, 400), T2 = P.T * .75, T3 = P.T * 1.25, ym = B(2.898e-3 / T3, T3) * 1.1;
      const { X, py, ph } = plot(c, [0, 0, w, h], { xr: [100, 3000], yr: [0, ym], xl: 'λ, nm', yl: 'B_λ, kW/(sr·m²·nm)', series: [{ pts: ls.map(l => [l, B(l * 1e-9, T3)]), c: '#64748b', dash: [5, 4], w: 1.2 }, { pts: ls.map(l => [l, B(l * 1e-9, T2)]), c: '#475569', dash: [5, 4], w: 1.2 }, { pts: ls.map(l => [l, B(l * 1e-9, P.T)]), c: C.amber, w: 2.8 }], vl: [{ x: 2.898e6 / P.T, l: 'λ_max', c: C.green }], legend: [{ c: C.amber, l: `T = ${P.T} K` }, { c: '#64748b', l: '1,25T va 0,75T' }] });
      for (let l = 380; l <= 750; l += 2) { c.fillStyle = wl2rgb(l, .8); c.fillRect(X(l), py + ph - 8, X(l + 2) - X(l) + 1, 8); }
      const lm = 2.898e-3 / P.T * 1e9;
      return { 'Vin qonuni λ_max = b/T, nm': fx(lm, 0), 'Stefan–Bolsman R = σT⁴, MW/m²': fx(sSB * P.T ** 4 / 1e6, 2), 'Ko‘rinadigan sohadagi ulush (taxm.)': fx((() => { let s = 0, t = 0; for (let l = 100; l < 20000; l += 5) { const v = B(l * 1e-9, P.T); t += v; if (l >= 380 && l <= 750) s += v; } return s / t; })(), 3), 'Nurlanish rangi': P.T < 3500 ? A('qizg‘ish') : P.T < 5000 ? A('to‘q sariq') : P.T < 6500 ? A('oq') : A('havorang-oq') };
    }
  };

  /* M23, L31–L32 — Tashqi fotoeffekt */
  const METAL = { 'Seziy (A = 2,1 eV)': 2.1, 'Kaliy (A = 2,3 eV)': 2.3, 'Natriy (A = 2,3 eV)': 2.3, 'Rux (A = 4,3 eV)': 4.3, 'Mis (A = 4,7 eV)': 4.7, 'Platina (A = 5,6 eV)': 5.6 };
  S.photo = {
    title: 'Tashqi fotoeffekt', stat: 'hν = A + mv²/2',
    params: [
      { k: 'lam', l: 'Yorug‘lik to‘lqin uzunligi λ, nm', min: 200, max: 700, step: 1, v: 400 },
      { k: 'met', l: 'Katod materiali', type: 'sel', opts: Object.keys(METAL), v: 'Kaliy (A = 2,3 eV)' },
      { k: 'Ip', l: 'Yorug‘lik intensivligi, %', min: 0, max: 100, step: 1, v: 70 },
      { k: 'U', l: 'Anod kuchlanishi U, V', min: -5, max: 5, step: .05, v: 1 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), Aw = METAL[P.met], Eph = 1239.84 / P.lam, Uz = Math.max(0, Eph - Aw), Is = Eph > Aw ? .1 * P.Ip : 0;
      const I = U => (Is <= 0 || U <= -Uz) ? 0 : Is * (1 - Math.exp(-3 * (U + Uz) / (Uz + .3)));
      const Us = lin(-5, 5, 300);
      plot(c, [0, 0, w * .5, h], { xr: [-5, 5], yr: [0, 11], xl: 'U, V', yl: 'I, mkA', series: [{ pts: Us.map(U => [U, I(U)]), c: C.cyan, w: 2.5 }], vl: Uz > 0 ? [{ x: -Uz, l: '−U_z', c: C.rose }] : [], marks: [{ x: P.U, y: I(P.U), c: C.amber }] });
      const nus = lin(0, 1.6, 100);
      plot(c, [w * .5, 0, w * .5, h], { xr: [0, 1.6], yr: [0, 5], xl: 'ν, 10¹⁵ Hz', yl: 'U_z, V', series: Object.entries(METAL).filter((e, i, arr) => arr.findIndex(x => x[1] === e[1]) === i).map(([nm, a]) => ({ pts: nus.map(n => [n, Math.max(0, hP * n * 1e15 / qe - a)]), c: a === Aw ? C.green : '#334155', w: a === Aw ? 2.5 : 1 })), marks: [{ x: c0 / (P.lam * 1e-9) / 1e15, y: Uz, c: C.amber }] });
      const v = Math.sqrt(2 * Uz * qe / 9.109e-31);
      return { 'Foton energiyasi hν, eV': fx(Eph, 3), 'Chastota ν, 10¹⁴ Hz': fx(c0 / (P.lam * 1e-9) / 1e14, 2), 'Qizil chegara λ₀ = hc/A, nm': fx(1239.84 / Aw, 0), 'Tormozlovchi kuchlanish U_z, V': fx(Uz, 3), 'Fotoelektron E_k,max, eV': fx(Uz, 3), 'v_max, km/s': fx(v / 1e3, 0), 'Fototok I, mkA': fx(I(P.U), 2) };
    }
  };

  /* M24 — Fotometriya */
  S.photometry = {
    title: 'Fotometr: ikki manbani taqqoslash', stat: 'E = I·cos α/r²',
    params: [
      { k: 'I1', l: '1-manba yorug‘lik kuchi I₁, kd', min: 10, max: 500, step: 5, v: 100 },
      { k: 'I2', l: '2-manba yorug‘lik kuchi I₂, kd', min: 10, max: 500, step: 5, v: 25 },
      { k: 'x', l: 'Ekran holati x (1-manbadan), m', min: .1, max: 1.9, step: .01, v: 1 },
      { k: 'al', l: 'Nurlarning tushish burchagi α, °', min: 0, max: 80, step: 1, v: 0 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), D = 2, ca = Math.cos(P.al * deg), E1 = P.I1 * ca / P.x ** 2, E2 = P.I2 * ca / (D - P.x) ** 2, xs = D / (1 + Math.sqrt(P.I2 / P.I1));
      const X = x => 30 + x / D * (w - 60), yb = h * .3;
      line(c, X(0), yb + 20, X(D), yb + 20, '#475569', 4);
      dot(c, X(0), yb, 12 + P.I1 / 50, '#fde047'); dot(c, X(D), yb, 12 + P.I2 / 50, '#fde047');
      const b1 = Math.min(1, E1 / 400), b2 = Math.min(1, E2 / 400);
      rect(c, X(P.x) - 5, yb - 30, 5, 50, `rgba(255,255,255,${.15 + .85 * b1})`); rect(c, X(P.x), yb - 30, 5, 50, `rgba(255,255,255,${.15 + .85 * b2})`);
      line(c, X(xs), yb + 28, X(xs), yb + 40, C.green, 2); label(c, 'muvozanat', X(xs), yb + 52, C.green, 'center', 11);
      const xx = lin(.1, 1.9, 200);
      plot(c, [0, h * .4, w, h * .6], { xr: [0, 2], yr: [1, 1e5], logy: true, xl: 'x, m', yl: 'E, lk', series: [{ pts: xx.map(x => [x, P.I1 * ca / x ** 2]), c: C.cyan, w: 2 }, { pts: xx.map(x => [x, P.I2 * ca / (D - x) ** 2]), c: C.rose, w: 2 }], vl: [{ x: P.x, c: C.amber }], legend: [{ c: C.cyan, l: 'E₁(x)' }, { c: C.rose, l: 'E₂(x)' }] });
      return { 'E₁ = I₁cos α/x², lk': fx(E1, 1), 'E₂ = I₂cos α/(D − x)², lk': fx(E2, 1), 'Muvozanat nuqtasi x*, m': fx(xs, 3), 'I₂/I₁ = ((D − x*)/x*)²': fx(((D - xs) / xs) ** 2, 3), 'To‘la oqim Φ₁ = 4πI₁, lm': fx(4 * Math.PI * P.I1, 0) };
    }
  };

  /* M25, L33 — Vodorod atomi */
  S.bohr = {
    title: 'Vodorod atomi: sathlar va spektral chiziqlar', stat: 'Bor nazariyasi',
    params: [
      { k: 'nu', l: 'Yuqori sath n_yu', min: 2, max: 7, step: 1, v: 3 },
      { k: 'nl', l: 'Quyi sath n_q', min: 1, max: 4, step: 1, v: 2 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), RH = 1.09678e7, E = n => -13.6057 / (n * n);
      let nu = P.nu, nl = P.nl; if (nl >= nu) nl = nu - 1;
      const lam = 1 / (RH * (1 / (nl * nl) - 1 / (nu * nu))) * 1e9, Ep = E(nu) - E(nl), ser = ['Layman', 'Balmer', 'Pashen', 'Brekett'][nl - 1];
      const x0 = 50, x1 = w * .42, Y = e => h * .92 - (e + 13.6) / 13.6 * h * .82;
      for (let n = 1; n <= 7; n++) { const y = Y(E(n)); line(c, x0, y, x1, y, n === nu || n === nl ? C.amber : '#64748b', n === nu || n === nl ? 2.4 : 1.2); if (n <= 5) label(c, `n=${n}`, x1 + 6, y + 4, '#94a3b8', 'left', 10); if (n <= 3) label(c, `${dc(E(n), 2)} eV`, 8, y + 4, '#94a3b8', 'left', 10); }
      line(c, x0, Y(0), x1, Y(0), C.rose, 1, [4, 4]); label(c, '0 (ionlanish)', x1 + 6, Y(0) + 4, C.rose, 'left', 10);
      arrow(c, (x0 + x1) / 2, Y(E(nu)), (x0 + x1) / 2, Y(E(nl)), lam >= 380 && lam <= 750 ? wl2rgb(lam) : C.violet, 3);
      const sx = w * .5, sw = w * .47, Lx = l => sx + (Math.log10(l) - Math.log10(90)) / (Math.log10(2700) - Math.log10(90)) * sw, yS = h * .3, hS = h * .3;
      rect(c, sx, yS, sw, hS, '#020617'); for (let l = 380; l <= 750; l += 3) { c.fillStyle = wl2rgb(l, .25); c.fillRect(Lx(l), yS, Lx(l + 3) - Lx(l) + 1, hS); }
      [1, 2, 3, 4].forEach(q => { for (let u = q + 1; u <= q + 8; u++) { const l = 1 / (RH * (1 / (q * q) - 1 / (u * u))) * 1e9; if (l > 2700) continue; line(c, Lx(l), yS, Lx(l), yS + hS, l >= 380 && l <= 750 ? wl2rgb(l) : '#64748b', q === nl && u === nu ? 3.5 : 1.2); } });
      [[100, '100 nm'], [380, '380'], [750, '750'], [2000, '2 mkm']].forEach(([l, t]) => label(c, t, Lx(l), yS + hS + 14, '#94a3b8', 'center', 10));
      label(c, 'UB: Layman', Lx(100), yS - 8, '#94a3b8', 'left', 10); label(c, 'Balmer', Lx(450), yS - 8, '#94a3b8', 'left', 10); label(c, 'IQ: Pashen', Lx(1000), yS - 8, '#94a3b8', 'left', 10);
      return { 'Seriya': ser, 'Foton energiyasi hν, eV': fx(Ep, 3), 'To‘lqin uzunligi λ, nm': fx(lam, 1), 'Chastota ν, 10¹⁴ Hz': fx(c0 / (lam * 1e-9) / 1e14, 3), 'Orbita radiusi r_n = 0,0529n² nm (n_yu)': fx(.0529 * nu * nu, 4), 'n_yu sathdan ionlanish energiyasi, eV': fx(-E(nu), 3) };
    }
  };

  /* L33 — Frank–Gers tajribasi */
  S.franck = {
    title: 'Frank–Gers tajribasi (simob bug‘i)', stat: 'E₁ = 4,9 eV',
    params: [
      { k: 'U', l: 'Tezlatuvchi kuchlanish U, V', min: 0, max: 30, step: .1, v: 12 },
      { k: 'Ur', l: 'Tormozlovchi kuchlanish U_t, V', min: 0, max: 2, step: .05, v: .5 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), E1 = 4.9, Uc = 1.8;
      const I = U => { const ue = U - Uc; if (ue <= 0) return 0; const eps = ue % E1, base = ue ** 1.5; const s = 1 / (1 + Math.exp(-(eps - P.Ur) / .25)); return base * (.18 + .82 * s); };
      const Us = lin(0, 30, 900), ym = I(30) * 1.2 || 1;
      plot(c, [0, 0, w, h], { xr: [0, 30], yr: [0, Math.max(...Us.map(I)) * 1.1], xl: 'U, V', yl: 'I_a (nisbiy birlik)', series: [{ pts: Us.map(U => [U, I(U)]), c: C.cyan, w: 2.2 }], vl: [1, 2, 3, 4, 5].map(k => ({ x: Uc + k * E1 + P.Ur, c: '#475569' })), marks: [{ x: P.U, y: I(P.U), c: C.amber }] });
      return { 'Simobning 1-qo‘zg‘alish energiyasi E₁, eV': '4,9', 'Maksimumlar orasidagi masofa ΔU, V': '4,9', 'Nurlanish λ = hc/E₁, nm': fx(1239.84 / E1, 0), 'Kontakt potensiallar farqi (model), V': fx(Uc, 1), 'Tok I_a(U), nisbiy': fx(I(P.U) / ym, 3) };
    }
  };

  /* M26 — Radioaktiv yemirilish */
  const ISO = { 'Yod-131 (T½ = 8,02 sutka)': [8.02 * 86400, 131], 'Radon-222 (T½ = 3,82 sutka)': [3.82 * 86400, 222], 'Kobalt-60 (T½ = 5,27 yil)': [5.27 * 3.156e7, 60], 'Seziy-137 (T½ = 30,1 yil)': [30.1 * 3.156e7, 137], 'Radiy-226 (T½ = 1600 yil)': [1600 * 3.156e7, 226], 'Uglerod-14 (T½ = 5730 yil)': [5730 * 3.156e7, 14] };
  S.decay = {
    title: 'Radioaktiv yemirilish: nazariya va tasodifiy model', stat: 'N = N₀·2^(−t/T½)', anim: true,
    params: [
      { k: 'iso', l: 'Izotop', type: 'sel', opts: Object.keys(ISO), v: 'Yod-131 (T½ = 8,02 sutka)' },
      { k: 'N0', l: 'Modeldagi yadrolar soni N₀', min: 100, max: 900, step: 100, v: 400 },
      { k: 'sp', l: 'Namoyish tezligi (T½ / s)', min: .2, max: 2, step: .1, v: .6 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), [T12, M] = ISO[P.iso], lam = Math.LN2 / T12;
      const s0 = st(cv, () => ({ key: '' })); const key = [P.iso, P.N0].join();
      if (s0.key !== key) { s0.key = key; s0.t = 0; s0.life = Array.from({ length: P.N0 }, () => -Math.log(1 - Math.random()) / Math.LN2); }
      s0.t += dt * P.sp; if (s0.t > 5.2) { s0.t = 0; s0.life = s0.life.map(() => -Math.log(1 - Math.random()) / Math.LN2); }
      const n = s0.life.filter(x => x > s0.t).length, cols = Math.ceil(Math.sqrt(P.N0)), cs = Math.min(w * .4, h * .9) / cols;
      s0.life.forEach((x, i) => dot(c, 14 + (i % cols) * cs + cs / 2, 14 + Math.floor(i / cols) * cs + cs / 2, cs * .36, x > s0.t ? '#fbbf24' : '#334155'));
      const ts = lin(0, 5, 200);
      plot(c, [w * .45, 0, w * .55, h], { xr: [0, 5], yr: [0, 1.05], xl: 't / T½', yl: 'N / N₀', series: [{ pts: ts.map(t => [t, 2 ** -t]), c: C.cyan, w: 2.5 }], marks: [{ x: s0.t, y: n / P.N0, c: C.amber }], vl: [{ x: 1, l: 'T½', c: '#64748b' }] });
      const N1 = 1e-6 / (M * 1e-3) * NA;
      return { 'Yemirilish doimiysi λ = ln2/T½, 1/s': sci(lam, 3), 'O‘rtacha yashash vaqti τ = 1/λ, T½ birligida': fx(1 / Math.LN2, 3), 'Hozirgi vaqt t / T½': fx(s0.t, 2), 'Qolgan yadrolar: nazariya / model': `${Math.round(P.N0 * 2 ** -s0.t)} / ${n}`, '1 mkg izotop aktivligi A = λN, Bq': sci(lam * N1, 2) };
    }
  };

  /* M27 — Bog'lanish energiyasi */
  const EXP = [[2, 1.112, '²H'], [4, 7.074, '⁴He'], [6, 5.332, '⁶Li'], [12, 7.680, '¹²C'], [16, 7.976, '¹⁶O'], [56, 8.790, '⁵⁶Fe'], [62, 8.795, '⁶²Ni'], [90, 8.710, '⁹⁰Zr'], [120, 8.505, '¹²⁰Sn'], [208, 7.867, '²⁰⁸Pb'], [235, 7.591, '²³⁵U'], [238, 7.570, '²³⁸U']];
  S.binding = {
    title: 'Solishtirma bog‘lanish energiyasi', stat: 'Veyszekker formulasi',
    params: [{ k: 'A', l: 'Massa soni A', min: 4, max: 240, step: 1, v: 56 }],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), aV = 15.8, aS = 18.3, aC = .714, aA = 23.2;
      const Zs = A => A / (1.98 + .0155 * A ** (2 / 3)), BA = A => { const Z = Zs(A); return (aV * A - aS * A ** (2 / 3) - aC * Z * (Z - 1) / A ** (1 / 3) - aA * (A - 2 * Z) ** 2 / A) / A; };
      const As = lin(4, 240, 300);
      const { X, Y } = plot(c, [0, 0, w, h], { xr: [0, 240], yr: [0, 9.5], xl: 'A (massa soni)', yl: 'E_bog‘ / A, MeV', series: [{ pts: As.map(A => [A, BA(A)]), c: C.cyan, w: 2.5 }], marks: [{ x: P.A, y: BA(P.A), c: C.amber }], legend: [{ c: C.cyan, l: 'tomchi modeli formulasi' }, { c: '#f472b6', l: 'tajriba qiymatlari' }] });
      EXP.forEach(([A, b, t]) => { dot(c, X(A), Y(b), 4, '#f472b6'); label(c, t, X(A) + 5, Y(b) + (A === 62 ? 14 : -6), '#f9a8d4', 'left', 10); });
      const fis = 2 * 117.5 * BA(117.5) - 235 * BA(235);
      return { 'Barqaror izobar Z ≈': fx(Zs(P.A), 1), 'E_bog‘/A (formula), MeV': fx(BA(P.A), 3), 'To‘liq bog‘lanish energiyasi, MeV': fx(BA(P.A) * P.A, 0), 'Massa defekti Δm = E/c², u': fx(BA(P.A) * P.A / 931.494, 3), '²³⁵U bo‘linishida ajraladigan energiya (taxm.), MeV': fx(fis, 0) };
    }
  };

  /* ---------- Simulyator konteynerini qurish ---------- */
  function build(box) {
    const key = box.dataset.sim, sim = S[key]; if (!sim) return;
    const id = `${key}-${Math.random().toString(36).slice(2, 7)}`;
    const ctrls = sim.params.map(p => {
      if (p.type === 'sel') return `<label class="control">${A(p.l)}<select data-k="${p.k}">${p.opts.map(o => `<option value="${o}"${o === p.v ? ' selected' : ''}>${A(o)}</option>`).join('')}</select></label>`;
      return `<label class="control">${A(p.l)} <output data-o="${p.k}"></output><input type="range" data-k="${p.k}" min="${p.min}" max="${p.max}" step="${p.step}" value="${p.v}"></label>`;
    }).join('');
    box.innerHTML = `<div class="sim-layout"><div class="card controls"><h3>${A(sim.title)}</h3>${ctrls}<div class="actions"><button class="secondary" type="button" data-reset>${A('Boshlang‘ich qiymatlar')}</button></div><div class="readout" aria-live="polite"></div></div><div class="card canvas-card"><div class="toolbar"><span>${A(sim.title)}</span><span class="stat notranslate">${A(sim.stat || 'model · SI')}</span></div><canvas id="${id}" role="img" aria-label="${A(sim.title)}"></canvas></div></div>`;
    const cv = box.querySelector('canvas'), ro = box.querySelector('.readout');
    const read = () => { const P = {}; box.querySelectorAll('[data-k]').forEach(el => { const p = sim.params.find(x => x.k === el.dataset.k); P[p.k] = p.type === 'sel' ? el.value : (p.log ? 10 ** +el.value : +el.value); const o = box.querySelector(`[data-o="${p.k}"]`); if (o) o.textContent = p.log ? sci(10 ** +el.value, 1) : String(+el.value).replace('.', ','); }); return P; };
    const render = (dt) => { const r = sim.draw(cv, read(), dt || 0); ro.innerHTML = Object.entries(r || {}).map(([k, v]) => `<span>${A(k)}</span><b>${A(v)}</b>`).join(''); };
    box.addEventListener('input', () => { if (!sim.anim) render(); }); box.addEventListener('change', () => { if (!sim.anim) render(); });
    box.querySelector('[data-reset]').addEventListener('click', () => { box.querySelectorAll('[data-k]').forEach(el => { const p = sim.params.find(x => x.k === el.dataset.k); el.value = p.v; }); if (!sim.anim) render(); });
    window.addEventListener('resize', () => { if (!sim.anim) render(); });
    render();
    if (sim.anim) { let last = performance.now(), vis = true; new IntersectionObserver(e => { vis = e[0].isIntersecting; }).observe(box); const loop = now => { if (vis) render(Math.min((now - last) / 1000, .1)); last = now; requestAnimationFrame(loop); }; requestAnimationFrame(loop); }
  }
  window.YAF_SIMS = S;
  const init = () => document.querySelectorAll('.sim-box[data-sim]').forEach(build);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
