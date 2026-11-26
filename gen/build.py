# -*- coding: utf-8 -*-
"""Umumiy fizika — sayt generatori.

Ishlatish (repozitoriya ildizida):   python gen/build.py

Mazmun manbalari:
  gen/src/lectures/lectureN.html, gen/src/labs/labN.html, gen/src/yoriqnomalar/MT-NN.html
      — ma'ruza, laboratoriya va yo'riqnoma matnlari (<h1> + <section><h2>..</h2>..</section>)
  gen/content.py — fan dasturi ma'lumotlari, lug'at, vositalar, simulyatorlar ro'yxati
Shablon, menyu va sahifalar shu faylda. Natija: ildizdagi *.html, lectures/, labs/, yoriqnomalar/.
"""
import os, re, html
from content import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'gen', 'src')
E = html.escape
YIL = '2026'

LECT = ["Kirish", "Kinematika", "Dinamika", "Statika", "Elastiklik", "Gravitatsiya", "Gazlar qonunlari",
        "Termodinamika", "Entropiya", "Molekulyar fizika", "Elektr maydon", "Magnetizm", "Elektr o‘tkazuvchanlik",
        "Elektrodinamika", "Optika – 1", "Optika – 2", "Yorug‘lik tabiati", "Kvant fizikasi – 1", "Kvant fizikasi – 2",
        "Atom tuzilishi", "Yadro fizikasi", "Elementar zarralar fizikasi", "Kvant mexanikasi", "Yangi fizikani izlash",
        "Kosmik fizika", "Fizikada metodologiya", "Fizikada ma’lumotlar tahlili", "Xulosa"]
LECT_D = ["Fizika fanining vazifalari, o‘rganish usullari va fizik qonunlar.",
          "Yo‘l, ko‘chish, tezlik va tezlanish; harakatni tasvirlash.",
          "Kuch tushunchasi va Nyuton qonunlari.",
          "Jismlar muvozanati, kuchlar tizimi va kuch momenti.",
          "Deformatsiya turlari va Guk qonuni.",
          "Butun olam tortishish qonuni va Yerning tortish kuchi.",
          "Boyl–Mariott, Gey-Lyussak, Avogadro va ideal gaz qonunlari.",
          "Issiqlik, ish, ichki energiya va termodinamikaning birinchi qonuni.",
          "Entropiya tushunchasi va termodinamik jarayonlar yo‘nalishi.",
          "Moddaning molekulyar tuzilishi va zarralar harakati.",
          "Elektr zaryadlari, Kulon qonuni va elektrostatik maydon.",
          "Magnit maydon, uning manbalari va moddalarning magnitlanishi.",
          "Elektr toki, qarshilik va elektr zanjirlar qonunlari.",
          "Elektr va magnit maydonlarning o‘zaro bog‘liqligi, elektromagnit induksiya.",
          "Yorug‘lik tabiati, yorug‘lik tezligi va to‘lqin xossalari.",
          "Yorug‘likning qaytishi va sinishi qonunlari.",
          "Yorug‘likning to‘lqin va zarra xossalari.",
          "Kvantlash g‘oyasi va fotoeffekt.",
          "Korpuskulyar-to‘lqin dualizmi va de Broyl to‘lqinlari.",
          "Atom modellari, yadro va elektron qobiqlar.",
          "Atom yadrosi tuzilishi, yadro reaksiyalari va radioaktivlik.",
          "Elementar zarralar va standart model.",
          "To‘lqin funksiyasi va Shredinger tenglamasi.",
          "Fizikaning zamonaviy chegaralari va ochiq muammolari.",
          "Koinot obyektlari va hodisalari fizikasi.",
          "Ilmiy bilish usullari: kuzatish, tajriba, model.",
          "O‘lchash natijalarini qayta ishlash va xatoliklar tahlili.",
          "Kurs bo‘yicha umumlashtirish va yakuniy xulosalar."]
LAB_N = ["Dinamika", "Statika", "Elastiklik", "Termodinamika", "Gazlar", "Elektr zanjir", "Magnit maydon",
         "Optika", "Linzalar", "Kvantlar", "Yadro fizikasi", "Kosmik fizika"]
LAB_D = {1: "Kuchlarning ta’siri va harakat qonunlarini tajribada tekshirish.",
         2: "Kuchlar muvozanati va kuch momentini o‘lchash.",
         3: "Guk qonuni va materiallarning elastik xossalarini aniqlash."}
MT_T = {1: "Dinamika va kuchlarning ta’siri", 2: "Kinematika va grafik tahlil", 3: "Elastiklik va Guk qonuni"}
BOLIM = [(1, 6, "Mexanika"), (7, 10, "Molekulyar fizika va termodinamika"), (11, 14, "Elektr va magnetizm"),
         (15, 17, "Optika"), (18, 23, "Kvant, atom va yadro fizikasi"), (24, 28, "Zamonaviy fizika va metodologiya")]
# Saytdagi ma'ruzalarga mos interaktiv modellar: (PhET slug lar, o'z simulyatorimiz id si)
LECT_SIM = {2: (["projectile-motion"], "otilish"), 3: (["collision-lab"], None), 5: (["hookes-law"], None),
            6: (["gravity-force-lab", "gravity-and-orbits"], None), 7: (["gas-properties"], None),
            8: (["gas-properties"], None), 10: (["gas-properties"], None),
            11: (["coulombs-law", "charges-and-fields"], None), 12: (["faradays-electromagnetic-lab"], None),
            13: (["circuit-construction-kit-dc"], None), 14: (["faradays-electromagnetic-lab"], None),
            15: (["wave-interference"], None), 16: (["bending-light", "geometric-optics"], "linza"),
            17: (["wave-interference"], None), 18: (["photoelectric", "blackbody-spectrum"], None),
            20: (["rutherford-scattering", "models-of-the-hydrogen-atom"], None), 21: (["alpha-decay", "nuclear-fission"], "yemirilish")}
PHET_T = {slug: t for _, t, slug, _ in PHET}
OWN_SIM = {"mayatnik": "Matematik mayatnik", "otilish": "Burchak ostida otilgan jism", "linza": "Yupqa linzada tasvir",
           "yemirilish": "Radioaktiv yemirilish"}


def exists(rel):
    return os.path.exists(os.path.join(SRC, rel))


def bolim(n):
    for a, b, t in BOLIM:
        if a <= n <= b:
            return t
    return ''


NAV = [("Darslik haqida", "annotatsiya.html"), ("Ma’ruzalar", "index.html#maruzalar"), ("Laboratoriya", "index.html#laboratoriya"),
       ("Mustaqil ta’lim", "mustaqil.html"), ("Simulyatorlar", "simulyatorlar.html"), ("Baholash", "baholash.html"),
       ("O‘qituvchi uchun", "oqituvchi.html"), ("Lug‘at", "glossariy.html"), ("Vositalar", "vositalar.html"), ("Muallif", "index.html#muallif")]


def drawer(pre, cur):
    def a(href, txt, ok=True):
        c = ' aria-current="page"' if href == cur else ''
        return f'<a href="{pre}{href}"{c}>{E(txt)}</a>' if ok else f'<a class="soon" aria-disabled="true">{E(txt)}</a>'
    g = ['<h4>Darslik</h4>', a('index.html', 'Bosh sahifa')]
    g += [a(h, t) for t, h in NAV if '#' not in h]
    g.append('<h4>Ma’ruzalar</h4>')
    g += [a(f'lectures/lecture{i}.html', f'{i}. {t}', exists(f'lectures/lecture{i}.html')) for i, t in enumerate(LECT, 1)]
    g.append('<h4>Laboratoriya ishlari</h4>')
    g += [a(f'labs/lab{i}.html', f'L{i}. {t}', exists(f'labs/lab{i}.html')) for i, t in enumerate(LAB_N, 1)]
    g.append('<h4>Yo‘riqnomalar (MT)</h4>')
    g += [a(f'yoriqnomalar/MT-{i:02d}.html', f'MT-{i:02d}' + (f'. {MT_T[i]}' if i in MT_T else ''), exists(f'yoriqnomalar/MT-{i:02d}.html')) for i in range(1, 16)]
    return ('<div class="drawer" id="drawer" role="dialog" aria-label="Menyu"><div class="drawer-bg" data-drawer-close></div>'
            '<div class="drawer-panel"><div class="drawer-head"><span class="kicker">Mundarija</span>'
            '<button class="icon-btn" data-drawer-close aria-label="Yopish"><i class="fas fa-xmark"></i></button></div>'
            + '\n'.join(g) + '</div></div>')


def page(rel, title, body, desc='', scripts=()):
    pre = '../' * rel.count('/')
    nav = ''.join(f'<a href="{pre}{h}"' + (' aria-current="page"' if h == rel else '') + f'>{E(t)}</a>' for t, h in NAV)
    sc = ''.join(f'<script src="{pre}js/{s}"></script>' for s in scripts)
    doc = f'''<!DOCTYPE html>
<html lang="uz" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{E(title)}</title>
<meta name="description" content="{E(desc or 'Umumiy fizika — interaktiv elektron darslik')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<link rel="stylesheet" href="{pre}css/darslik.css">
<script>try{{var t=localStorage.getItem('uf-theme');if(t)document.documentElement.setAttribute('data-theme',t);var m=document.cookie.match(/googtrans=\\/[a-z-]+\\/(ru|en)/);if(m)document.documentElement.setAttribute('data-tl',m[1]);}}catch(e){{}}</script>
</head>
<body>
<a class="skip-link" href="#main">Asosiy mazmunga o‘tish</a>
<header class="topbar"><div class="topbar-inner">
<a class="brand" href="{pre}index.html"><span class="brand-icon"><i class="fas fa-atom"></i></span><span><span class="brand-title">Umumiy fizika</span><span class="brand-sub">Interaktiv elektron darslik · Bakalavriat</span></span></a>
<nav class="nav" aria-label="Asosiy menyu">{nav}</nav>
<div class="tools">
<div class="lang-switch notranslate" translate="no" role="group" aria-label="Til"><button data-lang="uz">UZ</button><button data-lang="ru">RU</button><button data-lang="en">EN</button></div>
<button class="icon-btn" id="themeBtn" aria-label="Kun / tun rejimi"><i class="fas fa-sun"></i></button>
<button class="icon-btn menu-btn" data-drawer-open aria-label="Menyu"><i class="fas fa-bars"></i></button>
</div></div></header>
{drawer(pre, rel)}
<main id="main">
{body}
</main>
<footer class="footer">© {YIL} Umumiy fizika · Qo‘qon davlat universiteti, Fizika va astronomiya kafedrasi · Fan dasturi: {FAN['kod']}, {FAN['yil']}</footer>
{sc}<script src="{pre}js/app.js"></script>
</body>
</html>
'''
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(doc)


def hero(crumbs, kicker, title, chips='', listen=True, pre=''):
    cr = ' <span>/</span> '.join(f'<a href="{pre}{h}">{E(t)}</a>' if h else E(t) for t, h in crumbs)
    lb = '<button class="btn btn-ghost listen-btn" id="listenBtn" type="button"><i class="fas fa-volume-high"></i> Tinglash</button>' if listen else ''
    return (f'<section class="page-hero"><div class="inner"><div><nav class="crumbs" aria-label="Yo‘l">{cr}</nav>'
            f'<div class="kicker">{kicker}</div><h1>{title}</h1><div class="chips">{chips}</div></div>{lb}</div></section>')


def doc_layout(sections, toc=True):
    """sections: [(id, title, inner_html, hl)]"""
    secs, links = [], []
    for i, (sid, t, inner, hl) in enumerate(sections, 1):
        secs.append(f'<section class="card doc-sec{" hl" if hl else ""}" id="{sid}"><h2><span class="n">{i}</span>{t}</h2>\n{inner}\n</section>')
        links.append(f'<a href="#{sid}">{re.sub("<[^>]+>", "", t)}</a>')
    t = f'<nav class="card toc" aria-label="Mundarija"><span class="kicker">Mundarija</span>{"".join(links)}</nav>' if toc else ''
    return f'<div class="layout{"" if toc else " wide"}">{t}<div class="doc">\n' + '\n'.join(secs)


def pager(prev, nxt):
    p = f'<a class="card" href="{prev[1]}"><span class="lbl">← Oldingi</span>{E(prev[0])}</a>' if prev else '<span></span>'
    n = f'<a class="card nx" href="{nxt[1]}"><span class="lbl">Keyingi →</span>{E(nxt[0])}</a>' if nxt else '<span></span>'
    return f'<div class="pager">{p}{n}</div>'


def slug(t, i):
    s = re.sub(r'[^a-z0-9]+', '-', t.lower().replace('‘', '').replace('’', '').replace("'", '')).strip('-')
    return (s or 's') + ('' if i is None else '')


def read_src(rel):
    s = open(os.path.join(SRC, rel), encoding='utf-8').read()
    h1 = re.search(r'<h1>(.*?)</h1>', s, re.S).group(1).strip()
    meta = re.search(r'<p class="meta">(.*?)</p>', s)
    secs, used = [], set()
    for attrs, body in re.findall(r'<section([^>]*)>(.*?)</section>', s, re.S):
        m = re.match(r'\s*<h2>(.*?)</h2>(.*)', body, re.S)
        t, inner = m.group(1).strip(), m.group(2).strip()
        sid = slug(t, None)
        while sid in used:
            sid += '-2'
        used.add(sid)
        secs.append((sid, t, inner, 'hl' in attrs))
    return h1, (meta.group(1) if meta else ''), secs


def phet_link(sl):
    return f'<a href="https://phet.colorado.edu/en/simulations/{sl}" target="_blank" rel="noopener"><span class="notranslate" translate="no">{E(PHET_T.get(sl, sl))}</span></a>'


ADAB_SEC = ('<p>Fan dasturidagi asosiy adabiyotlar:</p><ol>' + ''.join(f'<li>{E(x)}</li>' for x in ADABIYOT_ASOSIY) +
            '</ol><p>To‘liq ro‘yxat: <a href="../annotatsiya.html#adabiyotlar">Darslik haqida → Adabiyotlar</a>.</p>')


# ================= Ma'ruzalar, laboratoriyalar, yo'riqnomalar =================
def build_lectures():
    have = [i for i in range(1, 29) if exists(f'lectures/lecture{i}.html')]
    for k, i in enumerate(have):
        h1, _, secs = read_src(f'lectures/lecture{i}.html')
        if i in LECT_SIM:
            sl, own = LECT_SIM[i]
            li = ''.join(f'<li>{phet_link(s)} — PhET simulyatori (brauzerda ishlaydi)</li>' for s in sl)
            if own:
                li = f'<li><a href="../simulyatorlar.html#{own}">{OWN_SIM[own]}</a> — saytning o‘z interaktiv modeli</li>' + li
            secs.insert(len(secs) - 1 if secs and secs[-1][3] else len(secs),
                        ('model', 'Interaktiv model', f'<p>Mavzuni mustahkamlash uchun parametrlarni o‘zgartirib, natijani oldindan taxmin qiling va keyin tekshiring:</p><ul>{li}</ul>', False))
        secs.append(('adabiyotlar', 'Adabiyotlar', ADAB_SEC, False))
        chips = (f'<span class="tag notranslate" translate="no">M{i}</span><span class="tag m">2 akademik soat</span>'
                 f'<span class="tag v">Bo‘lim: {E(bolim(i))}</span>')
        if i in LECT_SIM:
            chips += '<span class="tag a">Interaktiv model</span>'
        prev = (f'{have[k-1]}-ma’ruza. {LECT[have[k-1]-1]}', f'lecture{have[k-1]}.html') if k > 0 else None
        nxt = (f'{have[k+1]}-ma’ruza. {LECT[have[k+1]-1]}', f'lecture{have[k+1]}.html') if k + 1 < len(have) else None
        body = (hero([('Bosh sahifa', 'index.html'), ('Ma’ruzalar', 'index.html#maruzalar'), (f'{i}-ma’ruza', '')],
                     f'{i}-ma’ruza · M{i}', h1, chips, pre='../')
                + doc_layout(secs) + pager(prev, nxt) + '</div></div>')
        page(f'lectures/lecture{i}.html', f'{i}-ma’ruza. {LECT[i-1]} — Umumiy fizika', body, desc=LECT_D[i-1])


def build_labs():
    have = [i for i in range(1, 13) if exists(f'labs/lab{i}.html')]
    for k, i in enumerate(have):
        h1, _, secs = read_src(f'labs/lab{i}.html')
        secs.append(('adabiyotlar', 'Adabiyotlar', ADAB_SEC, False))
        chips = f'<span class="tag notranslate" translate="no">L{i}</span><span class="tag m">2 akademik soat</span><span class="tag v">Laboratoriya ishi</span>'
        prev = (f'L{have[k-1]}. {LAB_N[have[k-1]-1]}', f'lab{have[k-1]}.html') if k > 0 else None
        nxt = (f'L{have[k+1]}. {LAB_N[have[k+1]-1]}', f'lab{have[k+1]}.html') if k + 1 < len(have) else None
        body = (hero([('Bosh sahifa', 'index.html'), ('Laboratoriya', 'index.html#laboratoriya'), (f'L{i}', '')],
                     f'{i}-laboratoriya ishi · L{i}', h1, chips, pre='../') + doc_layout(secs) + pager(prev, nxt) + '</div></div>')
        page(f'labs/lab{i}.html', f'L{i}. {LAB_N[i-1]} — Umumiy fizika', body, desc=LAB_D.get(i, ''))


def build_mt():
    have = [i for i in range(1, 16) if exists(f'yoriqnomalar/MT-{i:02d}.html')]
    for k, i in enumerate(have):
        h1, meta, secs = read_src(f'yoriqnomalar/MT-{i:02d}.html')
        secs.append(('topshirish', 'Topshirish va baholash',
                     '<p>Bajarilgan ish belgilangan muddatda <b>HEMIS</b> tizimiga yuklanadi. Joriy nazorat mezonlari: '
                     '<a href="../baholash.html#jn-rubrika">Baholash → JN rubrikasi</a>. Mustaqil ta’lim mavzulari: '
                     '<a href="../mustaqil.html">Mustaqil ta’lim</a>.</p>', True))
        chips = f'<span class="tag notranslate" translate="no">MT-{i:02d}</span><span class="tag v">Mustaqil topshiriq</span>'
        if meta:
            chips += ''.join(f'<span class="tag m">{E(x.strip())}</span>' for x in meta.split('|'))
        prev = (f'MT-{have[k-1]:02d}', f'MT-{have[k-1]:02d}.html') if k > 0 else None
        nxt = (f'MT-{have[k+1]:02d}', f'MT-{have[k+1]:02d}.html') if k + 1 < len(have) else None
        body = (hero([('Bosh sahifa', 'index.html'), ('Mustaqil ta’lim', 'mustaqil.html'), (f'MT-{i:02d}', '')],
                     f'Yo‘riqnoma · MT-{i:02d}', h1, chips, pre='../') + doc_layout(secs) + pager(prev, nxt) + '</div></div>')
        page(f'yoriqnomalar/MT-{i:02d}.html', f'MT-{i:02d}. {h1} — Umumiy fizika', body)


# ================= Fan dasturi sahifalari =================
def table(head, rows, cls=()):
    th = ''.join(f'<th{" class=c" if i in cls else ""}>{h}</th>' for i, h in enumerate(head))
    tr = ''.join('<tr>' + ''.join(f'<td{" class=c" if i in cls else ""}>{c}</td>' for i, c in enumerate(r)) + '</tr>' for r in rows)
    return f'<div class="tbl-wrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def build_annotatsiya():
    f = FAN
    info = table(['Ko‘rsatkich', 'Qiymat'], [
        ['Fan nomi', f['nomi']], ['Fan kodi', f'<span class="mono">{f["kod"]}</span>'], ['O‘quv yili', f['yil']], ['Semestr', f['semestr']],
        ['ECTS kreditlar', f['ects']], ['Fan turi', f['turi']], ['O‘qitish tili', f['til']],
        ['O‘quv rejadagi tartib raqami', f['tartib']], ['Haftalik soat', f['hafta_soat']],
        ['Umumiy yuklama', f'{f["jami"]} soat: ma’ruza — {f["maruza"]}, laboratoriya — {f["lab"]}, mustaqil ta’lim — {f["mustaqil"]} (auditoriya — {f["auditoriya"]})'],
        ['Bilim sohasi', f['bilim_sohasi']], ['Ta’lim sohasi', f['talim_sohasi']], ['Ta’lim yo‘nalishi', f['yonalish']],
        ['Fakultet / kafedra', f'{f["fakultet"]} / {f["kafedra"]}']])
    tn = ('<h3>Kasbiy kompetensiyalar</h3><ul>' + ''.join(f'<li><b class="notranslate" translate="no">{c}</b> — {E(t)}</li>' for c, k, t in TN if k == 'k') +
          '</ul><h3>Ko‘nikmalar</h3><ul>' + ''.join(f'<li><b class="notranslate" translate="no">{c}</b> — {E(t)}</li>' for c, k, t in TN if k == 'n') + '</ul>')
    mar = table(['#', 'Mavzu va mazmuni', 'Soat', 'Adabiyot'],
                [[f'<span class="mono">M{i}</span>', f'<b>{E(t)}</b><br><span style="color:var(--text-2)">{E(d)}</span>', '2', f'[{a}]']
                 for i, (t, d, a) in enumerate(MARUZA, 1)], cls=(2,))
    lab = table(['#', 'Laboratoriya mashg‘uloti mavzusi', 'Soat'], [[f'<span class="mono">L{i}</span>', E(t), '2'] for i, t in enumerate(LAB, 1)], cls=(2,))
    adab = ('<h3>Asosiy adabiyotlar</h3><ol>' + ''.join(f'<li>{E(x)}</li>' for x in ADABIYOT_ASOSIY) + '</ol>'
            '<h3>Qo‘shimcha adabiyotlar</h3><ol>' + ''.join(f'<li>{E(x)}</li>' for x in ADABIYOT_QOSHIMCHA) + '</ol>'
            '<h3>Axborot resurslari</h3><ul>' + ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, u in RESURS) + '</ul>')
    muall = ('<h3>Tuzuvchilar</h3><ul>' + ''.join(f'<li><b>{E(n)}</b> — {E(r)}</li>' for n, r in TUZUVCHI) + '</ul>'
             '<h3>Taqrizchilar</h3><ul>' + ''.join(f'<li><b>{E(n)}</b> — {E(r)}</li>' for n, r in TAQRIZCHI) + '</ul>'
             f'<p>Fan dasturi {E(f["fakultet"])} Kengashida muhokama qilingan va tasdiqlashga tavsiya etilgan; '
             f'{E(f["kafedra"])} tomonidan taqdim etilgan. Elektron imzo bilan tasdiqlangan (cams.kokandsu.uz, ID: 2397).</p>')
    secs = [('malumot', 'Fan haqida ma’lumot', info, False),
            ('maqsad', 'Maqsad va vazifalar', f'<p><b>Fanning maqsadi</b> — {E(MAQSAD)}</p><p><b>Fanning vazifasi</b> — {E(VAZIFA)}</p>', False),
            ('prerekvizit', 'Prerekvizitlar', '<ol>' + ''.join(f'<li>{E(n)} (<span class="mono">{c}</span>)</li>' for n, c in PREREKV) + '</ol>', False),
            ('natijalar', 'Ta’lim natijalari (TN)', tn, True),
            ('maruzalar', f'Ma’ruza mavzulari — {f["maruza"]} soat', '<p>Fan dasturida tasdiqlangan 27 ta ma’ruza mavzusi:</p>' + mar, False),
            ('laboratoriya', f'Laboratoriya mashg‘ulotlari — {f["lab"]} soat', lab, False),
            ('mustaqil', f'Mustaqil ta’lim — {f["mustaqil"]} soat', f'<p>45 ta mavzu bo‘yicha taqdimot tayyorlash (har biri 4 soat). To‘liq ro‘yxat va talablar: <a href="mustaqil.html">Mustaqil ta’lim</a>.</p>', False),
            ('texnologiya', 'Ta’lim texnologiyalari va usullari', '<ul>' + ''.join(f'<li>{E(x)}</li>' for x in TEXNOLOGIYA) + '</ul>', False),
            ('kredit', 'Kredit olish uchun talablar', '<p>Talaba:</p><ul>' + ''.join(f'<li>{E(x)}</li>' for x in KREDIT) +
             f'</ul><p>Fan bo‘yicha belgilangan barcha topshiriqlarni muvaffaqiyatli bajargan va baholash mezonlari asosida yetarli ball to‘plagan talabaga <b>{f["ects"]} ECTS</b> kredit beriladi. Baholash tartibi: <a href="baholash.html">Baholash</a>.</p>', True),
            ('adabiyotlar', 'Adabiyotlar va axborot resurslari', adab, False),
            ('tuzuvchilar', 'Tuzuvchilar va taqrizchilar', muall, False)]
    chips = (f'<span class="tag notranslate" translate="no">{f["kod"]}</span><span class="tag m">{f["yil"]}</span>'
             f'<span class="tag g">{f["ects"]} ECTS · {f["jami"]} soat</span><span class="tag v">{E(f["yonalish"])}</span>')
    body = hero([('Bosh sahifa', 'index.html'), ('Darslik haqida', '')], 'Darslik haqida · Fan dasturi', 'Annotatsiya, ta’lim natijalari va fan mazmuni', chips) + doc_layout(secs) + '</div></div>'
    page('annotatsiya.html', 'Darslik haqida — Umumiy fizika', body, desc='Umumiy fizika fan dasturi: maqsad, ta’lim natijalari, mavzular, adabiyotlar.')


def build_baholash():
    umum = table(['Nazorat turi', 'Maks. ball', 'Saralash bali', 'Baholash vositalari'],
                 [[f'<b>{E(n)}</b>', str(m), str(s), E(v)] for n, m, s, v in NAZORAT] + [['<b>Jami</b>', '<b>100</b>', '—', '—']], cls=(1, 2))
    baho = table(['Umumiy ball', 'Baho', 'Ta’lim natijalariga erishish tavsifi'], [[f'<span class="mono">{b}</span>', f'<b>{E(n)}</b>', E(t)] for b, n, t in BAHO])
    note = '<div class="box note"><b>Eslatma.</b> JN, ON va YaN bo‘yicha saralash talabi alohida qo‘llanadi: bir nazorat turidagi yetishmagan ball boshqa nazorat turidagi yuqori ball hisobiga qoplanmaydi.</div>'
    sym = {'+': '<span class="ok">+</span>', '-': '<span style="color:var(--muted)">—</span>'}
    mat = table(['TN', 'Baholanadigan bilim / ko‘nikma / kompetensiya', 'JN', 'ON', 'YaN'],
                [[f'<b class="notranslate" translate="no">{c}</b>', E(t), *[sym[x] for x in TN_MATRIX[c]]] for c, _, t in TN], cls=(2, 3, 4))
    mat += '<p style="color:var(--text-2);font-size:14px">Baholash vositalari: laboratoriya mashg‘uloti, mustaqil ta’lim, test, yozma ish.</p>'
    jn = table(['Mezon', 'Ball', 'Yuqori daraja', 'Yetarli daraja', 'Minimal daraja', 'Erishilmagan'],
               [[f'<b>{E(m)}</b>', str(b), E(a), E(y), E(mi), E(e)] for m, b, a, y, mi, e in JN_RUBRIKA] + [['<b>Jami</b>', '<b>30</b>', 'Ko‘pi bilan 30 ball', '', '', '']], cls=(1,))
    on = ('<p>Oraliq nazorat o‘quv jarayonining <b>12-haftasida HEMIS</b> axborot tizimi orqali test shaklida o‘tkaziladi: '
          '20 ta savol, ko‘pi bilan 20 ball. Testda elektrostatika, o‘zgarmas tok va magnit maydon qonuniyatlarini bilish va qo‘llash tekshiriladi.</p>'
          + table(['Daraja', 'Ball', 'Tavsif'], [[n, b, E(t)] for n, (b, t) in zip(['Yuqori (a’lo)', 'Yetarli (yaxshi)', 'Minimal (qoniqarli)', 'Erishilmagan'], ON_RUBRIKA)]))
    yan = ('<p>Yakuniy nazorat attestatsiya haftasida <b>yozma ish</b> shaklida o‘tkaziladi, ko‘pi bilan 50 ball. Har bir variantda 4 ta topshiriq: '
           '3 ta nazariy savol va 1 ta amaliy keys.</p>')
    for nm, b, lv, extra in YAN_RUBRIKA:
        yan += f'<h3>{E(nm)} — {b} ball</h3><ul>' + ''.join(f'<li>{E(x)}</li>' for x in lv) + '</ul>' + (f'<div class="box">{E(extra)}</div>' if extra else '')
    calc = ('<p>Ballaringizni kiriting — jami ball va baho avtomatik hisoblanadi, har bir nazorat turi bo‘yicha saralash bali tekshiriladi.</p>'
            '<div class="calc" id="calc">'
            '<label>JN (0–30)<input id="c_jn" type="number" min="0" max="30" step="0.5" value="24"></label>'
            '<label>ON (0–20)<input id="c_on" type="number" min="0" max="20" step="0.5" value="15"></label>'
            '<label>YaN (0–50)<input id="c_yan" type="number" min="0" max="50" step="0.5" value="38"></label>'
            '<div class="calc-out" id="calcOut" aria-live="polite"></div></div>')
    secs = [('umumiy', 'Baholashning umumiy tartibi', umum, False), ('baho', 'Fan bo‘yicha bahoni aniqlash', baho + note, True),
            ('kalkulyator', 'Baho kalkulyatori', calc, True), ('matritsa', 'Ta’lim natijalari va baholash vositalari muvofiqligi', mat, False),
            ('jn-rubrika', 'Joriy nazorat rubrikasi — 30 ball', jn, False), ('on-rubrika', 'Oraliq nazorat rubrikasi — 20 ball', on, False),
            ('yan-rubrika', 'Yakuniy nazorat rubrikasi — 50 ball', yan, False)]
    chips = '<span class="tag">JN 30</span><span class="tag">ON 20</span><span class="tag">YaN 50</span><span class="tag g">Saralash: 18 / 12 / 30</span><span class="tag a">HEMIS</span>'
    body = hero([('Bosh sahifa', 'index.html'), ('Baholash', '')], 'Baholash · Fan dasturi, 9-bo‘lim', 'JN · ON · YaN rubrikalari va baho kalkulyatori', chips) + doc_layout(secs) + '</div></div>'
    page('baholash.html', 'Baholash — Umumiy fizika', body, desc='Joriy, oraliq va yakuniy nazorat mezonlari, baho kalkulyatori.')


def build_mustaqil():
    tal = ('<p>Mustaqil ta’lim fan dasturiga ko‘ra <b>180 soat</b> bo‘lib, 45 ta mavzu bo‘yicha taqdimot tayyorlashdan iborat (har biri 4 soat). '
           'Joriy nazoratda ikki topshiriq baholanadi:</p><ul>'
           '<li><b>1-MT — taqdimot va himoya (5 ball).</b> Qo‘shimcha ilmiy-uslubiy adabiyotlardan foydalanilgan, fizik jarayonlar, formulalar va chizmalar mantiqan izchil bayon qilingan bo‘lishi; himoyada fikrni mustaqil ifodalash talab etiladi.</li>'
           '<li><b>2-MT — keys-stadi tahlili va yechimi (5 ball).</b> Fizik qonunlarni hayotiy yoki amaliy muammoga qo‘llab, asoslangan yechim taklif qilish.</li></ul>'
           '<div class="box note">Ish belgilangan muddatda <b>HEMIS</b> tizimiga yuklanishi shart; muddatida yuklanmagan ish baholanmaydi. Ko‘chirmachilik minimal darajadan past baholanadi.</div>')
    tav = ('<p>Quyidagi tavsiyalar JN rubrikasining “yuqori daraja” mezonlaridan kelib chiqadi:</p><ol>'
           '<li>Mavzuning fizik mohiyati va asosiy qonuniyatlarini aniq ifodalang; formulalarni kattaliklar va birliklar bilan bering.</li>'
           '<li>Har bir muhim fikrni chizma, sxema yoki grafik bilan ko‘rsating.</li>'
           '<li>Asosiy darslikdan tashqari kamida bitta qo‘shimcha manbadan foydalaning va slayd oxirida manbalarni keltiring.</li>'
           '<li>Mavzuga oid hayotiy yoki texnik misol, iloji bo‘lsa simulyator yoki tajriba natijasini qo‘shing.</li>'
           '<li>Himoyaga tayyor matnsiz, o‘z so‘zlaringiz bilan gapirishga tayyorlaning.</li></ol>')
    rows = [[f'<span class="mono">{i}</span>', E(t), '4', 'Taqdimot'] for i, t in enumerate(MUSTAQIL, 1)]
    mtl = '<div class="grid">' + ''.join(
        (f'<a class="card" href="yoriqnomalar/MT-{i:02d}.html"><span class="tag">MT-{i:02d}</span><h3>{E(MT_T[i])}</h3><p>Nazariy savollar, masala yechish va amaliy tahlil.</p></a>'
         if exists(f'yoriqnomalar/MT-{i:02d}.html') else
         f'<div class="card soon"><div class="card-body"><span class="tag">MT-{i:02d}</span> <span class="tag m">tez orada</span><h3>Mustaqil topshiriq {i}</h3><p>Material tayyorlanmoqda.</p></div></div>')
        for i in range(1, 16)) + '</div>'
    secs = [('talablar', 'Talablar va baholash', tal, True),
            ('mavzular', '45 ta mavzu — fan dasturi bo‘yicha', table(['#', 'Mavzu', 'Soat', 'Shakl'], rows, cls=(2,)), False),
            ('taqdimot', 'Taqdimot tayyorlash bo‘yicha tavsiyalar', tav, False),
            ('yoriqnomalar', 'Yo‘riqnomalar (MT)', mtl, False)]
    chips = '<span class="tag">180 soat</span><span class="tag">45 mavzu</span><span class="tag v">1-MT: taqdimot · 2-MT: keys-stadi</span>'
    body = hero([('Bosh sahifa', 'index.html'), ('Mustaqil ta’lim', '')], 'Mustaqil ta’lim · Fan dasturi, 6-bo‘lim', 'Mustaqil ta’lim mavzulari va topshiriqlari', chips) + doc_layout(secs) + '</div></div>'
    page('mustaqil.html', 'Mustaqil ta’lim — Umumiy fizika', body, desc='Fan dasturidagi 45 ta mustaqil ta’lim mavzusi va topshiriq talablari.')


def build_oqituvchi():
    soat = table(['Mashg‘ulot turi', 'Soat', 'Izoh'], [
        ['Ma’ruza', FAN['maruza'], '27 mavzu × 2 soat'], ['Laboratoriya', FAN['lab'], '33 mashg‘ulot × 2 soat'],
        ['Mustaqil ta’lim', FAN['mustaqil'], '45 mavzu × 4 soat'], ['<b>Jami</b>', f'<b>{FAN["jami"]}</b>', f'{FAN["semestr"]}-semestrlar, haftasiga {FAN["hafta_soat"]} soat auditoriya']], cls=(1,))
    taqvim = table(['Nazorat', 'Muddat', 'Shakl'], [
        ['Joriy nazorat (JN)', 'Semestr davomida', '1-MT taqdimot va himoya, laboratoriyadagi faollik, 2-MT keys-stadi'],
        ['Oraliq nazorat (ON)', '12-hafta', 'HEMIS tizimida test, 20 savol'],
        ['Yakuniy nazorat (YaN)', 'Attestatsiya haftasi', 'Yozma ish: 3 nazariy savol + 1 keys']])
    usul = ('<ul>'
            '<li><b>Blits-so‘rov</b> — mashg‘ulot boshida oldingi mavzu bo‘yicha 3–5 ta qisqa savol; ma’ruza sahifalaridagi “Nazariy savollar” bo‘limidan foydalanish mumkin.</li>'
            '<li><b>Keys-stadi</b> — hayotiy vaziyatni fizik qonunlar orqali tahlil qilish; YaN ning 4-savoli va 2-MT shu shaklda.</li>'
            '<li><b>Guruhlarda ishlash</b> — laboratoriya natijalarini guruhlarda solishtirish va xatoliklarni muhokama qilish.</li>'
            '<li><b>Taqdimotlar</b> — mustaqil ta’lim mavzulari bo‘yicha (1-MT).</li>'
            '<li><b>Loyihalar</b> — jamoaviy ish va himoya; masalan, simulyator yordamida tajriba rejasini tuzish.</li></ul>')
    reja = table(['Bosqich', 'Vaqt', 'Mazmun'], [
        ['Kirish va blits-so‘rov', '10 daqiqa', 'Oldingi mavzuni takrorlash, maqsadni e’lon qilish'],
        ['Nazariy qism', '35 daqiqa', 'Asosiy tushunchalar va qonunlar, formulalarni keltirib chiqarish'],
        ['Interaktiv model / misol', '20 daqiqa', 'Simulyatorda parametrlarni o‘zgartirib, natijani oldindan taxmin qilish'],
        ['Mustahkamlash', '10 daqiqa', 'Nazariy savollar, qisqa masala'],
        ['Yakun va topshiriq', '5 daqiqa', 'Xulosa, mustaqil ta’lim topshirig‘ini berish']])
    reja = '<p>Bitta mashg‘ulot (2 akademik soat, 80 daqiqa) uchun <b>tavsiya</b> etiladigan tuzilma. Bu fan dasturining talabi emas, o‘qituvchi o‘z guruhiga moslashtiradi.</p>' + reja
    sayt = ('<ul><li><b>Til:</b> yuqoridagi UZ / RU / EN tugmalari butun sahifani tarjima qiladi (Google Translate). Fan rus tilida o‘qitiladi, shuning uchun RU rejimi talabalar uchun qulay.</li>'
            '<li><b>Elektron doska:</b> kun/tun tugmasi bilan yorqinlikni moslang; mundarija orqali bo‘limlarga tez o‘ting.</li>'
            '<li><b>Tinglash:</b> ma’ruza matnini brauzer ovozida o‘qitish mumkin; istalgan xatboshini bosib, o‘sha joydan davom ettiriladi.</li>'
            '<li><b>Chop etish:</b> brauzerning “Chop etish” funksiyasi menyusiz toza variantni chiqaradi.</li></ul>')
    hal = '<p>Fan dasturi talabiga ko‘ra talabalar akademik halollik tamoyillariga rioya qilishi shart. Mustaqil ish va keyslarda ko‘chirmachilik aniqlansa, rubrikaga ko‘ra minimal darajadan past baholanadi.</p>'
    secs = [('soatlar', 'Soatlar taqsimoti', soat, False), ('taqvim', 'Nazorat taqvimi', taqvim, True), ('usullar', 'Ta’lim texnologiyalarini qo‘llash', usul, False),
            ('reja', 'Mashg‘ulot rejasi namunasi (80 daqiqa)', reja, False), ('sayt', 'Saytdan darsda foydalanish', sayt, False), ('halollik', 'Akademik halollik', hal, False)]
    body = hero([('Bosh sahifa', 'index.html'), ('O‘qituvchi uchun', '')], 'O‘qituvchi uchun qo‘llanma', 'Fanni o‘qitish bo‘yicha qo‘llanma',
                '<span class="tag">54 + 66 + 180 soat</span><span class="tag v">ON — 12-hafta</span><span class="tag a">YaN — attestatsiya haftasi</span>') + doc_layout(secs) + '</div></div>'
    page('oqituvchi.html', 'O‘qituvchi uchun — Umumiy fizika', body)


def build_glossariy():
    items = sorted(GLOSSARIY, key=lambda x: x[0].replace('‘', '').replace('’', '').lower())
    lst = ''.join(f'<div class="gl-item"><b>{E(u)}</b><span class="tr notranslate" translate="no" data-noalif>{E(r)} · {E(e)}</span>'
                  f'<p>{E(d)} <a href="annotatsiya.html#maruzalar" class="mono" style="font-size:12px">M{n}</a></p></div>' for u, r, e, d, n in items)
    inner = f'<input class="search" id="glSearch" type="search" placeholder="Atamani qidiring (o‘zbekcha, ruscha yoki inglizcha)..." aria-label="Qidiruv">{lst}'
    secs = [('atamalar', f'{len(items)} ta atama: o‘zbekcha — ruscha — inglizcha', inner, False)]
    body = hero([('Bosh sahifa', 'index.html'), ('Atamalar lug‘ati', '')], '1-ilova', 'Atamalar lug‘ati',
                '<span class="tag">UZ · RU · EN</span><span class="tag m">Fan dasturi mavzulari bo‘yicha (M1–M27)</span>') + doc_layout(secs, toc=False) + '</div></div>'
    page('glossariy.html', 'Atamalar lug‘ati — Umumiy fizika', body)


def build_vositalar():
    cards = ''.join(f'<a class="card" href="{u}" target="_blank" rel="noopener"><span class="tag">{E(k)}</span> <span class="tag m">{E(p)}</span>'
                    f'<h3><span class="notranslate" translate="no">{E(n)}</span></h3><p>{E(d)}</p></a>' for n, k, d, u, p in VOSITALAR)
    secs = [('vositalar', 'Dasturiy vositalar va ochiq resurslar', f'<p>Laboratoriya natijalarini qayta ishlash, modellashtirish va mustaqil ta’lim uchun bepul yoki keng tarqalgan vositalar.</p><div class="grid-2">{cards}</div>', False)]
    body = hero([('Bosh sahifa', 'index.html'), ('Dasturiy vositalar', '')], '2-ilova', 'Dasturiy vositalar', '<span class="tag">Bepul vositalar</span><span class="tag g">Brauzerda ishlaydi</span>', listen=False) + doc_layout(secs, toc=False) + '</div></div>'
    page('vositalar.html', 'Dasturiy vositalar — Umumiy fizika', body)


def build_simulyatorlar():
    def sim(id_, title, ctl, txt):
        return (f'<div class="card sim" id="{id_}"><span class="tag a">Interaktiv model</span><h3 style="font-size:19px;margin:10px 0 4px">{title}</h3>'
                f'<p style="color:var(--text-2);font-size:14px">{txt}</p><canvas width="900" height="380" data-sim="{id_}" role="img" aria-label="{title}"></canvas>'
                f'<div class="sim-ctl">{ctl}</div><div class="sim-out" data-out="{id_}"></div></div>')
    def rng(id_, name, lbl, mn, mx, st, v, unit):
        return f'<label>{lbl}: <b data-v="{id_}-{name}">{v}</b> {unit}<input type="range" data-p="{id_}-{name}" min="{mn}" max="{mx}" step="{st}" value="{v}"></label>'
    own = ''.join([
        sim('mayatnik', 'Matematik mayatnik', rng('mayatnik', 'l', 'Ip uzunligi l', 0.2, 2.5, 0.05, 1.0, 'm') + rng('mayatnik', 'g', 'Erkin tushish tezlanishi g', 1.6, 24.8, 0.1, 9.8, 'm/s²') + rng('mayatnik', 'a', 'Boshlang‘ich og‘ish', 3, 40, 1, 15, '°'),
            'Davr $T = 2\\pi\\sqrt{l/g}$ ga teng va kichik og‘ishlarda amplitudaga bog‘liq emas. g ni Oy (1,6) yoki Yupiter (24,8) qiymatiga o‘zgartirib ko‘ring. (M7, L8)'),
        sim('otilish', 'Burchak ostida otilgan jism', rng('otilish', 'v', 'Boshlang‘ich tezlik v₀', 5, 40, 1, 20, 'm/s') + rng('otilish', 'u', 'Otilish burchagi α', 5, 85, 1, 45, '°') + rng('otilish', 'g', 'g', 1.6, 24.8, 0.1, 9.8, 'm/s²'),
            'Uchish uzoqligi $L = v_0^2\\sin 2\\alpha / g$, ko‘tarilish balandligi $H = v_0^2\\sin^2\\alpha / 2g$. Qaysi burchakda uzoqlik eng katta? (M1–M2, MT-5)'),
        sim('linza', 'Yupqa linzada tasvir yasash', rng('linza', 'F', 'Fokus masofasi F', -20, 20, 1, 10, 'sm') + rng('linza', 'd', 'Buyumgacha masofa d', 2, 45, 0.5, 25, 'sm'),
            'Yupqa linza formulasi $\\frac{1}{F} = \\frac{1}{d} + \\frac{1}{f}$. F manfiy bo‘lsa — sochuvchi linza. Buyumni fokusdan yaqinroq qo‘yib, mavhum tasvirni kuzating. (M22, L29)'),
        sim('yemirilish', 'Radioaktiv yemirilish', rng('yemirilish', 'T', 'Yarim yemirilish davri T½', 1, 10, 0.5, 3, 's') + '<label><button class="btn btn-ghost" type="button" data-reset="yemirilish"><i class="fas fa-rotate"></i> Qayta boshlash</button></label>',
            'Har bir yadro tasodifiy yemiriladi, lekin ko‘p yadrolar uchun $N = N_0\\, 2^{-t/T_{1/2}}$ qonuni bajariladi. Ko‘k chiziq — nazariya, nuqtalar — model. (M26)')])
    by = {}
    for n, t, sl, d in PHET:
        by.setdefault(n, []).append((t, sl, d))
    rows = []
    for n in sorted(by):
        for t, sl, d in by[n]:
            rows.append([f'<span class="mono">M{n}</span>', f'<a href="https://phet.colorado.edu/en/simulations/{sl}" target="_blank" rel="noopener"><span class="notranslate" translate="no">{E(t)}</span></a>', E(d)])
    phet = ('<p>Kolorado universitetining <b>PhET</b> simulyatorlari bepul, brauzerda ishlaydi va rus tilini qo‘llab-quvvatlaydi. Fan dasturi ma’ruzalariga moslab tanlangan:</p>'
            + table(['Ma’ruza', 'Simulyator', 'Nimani o‘rganadi'], rows))
    secs = [('modellar', 'Saytning interaktiv modellari', f'<div style="display:flex;flex-direction:column;gap:16px">{own}</div>', False),
            ('phet', 'PhET simulyatorlari — fan dasturi bo‘yicha', phet, False)]
    body = hero([('Bosh sahifa', 'index.html'), ('Simulyatorlar', '')], 'Interaktiv modellar', 'Simulyatorlar',
                f'<span class="tag a">4 ta o‘z modeli</span><span class="tag">{len(PHET)} ta PhET simulyatori</span>', listen=False) + doc_layout(secs) + '</div></div>'
    page('simulyatorlar.html', 'Simulyatorlar — Umumiy fizika', body, scripts=('sims.js',))


# ================= Bosh sahifa =================
def build_index():
    def lcard(i, t):
        if exists(f'lectures/lecture{i}.html'):
            return f'<a class="card" href="lectures/lecture{i}.html"><span class="tag">{i}-ma’ruza</span><h3>{E(t)}</h3><p>{E(LECT_D[i-1])}</p></a>'
        return f'<div class="card soon"><div class="card-body"><span class="tag">{i}-ma’ruza</span> <span class="tag m">tez orada</span><h3>{E(t)}</h3><p>Material tayyorlanmoqda.</p></div></div>'
    def bcard(i, t):
        if exists(f'labs/lab{i}.html'):
            return f'<a class="card" href="labs/lab{i}.html"><span class="tag">L{i}</span><h3>{E(t)}</h3><p>{E(LAB_D.get(i, ""))}</p></a>'
        return f'<div class="card soon"><div class="card-body"><span class="tag">L{i}</span> <span class="tag m">tez orada</span><h3>{E(t)}</h3><p>Material tayyorlanmoqda.</p></div></div>'
    L = '\n'.join(lcard(i, t) for i, t in enumerate(LECT, 1))
    B = '\n'.join(bcard(i, t) for i, t in enumerate(LAB_N, 1))
    nl = sum(exists(f'lectures/lecture{i}.html') for i in range(1, 29))
    about = [('annotatsiya.html', 'Kirish', 'Annotatsiya va fan dasturi', 'Fan ma’lumotlari, ta’lim natijalari (TN1–TN10), 27 ma’ruza va 33 laboratoriya mavzusi, adabiyotlar.'),
             ('baholash.html', 'Baholash', 'JN · ON · YaN rubrikalari', '100 ballik tizim, saralash ballari, TN–nazorat matritsasi va baho kalkulyatori.'),
             ('oqituvchi.html', 'O‘qituvchi', 'O‘qituvchi uchun qo‘llanma', 'Soatlar taqsimoti, nazorat taqvimi, mashg‘ulot rejasi namunasi va saytdan foydalanish.'),
             ('mustaqil.html', 'Mustaqil ta’lim', '45 mavzu va topshiriqlar', 'Taqdimot va keys-stadi talablari, yo‘riqnomalar (MT).'),
             ('glossariy.html', '1-ilova', 'Atamalar lug‘ati', f'{len(GLOSSARIY)} ta atama: o‘zbekcha–ruscha–inglizcha, qisqa ta’rif va mavzu havolasi.'),
             ('vositalar.html', '2-ilova', 'Dasturiy vositalar', 'PhET, Tracker, GeoGebra, Python va boshqa bepul vositalar.')]
    about = ''.join(f'<a class="card" href="{h}"><span class="tag">{E(k)}</span><h3>{E(t)}</h3><p>{E(d)}</p></a>' for h, k, t, d in about)
    steps = [('Maqsad', 'Mavzu maqsadi va asosiy tushunchalar bilan tanishish.'), ('Nazariya', 'Qonunlar va formulalarni o‘zlashtirish.'),
             ('Interaktiv model', 'Parametrlarni o‘zgartiring, natijani taxmin qiling, tekshiring.'), ('Laboratoriya', 'Tajriba, o‘lchov va natijalarni nazariya bilan solishtirish.'),
             ('Mustaqil ish', 'Taqdimot (1-MT) va keys-stadi (2-MT).'), ('Baholash', 'JN, ON va YaN natijalari HEMIS tizimida.')]
    steps = ''.join(f'<div class="card"><div class="card-body"><span class="tag">QADAM {i}</span><h3>{E(t)}</h3><p>{E(d)}</p></div></div>' for i, (t, d) in enumerate(steps, 1))
    simc = ''.join(f'<a class="card" href="simulyatorlar.html#{k}"><span class="tag a">Model</span><h3>{E(v)}</h3><p>Brauzerda ishlaydigan interaktiv model.</p></a>' for k, v in OWN_SIM.items())
    body = f'''<section class="hero">
<div class="kicker">{FAN['yonalish']} · {FAN['kod']} · {FAN['yil']}</div>
<h1>Tabiat qonunlarini<br><span class="grad">tushuning, o‘lchang<br>va modellashtiring.</span></h1>
<p class="hero-lead">Mexanika va termodinamikadan elektromagnetizm, optika, atom va yadro fizikasigacha — fan dasturi asosida tuzilgan ochiq elektron darslik. Baholash va rasmiy topshiriqlar HEMIS orqali amalga oshiriladi.</p>
<div class="hero-actions"><a class="btn btn-primary" href="lectures/lecture1.html"><i class="fas fa-play"></i> Birinchi ma’ruzadan boshlash</a><a class="btn btn-ghost" href="annotatsiya.html"><i class="fas fa-book-open"></i> Fan dasturi</a></div>
<div class="stats">
<div class="card stat"><div class="num">01</div><h3>{FAN['maruza']} soat ma’ruza</h3><p>{nl} ta ma’ruza sahifasi: maqsad, nazariya, interaktiv model va nazorat savollari.</p></div>
<div class="card stat"><div class="num">02</div><h3>{FAN['lab']} soat laboratoriya</h3><p>Fan dasturida 33 ta laboratoriya mashg‘uloti: o‘lchov, tajriba va tahlil.</p></div>
<div class="card stat"><div class="num">03</div><h3>{FAN['mustaqil']} soat mustaqil ta’lim</h3><p>45 ta mavzu bo‘yicha taqdimot va keys-stadi topshiriqlari.</p></div>
<div class="card stat"><div class="num">04</div><h3>{FAN['ects']} ECTS kredit</h3><p>{FAN['jami']} soat, {FAN['semestr']}-semestrlar. Baholash: JN 30 · ON 20 · YaN 50.</p></div>
</div></section>

<section class="section" id="darslik-haqida"><div class="wrap"><div class="kicker">Darslik haqida</div><h2>Annotatsiya, baholash va ilovalar</h2>
<p class="section-lead">{FAN['ects']} ECTS kredit ({FAN['jami']} soat), {FAN['semestr']}-semestrlar. Darslik {FAN['yil']} o‘quv yili uchun tasdiqlangan fan dasturi ({FAN['kod']}) asosida tuzilgan.</p>
<div class="grid">{about}</div></div></section>

<section class="section" id="oquv-modeli"><div class="wrap"><div class="kicker">O‘quv modeli</div><h2>Har bir mavzu bo‘yicha olti qadam</h2>
<p class="section-lead">Nazariya, interaktiv model, tajriba va mustaqil ish bitta o‘quv sikliga birlashtirilgan.</p><div class="grid">{steps}</div></div></section>

<section class="section" id="maruzalar"><div class="wrap"><div class="kicker">Ma’ruzalar · {FAN['maruza']} soat</div><h2>Ma’ruzalar</h2>
<p class="section-lead">Har bir ma’ruzada: maqsad, asosiy tushunchalar, nazariy ma’lumot, interaktiv model, nazorat savollari va adabiyotlar. Fan dasturidagi rasmiy mavzular ro‘yxati — <a href="annotatsiya.html#maruzalar">Darslik haqida</a>.</p>
<div class="grid">{L}</div></div></section>

<section class="section" id="laboratoriya"><div class="wrap"><div class="kicker">Laboratoriya ishlari · {FAN['lab']} soat</div><h2>Laboratoriya ishlari</h2>
<p class="section-lead">Maqsad, uskunalar, ish tartibi va hisobot talablari. Fan dasturidagi 33 ta mashg‘ulot ro‘yxati — <a href="annotatsiya.html#laboratoriya">Darslik haqida</a>.</p>
<div class="grid">{B}</div></div></section>

<section class="section" id="mustaqil"><div class="wrap"><div class="kicker">Mustaqil ta’lim · {FAN['mustaqil']} soat</div><h2>45 mavzu va yo‘riqnomalar</h2>
<p class="section-lead">Taqdimot (1-MT) va keys-stadi (2-MT) talablari, fan dasturidagi barcha mavzular va MT yo‘riqnomalari.</p>
<div class="hero-actions" style="justify-content:flex-start;margin-top:0"><a class="btn btn-primary" href="mustaqil.html"><i class="fas fa-list-check"></i> Mavzular va talablar</a><a class="btn btn-ghost" href="yoriqnomalar/MT-01.html">MT-01 yo‘riqnomasi</a></div></div></section>

<section class="section" id="simulyatorlar"><div class="wrap"><div class="kicker">Simulyatorlar</div><h2>Interaktiv modellar</h2>
<p class="section-lead">Saytning o‘z modellari va fan dasturiga moslab tanlangan {len(PHET)} ta PhET simulyatori.</p><div class="grid-2">{simc}</div></div></section>

<section class="section" id="baholash"><div class="wrap"><div class="card callout"><div class="kicker">Rasmiy jarayonlar</div><h2 style="margin-top:8px">Baholash va topshiriqlarni topshirish — HEMIS’da</h2>
<p>Ushbu sayt ochiq o‘quv materiallari to‘plami bo‘lib, baho qo‘ymaydi va topshiriq qabul qilmaydi. Joriy, oraliq (12-hafta) va yakuniy nazorat natijalari universitetning HEMIS axborot tizimida belgilangan tartibda yuritiladi. Mezonlar: <a href="baholash.html">Baholash</a>.</p></div></div></section>

<section class="section" id="muallif"><div class="wrap"><div class="card author"><div class="avatar">DE</div><div><div class="kicker">Elektron darslik muallifi</div>
<h2 style="margin:6px 0 4px">Ergashev Dadaxon</h2><div class="role">Qo‘qon davlat universiteti, Fizika va astronomiya kafedrasi</div>
<p>Fan dasturini tuzuvchilar: {', '.join(n for n, _ in TUZUVCHI)}. Taqrizchilar: {', '.join(n for n, _ in TAQRIZCHI)}.</p></div></div></div></section>'''
    page('index.html', 'Umumiy fizika — interaktiv elektron darslik', body, desc='Umumiy fizika fani bo‘yicha ochiq elektron darslik: ma’ruzalar, laboratoriya, mustaqil ta’lim, baholash.')


if __name__ == '__main__':
    build_lectures(); build_labs(); build_mt()
    build_annotatsiya(); build_baholash(); build_mustaqil(); build_oqituvchi()
    build_glossariy(); build_vositalar(); build_simulyatorlar(); build_index()
    print('Tayyor.')
