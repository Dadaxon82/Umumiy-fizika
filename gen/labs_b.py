"""Laboratoriya ishlari: L18–L33 (issiqlikdan kengayish, elektr va magnetizm, optika, kvant fizikasi)."""

B = []

B.append(dict(
 n=18, sess=[18], lec=10, area="issiq", tn=["TN2", "TN6"],
 title="Qattiq jismlarning issiqlikdan kengayish koeffitsiyentini aniqlash",
 goal="Metall naycha uzunligining temperatura bilan o‘zgarishini indikator yordamida o‘lchab, chiziqli issiqlikdan kengayish koeffitsiyentini aniqlash.",
 equip=["Dilatometr qurilmasi: metall naycha (mis, alyuminiy, po‘lat), suv yoki bug‘ bilan isitish tizimi", "Indikator (0,01 mm)", "Termometr yoki termopara", "O‘lchov tasmasi"],
 theory=r"""<p>Isitilganda qattiq jism uzunligi ortadi: \(l=l_0(1+\alpha\Delta t)\), \(\alpha\) — chiziqli kengayish koeffitsiyenti (K⁻¹): alyuminiy \(23\cdot10^{-6}\), latun \(19\cdot10^{-6}\), mis \(17\cdot10^{-6}\), po‘lat \(12\cdot10^{-6}\), shisha \(9\cdot10^{-6}\), kvars \(0{,}5\cdot10^{-6}\). Hajmiy koeffitsiyent \(\beta\approx3\alpha\). Kengayish atomlararo potensialning nosimmetrikligi (angarmonizm) bilan tushuntiriladi: tebranish amplitudasi ortishi bilan atomlar orasidagi o‘rtacha masofa ham ortadi. Tajribada naychaning bir uchi mahkamlangan, ikkinchi uchi indikator shtokiga tiralgan; naychadan issiq suv yoki bug‘ o‘tkazib, temperatura va uzayish \(\Delta l\) o‘lchanadi:</p>
$$\alpha=\frac{\Delta l}{l_0\,\Delta t}$$
<p>\(\Delta l(\Delta t)\) grafigining qiyaligi \(\alpha l_0\) ga teng.</p>""",
 steps=["Naychaning ishchi uzunligi l₀ ni (mahkamlash nuqtasidan indikatorgacha) o‘lchang.", "Indikatorni nolga sozlang va boshlang‘ich temperaturani yozing.", "Naychadan issiq suv o‘tkazib, temperaturani bosqichma-bosqich oshiring (har 20 °C); har barqaror holatda Δl ni yozing.", "Bug‘ bilan isitib (≈ 98 °C), maksimal uzayishni yozing.", "Sovitishda ham ko‘rsatishlarni yozing (gisterezis yo‘qligini tekshiring).", "Δl(Δt) grafigidan α ni toping va jadval qiymati bilan solishtiring; boshqa metall uchun takrorlang."],
 table=(["t, °C", "Δt, K", "Δl (isitishda), mm", "Δl (sovitishda), mm"], [["20,0", "0", "0,00", "0,00"], ["40,0", "20,0", "0,20", "0,21"], ["60,0", "40,0", "0,41", "0,41"], ["80,0", "60,0", "0,61", "0,62"], ["98,0", "78,0", "0,80", "0,80"]]),
 calc=r"""<p>Mis naycha: \(l_0=600\pm1\) mm. \(\Delta l(\Delta t)\) nuqtalariga to‘g‘ri chiziq o‘tkazamiz: qiyalik \(0{,}01025\) mm/K.</p>
$$\alpha=\frac{1}{l_0}\frac{d(\Delta l)}{dt}=\frac{0{,}01025}{600}=1{,}71\cdot10^{-5}\ \text{K}^{-1}$$
<p>Indikator (\(\pm0{,}01\) mm) va termometr (\(\pm0{,}5\) °C) xatoliklari tufayli qiyalik xatoligi \(\approx2\,\%\): \(\alpha=(1{,}71\pm0{,}04)\cdot10^{-5}\) K⁻¹ — mis uchun jadval qiymati \(1{,}7\cdot10^{-5}\) K⁻¹. Sovitishda nuqtalar takrorlanadi — deformatsiya elastik.</p>""",
 code="""import numpy as np
l0 = 600.0                                     # mm
t  = np.array([20.0, 40.0, 60.0, 80.0, 98.0])  # °C
dl = np.array([0.00, 0.20, 0.41, 0.61, 0.80])  # mm
(k, b), cov = np.polyfit(t - t[0], dl, 1, cov=True)
alpha = k/l0
print(f"alpha = ({alpha*1e6:.2f} ± {3.18*np.sqrt(cov[0, 0])/l0*1e6:.2f})·10^-6 1/K")
jadval = {"alyuminiy": 23, "mis": 17, "latun": 19, "po'lat": 12}
print("Eng yaqin material:", min(jadval, key=lambda m: abs(jadval[m] - alpha*1e6)))""",
 questions=["Issiqlikdan kengayishning molekulyar sababi nima?", "Chiziqli va hajmiy kengayish koeffitsiyentlari qanday bog‘langan?", "Temir yo‘l relslari orasida nima uchun tirqish qoldiriladi?", "Bimetall plastinka qanday ishlaydi?", "Kimyo laboratoriyasi idishlari nima uchun kvars yoki borosilikat shishadan tayyorlanadi?"]
))

B.append(dict(
 n=19, sess=[19], lec=12, area="elektr", sim="capacitor", tn=["TN2", "TN8"],
 title="Kondensatorlarning elektr sig‘imini aniqlash",
 goal="Kondensator sig‘imini ikki usulda — razryadlanish vaqt doimiysi (RC) bo‘yicha va o‘zgaruvchan tok zanjirida sig‘im qarshiligi orqali — aniqlash; ketma-ket va parallel ulangan kondensatorlar sig‘imi formulalarini tekshirish.",
 equip=["Kondensatorlar (220–470 mkF elektrolitik, 1–10 mkF qog‘oz)", "O‘zgarmas tok manbai (10–12 V), kalit", "Ma’lum qarshilik R (47 kΩ)", "Raqamli multimetr (voltmetr) va sekundomer yoki ma’lumot yig‘ish datchigi", "O‘zgaruvchan tok manbai (50 Hz), ampermetr va voltmetr"],
 theory=r"""<p><b>1-usul (razryadlanish).</b> \(U_0\) gacha zaryadlangan kondensator \(R\) qarshilik orqali razryadlanganda kuchlanish eksponensial kamayadi:</p>
$$u(t)=U_0e^{-t/RC}\quad\Longrightarrow\quad\ln u=\ln U_0-\frac{t}{RC}$$
<p>\(\ln u(t)\) grafigi to‘g‘ri chiziq, uning qiyaligi \(-1/(RC)\). Yoki kuchlanish \(U_0/e\) (0,368 \(U_0\)) gacha tushish vaqti \(\tau=RC\) o‘lchanadi. Voltmetr ichki qarshiligi \(R_V\) (raqamli multimetrda 10 MΩ) \(R\) ga parallel ulanadi, shuning uchun \(R\ll R_V\) bo‘lishi kerak.</p>
<p><b>2-usul (o‘zgaruvchan tok).</b> Kondensator chastotasi \(f\) bo‘lgan zanjirda \(X_C=1/(2\pi fC)\) qarshilik ko‘rsatadi: \(C=\dfrac{I}{2\pi fU}\). <b>Ulashlar:</b> parallel \(C=C_1+C_2\), ketma-ket \(C=\dfrac{C_1C_2}{C_1+C_2}\).</p>""",
 steps=["Sxemani yig‘ing: manba — kalit — kondensator; kondensatorga parallel R va voltmetr (elektrolitik kondensator qutblanishiga e’tibor bering!).", "Kondensatorni zaryadlab, U₀ ni yozing; kalitni o‘chirib, har 5 s da kuchlanishni yozing.", "\\(\\ln u(t)\\) grafigini quring, qiyalikdan τ va C = τ/R ni toping.", "Ikkinchi kondensator uchun takrorlang, so‘ng ularni parallel va ketma-ket ulab, umumiy sig‘imni o‘lchang.", "O‘zgaruvchan tok zanjirida (50 Hz) qog‘oz kondensator orqali tok va kuchlanishni o‘lchab, C ni hisoblang.", "Natijalarni nominal qiymatlar va ulash formulalari bilan solishtiring."],
 table=(["t, s", "u, V", "ln(u / 1 V)"], [["0", "10,00", "2,303"], ["5", "7,96", "2,074"], ["10", "6,35", "1,848"], ["15", "5,08", "1,625"], ["20", "4,04", "1,396"], ["25", "3,23", "1,172"], ["30", "2,57", "0,944"]]),
 calc=r"""<p>\(R=47{,}0\) kΩ (\(\pm1\,\%\)). \(\ln u(t)\) nuqtalariga to‘g‘ri chiziq: qiyalik \(-0{,}04523\) s⁻¹ \(\Rightarrow\tau=22{,}1\) s.</p>
$$C=\frac{\tau}{R}=\frac{22{,}1}{4{,}70\cdot10^4}=470\ \text{mkF}$$
<p>Xatolik: \(R\) (1 %) va qiyalik (0,3 %) \(\Rightarrow\varepsilon_C\approx1\,\%\): \(C_1=(470\pm5)\) mkF (nominal 470 mkF, ruxsat etilgan chetlanish ±20 %). Xuddi shunday \(C_2=(221\pm2)\) mkF. Ulashlar: parallel — o‘lchangan 690 mkF (hisob \(C_1+C_2=691\)), ketma-ket — 150 mkF (hisob 150,3). O‘zgaruvchan tok usuli: \(U=10{,}0\) V, \(I=12{,}4\) mA, \(C=\frac{I}{2\pi fU}=3{,}95\) mkF (nominal 4 mkF).</p>""",
 code="""import numpy as np
R = 47.0e3                                        # Ω
t = np.arange(0, 35, 5)                           # s
u = np.array([10.00, 7.96, 6.35, 5.08, 4.04, 3.23, 2.57])  # V
k, b = np.polyfit(t, np.log(u), 1)
tau = -1/k
print(f"tau = {tau:.2f} s, C = {tau/R*1e6:.0f} mkF")
C1, C2 = 470e-6, 221e-6
print(f"Parallel: {(C1 + C2)*1e6:.0f} mkF, ketma-ket: {C1*C2/(C1 + C2)*1e6:.1f} mkF")
f, U, I = 50.0, 10.0, 12.4e-3
print(f"AC usuli: C = {I/(2*np.pi*f*U)*1e6:.2f} mkF")""",
 questions=["Kondensator sig‘imi nimalarga bog‘liq?", "Vaqt doimiysi τ = RC ning fizik ma’nosi nima?", "Nima uchun \\(\\ln u(t)\\) grafigi to‘g‘ri chiziq?", "Elektrolitik kondensatorni ulashda nimaga e’tibor berish kerak?", "Ketma-ket ulanganda umumiy sig‘im nima uchun eng kichigidan ham kichik?"]
))

B.append(dict(
 n=20, sess=[20], lec=13, area="elektr", sim="circuit", tn=["TN2", "TN8"],
 title="Zanjir qismi uchun Om qonuni yordamida o‘tkazgich qarshiligini aniqlash",
 goal="Ampermetr–voltmetr usulida o‘tkazgich (nixrom sim) qarshiligini aniqlash; VAX ni qurish, asboblarni ulashning ikki sxemasi xatoligini tahlil qilish va solishtirma qarshilikni hisoblash.",
 equip=["Rostlanadigan o‘zgarmas tok manbai (0–12 V)", "Ampermetr (mA) va voltmetr (yoki ikki multimetr)", "Reoxorddagi nixrom sim (l = 1 m)", "Reostat, kalit, ulovchi simlar", "Mikrometr (sim diametri uchun)"],
 theory=r"""<p>Zanjir qismi uchun Om qonuni: \(I=U/R\), demak \(R=U/I\). VAX \(I(U)\) to‘g‘ri chiziq bo‘lsa, o‘tkazgich omik; qiyalik \(1/R\). Asboblarni ulashning ikki sxemasi bor: <b>a)</b> voltmetr rezistorga bevosita parallel — ampermetr voltmetr tokini ham o‘lchaydi: \(R_\text{o‘lch}=\frac{RR_V}{R+R_V}<R\) (kichik qarshiliklar uchun qulay); <b>b)</b> voltmetr ampermetr bilan birga ulangan — voltmetr ampermetrdagi kuchlanishni ham o‘lchaydi: \(R_\text{o‘lch}=R+R_A>R\) (katta qarshiliklar uchun qulay). Uzunligi \(l\), diametri \(d\) bo‘lgan sim uchun solishtirma qarshilik:</p>
$$\rho=\frac{RS}{l}=\frac{\pi d^2R}{4l}$$
<p>Nixrom uchun \(\rho\approx1{,}1\cdot10^{-6}\) Ω·m, konstantan \(0{,}50\cdot10^{-6}\), mis \(1{,}7\cdot10^{-8}\) Ω·m.</p>""",
 steps=["a) sxema bo‘yicha zanjirni yig‘ing; o‘qituvchi tekshirgach manbani ulang.", "Reostat bilan kuchlanishni 0,5 V dan 3 V gacha o‘zgartirib, 6 juft (U, I) qiymat yozing.", "VAX grafigini quring va qiyalikdan R ni toping.", "b) sxema bo‘yicha o‘lchashni takrorlang va natijalarni solishtiring; asboblar ichki qarshiliklari ta’sirini baholang.", "Simning uzunligi l va diametri d ni o‘lchab, ρ ni hisoblang.", "Turli uzunlikdagi sim bo‘laklari uchun R(l) ni o‘lchab, ρ ni grafik usulda toping."],
 table=(["U, V", "I (a sxema), mA", "I (b sxema), mA", "R = U/I (a), Ω"], [["0,50", "57", "54", "8,77"], ["1,00", "114", "108", "8,77"], ["1,50", "172", "161", "8,72"], ["2,00", "229", "215", "8,73"], ["2,50", "285", "269", "8,77"], ["3,00", "343", "323", "8,75"]]),
 calc=r"""<p>a) sxema: \(I(U)\) qiyaligi 0,1143 A/V \(\Rightarrow R=8{,}75\) Ω (voltmetr ichki qarshiligi 10 MΩ — tuzatma \(<10^{-5}\)). b) sxemada \(R_\text{o‘lch}=9{,}30\) Ω: farq 0,55 Ω — ampermetr ichki qarshiligi \(R_A\). Demak kichik qarshiliklar a) sxema bo‘yicha o‘lchanishi kerak.</p>
<p>Solishtirma qarshilik (\(l=1{,}000\) m, \(d=0{,}400\pm0{,}005\) mm):</p>
$$\rho=\frac{\pi d^2R}{4l}=\frac{\pi\cdot(4{,}00\cdot10^{-4})^2\cdot8{,}75}{4\cdot1{,}000}=1{,}10\cdot10^{-6}\ \Omega\cdot\text{m}$$
<p>\(\varepsilon_\rho=\sqrt{(2\varepsilon_d)^2+\varepsilon_R^2+\varepsilon_l^2}=\sqrt{2{,}5^2+0{,}5^2+0{,}1^2}\,\%=2{,}6\,\%\). <b>Natija:</b> \(\rho=(1{,}10\pm0{,}03)\cdot10^{-6}\) Ω·m — nixrom.</p>""",
 code="""import numpy as np
U  = np.array([0.50, 1.00, 1.50, 2.00, 2.50, 3.00])   # V
Ia = np.array([57, 114, 172, 229, 285, 343])*1e-3      # A, a) sxema
Ib = np.array([54, 108, 161, 215, 269, 323])*1e-3      # A, b) sxema
Ra = 1/np.polyfit(U, Ia, 1)[0]; Rb = 1/np.polyfit(U, Ib, 1)[0]
print(f"R(a) = {Ra:.2f} Ω, R(b) = {Rb:.2f} Ω, R_A ≈ {Rb - Ra:.2f} Ω")
l, d, dd = 1.000, 0.400e-3, 0.005e-3
rho = np.pi*d**2*Ra/(4*l)
eps = np.sqrt((2*dd/d)**2 + 0.005**2 + 0.001**2)
print(f"rho = ({rho*1e6:.2f} ± {rho*eps*1e6:.2f})·10^-6 Ω·m")""",
 questions=["Zanjir qismi uchun Om qonunini ta’riflang.", "Qaysi hollarda a) va b) sxemalar ishlatiladi?", "VAX to‘g‘ri chiziq bo‘lmasa, bu nimani bildiradi?", "Simning solishtirma qarshiligi nimalarga bog‘liq?", "Nima uchun sim diametrini o‘lchash xatoligi natijaga eng katta ta’sir qiladi?"]
))

B.append(dict(
 n=21, sess=[21], lec=13, area="elektr", sim="wheatstone", tn=["TN2", "TN8"],
 title="Uitston ko‘prigi yordamida qarshiliklarni aniqlash",
 goal="Reoxordli Uitston ko‘prigi yordamida noma’lum qarshiliklarni aniqlash; ketma-ket va parallel ulangan qarshiliklar formulalarini tekshirish; ko‘prik sezgirligi va eng aniq o‘lchash shartini o‘rganish.",
 equip=["Reoxord (L = 100 sm kalibrlangan sim, sirpang‘ich bilan)", "Namunaviy qarshiliklar magazini R₀", "Noma’lum qarshiliklar R₁, R₂", "Nol-galvanometr (sezgir mikroampermetr) va himoya qarshiligi", "O‘zgarmas tok manbai (1,5–4 V), kalit"],
 theory=r"""<p>Uitston ko‘prigi to‘rt yelkadan iborat: \(R_x\), \(R_0\) va reoxord simining ikki qismi \(l_1\), \(l_2=L-l_1\). Galvanometr ko‘prik diagonaliga ulanadi. Sirpang‘ich galvanometrdan tok o‘tmaydigan holatga keltiriladi (muvozanat): bunda diagonal uchlari potensiallari teng va Kirxgof qoidalaridan</p>
$$\frac{R_x}{R_0}=\frac{l_1}{l_2}\quad\Longrightarrow\quad R_x=R_0\frac{l_1}{L-l_1}$$
<p>Ko‘prik usuli — <b>nol usul</b>: natija manba kuchlanishi va galvanometr shkalasiga bog‘liq emas, shuning uchun aniqligi yuqori. Nisbiy xatolik \(\varepsilon_{R_x}=\frac{L\,\Delta l}{l_1(L-l_1)}\) sirpang‘ich o‘rtada (\(l_1=L/2\)) bo‘lganda minimal — shuning uchun \(R_0\) ni \(R_x\) ga yaqin tanlash kerak. Sim bir jinsli emasligi tufayli \(R_x\) va \(R_0\) o‘rinlari almashtirilib, natijalar o‘rtachalanadi (o‘rin almashganda \(R_x=R_0\,l_2/l_1\)).</p>""",
 steps=["Sxemani yig‘ing; galvanometrni himoya qarshiligi orqali ulang.", "R₀ ni R_x ga yaqin qiymatga qo‘ying (avval taxminiy o‘lchang).", "Sirpang‘ichni surib, galvanometr toki nolga teng holatni toping, l₁ ni yozing; himoya qarshiligini olib, aniq muvozanatga keltiring.", "R_x va R₀ o‘rinlarini almashtirib, o‘lchashni takrorlang.", "R₀ ning 2–3 xil qiymati bilan o‘lchab, R_x ning o‘rtacha qiymatini toping.", "R₁ va R₂ ni alohida, so‘ng ketma-ket va parallel ulab o‘lchang; formulalar bilan solishtiring."],
 table=(["Qarshilik", "R₀, Ω", "l₁, sm", "l₂, sm", "R_x, Ω"], [["R₁", "100", "54,5", "45,5", "119,8"], ["R₁ (o‘rin almashgan: R₀l₂/l₁)", "100", "45,3", "54,7", "120,8"], ["R₁", "120", "50,0", "50,0", "120,0"], ["R₁", "150", "44,5", "55,5", "120,3"], ["R₂", "330", "50,1", "49,9", "331,3"], ["R₂", "300", "52,4", "47,6", "330,3"], ["R₁ + R₂ (ketma-ket)", "450", "50,1", "49,9", "451,8"], ["R₁ ∥ R₂ (parallel)", "100", "46,9", "53,1", "88,3"]]),
 calc=r"""<p>\(R_1\) uchun to‘rt o‘lchash o‘rtachasi \(\bar R_1=120{,}2\) Ω. Bitta o‘lchash xatoligi (\(\Delta l=0{,}1\) sm, \(l_1\approx50\) sm): \(\varepsilon=\frac{L\Delta l}{l_1l_2}=\frac{100\cdot0{,}1}{50\cdot50}=0{,}4\,\%\); namunaviy qarshilik klassi 0,2 %. Tarqoqlikdan (\(n=4\), \(t=3{,}18\)) \(\Delta_t=0{,}7\) Ω. <b>Natija:</b> \(R_1=(120{,}2\pm0{,}8)\) Ω, \(R_2=(330{,}8\pm1{,}5)\) Ω.</p>
<p>Tekshiruv: ketma-ket \(R_1+R_2=451{,}0\) Ω (o‘lchangan 451,8 Ω), parallel \(\frac{R_1R_2}{R_1+R_2}=88{,}2\) Ω (o‘lchangan 88,3 Ω) — formulalar xatolik chegarasida tasdiqlandi.</p>""",
 code="""import numpy as np
L = 100.0
olch = [(100, 54.5, False), (100, 45.3, True), (120, 50.0, False), (150, 44.5, False)]  # (R0, l1, o'rin almashganmi)
Rx = np.array([R0*((L - l1)/l1 if sw else l1/(L - l1)) for R0, l1, sw in olch])
dR = np.hypot(3.18*Rx.std(ddof=1)/np.sqrt(len(Rx)), 0.004*Rx.mean())
print("R1 qiymatlari:", np.round(Rx, 2), f"-> R1 = ({Rx.mean():.1f} ± {dR:.1f}) Ω")
R1, R2 = Rx.mean(), 330.8
print(f"Ketma-ket: {R1 + R2:.1f} Ω, parallel: {R1*R2/(R1 + R2):.1f} Ω")
for l1 in (10, 30, 50, 70, 90):                  # sezgirlik: nisbiy xatolik l1 ga bog'liqligi
    print(f"l1 = {l1} sm -> eps = {100*L*0.1/(l1*(L - l1)):.2f} %")""",
 questions=["Ko‘prik muvozanati shartini Kirxgof qoidalaridan keltirib chiqaring.", "Nima uchun ko‘prik usuli “nol usul” deyiladi va uning afzalligi nimada?", "Sirpang‘ich qayerda bo‘lganda o‘lchash xatoligi minimal?", "Manba kuchlanishi o‘zgarsa, natija o‘zgaradimi?", "Ko‘prik sxemalari datchiklarda (qarshilik termometri, tenzometr) qanday ishlatiladi?"]
))

B.append(dict(
 n=22, sess=[22], lec=13, area="elektr", sim="kirchhoff", tn=["TN2", "TN6", "TN8"],
 title="Kirxgof qoidalarini o‘rganish",
 goal="Ikki manbali tarmoqlangan zanjirda tarmoq toklari va kuchlanishlarni o‘lchab, Kirxgofning birinchi (tugun) va ikkinchi (kontur) qoidalarini tajribada tekshirish; o‘lchangan toklarni hisoblangan qiymatlar bilan solishtirish.",
 equip=["Ikki o‘zgarmas tok manbai (6 V) yoki ikki chiqishli manba", "Uchta rezistor (10–20 Ω)", "Uchta ampermetr yoki multimetr", "Voltmetr", "Ulovchi simlar, kalit"],
 theory=r"""<p>Murakkab zanjirni ketma-ket va parallel ulashlarga keltirib bo‘lmasa, Kirxgof qoidalari qo‘llanadi. <b>1-qoida (tugun):</b> tugunga kiruvchi toklar yig‘indisi chiquvchi toklar yig‘indisiga teng, \(\sum I_k=0\) (zaryad saqlanishi). <b>2-qoida (kontur):</b> ixtiyoriy yopiq konturda kuchlanish tushishlari yig‘indisi EYuKlar yig‘indisiga teng, \(\sum I_kR_k=\sum\mathcal E_k\) (energiya saqlanishi). Ikki konturli zanjir uchun (\(\mathcal E_1,R_1\) | \(R_3\) | \(\mathcal E_2,R_2\)):</p>
$$I_3=I_1+I_2,\qquad \mathcal E_1=I_1R_1+I_3R_3,\qquad \mathcal E_2=I_2R_2+I_3R_3$$
<p>Toklar yo‘nalishi ixtiyoriy tanlanadi; hisobda manfiy chiqqan tok haqiqiy yo‘nalish teskari ekanini bildiradi. Manbalar va ampermetrlarning ichki qarshiliklari tegishli \(R\) larga qo‘shiladi.</p>""",
 steps=["Rezistorlar qarshiliklarini ommetr bilan, manbalar EYuK ini voltmetr bilan (yuklamasiz) o‘lchang.", "Zanjirni sxema bo‘yicha yig‘ing, har bir tarmoqqa ampermetr ulang; toklar yo‘nalishini belgilang.", "O‘qituvchi tekshirgach manbalarni ulab, I₁, I₂, I₃ ni yozing.", "Har bir rezistordagi kuchlanish tushishini voltmetr bilan o‘lchang.", "Tugun uchun I₁ + I₂ − I₃ ni va ikki kontur uchun kuchlanishlar balansini hisoblang.", "Kirxgof tenglamalarini yechib, nazariy toklarni toping va o‘lchangan qiymatlar bilan solishtiring.", "Bitta manba qutblarini almashtirib, tajribani takrorlang."],
 table=(["Kattalik", "Hisoblangan", "O‘lchangan", "Farq"], [["I₁, mA", "240", "238", "−0,8 %"], ["I₂, mA", "120", "121", "+0,8 %"], ["I₃, mA", "360", "358", "−0,6 %"], ["I₁ + I₂ − I₃, mA", "0", "1", "—"], ["ε₁ − U₁ − U₃, V", "0", "0,02", "—"], ["ε₂ − U₂ − U₃, V", "0", "0,00", "—"]]),
 calc=r"""<p>Parametrlar: \(\mathcal E_1=\mathcal E_2=6{,}00\) V, \(R_1=10{,}0\), \(R_2=20{,}0\), \(R_3=10{,}0\) Ω (manba va ampermetr qarshiliklari bilan birga). Kirxgof tenglamalari yechimi:</p>
$$I_3=\frac{\mathcal E_1/R_1+\mathcal E_2/R_2}{1+R_3(1/R_1+1/R_2)}=\frac{0{,}6+0{,}3}{2{,}5}=0{,}360\ \text{A},\qquad I_1=\frac{\mathcal E_1-I_3R_3}{R_1}=0{,}240\ \text{A},\qquad I_2=0{,}120\ \text{A}$$
<p>O‘lchangan toklar hisobdan 1 % dan kam farq qiladi (ampermetr klassi 1,0). Tugun qoidasi: \(238+121-358=1\) mA — o‘lchash xatoligi (\(\pm4\) mA) chegarasida nol. Kontur qoidasi ham 0,02 V aniqlikda bajarildi. Manba qutbi almashtirilganda \(I_2\) ishorasi teskari bo‘ldi (\(-0{,}36\) A), ammo tugun qoidasi saqlandi.</p>""",
 code="""import numpy as np
E1, E2, R1, R2, R3 = 6.0, 6.0, 10.0, 20.0, 10.0
# Noma'lumlar: I1, I2, I3.  Tenglamalar: I1 + I2 - I3 = 0;  R1*I1 + R3*I3 = E1;  R2*I2 + R3*I3 = E2
A = np.array([[1, 1, -1], [R1, 0, R3], [0, R2, R3]], dtype=float)
I = np.linalg.solve(A, [0, E1, E2])
print("Hisoblangan toklar, mA:", np.round(I*1e3, 1))
olch = np.array([238, 121, 358])*1e-3
print("Farq, %:", np.round(100*(olch - I)/I, 2))
P_manba = E1*I[0] + E2*I[1]
P_yuk = R1*I[0]**2 + R2*I[1]**2 + R3*I[2]**2
print(f"Quvvat balansi: {P_manba:.3f} W = {P_yuk:.3f} W")""",
 questions=["Kirxgof qoidalari qaysi saqlanish qonunlariga asoslangan?", "Tok yo‘nalishi noto‘g‘ri tanlansa, hisobda nima bo‘ladi?", "Mustaqil tenglamalar soni qanday aniqlanadi?", "Ampermetrlar ichki qarshiligi natijaga qanday ta’sir qiladi?", "Kirxgof qoidalarini elektrokimyoviy zanjirlarga qo‘llashga misol keltiring."]
))

B.append(dict(
 n=23, sess=[23], lec=14, area="elektr", sim="vacdiode", tn=["TN2", "TN4", "TN8"],
 title="Vakuum diodning volt-amper xarakteristikasini o‘rganish",
 goal="Vakuum diodning volt-amper xarakteristikasini katodning turli qizish toklarida qurish; “3/2” qonunini tekshirish va to‘yinish tokining katod temperaturasiga bog‘liqligini o‘rganish.",
 equip=["Vakuum diod (panel bilan)", "Anod manbai (0–150 V, rostlanadigan) va qizish manbai (6,3 V)", "Milliampermetr, voltmetr", "Qizish tokini rostlash reostati va ampermetr"],
 theory=r"""<p>Qizdirilgan katod termoelektron emissiya hisobiga elektronlar chiqaradi. Anod musbat bo‘lganda elektronlar anodga tortiladi. Kichik anod kuchlanishlarida katod yaqinidagi elektron buluti (fazoviy zaryad) maydonni zaiflashtiradi va tok Boguslavskiy–Lengmyur qonuniga bo‘ysunadi:</p>
$$I_a=bU_a^{3/2}\quad\Longrightarrow\quad\lg I_a=\lg b+\tfrac32\lg U_a$$
<p>Demak \(\lg I_a\) ning \(\lg U_a\) ga bog‘liqligi qiyaligi 1,5 bo‘lgan to‘g‘ri chiziq. Anod kuchlanishi yetarlicha katta bo‘lganda katoddan chiqqan barcha elektronlar anodga yetadi — <b>to‘yinish toki</b> \(I_\text{to‘y}=SBT^2e^{-A/kT}\) kuzatiladi; u katod temperaturasi (qizish toki) bilan keskin ortadi. Anod kuchlanishi teskari bo‘lsa, tok deyarli nol — diod to‘g‘rilagich vazifasini bajaradi.</p>""",
 steps=["Sxemani yig‘ing: qizish zanjiri (reostat, ampermetr) va anod zanjiri (manba, milliampermetr, voltmetr).", "Qizish tokini nominal qiymatga qo‘ying va 2–3 daqiqa kuting.", "Anod kuchlanishini 0 dan 120 V gacha oshirib (har 5–20 V), anod tokini yozing.", "Qizish tokini kamaytirib (yana ikki qiymat), VAX ni qayta yozing.", "Barcha VAX larni bitta grafikda chizing va to‘yinish toklarini aniqlang.", "Boshlang‘ich soha uchun \\(\\lg I_a(\\lg U_a)\\) grafigini quring va qiyalikni 1,5 bilan solishtiring."],
 table=(["U_a, V", "I_a, mA (I_q = 1,0 A)", "I_a, mA (I_q = 0,9 A)", "I_a, mA (I_q = 0,8 A)"], [["5", "0,22", "0,22", "0,22"], ["10", "0,63", "0,63", "0,63"], ["20", "1,79", "1,79", "1,78"], ["30", "3,29", "3,29", "3,10"], ["40", "5,06", "5,00", "4,30"], ["60", "9,30", "8,70", "4,90"], ["80", "14,3", "9,80", "5,00"], ["100", "19,2", "10,0", "5,00"], ["120", "19,9", "10,0", "5,00"]]),
 calc=r"""<p><b>“3/2” qonuni.</b> Boshlang‘ich soha (5–40 V) uchun \(\lg I_a(\lg U_a)\) nuqtalariga to‘g‘ri chiziq o‘tkazamiz: qiyalik \(1{,}51\pm0{,}02\) — nazariy 3/2 tasdiqlandi; \(b=2{,}0\cdot10^{-5}\) A/V\(^{3/2}\). Kichik kuchlanishlarda uchala egri chiziq ustma-ust tushadi: tok fazoviy zaryad bilan cheklangan va katod temperaturasiga bog‘liq emas.</p>
<p><b>To‘yinish toki</b> qizish tokiga keskin bog‘liq: 1,0 A da 20 mA, 0,9 A da 10 mA, 0,8 A da 5 mA — qizish toki 20 % kamayganda emissiya 4 marta kamaydi, bu Richardson–Deshman formulasidagi eksponensial bog‘lanishga mos keladi.</p>""",
 code="""import numpy as np
U  = np.array([5, 10, 20, 30, 40])                    # V (to'yinishdan uzoq soha)
Ia = np.array([0.22, 0.63, 1.79, 3.29, 5.06])*1e-3     # A
(k, lb), cov = np.polyfit(np.log10(U), np.log10(Ia), 1, cov=True)
print(f"Qiyalik = {k:.3f} ± {3.18*np.sqrt(cov[0, 0]):.3f} (nazariya 1,5);  b = {10**lb:.2e} A/V^1.5")
Iq = np.array([1.0, 0.9, 0.8]); Is = np.array([20.0, 10.0, 5.0])   # qizish toki, A; to'yinish toki, mA
print("To'yinish toklari nisbati:", Is/Is[0])""",
 questions=["Termoelektron emissiya nima va u nimaga bog‘liq?", "Nima uchun kichik kuchlanishlarda tok katod temperaturasiga bog‘liq emas?", "“3/2” qonunini qanday tekshirdingiz?", "To‘yinish toki nima uchun qizish tokiga keskin bog‘liq?", "Vakuum diod qayerda ishlatilgan va uni nima almashtirdi?"]
))

B.append(dict(
 n=24, sess=[24], lec=15, area="elektr", sim="bfield", tn=["TN2", "TN4"],
 title="Yer magnit maydoni kuchlanganligining gorizontal tashkil etuvchisini aniqlash",
 goal="Tangens-galvanometr yordamida Yer magnit maydoni induksiyasining gorizontal tashkil etuvchisini aniqlash.",
 equip=["Tangens-galvanometr (doiraviy g‘altak, markazida kompas, burchak shkalasi)", "O‘zgarmas tok manbai, reostat, kalit", "Ampermetr (0–1 A)", "Tok yo‘nalishini almashtirgich (kommutator)"],
 theory=r"""<p>Tangens-galvanometr g‘altagi tekisligi magnit meridiani bo‘ylab (kompas strelkasi g‘altak tekisligida) o‘rnatiladi. G‘altakdan \(I\) tok o‘tganda uning markazida meridianga perpendikulyar gorizontal maydon hosil bo‘ladi: \(B_\text{g‘}=\dfrac{\mu_0NI}{2R}\). Strelka natijaviy maydon bo‘ylab buriladi:</p>
$$\tan\varphi=\frac{B_\text{g‘}}{B_g}\quad\Longrightarrow\quad B_g=\frac{\mu_0NI}{2R\tan\varphi}$$
<p>Strelkaning ekssentrisiteti va g‘altak tekisligining meridiandan biroz og‘ishi xatoligini yo‘qotish uchun tok yo‘nalishi almashtirilib, \(\varphi_1\) va \(\varphi_2\) o‘rtachasi olinadi. Eng kichik nisbiy xatolik \(\varphi\approx45^\circ\) da: \(\frac{\Delta B}{B}=\frac{2\Delta\varphi}{\sin2\varphi}\). O‘zbekiston hududida \(B_g\approx25\)–28 mkT; yaqindagi temir buyumlar va tok o‘tkazgichlar o‘lchashni buzadi. Magnit maydon kuchlanganligi \(H_g=B_g/\mu_0\approx21\) A/m.</p>""",
 steps=["G‘altak radiusi R va o‘ramlar soni N ni yozing; asbobni temir buyumlardan uzoqroqqa qo‘ying.", "G‘altakni buring: kompas strelkasi g‘altak tekisligida bo‘lsin (shkala noli).", "Zanjirni yig‘ing va tokni bir necha qiymatga (0,10–0,30 A) qo‘ying.", "Har bir tokda strelka og‘ish burchagini yozing; tok yo‘nalishini almashtirib, yana yozing.", "Har bir o‘lchash uchun B_g ni hisoblang va o‘rtachasini toping.", "tg φ(I) grafigini quring va qiyalikdan B_g ni toping."],
 table=(["I, A", "φ₁, °", "φ₂ (tok teskari), °", "φ̄, °", "tg φ̄", "B_g, mkT"], [["0,10", "25,0", "26,0", "25,5", "0,477", "26,3"], ["0,15", "35,5", "36,5", "36,0", "0,727", "25,9"], ["0,20", "43,5", "44,5", "44,0", "0,966", "26,0"], ["0,25", "50,0", "51,0", "50,5", "1,213", "25,9"], ["0,30", "55,0", "56,0", "55,5", "1,455", "25,9"]]),
 calc=r"""<p>G‘altak: \(N=20\), \(R=10{,}0\) sm, \(\frac{\mu_0N}{2R}=1{,}257\cdot10^{-4}\) T/A. Masalan, \(I=0{,}20\) A: \(B_g=\frac{1{,}257\cdot10^{-4}\cdot0{,}20}{\tan44{,}0^\circ}=26{,}0\) mkT.</p>
<p>Besh o‘lchash o‘rtachasi \(\bar B_g=26{,}0\) mkT, tasodifiy xatolik 0,2 mkT; burchak (\(\pm0{,}5^\circ\)) va radius (\(\pm0{,}5\) mm) xatoliklari hissasi \(\approx0{,}4\) mkT. <b>Natija:</b> \(B_g=(26{,}0\pm0{,}5)\) mkT (\(H_g=20{,}7\) A/m). \(\tan\varphi(I)\) grafigi koordinata boshidan o‘tuvchi to‘g‘ri chiziq (qiyaligi 4,83 A⁻¹) — maydonlar superpozitsiyasi tasdiqlandi.</p>""",
 code="""import numpy as np
mu0, N, R = 4e-7*np.pi, 20, 0.100
I   = np.array([0.10, 0.15, 0.20, 0.25, 0.30])            # A
phi = np.array([[25.0, 26.0], [35.5, 36.5], [43.5, 44.5], [50.0, 51.0], [55.0, 56.0]]).mean(axis=1)
Bg = mu0*N*I/(2*R*np.tan(np.radians(phi)))
print("B_g, mkT:", np.round(Bg*1e6, 2), f"-> o'rtacha {Bg.mean()*1e6:.2f} mkT")
k = np.polyfit(I, np.tan(np.radians(phi)), 1)[0]
print(f"tg(phi)(I) qiyaligi = {k:.2f} 1/A -> B_g = {mu0*N/(2*R*k)*1e6:.2f} mkT")""",
 questions=["Tangens-galvanometr g‘altagi nima uchun magnit meridiani bo‘ylab o‘rnatiladi?", "Nima uchun tok yo‘nalishi almashtirilib, o‘rtacha burchak olinadi?", "Qaysi burchakda o‘lchash xatoligi minimal va nima uchun?", "Yaqindagi temir buyum natijaga qanday ta’sir qiladi?", "Yer magnit maydoni nima uchun muhim (kompas, magnitosfera)?"]
))

B.append(dict(
 n=25, sess=[25], lec=16, area="elektr", sim="induction", tn=["TN2", "TN4", "TN8"],
 title="Faradeyning elektromagnit induksiya qonunini o‘rganish",
 goal="G‘altakda induksiyalangan EYuK ning magnit oqimining o‘zgarish tezligiga, o‘ramlar soniga va magnit kuchiga bog‘liqligini tajribada o‘rganish; Lens qoidasini tekshirish.",
 equip=["Turli o‘ramlar soniga ega g‘altaklar (N = 300, 600, 1200)", "Doimiy magnitlar", "Galvanometr yoki kuchlanish datchigi (kompyuterga ulangan)", "Magnit tushadigan vertikal naycha (balandligi o‘zgartiriladi)", "Mis naycha (uyurmaviy toklarni kuzatish uchun)"],
 theory=r"""<p>Faradey qonuni: \(\mathcal E_i=-N\dfrac{d\Phi}{dt}\). Magnit g‘altakdan o‘tganda EYuK ikki qarama-qarshi ishorali impuls ko‘rinishida bo‘ladi (yaqinlashishda va uzoqlashishda). Bitta impuls yuzasi oqim o‘zgarishiga teng:</p>
$$\int\mathcal E\,dt=-N\Delta\Phi$$
<p>va u magnit tezligiga bog‘liq emas, maksimal EYuK esa tezlikka proporsional (\(\mathcal E_\text{max}\propto Nv\)). Magnit naychadan \(h\) balandlikdan tushirilsa, g‘altakka kirish tezligi \(v=\sqrt{2gh}\). Lens qoidasi: induksion tok magnit harakatiga qarshilik qiladi — galvanometr strelkasi yaqinlashish va uzoqlashishda qarama-qarshi tomonga og‘adi; mis naycha ichida magnit sekin tushadi (uyurmaviy toklar).</p>""",
 steps=["G‘altakni (N = 600) datchik yoki galvanometrga ulang.", "Magnitni qo‘lda g‘altakka kiriting va chiqaring: strelka og‘ish yo‘nalishlarini yozing (Lens qoidasi).", "Magnitni naychadan h = 10, 20, 40, 80 sm balandliklardan tushirib, ε(t) yozuvidan ε_max va impuls yuzasini aniqlang.", "ε_max ning v = √(2gh) ga bog‘liqligini grafikda tekshiring.", "N = 300 va 1200 g‘altaklar bilan, so‘ng ikkita magnit bilan tajribani takrorlang.", "Magnitni mis va plastmassa naychalardan tushirib, tushish vaqtini taqqoslang va izohlang."],
 table=(["h, sm", "v = √(2gh), m/s", "ε_max, V (N = 600)", "∫ε dt, mV·s", "ε_max/v, V·s/m"], [["10", "1,40", "0,218", "6,1", "0,156"], ["20", "1,98", "0,306", "6,0", "0,155"], ["40", "2,80", "0,433", "6,1", "0,155"], ["80", "3,96", "0,615", "6,2", "0,155"]]),
 calc=r"""<p>\(\mathcal E_\text{max}/v\) nisbati barcha balandliklarda deyarli bir xil (\(0{,}155\pm0{,}001\) V·s/m) — EYuK oqimning o‘zgarish tezligiga proporsional. Impuls yuzasi esa tezlikka bog‘liq emas: \(\int\mathcal E\,dt=(6{,}1\pm0{,}1)\) mV·s \(=N\Delta\Phi\) \(\Rightarrow\Delta\Phi=\frac{6{,}1\cdot10^{-3}}{600}=1{,}0\cdot10^{-5}\) Wb.</p>
<p>O‘ramlar soni bo‘yicha (\(h=40\) sm): \(N=300,\ 600,\ 1200\) da \(\mathcal E_\text{max}=0{,}218;\ 0{,}434;\ 0{,}866\) V — \(\mathcal E\propto N\). Ikkita magnit bilan \(\mathcal E_\text{max}\) 1,9 marta ortdi (oqim deyarli ikki baravar). Galvanometr strelkasi yaqinlashish va uzoqlashishda teskari og‘di — Lens qoidasi tasdiqlandi.</p>""",
 code="""import numpy as np
g, N = 9.81, 600
h    = np.array([0.10, 0.20, 0.40, 0.80])           # m
emax = np.array([0.218, 0.306, 0.433, 0.615])       # V
area = np.array([6.1, 6.0, 6.1, 6.2])*1e-3          # V·s
v = np.sqrt(2*g*h)
k = np.polyfit(v, emax, 1)
print("emax/v:", np.round(emax/v, 4), "  chiziqli moslash:", np.round(k, 4))
print(f"Delta Phi = {area.mean()/N:.2e} Wb (tezlikka bog'liq emas)")""",
 questions=["Faradey qonunini ta’riflang va undagi minus ishorasining ma’nosini tushuntiring.", "Nima uchun impuls yuzasi magnit tezligiga bog‘liq emas?", "Lens qoidasini tajribada qanday tekshirdingiz?", "Magnit mis naychada nima uchun sekin tushadi?", "Elektr generatorlari va transformatorlar qaysi hodisaga asoslangan?"]
))

B.append(dict(
 n=26, sess=[26], lec=22, area="optika", sim="snell", tn=["TN2", "TN9"],
 title="Ignalar yordamida shishaning sindirish ko‘rsatkichini aniqlash",
 goal="Yassi-parallel shisha plastinka orqali o‘tgan nur yo‘lini ignalar yordamida qurib, shishaning sindirish ko‘rsatkichini Snellius qonuni bo‘yicha aniqlash va nurning parallel siljishini o‘lchash.",
 equip=["Yassi-parallel shisha plastinka", "Ignalar (4 dona), kartonli taxta", "Oq qog‘oz varag‘i, chizg‘ich, transportir, sirkul", "Qalam"],
 theory=r"""<p>Ignalar yordamida nur yo‘li quriladi: plastinkaning bir tomoniga ikki igna (A, B) sanchiladi, ikkinchi tomondan qarab, ular bilan bir to‘g‘ri chiziqda ko‘rinadigan qilib yana ikki igna (C, D) sanchiladi. AB — tushgan nur, CD — chiqqan nur; ularni plastinka chegaralari bilan kesishish nuqtalari tutashtirilsa, singan nur hosil bo‘ladi. Snellius qonuni:</p>
$$n=\frac{\sin\alpha}{\sin\beta}$$
<p>Burchaklarni transportirsiz aniqlash uchun kirish nuqtasi markaz bo‘lgan radiusi \(r\) li aylana chiziladi va nurlarning normaldan masofalari \(a=r\sin\alpha\), \(b=r\sin\beta\) o‘lchanadi: \(n=a/b\). Chiqqan nur tushgan nurga parallel, ammo \(\delta=\dfrac{d\sin(\alpha-\beta)}{\cos\beta}\) masofaga siljigan (\(d\) — plastinka qalinligi). Oddiy (kron) shisha uchun \(n\approx1{,}50\)–1,52, flint shisha uchun 1,6–1,7.</p>""",
 steps=["Qog‘ozni taxtaga mahkamlang, plastinkani qo‘yib, uning chegaralarini qalam bilan chizing.", "Bir tomonga ikki ignani (A, B) qiya chiziq bo‘ylab sanching.", "Ikkinchi tomondan qarab, C va D ignalarni A va B tasvirlari bilan bir chiziqda ko‘rinadigan qilib sanching.", "Plastinkani olib, nur yo‘lini chizing: tushgan, singan va chiqqan nurlar; kirish nuqtasida normal o‘tkazing.", "α va β ni transportir bilan, a va b ni aylana usulida o‘lchang; n ni hisoblang.", "Tajribani 4 xil tushish burchagida takrorlang; nurning siljishi δ ni o‘lchab, formula bilan solishtiring."],
 table=(["α, °", "β, °", "sin α", "sin β", "n = sin α / sin β"], [["30,0", "19,5", "0,500", "0,334", "1,498"], ["40,0", "25,0", "0,643", "0,423", "1,521"], ["50,0", "30,5", "0,766", "0,508", "1,509"], ["60,0", "35,0", "0,866", "0,574", "1,510"]]),
 calc=r"""<p>To‘rt burchakda olingan natijalar o‘rtachasi \(\bar n=1{,}509\); tasodifiy xatolik (\(n=4\), \(t=3{,}18\)) 0,015; burchak o‘lchash xatoligi (\(\pm0{,}5^\circ\)) hissasi \(\Delta n=n\sqrt{(\cot\alpha\,\Delta\alpha)^2+(\cot\beta\,\Delta\beta)^2}\approx0{,}025\). <b>Natija:</b> \(n=1{,}51\pm0{,}03\) — kron shisha. Aylana usulida (\(r=50\) mm, \(\alpha=50^\circ\)): \(a=38{,}3\) mm, \(b=25{,}4\) mm, \(n=a/b=1{,}508\).</p>
<p>Nurning siljishi (\(d=10{,}0\) mm, \(\alpha=50^\circ\)): hisob \(\delta=\frac{d\sin(\alpha-\beta)}{\cos\beta}=3{,}9\) mm, o‘lchangan 3,9 mm.</p>""",
 code="""import numpy as np
alfa = np.radians([30.0, 40.0, 50.0, 60.0])
beta = np.radians([19.5, 25.0, 30.5, 35.0])
n = np.sin(alfa)/np.sin(beta)
dA = np.radians(0.5)
dnB = n*np.hypot(dA/np.tan(alfa), dA/np.tan(beta))        # burchak xatoligi hissasi
dn = np.hypot(3.18*n.std(ddof=1)/np.sqrt(len(n)), dnB.mean())
print("n:", np.round(n, 3), f"-> n = {n.mean():.3f} ± {dn:.3f}")
d, a, b = 10.0, np.radians(50), np.radians(30.5)
print(f"Siljish: {d*np.sin(a - b)/np.cos(b):.2f} mm")""",
 questions=["Snellius qonunini ta’riflang.", "Nima uchun yassi-parallel plastinkadan chiqqan nur tushgan nurga parallel?", "Aylana usulining afzalligi nimada?", "Tushish burchagi ortganda nurning siljishi qanday o‘zgaradi?", "Refraktometr yordamida suyuqlik konsentratsiyasini qanday aniqlash mumkin?"]
))

B.append(dict(
 n=27, sess=[27], lec=22, area="optika", sim="lens", tn=["TN2", "TN9"],
 title="Mikroskopning ishlash prinsipini o‘rganish va uning kattalashtirishini aniqlash",
 goal="Mikroskopning optik sxemasi va ishlash prinsipini o‘rganish; obyektiv va okulyar kombinatsiyalari uchun kattalashtirishni obyekt-mikrometr yordamida aniqlash; okulyar-mikrometr bo‘lim qiymatini kalibrlash.",
 equip=["Biologik mikroskop (obyektivlar 8×, 40×; okulyarlar 7×, 10×, 15×)", "Obyekt-mikrometr (1 mm 100 bo‘limga bo‘lingan)", "Okulyar-mikrometr (shkalali okulyar)", "Millimetrli qog‘oz (25 sm masofada proyeksiya uchun)", "Yoritgich"],
 theory=r"""<p>Mikroskop ikki yig‘uvchi optik sistemadan iborat. <b>Obyektiv</b> (fokus masofasi \(F_\text{ob}\) kichik) buyumning haqiqiy, teskari, kattalashgan tasvirini okulyar fokal tekisligi yaqinida hosil qiladi; <b>okulyar</b> bu tasvirni lupa kabi qo‘shimcha kattalashtiradi va mavhum tasvir eng yaxshi ko‘rish masofasida (\(D=25\) sm) hosil bo‘ladi. Umumiy kattalashtirish:</p>
$$\Gamma=\Gamma_\text{ob}\cdot\Gamma_\text{ok}\approx\frac{\delta}{F_\text{ob}}\cdot\frac{D}{F_\text{ok}}$$
<p>bu yerda \(\delta\) — tubusning optik uzunligi (\(\approx16\) sm). Kattalashtirishni tajribada aniqlash: obyekt-mikrometrning \(l\) uzunlikdagi qismi bir ko‘z bilan mikroskopda, ikkinchi ko‘z bilan 25 sm masofadagi millimetrli qog‘ozda ustma-ust ko‘rilib, uning tasviri uzunligi \(L\) o‘lchanadi: \(\Gamma=L/l\). Mikroskopning ajrata olish chegarasi difraksiya bilan cheklangan: \(d_\text{min}\approx\frac{0{,}61\lambda}{n\sin u}\) (\(\approx0{,}2\) mkm) — shuning uchun foydali kattalashtirish \(\sim1000\)–1500 dan oshmaydi.</p>""",
 steps=["Mikroskop qismlarini o‘rganing: obyektiv, okulyar, tubus, mikro- va makrovint, yoritgich, diafragma.", "Obyekt-mikrometrni stolchaga qo‘yib, 8× obyektiv bilan tiniq tasvir hosil qiling.", "Millimetrli qog‘ozni mikroskop yoniga ko‘zdan 25 sm masofaga qo‘ying; bir ko‘z bilan mikroskopga, ikkinchisi bilan qog‘ozga qarab, shkala tasvirini qog‘ozda belgilang.", "Obyekt-mikrometrning l uzunlikdagi qismi tasviri L ni o‘lchab, Γ = L/l ni hisoblang.", "Barcha obyektiv–okulyar juftlari uchun takrorlang va Γ_ob·Γ_ok bilan solishtiring.", "Okulyar-mikrometr bo‘lim qiymatini obyekt-mikrometr yordamida kalibrlang va kichik obyekt (soch tolasi, kristall) o‘lchamini aniqlang."],
 table=(["Obyektiv × okulyar", "Nominal Γ", "l, mm", "L, mm", "Γ = L/l"], [["8× × 7×", "56", "1,00", "55", "55"], ["8× × 10×", "80", "0,50", "40", "80"], ["8× × 15×", "120", "0,30", "35,5", "118"], ["40× × 10×", "400", "0,10", "39", "390"], ["40× × 15×", "600", "0,05", "29,5", "590"]]),
 calc=r"""<p>O‘lchangan kattalashtirishlar nominal qiymatlardan 2,5 % dan kam farq qiladi. Masalan, 40× × 10×: obyekt-mikrometrning 0,10 mm qismi tasviri 39 mm, \(\Gamma=390\) (nominal 400). Xatolik asosan tasvir uzunligini qog‘ozda belgilash aniqligi (\(\pm1\) mm) bilan aniqlanadi: \(\varepsilon\approx2{,}5\,\%\).</p>
<p><b>Okulyar-mikrometrni kalibrlash</b> (40× obyektiv): okulyar shkalasining 50 bo‘limi obyekt-mikrometrning 0,12 mm iga teng \(\Rightarrow\) bo‘lim qiymati 2,4 mkm. Soch tolasi 28 bo‘limni egalladi: diametri \(\approx67\) mkm.</p>
<p>Tubus optik uzunligi \(\delta=16\) sm deb olinsa, 40× obyektivning fokus masofasi \(F_\text{ob}\approx\delta/\Gamma_\text{ob}=4\) mm.</p>""",
 code="""import numpy as np
juftlar = [("8x7", 56, 1.00, 55.0), ("8x10", 80, 0.50, 40.0), ("8x15", 120, 0.30, 35.5),
           ("40x10", 400, 0.10, 39.0), ("40x15", 600, 0.05, 29.5)]
for nom, G0, l, L in juftlar:
    G = L/l
    print(f"{nom:6s}: Gamma = {G:6.0f} (nominal {G0}), farq {100*(G - G0)/G0:+.1f} %, xatolik ±{G*1.0/L:.0f}")
qiymat = 0.12/50                    # mm, okulyar-mikrometr bo'lim qiymati
print(f"Bo'lim qiymati = {qiymat*1e3:.1f} mkm, soch diametri = {28*qiymat*1e3:.0f} mkm")""",
 questions=["Mikroskopda obyektiv va okulyar qanday tasvir hosil qiladi?", "Umumiy kattalashtirish formulasini keltirib chiqaring.", "Nima uchun mikroskopning foydali kattalashtirishi chegaralangan?", "Immersion moy qanday maqsadda ishlatiladi?", "Okulyar-mikrometr nima uchun har bir obyektiv uchun alohida kalibrlanadi?"]
))

B.append(dict(
 n=28, sess=[28], lec=22, area="optika", sim="snell", tn=["TN2", "TN9"],
 title="Mikroskop yordamida shishaning sindirish ko‘rsatkichini aniqlash",
 goal="Shisha plastinkaning haqiqiy qalinligini mikrometr bilan, ko‘rinma qalinligini mikroskop mikrovinti bilan o‘lchab, sindirish ko‘rsatkichini aniqlash (ko‘rinma chuqurlik usuli).",
 equip=["Mikroskop (mikrovint barabani 0,002 mm bo‘limli yoki indikatorli)", "Ikki sirtiga belgi tushirilgan shisha plastinkalar", "Mikrometr", "Yoritgich"],
 theory=r"""<p>Plastinka ostidagi nuqta yuqoridan qaralganda ko‘tarilgandek — haqiqiy qalinlik \(d\) dan kichik \(h\) chuqurlikda ko‘rinadi. Normal yaqinidagi (paraksial) nurlar uchun Snellius qonunidan (\(\sin\alpha\approx\tan\alpha\)):</p>
$$n=\frac dh$$
<p>Mikroskop avval plastinkaning ostki sirtidagi belgiga (plastinka orqali), so‘ng ustki sirtdagi belgiga fokuslanadi; tubusning siljishi mikrovint bo‘yicha o‘lchanadi va u ko‘rinma qalinlik \(h\) ga teng. Mikroskopning maydon chuqurligi kichik (katta obyektivda bir necha mkm) bo‘lgani uchun fokuslash aniq bajariladi. Fokuslashni har doim bir tomondan (masalan, pastdan yuqoriga) bajarish vint lyufti xatoligini kamaytiradi.</p>""",
 steps=["Plastinka qalinligi d ni mikrometr bilan 5 joyda o‘lchang.", "Plastinkani mikroskop stolchasiga qo‘ying; ostki sirtdagi belgini mikrovint bilan aniq fokuslang va baraban ko‘rsatishini yozing.", "Ustki sirtdagi belgiga fokuslang va ko‘rsatishni yozing; ayirma — ko‘rinma qalinlik h.", "O‘lchashni 5 marta takrorlang (har safar fokusni buzib, qayta topib).", "n = d/h ni va xatolikni hisoblang.", "Boshqa plastinka uchun takrorlang; natijani 26-laboratoriya ishi bilan solishtiring."],
 table=(["№", "d, mm", "Ostki belgi, mm", "Ustki belgi, mm", "h, mm"], [["1", "3,02", "0,412", "2,410", "1,998"], ["2", "3,02", "0,405", "2,409", "2,004"], ["3", "3,01", "0,418", "2,413", "1,995"], ["4", "3,02", "0,401", "2,407", "2,006"], ["5", "3,03", "0,410", "2,410", "2,000"], ["O‘rtacha", "3,020", "", "", "2,001"]]),
 calc=r"""<p>\(\bar d=3{,}020\pm0{,}010\) mm (\(\varepsilon_d=0{,}33\,\%\)), \(\bar h=2{,}001\pm0{,}006\) mm (\(\varepsilon_h=0{,}30\,\%\)).</p>
$$n=\frac{\bar d}{\bar h}=\frac{3{,}020}{2{,}001}=1{,}509,\qquad \varepsilon_n=\sqrt{\varepsilon_d^2+\varepsilon_h^2}=0{,}45\,\%$$
<p><b>Natija:</b> \(n=1{,}509\pm0{,}007\). 26-laboratoriya ishidagi ignalar usuli natijasi (\(1{,}51\pm0{,}03\)) bilan mos, ammo mikroskop usuli taxminan 4 marta aniqroq.</p>""",
 code="""import numpy as np
d = np.array([3.02, 3.02, 3.01, 3.02, 3.03])                        # mm, mikrometr
past = np.array([0.412, 0.405, 0.418, 0.401, 0.410])                # mm, ostki belgi
yuqori = np.array([2.410, 2.409, 2.413, 2.407, 2.410])              # mm, ustki belgi
h = yuqori - past
def xato(x, asbob):
    return np.hypot(2.78*x.std(ddof=1)/np.sqrt(len(x)), asbob)
n = d.mean()/h.mean()
eps = np.hypot(xato(d, 0.005)/d.mean(), xato(h, 0.002)/h.mean())
print(f"d = {d.mean():.3f} mm, h = {h.mean():.4f} mm, n = {n:.3f} ± {n*eps:.3f}")""",
 questions=["Nima uchun plastinka ostidagi nuqta ko‘tarilgandek ko‘rinadi?", "n = d/h formulasi qanday yaqinlashuvda o‘rinli?", "Mikroskopning maydon chuqurligi o‘lchash aniqligiga qanday ta’sir qiladi?", "Vint lyufti xatoligini qanday kamaytirish mumkin?", "Ushbu usulni suyuqlik sindirish ko‘rsatkichini o‘lchashga qanday moslash mumkin?"]
))

B.append(dict(
 n=29, sess=[29], lec=22, area="optika", sim="lens", tn=["TN2", "TN6", "TN9"],
 title="Qavariq va botiq linzalarning bosh fokus masofasini aniqlash",
 goal="Yig‘uvchi linzaning fokus masofasini linza formulasi, Bessel (ko‘chirish) usuli va grafik usulda; sochuvchi linzaning fokus masofasini yig‘uvchi linza bilan kombinatsiya usulida aniqlash.",
 equip=["Optik skam’ya (shkalali)", "Yorug‘lik manbai va buyum (strelkali diafragma)", "Yig‘uvchi va sochuvchi linzalar", "Ekran", "Chizg‘ich"],
 theory=r"""<p><b>1) Linza formulasi usuli:</b> buyum va ekranni siljitib, tiniq tasvir hosil qilinadi va masofalar o‘lchanadi: \(F=\dfrac{dd'}{d+d'}\). <b>2) Bessel usuli:</b> buyum va ekran orasidagi masofa \(L>4F\) o‘zgarmas qilib qo‘yiladi; linzaning tiniq tasvir beradigan ikki holati orasidagi masofa \(l\) o‘lchanadi:</p>
$$F=\frac{L^2-l^2}{4L}$$
<p>Bu usulda linza optik markazining aniq joyini bilish shart emas (qalin linzalar uchun qulay). <b>3) Grafik usul:</b> \(1/d'\) ning \(1/d\) ga bog‘liqligi qiyaligi \(-1\) bo‘lgan to‘g‘ri chiziq, ozod hadi \(1/F\). <b>Sochuvchi linza</b> haqiqiy tasvir bermaydi, shuning uchun u kuchliroq yig‘uvchi linza bilan jips qo‘yiladi; sistemaning optik kuchi \(D=D_1+D_2\), bundan \(\dfrac{1}{F_2}=\dfrac{1}{F_\text{sist}}-\dfrac{1}{F_1}\) (\(F_2<0\)).</p>""",
 steps=["Optik skam’yada manba, buyum, linza va ekranni bir o‘qqa (balandlikda) joylashtiring.", "Linzani siljitib, ekranda tiniq tasvir hosil qiling; d va d′ ni o‘lchang. Buyum masofasini 5 marta o‘zgartirib takrorlang.", "Har bir o‘lchash uchun F ni hisoblang, o‘rtacha va xatolikni toping; 1/d′(1/d) grafigini quring.", "Bessel usuli: buyum–ekran masofasini L = 80 sm qilib, linzaning ikki holati orasidagi masofa l ni 3 marta o‘lchang.", "Sochuvchi linzani yig‘uvchi linza bilan jips qo‘yib, sistemaning fokus masofasini linza formulasi bilan aniqlang.", "Sochuvchi linza fokus masofasi va optik kuchini hisoblang."],
 table=(["d, sm", "d′, sm", "F = dd′/(d + d′), sm", "1/d, sm⁻¹", "1/d′, sm⁻¹"], [["20,0", "59,6", "14,97", "0,0500", "0,0168"], ["25,0", "37,6", "15,02", "0,0400", "0,0266"], ["30,0", "30,1", "15,02", "0,0333", "0,0332"], ["40,0", "24,0", "15,00", "0,0250", "0,0417"], ["50,0", "21,4", "14,99", "0,0200", "0,0467"]]),
 calc=r"""<p><b>1) Linza formulasi:</b> besh o‘lchash o‘rtachasi \(\bar F=15{,}00\) sm; tasodifiy xatolik 0,03 sm; masofalarni o‘lchash va tasvir tiniqligini baholash xatoligi hissasi \(\approx0{,}1\) sm. \(F_1=(15{,}0\pm0{,}1)\) sm, \(D_1=6{,}67\) dptr. Grafik usulda \(1/d'(1/d)\) to‘g‘ri chizig‘i qiyaligi \(-1{,}00\), ozod had \(1/F=0{,}0667\) sm⁻¹.</p>
<p><b>2) Bessel usuli:</b> \(L=80{,}0\) sm, \(l=40{,}0\) sm: \(F=\frac{L^2-l^2}{4L}=\frac{6400-1600}{320}=15{,}0\) sm — mos keladi.</p>
<p><b>3) Sochuvchi linza:</b> sistema uchun \(d=60{,}0\) sm, \(d'=99{,}5\) sm, \(F_\text{sist}=37{,}4\) sm. \(\frac{1}{F_2}=\frac{1}{37{,}4}-\frac{1}{15{,}0}\Rightarrow F_2=-25{,}0\) sm, \(D_2=-4{,}0\) dptr.</p>""",
 code="""import numpy as np
d  = np.array([20.0, 25.0, 30.0, 40.0, 50.0])     # sm
dp = np.array([59.6, 37.6, 30.1, 24.0, 21.4])
F = d*dp/(d + dp)
print("F:", np.round(F, 2), f"-> {F.mean():.2f} ± {2.78*F.std(ddof=1)/np.sqrt(5):.2f} sm")
k, b = np.polyfit(1/d, 1/dp, 1)
print(f"Grafik usul: qiyalik {k:.3f}, F = {1/b:.2f} sm")
L, l = 80.0, np.mean([39.9, 40.1, 40.0])
print(f"Bessel: F = {(L**2 - l**2)/(4*L):.2f} sm")
Fs = 60.0*99.5/(60.0 + 99.5); F2 = 1/(1/Fs - 1/F.mean())
print(f"Sochuvchi linza: F2 = {F2:.1f} sm, D2 = {100/F2:.2f} dptr")""",
 questions=["Yupqa linza formulasini yozing va ishoralar qoidasini tushuntiring.", "Bessel usulining afzalligi nimada? Nima uchun L > 4F bo‘lishi kerak?", "Sochuvchi linza fokus masofasini nima uchun bevosita o‘lchab bo‘lmaydi?", "Jips qo‘yilgan linzalar sistemasining optik kuchi qanday topiladi?", "Ko‘zoynak linzalarining optik kuchi qanday aniqlanadi?"]
))

B.append(dict(
 n=30, sess=[30], lec=20, area="optika", sim="grating", tn=["TN2", "TN9"],
 title="Difraksion panjara yordamida yorug‘lik to‘lqin uzunligini aniqlash",
 goal="Difraksion panjara yordamida lazer nurining va simob lampasi spektral chiziqlarining to‘lqin uzunliklarini aniqlash.",
 equip=["Difraksion panjara (300 shtrix/mm)", "Yarimo‘tkazgichli lazer (nominal λ = 650 nm)", "Simob lampasi va tirqish", "Ekran, o‘lchov tasmasi (yoki goniometr)", "Optik skam’ya"],
 theory=r"""<p>Panjara davri \(d=1/N_0\) (\(N_0\) — 1 mm dagi shtrixlar soni). Bosh maksimumlar sharti \(d\sin\varphi=k\lambda\). Ekran panjaradan \(L\) masofada bo‘lsa va \(k\)-tartib maksimum markazdan \(x_k\) masofada kuzatilsa, \(\tan\varphi=x_k/L\):</p>
$$\lambda=\frac{d\sin\varphi}{k}=\frac{d}{k}\,\frac{x_k}{\sqrt{x_k^2+L^2}}$$
<p>Kichik burchaklarda \(\lambda\approx dx_k/(kL)\), ammo katta burchaklarda aniq formula ishlatiladi. Aniqlik uchun chap va o‘ng maksimumlar orasidagi masofa \(2x_k\) o‘lchanadi. Oq yorug‘lik spektrga ajraladi: binafsha chiziq markazga yaqin, qizil uzoqroq. Agar panjara davri noma’lum bo‘lsa, u ma’lum to‘lqin uzunligi (masalan, simobning yashil chizig‘i 546,1 nm) bo‘yicha kalibrlanadi. Panjaraning ajrata olish qobiliyati \(R=kN\).</p>""",
 steps=["Lazer, panjara va ekranni optik skam’yaga joylashtiring; panjara nurga perpendikulyar bo‘lsin. Lazer nurini ko‘zga yo‘naltirmang!", "Ekrangacha masofa L ni o‘lchang.", "1- va 2-tartib maksimumlar orasidagi masofalar 2x₁ va 2x₂ ni o‘lchang.", "L ni 0,5; 0,8; 1,0 m ga o‘zgartirib takrorlang; λ ni har biri uchun aniq formula bilan hisoblang.", "Simob lampasi va tirqish bilan spektrni kuzating; sariq, yashil va binafsha chiziqlar o‘rnini o‘lchab, to‘lqin uzunliklarini toping.", "Natijalarni jadval qiymatlari bilan solishtiring va xatolikni baholang."],
 table=(["L, m", "2x₁, mm", "2x₂, mm", "λ (k = 1), nm", "λ (k = 2), nm"], [["0,500", "199", "425", "650,6", "651,9"], ["0,800", "319", "680", "651,8", "651,9"], ["1,000", "399", "850", "652,2", "651,9"]]),
 calc=r"""<p>Panjara: 300 shtrix/mm, \(d=3{,}333\) mkm. Masalan, \(L=0{,}800\) m, \(k=1\): \(x_1=159{,}5\) mm, \(\sin\varphi=\frac{159{,}5}{\sqrt{159{,}5^2+800^2}}=0{,}1955\), \(\lambda=d\sin\varphi=651{,}8\) nm.</p>
<p>Olti qiymat o‘rtachasi 651,7 nm, tasodifiy xatolik 0,6 nm; panjara davri noaniqligi (\(\pm0{,}3\,\%\)) hissasi \(\approx2\) nm. <b>Natija:</b> \(\lambda_\text{lazer}=(652\pm2)\) nm (nominal 650 ± 5 nm).</p>
<p>Simob lampasi (\(L=0{,}500\) m, 1-tartib): sariq chiziq \(x=88{,}0\) mm \(\Rightarrow\lambda=578\) nm (jadval: 577,0 va 579,1 nm dubleti), yashil 545,9 nm (546,1 nm), binafsha 436,2 nm (435,8 nm).</p>""",
 code="""import numpy as np
d = 1e-3/300                                        # m
L  = np.array([0.500, 0.800, 1.000])                # m
x1 = np.array([199, 319, 399])/2*1e-3               # m
x2 = np.array([425, 680, 850])/2*1e-3
lam = lambda x, L, k: d/k*x/np.hypot(x, L)
l_all = np.concatenate([lam(x1, L, 1), lam(x2, L, 2)])*1e9
dl = np.hypot(2.57*l_all.std(ddof=1)/np.sqrt(len(l_all)), 0.003*l_all.mean())
print("lambda, nm:", np.round(l_all, 1), f"-> {l_all.mean():.1f} ± {dl:.1f} nm")
for nom, x in [("sariq", 88.0), ("yashil", 83.0), ("binafsha", 66.0)]:
    print(f"Simob {nom}: {lam(x*1e-3, 0.5, 1)*1e9:.1f} nm")""",
 questions=["Difraksion panjara formulasini keltirib chiqaring.", "Nima uchun chap va o‘ng maksimumlar orasidagi masofa o‘lchanadi?", "Kichik burchak yaqinlashuvi qachon katta xatolik beradi?", "Panjarada nima uchun qizil nur ko‘proq og‘adi, prizmada esa aksincha?", "Spektral tahlilda difraksion panjaraning prizmadan afzalligi nimada?"]
))

B.append(dict(
 n=31, sess=[31, 32], lec=23, area="kvant", sim="photo", tn=["TN2", "TN3", "TN5", "TN9"],
 title="Tashqi fotoeffekt hodisasini o‘rganish",
 goal="Vakuumli fotoelement yordamida tashqi fotoeffekt qonunlarini o‘rganish: 1-mashg‘ulotda fotoelement VAX ini turli yorug‘lik oqimlarida qurish va Stoletov qonunini tekshirish; 2-mashg‘ulotda yorug‘lik filtrlari bilan tormozlovchi kuchlanishning chastotaga bog‘liqligidan Plank doimiysi va chiqish ishini aniqlash.",
 equip=["Vakuumli fotoelement (surma-seziy katodli)", "Yorug‘lik manbai (simob yoki cho‘g‘lanma lampa) va yorug‘lik filtrlari (ma’lum λ)", "Rostlanadigan va qutbi almashtiriladigan kuchlanish manbai (−3…+60 V)", "Nanoampermetr yoki mikroampermetr, voltmetr", "Optik skam’ya (manba–fotoelement masofasini o‘zgartirish uchun)"],
 theory=r"""<p>Yorug‘lik ta’sirida katoddan chiqqan fotoelektronlar anod kuchlanishi musbat bo‘lganda anodga yig‘iladi. Kuchlanish ortishi bilan fototok to‘yinadi: to‘yinish toki \(I_\text{to‘y}\) vaqt birligida chiqqan barcha elektronlarga mos va <b>yorug‘lik oqimiga proporsional</b> (Stoletov qonuni). Nuqtaviy manbadan \(r\) masofada oqim \(\Phi\propto1/r^2\), shuning uchun \(I_\text{to‘y}\propto1/r^2\). Teskari (tormozlovchi) kuchlanish \(U_z\) da hatto eng tez elektronlar ham anodga yetmaydi va tok nolga tushadi:</p>
$$eU_z=h\nu-A\quad\Longrightarrow\quad U_z=\frac he\,\nu-\frac Ae$$
<p>Demak, \(U_z(\nu)\) grafigi to‘g‘ri chiziq: qiyaligi \(h/e\), \(U_z=0\) dagi chastota — qizil chegara \(\nu_0=A/h\). Tormozlovchi kuchlanish yorug‘lik intensivligiga bog‘liq emas. Amalda o‘lchangan \(U_z\) ga katod va anod orasidagi kontakt potensiallar farqi qo‘shiladi; u faqat ozod hadni siljitadi, shuning uchun \(h\) qiyalikdan aniq topiladi.</p>""",
 steps=["1-mashg‘ulot. Fotoelementni manbadan r = 20 sm masofaga qo‘ying; anod kuchlanishini −2 V dan +60 V gacha o‘zgartirib, VAX ni yozing.", "Masofani 25, 30, 40 sm ga o‘zgartirib, VAX ni takrorlang.", "To‘yinish toklarini 1/r² ga qarshi grafikda tasvirlab, Stoletov qonunini tekshiring.", "2-mashg‘ulot. Filtrlarni navbatma-navbat qo‘yib (λ = 405, 436, 492, 546, 577 nm), har biri uchun tok nolga tushadigan tormozlovchi kuchlanish U_z ni aniqlang.", "Bitta filtr uchun yorug‘lik oqimini o‘zgartirib, U_z intensivlikka bog‘liq emasligini tekshiring.", "U_z(ν) grafigini quring, eng kichik kvadratlar usulida h/e va A ni toping.", "h ni CODATA qiymati (6,626·10⁻³⁴ J·s) bilan solishtiring, xatolik manbalarini tahlil qiling va hisobotni himoya qiling."],
 table=(["λ, nm (filtr)", "ν, 10¹⁴ Hz", "U_z, V"], [["405", "7,40", "1,10"], ["436", "6,88", "0,90"], ["492", "6,09", "0,56"], ["546", "5,49", "0,33"], ["577", "5,20", "0,19"]]),
 calc=r"""<p><b>1-mashg‘ulot.</b> To‘yinish toklari: \(r=20;\ 25;\ 30;\ 40\) sm da \(I_\text{to‘y}=1{,}80;\ 1{,}16;\ 0{,}80;\ 0{,}45\) mkA. \(I_\text{to‘y}r^2=\text{const}\) (\(720\pm5\) mkA·sm²) — fototok yorug‘lik oqimiga proporsional (Stoletov qonuni). Tormozlovchi kuchlanish masofaga bog‘liq bo‘lmadi.</p>
<p><b>2-mashg‘ulot.</b> \(U_z(\nu)\) nuqtalariga to‘g‘ri chiziq: qiyalik \(h/e=(4{,}12\pm0{,}19)\cdot10^{-15}\) V·s, ozod had \(-1{,}94\) V.</p>
$$h=e\cdot\frac{dU_z}{d\nu}=1{,}602\cdot10^{-19}\cdot4{,}12\cdot10^{-15}=(6{,}60\pm0{,}31)\cdot10^{-34}\ \text{J·s}$$
<p>CODATA qiymati \(6{,}626\cdot10^{-34}\) J·s xatolik chegarasida. Chiqish ishi (kontakt potensiallar farqi bilan birga) \(A\approx1{,}94\) eV, qizil chegara \(\lambda_0\approx636\) nm.</p>""",
 code="""import numpy as np
e, c = 1.602177e-19, 2.998e8
lam = np.array([405, 436, 492, 546, 577])*1e-9      # m
Uz  = np.array([1.10, 0.90, 0.56, 0.33, 0.19])      # V
nu = c/lam
(k, b), cov = np.polyfit(nu, Uz, 1, cov=True)
h, dh = e*k, e*3.18*np.sqrt(cov[0, 0])
print(f"h = ({h*1e34:.2f} ± {dh*1e34:.2f})·10^-34 J·s  (CODATA 6,626)")
print(f"A = {-b:.2f} eV, qizil chegara = {c/(-b/k)*1e9:.0f} nm")
r = np.array([20, 25, 30, 40]); Is = np.array([1.80, 1.16, 0.80, 0.45])
print("Stoletov: I*r^2 =", np.round(Is*r**2, 1), "mkA·sm²")""",
 questions=["Tashqi fotoeffektning uchta qonunini ayting.", "Nima uchun to‘yinish toki yorug‘lik oqimiga proporsional?", "Tormozlovchi kuchlanish nima uchun intensivlikka bog‘liq emas?", "U_z(ν) grafigidan Plank doimiysi va chiqish ishi qanday topiladi?", "Kontakt potensiallar farqi natijaga qanday ta’sir qiladi va nima uchun h ga ta’sir qilmaydi?"]
))

B.append(dict(
 n=33, sess=[33], lec=25, area="kvant", sim=["bohr", "franck"], tn=["TN5", "TN10"],
 title="Atomlar spektrlari bo‘yicha kompyuter tajribasi. Frank–Gers tajribasini o‘rganish",
 goal="Kompyuter modeli yordamida vodorod atomi spektral seriyalarini tadqiq qilib, Ridberg doimiysini aniqlash; Frank–Gers tajribasi modelida simob atomining birinchi qo‘zg‘alish energiyasini topish va atom energetik sathlarining diskretligini tasdiqlash.",
 equip=["Kompyuter (darslikdagi Bor va Frank–Gers modellari)", "PhET “Models of the Hydrogen Atom” simulyatori (qo‘shimcha)", "Python (Colab) — natijalarni qayta ishlash uchun", "Mavjud bo‘lsa: vodorod spektral trubkasi va spektroskop (taqqoslash uchun)"],
 theory=r"""<p><b>Vodorod spektri.</b> Bor nazariyasiga ko‘ra elektron \(n_{yu}\) sathdan \(n_q\) sathga o‘tganda chiqarilgan nurlanish to‘lqin uzunligi Ridberg formulasiga bo‘ysunadi: \(1/\lambda=R(1/n_q^2-1/n_{yu}^2)\). Balmer seriyasi chiziqlari uchun \(1/\lambda\) ning \(1/n_{yu}^2\) ga bog‘liqligi qiyaligi \(-R\) bo‘lgan to‘g‘ri chiziq; uning ozod hadi \(R/4\) seriya chegarasiga (365 nm) mos keladi.</p>
<p><b>Frank–Gers tajribasi.</b> Simob bug‘i to‘ldirilgan trubkada katoddan chiqqan elektronlar to‘r bilan tezlatiladi, anod oldida kichik tormozlovchi kuchlanish \(U_t\) qo‘yiladi. Elektron energiyasi simob atomining birinchi qo‘zg‘alish energiyasi \(E_1\) dan kichik bo‘lsa, to‘qnashuvlar elastik va anod toki ortadi; \(eU\) qiymati \(E_1\) ga yetganda elektronlar atomlarni qo‘zg‘atib, energiyasini yo‘qotadi va anodga yetolmaydi — tok keskin kamayadi. Bu jarayon har \(\Delta U=E_1/e\) da takrorlanadi:</p>
$$E_1=e\,\Delta U\approx4{,}9\ \text{eV},\qquad \lambda=\frac{hc}{E_1}\approx254\ \text{nm}$$
<p>Qo‘zg‘algan atomlar aynan shu ultrabinafsha nurni chiqaradi — bu Bor postulatlarining bevosita tasdig‘i (Nobel mukofoti, 1925). Birinchi maksimum holati kontakt potensiallar farqi tufayli siljigan, shuning uchun \(E_1\) qo‘shni maksimumlar orasidagi masofadan topiladi.</p>""",
 steps=["Bor modelida Balmer seriyasining n_yu = 3, 4, 5, 6 chiziqlari to‘lqin uzunliklarini yozing (yoki spektroskopda kuzatilgan qiymatlardan foydalaning).", "1/λ ni 1/n_yu² ga qarshi grafikda tasvirlab, eng kichik kvadratlar usulida Ridberg doimiysi R ni toping.", "Layman va Pashen seriyalarining birinchi chiziqlarini hisoblang va model bilan tekshiring.", "Frank–Gers modelida tezlatuvchi kuchlanishni 0 dan 30 V gacha o‘zgartirib, anod toki I(U) ni har 0,5 V da yozing (U_t = 0,5 V).", "I(U) grafigidagi maksimumlar holatlarini aniqlang va qo‘shni maksimumlar orasidagi masofa ΔU ni o‘rtachalang.", "E₁ = eΔU va chiqariladigan nur to‘lqin uzunligini hisoblang; U_t ni o‘zgartirib, ΔU o‘zgarmasligini tekshiring."],
 table=(["Chiziq", "n_yu", "λ, nm", "1/n_yu²", "1/λ, 10⁶ m⁻¹"], [["H_α", "3", "656,3", "0,1111", "1,5237"], ["H_β", "4", "486,1", "0,0625", "2,0572"], ["H_γ", "5", "434,0", "0,0400", "2,3041"], ["H_δ", "6", "410,2", "0,0278", "2,4378"]]),
 calc=r"""<p><b>Vodorod.</b> \(1/\lambda=a+k/n_{yu}^2\) to‘g‘ri chizig‘i: qiyalik \(k=-1{,}0972\cdot10^7\) m⁻¹ \(\Rightarrow R=(1{,}097\pm0{,}002)\cdot10^7\) m⁻¹; ozod had \(a=2{,}743\cdot10^6\) m⁻¹ \(=R/4\) — Balmer seriyasi chegarasi \(1/a=364{,}6\) nm. Jadval qiymati \(R_H=1{,}0968\cdot10^7\) m⁻¹.</p>
<p><b>Frank–Gers.</b> Anod toki maksimumlari: 6,90; 11,85; 16,70; 21,65; 26,50 V. Qo‘shni maksimumlar orasidagi o‘rtacha masofa \(\Delta U=(4{,}90\pm0{,}09)\) V:</p>
$$E_1=e\Delta U=4{,}90\ \text{eV},\qquad \lambda=\frac{hc}{E_1}=\frac{1239{,}8\ \text{eV·nm}}{4{,}90\ \text{eV}}=253\ \text{nm}$$
<p>Simobning rezonans chizig‘i 253,7 nm bilan mos keladi. Birinchi maksimum 4,9 V da emas, 6,9 V da — farq kontakt potensiallar farqi va tormozlovchi kuchlanish bilan izohlanadi; \(U_t\) o‘zgartirilganda \(\Delta U\) o‘zgarmadi.</p>""",
 code="""import numpy as np
n   = np.array([3, 4, 5, 6])
lam = np.array([656.3, 486.1, 434.0, 410.2])*1e-9      # m
(k, a), cov = np.polyfit(1/n**2, 1/lam, 1, cov=True)
print(f"R = {-k:.4e} 1/m (jadval 1,0968e7), seriya chegarasi = {1/a*1e9:.1f} nm")
Umax = np.array([6.90, 11.85, 16.70, 21.65, 26.50])    # V, Frank-Gers maksimumlari
dU = np.diff(Umax)
E1 = dU.mean()
print(f"dU = {E1:.2f} ± {3.18*dU.std(ddof=1)/np.sqrt(len(dU)):.2f} V, E1 = {E1:.2f} eV, lambda = {1239.84/E1:.0f} nm")""",
 questions=["Bor postulatlarini ayting; ular spektrni qanday tushuntiradi?", "Ridberg doimiysini grafik usulda qanday aniqladingiz?", "Frank–Gers tajribasida anod toki nima uchun davriy ravishda kamayadi?", "Nima uchun birinchi maksimum 4,9 V da emas?", "Bu tajriba Bor nazariyasining qaysi postulatini tasdiqlaydi?"]
))
