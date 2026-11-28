"""Umumiy shablonlar: sarlavha, navigatsiya, footer, bo'limlar (dizayn: Yarimo'tkazgich asboblar fizikasi darsligi asosida)."""
import html as _h

SITE = "Umumiy fizika"
AUTHOR = "D. Ergashev"
AUTHOR_FULL = "Ergashev Dadaxon"
CODE = "UMF11210"

NAV = [
    ("annotatsiya.html", "Darslik haqida"),
    ("index.html#maruzalar", "Ma’ruzalar"),
    ("index.html#laboratoriya", "Laboratoriya"),
    ("mustaqil.html", "Mustaqil ta’lim"),
    ("simulyatorlar.html", "Simulyatorlar"),
    ("baholash.html", "Baholash"),
    ("oqituvchi.html", "O‘qituvchi uchun"),
    ("glossariy.html", "Lug‘at"),
    ("vositalar.html", "Vositalar"),
    ("index.html#muallif", "Muallif"),
]

# Fan dasturidagi asosiy adabiyotlar (raqamlar dasturdagi [1..5] havolalarga mos)
BASE_LIT = {
    1: "Gaibov A. Fizika. — 2022.",
    2: "Abduraxmonov Q. va boshq. Fizika. — 2018.",
    3: "Eshboltayev I. va boshq. Umumiy fizikadan laboratoriya mashg‘ulotlari. — 2023.",
    4: "Трофимова Т.И. Курс физики. — 1985.",
    5: "Tursunov I. Fizika. — 2020.",
}
# Fan dasturidagi qo'shimcha adabiyotlar
ADD_LIT = {
    "q1": "Sultanov N. Fizika kursi. Darslik. — Classik, 2021. — 412 b.",
    "q2": "Nurmatov N.A., Raxmonov G‘.T., Alimov R., Sultonov O.Z., Xamidjonov I.X. Elektr va magnetizm fanidan praktikum. Uslubiy qo‘llanma. — Toshkent: Innovatsiya-Ziyo, 2021. — 176 b.",
    "q3": "Ульмасова М. и др. Практикум по физике. Механика и молекулярная физика. — Ташкент: Укитувчи, 1996.",
    "q4": "Giancoli D.C. Physics: Principles with Applications. 6th ed. — Prentice Hall, 2004.",
    "q5": "Serway R.A., Jewett J.W. Physics for Scientists and Engineers with Modern Physics. 9th ed. — Cengage Learning, 2013.",
}
WEB = [
    ("https://www.tdpu.uz", "www.tdpu.uz"), ("https://www.edu.uz", "www.edu.uz"), ("https://www.pedagog.uz", "www.pedagog.uz"),
    ("https://www.ziyonet.uz", "www.ziyonet.uz"), ("https://ocw.mit.edu/courses/5-61-physical-chemistry-fall-2017/", "MIT OpenCourseWare: 5.61 Physical Chemistry"),
]
# Xalqaro darsliklar (mustaqil chuqurlashtirish uchun)
INTL = {
    "halliday": "Halliday D., Resnick R., Walker J. Fundamentals of Physics. 12th ed. — Hoboken: Wiley, 2021.",
    "young": "Young H.D., Freedman R.A. University Physics with Modern Physics. 15th ed. — Pearson, 2020.",
    "openstax1": "Ling S.J., Sanny J., Moebs W. University Physics. Vol. 1. — Houston: OpenStax, 2016 (ochiq darslik).",
    "openstax2": "Ling S.J., Sanny J., Moebs W. University Physics. Vol. 2. — Houston: OpenStax, 2016 (ochiq darslik).",
    "openstax3": "Ling S.J., Sanny J., Moebs W. University Physics. Vol. 3. — Houston: OpenStax, 2016 (ochiq darslik).",
    "feynman": "Feynman R.P., Leighton R.B., Sands M. The Feynman Lectures on Physics. Vol. I–III. — Addison-Wesley, 1963–1965.",
    "kleppner": "Kleppner D., Kolenkow R. An Introduction to Mechanics. 2nd ed. — Cambridge University Press, 2014.",
    "schroeder": "Schroeder D.V. An Introduction to Thermal Physics. — Addison-Wesley, 1999.",
    "purcell": "Purcell E.M., Morin D.J. Electricity and Magnetism. 3rd ed. — Cambridge University Press, 2013.",
    "hecht": "Hecht E. Optics. 5th ed. — Pearson, 2017.",
    "krane": "Krane K.S. Modern Physics. 4th ed. — Wiley, 2020.",
    "atkins": "Atkins P., de Paula J., Keeler J. Atkins’ Physical Chemistry. 11th ed. — Oxford University Press, 2018.",
    "irodov": "Irodov I.E. Problems in General Physics. — Moscow: Mir Publishers, 1981.",
    "taylor": "Taylor J.R. An Introduction to Error Analysis. 2nd ed. — Sausalito: University Science Books, 1997.",
    "squires": "Squires G.L. Practical Physics. 4th ed. — Cambridge University Press, 2001.",
    "gum": "JCGM 100:2008. Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM). — BIPM, 2008.",
    "si": "BIPM. The International System of Units (SI Brochure). 9th ed. — 2019.",
}
INTL = {k: f'<span lang="en">{v}</span>' for k, v in INTL.items()}

HEAD_JS = r"""<script>(function(){var d=document.documentElement;try{d.dataset.theme=localStorage.getItem('yaf-theme')||'light';}catch(e){d.dataset.theme='light';}var m=document.cookie.match(/googtrans=\/uz\/(ru|en)/);if(m){d.classList.add('alif-old');d.dataset.tl=m[1];}})();</script>"""
esc = _h.escape
V = "15"  # kesh versiyasi


def head(title, desc, katex=True, extra_css=True, body_cls=""):
    k = ""
    if katex:
        k = ('<link rel="stylesheet" href="vendor/katex/katex.min.css">\n'
             '<script defer src="vendor/katex/katex.min.js"></script>\n'
             '<script defer src="vendor/katex/contrib/auto-render.min.js"></script>\n')
    return f"""<!doctype html>
<html lang="uz">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — {SITE}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="{AUTHOR_FULL}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
{HEAD_JS}
<script src="js/alifbo.js"></script>
<link rel="stylesheet" href="css/styles.css?v={V}">
{f'<link rel="stylesheet" href="css/darslik.css?v={V}">' if extra_css else ''}
{k}</head>
<body{f' class="{body_cls}"' if body_cls else ''}>
<a class="skip-link" href="#main">Asosiy mazmunga o‘tish</a>
"""

# Logotip: chiziqli atom belgisi (rangi CSS dagi currentColor dan olinadi)
ATOM = '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><ellipse cx="24" cy="24" rx="20" ry="8"/><ellipse cx="24" cy="24" rx="20" ry="8" transform="rotate(60 24 24)"/><ellipse cx="24" cy="24" rx="20" ry="8" transform="rotate(120 24 24)"/><circle cx="24" cy="24" r="3.6"/><circle cx="24" cy="24" r="1.4" fill="currentColor" stroke="none"/></svg>'


def header(active=""):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="site-header"><div class="container navbar"><a class="brand" href="index.html"><span class="brand-mark">{ATOM}</span><span class="brand-txt"><b>UMUMIY FIZIKA</b><small>Interaktiv elektron darslik · Bakalavriat</small></span></a><div class="hdr-tools notranslate" translate="no"><div class="lang-switch" role="group" aria-label="Til / Язык / Language"><button type="button" data-lang="uz">UZ</button><button type="button" data-lang="ru">RU</button><button type="button" data-lang="en">EN</button></div><span class="hdr-sep" aria-hidden="true"></span><button class="icon-btn theme-btn" type="button" aria-label="Kun va tun rejimini almashtirish" title="Kun / tun rejimi"><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button></div><button class="menu-toggle" type="button" aria-label="Menyuni ochish" aria-expanded="false">☰</button></div><div class="nav-row"><div class="container"><nav class="nav-links" aria-label="Asosiy navigatsiya">{links}</nav></div></div></header>
"""


def footer(sims=False):
    return f"""<footer class="footer"><div class="container">{SITE} — interaktiv elektron darslik ({CODE}) · Qo‘qon davlat universiteti, Fizika va astronomiya kafedrasi · 2026 · Muallif: <a href="index.html#muallif">{AUTHOR}</a><br>Rasmiy topshiriqlar va baholash faqat HEMIS axborot tizimida yuritiladi.</div></footer>
{'<script src="js/sims.js?v=' + V + '" defer></script>' if sims else ''}
<script src="js/app.js?v={V}" defer></script>
</body></html>
"""


SPEAKER = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 5 6 9H2v6h4l5 4V5z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/></svg>'


def hero(crumbs, badge, title, lead="", chips=(), read=None):
    cr = " / ".join(f'<a href="{h}">{t}</a>' if h else f"<span>{t}</span>" for h, t in crumbs)
    ch = "".join(f'<span class="chip {cls}">{t}</span>' for cls, t in chips)
    tools = f'<div class="hero-tools"><button class="voice-btn" type="button" data-read="{read}" aria-label="Mavzuni ovozli tinglash">{SPEAKER}<span>Tinglash</span></button></div>' if read else ""
    return f"""<section class="page-hero"><div class="container">{tools}<nav class="crumbs" aria-label="Yo‘l">{cr}</nav><div class="eyebrow" style="margin-top:1rem">{badge}</div><h1>{title}</h1>{f'<p class="lead">{lead}</p>' if lead else ''}<div class="chips">{ch}</div></div></section>
"""


def sec(sid, num, title, body, cls=""):
    n = f'<span class="num">{num}</span>' if num else ""
    return f'<section class="doc-sec{(" " + cls) if cls else ""}" id="{sid}"><h2>{n}{title}</h2>{body}</section>\n'


def doc(toc, sections, pager=""):
    t = "".join(f'<li><a href="#{i}">{n}</a></li>' for i, n in toc)
    return f"""<div class="container doc-layout"><aside class="toc" aria-label="Sahifa mundarijasi"><h2>Mundarija</h2><ol>{t}</ol></aside><div class="doc">{''.join(sections)}{pager}</div></div>
"""


def quiz(items, qid):
    out = []
    for i, (qs, opts, a, ex) in enumerate(items):
        o = "".join(f'<label><input type="radio" name="{qid}-{i}" value="{j}"> <span>{"ABCD"[j]}) {t}</span></label>' for j, t in enumerate(opts))
        out.append(f'<div class="q" data-a="{a}"><p>{i+1}. {qs}</p>{o}<div class="fb">To‘g‘ri javob: <b>{"ABCD"[a]}</b>. {ex}</div></div>')
    return f'<div class="quiz">{"".join(out)}<div class="actions"><button class="primary" type="button" data-check>Tekshirish</button><button class="secondary" type="button" data-reset-quiz>Qayta boshlash</button></div><div class="quiz-result" aria-live="polite"></div></div>'


def prompt(pid, text):
    return f'<div class="prompt-box"><button class="secondary copy" type="button" data-copy="{pid}">Nusxalash</button><pre id="{pid}">{esc(text)}</pre></div>'


def code(pid, text):
    return f'<div class="prompt-box"><button class="secondary copy" type="button" data-copy="{pid}">Nusxalash</button><pre class="code" id="{pid}">{esc(text)}</pre></div>'


def ul(items, ordered=False):
    tag = "ol" if ordered else "ul"
    return f"<{tag}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{tag}>"


def table(head_, rows):
    h = "".join(f"<th>{c}</th>" for c in head_)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="tw"><table class="t"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def card_link(href, badge, title, text):
    return f'<a class="card" href="{href}"><span class="badge">{badge}</span><h3>{title}</h3><p class="muted">{text}</p></a>'
