"""Laboratoriya ishlariga kirish: o'lchash xatoliklari (GUM), natijalarni qayta ishlash, xavfsizlik, hisobot."""
from common import code, table, ul

PY = """import numpy as np

T95 = {2: 12.71, 3: 4.30, 4: 3.18, 5: 2.78, 6: 2.57, 7: 2.45, 8: 2.36, 9: 2.31, 10: 2.26}  # Styudent, P = 0,95

def bevosita(x, asbob_xatoligi):
    \"\"\"Bevosita o'lchash: o'rtacha, tasodifiy (A) va to'liq xatolik.\"\"\"
    x = np.asarray(x, float); n = len(x)
    s = x.std(ddof=1) / np.sqrt(n)            # o'rtachaning standart chetlanishi
    d_t = T95[n] * s                          # tasodifiy xatolik (P = 0,95)
    d = np.hypot(d_t, asbob_xatoligi)         # to'liq xatolik
    return x.mean(), d

# 1) Bevosita o'lchash: silindr diametri (mm), shtangensirkul aniqligi 0,1 mm
d, dd = bevosita([20.1, 20.2, 20.1, 20.2, 20.1], 0.1)
print(f"d = ({d:.2f} ± {dd:.2f}) mm, eps = {100*dd/d:.1f} %")

# 2) Bilvosita o'lchash: rho = 4m/(pi d^2 h)  ->  eps^2 = eps_m^2 + (2 eps_d)^2 + eps_h^2
m, dm, h, dh = 39.05, 0.02, 45.26, 0.12          # g, mm
rho = 4*m/(np.pi*(d/10)**2*(h/10))                # g/sm³
eps = np.sqrt((dm/m)**2 + (2*dd/d)**2 + (dh/h)**2)
print(f"rho = ({rho:.2f} ± {rho*eps:.2f}) g/sm³")

# 3) Eng kichik kvadratlar usuli: y = kx + b, koeffitsiyentlar xatoligi bilan
x = np.array([1.47, 2.45, 3.43, 4.41]); y = np.array([0.45, 0.74, 1.04, 1.32])
(k, b), cov = np.polyfit(x, y, 1, cov=True)
t = T95[len(x) - 1]                                # erkinlik darajasi n − 2
print(f"k = {k:.3f} ± {t*np.sqrt(cov[0,0]):.3f},  b = {b:.3f} ± {t*np.sqrt(cov[1,1]):.3f}")
"""

INTRO = {
 "sections": [
  ("umumiy", "Laboratoriya ishlarining tartibi va xavfsizlik", r"""<p>Fan dasturiga ko‘ra laboratoriya mashg‘ulotlari 66 soatni (33 mashg‘ulot) tashkil etadi va joriy nazoratning asosiy qismi (DF — 20 ball) shu mashg‘ulotlardagi faollik bo‘yicha baholanadi. Har bir ish uch bosqichdan iborat: <b>tayyorgarlik</b> (nazariya, formula, jadval), <b>o‘lchash</b> (laboratoriyada, brigadada) va <b>hisobot himoyasi</b> (natija, xatolik, xulosa).</p>
""" + ul(["<b>Kirish nazorati:</b> talaba ish maqsadi, hisoblash formulasi va bajarish tartibini bilsagina o‘lchashga qo‘yiladi.", "<b>Elektr xavfsizligi:</b> zanjir faqat manba o‘chirilgan holda yig‘iladi va o‘qituvchi tekshirgandan keyin ulanadi; izolyatsiyasi shikastlangan simlardan foydalanilmaydi.", "<b>Issiqlik xavfsizligi:</b> qaynoq suv, bug‘ va qizdirilgan jismlar faqat qisqich yoki qo‘lqop bilan ushlanadi.", "<b>Optik xavfsizlik:</b> lazer nuri ko‘zga va boshqalarga yo‘naltirilmaydi; simob lampasi ultrabinafsha nuriga to‘g‘ridan-to‘g‘ri qaralmaydi.", "<b>Shisha va simob:</b> singan shisha qo‘l bilan yig‘ilmaydi; simob to‘kilganda darhol o‘qituvchiga xabar beriladi.", "<b>Tartib:</b> ish joyi toza saqlanadi, asboblar ish tugagach dastlabki holatiga qaytariladi; laboratoriyada ovqatlanish taqiqlanadi."]) + "<p>Birinchi mashg‘ulotda xavfsizlik bo‘yicha yo‘riqnoma o‘tkaziladi va jurnalga imzo olinadi.</p>"),
  ("xatolik", "O‘lchash xatoliklari va noaniqlik", r"""<p>Hech qanday o‘lchash mutlaq aniq emas: natija har doim <b>noaniqlik</b> (xatolik) bilan birga beriladi. Xalqaro me’yor — JCGM 100:2008 (GUM) — noaniqlikni baholashning yagona qoidalarini belgilaydi.</p>
<h3>Xatoliklar turlari</h3>""" + ul(["<b>Sistematik</b> — har bir o‘lchashda bir xil ishora va kattalikda takrorlanadi (asbob noli siljigan, usul kamchiligi). Takroriy o‘lchash ularni kamaytirmaydi; tuzatma kiritish yoki usulni o‘zgartirish kerak.", "<b>Tasodifiy</b> — o‘lchashdan o‘lchashga tartibsiz o‘zgaradi (reaksiya vaqti, tebranishlar). Ko‘p marta o‘lchab, statistik usulda baholanadi.", "<b>Qo‘pol xato (promax)</b> — noto‘g‘ri yozuv yoki o‘lchash; bunday natija tahlildan chiqariladi."]) + r"""<h3>Bevosita o‘lchash xatoligi</h3>
<p>Kattalik \(n\) marta o‘lchangan bo‘lsin: \(x_1,\dots,x_n\). O‘rtacha qiymat va o‘rtachaning standart chetlanishi (GUM bo‘yicha A turdagi noaniqlik):</p>
$$\bar x=\frac1n\sum_{i=1}^nx_i,\qquad S_{\bar x}=\sqrt{\frac{\sum(x_i-\bar x)^2}{n(n-1)}}$$
<p>Ishonchlilik ehtimoli \(P=0{,}95\) uchun tasodifiy xatolik \(\Delta x_\text{t}=t_{P,n}S_{\bar x}\), bu yerda \(t_{P,n}\) — Styudent koeffitsiyenti. Asbob xatoligi \(\Delta_\text{a}\) (B turdagi noaniqlik) asbob shkalasining bo‘lim qiymati yoki aniqlik klassi bo‘yicha olinadi (masalan, nonius uchun 0,1 mm; 1,0 klassli voltmetr uchun shkala chegarasining 1 %). To‘liq xatolik:</p>
$$\Delta x=\sqrt{\Delta x_\text{t}^2+\Delta_\text{a}^2},\qquad \varepsilon=\frac{\Delta x}{\bar x}\cdot100\,\%$$
""" + table(["O‘lchashlar soni n", "3", "4", "5", "6", "7", "8", "10", "∞"], [["\\(t_{0,95;\\,n}\\)", "4,30", "3,18", "2,78", "2,57", "2,45", "2,36", "2,26", "1,96"]]) + r"""<p class="muted" style="font-size:.85rem">GUM terminologiyasida \(u_A=S_{\bar x}\), \(u_B=\Delta_\text{a}/\sqrt3\) (tekis taqsimot), yig‘ma standart noaniqlik \(u_c=\sqrt{u_A^2+u_B^2}\), kengaytirilgan noaniqlik \(U=ku_c\) (\(k=2\), \(P\approx0{,}95\)). Darslikdagi soddalashtirilgan usul shunga yaqin natija beradi.</p>"""),
  ("bilvosita", "Bilvosita o‘lchash xatoligi", r"""<p>Natija \(y=f(x_1,x_2,\dots)\) formula orqali hisoblansa, xatoliklar qo‘shilishi (noaniqlik tarqalishi) qoidasi:</p>
$$\Delta y=\sqrt{\sum_i\left(\frac{\partial f}{\partial x_i}\Delta x_i\right)^2}$$
<p>Darajali ko‘paytma \(y=Cx_1^{a}x_2^{b}x_3^{c}\) uchun nisbiy xatoliklar bilan ishlash qulay:</p>
$$\varepsilon_y=\sqrt{(a\,\varepsilon_1)^2+(b\,\varepsilon_2)^2+(c\,\varepsilon_3)^2}$$
<p><b>Misol.</b> Silindr zichligi \(\rho=\dfrac{4m}{\pi d^2h}\): \(\varepsilon_\rho=\sqrt{\varepsilon_m^2+(2\varepsilon_d)^2+\varepsilon_h^2}\). Diametr kvadratda qatnashgani uchun uning xatoligi ikki baravar hissa qo‘shadi — demak eng aniq asbob aynan diametr uchun tanlanishi kerak. <b>Qoida:</b> natija xatoligiga eng katta hissa qo‘shayotgan kattalikni aniqlang va o‘lchash aniqligini birinchi navbatda o‘sha kattalik uchun oshiring.</p>"""),
  ("yozish", "Natijani yozish va yaxlitlash qoidalari", ul(["Absolyut xatolik 1–2 ta qiymatli raqamgacha yaxlitlanadi (birinchi raqam 1 yoki 2 bo‘lsa — ikkita, aks holda bitta): 0,0347 → 0,03; 0,0147 → 0,015.", "O‘rtacha qiymat xatolik bilan bir xil xonagacha yaxlitlanadi: 9,8093 ± 0,029 → (9,81 ± 0,03) m/s².", "Natija birlik va ishonchlilik ehtimoli bilan yoziladi: \\(g=(9{,}81\\pm0{,}03)\\) m/s², \\(P=0{,}95\\), \\(\\varepsilon=0{,}3\\,\\%\\).", "Katta va kichik sonlar o‘nning darajasi bilan: \\((1{,}10\\pm0{,}03)\\cdot10^{-6}\\) Ω·m.", "Oraliq hisoblarda bitta ortiqcha raqam saqlanadi; yaxlitlash faqat oxirida bajariladi.", "Natija jadval qiymati bilan solishtiriladi: farq \\(\\Delta x\\) dan kichik bo‘lsa — natijalar mos; katta bo‘lsa — sistematik xatolik manbaini izlash kerak."])),
  ("grafik", "Grafik qurish va eng kichik kvadratlar usuli", ul(["O‘qlarda kattalik nomi va birligi yoziladi; masshtab nuqtalar grafikning asosiy qismini egallaydigan qilib tanlanadi.", "Tajriba nuqtalari aniq belgilanadi (xatolik chegaralari bilan); egri chiziq nuqtalar orqali emas, ular orasidan silliq o‘tkaziladi.", "Imkon bo‘lsa, bog‘lanish <b>chiziqlilashtiriladi</b>: \\(T^2(l)\\), \\(\\ln u(t)\\), \\(\\lg I(\\lg U)\\), \\(1/\\lambda(1/n^2)\\)."]) + r"""<p>Tajriba nuqtalariga \(y=kx+b\) to‘g‘ri chizig‘ini o‘tkazishning eng yaxshi usuli — <b>eng kichik kvadratlar usuli</b> (chetlanishlar kvadratlari yig‘indisi minimal):</p>
$$k=\frac{n\sum x_iy_i-\sum x_i\sum y_i}{n\sum x_i^2-\left(\sum x_i\right)^2},\qquad b=\frac{\sum y_i-k\sum x_i}{n}$$
<p>Qiyalik xatoligi \(S_k=\sqrt{\dfrac{\sum(y_i-kx_i-b)^2}{(n-2)\sum(x_i-\bar x)^2}}\), \(\Delta k=t_{P,n-1}S_k\). Qiyalik va ozod hadning fizik ma’nosi har bir ishda ko‘rsatilgan (masalan, \(T^2=\frac{4\pi^2}{g}l\) da qiyalik \(4\pi^2/g\)).</p>"""),
  ("python", "Natijalarni Python bilan qayta ishlash", r"""<p>Quyidagi kodni Google Colab yoki Jupyter’da ishga tushiring. U barcha laboratoriya ishlarida qo‘llaniladigan uchta amalni bajaradi: bevosita o‘lchash xatoligi, bilvosita o‘lchash xatoligi va eng kichik kvadratlar usuli.</p>""" + code("code-intro", PY)),
  ("hisobot", "Hisobot tuzilishi va himoya", ul(["Titul: ish raqami va nomi, talaba F.I.Sh., guruh, sana.", "Ish maqsadi va asbob-jihozlar ro‘yxati (asboblar aniqligi bilan).", "Qurilma (zanjir) sxemasi va hisoblash formulasi (kattaliklar izohi bilan).", "O‘lchash natijalari jadvali (birliklari bilan) — xomaki yozuvlar ham ilova qilinadi.", "Hisoblash: o‘rtacha qiymat, xatoliklar, grafik(lar).", "Natija \\(x=(\\bar x\\pm\\Delta x)\\) birlik, \\(P=0{,}95\\), \\(\\varepsilon\\) — va jadval qiymati bilan solishtirish.", "Xulosa: maqsadga erishildimi, asosiy xatolik manbalari, aniqlikni oshirish yo‘llari.", "Himoyada: nazorat savollariga javob va natijani mustaqil tushuntirish."], True)),
 ],
 "quiz": [
  ("Bitta kattalik 5 marta o‘lchanganda tasodifiy xatolikni hisoblash uchun qaysi koeffitsiyent ishlatiladi (P = 0,95)?", ["Styudent koeffitsiyenti t ≈ 2,78", "1,00", "1,96", "4,30"], 0, "n = 5 uchun t₀,₉₅ = 2,78."),
  ("Takroriy o‘lchashlar qaysi xatolikni kamaytirmaydi?", ["sistematik xatolikni", "tasodifiy xatolikni", "o‘rtachaning standart chetlanishini", "qo‘pol xatoni aniqlashni"], 0, "Sistematik xatolik har safar bir xil."),
  ("y = x² bo‘lsa, ε_y =", ["2ε_x", "ε_x", "ε_x/2", "ε_x²"], 0, "Daraja ko‘rsatkichi ko‘paytiriladi."),
  ("Tasodifiy xatolik 0,068 mm, asbob xatoligi 0,1 mm. To‘liq xatolik:", ["≈ 0,12 mm", "0,168 mm", "0,1 mm", "0,032 mm"], 0, "√(0,068² + 0,1²)."),
  ("Qaysi yozuv to‘g‘ri?", ["g = (9,81 ± 0,03) m/s²", "g = (9,8093 ± 0,029) m/s²", "g = 9,81 ± 0,0291", "g = (9,8 ± 0,029) m/s²"], 0, "Xatolik 1–2 qiymatli raqamgacha, qiymat shu xonagacha."),
  ("T²(l) grafigi qiyaligi 4,02 s²/m. g =", ["≈ 9,82 m/s²", "4,02 m/s²", "≈ 2,0 m/s²", "≈ 39,5 m/s²"], 0, "g = 4π²/k."),
  ("Eng kichik kvadratlar usuli nimani minimallashtiradi?", ["chetlanishlar kvadratlari yig‘indisini", "chetlanishlar yig‘indisini", "nuqtalar sonini", "qiyalikni"], 0, "Gauss usuli."),
  ("Zichlik ρ = 4m/(πd²h). Qaysi kattalik xatoligi ikki baravar hissa qo‘shadi?", ["d", "m", "h", "π"], 0, "d kvadratda.")],
}
