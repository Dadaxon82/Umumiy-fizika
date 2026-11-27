"""V modul. Atom va yadro fizikasi: M25–M27 ma'ruzalar mazmuni."""
from lec_mex import AI

L = []

L.append(dict(
 n=25, short="Atom tuzilishi", sim="bohr", refs=[1, 2, 3, 4, 5], intl=["krane", "openstax3", "atkins"], tn=["TN5", "TN10"],
 phet=[("Models of the Hydrogen Atom", "models-of-the-hydrogen-atom"), ("Rutherford Scattering", "rutherford-scattering")],
 title="Atom tuzilishi. Tomson va Rezerford modellari. Vodorod atomi spektri. Bor postulatlari va vodorod atomi nazariyasi",
 goal="Atom tuzilishi haqidagi tasavvurlarning rivojlanishini (Tomson modeli, Rezerford tajribasi, yadro modeli), vodorod atomining chiziqli spektri va Ridberg formulasini, Bor postulatlari va vodorod atomi uchun Bor nazariyasini hamda Frank–Gers tajribasini o‘rganish.",
 outcomes=["Tomson va Rezerford modellarini tajriba natijalari asosida taqqoslaydi;", "Ridberg formulasi bo‘yicha vodorod spektral chiziqlari to‘lqin uzunligini hisoblaydi va seriyalarni farqlaydi;", "Bor postulatlaridan orbita radiusi, tezligi va energetik sathlarni hisoblaydi;", "Bor nazariyasining yutuqlari va cheklovlarini, kvant mexanikasiga o‘tish zaruriyatini tushuntiradi."],
 plan=["Tomson modeli", "Rezerford tajribasi. Atomning yadro modeli", "Vodorod atomining nurlanish spektri. Spektral seriyalar", "Bor postulatlari. Frank–Gers tajribasi", "Vodorod atomi uchun Bor nazariyasi va uning cheklovlari"],
 terms=["yadro modeli", "alfa-zarralar sochilishi", "Ridberg doimiysi R", "spektral seriya", "statsionar holat", "Bor radiusi \\(a_0\\)", "ionlanish energiyasi"],
 theory=[
  ("Tomson va Rezerford modellari", r"""<p>Elektron kashf etilgach (J. Tomson, 1897), Tomson atomni musbat zaryadlangan shar ichiga joylashgan elektronlar ko‘rinishida tasavvur qildi (“mayizli pudding” modeli). Rezerford rahbarligidagi Geyger va Marsden tajribalarida (1909–1911) yupqa metall folgadan o‘tgan alfa-zarralarning aksariyati deyarli og‘masdan o‘tdi, ammo taxminan 8000 tadan biri 90° dan katta burchakka og‘di. Bu musbat zaryad va deyarli butun massa juda kichik hajmda — <b>yadroda</b> to‘planganini ko‘rsatdi: yadro o‘lchami \(\sim10^{-15}\)–\(10^{-14}\) m, atomniki \(\sim10^{-10}\) m. Sochilgan zarralar soni \(N(\theta)\propto1/\sin^4(\theta/2)\) — Rezerford formulasi.</p>"""),
  ("Vodorod atomi spektri", r"""<p>Vodorod atomining nurlanish spektri chiziqli va seriyalarga bo‘linadi. Ridberg (umumlashgan Balmer) formulasi:</p>
$$\frac1\lambda=R\left(\frac{1}{n_q^2}-\frac{1}{n_{yu}^2}\right),\qquad R=1{,}097\cdot10^7\ \text{m}^{-1}$$
<p>\(n_q=1\) — Layman seriyasi (ultrabinafsha), \(n_q=2\) — Balmer seriyasi (ko‘rinadigan: H\(_\alpha\) 656 nm, H\(_\beta\) 486 nm, H\(_\gamma\) 434 nm, H\(_\delta\) 410 nm), \(n_q=3\) — Pashen seriyasi (infraqizil). Klassik elektrodinamikaga ko‘ra yadro atrofida aylanayotgan elektron nurlanib, yadroga qulashi kerak edi — Rezerford modeli atom barqarorligi va chiziqli spektrni tushuntira olmadi.</p>"""),
  ("Bor postulatlari va Frank–Gers tajribasi", r"""<p>Bor (1913) ikki postulat kiritdi: 1) atom faqat <b>statsionar holatlarda</b> bo‘la oladi va ularda nurlanmaydi; statsionar orbitalarda impuls momenti kvantlangan: \(m_evr=n\hbar\); 2) atom bir statsionar holatdan boshqasiga o‘tganda energiyalar farqiga teng foton chiqaradi yoki yutadi: \(h\nu=E_{n_{yu}}-E_{n_q}\). Energetik sathlarning diskretligini Frank va Gers tajribasi (1914) bevosita tasdiqladi: simob bug‘idagi elektronlar faqat 4,9 eV porsiyalar bilan energiya yo‘qotadi va atomlar 253,7 nm li nur chiqaradi (L33).</p>"""),
  ("Vodorod atomi uchun Bor nazariyasi", r"""<p>Kulon kuchi markazga intilma kuch vazifasini bajarishi va kvantlash shartidan:</p>
$$r_n=a_0n^2,\quad a_0=0{,}529\cdot10^{-10}\ \text{m};\qquad E_n=-\frac{m_ee^4}{8\varepsilon_0^2h^2}\frac1{n^2}=-\frac{13{,}6\ \text{eV}}{n^2}$$
<p>Ionlanish energiyasi 13,6 eV; nazariy Ridberg doimiysi tajriba qiymatiga mos keladi — bu Bor nazariyasining katta yutug‘i edi. Cheklovlari: ko‘p elektronli atomlar spektrini, chiziqlar intensivligini va magnit maydonda ajralishini tushuntira olmaydi; to‘liq tavsifni kvant mexanikasi beradi (to‘lqin funksiyasi, kvant sonlari n, l, m, s — MT-41, MT-42).</p>""")],
 chem=["Atom spektrlari elementlarning “barmoq izi”: atom-emission va atom-absorbsion spektroskopiya elementlar tarkibini aniqlaydi.",
       "Bor modeli elektron qobiqlar va davriy qonunni sifat jihatdan tushuntirishning ilk qadami; ionlanish energiyalari kimyoviy faollikni belgilaydi.",
       "Alanga ranglari (Na — sariq 589 nm, K — binafsha, Cu — yashil) atom sathlari orasidagi o‘tishlar natijasi; sifat tahlilida qo‘llaniladi."],
 example=[("Balmer seriyasi", r"Vodorod atomida elektron 3-sathdan 2-sathga o‘tdi. Chiqarilgan foton to‘lqin uzunligi va energiyasini toping.",
           r"\(\frac1\lambda=1{,}097\cdot10^7\left(\frac14-\frac19\right)=1{,}524\cdot10^6\) m⁻¹ \(\Rightarrow\lambda=656\) nm (qizil H\(_\alpha\) chizig‘i). \(E=13{,}6\,(1/4-1/9)=1{,}89\) eV."),
          ("Bor orbitasi", r"Vodorod atomining asosiy holatida elektron orbitasi radiusi va tezligini toping.",
           r"\(r_1=a_0=0{,}529\cdot10^{-10}\) m. \(m_evr=\hbar\Rightarrow v=\frac{\hbar}{m_ea_0}=\frac{1{,}055\cdot10^{-34}}{9{,}11\cdot10^{-31}\cdot0{,}529\cdot10^{-10}}=2{,}19\cdot10^6\) m/s \(\approx c/137\).")],
 simtask=["3 → 2 o‘tishni tanlang va to‘lqin uzunligini 1-misol bilan solishtiring; spektrdagi chiziq rangini ayting.", "Balmer seriyasining ko‘rinadigan chiziqlarini (n_yu = 3…6) toping va jadvalga yozing.", "Layman va Pashen seriyalari nima uchun ko‘zga ko‘rinmaydi? Spektr shkalasidan tushuntiring."],
 mistakes=[("“Elektron atomda sayyora kabi aniq orbita bo‘ylab aylanadi.”", "Bu Bor modelining soddalashtirilgan tasviri; kvant mexanikasida elektron holati ehtimollik bulutlari (orbitallar) bilan tavsiflanadi."),
           ("“Atom istalgan energiyali fotonni yutadi.”", "Atom faqat sathlar farqiga teng energiyali fotonlarni yutadi (rezonans yutilish)."),
           ("“Yadro atom hajmining katta qismini egallaydi.”", "Yadro o‘lchami atomnikidan 10⁴–10⁵ marta kichik; atom asosan bo‘shliqdan iborat.")],
 ai=AI.format(t="atom tuzilishi va Bor nazariyasi", b="1) Bor postulatlaridan r_n va E_n formulalarini keltirib chiqarishga yordam ber.\n2) Python’da vodorodning Layman, Balmer va Pashen seriyalari birinchi 5 tadan chizig‘ining to‘lqin uzunliklarini hisoblab, jadval va spektr diagrammasini chiz."),
 quiz=[("Rezerford tajribasida alfa-zarralarning katta burchakka og‘ishi nimani ko‘rsatdi?", ["musbat zaryad kichik yadroda to‘planganini", "elektronlar og‘irligini", "atom bo‘linmasligini", "yorug‘lik to‘lqin ekanini"], 0, "Faqat kichik massiv markaz katta og‘ish beradi."),
       ("Vodorod atomi asosiy holatining energiyasi:", ["−13,6 eV", "−3,4 eV", "0", "+13,6 eV"], 0, "E₁ = −13,6 eV."),
       ("Balmer seriyasi qaysi sathga o‘tishlarga mos?", ["n = 2", "n = 1", "n = 3", "n = 4"], 0, "Ko‘rinadigan chiziqlar."),
       ("n = 2 orbita radiusi n = 1 nikidan:", ["4 marta katta", "2 marta katta", "8 marta katta", "teng"], 0, "r ∝ n²."),
       ("Bor postulatiga ko‘ra chiqariladigan foton energiyasi:", [r"\(h\nu=E_{n_{yu}}-E_{n_q}\)", r"\(h\nu=E_n\)", r"\(h\nu=kT\)", r"\(h\nu=mc^2\)"], 0, "Sathlar farqi."),
       ("Layman seriyasi qaysi sohada joylashgan?", ["ultrabinafsha", "ko‘rinadigan", "infraqizil", "radio"], 0, "Asosiy sathga o‘tishlar."),
       ("Vodorodni n = 2 holatdan ionlash uchun kerakli energiya:", ["3,4 eV", "13,6 eV", "10,2 eV", "1,51 eV"], 0, "13,6/4."),
       ("Frank–Gers tajribasi nimani isbotladi?", ["atom energetik sathlarining diskretligini", "elektronning to‘lqin xossasini", "yadro mavjudligini", "fotoeffektni"], 0, "Energiya porsiyalarda yo‘qotiladi."),
       ("H_α chizig‘i (656 nm) rangi:", ["qizil", "ko‘k", "binafsha", "yashil"], 0, "Balmer seriyasining birinchi chizig‘i."),
       ("Atom o‘lchamining yadro o‘lchamiga nisbati tartibi:", ["10⁴–10⁵", "10", "10²", "10⁹"], 0, "10⁻¹⁰ m / 10⁻¹⁵ m.")],
 blits=["Nima uchun natriy lampasi sariq yorug‘lik beradi?", "Rezerford tajribasida nima uchun juda yupqa oltin folga ishlatilgan?", "Klassik fizika nima uchun atom barqarorligini tushuntira olmadi?", "Yulduzlar tarkibini qanday aniqlaymiz?", "Bor nazariyasi geliy atomiga qo‘llanadimi?"]
))

L.append(dict(
 n=26, short="Radioaktivlik", sim="decay", refs=[1, 2, 3, 4, 5], intl=["krane", "openstax3", "atkins"], tn=["TN1", "TN5", "TN10"],
 phet=[("Alpha Decay", "alpha-decay"), ("Beta Decay", "beta-decay"), ("Radioactive Dating Game", "radioactive-dating-game")],
 title="Radioaktivlik. Radioaktiv yemirilish qonuni. Siljish qoidasi. Alfa- va beta-yemirilish. Gamma-nurlanish va uning xossalari",
 goal="Radioaktivlik hodisasini, radioaktiv yemirilish qonuni, yarim yemirilish davri va aktivlikni, siljish qoidalarini, alfa- va beta-yemirilish mexanizmlarini, gamma-nurlanish va uning xossalarini hamda nurlanishdan himoyalanish asoslarini o‘rganish.",
 outcomes=["radioaktiv yemirilish qonuni bo‘yicha qolgan yadrolar soni, aktivlik va yarim yemirilish davrini hisoblaydi;", "siljish qoidalari asosida yadro o‘zgarishlari tenglamalarini yozadi;", "alfa, beta va gamma nurlanishlarning tabiati, kirish va ionlash qobiliyatlarini taqqoslaydi;", "radioaktiv izotoplarning tibbiyot, kimyo va arxeologiyada qo‘llanilishi va xavfsizlik qoidalarini tushuntiradi."],
 plan=["Radioaktivlikning kashf etilishi. Nurlanish turlari", "Radioaktiv yemirilish qonuni. Yarim yemirilish davri. Aktivlik", "Siljish qoidasi. Radioaktiv qatorlar", "Alfa-yemirilish. Beta-yemirilish va neytrino", "Gamma-nurlanish va uning xossalari. Dozimetriya va himoya"],
 terms=["yemirilish doimiysi \\(\\lambda\\)", "yarim yemirilish davri \\(T_{1/2}\\)", "aktivlik A (Bq)", "siljish qoidasi", "alfa-zarra", "beta-yemirilish", "yutilgan doza (Gy)"],
 theory=[
  ("Radioaktivlik va nurlanish turlari", r"""<p>Bekkerel (1896) uran tuzlari ko‘zga ko‘rinmas, qora qog‘ozdan o‘tuvchi nurlanish chiqarishini kashf etdi; Mariya va Pyer Kyuri poloniy va radiyni ajratib oldi. <b>Radioaktivlik</b> — beqaror yadrolarning o‘z-o‘zidan boshqa yadrolarga aylanishi va zarralar chiqarishi. Magnit maydonda nurlanish uch tashkil etuvchiga ajraladi: \(\alpha\) — geliy yadrolari (\(^4_2\)He), \(\beta^-\) — elektronlar, \(\gamma\) — yuqori energiyali fotonlar. Kirish qobiliyati: \(\alpha\) — qog‘oz varag‘ida to‘xtaydi, \(\beta\) — bir necha mm alyuminiyda, \(\gamma\) uchun sm–dm qalinlikdagi qo‘rg‘oshin kerak; ionlash qobiliyati esa teskari tartibda kamayadi.</p>"""),
  ("Radioaktiv yemirilish qonuni", r"""<p>Har bir yadroning yemirilishi tasodifiy, ammo ko‘p yadrolar uchun statistik qonun bajariladi: \(dN=-\lambda N\,dt\), bundan</p>
$$N=N_0e^{-\lambda t}=N_0\,2^{-t/T_{1/2}},\qquad T_{1/2}=\frac{\ln2}{\lambda},\qquad A=\lambda N$$
<p>Aktivlik birligi — bekkerel (1 Bq = 1 yemirilish/s); eski birlik kyuri (1 Ci = 3,7·10¹⁰ Bq). O‘rtacha yashash vaqti \(\tau=1/\lambda=T_{1/2}/\ln2\). Yarim yemirilish davrlari keng oraliqda: \(^{222}\)Rn 3,82 sutka, \(^{131}\)I 8,02 sutka, \(^{60}\)Co 5,27 yil, \(^{14}\)C 5730 yil, \(^{238}\)U 4,47 mlrd yil.</p>"""),
  ("Siljish qoidasi. Alfa- va beta-yemirilish", r"""<p>Zaryad va massa soni saqlanishidan siljish qoidalari kelib chiqadi:</p>
$$^A_ZX\to{}^{A-4}_{Z-2}Y+{}^4_2\text{He}\ (\alpha);\qquad ^A_ZX\to{}^{A}_{Z+1}Y+e^-+\tilde\nu_e\ (\beta^-);\qquad ^A_ZX\to{}^{A}_{Z-1}Y+e^++\nu_e\ (\beta^+)$$
<p>Alfa-yemirilishda zarra yadro potensial to‘sig‘ini tunnel effekti orqali yengib chiqadi (Gamov, 1928), shuning uchun uning energiyasi aniq (diskret spektr). Beta-yemirilishda yadrodagi neytron protonga aylanadi (\(n\to p+e^-+\tilde\nu\)); elektronlar energiya spektri uzluksiz — energiyaning bir qismini neytrino olib ketadi (Pauli gipotezasi, 1930). Ketma-ket yemirilishlar radioaktiv qatorlarni hosil qiladi (masalan, \(^{238}\)U → … → \(^{206}\)Pb).</p>"""),
  ("Gamma-nurlanish. Dozimetriya va himoya", r"""<p>Alfa yoki beta yemirilishdan keyin yadro ko‘pincha qo‘zg‘algan holatda qoladi va gamma-kvant chiqarib asosiy holatga o‘tadi; bunda Z va A o‘zgarmaydi. Gamma-nurlar (\(\lambda<10^{-11}\) m) modda bilan fotoeffekt, Kompton sochilishi va elektron-pozitron jufti hosil bo‘lishi orqali ta’sirlashadi; intensivlik eksponensial kamayadi: \(I=I_0e^{-\mu x}\). Nurlanish ta’siri yutilgan doza (grey, 1 Gy = 1 J/kg) va ekvivalent doza (zivert, Sv) bilan baholanadi; tabiiy fon yiliga \(\sim2{,}4\) mSv. Himoya qoidalari: ta’sir vaqtini qisqartirish, masofani oshirish, to‘siq (ekran) ishlatish.</p>""")],
 chem=["Nishonlangan atomlar usuli reaksiya mexanizmlarini o‘rganishga imkon beradi (masalan, ¹⁸O yordamida efirlanishda suv kislorodi qaysi reagentdan kelishi aniqlangan).",
       "Radiouglerod usuli (¹⁴C) organik namunalar yoshini aniqlaydi; geoxronologiyada U–Pb va K–Ar usullari ishlatiladi.",
       "Yadro tibbiyoti: ¹³¹I qalqonsimon bez kasalliklarini davolashda, ⁹⁹ᵐTc diagnostikada, ⁶⁰Co nurlanish terapiyasida qo‘llaniladi."],
 example=[("Yod-131", r"Bemorga yarim yemirilish davri 8 sutka bo‘lgan ¹³¹I preparati yuborildi. 24 sutkadan keyin uning qancha qismi qoladi? Yemirilish doimiysini toping.",
           r"\(t/T_{1/2}=3\Rightarrow N/N_0=2^{-3}=1/8\) (12,5 %). \(\lambda=\ln2/T_{1/2}=0{,}693/(8\cdot86400\ \text{s})=1{,}0\cdot10^{-6}\) s⁻¹."),
          ("Radiouglerod usuli", r"Qadimiy yog‘och namunasining ¹⁴C bo‘yicha solishtirma aktivligi tirik daraxtnikining 25 % iga teng. Namuna yoshini toping (\(T_{1/2}=5730\) yil).",
           r"\(A/A_0=1/4=2^{-2}\Rightarrow t=2T_{1/2}=11\,460\) yil.")],
 simtask=["Yod-131 ni tanlang va bitta T½ dan keyin qolgan yadrolar sonini nazariya va tasodifiy model bo‘yicha solishtiring.", "N₀ ni 100 dan 900 gacha oshiring: model natijasining nazariyadan chetlanishi qanday o‘zgaradi (√N qoidasi)?", "1 mkg izotop aktivligini turli izotoplar uchun solishtiring: nima uchun qisqa yashovchi izotoplar ancha faol?"],
 mistakes=[("“Ikki yarim yemirilish davridan keyin modda to‘liq yemiriladi.”", "Har bir T½ da qolganining yarmi yemiriladi: 2T½ dan keyin 1/4 qoladi."),
           ("“Radioaktiv yemirilishni qizdirish yoki bosim bilan tezlashtirish mumkin.”", "Yemirilish — yadro jarayoni; temperatura, bosim va kimyoviy holat uni deyarli o‘zgartirmaydi."),
           ("“Beta-zarra — yadroda tayyor turgan elektron.”", "Yadroda elektron yo‘q; u neytronning protonga aylanishi paytida hosil bo‘ladi.")],
 ai=AI.format(t="radioaktivlik", b="1) Yemirilish qonunini dN = −λN dt differensial tenglamadan keltirib chiqarishga yordam ber.\n2) Python’da N₀ = 1000 yadro uchun Monte-Karlo yemirilish modelini yozib, natijani N₀e^(−λt) bilan bitta grafikda solishtir."),
 quiz=[("Ikki yarim yemirilish davri o‘tgandan keyin qolgan yadrolar ulushi:", ["1/4", "1/2", "0", "1/8"], 0, "(1/2)²."),
       ("Aktivlik birligi:", ["bekkerel", "grey", "zivert", "rentgen"], 0, "1 Bq = 1 s⁻¹."),
       ("Alfa-yemirilishda massa soni va zaryad soni:", ["A − 4, Z − 2", "A, Z + 1", "A − 2, Z − 4", "A, Z − 1"], 0, "He yadrosi chiqadi."),
       ("β⁻-yemirilishda yadro zaryadi:", ["1 ga ortadi", "1 ga kamayadi", "2 ga kamayadi", "o‘zgarmaydi"], 0, "n → p + e⁻ + ν̃."),
       ("Eng katta kirish qobiliyatiga ega nurlanish:", ["gamma", "alfa", "beta", "barchasi teng"], 0, "Zaryadsiz foton."),
       ("Yemirilish doimiysi va yarim yemirilish davri bog‘lanishi:", [r"\(T_{1/2}=\ln2/\lambda\)", r"\(T_{1/2}=\lambda\ln2\)", r"\(T_{1/2}=1/\lambda\)", r"\(T_{1/2}=2/\lambda\)"], 0, "N = N₀/2 sharti."),
       ("²³⁸₉₂U alfa-yemirilishidan keyin hosil bo‘ladigan yadro:", ["²³⁴₉₀Th", "²³⁴₉₂U", "²³⁸₉₃Np", "²³⁶₉₀Th"], 0, "A − 4, Z − 2."),
       ("Gamma-nurlanishda Z va A:", ["o‘zgarmaydi", "Z ortadi", "A kamayadi", "ikkalasi kamayadi"], 0, "Faqat energiya chiqadi."),
       ("Beta-spektrning uzluksizligi qaysi zarra mavjudligini ko‘rsatdi?", ["neytrino", "pozitron", "neytron", "muon"], 0, "Pauli gipotezasi."),
       ("Radiouglerod usulida qaysi izotop ishlatiladi?", ["¹⁴C", "¹²C", "¹³¹I", "⁶⁰Co"], 0, "T½ = 5730 yil.")],
 blits=["Nima uchun radon gazi uylarda xavfli bo‘lishi mumkin?", "Atom elektr stansiyasi chiqindilari nima uchun uzoq saqlanadi?", "Radioaktiv izotoplar tibbiyotda qanday ishlatiladi?", "Nurlanishdan himoyalanishning uchta usulini ayting.", "Alfa-manba tashqarida deyarli xavfsiz, organizm ichiga tushsa esa nima uchun xavfli?"]
))

L.append(dict(
 n=27, short="Atom yadrosi", sim="binding", refs=[1, 2, 3, 4, 5], intl=["krane", "openstax3", "halliday"], tn=["TN3", "TN5", "TN10"],
 phet=[("Nuclear Fission", "nuclear-fission"), ("Build a Nucleus", "build-a-nucleus")],
 title="Atom yadrosining tuzilishi va xossalari. Yadro kuchlari. Massa defekti va bog‘lanish energiyasi. Yadro reaksiyalari, bo‘linish va sintez",
 goal="Atom yadrosining tarkibi va xossalarini, yadro kuchlarini, massa defekti va bog‘lanish energiyasini, yadroning tomchi va qobiq modellarini, yadro reaksiyalarini, og‘ir yadrolarning bo‘linishi va zanjir reaksiyani, yadro reaktorlari, yadro energetikasi muammolari va termoyadro reaksiyalarini o‘rganish.",
 outcomes=["yadro tarkibi (Z, N, A), izotoplar va yadro o‘lchamini tavsiflaydi;", "massa defekti va bog‘lanish energiyasini hisoblaydi, solishtirma bog‘lanish energiyasi egri chizig‘ini tahlil qiladi;", "yadro reaksiyalari energiyasini hisoblaydi, bo‘linish va sintez energetikasini tushuntiradi;", "zanjir reaksiya, reaktor tuzilishi va yadro energetikasining afzallik va muammolarini baholaydi."],
 plan=["Yadro tarkibi. Nuklonlar. Izotoplar. Yadro o‘lchami", "Yadro kuchlari va ularning xossalari", "Massa defekti va bog‘lanish energiyasi. Tomchi va qobiq modellari", "Yadro reaksiyalari. Og‘ir yadrolarning bo‘linishi. Zanjir reaksiya. Yadro reaktorlari", "Termoyadro reaksiyalari. Yadro energetikasi muammolari"],
 terms=["nuklon", "izotop", "yadro kuchlari", "massa defekti \\(\\Delta m\\)", "solishtirma bog‘lanish energiyasi", "zanjir reaksiya", "termoyadro sintezi"],
 theory=[
  ("Yadro tarkibi", r"""<p>Yadro proton va neytronlardan — nuklonlardan iborat (proton-neytron modeli: Ivanenko va Geyzenberg, 1932; neytronni Chedvik kashf etgan, 1932). Belgilash: \(^A_ZX\), \(Z\) — protonlar soni (zaryad soni), \(N=A-Z\) — neytronlar soni, \(A\) — massa soni. Bir xil Z, turli N li yadrolar — izotoplar (\(^1\)H, \(^2\)H, \(^3\)H; \(^{12}\)C, \(^{13}\)C, \(^{14}\)C). Yadro radiusi \(R\approx1{,}2\cdot10^{-15}A^{1/3}\) m, ya’ni yadro moddasining zichligi barcha yadrolar uchun deyarli bir xil va juda katta (\(\sim2\cdot10^{17}\) kg/m³).</p>"""),
  ("Yadro kuchlari", r"""<p>Protonlar orasidagi Kulon itarishiga qaramay yadroni <b>yadro kuchlari</b> (kuchli o‘zaro ta’sir) ushlab turadi. Ularning xossalari: juda kuchli (yadro masofalarida elektromagnit kuchlardan \(\sim100\) marta kuchli), qisqa ta’sirli (\(\sim10^{-15}\) m), zaryadga bog‘liq emas (p–p, n–n, p–n deyarli bir xil), to‘yinish xossasiga ega (nuklon faqat qo‘shnilari bilan ta’sirlashadi) va spinga bog‘liq. Yengil yadrolarda \(N\approx Z\), og‘irlarida neytronlar ko‘proq — Kulon itarishini kompensatsiyalash uchun.</p>"""),
  ("Massa defekti va bog‘lanish energiyasi", r"""<p>Yadro massasi uni tashkil etuvchi erkin nuklonlar massalari yig‘indisidan kichik. Massa defekti va bog‘lanish energiyasi:</p>
$$\Delta m=Zm_p+(A-Z)m_n-m_\text{ya},\qquad E_\text{bog‘}=\Delta mc^2,\qquad 1\ \text{u}\cdot c^2=931{,}5\ \text{MeV}$$
<p>Solishtirma bog‘lanish energiyasi \(E_\text{bog‘}/A\) temir va nikel (\(A\approx56\)–62) atrofida maksimal (\(\approx8{,}8\) MeV), og‘ir yadrolarda kamayadi (\(^{235}\)U uchun 7,6 MeV). Bundan og‘ir yadrolarning bo‘linishi va yengil yadrolarning qo‘shilishi energiya ajratishi kelib chiqadi. <b>Tomchi modeli</b> (Veyszekker formulasi) yadroni zaryadlangan suyuqlik tomchisi deb qarab, hajmiy, sirt, Kulon va simmetriya hadlari orqali bog‘lanish energiyasini tavsiflaydi; <b>qobiq modeli</b> sehrli sonlar (2, 8, 20, 28, 50, 82, 126) yadrolarining alohida barqarorligini tushuntiradi.</p>"""),
  ("Yadro reaksiyalari, bo‘linish va sintez", r"""<p>Yadro reaksiyalarida zaryad, nuklonlar soni, energiya va impuls saqlanadi; reaksiya energiyasi \(Q=(\sum m_\text{boshl}-\sum m_\text{oxir})c^2\). Birinchi sun’iy yadro reaksiyasi: \(^{14}_7\)N\(+\alpha\to{}^{17}_8\)O\(+p\) (Rezerford, 1919). Uran-235 sekin neytronni yutib bo‘linadi: \(^{235}\)U\(+n\to{}^{141}\)Ba\(+{}^{92}\)Kr\(+3n\); har bir bo‘linishda \(\approx200\) MeV ajraladi. Chiqqan 2–3 neytron yangi bo‘linishlarni keltirib chiqaradi — <b>zanjir reaksiya</b>; neytronlar ko‘payish koeffitsiyenti \(k=1\) da reaksiya boshqariladi (reaktor), \(k>1\) da boshqarilmaydi. Reaktor tarkibi: yoqilg‘i, sekinlatgich (suv, grafit), boshqaruv sterjenlari (bor, kadmiy), issiqlik tashuvchi va himoya.</p>
<p><b>Termoyadro sintezi</b>: \(^2\)H\(+{}^3\)H\(\to{}^4\)He\(+n+17{,}6\) MeV — Quyosh va yulduzlar energiyasining manbai; boshqariladigan sintez (tokamak, ITER loyihasi) kelajak energetikasi. Yadro energetikasi muammolari: radioaktiv chiqindilar, xavfsizlik, yoqilg‘i siklini yopish.</p>""")],
 chem=["Yuqori aniqlikdagi massa-spektrometriyada izotoplarning aniq massalari moddaning elementar tarkibini aniqlash imkonini beradi.",
       "Yadro yoqilg‘isi kimyosi: uranni boyitish (UF₆), ishlatilgan yoqilg‘ini qayta ishlash (PUREX ekstraksiyasi) — radiokimyoning asosiy yo‘nalishlari.",
       "Nukleosintez elementlarning Koinotda tarqalganligini tushuntiradi: temirgacha bo‘lgan elementlar yulduzlardagi sintez reaksiyalarida hosil bo‘ladi."],
 example=[("Geliy yadrosining bog‘lanish energiyasi", r"\(m_p=1{,}007276\) u, \(m_n=1{,}008665\) u, \(^4\)He yadrosi massasi 4,001506 u. Massa defekti, bog‘lanish energiyasi va solishtirma bog‘lanish energiyasini toping.",
           r"\(\Delta m=2\cdot1{,}007276+2\cdot1{,}008665-4{,}001506=0{,}030376\) u. \(E=0{,}030376\cdot931{,}5=28{,}3\) MeV. \(E/A=7{,}07\) MeV."),
          ("Bo‘linish energiyasi", r"Har bir \(^{235}\)U yadrosi bo‘linganda 200 MeV ajraladi. 1 g uran-235 to‘liq bo‘linganda qancha energiya ajraladi? Uni ko‘mir yonishi (29 MJ/kg) bilan solishtiring.",
           r"\(N=\frac{1}{235}\cdot6{,}02\cdot10^{23}=2{,}56\cdot10^{21}\). \(E=2{,}56\cdot10^{21}\cdot200\cdot1{,}6\cdot10^{-13}\ \text{J}=8{,}2\cdot10^{10}\) J. Shuncha energiya uchun \(\approx2800\) kg ko‘mir yoqish kerak bo‘lardi.")],
 simtask=["A = 56 (temir) ni tanlang va E/A ning maksimumga yaqinligini tajriba nuqtalari bilan solishtiring.", "A = 235 va A ≈ 117 da E/A farqidan bo‘linish energiyasini baholang (≈ 200 MeV).", "Yengil yadrolar (A < 20) uchun formula va tajriba farqini toping: tomchi modeli nima uchun bu sohada yomon ishlaydi?"],
 mistakes=[("“Yadro massasi nuklonlar massalari yig‘indisiga teng.”", "Yadro massasi kichikroq; farq (massa defekti) bog‘lanish energiyasiga mos keladi."),
           ("“Bo‘linishda massa “yo‘q bo‘lib”, energiyaga aylanadi.”", "Nuklonlar soni saqlanadi; tinchlikdagi massalar yig‘indisi kamayadi, farqi \\(\\Delta mc^2\\) bo‘laklarning kinetik energiyasiga o‘tadi."),
           ("“Har qanday yadro bo‘linganda energiya ajraladi.”", "Faqat temirdan og‘ir yadrolarning bo‘linishi energetik foydali; yengil yadrolar uchun sintez foydali.")],
 ai=AI.format(t="atom yadrosi va yadro energetikasi", b="1) Veyszekker formulasining har bir hadi (hajmiy, sirt, Kulon, simmetriya, juftlik) fizik ma’nosini tushuntirishga yordam ber.\n2) Python’da E/A(A) egri chizig‘ini formula bo‘yicha chizib, tajriba qiymatlari (²H, ⁴He, ¹²C, ⁵⁶Fe, ²³⁸U) bilan solishtir."),
 quiz=[("¹⁴₆C yadrosida neytronlar soni:", ["8", "6", "14", "20"], 0, "N = A − Z."),
       ("Yadro kuchlarining ta’sir radiusi:", ["~10⁻¹⁵ m", "~10⁻¹⁰ m", "~10⁻⁶ m", "cheksiz"], 0, "Qisqa ta’sirli kuchlar."),
       ("Massa defektining energiya ekvivalenti:", [r"\(\Delta mc^2\)", r"\(\Delta mc\)", r"\(\Delta m/c^2\)", r"\(mv^2/2\)"], 0, "Eynshteyn munosabati."),
       ("1 u massaga mos energiya:", ["931,5 MeV", "13,6 eV", "0,511 MeV", "1 GeV"], 0, "1,66·10⁻²⁷ kg · c²."),
       ("Solishtirma bog‘lanish energiyasi qaysi yadrolarda maksimal?", ["temir–nikel atrofida", "vodorodda", "uranda", "geliyda"], 0, "≈ 8,8 MeV."),
       ("Bitta uran-235 yadrosi bo‘linishida ajraladigan energiya:", ["≈200 MeV", "≈200 keV", "≈2 MeV", "≈20 GeV"], 0, "Bo‘laklar kinetik energiyasi asosiy qism."),
       ("Boshqariladigan zanjir reaksiya sharti:", ["k = 1", "k > 1", "k < 0,5", "k = 0"], 0, "Neytronlar soni o‘zgarmas."),
       ("Reaktorda neytronlarni sekinlatish uchun ishlatiladi:", ["suv yoki grafit", "kadmiy", "qo‘rg‘oshin", "uran-238"], 0, "Yengil yadrolar bilan elastik to‘qnashuv."),
       ("Quyosh energiyasining manbai:", ["termoyadro sintezi", "uran bo‘linishi", "kimyoviy yonish", "radioaktiv yemirilish"], 0, "Vodorodning geliyga aylanishi."),
       ("Izotoplar nimasi bilan farq qiladi?", ["neytronlar soni", "protonlar soni", "elektronlar soni", "kimyoviy xossalari keskin"], 0, "Z bir xil, N turlicha.")],
 blits=["Protonlar itarishiga qaramay yadro nima uchun barqaror?", "Atom bombasi va reaktor farqi nimada?", "Termoyadro reaktorini yaratish nima uchun qiyin?", "“Sehrli sonlar” nima?", "Yadro energetikasini rivojlantirishning afzallik va muammolari nimada?"]
))
