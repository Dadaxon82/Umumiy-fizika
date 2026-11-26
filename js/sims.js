/* Umumiy fizika — interaktiv modellar: mayatnik, otilgan jism, yupqa linza, radioaktiv yemirilish. */
(function () {
  'use strict';
  var A = function (s) { return window.UF ? UF.A(s) : s; };
  function css(v) { return getComputedStyle(document.documentElement).getPropertyValue(v).trim() || '#888'; }
  function fmt(x, d) { return (Math.round(x * Math.pow(10, d)) / Math.pow(10, d)).toString().replace('.', ','); }
  function P(id, name) { var el = document.querySelector('[data-p="' + id + '-' + name + '"]'); return el ? parseFloat(el.value) : 0; }
  function bind(id, cb) {
    document.querySelectorAll('[data-p^="' + id + '-"]').forEach(function (el) {
      var lab = document.querySelector('[data-v="' + el.getAttribute('data-p') + '"]');
      var upd = function () { if (lab) lab.textContent = fmt(parseFloat(el.value), 2); cb(); };
      el.addEventListener('input', upd); upd();
    });
  }
  function setup(id) {
    var c = document.querySelector('canvas[data-sim="' + id + '"]');
    if (!c) return null;
    var dpr = Math.min(window.devicePixelRatio || 1, 2), W = 900, H = 380;
    c.width = W * dpr; c.height = H * dpr;
    var g = c.getContext('2d'); g.scale(dpr, dpr);
    return { c: c, g: g, W: W, H: H, out: document.querySelector('[data-out="' + id + '"]') };
  }
  function visible(c) { var r = c.getBoundingClientRect(); return r.bottom > 0 && r.top < innerHeight; }
  function arrow(g, x1, y1, x2, y2, col) {
    g.strokeStyle = col; g.fillStyle = col; g.beginPath(); g.moveTo(x1, y1); g.lineTo(x2, y2); g.stroke();
    var a = Math.atan2(y2 - y1, x2 - x1); g.beginPath(); g.moveTo(x2, y2);
    g.lineTo(x2 - 9 * Math.cos(a - .4), y2 - 9 * Math.sin(a - .4)); g.lineTo(x2 - 9 * Math.cos(a + .4), y2 - 9 * Math.sin(a + .4)); g.fill();
  }

  /* 1. Matematik mayatnik */
  (function () {
    var s = setup('mayatnik'); if (!s) return;
    var t0 = performance.now();
    bind('mayatnik', function () { t0 = performance.now(); });
    function draw(now) {
      requestAnimationFrame(draw);
      if (!visible(s.c)) return;
      var l = P('mayatnik', 'l'), gg = P('mayatnik', 'g'), a0 = P('mayatnik', 'a') * Math.PI / 180;
      var T = 2 * Math.PI * Math.sqrt(l / gg), t = (now - t0) / 1000, th = a0 * Math.cos(2 * Math.PI * t / T);
      var g = s.g, px = 300, py = 40, L = 120 * l;
      g.clearRect(0, 0, s.W, s.H);
      g.strokeStyle = css('--border'); g.lineWidth = 6; g.beginPath(); g.moveTo(px - 70, py); g.lineTo(px + 70, py); g.stroke();
      g.setLineDash([4, 5]); g.lineWidth = 1; g.strokeStyle = css('--muted'); g.beginPath(); g.moveTo(px, py); g.lineTo(px, py + L + 30); g.stroke(); g.setLineDash([]);
      var bx = px + L * Math.sin(th), by = py + L * Math.cos(th);
      g.strokeStyle = css('--text-2'); g.lineWidth = 2; g.beginPath(); g.moveTo(px, py); g.lineTo(bx, by); g.stroke();
      g.fillStyle = css('--accent'); g.beginPath(); g.arc(bx, by, 16, 0, 7); g.fill();
      // grafik theta(t)
      var gx = 560, gy = 190, gw = 310, gh = 120;
      g.strokeStyle = css('--border'); g.lineWidth = 1; g.beginPath(); g.moveTo(gx, gy); g.lineTo(gx + gw, gy); g.moveTo(gx, gy - gh / 2 - 10); g.lineTo(gx, gy + gh / 2 + 10); g.stroke();
      g.strokeStyle = css('--accent-2'); g.lineWidth = 2; g.beginPath();
      for (var i = 0; i <= gw; i++) { var tt = t - (gw - i) / 60; var y = gy - (gh / 2) * Math.cos(2 * Math.PI * tt / T) * a0 / (40 * Math.PI / 180); i ? g.lineTo(gx + i, y) : g.moveTo(gx + i, y); }
      g.stroke();
      g.fillStyle = css('--muted'); g.font = '12px JetBrains Mono, monospace'; g.fillText('θ(t)', gx + 6, gy - gh / 2 - 14); g.fillText('t', gx + gw - 8, gy + 16);
      s.out.textContent = A('Davr T = ') + fmt(T, 3) + ' s   ·   ' + A('chastota ν = ') + fmt(1 / T, 3) + ' Hz   ·   ' + A('og‘ish θ = ') + fmt(th * 180 / Math.PI, 1) + '°';
    }
    requestAnimationFrame(draw);
  })();

  /* 2. Burchak ostida otilgan jism */
  (function () {
    var s = setup('otilish'); if (!s) return;
    var t0 = performance.now();
    bind('otilish', function () { t0 = performance.now(); });
    function draw(now) {
      requestAnimationFrame(draw);
      if (!visible(s.c)) return;
      var v = P('otilish', 'v'), al = P('otilish', 'u') * Math.PI / 180, gg = P('otilish', 'g');
      var tf = 2 * v * Math.sin(al) / gg, Lr = v * v * Math.sin(2 * al) / gg, Hm = Math.pow(v * Math.sin(al), 2) / (2 * gg);
      var x0 = 50, y0 = s.H - 40, sc = Math.min((s.W - 100) / Math.max(Lr, 1), (s.H - 80) / Math.max(Hm, 1), 12);
      var g = s.g; g.clearRect(0, 0, s.W, s.H);
      g.strokeStyle = css('--border'); g.lineWidth = 2; g.beginPath(); g.moveTo(20, y0); g.lineTo(s.W - 20, y0); g.stroke();
      g.setLineDash([5, 5]); g.strokeStyle = css('--muted'); g.lineWidth = 1.5; g.beginPath();
      for (var i = 0; i <= 120; i++) { var tt = tf * i / 120, x = v * Math.cos(al) * tt, y = v * Math.sin(al) * tt - gg * tt * tt / 2; i ? g.lineTo(x0 + x * sc, y0 - y * sc) : g.moveTo(x0, y0); }
      g.stroke(); g.setLineDash([]);
      var t = ((now - t0) / 1000) % (tf + 1); t = Math.min(t, tf);
      var bx = x0 + v * Math.cos(al) * t * sc, by = y0 - (v * Math.sin(al) * t - gg * t * t / 2) * sc;
      g.fillStyle = css('--accent'); g.beginPath(); g.arc(bx, by, 9, 0, 7); g.fill();
      var vx = v * Math.cos(al), vy = v * Math.sin(al) - gg * t;
      arrow(g, bx, by, bx + vx * 2.2, by - vy * 2.2, css('--accent-2'));
      g.fillStyle = css('--muted'); g.font = '12px JetBrains Mono, monospace';
      g.fillText('L = ' + fmt(Lr, 1) + ' m', x0 + Lr * sc - 30, y0 + 18); g.fillText('H = ' + fmt(Hm, 1) + ' m', x0 + Lr * sc / 2 - 30, y0 - Hm * sc - 12);
      s.out.textContent = A('Uchish vaqti t = ') + fmt(tf, 2) + ' s   ·   L = ' + fmt(Lr, 2) + ' m   ·   H = ' + fmt(Hm, 2) + ' m';
    }
    requestAnimationFrame(draw);
  })();

  /* 3. Yupqa linza */
  (function () {
    var s = setup('linza'); if (!s) return;
    function draw() {
      var F = P('linza', 'F') || 1, d = P('linza', 'd');
      if (Math.abs(F) < 1) F = F < 0 ? -1 : 1;
      var g = s.g, cx = s.W / 2, cy = s.H / 2, k = 9, h = 50;
      g.clearRect(0, 0, s.W, s.H);
      g.strokeStyle = css('--border'); g.lineWidth = 1; g.beginPath(); g.moveTo(10, cy); g.lineTo(s.W - 10, cy); g.stroke();
      g.strokeStyle = css('--accent'); g.lineWidth = 3; g.beginPath(); g.moveTo(cx, cy - 140); g.lineTo(cx, cy + 140); g.stroke();
      arrow(g, cx, cy, cx, cy - 145, css('--accent')); arrow(g, cx, cy, cx, cy + 145, css('--accent'));
      if (F < 0) { g.fillStyle = css('--surface'); g.fillRect(cx - 12, cy - 150, 24, 10); g.fillRect(cx - 12, cy + 140, 24, 10); arrow(g, cx, cy - 130, cx, cy - 150, css('--accent')); }
      g.fillStyle = css('--text-2'); g.font = '12px JetBrains Mono, monospace';
      [F, -F, 2 * F, -2 * F].forEach(function (f, i) { var x = cx + f * k; g.beginPath(); g.arc(x, cy, 3, 0, 7); g.fill(); g.fillText(i < 2 ? 'F' : '2F', x - 6, cy + 16); });
      var ox = cx - d * k;
      arrow(g, ox, cy, ox, cy - h, css('--text'));
      var inv = 1 / F - 1 / d, f = Math.abs(inv) < 1e-6 ? Infinity : 1 / inv, G = f / d;
      var ix = cx + f * k, ih = -h * G; // tasvir balandligi (yuqori - musbat)
      g.lineWidth = 1.5; g.strokeStyle = css('--amber');
      // 1-nur: optik o'qqa parallel -> fokus orqali
      var s1 = h / (F * k), s2 = h / (d * k); // linzadan keyingi nurlarning qiyaligi
      g.beginPath(); g.moveTo(ox, cy - h); g.lineTo(cx, cy - h); g.lineTo(cx + 600, cy - h + 600 * s1); g.stroke();
      if (f < 0) { g.setLineDash([4, 4]); g.beginPath(); g.moveTo(cx, cy - h); g.lineTo(cx - 600, cy - h - 600 * s1); g.stroke(); g.setLineDash([]); }
      // 2-nur: optik markaz orqali (sinmaydi)
      g.strokeStyle = css('--accent-2'); g.beginPath(); g.moveTo(ox, cy - h); g.lineTo(cx + 600, cy + 600 * s2); g.stroke();
      if (f < 0) { g.setLineDash([4, 4]); g.beginPath(); g.moveTo(ox, cy - h); g.lineTo(cx - 600, cy - 600 * s2); g.stroke(); g.setLineDash([]); }
      var txt;
      if (!isFinite(f)) txt = A('Buyum fokusda: tasvir hosil bo‘lmaydi (nurlar parallel).');
      else {
        g.setLineDash(f < 0 ? [5, 4] : []); arrow(g, ix, cy, ix, cy - ih, f < 0 ? css('--violet') : css('--bad')); g.setLineDash([]);
        txt = 'f = ' + fmt(f, 1) + A(' sm   ·   kattalashtirish Γ = ') + fmt(Math.abs(G), 2) + '   ·   ' +
          A(f > 0 ? 'haqiqiy, teskari' : 'mavhum, to‘g‘ri') + (Math.abs(G) > 1 ? A(', kattalashgan') : A(', kichraygan'));
      }
      s.out.textContent = txt + '   ·   D = ' + fmt(100 / F, 1) + A(' dptr');
    }
    bind('linza', draw);
    new MutationObserver(draw).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
  })();

  /* 4. Radioaktiv yemirilish */
  (function () {
    var s = setup('yemirilish'); if (!s) return;
    var N0 = 400, alive, hist, t, last;
    function reset() { alive = []; for (var i = 0; i < N0; i++) alive.push(true); hist = [[0, N0]]; t = 0; last = null; }
    reset();
    bind('yemirilish', reset);
    var rb = document.querySelector('[data-reset="yemirilish"]'); if (rb) rb.addEventListener('click', reset);
    function draw(now) {
      requestAnimationFrame(draw);
      if (!visible(s.c)) { last = null; return; }
      var T = P('yemirilish', 'T'), lam = Math.LN2 / T, dt = last ? Math.min((now - last) / 1000, .05) : 0; last = now;
      var tmax = 5 * T;
      if (t < tmax) {
        t += dt; var p = 1 - Math.exp(-lam * dt), n = 0;
        for (var i = 0; i < N0; i++) { if (alive[i] && Math.random() < p) alive[i] = false; if (alive[i]) n++; }
        hist.push([t, n]);
      }
      var g = s.g; g.clearRect(0, 0, s.W, s.H);
      for (var j = 0; j < N0; j++) {
        var x = 30 + (j % 20) * 17, y = 30 + Math.floor(j / 20) * 16;
        g.fillStyle = alive[j] ? css('--accent') : css('--border'); g.beginPath(); g.arc(x, y, 5.5, 0, 7); g.fill();
      }
      var gx = 420, gy = 340, gw = 450, gh = 300;
      g.strokeStyle = css('--border'); g.lineWidth = 1; g.beginPath(); g.moveTo(gx, gy - gh); g.lineTo(gx, gy); g.lineTo(gx + gw, gy); g.stroke();
      g.strokeStyle = css('--accent'); g.lineWidth = 2; g.beginPath();
      for (var k = 0; k <= 100; k++) { var tt = tmax * k / 100, yy = gy - gh * Math.exp(-lam * tt); k ? g.lineTo(gx + gw * k / 100, yy) : g.moveTo(gx, yy); }
      g.stroke();
      g.fillStyle = css('--bad');
      hist.forEach(function (h, i) { if (i % 3 === 0) { g.beginPath(); g.arc(gx + gw * h[0] / tmax, gy - gh * h[1] / N0, 2, 0, 7); g.fill(); } });
      g.fillStyle = css('--muted'); g.font = '12px JetBrains Mono, monospace';
      for (var m = 1; m <= 4; m++) { var xx = gx + gw * m / 5; g.fillText(m + 'T', xx - 8, gy + 16); }
      g.fillText('N/N₀', gx + 6, gy - gh - 6);
      var cur = hist[hist.length - 1][1];
      s.out.textContent = 't = ' + fmt(Math.min(t, tmax), 1) + ' s   ·   N = ' + cur + ' / ' + N0 + A('   ·   nazariya: ') + Math.round(N0 * Math.exp(-lam * Math.min(t, tmax)));
    }
    requestAnimationFrame(draw);
  })();
})();
