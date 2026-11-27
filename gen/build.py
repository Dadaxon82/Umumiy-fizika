"""Umumiy fizika elektron darsligi sahifalarini generatsiya qilish:  python gen/build.py .
Dizayn va tuzilma: "Yarimo'tkazgich asboblar fizikasi" interaktiv darsligi (I. Eshboltayev) asosida."""
import os, sys, re, json, random
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from lec_mex import L as L1
from lec_mol import L as L2
from lec_el import L as L3
from lec_opt import L as L4
from lec_atom import L as L5
from labs_a import B as B1
from labs_b import B as B2
from lab_intro import INTRO
import other
from tours import T as TOURS
from alifbo import html_to_new

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
LECT = sorted(L1 + L2 + L3 + L4 + L5, key=lambda x: x["n"])
LABS = sorted(B1 + B2, key=lambda x: x["n"])
NL = len(LECT)

SIMNAME = {
    "vernier": "Shtangensirkul (nonius) bilan o‘lchash", "kinem": "To‘g‘ri chiziqli harakat grafiklari", "projectile": "Gorizontga burchak ostida otilgan jism",
    "newton": "Qiya tekislik: kuchlar va ishqalanish", "spring": "Guk qonuni va Yung moduli", "beam": "Sterjenning egilishi", "collision": "Markaziy to‘qnashuv",
    "rotation": "Qiya tekislikdan dumalash va inersiya momenti", "oscill": "Mayatnik va prujinali tebrangich", "maxwell": "Maksvell tezliklar taqsimoti",
    "gas": "Ideal gaz izojarayonlari (p–V diagramma)", "calorimeter": "Kalorimetr: issiqlik balansi", "capillary": "Sirt taranglik va kapillyarlik",
    "archimedes": "Gidrostatik tortish (Arximed kuchi)", "coulomb": "Ikki nuqtaviy zaryad maydoni", "capacitor": "Kondensatorning zaryadlanishi (RC)",
    "circuit": "To‘la zanjir uchun Om qonuni", "kirchhoff": "Kirxgof qoidalari: ikki konturli zanjir", "wheatstone": "Uitston ko‘prigi",
    "vacdiode": "Vakuum diod VAX", "bfield": "Tokning magnit maydoni va tangens-galvanometr", "induction": "Elektromagnit induksiya",
    "rlc": "Tebranish konturi va rezonans", "ac": "O‘zgaruvchan tok zanjiri: faza va quvvat", "young": "Ikki tirqishdan interferensiya",
    "grating": "Difraksion panjara", "malus": "Malyus va Bryuster qonunlari", "lens": "Yupqa linzada tasvir", "snell": "Yorug‘likning sinishi va to‘la ichki qaytish",
    "planck": "Absolyut qora jism nurlanishi", "photo": "Tashqi fotoeffekt", "photometry": "Yoritilganlik qonuni", "bohr": "Vodorod atomi spektri (Bor nazariyasi)",
    "franck": "Frank–Gers tajribasi", "decay": "Radioaktiv yemirilish qonuni", "binding": "Yadroning solishtirma bog‘lanish energiyasi",
}
TN_TEXT = {
    "TN1": "Kelajakdagi mutaxassislik doirasida yuzaga keladigan masalalarda hodisalarning fizik mohiyatini ajrata olish",
    "TN2": "Zamonaviy fizik eksperimental asboblar (mikroskop, spektrograf va boshqalar) bilan tanish bo‘lish, turli fizik tajribalarni o‘tkazish ko‘nikmasiga ega bo‘lish",
    "TN3": "Fizik qonunlarning qo‘llanilish chegaralarini aniqlay olish, fizikaning turli bo‘limlariga nazariy yondashuvlarning umumiyligini hisobga olish",
    "TN4": "Elektr va magnit maydonlardagi hodisalar, elektromagnit induksiya, mexanik va elektromagnit tebranishlar hamda to‘lqinlar haqida bilimga ega bo‘lish",
    "TN5": "Atomlar tuzilishi va mikrodunyo fizikasi, atom yadrosi va elementar zarralar fizikasi haqida bilimga ega bo‘lish",
    "TN6": "Fizik qonuniyatlar bo‘yicha nazariy bilimlarni qo‘llab, tabiat qonunlariga oid asosiy masalalarni to‘g‘ri yecha olish",
    "TN7": "Jismlarning mexanik harakati, dinamika va saqlanish qonunlari, molekulyar-kinetik nazariya va termodinamika asoslarini bilish",
    "TN8": "O‘zgarmas va o‘zgaruvchan tok qonunlarini o‘rganish, taqqoslash va o‘lchov asboblari bilan mustaqil ishlay olish",
    "TN9": "Geometrik, to‘lqin va kvant optikasi masalalarini farqlay olish va yecha olish",
    "TN10": "Atom tuzilishi va mikrodunyo haqida tasavvurga ega bo‘lish",
}
# Fan dasturidagi TN — nazorat matritsasi (JN, ON, YaN)
TN_MATRIX = {t: ("+", "+", "+") for t in ["TN1", "TN2", "TN3", "TN4", "TN5", "TN6"]}
TN_MATRIX.update({"TN7": ("+", "—", "—"), "TN8": ("+", "—", "—"), "TN9": ("+", "+", "—"), "TN10": ("+", "—", "—")})
MODULES = [("I", "Mexanika", 1, 7), ("II", "Molekulyar fizika va termodinamika", 8, 11), ("III", "Elektr va magnetizm", 12, 18), ("IV", "Optika", 19, 24), ("V", "Atom va yadro fizikasi", 25, 27)]
AREA = {"mex": "Mexanika", "issiq": "Molekulyar fizika va termodinamika", "elektr": "Elektr va magnetizm", "optika": "Optika", "kvant": "Kvant va atom fizikasi"}


def fix_math(html):
    f = lambda m: m.group(0).replace("<", "\\lt ")
    html = re.sub(r"\\\(.*?\\\)", f, html, flags=re.S)
    return re.sub(r"\$\$.*?\$\$", f, html, flags=re.S)


# Oddiy matndagi (formuladan tashqaridagi) "C_k", "ε_max", "U_{z}" kabi belgilar → C<sub>k</sub>.
# Formulalar, kod, skriptlar va teglar ichiga tegilmaydi.
PROTECT = re.compile(r"<script\b.*?</script>|<style\b.*?</style>|<pre\b.*?</pre>|<code\b.*?</code>|<textarea\b.*?</textarea>|<[^>]+>|\$\$.*?\$\$|\\\(.*?\\\)", re.S)
PLAIN_SUB = re.compile(r"(?<![\\A-Za-z])([A-Za-zΑ-Ωα-ω])_(?:\{([^{}<>]+)\}|([A-Za-z0-9À-ž‘’ʻ]+))")


def plain_subs(html):
    rep = lambda m: f"{m.group(1)}<sub>{m.group(2) or m.group(3)}</sub>"
    out, pos = [], 0
    for m in PROTECT.finditer(html):
        out.append(PLAIN_SUB.sub(rep, html[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(PLAIN_SUB.sub(rep, html[pos:]))
    return "".join(out)


def write(name, html):
    html = html_to_new(plain_subs(fix_math(html)))
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


def strip_tags(s):
    return re.sub(r"<[^>]+>|\\\(|\\\)|\\[a-zA-Z]+|[{}$]", "", s)


def shuffled_quiz(items, seed):
    rnd = random.Random(seed); out = []
    for q, opts, a, ex in items:
        idx = list(range(len(opts))); rnd.shuffle(idx)
        out.append((q, [opts[i] for i in idx], idx.index(a), ex))
    return out


def sims_of(x):
    s = x.get("sim")
    return [] if not s else ([s] if isinstance(s, str) else list(s))


def sim_block(sim, uid):
    steps = TOURS.get(sim, [])
    lis = "".join(f"<li data-set='{json.dumps(p)}'>{t}</li>" for p, t in steps)
    tour = (f'<div class="tour-bar"><button class="voice-btn" type="button" data-tour="tour-{uid}">{SPEAKER}<span>Ovozli namoyish</span></button>'
            f'<span class="muted" style="font-size:.82rem">Model o‘zi parametrlarni o‘zgartirib, natijani tushuntiradi; so‘ng boshqaruv sizga o‘tadi.</span></div>'
            f'<div class="tour-cap" aria-live="polite"></div><ol class="vh tour-steps" id="tour-{uid}">{lis}</ol>') if steps else ""
    return f'<div class="sim-wrap"><div class="sim-box" data-sim="{sim}"></div>{tour}</div>'


def tn_chips(tns):
    return "".join(f'<span class="chip g" title="{TN_TEXT[t]}">{t}</span>' for t in tns)


def refs_html(refs, intl, add=()):
    items = [f"[{r}] {BASE_LIT[r]}" for r in refs] + [ADD_LIT[k] for k in add] + [INTL[k] for k in intl]
    return ul(items) + '<p class="muted" style="font-size:.85rem">[1]–[5] — fan dasturidagi asosiy adabiyotlar raqamlanishi. Xalqaro darsliklar (ingliz tilida) mavzuni chuqurlashtirish uchun tavsiya etiladi; OpenStax darsliklari internetda bepul.</p>'


def pager(prev, nxt):
    p = card_link(prev[0], "← Oldingi", prev[1], "") if prev else "<span></span>"
    n = card_link(nxt[0], "Keyingi →", nxt[1], "").replace('class="card"', 'class="card next"') if nxt else "<span></span>"
    return f'<nav class="pager" aria-label="Sahifalar">{p}{n}</nav>'


def lab_label(b):
    s = b["sess"]
    return f"{s[0]}–{s[-1]}" if len(s) > 1 else f"{s[0]}"


def lab_hours(b):
    return 2 * len(b["sess"])


def mod_of(n):
    for r, name, a, z in MODULES:
        if a <= n <= z:
            return r, name


def module_lit(n):
    return {1: "[1, 2, 3]", 7: "[1, 2, 3, 4]", 8: "[2, 3, 4, 5]", 11: "[1, 2, 3, 4]", 12: "[1, 2, 3, 4]"}.get(n)


# ---------------- Ma'ruza sahifalari ----------------
def lecture_page(L):
    n = L["n"]
    sims = sims_of(L)
    labs = [b for b in LABS if b["lec"] == n]
    mts = [(i, t) for i, (t, plan, lec) in enumerate(other.MT, 1) if n in lec]
    toc = [("maqsad", "Maqsad va natijalar"), ("reja", "Reja va tayanch tushunchalar"), ("nazariya", "Nazariy qism"), ("misol", "Ishlangan misollar"), ("model", "Interaktiv model"), ("si", "SI bilan ishlash"), ("xatolar", "Tipik xato tushunchalar"), ("test", "Nazorat testi"), ("blits", "Blits-so‘rov va topshiriqlar"), ("adabiyot", "Adabiyotlar"), ("oqituvchi", "O‘qituvchi uchun")]
    S = []
    S.append(sec("maqsad", 1, "Maqsad va kutilayotgan natijalar", f'<p>{L["goal"]}</p><h3>Mashg‘ulotdan so‘ng talaba:</h3>{ul(L["outcomes"])}<p class="muted">Fan dasturidagi ta’lim natijalari: {", ".join(f"<b>{t}</b> — {TN_TEXT[t]}" for t in L["tn"])}.</p>'))
    terms = "".join(f'<span class="chip c">{t}</span>' for t in L["terms"])
    S.append(sec("reja", 2, "Reja va tayanch tushunchalar", f'{ul(L["plan"], True)}<h3>Tayanch tushunchalar</h3><div class="chips">{terms}</div>'))
    th = "".join(f"<h3>{n}.{k+1}. {h}</h3>{b}" for k, (h, b) in enumerate(L["theory"]))
    if L.get("chem"):
        th += f'<div class="callout info"><b>Kimyogar uchun: fizika va kimyo bog‘liqligi</b>{ul(L["chem"])}</div>'
    S.append(sec("nazariya", 3, "Nazariy qism", th))
    ex = L["example"] if isinstance(L["example"], list) else [L["example"]]
    exh = "".join(f'<div class="example"><div class="ex-h">{k+1}-misol. {et}</div><div class="ex-b"><p><b>Shart.</b> {eg}</p><details><summary>Yechimni ko‘rsatish</summary><p>{es}</p></details></div></div>' for k, (et, eg, es) in enumerate(ex))
    S.append(sec("misol", 4, "Ishlangan misollar", exh + '<div class="callout info"><b>Mustaqil tekshiring</b>Avval yechimni ochmasdan o‘zingiz yeching. So‘ng javobni interaktiv model yoki kalkulyator bilan qayta hisoblang, birliklar (SI) va kattalik tartibini tekshiring.</div>'))
    simh = "".join(f'{"<h3>" + SIMNAME[s] + "</h3>" if len(sims) > 1 else ""}{sim_block(s, f"m{n}{k}")}' for k, s in enumerate(sims))
    phet = ""
    if L.get("phet"):
        phet = '<h3>Qo‘shimcha virtual laboratoriya (PhET, Kolorado universiteti)</h3>' + ul([f'<a href="https://phet.colorado.edu/en/simulations/{slug}" target="_blank" rel="noopener"><span lang="en">{name}</span></a>' for name, slug in L["phet"]])
    S.append(sec("model", 5, "Interaktiv model" + (f": {SIMNAME[sims[0]]}" if len(sims) == 1 else "lar"), f'{simh}<h3>Model bilan topshiriqlar</h3>{ul(L["simtask"], True)}<p class="muted" style="font-size:.85rem">Modellar o‘quv maqsadida soddalashtirilgan (havo qarshiligi, issiqlik yo‘qotishlari va asbob xatoliklari hisobga olinmagan bo‘lishi mumkin). Ularni tajriba natijalari va nazariya bilan solishtiring.</p>{phet}'))
    S.append(sec("si", 6, "Sun’iy intellekt bilan ishlash topshirig‘i", f'<div class="callout ai"><b>Qoidalar</b>SI — tekshirilishi shart bo‘lgan yordamchi. Har bir formula va son darslik yoki mustaqil hisob bilan solishtiriladi. Baholanadigan ishda SI dan qanday foydalanilgani (prompt va tekshiruv) ilova qilinadi.</div>{prompt(f"ai-{n}", L["ai"])}<h3>Javobni tekshirish ro‘yxati</h3>{ul(["Birliklar va o‘lchamlilik to‘g‘rimi (SI)?", "Limit holatlar mantiqiymi (masalan, \\(m\\to0\\), \\(t\\to\\infty\\), \\(\\alpha\\to0\\))?", "Sonlar darslikdagi ishlangan misol bilan mos keladimi?", "Manba ko‘rsatilmagan qiymatlar “taxmin” deb belgilanganmi?"])}'))
    S.append(sec("xatolar", 7, "Tipik xato tushunchalar", table(["Noto‘g‘ri tasavvur", "To‘g‘ri tushuncha"], L["mistakes"])))
    S.append(sec("test", 8, f"Nazorat testi ({len(L['quiz'])} savol, o‘z-o‘zini tekshirish)", quiz(shuffled_quiz(L["quiz"], 1000 + n), f"m{n}") + '<p class="muted" style="font-size:.85rem;margin-top:.6rem">Bu test o‘z-o‘zini tekshirish uchun; rasmiy oraliq nazorat HEMIS’da o‘tkaziladi.</p>'))
    rel = ""
    if labs:
        rel += "<h3>Bog‘liq laboratoriya ishlari</h3>" + ul([f'<a href="lab{b["n"]}.html">{lab_label(b)}-laboratoriya ishi. {b["title"]}</a>' for b in labs])
    if mts:
        rel += "<h3>Bog‘liq mustaqil ta’lim mavzulari</h3>" + ul([f'<a href="mustaqil.html#mt-{i:02d}">MT-{i:02d}. {t}</a>' for i, t in mts])
    S.append(sec("blits", 9, "Blits-so‘rov va bog‘liq topshiriqlar", ul(L["blits"], True) + rel))
    S.append(sec("adabiyot", 10, "Adabiyotlar", refs_html(L["refs"], L["intl"], L.get("add", ()))))
    S.append(f'<section class="doc-sec teacher-note" id="oqituvchi"><h2>O‘qituvchi uchun: 80 daqiqalik dars rejasi</h2>{table(["Vaqt", "Bosqich", "Faoliyat"], [["0–10", "Kirish", "Blits-so‘rov (9-bo‘lim), oldingi mavzu bilan bog‘lash, muammoli savol"], ["10–45", "Nazariya", "3-bo‘lim: asosiy qonunlarni doskada keltirib chiqarish, birliklarni tahlil qilish"], ["45–60", "Model", "5-bo‘lim: modelni proyektorda namoyish qilish; talabalar avval natijani bashorat qiladi, so‘ng tekshiradi"], ["60–72", "Misol", "4-bo‘lim: talabalar juftlikda yechadi, so‘ng yechim ochiladi"], ["72–80", "Yakun", "Nazorat testidan 3–4 savol, tipik xatolar muhokamasi, mustaqil ish topshirig‘i"]])}<p class="muted">Batafsil: <a href="oqituvchi.html">o‘qituvchi qo‘llanmasi</a>.</p></section>')
    prev = (f"lecture{n-1}.html", f"{n-1}-ma’ruza") if n > 1 else ("annotatsiya.html", "Darslik haqida")
    nxt = (f"lecture{n+1}.html", f"{n+1}-ma’ruza") if n < NL else ("laboratoriya.html", "Laboratoriya ishlariga kirish")
    r, mname = mod_of(n)
    chips = [("c", f"M{n}"), ("", "2 akademik soat"), ("v", f"{r}. {mname}"), ("a", "Adabiyot: " + ", ".join(f"[{x}]" for x in L["refs"]))]
    body = head(f"{n}-ma’ruza: {strip_tags(L['short'])}", strip_tags(L["goal"])[:160]) + header("index.html#maruzalar") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("index.html#maruzalar", "Ma’ruzalar"), ("", f"{n}-ma’ruza")], f"{n}-ma’ruza · M{n}", L["title"], "", chips, read="maqsad,reja,nazariya,misol,xatolar") + f'<div class="container" style="padding-top:1rem"><div class="chips">{tn_chips(L["tn"])}</div></div>' + doc(toc, S, pager(prev, nxt)) + "</main>" + footer(sims=True)
    write(f"lecture{n}.html", body)


# ---------------- Laboratoriya sahifalari ----------------
DF_RUBRIC = table(["Daraja", "Ball (20 dan)", "Mezon (fan dasturi bo‘yicha)"], [
    ["Yuqori", "18–20", "Fizik qonunlarning mohiyatini to‘liq tushunadi, kerakli qonuniyatlarni aniq tanlaydi, chizma va zanjir sxemalarini xatosiz chizadi, yechim (o‘lchash va hisoblash) algoritmini mustaqil tuzadi."],
    ["Yetarli", "14–17", "Asosiy qonuniyatlarni yozadi, biroq murakkabroq sxemalar va hisoblash ketma-ketligini tuzishda o‘qituvchi yordamiga tayanadi."],
    ["Minimal", "12–13", "Faqat bitta formulaga qo‘yiladigan eng sodda masalalarni yozadi; chizma va sxemalarni mustaqil tuza olmaydi, qonuniyatni tanlashda adashadi."],
    ["Erishilmagan", "0–11", "Ish shartini tushunmaydi, fizik qonuniyatlarni amaliyot bilan bog‘lay olmaydi, sxema va chizmalarni chiza olmaydi."]])
SAFETY = {
    "mex": ["Yuk va mayatniklarni ehtiyotkorlik bilan osing; tebranayotgan jism yo‘nalishida turmang.", "Shisha idishlar (piknometr, menzurka) bilan ehtiyot bo‘ling; singan shishani qo‘l bilan yig‘mang.", "Asboblarni ish tugagach dastlabki holatiga qaytaring."],
    "issiq": ["Qaynoq suv va qizdirilgan jismlarni faqat qisqich yoki issiqbardosh qo‘lqop bilan ushlang.", "Elektr isitgichni suvsiz yoqmang; shnur va vilkaning butunligini tekshiring.", "Termometrlarni ehtiyot qiling; simob termometri singanda darhol o‘qituvchiga xabar bering."],
    "elektr": ["Zanjirni faqat manba o‘chirilgan holda yig‘ing; o‘qituvchi tekshirmaguncha tokni ulamang.", "Ampermetrni ketma-ket, voltmetrni parallel ulang; o‘lchash chegarasini kattasidan boshlang.", "Izolyatsiyasi shikastlangan simlardan foydalanmang; ish tugagach manbani o‘chiring."],
    "optika": ["Lazer nurini ko‘zga va boshqa talabaga yo‘naltirmang; aks etuvchi sirtlardan ehtiyot bo‘ling.", "Linza va panjaralar sirtini barmoq bilan ushlamang — faqat chetidan tuting.", "Yorug‘lik manbalari (lampa) qiziydi: ularni sovigandan keyin siljiting."],
    "kvant": ["Yuqori kuchlanishli manbalar (fotoelement, Frank–Gers trubkasi) faqat o‘qituvchi ruxsati bilan yoqiladi.", "Simob lampasi ultrabinafsha nur chiqaradi: unga to‘g‘ridan-to‘g‘ri qaramang.", "Kompyuter tajribasida natijalarni faylga saqlang va hisobotga ilova qiling."],
}


def lab_page(b):
    n = b["n"]
    sims = sims_of(b)
    toc = [("maqsad", "Ishning maqsadi"), ("jihoz", "Asbob va jihozlar"), ("nazariy", "Nazariy asos"), ("tartib", "Bajarish tartibi"), ("jadval", "O‘lchash jadvali"), ("hisob", "Hisoblash va xatolik")]
    if sims: toc.append(("model", "Virtual model"))
    toc += [("kod", "Python bilan ishlov"), ("savollar", "Nazorat savollari"), ("xavfsizlik", "Xavfsizlik"), ("baho", "Hisobot va baholash")]
    lec = b["lec"]
    S = [sec("maqsad", 1, "Ishning maqsadi", f'<p>{b["goal"]}</p><p class="muted">Nazariy asos: <a href="lecture{lec}.html">{lec}-ma’ruza</a>. Ta’lim natijalari: {", ".join(f"<b>{t}</b>" for t in b["tn"])}. Hajmi: {lab_hours(b)} akademik soat{" (ikki mashg‘ulot)" if len(b["sess"]) > 1 else ""}.</p><div class="callout info"><b>Tayyorgarlik</b>Mashg‘ulotdan oldin nazariy asos va bajarish tartibini o‘qing, o‘lchash jadvalini daftarga chizib keling. Xatoliklarni hisoblash qoidalari: <a href="laboratoriya.html#xatolik">laboratoriya ishlariga kirish</a>.</div>'),
         sec("jihoz", 2, "Asbob va jihozlar", ul(b["equip"])),
         sec("nazariy", 3, "Nazariy asos", b["theory"]),
         sec("tartib", 4, "Ishni bajarish tartibi", ul(b["steps"], True)),
         sec("jadval", 5, "O‘lchash natijalari jadvali", '<p class="muted">Quyida namunaviy (o‘quv) natijalar keltirilgan. Hisobotda o‘zingiz o‘lchagan qiymatlarni yozing.</p>' + table(b["table"][0], b["table"][1])),
         sec("hisob", 6, "Natijalarni hisoblash va xatolikni baholash", b["calc"])]
    if sims:
        simh = "".join(f'{"<h3>" + SIMNAME[s] + "</h3>" if len(sims) > 1 else ""}{sim_block(s, f"l{n}{k}")}' for k, s in enumerate(sims))
        S.append(sec("model", 7, "Virtual model (tayyorgarlik va tekshiruv uchun)", simh + '<p class="muted" style="font-size:.85rem">Virtual model haqiqiy tajribaning o‘rnini bosmaydi: undan bashorat qilish va natijangizni tekshirish uchun foydalaning.</p>'))
    k = len(S)
    S.append(sec("kod", k + 1, "Kompyuterda ishlov berish (Python)", f'<p class="muted">Kodni Google Colab yoki Jupyter’da ishga tushiring, namunaviy sonlar o‘rniga o‘z o‘lchovlaringizni kiriting va natijani qo‘lda hisob bilan solishtiring.</p>{code(f"code-{n}", b["code"])}'))
    S.append(sec("savollar", k + 2, "Nazorat savollari", ul(b["questions"], True)))
    S.append(sec("xavfsizlik", k + 3, "Xavfsizlik texnikasi", ul(SAFETY[b["area"]] + ["Laboratoriyada ovqatlanish, telefonni asbob ustiga qo‘yish va ruxsatsiz asbobni yoqish taqiqlanadi."])))
    S.append(sec("baho", k + 4, "Hisobot va baholash", '<h3>Hisobot tarkibi</h3>' + ul(["Ish nomi, maqsadi, asbob va jihozlar ro‘yxati", "Qurilma (zanjir) sxemasi va asosiy hisoblash formulasi", "O‘lchash natijalari jadvali (birliklari bilan)", "Hisoblash, absolyut va nisbiy xatolik; natija \\(x=\\bar x\\pm\\Delta x\\) ko‘rinishida", "Grafik (zarur bo‘lsa) va xulosa: natijani jadvaldagi qiymat bilan taqqoslash, xatolik manbalari"], True) + "<h3>Laboratoriya mashg‘ulotlaridagi faollik (JN tarkibidagi 20 ball)</h3>" + DF_RUBRIC + '<p class="muted" style="font-size:.85rem">Fan dasturiga ko‘ra laboratoriya mashg‘ulotlaridagi faollik (DF) semestr davomida jami 20 ball bilan baholanadi. Rasmiy ball HEMIS’da qo‘yiladi.</p>'))
    i = LABS.index(b)
    prev = (f"lab{LABS[i-1]['n']}.html", f"{lab_label(LABS[i-1])}-laboratoriya") if i > 0 else ("laboratoriya.html", "Laboratoriyaga kirish")
    nxt = (f"lab{LABS[i+1]['n']}.html", f"{lab_label(LABS[i+1])}-laboratoriya") if i < len(LABS) - 1 else ("mustaqil.html", "Mustaqil ta’lim")
    chips = [("c", "L" + lab_label(b).replace("–", "–L")), ("", f"{lab_hours(b)} akademik soat"), ("v", AREA[b["area"]]), ("a", f"Ma’ruza: M{lec}")]
    body = head(f"{lab_label(b)}-laboratoriya ishi: {strip_tags(b['title'])}", strip_tags(b["goal"])[:160]) + header("index.html#laboratoriya") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("index.html#laboratoriya", "Laboratoriya"), ("", f"L{lab_label(b)}")], f"{lab_label(b)}-laboratoriya ishi", b["title"], "", chips, read="maqsad,nazariy,tartib") + f'<div class="container" style="padding-top:1rem"><div class="chips">{tn_chips(b["tn"])}</div></div>' + doc(toc, S, pager(prev, nxt)) + "</main>" + footer(sims=bool(sims))
    write(f"lab{n}.html", body)
    for s in b["sess"][1:]:
        redirect(f"lab{s}.html", f"lab{n}.html", f"{lab_label(b)}-laboratoriya ishi")


def redirect(name, target, title):
    depth = name.count("/")
    pre = "../" * depth
    html = f"""<!doctype html><html lang="uz"><head><meta charset="UTF-8"><title>{esc(title)} — {SITE}</title><meta http-equiv="refresh" content="0; url={pre}{target}"><link rel="canonical" href="{pre}{target}"><meta name="robots" content="noindex"></head><body><p>Sahifa ko‘chirildi: <a href="{pre}{target}">{esc(title)}</a></p></body></html>
"""
    write(name, html)


def lab_intro_page():
    I = INTRO
    toc = [(sid, t) for sid, t, _ in I["sections"]] + [("test", "O‘z-o‘zini tekshirish")]
    S = [sec(sid, k + 1, t, b) for k, (sid, t, b) in enumerate(I["sections"])]
    S.append(sec("test", len(S) + 1, "O‘z-o‘zini tekshirish testi", quiz(shuffled_quiz(I["quiz"], 77), "lab0")))
    body = head("Laboratoriya ishlariga kirish", "O‘lchash xatoliklari, natijalarni qayta ishlash, xavfsizlik va hisobot talablari") + header("index.html#laboratoriya") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("index.html#laboratoriya", "Laboratoriya"), ("", "Kirish")], "Laboratoriya praktikumi · 66 soat", "Laboratoriya ishlariga kirish: o‘lchash va xatoliklar", "Fizik kattaliklarni o‘lchash, xatoliklarni baholash (GUM), grafik qurish, xavfsizlik qoidalari va hisobot talablari.", [("c", "33 mashg‘ulot"), ("", "29 ta ish"), ("g", "TN2, TN6, TN8")], read=",".join(s[0] for s in I["sections"][:3])) + doc(toc, S, pager(("lecture27.html", "27-ma’ruza"), (f"lab{LABS[0]['n']}.html", "1-laboratoriya ishi"))) + "</main>" + footer()
    write("laboratoriya.html", body)


# ---------------- Bosh sahifa ----------------
def index_page():
    mods = ""
    for r, name, a, z in MODULES:
        cards = "".join(card_link(f"lecture{L['n']}.html", f"{L['n']}-ma’ruza", L["short"], strip_tags(L["goal"])[:115] + "…") for L in LECT if a <= L["n"] <= z)
        mods += f'<h3 class="mod-h" style="margin:1.6rem 0 .8rem">{r}. {name} <span class="muted" style="font-weight:500;font-size:.9rem">· M{a}–M{z}</span></h3><div class="grid grid-3">{cards}</div>'
    lab_cards = card_link("laboratoriya.html", "Kirish", "O‘lchash, xatoliklar va xavfsizlik", "Laboratoriya ishlaridan oldin o‘qiladi: GUM, Styudent koeffitsiyenti, grafik, hisobot.")
    lab_cards += "".join(card_link(f"lab{b['n']}.html", f"L{lab_label(b)}", b["title"], f"{AREA[b['area']]} · M{b['lec']} · {lab_hours(b)} soat") for b in LABS)
    allsims = {}
    for L in LECT:
        for s in sims_of(L): allsims.setdefault(s, f"lecture{L['n']}.html")
    for b in LABS:
        for s in sims_of(b): allsims.setdefault(s, f"lab{b['n']}.html")
    steps = [("1", "Diagnostika", "Blits-so‘rov va o‘z-o‘zini tekshirish testi orqali boshlang‘ich bilimni aniqlash."), ("2", "Nazariya", "Asosiy qonunlar keltirib chiqariladi, birliklar va qo‘llanish chegaralari ko‘rsatiladi."), ("3", "Interaktiv model", f"{len(SIMNAME)} ta brauzer modeli: parametrni o‘zgartiring, bashorat qiling, tekshiring."), ("4", "Masala", "Ishlangan misollar va tipik xatolar tahlili."), ("5", "Laboratoriya", "O‘lchash, xatolikni baholash va Python bilan natijani qayta ishlash."), ("6", "Taqdimot va keys", "Mustaqil ta’lim: 45 mavzu bo‘yicha taqdimot va amaliy keys-stadi.")]
    st = "".join(f'<article class="card"><span class="badge">QADAM {a}</span><h3>{b}</h3><p class="muted">{c}</p></article>' for a, b, c in steps)
    html = head("Bosh sahifa", f"Umumiy fizika — bakalavriat uchun interaktiv ovozli elektron darslik: 27 ma’ruza, 33 laboratoriya mashg‘uloti, 45 mustaqil ta’lim mavzusi, {len(SIMNAME)} interaktiv model.") + header() + f"""<main id="main">
<section class="hero"><div class="container"><div class="eyebrow">60530100 — Kimyo · Bakalavriat · {CODE} · 1–2-semestr</div><h1>Tabiat qonunlarini <span>tushuning, o‘lchang va modellashtiring.</span></h1><p class="lead">Mexanikadan atom yadrosigacha — fan dasturi asosidagi ochiq interaktiv elektron darslik: har bir ma’ruza ovozli o‘qiladi, formulalar so‘z bilan aytiladi, har bir qonunni brauzerdagi modelda sinab ko‘rish mumkin. Baholash va rasmiy topshirish HEMIS orqali amalga oshiriladi.</p>
<div class="grid grid-4" style="margin-top:2rem"><div class="card"><div class="eyebrow">01</div><h3>27 ta ma’ruza</h3><p class="muted">54 soat: nazariya, ishlangan misollar, ovozli o‘qish va 10 savolli test.</p></div><div class="card"><div class="eyebrow">02</div><h3>{len(LABS)} ta laboratoriya ishi</h3><p class="muted">66 soat (33 mashg‘ulot): tartib, jadval, xatolik hisobi va Python.</p></div><div class="card"><div class="eyebrow">03</div><h3>45 ta mustaqil ish</h3><p class="muted">180 soat: taqdimot rejalari va keys-stadi banki.</p></div><div class="card"><div class="eyebrow">04</div><h3>{len(SIMNAME)} ta model</h3><p class="muted">Brauzerda ishlaydigan, ovozli namoyishli interaktiv modellar.</p></div></div></div></section>
<section id="darslik" class="section"><div class="container"><div class="section-head"><div class="eyebrow">Darslik haqida</div><h2>Annotatsiya, baholash va ilovalar</h2><p class="muted">10 ECTS kredit (300 soat), 1–2-semestr. Darslik fan dasturi, ECTS va xalqaro sifat mezonlariga muvofiq tuzilgan.</p></div><div class="grid grid-3">
{card_link("annotatsiya.html", "Kirish", "Annotatsiya, mundarija va xalqaro standartlar", "Bibliografik ma’lumot, uch tildagi annotatsiya, ta’lim natijalari va sifat mezonlariga muvofiqlik.")}
{card_link("baholash.html", "Baholash", "JN · ON · YaN rubrikalari", "100 ballik tizim, saralash ballari, TN–nazorat matritsasi va baho kalkulyatori.")}
{card_link("oqituvchi.html", "O‘qituvchi", "O‘qituvchi uchun qo‘llanma", "30 haftalik taqvim, dars rejasi shablonlari, laboratoriyani tashkil etish va SI siyosati.")}
{card_link("mustaqil.html", "Mustaqil ta’lim", "45 mavzu va keys-stadi banki", "Har bir mavzu uchun reja, manbalar va taqdimot talablari; kimyo va texnikaga oid keyslar.")}
{card_link("glossariy.html", "1-ilova", "Atamalar lug‘ati", f"{len(other.GLOSS)} ta atama: o‘zbekcha–ruscha–inglizcha, qisqa ta’rif va mavzu havolasi.")}
{card_link("vositalar.html", "2-ilova", "Dasturiy vositalar", "PhET, Python, Tracker, GeoGebra va boshqa bepul vositalar.")}
</div></div></section>
<section id="model" class="section"><div class="container"><div class="section-head"><div class="eyebrow">O‘quv modeli</div><h2>Har bir mavzu bo‘yicha olti qadam</h2><p class="muted">Nazariya, interaktiv model, masala va laboratoriya tajribasi bitta o‘quv sikliga birlashtirilgan.</p></div><div class="grid grid-3">{st}</div></div></section>
<section id="maruzalar" class="section"><div class="container"><div class="section-head"><div class="eyebrow">Ma’ruzalar · 54 soat</div><h2>27 ta ma’ruza — besh modul</h2><p class="muted">Har bir ma’ruza sahifasida “Tinglash” tugmasi bor: matn tabiiy o‘zbekcha ovozda o‘qiladi.</p></div>{mods}</div></section>
<section id="laboratoriya" class="section"><div class="container"><div class="section-head"><div class="eyebrow">Laboratoriya mashg‘ulotlari · 66 soat</div><h2>{len(LABS)} ta laboratoriya ishi (33 mashg‘ulot)</h2><p class="muted">Har birida asbob-jihozlar, bajarish tartibi, namunaviy o‘lchash jadvali, xatolik hisobi, Python kodi va nazorat savollari.</p></div><div class="grid grid-3">{lab_cards}</div></div></section>
<section id="simulyatorlar" class="section"><div class="container"><div class="section-head"><div class="eyebrow">Interaktiv modellar</div><h2>Fizik jarayonlar simulyatorlari</h2><p class="muted">Quyida ikkita model; barchasi <a href="simulyatorlar.html">simulyatorlar sahifasida</a>.</p></div>
{sim_block("projectile", "i1")}<div style="margin-top:1.4rem">{sim_block("lens", "i2")}</div></div></section>
<section id="ai-lab" class="section"><div class="container"><div class="section-head"><div class="eyebrow">SI integratsiyasi</div><h2>Prompt generatori</h2><p class="muted">Mavzu va rolni tanlang — tekshiruv qoidalari kiritilgan tayyor prompt hosil bo‘ladi.</p></div><div class="grid grid-2"><div class="card"><label class="control">Mavzu<select id="p-topic">{''.join(f'<option>{strip_tags(L["short"])}</option>' for L in LECT)}</select></label><label class="control" style="margin-top:.8rem">Daraja<select id="p-level"><option>Boshlang‘ich</option><option selected>O‘rta</option><option>Ilg‘or</option></select></label><label class="control" style="margin-top:.8rem">Rol<select id="p-role"><option value="student">talaba</option><option value="teacher">o‘qituvchi</option></select></label><button class="primary" id="gen-prompt" style="margin-top:1rem" type="button">Prompt yaratish</button></div><div class="card"><div class="prompt-box"><button class="secondary copy" type="button" data-copy="p-out">Nusxalash</button><pre id="p-out">Prompt shu yerda ko‘rinadi…</pre></div></div></div></div></section>
<section id="hemis" class="section"><div class="container"><div class="card" style="border-left:4px solid #38bdf8"><div class="eyebrow">Rasmiy jarayonlar</div><h2>Baholash va topshiriqlarni topshirish — HEMIS’da</h2><p class="muted">Ushbu sayt ochiq o‘quv materiallari to‘plami bo‘lib, hisob yaratmaydi va baho qo‘ymaydi. Mustaqil ta’lim topshiriqlari (1-MT, 2-MT), oraliq nazorat testi (12-hafta) va yakuniy nazorat natijalari universitetning HEMIS axborot tizimida belgilangan tartibda yuritiladi.</p></div></div></section>
<section id="muallif" class="section"><div class="container"><div class="card author-card"><div class="author-info"><div class="eyebrow">Muallif</div><h2>{AUTHOR_FULL}</h2><p class="author-role">Elektron darslik muallifi</p><p class="muted">Qo‘qon davlat universiteti, Fizika va astronomiya kafedrasi.</p><p class="muted">Fan dasturini tuzuvchilar: Meliqo‘ziyev Dadaqo‘zi Jo‘raqo‘ziyevich (PhD), Mirsultonov Ilhomjon Mirzaxakimovich (PhD). Taqrizchilar: N.X. Yo‘ldoshev — f.-m.f.d., professor (Farg‘ona davlat texnika universiteti); F.O. Dadaboyeva — p.f.f.d. (PhD), dotsent (Qo‘qon davlat universiteti).</p><p class="muted" style="font-size:.85rem">Dizayn va tuzilma: I.M. Eshboltayevning “Yarimo‘tkazgich asboblar fizikasi” interaktiv elektron darsligi asosida.</p></div></div></div></section>
</main>""" + footer(sims=True)
    write("index.html", html)


# ---------------- Simulyatorlar ----------------
def sims_page():
    used = {}
    for L in LECT:
        for s in sims_of(L): used.setdefault(s, []).append((f"lecture{L['n']}.html#model", f"M{L['n']}"))
    for b in LABS:
        for s in sims_of(b): used.setdefault(s, []).append((f"lab{b['n']}.html#model", f"L{lab_label(b)}"))
    groups = [("Mexanika", ["vernier", "kinem", "projectile", "newton", "spring", "beam", "collision", "rotation", "oscill"]), ("Molekulyar fizika va termodinamika", ["maxwell", "gas", "calorimeter", "capillary", "archimedes"]), ("Elektr va magnetizm", ["coulomb", "capacitor", "circuit", "kirchhoff", "wheatstone", "vacdiode", "bfield", "induction", "rlc", "ac"]), ("Optika", ["young", "grating", "malus", "lens", "snell", "planck", "photo", "photometry"]), ("Atom va yadro fizikasi", ["bohr", "franck", "decay", "binding"])]
    S, toc = [], []
    for k, (g, keys) in enumerate(groups, 1):
        cards = "".join(f'<div class="card"><span class="badge">model</span><h3>{SIMNAME[s]}</h3><p class="muted">{" · ".join(f"<a href=\"{h}\">{t}</a>" for h, t in used.get(s, []))}</p></div>' for s in keys)
        S.append(sec(f"g{k}", k, g, f'<div class="grid grid-3">{cards}</div>'))
        toc.append((f"g{k}", g))
    S.append(sec("demo", len(groups) + 1, "Namoyish: tebranishlar va fotoeffekt", sim_block("oscill", "s1") + '<div style="margin-top:1.4rem"></div>' + sim_block("photo", "s2")))
    toc.append(("demo", "Namoyish modellari"))
    html = head("Simulyatorlar", f"{len(SIMNAME)} ta interaktiv fizik model: mexanika, termodinamika, elektr, optika, atom fizikasi") + header("simulyatorlar.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Simulyatorlar")], "Interaktiv modellar", "Fizik jarayonlar simulyatorlari", "Har bir model tegishli ma’ruza yoki laboratoriya sahifasida ochiladi; modellar internetsiz ham ishlaydi.", [("c", f"{len(SIMNAME)} model"), ("v", "Ovozli namoyish")]) + doc(toc, S) + "</main>" + footer(sims=True)
    write("simulyatorlar.html", html)


# ---------------- Annotatsiya ----------------
def annot_page():
    toc = [("bib", "Bibliografik ma’lumot"), ("ann", "Annotatsiya (uz/ru/en)"), ("soz", "So‘z boshi"), ("fan", "Fan ma’lumotlari"), ("tn", "Ta’lim natijalari"), ("std", "Xalqaro standartlar"), ("mund", "Mundarija"), ("adab", "Adabiyotlar"), ("foyd", "Foydalanish tavsiyalari")]
    S = []
    S.append(sec("bib", 1, "Bibliografik ma’lumot", f"""<p><b>{AUTHOR}</b> Umumiy fizika: interaktiv ovozli elektron darslik (bakalavriat, 60530100 — Kimyo). — Qo‘qon: Qo‘qon davlat universiteti, 2026.</p>
<p><b>Fan dasturini tuzuvchilar:</b> Meliqo‘ziyev Dadaqo‘zi Jo‘raqo‘ziyevich — QDU Fizika va astronomiya kafedrasi o‘qituvchisi, PhD; Mirsultonov Ilhomjon Mirzaxakimovich — QDU Fizika va astronomiya kafedrasi o‘qituvchisi, PhD.</p>
<p><b>Taqrizchilar:</b> N.X. Yo‘ldoshev — fizika-matematika fanlari doktori, professor (Farg‘ona davlat texnika universiteti, “Fizika” kafedrasi); F.O. Dadaboyeva — pedagogika fanlari bo‘yicha falsafa doktori (PhD), dotsent (Qo‘qon davlat universiteti, “Fizika va astronomiya” kafedrasi).</p>
<p class="muted">Darslik “Umumiy fizika” fanining 2026/2027 o‘quv yili uchun tasdiqlangan o‘quv dasturi ({CODE}) asosida tayyorlangan. Fan dasturi Tabiiy fanlar va iqtisodiyot fakulteti Kengashida ma’qullangan, elektron imzo bilan tasdiqlangan (cams.kokandsu.uz, ID: 2397).</p>"""))
    S.append(sec("ann", 2, "Annotatsiya", """<h3>O‘zbekcha</h3><p>Elektron darslikda umumiy fizika kursining besh bo‘limi — mexanika, molekulyar fizika va termodinamika, elektr va magnetizm, optika, atom va yadro fizikasi — fan dasturidagi 27 ta ma’ruza, 33 ta laboratoriya mashg‘uloti va 45 ta mustaqil ta’lim mavzusi asosida bayon etilgan. Har bir ma’ruza maqsad va ta’lim natijalari, nazariy qism, ishlangan misollar, interaktiv model, sun’iy intellekt bilan ishlash topshirig‘i, tipik xato tushunchalar tahlili, 10 savolli test va adabiyotlardan iborat; matn tabiiy o‘zbekcha ovozda tinglanadi. Laboratoriya ishlari o‘lchash xatoliklarini xalqaro GUM tavsiyalari asosida baholash va natijalarni Python bilan qayta ishlashni o‘z ichiga oladi. Darslik kimyo yo‘nalishi talabalari va o‘qituvchilar uchun mo‘ljallangan.</p>
<div lang="ru"><h3>Русский</h3><p>В электронном учебнике изложены пять разделов курса общей физики — механика, молекулярная физика и термодинамика, электричество и магнетизм, оптика, атомная и ядерная физика — в соответствии с 27 лекциями, 33 лабораторными занятиями и 45 темами самостоятельной работы учебной программы. Каждая лекция содержит цели и результаты обучения, теорию, решённые примеры, интерактивную модель, задание с использованием ИИ, разбор типичных ошибок, тест из 10 вопросов и список литературы; текст озвучен естественным узбекским голосом. Лабораторные работы включают оценку погрешностей по рекомендациям GUM и обработку результатов на Python. Учебник предназначен для студентов направления «Химия» и преподавателей.</p></div>
<div lang="en"><h3>English</h3><p>This interactive, voice-enabled e-textbook covers the five parts of the general physics course — mechanics, molecular physics and thermodynamics, electricity and magnetism, optics, atomic and nuclear physics — following the 27 lectures, 33 laboratory sessions and 45 independent-study topics of the approved syllabus. Each lecture includes learning objectives and outcomes, theory, worked examples, an interactive model, an AI-assisted task, an analysis of common misconceptions, a 10-question quiz and references; the text can be listened to in natural Uzbek speech. Laboratory work includes uncertainty evaluation following the GUM and data processing in Python. It is intended for Chemistry undergraduates and instructors.</p></div>"""))
    S.append(sec("soz", 3, "So‘z boshi", "<p>Kimyogar uchun fizika — bu moddaning tuzilishi va o‘zgarishini tushunish tili: gaz qonunlari va termodinamika reaksiyalar energetikasini, elektr va magnetizm elektrokimyo va spektroskopiyani, optika va kvant fizikasi esa zamonaviy tahlil usullarini (spektrofotometriya, rentgen-struktura tahlili, YaMR) tushuntiradi. Shu sababli har bir mavzuda “Kimyogar uchun” izohi berilgan.</p><p>Darslik fizik modeldan o‘lchanadigan natijagacha bo‘lgan yo‘lni takrorlaydi: hodisa → qonun → formula → son → grafik → tajriba. Interaktiv modellar parametrlar natijaga qanday ta’sir qilishini bevosita ko‘rish imkonini beradi, laboratoriya ishlari esa natijani o‘lchash xatoligi bilan birga asoslashga o‘rgatadi. Sun’iy intellekt vositalari yordamchi sifatida, aniq tekshiruv qoidalari bilan kiritilgan.</p>"))
    S.append(sec("fan", 4, "Fan ma’lumotlari", table(["Ko‘rsatkich", "Qiymat"], [["Fan nomi / kodi", f"Umumiy fizika (Общая физика) / {CODE}"], ["Ta’lim yo‘nalishi", "60530100 — Kimyo (kunduzgi ta’lim), o‘quv rejadagi tartib raqami 1.11"], ["Bilim / ta’lim sohasi", "500 000 — Tabiiy fanlar, matematika va statistika / 530 000 — Fizika va tabiiy fanlar"], ["O‘quv yili / semestr", "2026/2027 / 1–2-semestr"], ["ECTS kreditlar", "10 (jami 300 soat)"], ["Jami yuklama", "Auditoriya 120 soat: ma’ruza 54, laboratoriya 66; mustaqil ta’lim 180 soat"], ["Haftalik auditoriya soati", "4"], ["Fan turi / o‘qitish tili (dastur bo‘yicha)", "Majburiy / rus tili; darslik tili — o‘zbek (UZ/RU/EN tarjima tugmalari mavjud)"], ["Baholash", "JN 30 + ON 20 + YaN 50 = 100 ball; saralash 18/12/30"]]) + "<h3>Maqsad va vazifalar</h3><p><b>Fanning maqsadi</b> — talabalarni makro va mikrodunyodagi harakat va uning turlari, modda tuzilishi va xossalari, turli agregat holatlardagi makroskopik tizimlarning (alohida jismlar va maydonlar uchun) fizik xossalari, Koinot obyektlari va hodisalari haqidagi zarur ilmiy tasavvurlar, bilim va tushunchalar bilan qurollantirish hamda ularda fenomenologik bilim, ko‘nikma va malakalarni shakllantirish.</p><p><b>Fanning vazifasi</b> — talabalarda umumiy fizika kursi bo‘limlari bo‘yicha masala yechish ko‘nikmasini, laboratoriya ishlarini tushunish va ular bo‘yicha xulosa chiqara olishni, shuningdek fizik qonuniyatlar va munosabatlarni to‘g‘ri aniqlashni shakllantirish.</p><h3>Boshlang‘ich bilimlar (prerekvizitlar)</h3>" + ul(["Umumiy fizika (UMF11210) — maktab fizika kursi asosida", "Umumiy psixologiya (UMP1106)", "Oliy matematika (OMT11208): hosila, integral, vektorlar"]) + "<h3>Ta’lim texnologiyalari</h3>" + ul(["Ma’ruzalar (multimedia, ovozli o‘qish, interaktiv modellar)", "Laboratoriya ishlarini bajarish va tahlil qilish", "Interaktiv keys-stadilar", "Blits-so‘rov", "Guruhlarda ishlash", "Taqdimotlar o‘tkazish", "Jamoaviy ish va himoya uchun loyihalar"])))
    S.append(sec("tn", 5, "Ta’lim natijalari (TN1–TN10)", "<p>TN1–TN5 — kasbiy kompetensiyalar, TN6–TN10 — ko‘nikmalar (fan dasturi, 4-bo‘lim). Jadvalda har bir natija darslikning qaysi sahifalarida shakllantirilishi ko‘rsatilgan.</p>" + table(["Kod", "Natija", "Darslikdagi mavzular"], [[t, TN_TEXT[t], ", ".join([f'<a href="lecture{L["n"]}.html">M{L["n"]}</a>' for L in LECT if t in L["tn"]] + [f'<a href="lab{b["n"]}.html">L{lab_label(b)}</a>' for b in LABS if t in b["tn"]]) or "Mustaqil ta’lim, keys-stadi"] for t in TN_TEXT])))
    S.append(sec("std", 6, "Xalqaro ta’lim talablariga muvofiqlik", "<p>Darslik quyidagi xalqaro mezonlar asosida loyihalangan. Jadvalda har bir mezon darslikda qanday amalga oshirilgani ko‘rsatilgan.</p>" + table(["Mezon", "Talab", "Darslikda amalga oshirilishi"], [
        ["ECTS Users’ Guide (2015), Bolonya jarayoni", "Ta’lim natijalari va kredit yuklamasi aniq; 1 kredit ≈ 25–30 soat", "10 ECTS = 300 soat; har bir mavzu TN kodlariga bog‘langan; mustaqil ta’lim soatlari ko‘rsatilgan"],
        ["Dublin deskriptorlari (1-bosqich — bakalavriat)", "Bilim va tushunish, qo‘llash, mustaqil xulosa, kommunikatsiya, o‘rganish ko‘nikmasi", "Nazariya + misol (bilim), model, masala va laboratoriya (qo‘llash), keys-stadi (xulosa), taqdimot himoyasi (kommunikatsiya)"],
        ["Konstruktiv moslashuv (Biggs) va Blum taksonomiyasi", "Natija → faoliyat → baholash bir-biriga mos", "TN–nazorat matritsasi (baholash sahifasi); “eslash”dan “baholash/yaratish”gacha bo‘lgan topshiriqlar"],
        ["Fizika ta’limi tadqiqotlari (PER): faol o‘rganish", "Bashorat → kuzatish → tushuntirish, xato tushunchalar bilan ishlash", "Har bir ma’ruzada interaktiv model, POE topshiriqlari va “Tipik xato tushunchalar” bo‘limi"],
        ["Quality Matters (QM) — oliy ta’lim kurs dizayni rubrikasi", "Aniq maqsadlar, o‘lchanadigan natijalar, ochiq baholash mezonlari, faol o‘rganish, qulaylik", "Har bir sahifada maqsad va natijalar; rubrikalar ochiq; modellar va testlar; mundarija va navigatsiya"],
        ["JCGM 100:2008 (GUM) — o‘lchash noaniqligi", "Natija noaniqlik bilan birga, yagona qoidalar asosida beriladi", "Laboratoriyaga kirish sahifasi: A va B turdagi noaniqlik, Styudent koeffitsiyenti, bilvosita o‘lchash; har bir ishda xatolik hisobi"],
        ["SI birliklar tizimi (BIPM, 9-nashr, 2019)", "Kattaliklar va birliklarning bir xil yozilishi", "Barcha misollarda SI birliklari; asosiy doimiylar CODATA qiymatlarida"],
        ["WCAG 2.2 AA (veb-qulaylik)", "Kontrast, klaviatura bilan boshqarish, matnli muqobil, ovozli o‘qish", "“Asosiy mazmunga o‘tish” havolasi, fokus belgisi, aria-yorliqlar, ovozli o‘qish, kun/tun rejimi, chop etish uslubi"],
        ["UNESCO OER tavsiyasi (2019)", "Ochiq, qayta foydalaniladigan o‘quv resurslari", "Ro‘yxatdan o‘tishsiz kirish, manba kodi GitHub’da; formulalar va modellar internetsiz ham ishlaydi"],
        ["Akademik halollik va SI dan mas’uliyatli foydalanish", "SI yordamini oshkor qilish, natijani tekshirish", "Har bir ma’ruzada SI topshirig‘i tekshiruv ro‘yxati bilan; baholanadigan ishda prompt ilova qilinadi"],
        ["Xalqaro dasturlar bilan qiyoslash", "Mazmunni yetakchi universitet kurslari bilan solishtirish", "Mavzular qamrovi Halliday–Resnick–Walker, Young–Freedman, OpenStax University Physics darsliklari va MIT OCW materiallari bilan muvofiqlashtirilgan"]])
        + '<p class="muted" style="font-size:.85rem">Eslatma: jadval darslik dizayni qaysi mezonlarga yo‘naltirilganini ko‘rsatadi; rasmiy akkreditatsiya yoki sertifikatlashni anglatmaydi.</p>'))
    mund = ""
    for r, name, a, z in MODULES:
        mund += f"<h3>{r}. {name}</h3>" + ul([f'<a href="lecture{L["n"]}.html">{L["n"]}-ma’ruza. {L["title"]}</a>' for L in LECT if a <= L["n"] <= z])
    mund += "<h3>Laboratoriya ishlari</h3>" + ul(['<a href="laboratoriya.html">Laboratoriya ishlariga kirish: o‘lchash va xatoliklar</a>'] + [f'<a href="lab{b["n"]}.html">{lab_label(b)}. {b["title"]}</a>' for b in LABS])
    mund += "<h3>Mustaqil ta’lim va baholash</h3>" + ul(['<a href="mustaqil.html">45 ta mustaqil ta’lim mavzusi va keys-stadi banki</a>', '<a href="baholash.html">Baholash rubrikalari va kalkulyator</a>', '<a href="oqituvchi.html">O‘qituvchi uchun qo‘llanma</a>', '<a href="simulyatorlar.html">Interaktiv modellar</a>']) + "<h3>Ilovalar</h3>" + ul(['<a href="glossariy.html">1-ilova. Atamalar lug‘ati</a>', '<a href="vositalar.html">2-ilova. Dasturiy vositalar</a>'])
    S.append(sec("mund", 7, "Mundarija", mund))
    lit = "<h3>Asosiy adabiyotlar (fan dasturi)</h3>" + ul([f"[{k}] {v}" for k, v in BASE_LIT.items()]) + "<h3>Qo‘shimcha adabiyotlar (fan dasturi)</h3>" + ul(list(ADD_LIT.values())) + "<h3>Axborot resurslari</h3>" + ul([f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for u, t in WEB]) + "<h3>Xalqaro darsliklar va standartlar (tavsiya)</h3>" + ul(list(INTL.values()))
    S.append(sec("adab", 8, "Adabiyotlar va axborot resurslari", lit))
    S.append(sec("foyd", 9, "Foydalanish tavsiyalari", ul(["<b>Talabaga:</b> ma’ruza sahifasini tartib bilan o‘qing yoki tinglang; ishlangan misolni yechimni ochmasdan avval o‘zingiz yeching; modelda bashorat qiling, keyin tekshiring; testni oxirida bajaring.", "<b>Tinglash:</b> sarlavha yonidagi “Tinglash” tugmasi matnni tabiiy o‘zbekcha ovozda o‘qiydi; istalgan xatboshini bosib, o‘sha joydan davom ettirish mumkin.", "<b>Laboratoriyaga:</b> har bir ishdan oldin “Laboratoriya ishlariga kirish” sahifasidagi xatolik qoidalarini takrorlang.", "<b>O‘qituvchiga:</b> har bir ma’ruza oxirida 80 daqiqalik dars rejasi berilgan; modellarni proyektorda namoyish qilish mumkin.", "<b>Chop etish:</b> brauzerda Ctrl+P — interaktiv elementlarsiz toza matn chiqadi (PDF sifatida saqlash mumkin).", "<b>Rasmiy topshirish</b> faqat HEMIS’da."])))
    html = head("Darslik haqida", "Annotatsiya, fan ma’lumotlari, ta’lim natijalari va xalqaro standartlarga muvofiqlik") + header("annotatsiya.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Darslik haqida")], "Kirish", "Annotatsiya, so‘z boshi va mundarija", "Bibliografik ma’lumot, uch tildagi annotatsiya, fan ma’lumotlari, ta’lim natijalari va xalqaro ta’lim talablariga muvofiqlik.", [("c", "10 ECTS"), ("", "300 soat"), ("g", "TN1–TN10")]) + doc(toc, S) + "</main>" + footer()
    write("annotatsiya.html", html)


# ---------------- Mustaqil ta'lim ----------------
def mustaqil_page():
    items = []
    for i, (t, plan, lec) in enumerate(other.MT, 1):
        links = ", ".join(f'<a href="lecture{m}.html">M{m}</a>' for m in lec)
        items.append(f'<details class="mt-item" id="mt-{i:02d}"><summary><span class="badge">MT-{i:02d}</span> {t} <span class="muted" style="margin-left:auto;font-weight:500">4 soat</span></summary><div class="body"><b>Taqdimot rejasi:</b>{ul(plan)}<p class="muted">Bog‘liq ma’ruza: {links}. Manbalar: fan dasturidagi [1]–[5], <a href="glossariy.html">lug‘at</a> va xalqaro darsliklar. Hajmi: 10–12 slayd, kamida bitta chizma yoki grafik, kamida 3 manba.</p></div></details>')
    keys = "".join(f'<div class="example"><div class="ex-h">{t}</div><div class="ex-b"><p>{d}</p><p class="tn">{", ".join(tn)}</p></div></div>' for t, d, tn in other.KEYS)
    toc = [("umumiy", "Umumiy talablar"), ("mavzular", "45 ta mavzu"), ("taqdimot", "1-MT: taqdimot talablari"), ("keys", "2-MT: keys-stadi banki"), ("halollik", "Akademik halollik")]
    S = [sec("umumiy", 1, "Umumiy talablar", table(["Ko‘rsatkich", "Qiymat"], [["Jami hajm", "180 soat (45 mavzu × 4 soat)"], ["1-MT", "Taqdimot va uning himoyasi — 5 ball (HEMIS’ga yuklash)"], ["2-MT", "Keys-stadi tahlili va yechimi — 5 ball (HEMIS’ga yuklash)"], ["Mavzuni tanlash", "O‘qituvchi tomonidan guruh ro‘yxati bo‘yicha taqsimlanadi (bir mavzu — bir talaba)"], ["Muddat", "O‘qituvchi belgilagan muddatda; muddatida yuklanmagan ish baholanmaydi"]])),
         sec("mavzular", 2, "Mustaqil ta’lim mavzulari (fan dasturi, 6-bo‘lim)", f'<input class="search" type="text" placeholder="Mavzu bo‘yicha qidirish…" data-filter=".mt-item" data-count="mt-count" aria-label="Mavzu qidirish"><p class="muted" id="mt-count">{len(other.MT)} ta natija</p><div class="acc">{"".join(items)}</div>'),
         sec("taqdimot", 3, "1-MT: taqdimot va himoya talablari (5 ball)", table(["Daraja", "Tavsif (fan dasturi bo‘yicha)"], [["Yuqori", "Qo‘shimcha ilmiy-metodik adabiyotlardan foydalanib batafsil taqdimot tayyorlagan; fizik jarayonlar, formulalar va chizmalarni mantiqan izchil bayon qiladi, himoyada fikrini mustaqil va erkin ifodalaydi."], ["Yetarli", "Mavzu asosan yoritilgan, taqdimot tushunarli, ammo faqat asosiy darsliklar bilan cheklangan; himoyada tayyor matnga qaram, ayrim atama va formulalarni tushuntirishda kichik noaniqliklar bor."], ["Minimal", "Taqdimot yuzaki, materiallar to‘liq tahlil qilinmagan va ko‘chirmachilikka yo‘l qo‘yilgan; slaydlarda zarur chizma va diagrammalar yo‘q, mavzuni tushuntira olmaydi."], ["Erishilmagan", "Taqdimot tayyorlanmagan, mavzuni bilmaydi yoki belgilangan muddatda HEMIS’ga yuklanmagan."]]) + "<h3>Slaydlar tuzilishi (tavsiya)</h3>" + ul(["Sarlavha, muallif, guruh", "Hodisa va uning dolzarbligi (texnika, kimyo, tabiatdagi misol)", "Asosiy qonun: formula, kattaliklar va SI birliklari", "Chizma yoki grafik (o‘zingiz chizgan yoki modeldan olingan)", "Raqamli misol yoki tajriba natijasi", "Xulosa va 3–5 manba"], True)),
         sec("keys", 4, "2-MT: keys-stadi banki (5 ball)", f'<p>Har bir talaba bitta keysni tanlaydi (yoki o‘qituvchi tayinlaydi). Yechim 3–5 betlik hisobot: muammo tahlili → fizik sabablar → hisob → kamida ikki yechim varianti va ularni taqqoslash → xulosa.</p>{keys}<h3>Baholash mezoni (fan dasturi bo‘yicha)</h3>' + table(["Daraja", "Tavsif"], [["Yuqori", "Muammoli fizik vaziyat chuqur tahlil qilingan, fizik qonuniyatlar asosida to‘liq va ijodiy yechim taklif etilgan; barcha xulosalar mantiqan to‘g‘ri va ilmiy asoslangan."], ["Yetarli", "Keys tahlil qilingan, asosiy fizik qonunlar qisman to‘g‘ri qo‘llangan; yechimni asoslash yoki formulalarni amaliyotga bog‘lashda kamchiliklar bor, mustaqil yondashuv yetishmaydi."], ["Minimal", "Muammo mohiyati to‘liq anglanmagan, aniq yechim taklif qilinmagan; tahlil o‘rniga umumiy so‘zlar yozilgan yoki boshqa mavzuga chalg‘ilgan."], ["Erishilmagan", "Keys bajarilmagan, yechim taqdim etilmagan yoki muddatida topshirilmagan."]])),
         sec("halollik", 5, "Akademik halollik va SI", ul(["Taqdimot va keys yechimi talabaning o‘z ishi bo‘lishi kerak; boshqa manbalardan olingan rasm va matnlar havola bilan beriladi.", "SI vositalaridan foydalanilgan bo‘lsa, ishga qisqa ilova qo‘shiladi: qaysi vosita, qaysi prompt, natija qanday tekshirildi.", "SI yozgan matnni o‘zgartirmasdan topshirish va manbalarni uydirish qoidabuzarlik hisoblanadi."]))]
    html = head("Mustaqil ta’lim", "45 ta mustaqil ta’lim mavzusi, taqdimot talablari va keys-stadi banki") + header("mustaqil.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Mustaqil ta’lim")], "Mustaqil ta’lim · 180 soat", "Mustaqil ta’lim topshiriqlari", "Fan dasturidagi 45 ta mavzu bo‘yicha taqdimot rejalari va fizik qonunlarni amaliy muammolarga qo‘llashga oid keys-stadilar.", [("c", "45 mavzu"), ("a", "1-MT: taqdimot"), ("a", "2-MT: keys-stadi")]) + doc(toc, S) + "</main>" + footer()
    write("mustaqil.html", html)


# ---------------- Baholash ----------------
def baholash_page():
    toc = [("tartib", "Umumiy tartib"), ("matritsa", "TN–nazorat matritsasi"), ("jn", "Joriy nazorat (30)"), ("on", "Oraliq nazorat (20)"), ("yn", "Yakuniy nazorat (50)"), ("baho", "Yakuniy baho"), ("kalk", "Baho kalkulyatori")]
    mat = table(["TN", "Natija", "JN", "ON", "YaN"], [[t, TN_TEXT[t]] + [f'<span class="{"plus" if v == "+" else "minus"}">{v}</span>' for v in TN_MATRIX[t]] for t in TN_TEXT])
    S = [sec("tartib", 1, "Baholashning umumiy tartibi", "<p>Fan bo‘yicha talabaning bilimi 100 ballik tizimda baholanadi va uchta asosiy bosqichni qamrab oladi. Talaba har bir nazorat turidan muvaffaqiyatli o‘tishi uchun ajratilgan maksimal ballning kamida 60 foizini to‘plashi shart.</p>" + table(["Nazorat turi", "Maksimal ball", "Saralash bali", "Baholash vositasi (fan dasturi bo‘yicha)"], [["Joriy nazorat (JN)", "30", "18", "1-MT: mustaqil ta’lim taqdimoti va himoyasi (5); DF: laboratoriya mashg‘ulotlaridagi faollik — fizik qonunlarni tahlil qilish va yechim modelini tuzish (20); 2-MT: keys-stadi tahlili va yechimi (5)"], ["Oraliq nazorat (ON)", "20", "12", "12-haftada HEMIS’da 20 savolli test"], ["Yakuniy nazorat (YaN)", "50", "30", "1-kurslar uchun yozma ish: 3 nazariy savol + 1 amaliy keys"], ["Jami", "100", "—", ""]]) + '<div class="callout warn"><b>Muhim</b>Saralash talabi JN, ON va YaN bo‘yicha alohida qo‘llaniladi. Bir nazorat turidagi yetishmagan ball boshqasidagi yuqori ball hisobiga qoplanmaydi.</div>'),
         sec("matritsa", 2, "Ta’lim natijasi — baholash vositasi muvofiqligi", "<p>Har bir ta’lim natijasi qaysi nazorat turida baholanishi fan dasturida belgilangan. Vositalar: laboratoriya mashg‘uloti, mustaqil ta’lim, test, yozma ish.</p>" + mat),
         sec("jn", 3, "Joriy nazorat rubrikasi — 30 ball", table(["Mezon", "Ball", "Yuqori", "Yetarli", "Minimal", "Erishilmagan"], [
             ["1-MT: mustaqil ta’lim taqdimoti va himoyasi", "5", "Qo‘shimcha adabiyot bilan batafsil taqdimot; jarayon, formula va chizmalarni izchil bayon qiladi, erkin fikr bildiradi", "Tushunarli, lekin darsliklar bilan cheklangan; himoyada matnga qaram", "Yuzaki, ko‘chirmachilik, chizmalar yo‘q", "Tayyorlanmagan yoki muddatida yuklanmagan"],
             ["DF: fizik qonunlarni tahlil qilish va yechim modelini tuzish (laboratoriya mashg‘ulotlari)", "20", "Qonuniyatni aniq tanlaydi, chizma va sxemalarni xatosiz chizadi, algoritmni mustaqil tuzadi", "Asosiy qonunlarni yozadi, murakkab sxemada yordamga tayanadi", "Faqat bitta formulali sodda masalalar; sxema chiza olmaydi", "Shartni tushunmaydi, sxema va chizma chiza olmaydi"],
             ["2-MT: keys-stadi tahlili va yechimi", "5", "Chuqur tahlil, to‘liq va ijodiy, ilmiy asoslangan yechim", "Qisman to‘g‘ri, asoslashda kamchilik", "Mohiyat anglanmagan, umumiy so‘zlar", "Bajarilmagan yoki muddatida topshirilmagan"]]) + '<p class="muted" style="font-size:.85rem">Jami 30 balldan oshmaydi.</p>'),
         sec("on", 4, "Oraliq nazorat rubrikasi — 20 ball", "<p>Oraliq nazorat o‘quv jarayonining 12-haftasida HEMIS axborot tizimi orqali test shaklida o‘tkaziladi. Test sinovlari talabalarning elektrostatika, o‘zgarmas va o‘zgaruvchan tok, magnit maydon qonunlarini qanchalik mustaqil kuzata olishi, olingan bilimlarni amalda qo‘llay olishi va fan mohiyatini tushunishini tahlil qiladi.</p>" + table(["Daraja", "To‘g‘ri javoblar (20 tadan)", "Tavsif"], [["Yuqori", "18–20 (90–100 %)", "Fan mohiyatini to‘liq tushunadi, mustaqil fikrlaydi va olgan bilimini to‘g‘ri ifodalaydi"], ["Yetarli", "14–17 (70–89,9 %)", "Fan mohiyatini tushunadi va biladi, ammo ayrim murakkabroq nazariy savol yoki hisoblarda xato qiladi"], ["Minimal", "12–13 (60–69,9 %)", "Olingan bilimni amaliyotda qo‘llashda qiynaladi, fan haqida umumiy tasavvurga ega, asosan sodda savollarni yechadi"], ["Erishilmagan", "0–11 (0–59,9 %)", "Fan dasturini o‘zlashtirmagan, mavzular mohiyatini tushunmaydi"]]) + f'<p class="muted">Tayyorgarlik uchun har bir ma’ruzadagi nazorat testlaridan foydalaning (jami {sum(len(L["quiz"]) for L in LECT)} savol).</p>'),
         sec("yn", 5, "Yakuniy nazorat rubrikasi — 50 ball", "<p>Yakuniy nazorat attestatsiya haftasida yozma ish shaklida o‘tkaziladi. Har bir variant 4 ta topshiriqdan iborat: 3 ta nazariy savol va 1 ta amaliy keys. Nazariy savollar orqali talabaning asosiy ifoda va qonunlardan to‘g‘ri foydalanishi, hodisalarni mantiqan izchil tushuntira olishi; keys orqali esa nazariy bilimni aniq muammoli vaziyatga qo‘llay olishi tekshiriladi.</p>" + table(["Topshiriq", "Ball", "Yuqori", "Yetarli", "Minimal", "Erishilmagan"], [["Nazariy savollar (1–3), har biri 10 ball: mohiyatni ochib berish (4) + atama va kalit ifodalar (3) + fikrni mantiqiy bayon qilish (3)", "30", "27–30", "21–26", "18–20", "0–17"], ["Keys topshirig‘i (4-savol): fizik qonunlarni muammoli vaziyatga qo‘llash va masalani yechish (natija SI birliklarida)", "20", "18–20", "14–17", "12–13", "0–11"]]) + "<h3>Namunaviy keys (4-savol)</h3><p>Laboratoriyada 1,5 kVt quvvatli elektr choynakda 1,2 kg suv 20 °C dan qaynaguncha 6 daqiqada isitildi. Choynakning foydali ish koeffitsiyentini toping; agar tarmoq kuchlanishi 10 % ga pasaysa, isitish vaqti qanday o‘zgaradi? Natijani Joul–Lens qonuni va issiqlik balansi asosida tahlil qiling. (Yechim yo‘nalishi: <a href=\"lecture10.html\">M10</a>, <a href=\"lecture13.html\">M13</a>.)</p>"),
         sec("baho", 6, "Fan bo‘yicha bahoni aniqlash", table(["Jami ball", "Baho", "Tavsif"], [["90–100", "A’lo", "Ta’lim natijalarini yuqori darajada egallagan; bilimni mustaqil tahlil qiladi va yangi vaziyatlarda qo‘llaydi."], ["70–89,9", "Yaxshi", "Asosiy ta’lim natijalarini barqaror egallagan; bilim va ko‘nikmalarni amaliy vaziyatlarda qo‘llaydi."], ["60–69,9", "Qoniqarli", "Minimal talab etiladigan natijalarga erishgan, biroq tahlil, asoslash yoki mustaqil qo‘llashda cheklovlar mavjud."], ["0–59,9", "Qoniqarsiz", "Minimal ta’lim natijalariga yetarli darajada erishmagan."]])),
         sec("kalk", 7, "Baho kalkulyatori", """<div id="grade-calc" class="two"><div>
<label class="control">1-MT taqdimot (0–5) <output data-for="jn-mt1"></output><input id="jn-mt1" type="range" min="0" max="5" step="0.5" value="4"></label>
<label class="control">DF laboratoriya faolligi (0–20) <output data-for="jn-df"></output><input id="jn-df" type="range" min="0" max="20" step="0.5" value="15"></label>
<label class="control">2-MT keys-stadi (0–5) <output data-for="jn-mt2"></output><input id="jn-mt2" type="range" min="0" max="5" step="0.5" value="4"></label>
<label class="control">Oraliq nazorat (0–20) <output data-for="on"></output><input id="on" type="range" min="0" max="20" step="1" value="15"></label>
<label class="control">Yakuniy nazorat (0–50) <output data-for="yn"></output><input id="yn" type="range" min="0" max="50" step="1" value="38"></label></div>
<div class="card kpi"><div class="l">Jami</div><div class="calc-out" id="calc-total"></div><div class="l" style="margin-top:.6rem">Baho</div><div class="v" id="calc-grade" style="font-size:1.3rem"></div><p class="muted" id="calc-detail" style="font-size:.8rem"></p></div></div><p class="muted" style="font-size:.85rem">Kalkulyator ma’lumot uchun; rasmiy ball HEMIS’da hisoblanadi.</p>""")]
    html = head("Baholash", "JN, ON, YaN rubrikalari, TN–nazorat matritsasi va baho kalkulyatori") + header("baholash.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Baholash")], "Baholash · 100 ball", "Talaba bilimini baholash mezonlari", "Fan dasturidagi baholash tartibi, rubrikalar va ta’lim natijalari bilan muvofiqlik.", [("c", "JN 30 / 18"), ("c", "ON 20 / 12"), ("c", "YaN 50 / 30")]) + doc(toc, S) + "</main>" + footer()
    write("baholash.html", html)


# ---------------- O'qituvchi qo'llanmasi ----------------
def calendar():
    """30 haftalik taqvim: har haftada 2 mashg'ulot (ma'ruza yoki laboratoriya)."""
    byn = {b["n"]: b for b in LABS}
    sess = {}
    for b in LABS:
        for k, s in enumerate(b["sess"]):
            sess[s] = (b, k)
    def lab_cell(s):
        b, k = sess[s]
        return f'<a href="lab{b["n"]}.html">L{s}</a>: {b["title"][:60]}{"…" if len(b["title"]) > 60 else ""}' + (f" ({k+1}-qism)" if len(b["sess"]) > 1 else "")
    def lec_cell(m):
        return f'<a href="lecture{m}.html">M{m}</a>: {strip_tags(LECT[m-1]["short"])}'
    rows = []
    plan = [(1, list(range(1, 14)), list(range(1, 18))), (2, list(range(14, 28)), list(range(18, 34)))]
    notes = {5: "1-MT mavzularini taqsimlash va himoya boshlanadi", 10: "2-MT: keys-stadi topshirig‘i", 12: "Oraliq nazorat (HEMIS, 20 savol)", 15: "Yakuniy nazoratga tayyorgarlik"}
    for sem, lecs, labs in plan:
        lecs, labs = lecs[:], labs[:]
        for w in range(1, 16):
            a = lec_cell(lecs.pop(0)) if lecs else lab_cell(labs.pop(0))
            bcell = lab_cell(labs.pop(0)) if labs else "—"
            rows.append([f"{sem}-sem., {w}", a, bcell, notes.get(w, "—")])
    return rows


def teacher_page():
    toc = [("taqvim", "30 haftalik taqvim"), ("shablon", "Dars rejasi shablonlari"), ("lab", "Laboratoriyani tashkil etish"), ("model", "Modellar va ovozdan foydalanish"), ("si", "SI siyosati"), ("baholash", "Baholashni tashkil etish"), ("moslash", "Darslikni yangilash")]
    S = [sec("taqvim", 1, "O‘quv taqvimi: 2 semestr × 15 hafta (haftada 4 soat)", table(["Hafta", "1-mashg‘ulot (2 soat)", "2-mashg‘ulot (2 soat)", "Nazorat / izoh"], calendar()) + '<p class="muted" style="font-size:.85rem">Taqvim fan dasturidagi M1–M27 va L1–L33 tartibiga mos tavsiya. 1-semestr: M1–M13 va L1–L17; 2-semestr: M14–M27 va L18–L33. Nazorat muddatlari fakultetning o‘quv jarayoni jadvali va HEMIS bo‘yicha aniqlashtiriladi.</p>'),
         sec("shablon", 2, "Ma’ruza va laboratoriya darsi rejasi shabloni", "<h3>Ma’ruza (80 daqiqa)</h3>" + table(["Vaqt", "Bosqich", "O‘qituvchi", "Talaba"], [["0–10", "Kirish", "Blits-so‘rov, muammoli savol", "Javob beradi, bashorat qiladi"], ["10–45", "Nazariya", "Qonunlarni keltirib chiqaradi", "Konspekt, savollar"], ["45–60", "Model", "Simulyatorni namoyish qiladi", "Bashorat → kuzatish → izoh"], ["60–72", "Misol", "Masalani beradi, yo‘naltiradi", "Juftlikda yechadi"], ["72–80", "Yakun", "Test, xato tushunchalar", "O‘z-o‘zini tekshiradi"]]) + "<h3>Laboratoriya mashg‘uloti (80 daqiqa)</h3>" + table(["Vaqt", "Bosqich"], [["0–10", "Kirish nazorati: ish maqsadi, hisoblash formulasi, xavfsizlik (2–3 savol)"], ["10–55", "O‘lchashlar: juftlikda ishlash, jadvalni to‘ldirish; o‘qituvchi DF bahosi uchun kuzatadi"], ["55–70", "Hisoblash va xatolikni baholash (kalkulyator yoki Python)"], ["70–80", "Natijani himoya qilish: jadval qiymati bilan solishtirish, nazorat savollari"]])),
         sec("lab", 3, "Laboratoriya ishlarini tashkil etish", ul(["<b>Guruhlash:</b> 2–3 talabadan iborat brigadalar; har bir brigada semestr davomida ishlarni aylanma (frontal emas) tartibda bajaradi.", "<b>Kirish nazorati:</b> talaba ish nazariyasi va tartibini bilmasa, o‘lchashga qo‘yilmaydi — tayyorgarlik uchun darslik sahifasi va virtual model tavsiya etiladi.", "<b>Ikki mashg‘ulotli ishlar</b> (L6–L7, L13–L14, L15–L16, L31–L32): 1-mashg‘ulotda asosiy o‘lchash, 2-mashg‘ulotda boshqa namuna yoki rejim, natijalarni umumlashtirish va himoya.", "<b>Xatolik hisobi:</b> barcha hisobotlarda natija \\(x=\\bar x\\pm\\Delta x\\) ko‘rinishida, ishonchlilik ehtimoli \\(P=0{,}95\\) ko‘rsatiladi (laboratoriyaga kirish sahifasi).", "<b>L33 kompyuter tajribasi:</b> darslikdagi Bor va Frank–Gers modellari yoki PhET “Models of the Hydrogen Atom” simulyatoridan foydalaniladi.", "<b>Xavfsizlik:</b> har bir ish sahifasida xavfsizlik texnikasi bo‘limi bor; birinchi mashg‘ulotda yo‘riqnoma o‘tkazilib, jurnalga imzo olinadi."])),
         sec("model", 4, "Interaktiv modellar va ovozdan foydalanish", ul(["<b>Bashorat → kuzatish → tushuntirish (POE):</b> parametrni o‘zgartirishdan oldin talabalardan natijani bashorat qilishni so‘rang.", "<b>Ishlangan misol bilan tekshirish:</b> misoldagi qiymatlarni modelga kiriting — natija mos kelishi kerak.", "<b>Cheklovlarni muhokama qiling:</b> modellar soddalashtirilgan (havo qarshiligi, issiqlik yo‘qotishi, ideal asboblar); qaysi effektlar hisobga olinmaganini so‘rang.", "<b>Proyektor uchun:</b> brauzerni to‘liq ekranga o‘tkazing (F11); modellar internetsiz ham ishlaydi.", "<b>Ovozli namoyish:</b> model ostidagi tugma parametrlarni o‘zi bosqichma-bosqich o‘zgartirib, natijani ovoz va yozuv bilan tushuntiradi; tugagach boshqaruv talabalarga o‘tadi.", "<b>Tinglash:</b> sarlavha yonidagi tugma nazariya va misollarni o‘qiydi, formulalarni so‘z bilan aytadi. O‘zbekcha matnlar oldindan tayyorlangan neyron ovozli MP3 fayllardan ijro etiladi — barcha qurilmalarda bir xil tabiiy ovoz eshitiladi. Pastdagi panel: pauza / davom, oldingi va keyingi xatboshi, to‘xtatish (Esc); istalgan xatboshini bosib, o‘sha joydan o‘qish mumkin.", "<b>Til:</b> UZ / RU / EN tugmalari butun saytni (testlar bilan birga) Google Translate orqali tarjima qiladi; rus va ingliz tillarida brauzer ovozi ishlatiladi."])),
         sec("si", 5, "Sun’iy intellekt bo‘yicha kurs siyosati (tavsiya)", ul(["SI tushuntirish, masala yechimini tekshirish va Python kod qoralamasi uchun ruxsat etiladi.", "Baholanadigan ishda SI ishlatilgan bo‘lsa, prompt va tekshiruv natijasi ilova qilinadi.", "SI bergan son va formulalar darslik yoki mustaqil hisob bilan tasdiqlanishi shart.", "Yozma nazoratlarda (ON, YaN) SI dan foydalanish taqiqlanadi.", "Laboratoriya o‘lchov natijalarini SI yordamida “to‘g‘rilash” yoki uydirish akademik halollik buzilishi hisoblanadi."])),
         sec("baholash", 6, "Baholashni tashkil etish bo‘yicha tavsiyalar", ul(["<b>DF (20 ball):</b> har laboratoriya mashg‘ulotida kirish nazorati, o‘lchash madaniyati va hisobot himoyasini kuzating; 4 darajali rubrikadan foydalaning (laboratoriya sahifalarining oxirgi bo‘limi).", "<b>1-MT:</b> 45 mavzuni 1-haftada taqsimlang; himoya 5–7 daqiqa + 3 daqiqa savol.", "<b>2-MT:</b> keys-stadi bankidan tanlov; hisobot 3–5 bet.", f"<b>ON:</b> ma’ruzalardagi {sum(len(L['quiz']) for L in LECT)} ta test savoli HEMIS savol banki uchun namuna bo‘la oladi (yangi variantlar tuzish tavsiya etiladi).", "<b>YaN:</b> namunaviy keys baholash sahifasida."])),
         sec("moslash", 7, "Darslikni moslashtirish va yangilash", "<p>Sayt statik HTML/CSS/JS fayllaridan iborat va GitHub Pages’da ishlaydi. Mazmun <code>gen/</code> papkasidagi Python fayllarida saqlanadi: <code>lec_mex.py</code>, <code>lec_mol.py</code>, <code>lec_el.py</code>, <code>lec_opt.py</code>, <code>lec_atom.py</code> (ma’ruzalar), <code>labs_a.py</code>, <code>labs_b.py</code>, <code>lab_intro.py</code> (laboratoriya), <code>other.py</code> (mustaqil ta’lim, keyslar, lug‘at, vositalar), <code>tours.py</code> (ovozli namoyishlar). Matnni o‘zgartirgach, <code>python gen/build.py .</code> buyrug‘i barcha sahifalarni qayta yaratadi; o‘zgargan xatboshilar uchun ovoz GitHub Actions orqali avtomatik yangilanadi. Simulyatorlar <code>js/sims.js</code> faylida.</p>")]
    html = head("O‘qituvchi uchun", "30 haftalik taqvim, dars rejasi shablonlari, laboratoriyani tashkil etish va SI siyosati") + header("oqituvchi.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "O‘qituvchi uchun")], "Metodik qo‘llanma", "O‘qituvchi uchun qo‘llanma", "Fan dasturi asosidagi haftalik taqvim, dars shablonlari, laboratoriyani tashkil etish, baholash va darslikni yangilash bo‘yicha ko‘rsatmalar.", [("a", "2 × 15 hafta"), ("", "Haftada 4 soat")]) + doc(toc, S) + "</main>" + footer()
    write("oqituvchi.html", html)


# ---------------- Lug'at ----------------
def gloss_page():
    def mlink(m):
        return f'<a href="lecture{m}.html">M{m}</a>' if isinstance(m, int) else f'<a href="lab{m[1:]}.html">{m}</a>'
    rows = "".join(f'<tr class="g-row"><td><b>{u}</b></td><td><span lang="ru">{r}</span></td><td><i lang="en">{e}</i></td><td>{d}</td><td>{mlink(m)}</td></tr>' for u, r, e, d, m in sorted(other.GLOSS, key=lambda x: x[0].lower()))
    body = f'<input class="search" type="text" placeholder="Atama qidirish (o‘zbekcha, ruscha yoki inglizcha)…" data-filter=".g-row" data-count="g-count" aria-label="Atama qidirish"><p class="muted" id="g-count">{len(other.GLOSS)} ta natija</p><div class="tw"><table class="t"><thead><tr><th>Atama</th><th>Русский</th><th>English</th><th>Ta’rif</th><th>Mavzu</th></tr></thead><tbody>{rows}</tbody></table></div>'
    html = head("Atamalar lug‘ati", "Umumiy fizika atamalari: o‘zbekcha–ruscha–inglizcha lug‘at") + header("glossariy.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Lug‘at")], "1-ilova", "Atamalar lug‘ati", "O‘zbekcha atama, ruscha va inglizcha muqobili, qisqa ta’rif va u o‘rganiladigan mavzu.", [("c", f"{len(other.GLOSS)} atama")]) + f'<div class="container" style="padding:2rem 0 3rem"><section class="doc-sec">{body}</section></div></main>' + footer()
    write("glossariy.html", html)


def tools_page():
    secs, toc = [], []
    for i, (cat, items) in enumerate(other.TOOLS, 1):
        rows = [[(f'<a href="{u}" rel="noopener" target="_blank">{n}</a>' if u.startswith("http") else f'<a href="{u}">{n}</a>') if u else f"<b>{n}</b>", d, a] for n, u, d, a in items]
        secs.append(sec(f"t{i}", i, cat, table(["Vosita", "Darslikda qo‘llanilishi", "Kirish"], rows)))
        toc.append((f"t{i}", cat))
    secs.append('<div class="callout info"><b>Eslatma</b>Tariflar va litsenziya shartlari o‘zgarib turadi — foydalanishdan oldin rasmiy saytni tekshiring. Darslikdagi barcha topshiriqlarni bepul vositalar (PhET, Python/Colab, Tracker, GeoGebra) bilan bajarish mumkin.</div>')
    html = head("Dasturiy vositalar", "PhET, Python, Tracker, GeoGebra va boshqa bepul vositalar") + header("vositalar.html") + '<main id="main">' + hero([("index.html", "Bosh sahifa"), ("", "Vositalar")], "2-ilova", "Dasturiy vositalar va virtual laboratoriyalar", "Ma’ruza, laboratoriya va mustaqil ta’lim topshiriqlari uchun tavsiya etilgan bepul vositalar.", []) + doc(toc, secs) + "</main>" + footer()
    write("vositalar.html", html)


def notfound():
    html = head("Sahifa topilmadi", "404") + header() + '<main id="main">' + hero([("index.html", "Bosh sahifa")], "404", "Sahifa topilmadi", "So‘ralgan sahifa mavjud emas yoki ko‘chirilgan. Bosh sahifaga qayting.", []) + "</main>" + footer()
    write("404.html", html)


def legacy_redirects():
    """Avvalgi versiya manzillari (lectures/, labs/, yoriqnomalar/) yangi sahifalarga yo'naltiriladi."""
    for i in range(1, 25):
        redirect(f"lectures/lecture{i}.html", "index.html#maruzalar", "Ma’ruzalar")
    for i in range(1, 4):
        redirect(f"labs/lab{i}.html", "index.html#laboratoriya", "Laboratoriya ishlari")
    for i in range(1, 4):
        redirect(f"yoriqnomalar/MT-{i:02d}.html", "mustaqil.html", "Mustaqil ta’lim")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    assert [L["n"] for L in LECT] == list(range(1, 28)), "ma'ruzalar 1..27 bo'lishi kerak"
    allsess = sorted(s for b in LABS for s in b["sess"])
    assert allsess == list(range(1, 34)), f"laboratoriya mashg'ulotlari 1..33: {allsess}"
    for L in LECT:
        for s in sims_of(L): assert s in SIMNAME, s
        lecture_page(L)
    for b in LABS:
        for s in sims_of(b): assert s in SIMNAME, s
        lab_page(b)
    lab_intro_page(); index_page(); sims_page(); annot_page(); mustaqil_page(); baholash_page(); teacher_page(); gloss_page(); tools_page(); notfound(); legacy_redirects()
    print("OK:", len(LECT), "ma'ruza,", len(LABS), "laboratoriya ishi ->", os.path.abspath(OUT))
