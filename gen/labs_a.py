"""Laboratoriya ishlari: L1–L17 (mexanika, molekulyar fizika va termodinamika)."""

B = []

B.append(dict(
 n=1, sess=[1], lec=1, area="mex", sim="vernier", tn=["TN2", "TN6"],
 title="Shtangensirkul yordamida jismlarning chiziqli o‘lchamlarini aniqlash",
 goal="Shtangensirkul (nonius) yordamida jismlarning chiziqli o‘lchamlarini 0,1 mm (0,05 mm) aniqlikda o‘lchashni, ko‘p marta o‘lchash natijalarini qayta ishlashni hamda tasodifiy va asbob xatoliklarini baholashni o‘rganish; silindr hajmini xatoligi bilan aniqlash.",
 equip=["Shtangensirkul (nonius aniqligi 0,1 yoki 0,05 mm)", "Mikrometr (0,01 mm) — taqqoslash uchun", "O‘lchanadigan jismlar: silindr, ichi bo‘sh silindr (vtulka), parallelepiped", "Chizg‘ich (1 mm)"],
 theory=r"""<p>Shtangensirkul asosiy shkala (mm bo‘limli) va unga nisbatan suriladigan <b>nonius</b> (vernyer)dan iborat. Nonius \(n\) ta bo‘limga ega bo‘lib, ularning umumiy uzunligi asosiy shkalaning \((n-1)\) mm iga teng; bitta nonius bo‘limi \(1-1/n\) mm. Asbob aniqligi (nonius qiymati): \(\Delta=1/n\) mm (\(n=10\) da 0,1 mm, \(n=20\) da 0,05 mm).</p>
<p><b>O‘qish qoidasi:</b> nonius nolidan chapdagi asosiy shkalaning butun millimetrlari \(N\) olinadi, so‘ng asosiy shkala chizig‘i bilan aniq ustma-ust tushgan nonius chizig‘ining tartib raqami \(k\) topiladi:</p>
$$L=N+k\Delta$$
<p>Tashqi o‘lcham katta jag‘lar bilan, ichki o‘lcham (teshik diametri) kichik (ustki) jag‘lar bilan, chuqurlik esa chuqurlik o‘lchagich bilan o‘lchanadi. Silindr hajmi \(V=\pi d^2h/4\); uning nisbiy xatoligi \(\varepsilon_V=\sqrt{(2\varepsilon_d)^2+\varepsilon_h^2}\).</p>""",
 steps=["Jag‘larni jipslashtirib, nol holatni tekshiring: nonius noli asosiy shkala noli bilan ustma-ust tushishi kerak (aks holda nol tuzatmani yozib oling).", "Nonius qiymatini aniqlang: Δ = 1/n mm (n — nonius bo‘limlari soni).", "Silindr diametrini turli joylarda va turli yo‘nalishlarda 5 marta o‘lchang; jag‘larni ortiqcha qismang.", "Silindr balandligini 5 marta o‘lchang.", "Vtulkaning ichki diametrini kichik jag‘lar bilan, teshik chuqurligini chuqurlik o‘lchagich bilan o‘lchang.", "Har bir kattalik uchun o‘rtacha qiymat va tasodifiy xatolikni (Styudent koeffitsiyenti bilan) hisoblang.", "Asbob xatoligini hisobga olib to‘liq xatolikni toping va silindr hajmini xatoligi bilan hisoblang.", "Diametrni mikrometr bilan o‘lchab, natijalarni taqqoslang."],
 table=(["№", "d, mm", "h, mm", "dᵢ − d̄, mm", "hᵢ − h̄, mm"], [["1", "20,1", "45,3", "−0,04", "+0,04"], ["2", "20,2", "45,2", "+0,06", "−0,06"], ["3", "20,1", "45,3", "−0,04", "+0,04"], ["4", "20,2", "45,2", "+0,06", "−0,06"], ["5", "20,1", "45,3", "−0,04", "+0,04"], ["O‘rtacha", "20,14", "45,26", "", ""]]),
 calc=r"""<p><b>1. O‘rtacha qiymatlar:</b> \(\bar d=20{,}14\) mm, \(\bar h=45{,}26\) mm.</p>
<p><b>2. Tasodifiy xatolik</b> (\(n=5\), \(P=0{,}95\), \(t=2{,}78\)): \(S_{\bar d}=\sqrt{\frac{\sum(d_i-\bar d)^2}{n(n-1)}}=\sqrt{\frac{0{,}0120}{20}}=0{,}024\) mm, \(\Delta d_\text{t}=tS_{\bar d}=0{,}068\) mm.</p>
<p><b>3. To‘liq xatolik</b> (asbob xatoligi \(\Delta_\text{a}=0{,}1\) mm): \(\Delta d=\sqrt{\Delta d_\text{t}^2+\Delta_\text{a}^2}=0{,}12\) mm. Xuddi shunday \(\Delta h=0{,}12\) mm.</p>
<p><b>4. Natija:</b> \(d=(20{,}14\pm0{,}12)\) mm, \(\varepsilon_d=0{,}6\,\%\); \(h=(45{,}26\pm0{,}12)\) mm, \(\varepsilon_h=0{,}3\,\%\).</p>
<p><b>5. Hajm:</b> \(V=\frac{\pi\bar d^2\bar h}{4}=14{,}42\) sm³; \(\varepsilon_V=\sqrt{(2\varepsilon_d)^2+\varepsilon_h^2}=1{,}2\,\%\); \(V=(14{,}42\pm0{,}18)\) sm³, \(P=0{,}95\).</p>
<div class="callout info"><b>Xulosa</b>Xatolikka asosan asbob xatoligi hissa qo‘shadi; aniqroq natija uchun diametrni mikrometr bilan o‘lchash kerak.</div>""",
 code="""import numpy as np
# Silindr o'lchovlari (mm) — o'z natijalaringizni kiriting
d = np.array([20.1, 20.2, 20.1, 20.2, 20.1])
h = np.array([45.3, 45.2, 45.3, 45.2, 45.3])
T95 = {3: 4.30, 4: 3.18, 5: 2.78, 6: 2.57, 7: 2.45, 8: 2.36, 10: 2.26}  # Styudent koeffitsiyenti, P = 0,95
D_ASB = 0.1  # asbob (nonius) xatoligi, mm

def natija(x, nom):
    n = len(x); m = x.mean()
    s = x.std(ddof=1)/np.sqrt(n)        # o'rtachaning standart chetlanishi
    D = np.hypot(T95[n]*s, D_ASB)       # to'liq xatolik
    print(f"{nom} = ({m:.2f} ± {D:.2f}) mm,  eps = {100*D/m:.1f} %")
    return m, D

dm, dD = natija(d, "d"); hm, hD = natija(h, "h")
V = np.pi*dm**2*hm/4
eps_V = np.hypot(2*dD/dm, hD/hm)
print(f"V = ({V/1000:.2f} ± {eps_V*V/1000:.2f}) sm³,  eps = {100*eps_V:.1f} %")""",
 questions=["Nonius qiymati qanday aniqlanadi va 20 bo‘limli noniusda u nimaga teng?", "Nima uchun bir kattalik bir necha marta o‘lchanadi?", "Asbob xatoligi va tasodifiy xatolik qanday qo‘shiladi?", "Silindr hajmi xatoligiga qaysi o‘lcham ko‘proq hissa qo‘shadi va nima uchun?", "Shtangensirkul va mikrometr aniqligini taqqoslang; qaysi holda qaysi biri ishlatiladi?"]
))

B.append(dict(
 n=2, sess=[2], lec=11, area="mex", sim="vernier", tn=["TN2", "TN6"],
 title="To‘g‘ri geometrik shakldagi jismlarning zichligini aniqlash",
 goal="To‘g‘ri geometrik shakldagi (silindr, parallelepiped) jismlarning massasini tarozida, o‘lchamlarini shtangensirkulda o‘lchab, ularning zichligini aniqlash va bilvosita o‘lchash xatoligini hisoblash; natija asosida jism materialini aniqlash.",
 equip=["Texnik yoki elektron tarozi (aniqlik 0,01 g)", "Shtangensirkul", "Turli materiallardan (alyuminiy, latun, po‘lat) yasalgan silindr va parallelepipedlar", "Moddalar zichligi jadvali"],
 theory=r"""<p>Bir jinsli jism <b>zichligi</b> — uning massasining hajmiga nisbati: \(\rho=m/V\) (kg/m³; amalda g/sm³ ham ishlatiladi, 1 g/sm³ = 1000 kg/m³). To‘g‘ri geometrik shakldagi jism hajmi o‘lchamlaridan hisoblanadi: silindr \(V=\pi d^2h/4\), parallelepiped \(V=abc\). Silindr uchun:</p>
$$\rho=\frac{4m}{\pi d^2h},\qquad \varepsilon_\rho=\sqrt{\varepsilon_m^2+(2\varepsilon_d)^2+\varepsilon_h^2}$$
<p>Bu — <b>bilvosita o‘lchash</b>: natija bevosita o‘lchangan kattaliklardan formula orqali topiladi, xatolik esa xatoliklarni qo‘shish qoidasi bilan hisoblanadi. Diametr kvadratda qatnashgani uchun uning nisbiy xatoligi ikki marta katta hissa qo‘shadi. Natija jadval qiymati bilan solishtirilib, jism materiali aniqlanadi (alyuminiy 2,70; po‘lat 7,8; latun 8,4–8,7; mis 8,96 g/sm³).</p>""",
 steps=["Tarozini sathga keltiring (elektron tarozini nolga sozlang).", "Jism massasini 3 marta o‘lchang (har safar qaytadan qo‘yib).", "Silindr diametri va balandligini (parallelepipedning uch qirrasini) shtangensirkul bilan 5 martadan o‘lchang.", "Har bir kattalikning o‘rtacha qiymati va to‘liq xatoligini hisoblang.", "Zichlikni hamda uning nisbiy va absolyut xatoligini hisoblang.", "Natijani jadval qiymatlari bilan solishtirib, jism materialini aniqlang; farq xatolik chegarasida ekanini tekshiring.", "Boshqa shakldagi jism uchun 2–6-bandlarni takrorlang."],
 table=(["Jism", "m, g", "d (a), mm", "h (b, c), mm", "V, sm³", "ρ, g/sm³"], [["Silindr №1", "39,05", "20,14", "45,26", "14,42", "2,71"], ["Parallelepiped №2", "112,4", "a = 20,0", "b = 15,1; c = 44,1", "13,32", "8,44"]]),
 calc=r"""<p><b>Silindr:</b> \(\bar m=39{,}05\) g (\(\Delta m=0{,}02\) g, \(\varepsilon_m=0{,}05\,\%\)), \(\bar d=20{,}14\pm0{,}12\) mm (\(\varepsilon_d=0{,}60\,\%\)), \(\bar h=45{,}26\pm0{,}12\) mm (\(\varepsilon_h=0{,}27\,\%\)).</p>
$$\rho=\frac{4\cdot39{,}05}{\pi\cdot2{,}014^2\cdot4{,}526}=2{,}71\ \text{g/sm}^3$$
<p>\(\varepsilon_\rho=\sqrt{0{,}05^2+(2\cdot0{,}60)^2+0{,}27^2}\,\%=1{,}2\,\%\), \(\Delta\rho=0{,}03\) g/sm³. <b>Natija:</b> \(\rho=(2{,}71\pm0{,}03)\) g/sm³, \(P=0{,}95\) — alyuminiy (jadvalda 2,70 g/sm³).</p>
<p><b>Parallelepiped:</b> \(V=abc=13{,}32\) sm³, \(\rho=112{,}4/13{,}32=8{,}44\) g/sm³ — latun.</p>""",
 code="""import numpy as np
m, dm = 39.05, 0.02          # g
d, dd = 2.014, 0.012         # sm
h, dh = 4.526, 0.012         # sm
rho = 4*m/(np.pi*d**2*h)
eps = np.sqrt((dm/m)**2 + (2*dd/d)**2 + (dh/h)**2)
print(f"rho = ({rho:.2f} ± {rho*eps:.2f}) g/sm³, eps = {100*eps:.1f} %")
jadval = {"alyuminiy": 2.70, "po'lat": 7.80, "latun": 8.50, "mis": 8.96, "qo'rg'oshin": 11.34}
mat = min(jadval, key=lambda k: abs(jadval[k] - rho))
print("Eng yaqin material:", mat, jadval[mat])""",
 questions=["Zichlikning SI birligi va g/sm³ bilan bog‘lanishi qanday?", "Bilvosita o‘lchash xatoligi qanday hisoblanadi?", "Nima uchun diametr xatoligi zichlik xatoligiga ikki baravar ko‘p hissa qo‘shadi?", "Jism ichida bo‘shliq bo‘lsa, natija qanday o‘zgaradi?", "Noto‘g‘ri shakldagi jism zichligini qanday aniqlash mumkin (L3, L4 ga bog‘lang)?"]
))

B.append(dict(
 n=3, sess=[3], lec=11, area="mex", tn=["TN2", "TN6"],
 title="Piknometr yordamida suyuqlik zichligini aniqlash",
 goal="Piknometr yordamida suyuqlik (etil spirti, eritma yoki glitserin) zichligini distillangan suv zichligi bilan taqqoslash usulida aniqlash va natija xatoligini baholash.",
 equip=["Piknometr (25 yoki 50 ml)", "Elektron tarozi (0,001 g)", "Distillangan suv va tekshiriladigan suyuqlik", "Termometr", "Filtr qog‘ozi, pipetka"],
 theory=r"""<p><b>Piknometr</b> — hajmi aniq belgilangan (kapillyarli tiqin yoki belgi bilan) kichik shisha idish. Usul hajmni bevosita o‘lchamasdan, massalarni taqqoslashga asoslangan. Bo‘sh piknometr massasi \(m_0\), suv bilan \(m_1\), tekshiriladigan suyuqlik bilan \(m_2\) bo‘lsin. Ikkala holatda hajm bir xil, shuning uchun:</p>
$$\rho_x=\rho_\text{suv}\frac{m_2-m_0}{m_1-m_0}$$
<p>Suv zichligi temperaturaga bog‘liq: 15 °C da 999,1; 20 °C da 998,2; 25 °C da 997,0 kg/m³ — shuning uchun tajriba temperaturasi yoziladi. Usul aniqligi yuqori (0,05 % gacha), chunki asosiy xatolik manbai faqat tortish va piknometrni belgigacha to‘ldirish aniqligidir. Havo pufakchalari va piknometr tashqarisidagi namlik xatolikka olib keladi.</p>""",
 steps=["Piknometrni yuvib, quriting va bo‘sh holda (tiqini bilan) tortib, m₀ ni yozing.", "Piknometrni distillangan suv bilan belgigacha to‘ldiring, tashqarisini filtr qog‘oz bilan quriting va torting — m₁.", "Suv temperaturasini o‘lchang va jadvaldan ρ_suv ni oling.", "Suvni to‘kib, piknometrni tekshiriladigan suyuqlik bilan chayqang, so‘ng to‘ldirib torting — m₂.", "Har bir tortishni 3 marta takrorlang (piknometrni qaytadan to‘ldirib).", "ρ_x ni va uning xatoligini hisoblang, jadval qiymati bilan solishtiring."],
 table=(["Tajriba", "m₀, g", "m₁ (suv bilan), g", "m₂ (suyuqlik bilan), g", "ρ_x, kg/m³"], [["1", "18,215", "43,180", "37,962", "789,6"], ["2", "18,214", "43,178", "37,958", "789,5"], ["3", "18,216", "43,183", "37,965", "789,6"], ["O‘rtacha", "18,215", "43,180", "37,962", "789,5"]]),
 calc=r"""<p>Har bir tajriba uchun \(\rho_x=\rho_\text{suv}\frac{m_2-m_0}{m_1-m_0}\), \(\rho_\text{suv}(20\,^\circ\text{C})=998{,}2\) kg/m³. Masalan, 1-tajriba: \(\rho_x=998{,}2\cdot\frac{19{,}747}{24{,}965}=789{,}6\) kg/m³.</p>
<p>O‘rtacha \(\bar\rho_x=789{,}5\) kg/m³; tasodifiy xatolik (\(n=3\), \(t=4{,}30\)): \(\Delta_\text{t}=0{,}13\) kg/m³. Tortish (\(\Delta m=0{,}002\) g) va temperatura (\(\pm0{,}5\) °C) xatoliklaridan \(\varepsilon_\text{B}\approx0{,}02\,\%\), \(\Delta_\text{B}=0{,}16\) kg/m³. To‘liq: \(\Delta\rho=\sqrt{0{,}13^2+0{,}16^2}=0{,}2\) kg/m³.</p>
<p><b>Natija:</b> \(\rho_x=(789{,}5\pm0{,}2)\) kg/m³, \(P=0{,}95\). Jadvalda etil spirti uchun 20 °C da 789,3 kg/m³ — natija mos keladi.</p>""",
 code="""import numpy as np
m0 = np.array([18.215, 18.214, 18.216])   # bo'sh piknometr, g
m1 = np.array([43.180, 43.178, 43.183])   # suv bilan, g
m2 = np.array([37.962, 37.958, 37.965])   # suyuqlik bilan, g
rho_w = 998.2                              # suv zichligi (20 °C), kg/m³
rho = rho_w*(m2 - m0)/(m1 - m0)
n = len(rho); t95 = {3: 4.30, 4: 3.18, 5: 2.78}[n]
dt = t95*rho.std(ddof=1)/np.sqrt(n)
dB = rho.mean()*np.sqrt((0.0028/(m2 - m0).mean())**2 + (0.0028/(m1 - m0).mean())**2 + (0.1/rho_w)**2)
print("Har bir tajriba:", np.round(rho, 1))
print(f"rho = ({rho.mean():.1f} ± {np.hypot(dt, dB):.1f}) kg/m³")""",
 questions=["Piknometr usulining g‘oyasi nimada? Nima uchun hajmni o‘lchash shart emas?", "Suv zichligi temperaturaga qanday bog‘liq va bu natijaga qanday ta’sir qiladi?", "Piknometrda havo pufakchasi qolsa, natija ortadimi yoki kamayadimi?", "Eritma konsentratsiyasini zichlik orqali qanday aniqlash mumkin?", "Piknometr va areometr usullarini aniqlik bo‘yicha taqqoslang."]
))

B.append(dict(
 n=4, sess=[4], lec=11, area="mex", sim="archimedes", tn=["TN2", "TN6"],
 title="Suyuqlikda cho‘kadigan jismlarning zichligini gidrostatik tortish usulida aniqlash",
 goal="Suyuqlikda cho‘kadigan noto‘g‘ri shakldagi jismlarning zichligini gidrostatik tortish (Arximed qonuni) usulida aniqlash; usulni suyuqlik zichligini aniqlashga qo‘llash.",
 equip=["Gidrostatik tortish moslamasi bo‘lgan tarozi (0,01 g)", "Ingichka ip yoki sim ilmoq", "Distillangan suv solingan stakan", "Tekshiriladigan jismlar (metall bo‘laklari, shisha)", "Termometr"],
 theory=r"""<p>Jism havoda tortilganda tarozi \(m_1\) ni ko‘rsatadi. Suyuqlikka to‘liq botirilganda unga Arximed kuchi \(F_A=\rho_\text{s}gV\) ta’sir qiladi va ko‘rsatish \(m_2=m_1-\rho_\text{s}V\) gacha kamayadi. Bundan jism hajmi \(V=(m_1-m_2)/\rho_\text{s}\) va zichligi:</p>
$$\rho=\rho_\text{s}\frac{m_1}{m_1-m_2}$$
<p>Usul noto‘g‘ri shakldagi jismlar uchun qulay. Aniq o‘lchashda havoning Arximed kuchi (\(\rho_\text{havo}\approx1{,}2\) kg/m³) uchun tuzatma kiritiladi: \(\rho=(\rho_\text{s}-\rho_\text{havo})\frac{m_1}{m_1-m_2}+\rho_\text{havo}\). Jism sirtidagi havo pufakchalari \(m_2\) ni oshirib, zichlikni kamaytiradi — ularni yo‘qotish kerak. Shu usulni teskari qo‘llab, zichligi ma’lum jism yordamida noma’lum suyuqlik zichligini topish mumkin: \(\rho_x=\rho_\text{j}(m_1-m_3)/m_1\).</p>""",
 steps=["Tarozini sozlang; ilmoq (ip) massasini alohida tortib, hisobga oling.", "Jismni havoda 3 marta torting — m₁.", "Jismni stakandagi suvga to‘liq botiring (idish devori va tubiga tegmasin) va havo pufakchalarini yo‘qoting.", "Suvdagi ko‘rsatishni 3 marta yozing — m₂.", "Suv temperaturasini o‘lchab, ρ_suv ni jadvaldan oling.", "Zichlik va xatolikni hisoblang, materialni aniqlang.", "Qo‘shimcha: shu jismni noma’lum suyuqlikda tortib (m₃), suyuqlik zichligini toping."],
 table=(["Jism", "m₁ (havoda), g", "m₂ (suvda), g", "m₁ − m₂, g", "V, sm³", "ρ, kg/m³"], [["Metall bo‘lagi", "62,48", "54,52", "7,96", "7,97", "7835"], ["Shisha bo‘lagi", "25,30", "15,18", "10,12", "10,14", "2495"]]),
 calc=r"""<p>\(\rho_\text{suv}=998{,}2\) kg/m³ (20 °C). Metall uchun: \(\rho=998{,}2\cdot\frac{62{,}48}{7{,}96}=7835\) kg/m³.</p>
<p>Xatolik: \(\Delta m_1=\Delta m_2=0{,}02\) g bo‘lsa, \(\Delta(m_1-m_2)=0{,}028\) g. \(\varepsilon_\rho=\sqrt{\left(\frac{0{,}02}{62{,}48}\right)^2+\left(\frac{0{,}028}{7{,}96}\right)^2}\approx0{,}35\,\%\), \(\Delta\rho\approx28\) kg/m³.</p>
<p><b>Natija:</b> \(\rho=(7835\pm28)\) kg/m³ — po‘lat (jadvalda 7800–7850 kg/m³). Shisha uchun \(\rho=(2495\pm7)\) kg/m³.</p>
<div class="callout info"><b>E’tibor bering</b>Asosiy xatolik ayirma \(m_1-m_2\) dan keladi: jism hajmi qanchalik kichik bo‘lsa, nisbiy xatolik shunchalik katta.</div>""",
 code="""import numpy as np
rho_s = 998.2                              # suv zichligi, kg/m³ (20 °C)
m1 = np.array([62.48, 62.47, 62.49])       # havoda, g
m2 = np.array([54.52, 54.53, 54.51])       # suvda, g
M1, M2 = m1.mean(), m2.mean()
rho = rho_s*M1/(M1 - M2)
dm = 0.02
eps = np.hypot(dm/M1, np.sqrt(2)*dm/(M1 - M2))
print(f"V = {(M1 - M2)/rho_s*1000:.2f} sm³")
print(f"rho = ({rho:.0f} ± {rho*eps:.0f}) kg/m³")""",
 questions=["Arximed qonunini ta’riflang va gidrostatik tortishda u qanday ishlatiladi?", "Jism sirtida havo pufakchalari qolsa, natija qanday o‘zgaradi?", "Suvdan yengil jismning zichligini bu usulda qanday aniqlash mumkin (cho‘ktiruvchi yuk)?", "Havoning Arximed kuchi uchun tuzatma qachon zarur?", "Bu usul bilan noma’lum suyuqlik zichligi qanday topiladi?"]
))

B.append(dict(
 n=5, sess=[5], lec=4, area="mex", sim="newton", tn=["TN2", "TN6"],
 title="Qattiq jismlarning sirpanish ishqalanish koeffitsiyentini aniqlash",
 goal="Qattiq jismlarning sirpanish ishqalanish koeffitsiyentini ikki usulda — dinamometr bilan tekis sudrash va qiya tekislik (sirpanish burchagi) usulida — aniqlash va natijalarni taqqoslash.",
 equip=["Burchagi o‘zgartiriladigan taxta (qiya tekislik) burchak o‘lchagich bilan", "Brusok (yog‘och)", "Dinamometr (0–5 N)", "Yuklar to‘plami (100 g)", "Tarozi"],
 theory=r"""<p>Sirpanish ishqalanish kuchi \(F_\text{ishq}=\mu N\), bu yerda \(N\) — tayanch reaksiya kuchi. <b>1-usul (dinamometr):</b> brusokni gorizontal sirtda tekis (o‘zgarmas tezlik bilan) sudraganda tortish kuchi ishqalanish kuchiga teng: \(F=\mu mg\). Turli yuklar bilan \(F(N)\) grafigi quriladi; uning qiyaligi \(\mu\) ni beradi.</p>
<p><b>2-usul (qiya tekislik):</b> tekislik burchagi asta oshirilib, brusok tekis sirpanadigan burchak \(\alpha_0\) topiladi. Bunda \(mg\sin\alpha_0=\mu mg\cos\alpha_0\):</p>
$$\mu=\tan\alpha_0$$
<p>Tinchlikdagi ishqalanish koeffitsiyenti \(\mu_0\) sirpanishnikidan biroz katta: jism harakatga keladigan burchak uchun \(\tan\alpha_\text{max}=\mu_0\). Ishqalanish koeffitsiyenti sirtlar materiali, ishlov berilishi, namligi va moylanganligiga bog‘liq, ammo birinchi yaqinlashuvda tegish yuzasiga bog‘liq emas.</p>""",
 steps=["Brusok massasini tarozida o‘lchang.", "Brusokni gorizontal taxtada dinamometr bilan tekis sudrang va kuchni 3 marta yozing.", "Brusokka 100 g, 200 g, 300 g yuklar qo‘yib, tajribani takrorlang.", "F(N) grafigini quring va eng kichik kvadratlar usulida qiyalikni (μ) toping.", "Taxtani qiya tekislikka aylantiring; burchakni asta oshirib, brusok tekis sirpana boshlaydigan burchakni 5 marta aniqlang.", "μ = tg α₀ ni hisoblab, 1-usul natijasi bilan solishtiring.", "Brusokni boshqa yon tomoni (yuzasi kichikroq) bilan qo‘yib, μ yuzaga bog‘liqmi — tekshiring."],
 table=(["m, kg", "N = mg, N", "F₁, N", "F₂, N", "F₃, N", "F̄, N"], [["0,150", "1,47", "0,44", "0,46", "0,45", "0,450"], ["0,250", "2,45", "0,74", "0,75", "0,73", "0,740"], ["0,350", "3,43", "1,03", "1,05", "1,04", "1,040"], ["0,450", "4,41", "1,31", "1,33", "1,32", "1,320"]]),
 calc=r"""<p><b>1-usul.</b> \(F(N)\) nuqtalariga eng kichik kvadratlar usulida to‘g‘ri chiziq o‘tkazamiz: qiyalik \(\mu=0{,}297\), ozod had 0,015 N (dinamometr nol xatoligi chegarasida). Qiyalik xatoligi (\(n=4\), \(t=4{,}30\)): \(\Delta\mu=0{,}012\). Demak \(\mu_1=0{,}297\pm0{,}012\).</p>
<p><b>2-usul.</b> Sirpanish burchagi: 16,5°; 17,0°; 16,0°; 16,5°; 17,0° \(\Rightarrow\bar\alpha_0=16{,}6^\circ\pm0{,}7^\circ\). \(\mu_2=\tan16{,}6^\circ=0{,}298\), \(\Delta\mu=\dfrac{\Delta\alpha}{\cos^2\alpha}=0{,}014\).</p>
<p><b>Xulosa:</b> ikki usul natijalari xatolik chegarasida mos keladi: \(\mu=0{,}30\pm0{,}01\) (yog‘och — yog‘och).</p>""",
 code="""import numpy as np
m = np.array([0.150, 0.250, 0.350, 0.450])          # kg
F = np.array([[0.44, 0.46, 0.45], [0.74, 0.75, 0.73],
              [1.03, 1.05, 1.04], [1.31, 1.33, 1.32]]).mean(axis=1)   # N
N = m*9.81
(k, b), cov = np.polyfit(N, F, 1, cov=True)
print(f"1-usul: mu = {k:.3f} ± {4.30*np.sqrt(cov[0, 0]):.3f}  (ozod had {b:.3f} N)")
alfa = np.array([16.5, 17.0, 16.0, 16.5, 17.0])     # gradus
a = np.radians(alfa.mean())
da = np.radians(np.hypot(2.78*alfa.std(ddof=1)/np.sqrt(len(alfa)), 0.5))
print(f"2-usul: mu = {np.tan(a):.3f} ± {da/np.cos(a)**2:.3f}")""",
 questions=["Tinchlikdagi va sirpanish ishqalanish koeffitsiyentlari qanday farq qiladi?", "Nima uchun qiya tekislik usulida μ = tg α₀?", "Ishqalanish kuchi tegish yuzasiga bog‘liqmi? Tajribangiz nimani ko‘rsatdi?", "F(N) grafigining ozod hadi nimani bildiradi?", "Ishqalanish koeffitsiyentini kamaytirish usullarini ayting."]
))

B.append(dict(
 n=6, sess=[6, 7], lec=4, area="mex", sim="beam", tn=["TN2", "TN3", "TN6"],
 title="Qattiq jismlarning elastiklik modulini egilish usulida aniqlash",
 goal="Ikki tayanchga erkin qo‘yilgan sterjen o‘rtasiga yuk osib, egilish strelasini indikator bilan o‘lchash orqali materialning Yung modulini aniqlash: 1-mashg‘ulotda po‘lat, 2-mashg‘ulotda latun (yoki alyuminiy) sterjen uchun natijalarni olib, taqqoslash.",
 equip=["Ikki prizmatik tayanchli qurilma", "To‘g‘ri burchakli kesimli sterjenlar (po‘lat, latun, alyuminiy)", "Indikator (soat tipidagi mikrometr, 0,01 mm)", "Yuk osish uchun ilmoq va 0,5 kg li yuklar", "Shtangensirkul, mikrometr, o‘lchov tasmasi"],
 theory=r"""<p>Tayanchlar orasidagi masofa \(l\), kesimi \(b\times h\) bo‘lgan sterjen o‘rtasiga \(F\) kuch qo‘yilganda uning o‘rta nuqtasi \(f\) ga egiladi (egilish strelasi). Elastiklik nazariyasidan:</p>
$$f=\frac{Fl^3}{48EI},\qquad I=\frac{bh^3}{12}\quad\Longrightarrow\quad E=\frac{Fl^3}{4bh^3f}$$
<p>bu yerda \(I\) — kesimning geometrik inersiya momenti. Egilishda sterjenning yuqori qatlamlari siqiladi, pastki qatlamlari cho‘ziladi, o‘rtadagi neytral qatlam esa uzunligini saqlaydi — shuning uchun Yung moduli egilishni ham belgilaydi. Natijaga eng katta hissani \(h\) va \(l\) (kubda) xatoligi qo‘shadi: \(\varepsilon_E=\sqrt{\varepsilon_F^2+(3\varepsilon_l)^2+\varepsilon_b^2+(3\varepsilon_h)^2+\varepsilon_f^2}\); shuning uchun \(h\) mikrometr bilan o‘lchanadi. Guk qonuni bajarilishini tekshirish uchun \(f(F)\) grafigi quriladi: u to‘g‘ri chiziq bo‘lishi va yuk olinganda strela nolga qaytishi kerak.</p>""",
 steps=["1-mashg‘ulot. Sterjen kengligi b ni shtangensirkul bilan, qalinligi h ni mikrometr bilan turli joylarda 5 martadan o‘lchang.", "Tayanchlar orasidagi masofa l ni o‘lchang va sterjenni tayanchlarga simmetrik qo‘ying.", "Indikatorni sterjen o‘rtasiga o‘rnatib, nolga sozlang.", "Yukni ketma-ket 0,5 kg dan oshirib (4 qiymat), har bir yukda indikator ko‘rsatishini yozing; so‘ng yuklarni kamaytirib, qaytish ko‘rsatishlarini yozing.", "Har bir yuk uchun o‘rtacha strelani hisoblab, \\(f(F)\\) grafigini quring; qiyalikdan \\(f/F\\) ni toping.", "E ni hisoblang va xatolikni baholang.", "2-mashg‘ulot. Latun (alyuminiy) sterjen uchun 1–6-bandlarni takrorlang.", "Ikki material natijalarini jadval qiymatlari bilan taqqoslang, xatolik manbalarini tahlil qiling va hisobotni himoya qiling."],
 table=(["F, N", "f (yuklashda), mm", "f (bo‘shatishda), mm", "f̄, mm"], [["4,91", "0,30", "0,30", "0,300"], ["9,81", "0,59", "0,60", "0,595"], ["14,72", "0,89", "0,90", "0,895"], ["19,62", "1,19", "1,20", "1,195"]]),
 calc=r"""<p>Po‘lat sterjen: \(l=500\pm1\) mm, \(b=20{,}0\pm0{,}1\) mm, \(h=5{,}00\pm0{,}01\) mm. \(f(F)\) nuqtalariga to‘g‘ri chiziq o‘tkazamiz: qiyalik \(k=f/F=0{,}0609\) mm/N (\(\varepsilon_k=1{,}2\,\%\)), ozod had \(\approx0\) — Guk qonuni bajariladi.</p>
$$E=\frac{l^3}{4bh^3k}=\frac{0{,}125}{4\cdot0{,}020\cdot1{,}25\cdot10^{-7}\cdot6{,}09\cdot10^{-5}}=2{,}05\cdot10^{11}\ \text{Pa}$$
<p>\(\varepsilon_E=\sqrt{(3\varepsilon_l)^2+\varepsilon_b^2+(3\varepsilon_h)^2+\varepsilon_k^2}=\sqrt{0{,}6^2+0{,}5^2+0{,}6^2+1{,}2^2}\,\%=1{,}6\,\%\). <b>Natija:</b> \(E=(205\pm3)\) GPa — po‘lat (jadvalda 195–210 GPa).</p>
<p>2-mashg‘ulot (latun sterjen, namunaviy natija): \(E=(101\pm2)\) GPa (jadvalda 97–105 GPa).</p>""",
 code="""import numpy as np
l, b, h = 0.500, 0.0200, 0.00500          # m
F = np.array([4.91, 9.81, 14.72, 19.62])   # N
f = np.array([[0.30, 0.30], [0.59, 0.60], [0.89, 0.90], [1.19, 1.20]]).mean(axis=1)*1e-3  # m
(k, b0), cov = np.polyfit(F, f, 1, cov=True)
E = l**3/(4*b*h**3*k)
eps = np.sqrt((3*1/500)**2 + (0.1/20)**2 + (3*0.01/5)**2 + (4.30*np.sqrt(cov[0, 0])/k)**2)
print(f"k = {k*1e3:.4f} mm/N, ozod had = {b0*1e3:.4f} mm")
print(f"E = ({E/1e9:.0f} ± {E*eps/1e9:.0f}) GPa, eps = {100*eps:.1f} %")""",
 questions=["Egilishda sterjenning qaysi qatlamlari cho‘ziladi va qaysilari siqiladi?", "Nima uchun qalinlik h mikrometr bilan o‘lchanadi?", "f(F) grafigi to‘g‘ri chiziq bo‘lishi nimani tasdiqlaydi?", "Yuk olinganda strela nolga qaytmasa, bu nimani bildiradi?", "Bir xil o‘lchamli po‘lat va latun sterjenlar egilishini taqqoslang va Yung moduli bilan tushuntiring."]
))

B.append(dict(
 n=8, sess=[8], lec=7, area="mex", sim="oscill", tn=["TN2", "TN6"],
 title="Matematik mayatnik yordamida erkin tushish tezlanishini aniqlash",
 goal="Matematik mayatnikning tebranish davrini turli uzunliklarda o‘lchab, erkin tushish tezlanishini aniqlash; T²(l) bog‘lanishining chiziqliligini tekshirish va g ni grafik usulda topish.",
 equip=["Uzunligi o‘zgartiriladigan ipga osilgan metall sharcha (shtativda)", "Sekundomer yoki fotodatchikli raqamli taymer", "O‘lchov tasmasi (1 mm)", "Shtangensirkul (sharcha diametri uchun)"],
 theory=r"""<p>Matematik mayatnik — vaznsiz cho‘zilmas ipga osilgan moddiy nuqta. Kichik og‘ishlarda (\(\varphi_0\lesssim5^\circ\)) u garmonik tebranadi va davri:</p>
$$T=2\pi\sqrt{\frac lg}\quad\Longrightarrow\quad g=\frac{4\pi^2l}{T^2}$$
<p>Real mayatnikda uzunlik \(l\) — osish nuqtasidan sharcha markazigacha: \(l=l_\text{ip}+d/2\). Davrni aniqroq o‘lchash uchun \(N=20\) ta tebranish vaqti \(t\) o‘lchanadi: \(T=t/N\); bunda reaksiya vaqti xatoligi (\(\sim0{,}2\) s) \(N\) marta kamayadi. Bir nechta uzunlikda o‘lchab, \(T^2\) ning \(l\) ga bog‘liqligi quriladi: bu to‘g‘ri chiziq, qiyaligi \(k=4\pi^2/g\). Grafik usul osish nuqtasi noaniqligini chetlab o‘tadi, chunki \(l\) dagi doimiy xatolik faqat ozod hadga ta’sir qiladi. Katta amplitudalarda davr ortadi: \(T\approx T_0(1+\varphi_0^2/16)\).</p>""",
 steps=["Sharcha diametrini shtangensirkul bilan o‘lchang; ip uzunligini l ≈ 0,4 m bo‘ladigan qilib tanlang.", "Mayatnikni 4–5° ga og‘dirib qo‘yib yuboring (bir tekislikda tebransin, aylanmasin).", "N = 20 ta to‘liq tebranish vaqtini 3 marta o‘lchang.", "Uzunlikni 0,6; 0,8; 1,0; 1,2 m ga o‘zgartirib, 2–3-bandlarni takrorlang.", "Har bir uzunlik uchun T va g ni hisoblang.", "T²(l) grafigini quring, qiyalikdan g ni toping va ikki usul natijasini solishtiring.", "Qo‘shimcha: amplitudani 20° ga oshirib, davr o‘zgarishini tekshiring."],
 table=(["l, m", "t (N = 20), s", "T, s", "T², s²", "g, m/s²"], [["0,400", "25,36", "1,268", "1,608", "9,82"], ["0,600", "31,10", "1,555", "2,418", "9,80"], ["0,800", "35,87", "1,794", "3,217", "9,82"], ["1,000", "40,15", "2,008", "4,030", "9,80"], ["1,200", "43,94", "2,197", "4,827", "9,81"]]),
 calc=r"""<p>Har bir uzunlik uchun \(g=4\pi^2l/T^2\); masalan, \(l=1{,}000\) m: \(T=40{,}15/20=2{,}0075\) s, \(g=39{,}478/4{,}030=9{,}80\) m/s². Besh qiymat o‘rtachasi \(\bar g=9{,}809\) m/s²; tasodifiy xatolik (\(n=5\), \(t=2{,}78\)) \(\Delta g_\text{t}=0{,}016\) m/s²; uzunlik xatoligi (\(\pm2\) mm) hissasi \(\approx0{,}025\) m/s². <b>Natija:</b> \(g=(9{,}81\pm0{,}03)\) m/s², \(P=0{,}95\).</p>
<p><b>Grafik usul:</b> \(T^2=kl+b\) to‘g‘ri chizig‘ining qiyaligi \(k=4{,}025\) s²/m, \(g=4\pi^2/k=9{,}808\) m/s²; ozod had \(\approx0\) — osish nuqtasi to‘g‘ri aniqlangan. Ikkala natija jadval qiymati (\(g\approx9{,}80\) m/s²) bilan mos keladi.</p>""",
 code="""import numpy as np
l = np.array([0.400, 0.600, 0.800, 1.000, 1.200])   # m
t = np.array([25.36, 31.10, 35.87, 40.15, 43.94])   # 20 ta tebranish vaqti, s
T = t/20
g = 4*np.pi**2*l/T**2
print("g har bir uzunlikda:", np.round(g, 3))
dg = np.hypot(2.78*g.std(ddof=1)/np.sqrt(len(g)), g.mean()*0.002/l.mean())
print(f"g = ({g.mean():.2f} ± {dg:.2f}) m/s²")
k, b = np.polyfit(l, T**2, 1)
print(f"Grafik usul: k = {k:.3f} s²/m, g = {4*np.pi**2/k:.3f} m/s², ozod had = {b:.4f} s²")""",
 questions=["Qanday sharoitda mayatnikni matematik deb hisoblash mumkin?", "Nima uchun bitta emas, 20 ta tebranish vaqti o‘lchanadi?", "T²(l) grafigining ozod hadi noldan farq qilsa, bu nimani bildiradi?", "Amplituda katta bo‘lsa, hisoblangan g qanday buziladi (ortadi yoki kamayadi)?", "Erkin tushish tezlanishi geografik kenglikka qanday bog‘liq?"]
))

B.append(dict(
 n=9, sess=[9], lec=7, area="mex", sim="oscill", tn=["TN2", "TN3", "TN6"],
 title="Fizik mayatnik yordamida erkin tushish tezlanishini aniqlash",
 goal="Fizik mayatnik (bir jinsli sterjen) tebranish davrini osish nuqtasining turli holatlarida o‘lchab, erkin tushish tezlanishini aniqlash; keltirilgan uzunlik va Shteyner teoremasini tajribada qo‘llash.",
 equip=["Bir jinsli metall sterjen (L = 1 m) teshiklari bilan yoki ag‘darma mayatnik", "Prizma shaklidagi tayanch (osish o‘qi)", "Sekundomer yoki raqamli taymer", "O‘lchov tasmasi"],
 theory=r"""<p>Fizik mayatnik — og‘irlik markazidan o‘tmaydigan gorizontal o‘q atrofida tebranuvchi qattiq jism. Kichik tebranishlar davri:</p>
$$T=2\pi\sqrt{\frac{I}{mga}},\qquad I=I_c+ma^2\ \text{(Shteyner)}$$
<p>bu yerda \(a\) — osish o‘qidan massa markazigacha masofa. Uzunligi \(L\) bo‘lgan bir jinsli sterjen uchun \(I_c=mL^2/12\), shunda</p>
$$T=2\pi\sqrt{\frac{L^2/12+a^2}{ga}},\qquad g=\frac{4\pi^2}{T^2}\left(\frac{L^2}{12a}+a\right)$$
<p>Keltirilgan uzunlik \(l_\text{kel}=I/(ma)\) — shu davrga ega matematik mayatnik uzunligi. Davr \(a\) ga bog‘liq va \(a=L/\sqrt{12}\) da minimal. Ag‘darma mayatnikda davrlar teng bo‘ladigan ikki qo‘shma o‘q topiladi; ular orasidagi masofa \(l_\text{kel}\) ga teng va \(g=4\pi^2l_\text{kel}/T^2\) — bu usul inersiya momentini bilishni talab qilmaydi (Kater mayatnigi).</p>""",
 steps=["Sterjen uzunligi L ni o‘lchang va massa markazini (o‘rtasini) belgilang.", "Sterjenni o‘rtasidan a ≈ 0,45 m masofadagi teshikdan osing va a ni aniq o‘lchang.", "Sterjenni 5° gacha og‘dirib, N = 20 ta tebranish vaqtini 3 marta o‘lchang.", "Tajribani a ning yana 4 xil qiymati uchun (0,10–0,35 m) takrorlang.", "Har bir a uchun g ni formuladan hisoblang.", "T(a) grafigini quring, minimal davrni toping va uni nazariy a = L/√12 bilan solishtiring.", "Natijani 8-laboratoriya ishi (matematik mayatnik) natijasi bilan taqqoslang."],
 table=(["a, m", "t (N = 20), s", "T, s", "l_kel = L²/(12a) + a, m", "g, m/s²"], [["0,450", "31,98", "1,599", "0,635", "9,81"], ["0,350", "30,76", "1,538", "0,588", "9,82"], ["0,290", "30,49", "1,525", "0,577", "9,81"], ["0,200", "31,51", "1,576", "0,617", "9,81"], ["0,100", "38,75", "1,938", "0,933", "9,82"]]),
 calc=r"""<p>Sterjen uzunligi \(L=1{,}000\) m. Masalan, \(a=0{,}450\) m: \(T=31{,}98/20=1{,}599\) s, \(l_\text{kel}=\frac{L^2}{12a}+a=0{,}635\) m, \(g=\frac{4\pi^2l_\text{kel}}{T^2}=\frac{39{,}478\cdot0{,}635}{2{,}557}=9{,}81\) m/s².</p>
<p>Besh qiymat o‘rtachasi \(\bar g=9{,}811\) m/s², tasodifiy xatolik 0,005 m/s²; \(a\) va \(L\) ni o‘lchash xatoligi (\(\pm1\) mm) hissasi \(\approx0{,}02\) m/s². <b>Natija:</b> \(g=(9{,}81\pm0{,}02)\) m/s².</p>
<p>\(T(a)\) grafigi \(a\approx0{,}29\) m da minimumga ega — nazariy \(a=L/\sqrt{12}=0{,}289\) m bilan mos keladi.</p>""",
 code="""import numpy as np
L = 1.000                                         # sterjen uzunligi, m
a = np.array([0.450, 0.350, 0.290, 0.200, 0.100])
t = np.array([31.98, 30.76, 30.49, 31.51, 38.75])  # 20 ta tebranish, s
T = t/20
lkel = L**2/(12*a) + a
g = 4*np.pi**2*lkel/T**2
print("g:", np.round(g, 3), " o'rtacha:", round(g.mean(), 3))
aa = np.linspace(0.05, 0.5, 200)
Tn = 2*np.pi*np.sqrt((L**2/12 + aa**2)/(9.81*aa))
print(f"Nazariy minimum: a = {aa[Tn.argmin()]:.3f} m (L/√12 = {L/np.sqrt(12):.3f} m)")""",
 questions=["Fizik va matematik mayatnik farqi nimada?", "Keltirilgan uzunlik nima va u qanday hisoblanadi?", "Nima uchun T(a) bog‘lanishi minimumga ega?", "Ag‘darma mayatnik usulining afzalligi nimada?", "Shteyner teoremasini ushbu ishda qanday qo‘lladingiz?"]
))

B.append(dict(
 n=10, sess=[10], lec=10, area="issiq", tn=["TN2", "TN6"],
 title="Suyuqliklarning hajmiy kengayish koeffitsiyentini aniqlash",
 goal="Dilatometr (kapillyarli kolba) yordamida suyuqlikning hajmiy issiqlikdan kengayish koeffitsiyentini aniqlash va idish kengayishini hisobga olish.",
 equip=["Kapillyar naychali shisha kolba (dilatometr)", "Suv hammomi yoki isitgichli stakan", "Termometr (0,1–0,5 °C)", "Millimetrli shkala yoki kapillyar bo‘limlari", "Tekshiriladigan suyuqlik (etil spirti)"],
 theory=r"""<p>Isitilganda suyuqlik hajmi ortadi: \(V=V_0(1+\beta\Delta t)\), bu yerda \(\beta\) — hajmiy kengayish koeffitsiyenti (K⁻¹). Suyuqliklar uchun \(\beta\) qattiq jismlarnikidan 10–100 marta katta: suv (20 °C) \(2{,}1\cdot10^{-4}\), etil spirti \(1{,}1\cdot10^{-3}\), glitserin \(5\cdot10^{-4}\) K⁻¹. Dilatometrda suyuqlik kolba va kapillyarni to‘ldiradi; isitilganda kapillyardagi sath \(\Delta h\) ga ko‘tariladi. Kuzatiladigan (ko‘rinma) kengayish idishning ham kengayishi hisobiga haqiqiydan kichik:</p>
$$\beta=\beta_\text{ko‘r}+\beta_\text{shisha},\qquad \beta_\text{ko‘r}=\frac{S\,\Delta h}{V_0\,\Delta t}$$
<p>bu yerda \(S\) — kapillyar ko‘ndalang kesim yuzasi, \(V_0\) — boshlang‘ich hajm, \(\beta_\text{shisha}\approx2{,}5\cdot10^{-5}\) K⁻¹. Suv 0–4 °C oralig‘ida anomal xossaga ega: 4 °C da uning zichligi maksimal, shuning uchun bu oraliqda \(\beta<0\).</p>""",
 steps=["Dilatometr hajmi V₀ va kapillyar diametri d ni (pasportdan yoki suv bilan tortib) aniqlang.", "Dilatometrni suyuqlik bilan havo pufakchalarisiz to‘ldiring va suv hammomiga joylashtiring.", "Boshlang‘ich temperatura t₀ va kapillyardagi sath h₀ ni yozing.", "Hammomni asta isitib, har 10 °C da (temperatura barqarorlashgach) sath h ni yozing (20–60 °C).", "Sovitishda ham o‘lchab, natijalar takrorlanishini tekshiring.", "ΔV = SΔh ni Δt ga qarshi grafikda tasvirlang; qiyalikdan β_ko‘r ni, so‘ng β ni toping."],
 table=(["t, °C", "h, sm", "Δh, sm", "ΔV = SΔh, sm³"], [["20,0", "0,00", "0,00", "0,000"], ["30,0", "3,40", "3,40", "0,107"], ["40,0", "6,86", "6,86", "0,215"], ["50,0", "10,28", "10,28", "0,323"], ["60,0", "13,68", "13,68", "0,430"]]),
 calc=r"""<p>Dilatometr: \(V_0=10{,}00\) sm³, kapillyar diametri 2,00 mm, \(S=0{,}0314\) sm². \(\Delta V(\Delta t)\) nuqtalariga eng kichik kvadratlar usulida to‘g‘ri chiziq o‘tkazamiz: qiyalik \(0{,}01075\) sm³/K.</p>
$$\beta_\text{ko‘r}=\frac{1}{V_0}\frac{dV}{dt}=\frac{0{,}01075}{10{,}00}=1{,}075\cdot10^{-3}\ \text{K}^{-1},\qquad \beta=\beta_\text{ko‘r}+\beta_\text{shisha}=1{,}10\cdot10^{-3}\ \text{K}^{-1}$$
<p>Xatolik: kapillyar diametri (\(\pm0{,}02\) mm \(\Rightarrow\varepsilon_S=2\,\%\)), \(V_0\) (0,5 %) va qiyalik (1 %) hissalaridan \(\varepsilon_\beta\approx2{,}3\,\%\). <b>Natija:</b> \(\beta=(1{,}10\pm0{,}03)\cdot10^{-3}\) K⁻¹ — etil spirti uchun jadval qiymati (\(1{,}1\cdot10^{-3}\) K⁻¹) bilan mos.</p>""",
 code="""import numpy as np
V0, d = 10.00, 0.200                             # sm³, kapillyar diametri, sm
S = np.pi*d**2/4                                 # sm²
t = np.array([20.0, 30.0, 40.0, 50.0, 60.0])     # °C
h = np.array([0.00, 3.40, 6.86, 10.28, 13.68])   # sm
dV = S*h
k, b = np.polyfit(t - t[0], dV, 1)
beta = k/V0 + 2.5e-5                             # shisha kengayishi tuzatmasi
print(f"dV/dt = {k:.5f} sm³/K, beta = {beta:.3e} 1/K")""",
 questions=["Nima uchun kuzatiladigan kengayish haqiqiysidan kichik?", "Suvning 0–4 °C dagi anomal xossasi tabiatda qanday ahamiyatga ega?", "Suyuqlikli termometrlar qaysi hodisaga asoslangan?", "Kapillyar qanchalik ingichka bo‘lsa, usul sezgirligi qanday o‘zgaradi?", "Yoqilg‘i baklari nima uchun to‘liq to‘ldirilmaydi?"]
))

B.append(dict(
 n=11, sess=[11], lec=9, area="issiq", tn=["TN2", "TN6"],
 title="Havo namligini aniqlash",
 goal="Psixrometr va kondensatsion gigrometr yordamida xona havosining nisbiy va absolyut namligini hamda shudring nuqtasini aniqlash; natijalarni psixrometrik formula va elektron gigrometr bilan taqqoslash.",
 equip=["Avgust psixrometri (quruq va ho‘l termometrlar)", "Kondensatsion gigrometr (yaltiroq sirtli kamera, efir)", "Psixrometrik jadval, to‘yingan bug‘ bosimi jadvali", "Elektron gigrometr (taqqoslash uchun)", "Barometr"],
 theory=r"""<p>Nisbiy namlik \(\varphi=p/p_\text{t}(t)\cdot100\,\%\), bu yerda \(p\) — havodagi suv bug‘ining parsial bosimi, \(p_\text{t}(t)\) — havo temperaturasidagi to‘yingan bug‘ bosimi. Absolyut namlik \(\rho=\dfrac{pM}{RT}\) (g/m³).</p>
<p><b>Psixrometr:</b> ho‘l termometr dokasidan suv bug‘lanadi va uni sovitadi; havo qanchalik quruq bo‘lsa, quruq (\(t\)) va ho‘l (\(t_h\)) termometrlar farqi shunchalik katta. Psixrometrik formula:</p>
$$p=p_\text{t}(t_h)-A\,p_\text{atm}(t-t_h)$$
<p>bu yerda \(A\) — psixrometrik koeffitsiyent (aspiratsion psixrometr uchun \(\approx6{,}6\cdot10^{-4}\) K⁻¹, Avgust psixrometri uchun havo harakatiga qarab \(\approx8\cdot10^{-4}\)–\(1{,}2\cdot10^{-3}\) K⁻¹). Amalda \(\varphi\) psixrometrik jadvaldan topiladi. <b>Kondensatsion gigrometr:</b> yaltiroq sirt asta sovitiladi; sirt xiralashgan (shudring tushgan) temperatura — shudring nuqtasi \(t_\text{sh}\). U holda \(p=p_\text{t}(t_\text{sh})\) va \(\varphi=p_\text{t}(t_\text{sh})/p_\text{t}(t)\).</p>""",
 steps=["Psixrometr ho‘l termometri dokasini distillangan suv bilan namlang.", "10–15 daqiqadan keyin (ko‘rsatish barqarorlashgach) t va t_h ni yozing; o‘lchashni 3 marta takrorlang.", "Psixrometrik jadvaldan φ ni toping va formula bo‘yicha ham hisoblang.", "Kondensatsion gigrometr kamerasiga efir quyib, havo puflab sirtni asta soviting; shudring paydo bo‘lgan va yo‘qolgan temperaturalarni yozing, o‘rtachasini t_sh deb oling.", "φ va absolyut namlikni shudring nuqtasi bo‘yicha hisoblang.", "Ikki usul va elektron gigrometr natijalarini taqqoslang."],
 table=(["Usul", "O‘lchangan kattaliklar", "p, kPa", "φ, %", "ρ, g/m³"], [["Psixrometr", "t = 22,0 °C, t_h = 15,0 °C", "1,16", "44", "8,5"], ["Kondensatsion gigrometr", "t_sh = 9,3 °C (8,8 va 9,8 °C)", "1,17", "44", "8,6"], ["Elektron gigrometr", "—", "—", "45", "—"]]),
 calc=r"""<p>To‘yingan bug‘ bosimi jadvalidan: \(p_\text{t}(22\,^\circ\text{C})=2{,}645\) kPa, \(p_\text{t}(15\,^\circ\text{C})=1{,}705\) kPa. Psixrometrik formula (\(A=8\cdot10^{-4}\) K⁻¹, \(p_\text{atm}=96{,}5\) kPa):</p>
$$p=1{,}705-8\cdot10^{-4}\cdot96{,}5\cdot7=1{,}165\ \text{kPa},\qquad \varphi=\frac{1{,}165}{2{,}645}=44\,\%$$
<p>Gigrometr: \(t_\text{sh}=9{,}3\) °C, \(p=p_\text{t}(9{,}3\,^\circ\text{C})=1{,}172\) kPa, \(\varphi=44\,\%\). Absolyut namlik \(\rho=\frac{pM}{RT}=\frac{1172\cdot0{,}018}{8{,}314\cdot295{,}2}=8{,}6\) g/m³. Termometrlar xatoligi (\(\pm0{,}2\) °C) uchun \(\Delta\varphi\approx\pm2\,\%\). <b>Natija:</b> \(\varphi=(44\pm2)\,\%\) — uchala usul mos keladi.</p>""",
 code="""import numpy as np
def p_t(t):                       # to'yingan bug' bosimi, kPa (Magnus formulasi, 0–50 °C)
    return 0.6112*np.exp(17.62*t/(243.12 + t))
t, th, p_atm, A = 22.0, 15.0, 96.5, 8e-4
p = p_t(th) - A*p_atm*(t - th)
phi = p/p_t(t)
rho = p*1e3*0.018/(8.314*(t + 273.15))*1e3      # g/m³
x = np.log(p/0.6112); t_sh = 243.12*x/(17.62 - x)   # shudring nuqtasi
print(f"p = {p:.3f} kPa, phi = {100*phi:.0f} %, rho = {rho:.1f} g/m³, t_sh = {t_sh:.1f} °C")""",
 questions=["Absolyut va nisbiy namlik farqi nimada?", "Nima uchun ho‘l termometr quruqdan past ko‘rsatadi?", "Shudring nuqtasi nima va u qanday aniqlanadi?", "Havo harakati psixrometr ko‘rsatishiga qanday ta’sir qiladi?", "Kimyo laboratoriyasida namlikni nazorat qilish nima uchun muhim?"]
))

B.append(dict(
 n=12, sess=[12], lec=10, area="issiq", sim="calorimeter", tn=["TN2", "TN6", "TN7"],
 title="Suv aralashmasining temperaturasini aniqlash",
 goal="Turli temperaturadagi suv massalarini kalorimetrda aralashtirib, aralashma temperaturasini o‘lchash va uni issiqlik balansi tenglamasi bo‘yicha hisoblangan qiymat bilan solishtirish; kalorimetrning issiqlik sig‘imini aniqlash.",
 equip=["Kalorimetr (ichki stakan, izolyatsiya, aralashtirgich)", "Termometrlar (0,1 °C)", "Elektron tarozi", "Issiq suv (isitgich) va sovuq suv", "Menzurka"],
 theory=r"""<p>Issiqlik almashinuvi faqat aralashayotgan jismlar orasida bo‘lsa (izolyatsiyalangan sistema), berilgan va olingan issiqliklar teng — <b>issiqlik balansi</b>: \(\sum Q_i=0\). Sovuq suv (\(m_1\), \(t_1\)) bo‘lgan kalorimetrga (issiqlik sig‘imi \(C_k\)) issiq suv (\(m_2\), \(t_2\)) quyilsa:</p>
$$(cm_1+C_k)(\theta-t_1)=cm_2(t_2-\theta)\quad\Rightarrow\quad\theta=\frac{(cm_1+C_k)t_1+cm_2t_2}{c(m_1+m_2)+C_k}$$
<p>Agar \(C_k\) noma’lum bo‘lsa, o‘lchangan \(\theta\) dan uni topish mumkin: \(C_k=\dfrac{cm_2(t_2-\theta)}{\theta-t_1}-cm_1\). Bu qiymat keyingi kalorimetrik ishlarda (L13–L14) ishlatiladi. Asosiy xatolik manbai — atrof bilan issiqlik almashinuvi; uni kamaytirish uchun issiq suv tez quyiladi, aralashma doimiy aralashtirib turiladi va \(\theta\) sifatida maksimal (barqaror) ko‘rsatish olinadi.</p>""",
 steps=["Kalorimetr ichki stakanini quruq holda torting, so‘ng sovuq suv quyib qayta torting — m₁.", "Sovuq suv temperaturasi t₁ ni yozing.", "Issiq suv temperaturasi t₂ ni o‘lchab, uni tezda kalorimetrga quying va aralashtiring.", "Aralashmaning barqaror (maksimal) temperaturasi θ ni yozing; keyin stakanni tortib, issiq suv massasi m₂ ni toping.", "C_k = 0 deb hisoblangan θ bilan o‘lchangan θ ni solishtiring.", "Kalorimetr issiqlik sig‘imi C_k ni hisoblang; tajribani boshqa massalar nisbati bilan takrorlang."],
 table=(["Tajriba", "m₁, g", "t₁, °C", "m₂, g", "t₂, °C", "θ (o‘lch.), °C", "θ (C_k = 0), °C", "C_k, J/K"], [["1", "150,0", "18,5", "100,0", "70,0", "38,3", "39,1", "42"], ["2", "120,0", "18,6", "130,0", "69,5", "44,0", "45,1", "44"]]),
 calc=r"""<p>1-tajriba: kalorimetr hisobga olinmasa \(\theta=\frac{m_1t_1+m_2t_2}{m_1+m_2}=39{,}1\) °C, o‘lchangan \(\theta=38{,}3\) °C. Farq kalorimetr isishiga ketgan issiqlik bilan izohlanadi:</p>
$$C_k=\frac{cm_2(t_2-\theta)}{\theta-t_1}-cm_1=\frac{418{,}6\cdot31{,}7}{19{,}8}-627{,}9=42\ \text{J/K}$$
<p>2-tajribada \(C_k=44\) J/K. Termometrlar xatoligi (\(\pm0{,}1\) °C) har bir tajribada \(\Delta C_k\approx7\) J/K beradi. O‘rtacha: \(C_k=(43\pm5)\) J/K. Bu qiymat L13–L14 da ishlatiladi.</p>""",
 code="""import numpy as np
c = 4186.0                                   # J/(kg·K)
m1, t1, m2, t2, th = 0.150, 18.5, 0.100, 70.0, 38.3
th0 = (m1*t1 + m2*t2)/(m1 + m2)              # kalorimetrsiz nazariy qiymat
Ck = c*m2*(t2 - th)/(th - t1) - c*m1
# xatolik: termometrlar ±0,1 °C
dC = np.sqrt((c*m2*(t2 - t1)/(th - t1)**2*0.1)**2 + (c*m2*(t2 - th)/(th - t1)**2*0.1)**2 + (c*m2/(th - t1)*0.1)**2)
print(f"theta(Ck=0) = {th0:.1f} °C, Ck = ({Ck:.0f} ± {dC:.0f}) J/K")""",
 questions=["Issiqlik balansi tenglamasi qaysi saqlanish qonunining natijasi?", "Nima uchun o‘lchangan θ nazariy qiymatdan kichik?", "Kalorimetrning issiqlik sig‘imi nima va u qanday topiladi?", "Atrof bilan issiqlik almashinuvini qanday kamaytirish mumkin?", "Aralashma temperaturasini o‘lchashda nima uchun maksimal ko‘rsatish olinadi?"]
))

B.append(dict(
 n=13, sess=[13, 14], lec=10, area="issiq", sim="calorimeter", tn=["TN2", "TN6", "TN7"],
 title="Qattiq jismlarning solishtirma issiqlik sig‘imini aniqlash",
 goal="Aralashtirish (kalorimetrik) usulida qattiq jismlarning — 1-mashg‘ulotda alyuminiy, 2-mashg‘ulotda mis yoki po‘lat — solishtirma issiqlik sig‘imini aniqlash va natijani Dyulong–Pti qonuni bilan solishtirish.",
 equip=["Kalorimetr (C_k L12 dan ma’lum)", "Bug‘li isitgich (qaynatgich) va metall namunalar (Al, Cu, po‘lat)", "Termometrlar (0,1 °C)", "Elektron tarozi", "Qisqich"],
 theory=r"""<p>Qaynayotgan suv bug‘ida \(t_2\approx100\) °C gacha qizdirilgan, massasi \(m\) bo‘lgan jism suvli kalorimetrga (\(m_1\), \(t_1\), \(C_k\)) tez tushiriladi. Issiqlik balansidan:</p>
$$cm(t_2-\theta)=(c_\text{s}m_1+C_k)(\theta-t_1)\quad\Rightarrow\quad c=\frac{(c_\text{s}m_1+C_k)(\theta-t_1)}{m(t_2-\theta)}$$
<p>Natijani Dyulong–Pti qonuni bilan solishtirish mumkin: oddiy temperaturalarda ko‘pchilik metallarning molyar issiqlik sig‘imi \(C_\mu=cM\approx3R\approx25\) J/(mol·K). Bu qonun kristall panjara atomlarining tebranma energiyasi (har bir atomga \(3kT\)) bilan tushuntiriladi; past temperaturalarda u buziladi (Eynshteyn va Debay kvant nazariyasi). Jadval qiymatlari: Al 900, Fe 450, Cu 385, Pb 130 J/(kg·K).</p>""",
 steps=["1-mashg‘ulot. Alyuminiy namunani tortib, qaynatgichga joylashtiring va 15–20 daqiqa qizdiring (t₂ ni termometr bilan nazorat qiling).", "Kalorimetrga m₁ massali sovuq suv quyib, t₁ ni yozing.", "Namunani tezda (1–2 s ichida) kalorimetrga o‘tkazing, aralashtiring va maksimal temperatura θ ni yozing.", "c ni hisoblang; tajribani yana bir marta takrorlang.", "2-mashg‘ulot. Mis (yoki po‘lat) namuna uchun 1–4-bandlarni takrorlang.", "Har bir metall uchun molyar issiqlik sig‘imini hisoblab, Dyulong–Pti qonuni bilan solishtiring.", "Xatolik manbalarini (namunani o‘tkazishda sovish, issiqlik yo‘qotish) tahlil qiling va hisobotni himoya qiling."],
 table=(["Namuna", "m, g", "t₂, °C", "m₁, g", "t₁, °C", "θ, °C", "c, J/(kg·K)", "C_μ = cM, J/(mol·K)"], [["Alyuminiy", "80,0", "99,5", "150,0", "19,0", "26,7", "887", "23,9"], ["Mis", "120,0", "99,5", "150,0", "19,2", "24,3", "379", "24,1"]]),
 calc=r"""<p>Kalorimetr: \(C_k=43\) J/K (L12), \(c_\text{s}m_1+C_k=4186\cdot0{,}150+43=670{,}9\) J/K.</p>
$$c_\text{Al}=\frac{670{,}9\cdot(26{,}7-19{,}0)}{0{,}080\cdot(99{,}5-26{,}7)}=887\ \text{J/(kg·K)}$$
<p>Xatolik asosan \(\theta-t_1\) ayirmasidan (\(\pm0{,}14\) °C, 1,8 %) va \(C_k\) dan (0,7 %): \(\varepsilon_c\approx2\,\%\). <b>Natija:</b> \(c_\text{Al}=(890\pm20)\) J/(kg·K) (jadvalda 900), \(c_\text{Cu}=(380\pm11)\) J/(kg·K) (jadvalda 385). Molyar issiqlik sig‘imlari 23,9 va 24,1 J/(mol·K) — Dyulong–Pti qiymatiga (\(3R=24{,}9\)) yaqin.</p>
<div class="callout info"><b>Sistematik xatolik</b>Natijalar jadvaldan biroz kichik: namuna kalorimetrga o‘tkazilayotganda soviydi va aralashma atrofga issiqlik beradi — ikkalasi ham c ni kamaytiradi.</div>""",
 code="""import numpy as np
cs, Ck, dCk = 4186.0, 43.0, 5.0
namunalar = {  # nom: (m, t2, m1, t1, theta, M)
    "Alyuminiy": (0.080, 99.5, 0.150, 19.0, 26.7, 0.02698),
    "Mis":       (0.120, 99.5, 0.150, 19.2, 24.3, 0.06355)}
for nom, (m, t2, m1, t1, th, M) in namunalar.items():
    A = cs*m1 + Ck
    c = A*(th - t1)/(m*(t2 - th))
    eps = np.hypot(np.sqrt(2)*0.1/(th - t1), dCk/A)
    print(f"{nom}: c = ({c:.0f} ± {c*eps:.0f}) J/(kg·K), C_mol = {c*M:.1f} J/(mol·K)  (3R = {3*8.314:.1f})")""",
 questions=["Solishtirma va molyar issiqlik sig‘imlari qanday bog‘langan?", "Dyulong–Pti qonuni nimani ta’kidlaydi va qachon buziladi?", "Namunani kalorimetrga sekin o‘tkazsak, natija qanday o‘zgaradi?", "Nima uchun suvning solishtirma issiqlik sig‘imi metallarnikidan ancha katta?", "Kalorimetr issiqlik sig‘imi hisobga olinmasa, c qanday buziladi?"]
))

B.append(dict(
 n=15, sess=[15, 16], lec=10, area="issiq", sim="gas", tn=["TN2", "TN3", "TN6"],
 title="Gazlar solishtirma issiqlik sig‘imlarining nisbatini aniqlash (Kleman–Dezorm usuli)",
 goal="Kleman–Dezorm usulida havoning issiqlik sig‘imlari nisbati \\(\\gamma=C_p/C_V\\) ni aniqlash: 1-mashg‘ulotda o‘lchashlar seriyasini bajarish, 2-mashg‘ulotda klapan ochiq turish vaqtini o‘zgartirib, sistematik xatolikni tahlil qilish va natijani ekstrapolyatsiya qilish.",
 equip=["Katta shisha ballon (10–20 L) jo‘mrak va klapan bilan", "Suvli U-simon manometr", "Qo‘l nasosi (rezina nok)", "Sekundomer"],
 theory=r"""<p>Ballonga havo damlanib, ortiqcha bosim hosil qilinadi; temperatura xona temperaturasiga tenglashgach manometr \(h_1\) ni ko‘rsatadi (1-holat: \(p_1=p_0+\rho gh_1\), \(T_0\)). Klapan qisqa vaqtga ochilib, bosim atmosfera bosimigacha tushadi — kengayish tez bo‘lgani uchun <b>adiabatik</b>, havo soviydi (2-holat: \(p_0\), \(T<T_0\)). Klapan yopilgach havo izoxorik ravishda xona temperaturasigacha isiydi va manometr \(h_2\) ni ko‘rsatadi (3-holat: \(p_2=p_0+\rho gh_2\), \(T_0\)). 1→2 adiabata va 1, 3 holatlar bir izotermada yotishidan:</p>
$$\left(\frac{p_1}{p_0}\right)^{\gamma-1}=\left(\frac{p_1}{p_2}\right)^{\gamma}\quad\Longrightarrow\quad\gamma\approx\frac{h_1}{h_1-h_2}$$
<p>(taqribiy formula \(h\ll p_0/\rho g\) da o‘rinli). Havo asosan ikki atomli gaz bo‘lgani uchun nazariy \(\gamma=(i+2)/i=1{,}40\). Klapan uzoq ochiq tursa, gaz qisman isishga ulguradi, \(h_2\) kamayib, \(\gamma\) kichik chiqadi; juda qisqa ochilsa, bosim atmosferagacha tushmaydi — shuning uchun 2-mashg‘ulotda ochiq turish vaqtining ta’siri tekshiriladi.</p>""",
 steps=["1-mashg‘ulot. Jo‘mrak orqali ballonga havo damlab, manometrda 20–25 sm farq hosil qiling va jo‘mrakni yoping.", "2–3 daqiqa kuting (temperatura tenglashadi), barqaror farq h₁ ni yozing.", "Klapanni tez ochib, bosim tenglashgan zahoti (≈ 0,5 s) yoping.", "Havo isishini kutib (2–3 daqiqa), barqaror farq h₂ ni yozing.", "Tajribani 6–10 marta takrorlang va γ ni har biri uchun hisoblang.", "2-mashg‘ulot. Klapan ochiq turish vaqti τ = 0,5; 1; 2; 3 s bo‘lgan seriyalarni bajaring.", "γ(τ) grafigini quring, τ → 0 ga ekstrapolyatsiya qiling va natijani nazariy 1,40 bilan solishtiring."],
 table=(["№", "h₁, sm", "h₂, sm", "h₁ − h₂, sm", "γ = h₁/(h₁ − h₂)"], [["1", "22,0", "5,9", "16,1", "1,366"], ["2", "23,5", "6,4", "17,1", "1,374"], ["3", "21,0", "5,6", "15,4", "1,364"], ["4", "24,0", "6,6", "17,4", "1,379"], ["5", "22,5", "6,0", "16,5", "1,364"], ["6", "20,5", "5,6", "14,9", "1,376"], ["O‘rtacha", "", "", "", "1,371"]]),
 calc=r"""<p>1-mashg‘ulot (klapan ≈ 0,5 s ochiq): olti tajriba o‘rtachasi \(\bar\gamma=1{,}371\); tasodifiy xatolik (\(n=6\), \(t=2{,}57\)) 0,007; manometr shkalasi (\(\pm1\) mm) hissasi \(\approx0{,}006\). Natija: \(\gamma=1{,}37\pm0{,}01\).</p>
<p>2-mashg‘ulot: klapanning ochiq turish vaqti \(\tau=0{,}5;\ 1;\ 2;\ 3\) s da \(\gamma=1{,}37;\ 1{,}34;\ 1{,}30;\ 1{,}26\). Chiziqli ekstrapolyatsiya \(\tau\to0\): \(\gamma_0=1{,}39\pm0{,}02\) — ikki atomli gaz uchun nazariy 1,40 ga mos. Kichikroq natijalar kengayish to‘liq adiabatik bo‘lmasligi (devorlardan issiqlik oqimi) bilan izohlanadi.</p>""",
 code="""import numpy as np
h1 = np.array([22.0, 23.5, 21.0, 24.0, 22.5, 20.5])   # sm
h2 = np.array([5.9, 6.4, 5.6, 6.6, 6.0, 5.6])
g = h1/(h1 - h2)
dg = np.hypot(2.57*g.std(ddof=1)/np.sqrt(len(g)), 0.006)
print("gamma:", np.round(g, 3), f"-> {g.mean():.3f} ± {dg:.3f}")
tau = np.array([0.5, 1.0, 2.0, 3.0]); gt = np.array([1.37, 1.34, 1.30, 1.26])
k, b = np.polyfit(tau, gt, 1)
print(f"Ekstrapolyatsiya tau -> 0: gamma0 = {b:.3f} (nazariya: 1,400 ikki atomli gaz uchun)")""",
 questions=["Nima uchun klapan ochilganda havo soviydi?", "Qaysi jarayonlar adiabatik, izoxorik va izotermik deb qaraladi?", "γ ning nazariy qiymati gaz molekulasi tuzilishiga qanday bog‘liq?", "Klapan uzoq ochiq tursa, natija qanday buziladi va nima uchun?", "γ ni bilish tovush tezligini hisoblashda qanday qo‘llaniladi?"]
))

B.append(dict(
 n=17, sess=[17], lec=11, area="issiq", sim="capillary", tn=["TN2", "TN6"],
 title="Tomchilar usulida sirt taranglik koeffitsiyentini aniqlash",
 goal="Tomchilar (tomchi uzilishi) usulida suyuqliklarning sirt taranglik koeffitsiyentini aniqlash; suv bilan taqqoslash orqali nisbiy usulni qo‘llash va sirt-faol modda ta’sirini kuzatish.",
 equip=["Byuretka yoki jo‘mrakli tomizgich (bo‘yni diametri ma’lum)", "Elektron tarozi (0,001 g) va byuks", "Distillangan suv, tekshiriladigan suyuqliklar (spirt, sovunli suv)", "Shtangensirkul yoki o‘lchov mikroskopi (bo‘yin diametri uchun)", "Termometr"],
 theory=r"""<p>Tomizgich uchida osilib turgan tomchini sirt taranglik kuchi ushlab turadi; tomchi og‘irligi bo‘yin aylanasi bo‘ylab ta’sir etuvchi sirt taranglik kuchiga tenglashganda u uziladi:</p>
$$mg\approx\pi d\sigma\quad\Longrightarrow\quad\sigma=\frac{mg}{\pi d}=\frac{Mg}{\pi dN}$$
<p>bu yerda \(M\) — \(N\) ta tomchi massasi, \(d\) — tomchi uzilish bo‘yni diametri. Haqiqatda tomchining bir qismi uzilmay qoladi, shuning uchun aniq o‘lchashda tuzatish koeffitsiyenti kiritiladi yoki <b>nisbiy usul</b> qo‘llanadi: bir xil tomizgichdan suv (\(\sigma_0\) ma’lum) va tekshiriladigan suyuqlik tomiziladi:</p>
$$\sigma_x=\sigma_0\frac{m_x}{m_0}$$
<p>(\(m_x\), \(m_0\) — bitta tomchining o‘rtacha massalari). Sirt taranglik temperatura ortishi bilan kamayadi (suv: 20 °C da 72,8; 40 °C da 69,6 mN/m), sirt-faol moddalar qo‘shilganda keskin kamayadi.</p>""",
 steps=["Toza byuksni torting.", "Byuretkadan byuksga suvni sekin tomizib (bir tomchi 2–3 s da), N = 50 tomchini sanang; byuksni torting va bitta tomchi massasi m₀ ni toping. 3 marta takrorlang.", "Tomizgich bo‘yni diametri d ni o‘lchang.", "Xuddi shu tomizgich bilan tekshiriladigan suyuqlik (spirt) uchun 2-bandni takrorlang — m_x.", "σ ni absolyut formula va nisbiy usul bilan hisoblang.", "Suvga bir tomchi suyuq sovun qo‘shib, tajribani takrorlang va natijani izohlang."],
 table=(["Suyuqlik", "50 tomchi massasi M, g (3 tajriba)", "Bitta tomchi m, mg", "σ (nisbiy usul), mN/m"], [["Distillangan suv (20 °C)", "1,470; 1,472; 1,467", "29,39", "72,8 (jadval)"], ["Etil spirti", "0,451; 0,449; 0,452", "9,01", "22,3"], ["Sovunli suv", "0,621; 0,618; 0,622", "12,41", "30,7"]]),
 calc=r"""<p><b>Absolyut baho</b> (suv, \(d=2{,}10\) mm): \(\sigma=\frac{mg}{\pi d}=\frac{29{,}39\cdot10^{-6}\cdot9{,}81}{\pi\cdot2{,}10\cdot10^{-3}}=43{,}7\) mN/m — jadval qiymatidan (72,8) ancha kichik: uzilishda tomchining \(\approx40\,\%\) qismi tomizgichda qoladi (Xarkins–Braun tuzatmasi \(f\approx0{,}6\)).</p>
<p><b>Nisbiy usul:</b> \(\sigma_x=\sigma_0\frac{m_x}{m_0}=72{,}8\cdot\frac{9{,}01}{29{,}39}=22{,}3\) mN/m. Xatolik: tortish (0,2–0,4 %), tomchilar hajmidagi tarqoqlik (\(\approx1\,\%\)) va tuzatma koeffitsiyentining suyuqlikka bog‘liqligi (\(\approx2\,\%\)): \(\varepsilon\approx2{,}5\,\%\). <b>Natija:</b> \(\sigma_\text{spirt}=(22{,}3\pm0{,}6)\) mN/m (jadvalda 22,3 mN/m). Sovun qo‘shilganda σ 72,8 dan 30,7 mN/m gacha kamaydi — sirt-faol modda ta’siri.</p>""",
 code="""import numpy as np
sigma0, N, d, g = 72.8e-3, 50, 2.10e-3, 9.81       # N/m, tomchilar soni, m, m/s²
M = {"suv": [1.470, 1.472, 1.467], "spirt": [0.451, 0.449, 0.452], "sovunli suv": [0.621, 0.618, 0.622]}  # g
m = {k: np.mean(v)/N*1e-3 for k, v in M.items()}    # bitta tomchi, kg
print(f"Absolyut baho (suv): sigma = {m['suv']*g/(np.pi*d)*1e3:.1f} mN/m")
for k in ["spirt", "sovunli suv"]:
    s = sigma0*m[k]/m["suv"]
    print(f"{k}: sigma = ({s*1e3:.1f} ± {0.025*s*1e3:.1f}) mN/m")""",
 questions=["Sirt taranglikning molekulyar sababi nima?", "Nima uchun absolyut formula sirt taranglikni kam ko‘rsatadi?", "Nisbiy usulning afzalligi nimada?", "Tomchilarni juda tez tomizsak, natija qanday o‘zgaradi?", "Sirt-faol moddalarning yuvish ta’siri qanday tushuntiriladi?"]
))
