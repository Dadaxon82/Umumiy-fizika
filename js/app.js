/* Umumiy fizika — umumiy skript.
   Kun/tun rejimi, UZ/RU/EN (Google Translate), yangi o'zbek alifbosi (Ö, Ğ, Ş, Ç),
   formulalar (KaTeX), mundarija, menyu, "Tinglash", lug'at qidiruvi va baho kalkulyatori. */
(function () {
  'use strict';
  var html = document.documentElement;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- Til ---------- */
  function readLang() {
    var m = document.cookie.match(/(?:^|;\s*)googtrans=\/[a-z-]+\/([a-z-]+)/i);
    var l = m ? m[1].toLowerCase() : 'uz';
    return (l === 'ru' || l === 'en') ? l : 'uz';
  }
  var LANG = readLang();
  html.setAttribute('data-tl', LANG);

  function setLangCookie(l) {
    var host = location.hostname;
    var exp = l === 'uz' ? '; expires=Thu, 01 Jan 1970 00:00:00 GMT' : '';
    var val = l === 'uz' ? '' : '/uz/' + l;
    document.cookie = 'googtrans=' + val + '; path=/' + exp;
    if (host.indexOf('.') > 0) {
      document.cookie = 'googtrans=' + val + '; path=/; domain=' + host + exp;
      document.cookie = 'googtrans=' + val + '; path=/; domain=.' + host.split('.').slice(-2).join('.') + exp;
    }
  }
  $$('.lang-switch button').forEach(function (b) {
    b.setAttribute('aria-pressed', String(b.getAttribute('data-lang') === LANG));
    b.addEventListener('click', function () {
      var l = b.getAttribute('data-lang');
      if (l === LANG) return;
      setLangCookie(l);
      location.reload();
    });
  });

  /* ---------- Kun / tun ---------- */
  var themeBtn = $('#themeBtn');
  function themeIcon() {
    if (themeBtn) themeBtn.innerHTML = html.getAttribute('data-theme') === 'dark' ? '<i class="fas fa-moon"></i>' : '<i class="fas fa-sun"></i>';
  }
  themeIcon();
  if (themeBtn) themeBtn.addEventListener('click', function () {
    var next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    try { localStorage.setItem('uf-theme', next); } catch (e) { /* saqlab bo'lmadi */ }
    themeIcon();
  });

  /* ---------- Menyu (drawer) ---------- */
  var drawer = $('#drawer');
  function drawerOpen(o) { if (drawer) { drawer.classList.toggle('open', o); document.body.style.overflow = o ? 'hidden' : ''; } }
  $$('[data-drawer-open]').forEach(function (b) { b.addEventListener('click', function () { drawerOpen(true); }); });
  $$('[data-drawer-close]').forEach(function (b) { b.addEventListener('click', function () { drawerOpen(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') drawerOpen(false); });

  /* ---------- Yangi alifbo ---------- */
  var EXC = {};
  ('push pull touch match watch fresh english chip chrome chat shift search switch check chart which machine shared each such much ' +
   'schrodinger schrödinger kirchhoff michelson fischer fisher bosch zeeman cherenkov chadwick church archimedes ' +
   'technology physics chemistry sch phet tracker python geogebra desmos algodoo openstax hyperphysics hemis').split(' ')
    .forEach(function (w) { if (w) EXC[w] = 1; });
  var WORD = /[A-Za-zÀ-ž‘’ʻʼ'`]+/g;
  function wordNew(w) {
    if (EXC[w.toLowerCase().replace(/[‘’ʻʼ'`]/g, '')]) return w;
    return w.replace(/([oOgG])[‘ʻ'`’]/g, function (m, c) { return { o: 'ö', O: 'Ö', g: 'ğ', G: 'Ğ' }[c]; })
      .replace(/SH/g, 'Ş').replace(/Sh/g, 'Ş').replace(/sh/g, 'ş')
      .replace(/CH/g, 'Ç').replace(/Ch/g, 'Ç').replace(/ch/g, 'ç');
  }
  function toNew(s) {
    // $...$ formulalar o'zgarmaydi
    return String(s).split(/(\$\$[\s\S]*?\$\$|\$[^$]*\$)/).map(function (p, i) {
      return i % 2 ? p : p.replace(WORD, wordNew);
    }).join('');
  }
  function toOld(s) {
    return String(s).replace(/Ö/g, 'O‘').replace(/ö/g, 'o‘').replace(/Ğ/g, 'G‘').replace(/ğ/g, 'g‘')
      .replace(/Ş(?=[A-ZÇŞÖĞ])/g, 'SH').replace(/Ş/g, 'Sh').replace(/ş/g, 'sh')
      .replace(/Ç(?=[A-ZÇŞÖĞ])/g, 'CH').replace(/Ç/g, 'Ch').replace(/ç/g, 'ch');
  }
  var SKIP = 'script,style,code,pre,textarea,input,select,.katex,.notranslate,[data-noalif],[lang="ru"],[lang="en"]';
  function convertTree(root) {
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!/[A-Za-z]/.test(n.nodeValue)) return NodeFilter.FILTER_REJECT;
        var p = n.parentElement;
        return p && !p.closest(SKIP) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var list = [], n;
    while ((n = w.nextNode())) list.push(n);
    list.forEach(function (t) { t.nodeValue = toNew(t.nodeValue); });
    $$('[title],[aria-label],[placeholder]', root).forEach(function (el) {
      if (el.parentElement && el.parentElement.closest(SKIP)) return;
      ['title', 'aria-label', 'placeholder'].forEach(function (a) { if (el.hasAttribute(a)) el.setAttribute(a, toNew(el.getAttribute(a))); });
    });
  }
  window.UF = { toNew: toNew, toOld: toOld, lang: LANG, A: function (s) { return LANG === 'uz' ? toNew(s) : s; } };

  /* ---------- Formulalar (KaTeX) ---------- */
  function renderMath(done) {
    if (!/\$/.test(document.body.textContent)) return done();
    var finished = false;
    function fin() { if (!finished) { finished = true; done(); } }
    function css(h) { var l = document.createElement('link'); l.rel = 'stylesheet'; l.href = h; document.head.appendChild(l); }
    function js(src, cb) { var s = document.createElement('script'); s.src = src; s.onload = cb; s.onerror = fin; document.head.appendChild(s); }
    var base = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/';
    css(base + 'katex.min.css');
    js(base + 'katex.min.js', function () {
      js(base + 'contrib/auto-render.min.js', function () {
        try {
          window.renderMathInElement(document.body, {
            delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }],
            ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'input'], throwOnError: false
          });
        } catch (e) { /* formula xatosi */ }
        $$('.katex').forEach(function (k) { k.classList.add('notranslate'); k.setAttribute('translate', 'no'); });
        fin();
      });
    });
    setTimeout(fin, 4000);
  }

  /* ---------- Google Translate ---------- */
  function startTranslate() {
    if (LANG === 'uz') return;
    var el = document.createElement('div'); el.id = 'gt-el'; document.body.appendChild(el);
    window.ufGtInit = function () {
      try { new google.translate.TranslateElement({ pageLanguage: 'uz', includedLanguages: 'en,ru', autoDisplay: false }, 'gt-el'); } catch (e) { /* tarmoq yo'q */ }
    };
    var s = document.createElement('script');
    s.src = 'https://translate.google.com/translate_a/element.js?cb=ufGtInit'; s.async = true;
    document.body.appendChild(s);
  }

  renderMath(function () {
    if (LANG === 'uz') { convertTree(document.body); document.title = toNew(document.title); }
    else startTranslate();
  });

  /* ---------- Mundarija: joriy bo'limni belgilash ---------- */
  var tocLinks = $$('.toc a[href^="#"]');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting && map[e.target.id]) {
          tocLinks.forEach(function (a) { a.classList.remove('active'); });
          map[e.target.id].classList.add('active');
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px' });
    Object.keys(map).forEach(function (id) { var s = document.getElementById(id); if (s) io.observe(s); });
  }

  /* ---------- Tinglash (brauzer ovozi, Web Speech API) ---------- */
  var listenBtn = $('#listenBtn');
  var synth = window.speechSynthesis;
  var BCP = { uz: 'uz-UZ', ru: 'ru-RU', en: 'en-US' };
  var LBL = { uz: ['Tinglash', 'To‘xtatish'], ru: ['Слушать', 'Стоп'], en: ['Listen', 'Stop'] };
  if (listenBtn && !synth) listenBtn.style.display = 'none';
  if (listenBtn && synth) {
    var queue = [], idx = 0, playing = false, cur = null;
    function setLbl() {
      listenBtn.innerHTML = '<i class="fas ' + (playing ? 'fa-stop' : 'fa-volume-high') + '"></i> <span class="notranslate">' + UF.A(LBL[LANG][playing ? 1 : 0]) + '</span>';
    }
    function pickVoice() {
      var vs = synth.getVoices() || [];
      var pre = LANG;
      var v = vs.filter(function (x) { return x.lang.toLowerCase().indexOf(pre) === 0; });
      if (!v.length && LANG === 'uz') v = vs.filter(function (x) { return x.lang.toLowerCase().indexOf('tr') === 0; });
      v.sort(function (a, b) { return (/natural|neural|online/i.test(b.name) ? 1 : 0) - (/natural|neural|online/i.test(a.name) ? 1 : 0); });
      return v[0] || null;
    }
    function textOf(el) {
      var t = '';
      el.childNodes.forEach(function (n) {
        if (n.nodeType === 3) t += n.nodeValue;
        else if (n.nodeType === 1) {
          if (n.classList.contains('katex')) { var a = n.querySelector('annotation'); t += ' ' + (a ? a.textContent : '') + ' '; }
          else t += textOf(n);
        }
      });
      return t;
    }
    function stop() {
      playing = false; synth.cancel();
      if (cur) cur.classList.remove('speaking');
      cur = null; setLbl();
    }
    function next() {
      if (!playing) return;
      if (cur) cur.classList.remove('speaking');
      if (idx >= queue.length) return stop();
      cur = queue[idx++];
      cur.classList.add('speaking');
      cur.scrollIntoView({ block: 'center', behavior: 'smooth' });
      var text = textOf(cur).replace(/\s+/g, ' ').trim();
      if (LANG === 'uz') text = toOld(text);
      if (!text) return next();
      var u = new SpeechSynthesisUtterance(text);
      var v = pickVoice();
      if (v) { u.voice = v; u.lang = v.lang; } else u.lang = BCP[LANG];
      u.rate = LANG === 'uz' ? 0.95 : 1;
      u.onend = u.onerror = next;
      synth.speak(u);
    }
    function start(from) {
      queue = $$('.doc h1, .doc-sec > h2, .doc-sec h3, .doc-sec p, .doc-sec li, .page-hero h1').filter(function (e) { return e.offsetParent !== null; });
      idx = Math.max(0, queue.indexOf(from));
      playing = true; setLbl(); synth.cancel(); next();
    }
    setLbl();
    listenBtn.addEventListener('click', function () { playing ? stop() : start(); });
    var docEl = $('.doc');
    if (docEl) docEl.addEventListener('click', function (e) {
      if (!playing) return;
      var t = e.target.closest('p, li, h2, h3');
      if (t) { synth.cancel(); playing = false; start(t); }
    });
    if (synth.onvoiceschanged !== undefined) synth.onvoiceschanged = function () { };
  }

  /* ---------- Lug'at qidiruvi ---------- */
  var gs = $('#glSearch');
  if (gs) gs.addEventListener('input', function () {
    var q = toOld(gs.value.trim().toLowerCase());
    var norm = function (s) { return toOld(s.toLowerCase()).replace(/[‘’ʻʼ'`]/g, ''); };
    q = norm(q);
    $$('.gl-item').forEach(function (it) { it.style.display = !q || norm(it.textContent).indexOf(q) >= 0 ? '' : 'none'; });
  });

  /* ---------- Baho kalkulyatori ---------- */
  var calc = $('#calc');
  if (calc) {
    var out = $('#calcOut');
    var lim = { jn: [30, 18], on: [20, 12], yan: [50, 30] };
    var upd = function () {
      var v = {}, sum = 0, fails = [];
      Object.keys(lim).forEach(function (k) {
        var x = parseFloat(($('#c_' + k).value || '0').replace(',', '.')) || 0;
        x = Math.max(0, Math.min(lim[k][0], x)); v[k] = x; sum += x;
        if (x < lim[k][1]) fails.push(k.toUpperCase());
      });
      var g = sum >= 90 ? 'A’lo' : sum >= 70 ? 'Yaxshi' : sum >= 60 ? 'Qoniqarli' : 'Qoniqarsiz';
      var note = fails.length
        ? '<div class="bad">Saralash bali to‘planmagan: ' + fails.join(', ') + '. Har bir nazorat turi alohida hisoblanadi.</div>'
        : '<div class="ok">Barcha nazorat turlari bo‘yicha saralash bali to‘plangan.</div>';
      out.innerHTML = '<div>Jami: <b>' + (Math.round(sum * 10) / 10) + '</b> / 100 — <b>' + (fails.length ? 'Qoniqarsiz' : g) + '</b></div>' + note;
      if (LANG === 'uz') convertTree(out);
    };
    $$('input', calc).forEach(function (i) { i.addEventListener('input', upd); });
    upd();
  }
})();
