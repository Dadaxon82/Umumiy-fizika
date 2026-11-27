"""I modul. Mexanika: M1–M7 ma'ruzalar mazmuni."""

AI = "Sen umumiy fizika bo‘yicha sokratik repetitorsan. Mavzu: {t}.\n{b}\nJavobingda men tekshirishim kerak bo‘lgan 3 ta “xavfli” joyni (ishoralar, birliklar, yaqinlashuvlar) alohida sanab ber. Javobni darhol berma — avval 2 ta yo‘naltiruvchi savol ber."

L = []

L.append(dict(
 n=1, short="Moddiy nuqta kinematikasi", sim="kinem", refs=[1, 2, 3], intl=["halliday", "openstax1", "si"], tn=["TN1", "TN3", "TN7"],
 phet=[("The Moving Man", "moving-man"), ("Vector Addition", "vector-addition")],
 title="Moddiy nuqta kinematikasi. Fazo, vaqt va sanoq sistemasi. Fizik kattaliklar va o‘lchov birliklari",
 goal="Mexanik harakatni tavsiflash usullarini — sanoq sistemasi, trayektoriya, yo‘l va ko‘chish, tezlik va tezlanish tushunchalarini — hamda fizik kattaliklar va SI birliklar tizimini o‘rganish; to‘g‘ri chiziqli tekis o‘zgaruvchan harakat tenglamalarini qo‘llash ko‘nikmasini shakllantirish.",
 outcomes=["sanoq sistemasini tanlaydi va harakatning nisbiyligini misollar bilan izohlaydi;",
           "yo‘l va ko‘chishni, o‘rtacha va oniy tezlikni farqlaydi;",
           "tekis o‘zgaruvchan harakat tenglamalaridan koordinata, tezlik va vaqtni hisoblaydi, \\(x(t)\\) va \\(v(t)\\) grafiklarini o‘qiydi;",
           "kattaliklarni SI birliklarida ifodalaydi va formulalarning o‘lchamliligini tekshiradi."],
 plan=["Mexanik harakat. Fazo va vaqt. Sanoq sistemasi, harakatning nisbiyligi", "Moddiy nuqta, trayektoriya, yo‘l va ko‘chish", "O‘rtacha va oniy tezlik", "Tezlanish. To‘g‘ri chiziqli tekis o‘zgaruvchan harakat", "Fizik kattaliklar. SI birliklar tizimi va o‘lchamlilik tahlili"],
 terms=["sanoq sistemasi", "moddiy nuqta", "trayektoriya", "ko‘chish \\(\\Delta\\vec r\\)", "oniy tezlik \\(\\vec v=d\\vec r/dt\\)", "tezlanish \\(\\vec a=d\\vec v/dt\\)", "SI asosiy birliklari"],
 theory=[
  ("Mexanik harakat, fazo, vaqt va sanoq sistemasi", r"""<p>Mexanik harakat — jismning vaqt o‘tishi bilan boshqa jismlarga nisbatan fazodagi vaziyatining o‘zgarishi. Harakatni tavsiflash uchun <b>sanoq sistemasi</b> tanlanadi: sanoq jismi, unga bog‘langan koordinatalar sistemasi va vaqtni o‘lchash asbobi (soat). Klassik mexanikada fazo bir jinsli va izotrop, vaqt esa barcha sanoq sistemalarida bir xil o‘tadi deb qaraladi.</p>
<p>Harakat <b>nisbiy</b>: vagondagi yo‘lovchi vagonga nisbatan tinch, Yerga nisbatan esa harakatda. Tezliklarni qo‘shishning klassik qonuni: \(\vec v=\vec v\,'+\vec u\), bu yerda \(\vec v\,'\) — jismning harakatlanuvchi sistemaga nisbatan tezligi, \(\vec u\) — shu sistemaning tezligi.</p>"""),
  ("Moddiy nuqta, trayektoriya, yo‘l va ko‘chish", r"""<p>Agar masala shartida jism o‘lchamlari bosib o‘tilgan masofaga nisbatan e’tiborga olinmaydigan darajada kichik bo‘lsa, jism <b>moddiy nuqta</b> deb qaraladi. Nuqtaning vaziyati radius-vektor \(\vec r(t)=x\vec i+y\vec j+z\vec k\) bilan beriladi. Radius-vektor uchi chizgan chiziq — <b>trayektoriya</b>; trayektoriya bo‘ylab o‘lchangan uzunlik — <b>yo‘l</b> \(s\) (skalyar, kamaymaydi); boshlang‘ich va oxirgi nuqtalarni tutashtiruvchi vektor — <b>ko‘chish</b> \(\Delta\vec r\). Umuman \(s\ge|\Delta\vec r|\); tenglik faqat yo‘nalishi o‘zgarmaydigan to‘g‘ri chiziqli harakatda bajariladi.</p>"""),
  ("Tezlik va tezlanish. Tekis o‘zgaruvchan harakat", r"""<p>O‘rtacha tezlik \(\langle\vec v\rangle=\Delta\vec r/\Delta t\); oniy tezlik va tezlanish — vaqt bo‘yicha hosilalar:</p>
$$\vec v=\frac{d\vec r}{dt},\qquad \vec a=\frac{d\vec v}{dt}=\frac{d^2\vec r}{dt^2}$$
<p>Oniy tezlik trayektoriyaga urinma bo‘ylab yo‘nalgan. To‘g‘ri chiziqli <b>tekis o‘zgaruvchan</b> harakatda (\(a=\text{const}\)):</p>
$$v=v_0+at,\qquad x=x_0+v_0t+\frac{at^2}{2},\qquad v^2-v_0^2=2a(x-x_0)$$
<p>Grafik ma’no: \(x(t)\) grafigiga o‘tkazilgan urinmaning qiyaligi — tezlik, \(v(t)\) grafigi ostidagi yuza — ko‘chish. Erkin tushish — \(a=g\approx9{,}81\) m/s² bo‘lgan tekis tezlanuvchan harakat.</p>"""),
  ("Fizik kattaliklar va SI birliklari", r"""<p>Fizik kattalik son qiymati va birligi bilan beriladi. Xalqaro birliklar tizimi (SI) yettita asosiy birlikka ega: metr (m), kilogramm (kg), sekund (s), amper (A), kelvin (K), mol (mol), kandela (cd). 2019-yildan boshlab ular fundamental doimiylarning aniq qiymatlari orqali ta’riflanadi: metr — yorug‘likning vakuumdagi tezligi \(c=299\,792\,458\) m/s orqali, kilogramm — Plank doimiysi \(h\) orqali, mol — Avogadro doimiysi \(N_A\) orqali.</p>
<p><b>O‘lchamlilik tahlili:</b> tenglamaning ikki tomoni bir xil birlikka ega bo‘lishi shart. Masalan, \([v_0t]=\text{m/s}\cdot\text{s}=\text{m}\) va \([at^2/2]=\text{m/s}^2\cdot\text{s}^2=\text{m}\) — formula to‘g‘ri. Ko‘p ishlatiladigan old qo‘shimchalar: kilo (10³), santi (10⁻²), milli (10⁻³), mikro (10⁻⁶), nano (10⁻⁹).</p>""")],
 chem=["Reaksiya tezligi \\(v=dc/dt\\) — kinematik tezlikning kimyoviy o‘xshashi: konsentratsiyaning vaqt bo‘yicha hosilasi; u ham \\(c(t)\\) grafigiga urinmaning qiyaligi orqali topiladi.",
       "Kimyoviy hisoblarda birliklarni tekshirish (masalan, mol/(L·s)) — o‘lchamlilik tahlilining aynan o‘zi.",
       "Xromatografiyada modda kolonka bo‘ylab o‘rtacha tezlik bilan ko‘chadi: ushlanish vaqti \\(t_R=L/v\\)."],
 example=[("Tormozlanayotgan avtomobil", r"Avtomobil 72 km/soat tezlik bilan harakatlanib, tormozlay boshladi va 4 s da to‘xtadi. Tezlanish, tormozlanish yo‘li va to‘xtashdan 1 s oldingi tezlikni toping.",
           r"\(v_0=72\) km/soat \(=20\) m/s. \(a=(0-20)/4=-5\) m/s². Yo‘l \(s=v_0t+at^2/2=80-40=40\) m (tekshiruv: \(s=v_0^2/(2|a|)=400/10=40\) m). \(t=3\) s da \(v=20-5\cdot3=5\) m/s."),
          ("Yo‘l va ko‘chish", r"Jism \(x(t)=8t-t^2\) (m) qonun bo‘yicha harakatlanadi. Dastlabki 6 s dagi ko‘chish va yo‘lni toping.",
           r"\(v=8-2t\); \(t=4\) s da \(v=0\) — burilish nuqtasi, \(x(4)=16\) m. \(x(6)=48-36=12\) m. Ko‘chish \(\Delta x=12\) m, yo‘l \(s=16+(16-12)=20\) m, ya’ni \(s>|\Delta x|\).")],
 simtask=["\\(v_0=8\\) m/s, \\(a=-2\\) m/s² o‘rnating. To‘xtash vaqtini avval hisoblang, keyin modelda tekshiring.",
          "\\(t\\) ni 0 dan 10 s gacha o‘zgartirib, ko‘chish va yo‘l qachon farq qila boshlashini aniqlang va izohlang.",
          "\\(v(t)\\) grafigi ostidagi yashil yuza ko‘chishga tengligini 2-misol qiymatlari bilan tekshiring."],
 mistakes=[("“Tezlik nol bo‘lsa, tezlanish ham nol.”", "Burilish nuqtasida \\(v=0\\), lekin \\(a\\ne0\\) bo‘lishi mumkin: yuqoriga otilgan jismda eng yuqori nuqtada ham \\(a=g\\)."),
           ("“Yo‘l va ko‘chish — bitta narsa.”", "Yo‘l — skalyar, trayektoriya uzunligi; ko‘chish — vektor. Yopiq trayektoriyada ko‘chish nol, yo‘l esa noldan katta."),
           ("“Manfiy tezlanish har doim sekinlashishni bildiradi.”", "Ishora o‘q yo‘nalishiga bog‘liq: \\(v<0\\) va \\(a<0\\) bo‘lsa, jism tezlashadi.")],
 ai=AI.format(t="moddiy nuqta kinematikasi", b="1) x(t) = 8t − t² (m) uchun v(t), a(t), burilish nuqtasi, 6 s dagi yo‘l va ko‘chishni bosqichma-bosqich hisoblashga yordam ber; har qadamda birliklarni ko‘rsat.\n2) Python (numpy, matplotlib) kodida x(t) va v(t) grafiklarini chizdir; v(t) ostidagi yuzani sonli integrallab ko‘chish bilan solishtir."),
 quiz=[("Qaysi holda jismni moddiy nuqta deb qarash mumkin?", ["Yerning Quyosh atrofida aylanishini o‘rganishda", "Yerning o‘z o‘qi atrofida aylanishini o‘rganishda", "Avtomobilni garajga joylashda", "G‘ildirakning aylanishini o‘rganishda"], 0, "Orbita radiusi (1,5·10⁸ km) Yer o‘lchamlaridan ancha katta."),
       ("Jism radiusi R bo‘lgan aylananing yarmini bosib o‘tdi. Ko‘chish moduli va yo‘l:", ["2R va πR", "πR va 2R", "0 va 2πR", "R va πR"], 0, "Ko‘chish — diametr 2R, yo‘l — yarim aylana uzunligi πR."),
       ("72 km/soat necha m/s?", ["20 m/s", "7,2 m/s", "36 m/s", "259 m/s"], 0, "72·1000/3600 = 20 m/s."),
       (r"\(v(t)\) grafigi ostidagi yuza nimaga teng?", ["ko‘chishga (o‘qqa proyeksiyada)", "tezlanishga", "vaqtga", "kuchga"], 0, r"\(\Delta x=\int v\,dt\)."),
       (r"\(x=5+3t-2t^2\) (m). Tezlanish:", ["−4 m/s²", "−2 m/s²", "3 m/s²", "5 m/s²"], 0, r"\(a/2=-2\Rightarrow a=-4\) m/s²."),
       ("Erkin tushayotgan jism 2 s da qancha masofani bosib o‘tadi (v₀ = 0, g = 9,8 m/s²)?", ["19,6 m", "9,8 m", "39,2 m", "4,9 m"], 0, r"\(h=gt^2/2=19{,}6\) m."),
       ("SI ning asosiy birligi emas:", ["nyuton", "kelvin", "mol", "kandela"], 0, "Nyuton — hosila birlik: 1 N = 1 kg·m/s²."),
       ("Qaysi formula o‘lchamlilik bo‘yicha noto‘g‘ri?", [r"\(v=at^2\)", r"\(s=vt\)", r"\(v^2=2as\)", r"\(s=at^2/2\)"], 0, r"\([at^2]=\text{m}\), tezlik esa m/s da o‘lchanadi."),
       ("Daryo oqimi 1 m/s, qayiqning suvga nisbatan tezligi oqim bo‘ylab 3 m/s. Qirg‘oqqa nisbatan tezlik:", ["4 m/s", "2 m/s", "3 m/s", "√10 m/s"], 0, "Klassik qo‘shish qonuni: 3 + 1 = 4 m/s."),
       (r"\(v_0=10\) m/s, \(a=-2\) m/s². Jism qachon to‘xtaydi va qancha yo‘l bosadi?", ["5 s, 25 m", "5 s, 50 m", "10 s, 50 m", "2 s, 16 m"], 0, r"\(t=v_0/|a|=5\) s, \(s=v_0^2/(2|a|)=25\) m.")],
 blits=["Sanoq sistemasi qaysi uch elementdan iborat?", "Yo‘l ko‘chish modulidan kichik bo‘lishi mumkinmi?", "Spidometr o‘rtacha tezlikni ko‘rsatadimi yoki oniy tezlikni?", "Nima uchun 2019-yilda SI asosiy birliklari qayta ta’riflandi?", "x(t) grafigining eng yuqori nuqtasida tezlik nimaga teng?"]
))

L.append(dict(
 n=2, short="Egri chiziqli harakat", sim="projectile", refs=[1, 2, 3], intl=["halliday", "openstax1", "young"], tn=["TN6", "TN7"],
 phet=[("Projectile Motion", "projectile-motion"), ("Ladybug Revolution", "rotation")],
 title="Egri chiziqli harakat. Tangensial va normal tezlanish. Qattiq jism aylanma harakatining kinematikasi",
 goal="Egri chiziqli harakatda tezlik va tezlanishni tashkil etuvchilarga ajratish, gorizontga burchak ostida otilgan jism harakatini tahlil qilish hamda qattiq jism aylanma harakatining burchak kattaliklarini (burilish burchagi, burchak tezlik, burchak tezlanish) chiziqli kattaliklar bilan bog‘lashni o‘rganish.",
 outcomes=["egri chiziqli harakatda tezlanishni tangensial va normal tashkil etuvchilarga ajratadi;", "otilgan jism uchun uchish vaqti, maksimal balandlik va uchish uzoqligini hisoblaydi;", "burchak tezlik va burchak tezlanishni chiziqli tezlik va tezlanish bilan bog‘laydi;", "tekis aylanma harakatda davr, chastota va markazga intilma tezlanishni hisoblaydi."],
 plan=["Egri chiziqli harakatda tezlik va tezlanish", "Tangensial va normal tezlanish, egrilik radiusi", "Gorizontga burchak ostida otilgan jism harakati", "Qattiq jismning aylanma harakati: burilish burchagi, burchak tezlik va burchak tezlanish", "Chiziqli va burchak kattaliklar orasidagi bog‘lanish"],
 terms=["egrilik radiusi R", "tangensial tezlanish \\(a_\\tau\\)", "normal tezlanish \\(a_n=v^2/R\\)", "burilish burchagi \\(\\varphi\\)", "burchak tezlik \\(\\omega\\)", "burchak tezlanish \\(\\varepsilon\\)", "davr va chastota"],
 theory=[
  ("Egri chiziqli harakatda tezlanish", r"""<p>Egri chiziqli harakatda tezlik vektori trayektoriyaga urinma bo‘ylab yo‘naladi va yo‘nalishini uzluksiz o‘zgartiradi, shuning uchun tezlik moduli o‘zgarmasa ham tezlanish mavjud. To‘liq tezlanishni ikki tashkil etuvchiga ajratamiz:</p>
$$a_\tau=\frac{dv}{dt},\qquad a_n=\frac{v^2}{R},\qquad a=\sqrt{a_\tau^2+a_n^2}$$
<p>Tangensial tezlanish \(a_\tau\) tezlik modulining o‘zgarishini, normal (markazga intilma) tezlanish \(a_n\) esa tezlik yo‘nalishining o‘zgarishini tavsiflaydi; \(R\) — trayektoriyaning berilgan nuqtadagi egrilik radiusi.</p>"""),
  ("Gorizontga burchak ostida otilgan jism", r"""<p>Havo qarshiligi hisobga olinmasa, harakat ikki mustaqil harakatning yig‘indisi: gorizontal yo‘nalishda tekis (\(v_x=v_0\cos\alpha\)), vertikal yo‘nalishda tekis o‘zgaruvchan (\(a_y=-g\)):</p>
$$x=v_0\cos\alpha\, t,\qquad y=v_0\sin\alpha\, t-\frac{gt^2}{2}$$
<p>Trayektoriya — parabola. Yer sirtidan otilganda uchish vaqti \(T=\dfrac{2v_0\sin\alpha}{g}\), maksimal balandlik \(H=\dfrac{v_0^2\sin^2\alpha}{2g}\), uchish uzoqligi \(L=\dfrac{v_0^2\sin2\alpha}{g}\) — u \(\alpha=45^\circ\) da eng katta, \(\alpha\) va \(90^\circ-\alpha\) burchaklarda esa bir xil. Gorizontal otishda (\(\alpha=0\), balandlik \(h\)) tushish vaqti \(t=\sqrt{2h/g}\) va u boshlang‘ich tezlikka bog‘liq emas.</p>"""),
  ("Qattiq jismning aylanma harakati", r"""<p>Qattiq jism qo‘zg‘almas o‘q atrofida aylanganda uning barcha nuqtalari bir xil vaqtda bir xil burchakka buriladi. Burilish burchagi \(\varphi\) radianlarda o‘lchanadi; burchak tezlik va burchak tezlanish:</p>
$$\omega=\frac{d\varphi}{dt},\qquad \varepsilon=\frac{d\omega}{dt}$$
<p>Tekis aylanishda \(\omega=2\pi/T=2\pi\nu\) (\(T\) — davr, \(\nu\) — aylanish chastotasi). Tekis o‘zgaruvchan aylanishda \(\omega=\omega_0+\varepsilon t\), \(\varphi=\omega_0t+\varepsilon t^2/2\) — to‘g‘ri chiziqli harakat formulalarining to‘liq o‘xshashi. Burchak tezlik vektori aylanish o‘qi bo‘ylab o‘ng vint qoidasi bo‘yicha yo‘naladi.</p>"""),
  ("Chiziqli va burchak kattaliklar bog‘lanishi", r"""<p>O‘qdan \(r\) masofadagi nuqta uchun:</p>
$$v=\omega r,\qquad a_\tau=\varepsilon r,\qquad a_n=\omega^2r=\frac{v^2}{r}$$
<p>Aylanayotgan diskning chetidagi nuqtalar markazga yaqin nuqtalardan tezroq harakatlanadi, garchi burchak tezlik hamma uchun bir xil bo‘lsa ham. Masalan, Yer ekvatoridagi nuqta \(v=\omega R_\text{Y}=\frac{2\pi}{86\,164\ \text{s}}\cdot6{,}38\cdot10^6\ \text{m}\approx465\) m/s tezlik bilan harakatlanadi.</p>""")],
 chem=["Sentrifugada zarralarni ajratish markazga intilma tezlanishga asoslangan: \\(a_n=\\omega^2r\\) bir necha ming \\(g\\) ga yetadi va og‘irroq zarralarni tezroq cho‘ktiradi.",
       "Massa-spektrometrda ionlar magnit maydonda aylana bo‘ylab harakatlanadi; trayektoriya radiusidan ion massasi aniqlanadi (M15).",
       "Rotorli bug‘latgich va aralashtirgichlarning tezligi ayl/min da beriladi: \\(\\omega=2\\pi n/60\\)."],
 example=[("Otilgan to‘p", r"To‘p gorizontga 30° burchak ostida 20 m/s tezlik bilan otildi (g = 9,8 m/s²). Uchish vaqti, maksimal balandlik va uchish uzoqligini toping.",
           r"\(v_y=20\sin30^\circ=10\) m/s, \(v_x=17{,}3\) m/s. \(T=2v_y/g=2{,}04\) s; \(H=v_y^2/(2g)=5{,}1\) m; \(L=v_xT=35{,}3\) m. Tekshiruv: \(L=v_0^2\sin60^\circ/g=400\cdot0{,}866/9{,}8=35{,}3\) m."),
          ("Laboratoriya sentrifugasi", r"Rotor radiusi 10 sm, aylanish chastotasi 6000 ayl/min. Probirka tubining chiziqli tezligi va markazga intilma tezlanishini (g birligida) toping.",
           r"\(\nu=100\) s⁻¹, \(\omega=2\pi\nu=628\) rad/s. \(v=\omega r=62{,}8\) m/s. \(a_n=\omega^2r=628^2\cdot0{,}1\approx3{,}95\cdot10^4\) m/s² \(\approx4000g\).")],
 simtask=["1-misol qiymatlarini modelga kiriting va T, H, L ni qo‘lda hisoblangan qiymatlar bilan solishtiring.", "Burchakni 15° dan 75° gacha o‘zgartirib, qaysi burchaklar juftligi bir xil uzoqlik berishini aniqlang va formuladan isbotlang.", "Oyda va Marsda otishni sinab ko‘ring: uchish uzoqligi g ga qanday bog‘liq?"],
 mistakes=[("“Tekis aylanma harakatda tezlanish yo‘q.”", "Tezlik moduli o‘zgarmasa ham yo‘nalishi o‘zgaradi: \\(a_n=v^2/R\\neq0\\)."),
           ("“Trayektoriyaning eng yuqori nuqtasida tezlanish nolga teng.”", "Butun parvoz davomida \\(\\vec a=\\vec g\\); yuqori nuqtada faqat \\(v_y=0\\)."),
           ("“Gorizontal otilgan jism tezroq otilsa, yerga kechroq tushadi.”", "Tushish vaqti faqat balandlikka bog‘liq: \\(t=\\sqrt{2h/g}\\).")],
 ai=AI.format(t="egri chiziqli harakat va otilgan jism", b="1) 30° va 60° burchak ostida bir xil tezlik bilan otilgan jismlarning uchish uzoqligi tengligini isbotlashga yordam ber.\n2) Python’da havo qarshiligi bor (F = −kv) va yo‘q hollar uchun trayektoriyalarni Eyler usulida hisoblab, bitta grafikda solishtir."),
 quiz=[("Tekis aylanma harakatda qaysi kattalik o‘zgaradi?", ["tezlik vektorining yo‘nalishi", "tezlik moduli", "burchak tezlik", "aylanish davri"], 0, "Tezlik moduli o‘zgarmaydi, yo‘nalishi uzluksiz o‘zgaradi."),
       ("Radiusi 0,5 m bo‘lgan g‘ildirak 4 rad/s burchak tezlik bilan aylanadi. Chetidagi nuqtaning chiziqli tezligi:", ["2 m/s", "8 m/s", "0,125 m/s", "4 m/s"], 0, r"\(v=\omega r=2\) m/s."),
       ("Normal tezlanish nimani tavsiflaydi?", ["tezlik yo‘nalishining o‘zgarishini", "tezlik modulining o‘zgarishini", "burilish burchagini", "bosib o‘tilgan yo‘lni"], 0, r"\(a_n=v^2/R\) yo‘nalish o‘zgarishi bilan bog‘liq."),
       ("Havo qarshiligisiz yerdan otilganda qaysi burchakda uchish uzoqligi eng katta?", ["45°", "30°", "60°", "90°"], 0, r"\(L\propto\sin2\alpha\)."),
       ("Gorizontal otilgan jism 20 m balandlikdan necha sekundda tushadi (g = 10 m/s²)?", ["2 s", "4 s", "1 s", "√2 s"], 0, r"\(t=\sqrt{2h/g}=2\) s."),
       ("Soat minut milining burchak tezligi:", [r"\(\pi/1800\) rad/s", r"\(\pi/30\) rad/s", r"\(2\pi\) rad/s", r"\(\pi/21600\) rad/s"], 0, r"\(T=3600\) s, \(\omega=2\pi/3600\)."),
       ("Trayektoriyaning eng yuqori nuqtasida otilgan jismning tezligi:", [r"\(v_0\cos\alpha\)", "0", r"\(v_0\)", r"\(v_0\sin\alpha\)"], 0, "Faqat gorizontal tashkil etuvchi qoladi."),
       ("Aylana bo‘ylab tezlik moduli ortib borsa, to‘liq tezlanish vektori qanday yo‘nalgan?", ["markazga va harakat tomonga og‘gan", "faqat markazga", "faqat urinma bo‘ylab", "nolga teng"], 0, r"\(a_\tau>0\) va \(a_n>0\)."),
       ("Aylanish chastotasi 50 Hz. Davr:", ["0,02 s", "50 s", "0,2 s", "2 s"], 0, "T = 1/ν."),
       ("Tezlik 2 marta ortsa, o‘sha radiusdagi normal tezlanish:", ["4 marta ortadi", "2 marta ortadi", "o‘zgarmaydi", "2 marta kamayadi"], 0, r"\(a_n=v^2/R\).")],
 blits=["Nima uchun Yer sirtidagi har bir jism markazga intilma tezlanishga ega?", "Uchish uzoqligi 30° va 60° da bir xil bo‘lishini qanday tushuntirasiz?", "Radian nima va u nima uchun o‘lchamsiz?", "Disk chetidagi va markazga yaqin nuqtalar uchun ω va v bir xilmi?", "Havo qarshiligi trayektoriyani qanday o‘zgartiradi?"]
))

L.append(dict(
 n=3, short="Moddiy nuqta dinamikasi", sim="newton", refs=[1, 2, 3], intl=["halliday", "kleppner", "openstax1"], tn=["TN3", "TN6", "TN7"],
 phet=[("Forces and Motion: Basics", "forces-and-motion-basics")],
 title="Moddiy nuqta dinamikasi. Nyuton qonunlari. Galileyning nisbiylik prinsipi",
 goal="Nyutonning uchta qonunini, inersial sanoq sistemasi, massa, kuch va impuls tushunchalarini hamda Galileyning nisbiylik prinsipini o‘rganish; ilgarilanma harakat dinamikasining asosiy tenglamasini masalalar yechishda qo‘llash ko‘nikmasini shakllantirish.",
 outcomes=["inersial va noinersial sanoq sistemalarini farqlaydi;", "jismga ta’sir etuvchi kuchlarni chizmada ko‘rsatib, Nyutonning ikkinchi qonunini proyeksiyalarda yozadi;", "impuls va kuch impulsi orqali dinamika tenglamasini ifodalaydi;", "Galiley almashtirishlari va nisbiylik prinsipining mazmunini tushuntiradi."],
 plan=["Nyutonning birinchi qonuni. Inersial sanoq sistemasi", "Massa va kuch. Jism impulsi", "Nyutonning ikkinchi qonuni — ilgarilanma harakat dinamikasining asosiy tenglamasi", "Nyutonning uchinchi qonuni", "Galiley almashtirishlari va nisbiylik prinsipi"],
 terms=["inersiya", "inersial sanoq sistemasi", "massa m", "kuch \\(\\vec F\\)", "impuls \\(\\vec p=m\\vec v\\)", "kuch impulsi", "Galiley almashtirishlari"],
 theory=[
  ("Nyutonning birinchi qonuni va inersial sanoq sistemalari", r"""<p>Agar jismga boshqa jismlar ta’sir etmasa yoki ta’sirlar o‘zaro muvozanatlashsa, jism tinch holatini yoki to‘g‘ri chiziqli tekis harakatini saqlaydi. Bu qonun bajariladigan sanoq sistemalari <b>inersial</b> deyiladi. Yer bilan bog‘langan sistemani ko‘pchilik texnik masalalarda inersial deb hisoblash mumkin: Yer aylanishi bilan bog‘liq tezlanishlar \(\sim0{,}03\) m/s², ya’ni \(g\) ning 0,3 % idan kichik.</p>"""),
  ("Massa, kuch va impuls", r"""<p><b>Massa</b> — jismning inertlik o‘lchovi (kg). <b>Kuch</b> — boshqa jismlar ta’sirining o‘lchovi bo‘lgan vektor kattalik (N). Jism <b>impulsi</b> \(\vec p=m\vec v\) (kg·m/s). Bir nechta kuch ta’sir etganda ularning vektor yig‘indisi — teng ta’sir etuvchi kuch olinadi (kuchlar superpozitsiyasi prinsipi).</p>"""),
  ("Nyutonning ikkinchi va uchinchi qonunlari", r"""<p>Ilgarilanma harakat dinamikasining asosiy tenglamasi:</p>
$$\frac{d\vec p}{dt}=\vec F\qquad\Longrightarrow\qquad m\vec a=\sum_i\vec F_i\quad(m=\text{const})$$
<p>Undan kuch impulsi va impuls o‘zgarishi bog‘lanishi kelib chiqadi: \(\Delta\vec p=\int\vec F\,dt\). <b>Masala yechish algoritmi:</b> 1) jismni ajratib, unga ta’sir etuvchi barcha kuchlarni chizish; 2) o‘qlarni tanlash; 3) ikkinchi qonunni proyeksiyalarda yozish; 4) tenglamalar sistemasini yechish va birliklarni tekshirish.</p>
<p><b>Uchinchi qonun:</b> ikki jism bir-biriga moduli teng, yo‘nalishi qarama-qarshi kuchlar bilan ta’sir qiladi: \(\vec F_{12}=-\vec F_{21}\). Bu kuchlar <i>turli</i> jismlarga qo‘yilgan, shuning uchun bir-birini muvozanatlamaydi.</p>"""),
  ("Galileyning nisbiylik prinsipi", r"""<p>Bir-biriga nisbatan \(u\) tezlik bilan tekis harakatlanayotgan ikki inersial sistemada koordinatalar Galiley almashtirishlari bilan bog‘langan:</p>
$$x=x'+ut,\qquad y=y',\qquad z=z',\qquad t=t'$$
<p>Bundan tezlanish barcha inersial sistemalarda bir xil: \(\vec a=\vec a\,'\). Demak, mexanika qonunlari barcha inersial sanoq sistemalarida bir xil ko‘rinishga ega — <b>Galileyning nisbiylik prinsipi</b>. Yorug‘lik tezligiga yaqin tezliklarda bu almashtirishlar Lorens almashtirishlari bilan almashtiriladi (maxsus nisbiylik nazariyasi).</p>""")],
 chem=["Molekulalarning idish devoriga urilishidagi impuls o‘zgarishi gaz bosimini hosil qiladi: \\(F=\\Delta p/\\Delta t\\) — molekulyar-kinetik nazariyaning asosi (M8).",
       "Analitik tarozida massa og‘irlik kuchlari orqali taqqoslanadi; bunga inert va gravitatsion massalarning tengligi asos bo‘ladi.",
       "Raketa va reaktiv dvigatellarda yonilg‘i yonishining kimyoviy energiyasi gazlar impulsiga aylanadi."],
 example=[("Atvud mashinasi", r"Vaznsiz blok orqali o‘tkazilgan ip uchlariga \(m_1=3\) kg va \(m_2=2\) kg yuklar osilgan. Tezlanish va ip tarangligini toping (g = 9,8 m/s², ishqalanish yo‘q).",
           r"Yuklar uchun: \(m_1a=m_1g-T\), \(m_2a=T-m_2g\). Qo‘shsak: \(a=\frac{m_1-m_2}{m_1+m_2}g=1{,}96\) m/s². \(T=m_2(g+a)=23{,}5\) N. Tekshiruv: \(m_1g=29{,}4\) N \(>T>m_2g=19{,}6\) N — mantiqiy."),
          ("Kuch impulsi", r"Massasi 0,15 kg bo‘lgan to‘p 20 m/s tezlik bilan devorga perpendikulyar urilib, 15 m/s tezlik bilan qaytdi. Zarba 0,01 s davom etdi. Devorning to‘pga o‘rtacha ta’sir kuchini toping.",
           r"O‘qni qaytish yo‘nalishida olamiz: \(\Delta p=0{,}15\,(15-(-20))=5{,}25\) kg·m/s. \(F=\Delta p/\Delta t=525\) N. Uchinchi qonunga ko‘ra to‘p ham devorga 525 N kuch bilan ta’sir qiladi.")],
 simtask=["α = 30°, μ = 0 o‘rnating: tezlanish \\(g\\sin\\alpha\\) ga tengligini tekshiring.", "μ = 0,3 da burchakni oshirib, jism qaysi burchakda harakatga kelishini toping va natijani \\(\\tan\\alpha=\\mu\\) bilan solishtiring.", "Massani o‘zgartiring: nima uchun tezlanish massaga bog‘liq emas? Ikkinchi qonun orqali tushuntiring."],
 mistakes=[("“Harakatni saqlab turish uchun kuch kerak.”", "Kuch tezlikni o‘zgartirish uchun kerak; ishqalanish bo‘lmasa, jism kuchsiz ham tekis harakatlanadi (1-qonun)."),
           ("“Ta’sir va aks ta’sir kuchlari bir-birini muvozanatlaydi.”", "Ular turli jismlarga qo‘yilgan, shuning uchun qo‘shilmaydi."),
           ("“Og‘ir jism kattaroq kuch bilan tortiladi, shuning uchun tezroq tushadi.”", "Og‘irlik kuchi massaga proporsional, tezlanish \\(a=F/m=g\\) esa bir xil.")],
 ai=AI.format(t="Nyuton qonunlari", b="1) Atvud mashinasi uchun kuchlar chizmasini so‘z bilan tasvirlashga va tenglamalarni proyeksiyalarda yozishga yordam ber.\n2) Qiya tekislikdagi jism uchun a(α, μ) grafigini Python’da chizadigan kod yoz va tinchlik/sirpanish chegarasini belgilab ber."),
 quiz=[("Qaysi sanoq sistemasini inersial deb hisoblash mumkin?", ["Yerga nisbatan tekis to‘g‘ri chiziqli harakatlanayotgan poyezd", "Tormozlanayotgan avtobus", "Burilayotgan avtomobil", "Aylanayotgan karusel"], 0, "Inersial sistemaga nisbatan tekis harakatlanayotgan sistema ham inersial."),
       ("1 N kuch 2 kg massali jismga qanday tezlanish beradi?", ["0,5 m/s²", "2 m/s²", "1 m/s²", "9,8 m/s²"], 0, "a = F/m."),
       ("Impulsning SI birligi:", ["kg·m/s", "N/s", "kg·m/s²", "J·s"], 0, "p = mv."),
       ("Ot aravani tortmoqda. Arava otni qanday kuch bilan tortadi?", ["Ot aravani qanday kuch bilan tortsa, xuddi shunday kuch bilan", "kichikroq kuch bilan", "kattaroq kuch bilan", "tortmaydi"], 0, "Nyutonning 3-qonuni."),
       ("Jismga ta’sir etuvchi kuchlarning teng ta’sir etuvchisi nolga teng. Jism:", ["tinch yoki tekis to‘g‘ri chiziqli harakatda", "albatta tinch", "tekis tezlanuvchan harakatda", "aylana bo‘ylab harakatda"], 0, "1-qonun."),
       ("Liftda turgan 60 kg massali odam lift yuqoriga 2 m/s² tezlanish bilan ko‘tarilganda polga qanday kuch bilan bosadi (g = 10 m/s²)?", ["720 N", "600 N", "480 N", "120 N"], 0, "N = m(g + a) = 720 N."),
       ("Kuch impulsi nimaga teng?", ["jism impulsining o‘zgarishiga", "kinetik energiyaga", "bajarilgan ishga", "quvvatga"], 0, r"\(\vec F\Delta t=\Delta\vec p\)."),
       ("Galiley almashtirishlarida qaysi kattalik barcha inersial sistemalarda bir xil?", ["tezlanish", "tezlik", "koordinata", "trayektoriya shakli"], 0, r"\(\vec a=\vec a\,'\)."),
       ("Atvud mashinasida \\(m_1=m_2\\) bo‘lsa, yuklar tezlanishi:", ["0", "g", "g/2", "2g"], 0, "Kuchlar muvozanatda."),
       ("Jism massasi 2 marta, kuch 4 marta oshirilsa, tezlanish:", ["2 marta ortadi", "4 marta ortadi", "o‘zgarmaydi", "2 marta kamayadi"], 0, "a = F/m.")],
 blits=["Avtobus keskin tormozlaganda yo‘lovchilar nima uchun oldinga intiladi?", "Massa va og‘irlik orasidagi farq nima?", "Devorni itarsak, nima uchun o‘zimiz orqaga suriladimiz?", "Inersial sistemani tajribada qanday aniqlash mumkin?", "Dinamometr qaysi qonunlarga asoslanib kuchni o‘lchaydi?"]
))

L.append(dict(
 n=4, short="Tabiatdagi kuchlar", sim="spring", refs=[1, 2, 3], intl=["halliday", "openstax1", "young"], tn=["TN1", "TN6", "TN7"],
 phet=[("Hooke's Law", "hookes-law"), ("Friction", "friction"), ("Gravity Force Lab", "gravity-force-lab")],
 title="Tabiatdagi kuchlar va ularning xossalari: elastiklik, ishqalanish, gravitatsiya. Og‘irlik kuchi va vazn",
 goal="Elastiklik kuchi va Guk qonuni, Yung moduli, ishqalanish kuchlarining turlari, butun olam tortishish qonuni, og‘irlik kuchi va vazn tushunchalarini o‘rganish; kuchlarning fizik tabiatini va qo‘llanish chegaralarini tushunish.",
 outcomes=["Guk qonunini bikrlik va Yung moduli orqali ifodalaydi, mexanik kuchlanish va nisbiy deformatsiyani hisoblaydi;", "tinchlikdagi, sirpanish va dumalash ishqalanishini farqlaydi;", "butun olam tortishish qonunidan erkin tushish tezlanishi va kosmik tezlikni hisoblaydi;", "og‘irlik kuchi va vazn farqini, vaznsizlik va o‘ta yuklanish holatlarini tushuntiradi."],
 plan=["Fundamental o‘zaro ta’sirlar va mexanik kuchlar", "Elastiklik kuchi. Guk qonuni. Yung moduli", "Ishqalanish kuchlari va ularning turlari", "Butun olam tortishish qonuni. Gravitatsiya kuchi", "Og‘irlik kuchi va vazn. Vaznsizlik"],
 terms=["deformatsiya", "bikrlik k", "mexanik kuchlanish \\(\\sigma=F/S\\)", "Yung moduli E", "ishqalanish koeffitsiyenti \\(\\mu\\)", "gravitatsiya doimiysi G", "vazn"],
 theory=[
  ("Kuchlarning tabiati", r"""<p>Tabiatda to‘rt fundamental o‘zaro ta’sir mavjud: gravitatsion, elektromagnit, kuchli va kuchsiz. Mexanikada uchraydigan elastiklik va ishqalanish kuchlari mohiyatan atom va molekulalar orasidagi <b>elektromagnit</b> o‘zaro ta’sirning makroskopik namoyon bo‘lishidir; og‘irlik kuchi esa gravitatsion tabiatga ega.</p>"""),
  ("Elastiklik kuchi. Guk qonuni", r"""<p>Kichik deformatsiyalarda elastiklik kuchi deformatsiyaga proporsional va unga qarama-qarshi yo‘nalgan:</p>
$$F_x=-kx,\qquad \sigma=E\varepsilon,\quad \sigma=\frac FS,\quad \varepsilon=\frac{\Delta l}{l_0}$$
<p>Bu yerda \(k\) — bikrlik (N/m), \(E\) — Yung moduli (Pa), materialning xossasi: po‘lat uchun \(\approx2\cdot10^{11}\) Pa, mis \(\approx1{,}2\cdot10^{11}\) Pa, alyuminiy \(\approx7\cdot10^{10}\) Pa. Sterjen uchun \(k=ES/l_0\). Guk qonuni proporsionallik chegarasigacha bajariladi; undan keyin plastik deformatsiya va oquvchanlik boshlanadi. Egilish deformatsiyasida ham Yung moduli ishtirok etadi: ikki tayanchli sterjen o‘rtasiga \(F\) kuch qo‘yilganda egilish strelasi \(f=\dfrac{Fl^3}{48EI}\) (L6–L7).</p>"""),
  ("Ishqalanish kuchlari", r"""<p><b>Tinchlikdagi ishqalanish</b> kuchi tashqi kuchga teng va qarama-qarshi bo‘lib, maksimal qiymatgacha o‘zgaradi: \(F_\text{t}\le\mu_0N\). <b>Sirpanish ishqalanish</b> kuchi \(F=\mu N\), bu yerda \(N\) — tayanch reaksiyasi, \(\mu\) — sirtlar materiali va holatiga bog‘liq koeffitsiyent (odatda \(\mu<\mu_0\)). <b>Dumalash ishqalanishi</b> sirpanishnikidan ancha kichik — shuning uchun g‘ildirak va podshipniklar ishlatiladi. Suyuqlik va gazlarda harakatlanayotgan jismga qarshilik kuchi ta’sir qiladi: kichik tezliklarda \(F\propto v\), kattalarida \(F\propto v^2\).</p>"""),
  ("Butun olam tortishish qonuni, og‘irlik kuchi va vazn", r"""<p>Ikki moddiy nuqta bir-biriga quyidagi kuch bilan tortiladi:</p>
$$F=G\frac{m_1m_2}{r^2},\qquad G=6{,}674\cdot10^{-11}\ \text{N·m}^2/\text{kg}^2$$
<p>Yer sirtida \(g=GM_\text{Y}/R_\text{Y}^2\approx9{,}8\) m/s²; balandlik ortishi bilan \(g(h)=g\,R^2/(R+h)^2\). Birinchi kosmik tezlik \(v_1=\sqrt{gR}\approx7{,}9\) km/s. <b>Og‘irlik kuchi</b> \(m\vec g\) jismga qo‘yilgan, <b>vazn</b> esa jismning tayanch yoki osmaga ta’sir kuchi. Yuqoriga \(a\) tezlanish bilan harakatlanayotgan liftda vazn \(P=m(g+a)\) (o‘ta yuklanish), erkin tushishda \(P=0\) (vaznsizlik).</p>""")],
 chem=["Polimer va metallarning mexanik xossalari (Yung moduli, mustahkamlik) materialshunoslik va polimer kimyosida asosiy tavsiflardir.",
       "Molekulalararo (van-der-Vaals) kuchlar ham elektromagnit tabiatga ega; ular sirt taranglik va adgeziyani belgilaydi (M11).",
       "Moylash materiallari ishqalanish koeffitsiyentini kamaytirish uchun kimyoviy tarkibiga ko‘ra maxsus tanlanadi."],
 example=[("Simning uzayishi", r"Uzunligi 2 m, diametri 1 mm bo‘lgan po‘lat simga 100 N yuk osildi (E = 2·10¹¹ Pa). Mexanik kuchlanish, nisbiy va absolyut uzayishni toping.",
           r"\(S=\pi d^2/4=7{,}85\cdot10^{-7}\) m². \(\sigma=F/S=1{,}27\cdot10^8\) Pa \(=127\) MPa. \(\varepsilon=\sigma/E=6{,}4\cdot10^{-4}\). \(\Delta l=\varepsilon l_0=1{,}27\) mm."),
          ("Yer sun’iy yo‘ldoshi", r"Yer sirtidan 300 km balandlikda aylana orbita bo‘ylab uchayotgan yo‘ldoshning tezligi va aylanish davrini toping (\(R_\text{Y}=6370\) km, \(g_0=9{,}8\) m/s²).",
           r"Gravitatsiya markazga intilma kuchni ta’minlaydi: \(v=\sqrt{g_0R^2/(R+h)}=\sqrt{9{,}8\cdot(6{,}37\cdot10^6)^2/6{,}67\cdot10^6}\approx7{,}73\) km/s. \(T=2\pi(R+h)/v\approx5420\) s \(\approx90\) min.")],
 simtask=["1-misoldagi qiymatlarni (F = 100 N, L₀ = 2 m, d = 1 mm, po‘lat) o‘rnating va uzayishni hisob bilan solishtiring.", "Bir xil kuchda to‘rt materialni taqqoslang: uzayish Yung moduliga qanday bog‘liq?", "Diametrni ikki marta oshiring — uzayish necha marta kamayadi va nima uchun?"],
 mistakes=[("“Ishqalanish kuchi har doim μN ga teng.”", "Tinch turgan jismga ta’sir etuvchi ishqalanish tashqi kuchga teng; faqat uning maksimal qiymati \\(\\mu_0N\\)."),
           ("“Vazn va og‘irlik kuchi bir xil narsa.”", "Og‘irlik kuchi jismga, vazn esa tayanchga qo‘yilgan; tezlanish bilan harakatda ular farq qiladi."),
           ("“Kosmonavtlar orbitada vaznsiz, chunki u yerda gravitatsiya yo‘q.”", "300 km balandlikda \\(g\\approx8{,}9\\) m/s²; vaznsizlik — erkin tushish holati.")],
 ai=AI.format(t="elastiklik, ishqalanish va gravitatsiya kuchlari", b="1) Bikrliklari k₁ va k₂ bo‘lgan prujinalarni ketma-ket va parallel ulaganda umumiy bikrlikni keltirib chiqarishga yordam ber.\n2) g(h) bog‘lanishini 0–1000 km balandlik uchun Python’da hisoblab, grafikda ko‘rsat; MKS orbitasidagi qiymatni belgilab ber."),
 quiz=[("Prujinaga 10 N kuch ta’sir etganda u 2 sm cho‘zildi. Bikrlik:", ["500 N/m", "5 N/m", "20 N/m", "0,2 N/m"], 0, "k = F/x = 10/0,02."),
       ("Yung modulining birligi:", ["Pa", "N/m", "N", "J"], 0, r"\(E=\sigma/\varepsilon\), \(\varepsilon\) o‘lchamsiz."),
       ("Ikki jism orasidagi masofa 3 marta oshirilsa, tortishish kuchi:", ["9 marta kamayadi", "3 marta kamayadi", "9 marta ortadi", "o‘zgarmaydi"], 0, r"\(F\propto1/r^2\)."),
       ("Gorizontal sirtda 5 kg massali qutini tekis sudrash uchun 15 N kuch kerak. μ (g = 10 m/s²):", ["0,3", "3", "0,15", "0,75"], 0, "μ = F/(mg) = 15/50."),
       ("Qaysi ishqalanish odatda eng kichik?", ["dumalash ishqalanishi", "sirpanish ishqalanishi", "tinchlikdagi ishqalanish maksimumi", "hammasi teng"], 0, "Shuning uchun g‘ildirak va podshipniklar ishlatiladi."),
       ("Pastga 2 m/s² tezlanish bilan tushayotgan liftda 50 kg massali odamning vazni (g = 10 m/s²):", ["400 N", "500 N", "600 N", "100 N"], 0, "P = m(g − a)."),
       ("Birinchi kosmik tezlik taxminan:", ["7,9 km/s", "11,2 km/s", "3,1 km/s", "16,7 km/s"], 0, r"\(v_1=\sqrt{gR}\)."),
       ("Elastiklik kuchining tabiati:", ["elektromagnit", "gravitatsion", "yadro kuchlari", "kuchsiz o‘zaro ta’sir"], 0, "Atomlararo elektr kuchlari."),
       ("Sim diametri 2 marta kattalashtirilsa, bir xil kuch ta’sirida uzayish:", ["4 marta kamayadi", "2 marta kamayadi", "4 marta ortadi", "o‘zgarmaydi"], 0, r"\(S\propto d^2\)."),
       ("Yer sirtidan Yer radiusiga teng balandlikda erkin tushish tezlanishi:", ["g/4", "g/2", "g", "2g"], 0, r"\(g(h)=gR^2/(2R)^2\).")],
 blits=["Nima uchun qishda yo‘llarga qum sepiladi?", "Prujinani teng ikkiga bo‘lsak, har bir bo‘lak bikrligi qanday o‘zgaradi?", "Oyda vazningiz qancha bo‘ladi?", "Ishqalanish foydali bo‘lgan 3 ta misol keltiring.", "Guk qonuni qachon buziladi?"]
))

L.append(dict(
 n=5, short="Mexanikada saqlanish qonunlari", sim="collision", refs=[1, 2, 3], intl=["halliday", "openstax1", "kleppner"], tn=["TN3", "TN6", "TN7"],
 phet=[("Energy Skate Park", "energy-skate-park"), ("Collision Lab", "collision-lab")],
 title="Mexanikada saqlanish qonunlari: impuls, ish, energiya va quvvat. Markaziy to‘qnashuvlar",
 goal="Impulsning va mexanik energiyaning saqlanish qonunlarini, ish, quvvat, kinetik va potensial energiya tushunchalarini o‘rganish; markaziy elastik va noelastik to‘qnashuvlarni saqlanish qonunlari asosida tahlil qilish.",
 outcomes=["yopiq sistema uchun impulsning saqlanish qonunini qo‘llaydi;", "o‘zgaruvchan kuch ishini integral va grafik orqali hisoblaydi, quvvatni topadi;", "konservativ kuchlar maydonida mexanik energiyaning saqlanishini qo‘llaydi, potensial egri chiziqni tahlil qiladi;", "markaziy elastik va mutlaq noelastik to‘qnashuvlarda tezliklarni va energiya yo‘qotishini hisoblaydi."],
 plan=["Impulsning saqlanish qonuni. Reaktiv harakat", "Ish va quvvat", "Kinetik va potensial energiya", "Mexanik energiyaning saqlanish qonuni. Energiyaning grafik tasviri", "Markaziy absolyut elastik va noelastik to‘qnashuvlar"],
 terms=["yopiq sistema", "ish \\(A=\\int\\vec F\\cdot d\\vec r\\)", "quvvat N", "kinetik energiya", "potensial energiya", "konservativ kuch", "potensial o‘ra"],
 theory=[
  ("Impulsning saqlanish qonuni", r"""<p>Tashqi kuchlar ta’sir etmaydigan (yoki ularning yig‘indisi nolga teng) sistema <b>yopiq</b> deyiladi. Nyutonning 2- va 3-qonunlaridan yopiq sistemaning to‘liq impulsi saqlanishi kelib chiqadi:</p>
$$\sum_i m_i\vec v_i=\text{const}$$
<p>Qonun reaktiv harakatni tushuntiradi: raketadan \(u\) nisbiy tezlik bilan chiqayotgan gazlar raketaga \(F=u\,|dm/dt|\) reaktiv kuch beradi. Tsiolkovskiy formulasi: \(v=u\ln(m_0/m)\).</p>"""),
  ("Ish va quvvat", r"""<p>Kuchning elementar ishi \(\delta A=\vec F\cdot d\vec r=F\,ds\cos\alpha\). O‘zgarmas kuch to‘g‘ri chiziqli ko‘chishda \(A=Fs\cos\alpha\); o‘zgaruvchan kuch uchun \(A=\int F_s\,ds\) — \(F_s(s)\) grafigi ostidagi yuza. Masalan, prujinani \(x\) ga cho‘zishda bajarilgan ish \(A=kx^2/2\). Quvvat — ish bajarilish tezligi: \(N=dA/dt=\vec F\cdot\vec v\) (W).</p>"""),
  ("Kinetik va potensial energiya", r"""<p>Kinetik energiya haqidagi teorema: barcha kuchlar ishining yig‘indisi kinetik energiya o‘zgarishiga teng: \(A=\Delta\left(\dfrac{mv^2}{2}\right)\). Ishi yo‘l shakliga bog‘liq bo‘lmagan kuchlar (og‘irlik, elastiklik, gravitatsiya) <b>konservativ</b> deyiladi; ular uchun potensial energiya kiritiladi: \(E_p=mgh\), \(E_p=kx^2/2\), \(E_p=-GMm/r\). Kuch va potensial energiya bog‘lanishi: \(F_x=-dE_p/dx\).</p>"""),
  ("Energiyaning saqlanishi va to‘qnashuvlar", r"""<p>Faqat konservativ kuchlar ta’sir etadigan yopiq sistemada mexanik energiya saqlanadi: \(E=E_k+E_p=\text{const}\). Potensial egri chiziq \(E_p(x)\) da jism faqat \(E\ge E_p\) sohada harakatlanadi; minimum — turg‘un, maksimum — noturg‘un muvozanat. Markaziy <b>elastik</b> to‘qnashuvda impuls ham, kinetik energiya ham saqlanadi:</p>
$$u_1=\frac{(m_1-m_2)v_1+2m_2v_2}{m_1+m_2},\qquad u_2=\frac{(m_2-m_1)v_2+2m_1v_1}{m_1+m_2}$$
<p><b>Mutlaq noelastik</b> to‘qnashuvda jismlar birlashadi: \(u=\dfrac{m_1v_1+m_2v_2}{m_1+m_2}\); kinetik energiyaning \(\Delta E=\dfrac{m_1m_2(v_1-v_2)^2}{2(m_1+m_2)}\) qismi ichki energiyaga aylanadi.</p>""")],
 chem=["Kimyoviy reaksiyalarda energiya saqlanish qonuni termokimyoviy tenglamalar va Gess qonuni ko‘rinishida qo‘llaniladi.",
       "Molekulalar to‘qnashuvi reaksiya kinetikasining asosi: energiyasi aktivatsiya energiyasidan katta bo‘lgan to‘qnashuvlargina reaksiyaga olib keladi.",
       "Kimyoviy bog‘ning potensial energiya egri chizig‘i (Morze potensiali) — potensial o‘raning muhim namunasi; o‘ra chuqurligi bog‘ uzilish energiyasiga teng."],
 example=[("Ballistik mayatnik", r"Massasi 10 g bo‘lgan o‘q 400 m/s tezlik bilan osilgan 2 kg massali qum qopiga tegib, unda tiqilib qoldi. Qop qanday balandlikka ko‘tariladi? Energiyaning qancha qismi issiqlikka aylanadi?",
           r"Noelastik zarba: \(u=\frac{0{,}01\cdot400}{2{,}01}=1{,}99\) m/s. Ko‘tarilish: \(h=u^2/(2g)=0{,}20\) m. Boshlang‘ich \(E_k=800\) J, zarbadan keyin \(\approx3{,}98\) J — energiyaning 99,5 % i issiqlikka aylandi."),
          ("Elastik to‘qnashuv", r"1 kg massali shar 3 m/s tezlik bilan tinch turgan 2 kg massali sharga markaziy elastik uriladi. To‘qnashuvdan keyingi tezliklarni toping.",
           r"\(u_1=\frac{(1-2)\cdot3}{3}=-1\) m/s (orqaga qaytadi), \(u_2=\frac{2\cdot1\cdot3}{3}=2\) m/s. Tekshiruv: impuls \(3=-1+4\); energiya \(4{,}5=0{,}5+4\) J.")],
 simtask=["2-misol qiymatlarini (m₁ = 1, m₂ = 2, v₁ = 3, v₂ = 0, k = 1) kiriting va natijani tekshiring.", "k ni 1 dan 0 gacha kamaytiring: impuls va energiya ustunlarini kuzatib, xulosa yozing.", "Massalar teng va k = 1 bo‘lganda nima sodir bo‘ladi? Bilyard o‘yinida bu qanday ko‘rinadi?"],
 mistakes=[("“Noelastik to‘qnashuvda impuls saqlanmaydi.”", "Impuls har qanday to‘qnashuvda saqlanadi (yopiq sistema); saqlanmaydigan kattalik — kinetik energiya."),
           ("“Ish har doim musbat.”", "Kuch harakatga qarshi bo‘lsa (ishqalanish), ish manfiy; harakatga perpendikulyar kuch ish bajarmaydi."),
           ("“Potensial energiyaning mutlaq qiymati muhim.”", "Faqat uning o‘zgarishi fizik ma’noga ega; nol sath ixtiyoriy tanlanadi.")],
 ai=AI.format(t="impuls va energiyaning saqlanish qonunlari", b="1) Elastik to‘qnashuv formulalarini impuls va energiya saqlanishidan keltirib chiqarishga yordam ber.\n2) Python’da m₂/m₁ nisbatiga qarab birinchi sharga qolgan energiya ulushini hisoblab, grafik chiz va maksimal uzatish shartini top."),
 quiz=[("Impulsning saqlanish qonuni qaysi sistemada bajariladi?", ["yopiq sistemada", "faqat elastik to‘qnashuvda", "faqat tinch sistemada", "har qanday sistemada"], 0, "Tashqi kuchlar yig‘indisi nol bo‘lishi kerak."),
       ("2 kg jism 3 m/s tezlik bilan harakatlanmoqda. Kinetik energiya:", ["9 J", "6 J", "18 J", "3 J"], 0, "mv²/2 = 9 J."),
       ("Prujina (k = 200 N/m) 0,1 m ga cho‘zilgan. Potensial energiya:", ["1 J", "20 J", "10 J", "2 J"], 0, "kx²/2 = 200·0,01/2."),
       ("10 m balandlikdan erkin tushgan jismning yerga tegish tezligi (g = 10 m/s²):", ["≈14 m/s", "10 m/s", "100 m/s", "20 m/s"], 0, r"\(v=\sqrt{2gh}=\sqrt{200}\)."),
       ("Quvvatning SI birligi:", ["vatt", "joul", "nyuton", "ot kuchi"], 0, "1 W = 1 J/s."),
       ("Mutlaq noelastik to‘qnashuvda qaysi kattalik saqlanadi?", ["impuls", "kinetik energiya", "har bir jism tezligi", "hech biri"], 0, "Energiyaning bir qismi issiqlikka aylanadi."),
       ("Teng massali sharlarning markaziy elastik to‘qnashuvida (ikkinchisi tinch):", ["tezliklar almashadi", "ikkalasi to‘xtaydi", "birinchisi ikki marta tez qaytadi", "birlashadi"], 0, "u₁ = 0, u₂ = v₁."),
       ("Avtomobil 20 m/s tezlik bilan harakatlanib, 1500 N tortish kuchi rivojlantirmoqda. Quvvat:", ["30 kW", "75 W", "3 kW", "300 kW"], 0, "N = Fv."),
       ("Aylana bo‘ylab tekis harakatda markazga intilma kuchning ishi:", ["nolga teng", "musbat", "manfiy", "mv² ga teng"], 0, "Kuch tezlikka perpendikulyar."),
       ("Potensial egri chiziqning minimumi nimani bildiradi?", ["turg‘un muvozanatni", "noturg‘un muvozanatni", "harakat mumkin emasligini", "kinetik energiya nolligini"], 0, "Kichik og‘ishda jism qaytadi.")],
 blits=["Nima uchun miltiq otilganda yelkaga zarba beradi?", "Avtomobil xavfsizlik yostig‘i qaysi fizik qonunga asoslangan?", "Konservativ va nokonservativ kuchlarga misol keltiring.", "Mayatnik tebranishida energiya qanday aylanadi?", "Raketa vakuumda nimadan itarilib harakatlanadi?"]
))

L.append(dict(
 n=6, short="Aylanma harakat dinamikasi", sim="rotation", refs=[1, 2, 3], intl=["halliday", "kleppner", "openstax1"], tn=["TN6", "TN7"],
 phet=[("Torque", "torque"), ("Ladybug Revolution", "rotation")],
 title="Qattiq jism aylanma harakati dinamikasi. Inersiya momenti. Impuls momentining saqlanish qonuni",
 goal="Moddiy nuqta va qattiq jismning inersiya momenti, Shteyner teoremasi, kuch momenti, aylanma harakat dinamikasining asosiy tenglamasi, aylanma harakatdagi ish va kinetik energiya hamda impuls momentining saqlanish qonunini o‘rganish.",
 outcomes=["oddiy shakldagi jismlarning inersiya momentini hisoblaydi va Shteyner teoremasini qo‘llaydi;", "kuch momentini topib, aylanma harakat dinamikasining asosiy tenglamasini yozadi;", "aylanma va dumalash harakatida kinetik energiyani hisoblaydi;", "impuls momentining saqlanish qonuni bilan izohlanadigan hodisalarni tushuntiradi."],
 plan=["Moddiy nuqta va jismning inersiya momenti", "Shteyner teoremasi", "Kuch momenti. Aylanma harakat dinamikasining asosiy tenglamasi", "Aylanma harakatda ish va kinetik energiya", "Impuls momenti va uning saqlanish qonuni"],
 terms=["inersiya momenti \\(I=\\sum m_ir_i^2\\)", "Shteyner teoremasi", "kuch momenti \\(\\vec M=\\vec r\\times\\vec F\\)", "kuch yelkasi", "impuls momenti \\(L=I\\omega\\)", "dumalash", "giroskop"],
 theory=[
  ("Inersiya momenti", r"""<p>Moddiy nuqtaning o‘qqa nisbatan inersiya momenti \(I=mr^2\), jismniki — \(I=\sum m_ir_i^2=\int r^2dm\). U aylanma harakatdagi inertlik o‘lchovi bo‘lib, massaning o‘qqa nisbatan taqsimlanishiga bog‘liq. Massasi \(m\), radiusi \(R\) bo‘lgan jismlarning simmetriya o‘qiga nisbatan inersiya momentlari: yupqa halqa \(mR^2\), yaxlit disk (silindr) \(mR^2/2\), shar \(2mR^2/5\), yupqa sferik qobiq \(2mR^2/3\); uzunligi \(l\) bo‘lgan sterjen o‘rtasidan o‘tgan o‘qqa nisbatan \(ml^2/12\).</p>"""),
  ("Shteyner teoremasi", r"""<p>Ixtiyoriy o‘qqa nisbatan inersiya momenti massa markazidan o‘tuvchi parallel o‘qqa nisbatan inersiya momenti va \(ma^2\) ning yig‘indisiga teng:</p>
$$I=I_c+ma^2$$
<p>Masalan, sterjen uchidan o‘tgan o‘qqa nisbatan: \(I=\frac{ml^2}{12}+m\left(\frac l2\right)^2=\frac{ml^2}{3}\). Bu natija fizik mayatnik davrini hisoblashda ishlatiladi (M7, L9).</p>"""),
  ("Kuch momenti va dinamikaning asosiy tenglamasi", r"""<p>Kuch momenti \(\vec M=\vec r\times\vec F\), moduli \(M=Fd\) (\(d\) — kuch yelkasi). Qo‘zg‘almas o‘q atrofida aylanish uchun Nyutonning ikkinchi qonuni:</p>
$$I\varepsilon=\sum M_i,\qquad \frac{d\vec L}{dt}=\vec M$$
<p>Aylanma harakatda ish \(A=\int M\,d\varphi\), kinetik energiya \(E_k=I\omega^2/2\), quvvat \(N=M\omega\). Dumalayotgan jism energiyasi ilgarilanma va aylanma qismlardan iborat: \(E_k=\frac{mv^2}{2}+\frac{I\omega^2}{2}\), \(v=\omega R\). Shu sababli qiya tekislikdan dumalab tushish tezlanishi \(a=\dfrac{g\sin\alpha}{1+I/(mR^2)}\) — u jism shakliga bog‘liq, ammo massa va radiusga bog‘liq emas.</p>"""),
  ("Impuls momentining saqlanishi", r"""<p>Moddiy nuqtaning impuls momenti \(\vec L=\vec r\times\vec p\), jismniki qo‘zg‘almas o‘qqa nisbatan \(L=I\omega\). Tashqi kuchlar momenti nolga teng bo‘lsa, impuls momenti saqlanadi: \(I_1\omega_1=I_2\omega_2\). Figurachi qo‘llarini yig‘ganda inersiya momenti kamayib, aylanish tezlashadi; giroskop o‘qining fazodagi yo‘nalishini saqlashi ham shu qonunga asoslangan.</p>""")],
 chem=["Molekulalarning aylanma energiyasi \\(E=\\frac{L^2}{2I}\\) kvantlangan; mikroto‘lqinli (aylanma) spektroskopiyada molekulaning inersiya momenti va bog‘ uzunligi aniqlanadi.",
       "Gaz molekulalarining issiqlik sig‘imiga aylanma erkinlik darajalari hissa qo‘shadi (M8, M10).",
       "Sentrifuga va magnit aralashtirgich rotorlarining inersiya momenti ularning ishga tushish vaqtini belgilaydi."],
 example=[("Blokka o‘ralgan ip", r"Massasi 2 kg, radiusi 0,1 m bo‘lgan yaxlit disk-blokka ip o‘ralgan, ip uchiga 1 kg yuk osilgan. Yukning tezlanishi va ip tarangligini toping (g = 9,8 m/s²).",
           r"Yuk: \(ma=mg-T\); blok: \(I\varepsilon=TR\), \(I=MR^2/2\), \(\varepsilon=a/R\Rightarrow T=Ma/2\). Demak \(a=\frac{mg}{m+M/2}=4{,}9\) m/s², \(T=1\cdot(9{,}8-4{,}9)=4{,}9\) N."),
          ("Figurachi", r"Figurachi qo‘llari yoyilgan holda 2 ayl/s chastota bilan aylanmoqda, inersiya momenti 4 kg·m². Qo‘llarini yig‘ganda inersiya momenti 1,6 kg·m² ga kamaydi. Yangi chastota va kinetik energiya o‘zgarishini toping.",
           r"\(I_1\nu_1=I_2\nu_2\Rightarrow\nu_2=5\) ayl/s. \(E=I\omega^2/2=2\pi^2I\nu^2\): \(E_1\approx316\) J, \(E_2\approx790\) J — energiya qo‘l mushaklari bajargan ish hisobiga ortdi.")],
 simtask=["Bir xil h va α da shar, disk va halqaning tushish vaqtlarini taqqoslang. Nima uchun massa va radius ahamiyatsiz?", "Disk uchun pastdagi tezlikni \\(v=\\sqrt{4gh/3}\\) formulasi bilan tekshiring.", "Qaysi shakl uchun aylanma energiya ulushi eng katta? Natijani inersiya momenti bilan bog‘lang."],
 mistakes=[("“Inersiya momenti faqat massaga bog‘liq.”", "U massaning o‘qqa nisbatan taqsimlanishiga bog‘liq: bir xil massali halqaning I si diskdan ikki marta katta."),
           ("“Kuch qancha katta bo‘lsa, aylantiruvchi ta’sir shuncha katta.”", "Aylantiruvchi ta’sir kuch momenti \\(M=Fd\\) bilan aniqlanadi; o‘qdan o‘tuvchi kuch aylantirmaydi."),
           ("“Dumalab tushayotgan jismlar bir vaqtda tushadi.”", "Tushish vaqti \\(I/(mR^2)\\) ga bog‘liq: shar diskdan, disk halqadan tezroq tushadi.")],
 ai=AI.format(t="aylanma harakat dinamikasi", b="1) Yaxlit disk va halqa inersiya momentlarini integral orqali keltirib chiqarishga yordam ber.\n2) Python’da qiya tekislikdan dumalab tushayotgan to‘rt shakl uchun x(t) ni hisoblab, bitta grafikda solishtir."),
 quiz=[("Massasi 2 kg, radiusi 0,5 m bo‘lgan yaxlit diskning inersiya momenti:", ["0,25 kg·m²", "0,5 kg·m²", "1 kg·m²", "0,2 kg·m²"], 0, "mR²/2."),
       ("Shteyner teoremasi:", [r"\(I=I_c+ma^2\)", r"\(I=I_c-ma^2\)", r"\(I=ma^2\)", r"\(I=I_c a^2\)"], 0, "Parallel o‘qlar teoremasi."),
       ("Kuch momentining SI birligi:", ["N·m", "N/m", "J/s", "kg·m²"], 0, "M = Fd."),
       ("Impuls momentining saqlanishi qachon bajariladi?", ["tashqi kuchlar momenti nolga teng bo‘lganda", "kuchlar umuman bo‘lmaganda", "faqat ω o‘zgarmaganda", "har doim"], 0, r"\(d\vec L/dt=\vec M\)."),
       ("Aylanma harakat kinetik energiyasi:", [r"\(I\omega^2/2\)", r"\(I\omega/2\)", r"\(m\omega^2/2\)", r"\(I^2\omega/2\)"], 0, "mv²/2 ning o‘xshashi."),
       ("Qiya tekislikdan bir xil balandlikdan qaysi jism eng tez tushadi?", ["shar", "yaxlit disk", "halqa", "barchasi bir vaqtda"], 0, "I/(mR²) eng kichik."),
       ("Uzunligi l bo‘lgan sterjenning uchidan o‘tgan o‘qqa nisbatan inersiya momenti:", [r"\(ml^2/3\)", r"\(ml^2/12\)", r"\(ml^2/2\)", r"\(ml^2\)"], 0, "Shteyner teoremasi."),
       ("Diskning inersiya momenti 0,5 kg·m², unga 2 N·m moment ta’sir etmoqda. Burchak tezlanish:", ["4 rad/s²", "1 rad/s²", "0,25 rad/s²", "2 rad/s²"], 0, "ε = M/I."),
       ("Figurachi qo‘llarini yig‘sa, burchak tezligi:", ["ortadi", "kamayadi", "o‘zgarmaydi", "nolga teng bo‘ladi"], 0, "Iω = const."),
       ("Dumalayotgan yaxlit diskda aylanma energiya to‘liq kinetik energiyaning qancha qismi?", ["1/3", "1/2", "2/7", "1/4"], 0, "k/(1 + k), k = 1/2.")],
 blits=["Nima uchun eshik dastasi ilgakdan uzoqroqqa o‘rnatiladi?", "Velosiped harakatlanayotganda nima uchun yiqilmaydi?", "Mushuk qanday qilib har doim oyog‘iga tushadi?", "Inersiya momentini tajribada qanday o‘lchash mumkin?", "Yer aylanishining impuls momenti nima uchun deyarli o‘zgarmaydi?"]
))

L.append(dict(
 n=7, short="Mexanik tebranishlar va to‘lqinlar", sim="oscill", refs=[1, 2, 3, 4], intl=["halliday", "openstax1", "feynman"], tn=["TN4", "TN7"],
 phet=[("Pendulum Lab", "pendulum-lab"), ("Masses and Springs", "masses-and-springs"), ("Wave on a String", "wave-on-a-string")],
 title="Mexanik tebranishlar va to‘lqinlar. Prujinali, matematik va fizik mayatniklar. Tovush to‘lqinlari",
 goal="Garmonik tebranishlarning tenglamasi va parametrlarini (amplituda, siklik chastota, faza), prujinali, matematik va fizik mayatniklar davrini, so‘nuvchi tebranishlarni hamda mexanik to‘lqinlarning (ko‘ndalang, bo‘ylama, tovush) tarqalish qonuniyatlarini o‘rganish.",
 outcomes=["garmonik tebranish tenglamasini yozadi, amplituda, chastota va fazani grafikdan aniqlaydi;", "prujinali, matematik va fizik mayatnik davrini hisoblaydi;", "so‘nuvchi tebranishlar va rezonans hodisasini tushuntiradi;", "to‘lqin uzunligi, chastota va tezlik bog‘lanishini qo‘llaydi, tovush xarakteristikalarini izohlaydi."],
 plan=["Garmonik tebranishlar: amplituda, siklik chastota, faza", "Prujinali, matematik va fizik mayatniklar", "Tebranish energiyasi. So‘nuvchi va majburiy tebranishlar, rezonans", "Mexanik to‘lqinlar: ko‘ndalang va bo‘ylama to‘lqinlar", "To‘lqinlarning muhitda tarqalishi. Tovush to‘lqinlari"],
 terms=["amplituda A", "siklik chastota \\(\\omega_0\\)", "boshlang‘ich faza \\(\\varphi_0\\)", "keltirilgan uzunlik", "so‘nish koeffitsiyenti \\(\\beta\\)", "to‘lqin uzunligi \\(\\lambda\\)", "intensivlik darajasi (dB)"],
 theory=[
  ("Garmonik tebranishlar", r"""<p>Kattalikning vaqt bo‘yicha sinus yoki kosinus qonuni bilan o‘zgarishi garmonik tebranish deyiladi:</p>
$$x=A\cos(\omega_0t+\varphi_0),\qquad \ddot x+\omega_0^2x=0$$
<p>\(A\) — amplituda, \(\omega_0=2\pi/T=2\pi\nu\) — siklik chastota, \(\omega_0t+\varphi_0\) — faza. Tezlik \(v=-A\omega_0\sin(\omega_0t+\varphi_0)\), tezlanish \(a=-\omega_0^2x\). Garmonik tebranish qaytaruvchi kuch siljishga proporsional bo‘lganda (\(F=-kx\)) yuzaga keladi.</p>"""),
  ("Mayatniklar", r"""<p>Prujinali tebrangich: \(T=2\pi\sqrt{m/k}\). Matematik mayatnik (kichik burchaklarda, \(\sin\varphi\approx\varphi\)): \(T=2\pi\sqrt{l/g}\) — davr massa va amplitudaga bog‘liq emas. Fizik mayatnik — o‘qqa osilgan ixtiyoriy jism:</p>
$$T=2\pi\sqrt{\frac{I}{mga}}=2\pi\sqrt{\frac{l_\text{kel}}{g}},\qquad l_\text{kel}=\frac{I}{ma}$$
<p>bu yerda \(a\) — osish nuqtasidan massa markazigacha masofa, \(l_\text{kel}\) — keltirilgan uzunlik. Uchidan osilgan sterjen uchun \(l_\text{kel}=2l/3\). Katta amplitudalarda davr ortadi: \(T\approx T_0(1+\varphi_0^2/16)\). Mayatnik davrini o‘lchab \(g\) ni aniqlash — L8 va L9 laboratoriya ishlarining asosi.</p>"""),
  ("Energiya, so‘nish va rezonans", r"""<p>Garmonik tebranishning to‘liq energiyasi \(E=kA^2/2=m\omega_0^2A^2/2\) doimiy: kinetik va potensial energiya bir-biriga aylanadi. Qarshilik kuchi \(F=-rv\) bo‘lsa, tebranishlar so‘nadi: \(x=A_0e^{-\beta t}\cos(\omega t+\varphi_0)\), \(\beta=r/(2m)\), \(\omega=\sqrt{\omega_0^2-\beta^2}\). Davriy tashqi kuch ta’sirida majburiy tebranishlar yuzaga keladi; kuch chastotasi xususiy chastotaga yaqinlashganda amplituda keskin ortadi — <b>rezonans</b>.</p>"""),
  ("Mexanik to‘lqinlar va tovush", r"""<p>To‘lqin — tebranishlarning muhitda tarqalishi; bunda energiya ko‘chadi, modda esa ko‘chmaydi. Zarralar tarqalish yo‘nalishiga perpendikulyar tebransa — <b>ko‘ndalang</b>, bo‘ylab tebransa — <b>bo‘ylama</b> to‘lqin. Yassi garmonik to‘lqin tenglamasi va asosiy bog‘lanish:</p>
$$\xi(x,t)=A\cos(\omega t-kx),\qquad k=\frac{2\pi}{\lambda},\qquad v=\lambda\nu$$
<p>Tovush — chastotasi 16 Hz dan 20 kHz gacha bo‘lgan bo‘ylama elastik to‘lqin; havoda (20 °C) uning tezligi \(\approx343\) m/s, suvda \(\approx1480\) m/s, po‘latda \(\approx5000\) m/s. Tovush balandligi chastotaga, qattiqligi intensivlikka bog‘liq; intensivlik darajasi \(L=10\lg(I/I_0)\) dB, \(I_0=10^{-12}\) W/m². Manba yoki kuzatuvchi harakatlanganda qabul qilinadigan chastota o‘zgaradi — Doppler effekti.</p>""")],
 chem=["Molekulalarning tebranma harakati (kimyoviy bog‘ — “prujina”) infraqizil va Raman spektroskopiyasining asosi: \\(\\nu=\\frac1{2\\pi}\\sqrt{k/\\mu}\\), \\(\\mu\\) — keltirilgan massa.",
       "Ultratovush (20 kHz dan yuqori) sonokimyoda reaksiyalarni tezlashtirish va eritmalarni gomogenlashtirish uchun ishlatiladi.",
       "Kvars rezonatorli mikrotarozilar (QCM) rezonans chastotasining siljishi orqali nanogramm massalarni o‘lchaydi."],
 example=[("Mayatnik bilan g ni aniqlash", r"Uzunligi 1,20 m bo‘lgan matematik mayatnik 20 ta tebranishni 43,9 s da bajardi. Erkin tushish tezlanishini toping.",
           r"\(T=43{,}9/20=2{,}195\) s. \(g=4\pi^2l/T^2=39{,}48\cdot1{,}20/4{,}818=9{,}83\) m/s². Farq jadval qiymatidan (\(\approx9{,}80\) m/s²) 0,3 % — vaqtni o‘lchash xatoligi chegarasida."),
          ("Tovush to‘lqini", r"Kamerton 440 Hz chastotada tebranmoqda. Havoda (v = 343 m/s) va suvda (v = 1480 m/s) to‘lqin uzunligini toping. Ikkala muhitda chastota o‘zgaradimi?",
           r"\(\lambda=v/\nu\): havoda 0,78 m, suvda 3,36 m. Chastota manba bilan belgilanadi va o‘zgarmaydi; muhit almashganda tezlik va to‘lqin uzunligi o‘zgaradi.")],
 simtask=["1-misoldagi uzunlik (1,20 m) ni o‘rnating va model davrini 2,195 s bilan solishtiring.", "Amplitudani 5° dan 60° gacha oshiring: davr qanchaga o‘zgaradi? Kichik burchak yaqinlashuvi qachon buziladi?", "Prujinali tebrangichda m ni 4 marta oshiring — davr qanday o‘zgaradi? β ni oshirib, so‘nishni kuzating."],
 mistakes=[("“Mayatnikning og‘ir yuki tezroq tebranadi.”", "Matematik mayatnik davri massaga bog‘liq emas: \\(T=2\\pi\\sqrt{l/g}\\)."),
           ("“To‘lqin bilan birga modda ham ko‘chadi.”", "Zarralar muvozanat holati atrofida tebranadi; energiya va impuls ko‘chadi."),
           ("“Tovush vakuumda ham tarqaladi.”", "Tovush — elastik to‘lqin, unga muhit kerak; vakuumda tarqalmaydi.")],
 ai=AI.format(t="mexanik tebranishlar va to‘lqinlar", b="1) Matematik mayatnik tenglamasini Nyutonning ikkinchi qonunidan keltirib chiqarishga yordam ber va kichik burchak yaqinlashuvining ma’nosini tushuntir.\n2) Python’da so‘nuvchi tebranish x(t) ni β ning uch qiymati uchun chizadigan kod yoz va logarifmik dekrementni hisobla."),
 quiz=[("x = 0,05cos(10πt) m. Amplituda va chastota:", ["5 sm, 5 Hz", "0,05 sm, 10 Hz", "5 sm, 10π Hz", "10 sm, 5 Hz"], 0, "ω = 10π ⇒ ν = 5 Hz."),
       ("Matematik mayatnik uzunligi 4 marta oshirilsa, davr:", ["2 marta ortadi", "4 marta ortadi", "2 marta kamayadi", "o‘zgarmaydi"], 0, r"\(T\propto\sqrt l\)."),
       ("Prujinali tebrangich: m = 0,4 kg, k = 40 N/m. Davr:", ["≈0,63 s", "≈6,3 s", "0,1 s", "1 s"], 0, r"\(T=2\pi\sqrt{0{,}01}=0{,}628\) s."),
       ("Garmonik tebranishda tezlanish qayerda eng katta?", ["chetki nuqtalarda", "muvozanat holatida", "hamma joyda bir xil", "hech qayerda"], 0, r"\(a=-\omega^2x\)."),
       ("Tovush havoda 340 m/s tezlikda, chastotasi 680 Hz. To‘lqin uzunligi:", ["0,5 m", "2 m", "0,2 m", "5 m"], 0, "λ = v/ν."),
       ("Bo‘ylama to‘lqinlar qaysi muhitlarda tarqaladi?", ["qattiq, suyuq va gazsimon", "faqat qattiq", "faqat gazlarda", "faqat vakuumda"], 0, "Siqilish-cho‘zilish deformatsiyasi barcha muhitlarda bor."),
       ("Uchidan osilgan, uzunligi 1,5 m bo‘lgan sterjenning keltirilgan uzunligi:", ["1 m", "1,5 m", "0,75 m", "0,5 m"], 0, "2l/3."),
       ("Tovush intensivligi 100 marta ortsa, uning darajasi necha dB ga ortadi?", ["20 dB", "100 dB", "10 dB", "2 dB"], 0, "10·lg100 = 20."),
       ("Rezonans nima?", ["majburlovchi kuch chastotasi xususiy chastotaga yaqinlashganda amplitudaning keskin ortishi", "tebranishlarning so‘nishi", "to‘lqinning qaytishi", "chastotaning ikki marta ortishi"], 0, "Energiya eng samarali uzatiladi."),
       ("Tebranish amplitudasi 2 marta oshsa, energiya:", ["4 marta ortadi", "2 marta ortadi", "o‘zgarmaydi", "√2 marta ortadi"], 0, r"\(E\propto A^2\).")],
 blits=["Nima uchun askarlarga ko‘prikdan bir maromda qadam tashlab o‘tish taqiqlanadi?", "Mayatnikli soat yozda orqada qoladimi yoki oldinga ketadimi?", "Chaqmoq va momaqaldiroq orasidagi vaqtdan masofani qanday topish mumkin?", "Ko‘ndalang to‘lqin gazda tarqaladimi?", "Doppler effektiga hayotiy misol keltiring."]
))
