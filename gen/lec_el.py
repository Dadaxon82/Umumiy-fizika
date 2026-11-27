"""III modul. Elektr va magnetizm: M12–M18 ma'ruzalar mazmuni."""
from lec_mex import AI

L = []

L.append(dict(
 n=12, short="Elektrostatik maydon", sim=["coulomb", "capacitor"], refs=[1, 2, 3, 4], intl=["purcell", "openstax2", "halliday"], tn=["TN4", "TN6"],
 phet=[("Coulomb's Law", "coulombs-law"), ("Charges and Fields", "charges-and-fields"), ("Capacitor Lab: Basics", "capacitor-lab-basics")],
 title="Elektrostatik maydon va uning xossalari. Kulon qonuni. Maydon kuchlanganligi va potensiali. Kondensatorlar",
 goal="Elektr zaryadi va uning xossalari (diskretlik, saqlanish), Kulon qonuni, elektrostatik maydon kuchlanganligi va potensiali, superpozitsiya prinsipi, kondensatorlar va ularni ulash hamda elektrostatik maydon energiyasini o‘rganish.",
 outcomes=["Kulon qonuni va superpozitsiya prinsipi asosida nuqtaviy zaryadlar sistemasining maydonini hisoblaydi;", "kuchlanganlik va potensial orasidagi bog‘lanishni qo‘llaydi, ekvipotensial sirtlarni tushuntiradi;", "yassi kondensator, ketma-ket va parallel ulangan kondensatorlar sig‘imini hisoblaydi;", "zaryadlangan kondensator va elektr maydon energiyasini hisoblaydi."],
 plan=["Elektr zaryadi. Zaryadning diskretligi va saqlanish qonuni", "Kulon qonuni. Muhitning dielektrik singdiruvchanligi", "Maydon kuchlanganligi. Superpozitsiya prinsipi. Gauss teoremasi", "Potensial. Kuchlanganlik va potensial bog‘lanishi", "Kondensatorlar va ularni ulash. Elektrostatik maydon energiyasi"],
 terms=["elementar zaryad e", "Kulon qonuni", "kuchlanganlik \\(\\vec E\\)", "potensial \\(\\varphi\\)", "elektr sig‘im C", "dielektrik singdiruvchanlik \\(\\varepsilon\\)", "maydon energiya zichligi"],
 theory=[
  ("Elektr zaryadi va Kulon qonuni", r"""<p>Elektr zaryadi — zarralarning elektromagnit o‘zaro ta’sirdagi ishtirokini tavsiflovchi kattalik (kulon, C). U ikki ishorali: musbat va manfiy. Zaryad <b>diskret</b>: har qanday zaryad elementar zaryadga karrali, \(q=Ne\), \(e=1{,}602\,176\,634\cdot10^{-19}\) C (Milliken tajribasi). <b>Zaryadning saqlanish qonuni:</b> yopiq sistemada zaryadlarning algebraik yig‘indisi o‘zgarmaydi. Nuqtaviy zaryadlarning o‘zaro ta’sir kuchi:</p>
$$F=\frac{1}{4\pi\varepsilon_0\varepsilon}\frac{|q_1q_2|}{r^2},\qquad \frac{1}{4\pi\varepsilon_0}=8{,}99\cdot10^9\ \text{N·m}^2/\text{C}^2$$
<p>Muhitda kuch \(\varepsilon\) marta kamayadi (suv uchun \(\varepsilon\approx81\)).</p>"""),
  ("Maydon kuchlanganligi va superpozitsiya", r"""<p>Elektrostatik maydon kuchlanganligi — sinov zaryadiga ta’sir etuvchi kuchning zaryadga nisbati: \(\vec E=\vec F/q\) (V/m). Nuqtaviy zaryad maydoni \(E=kq/(\varepsilon r^2)\). Bir nechta zaryad maydonlari vektor ravishda qo‘shiladi: \(\vec E=\sum\vec E_i\) (superpozitsiya prinsipi). Kuch chiziqlari musbat zaryaddan boshlanib, manfiy zaryadda tugaydi. <b>Gauss teoremasi:</b> yopiq sirt orqali kuchlanganlik oqimi \(\oint\vec E\cdot d\vec S=q_\text{ich}/\varepsilon_0\); undan cheksiz zaryadlangan tekislik maydoni \(E=\sigma/(2\varepsilon_0)\) va yassi kondensator maydoni \(E=\sigma/\varepsilon_0\) kelib chiqadi.</p>"""),
  ("Potensial", r"""<p>Elektrostatik maydon konservativ; potensial — birlik musbat zaryadning potensial energiyasi: \(\varphi=W/q\) (V). Nuqtaviy zaryad uchun \(\varphi=kq/(\varepsilon r)\). Zaryadni ko‘chirishda maydon ishi \(A=q(\varphi_1-\varphi_2)=qU\). Kuchlanganlik va potensial bog‘lanishi:</p>
$$\vec E=-\nabla\varphi,\qquad E=\frac{U}{d}\ \text{(bir jinsli maydon)}$$
<p>Potensiali bir xil nuqtalar — ekvipotensial sirtlar; kuch chiziqlari ularga perpendikulyar. O‘tkazgich sirti ekvipotensial, ichida maydon nolga teng (elektrostatik himoya — Faradey qafasi).</p>"""),
  ("Kondensatorlar va maydon energiyasi", r"""<p>Elektr sig‘im \(C=q/U\) (F). Yassi kondensator: \(C=\varepsilon\varepsilon_0S/d\). Ulash: parallel \(C=\sum C_i\), ketma-ket \(1/C=\sum1/C_i\). Zaryadlangan kondensator energiyasi va maydon energiya zichligi:</p>
$$W=\frac{CU^2}{2}=\frac{q^2}{2C},\qquad w=\frac{\varepsilon\varepsilon_0E^2}{2}$$
<p>Kondensatorning rezistor orqali zaryadlanishi eksponensial: \(u_C=\mathcal E(1-e^{-t/RC})\), \(\tau=RC\) — vaqt doimiysi (L19).</p>""")],
 chem=["Kulon qonuni ion bog‘lanish va kristall panjara energiyasini (Born–Lande tenglamasi) baholashda asosiy.",
       "Suvning katta dielektrik singdiruvchanligi (ε ≈ 81) ionlar orasidagi tortishishni 81 marta kamaytiradi — tuzlarning suvda yaxshi erishi va dissotsiatsiyalanishi shu bilan bog‘liq.",
       "Elektroforez va ion almashinish xromatografiyasida zarralar elektr maydonida zaryadi va o‘lchamiga qarab ajraladi."],
 example=[("Ikki zaryad maydoni", r"Bir-biridan 10 sm masofada \(q_1=+5\) nC va \(q_2=-5\) nC zaryadlar joylashgan (vakuum). O‘zaro ta’sir kuchi, ular o‘rtasidagi nuqtada maydon kuchlanganligi va potensialni toping.",
           r"\(F=9\cdot10^9\cdot25\cdot10^{-18}/0{,}01=2{,}25\cdot10^{-5}\) N (tortishish). O‘rtadagi nuqtada har bir zaryad maydoni \(E_1=9\cdot10^9\cdot5\cdot10^{-9}/0{,}05^2=1{,}8\cdot10^4\) V/m va ular bir xil yo‘nalgan (musbatdan manfiyga): \(E=3{,}6\cdot10^4\) V/m. Potensial \(\varphi=k(q_1+q_2)/r=0\)."),
          ("Kondensatorlar batareyasi", r"\(C_1=2\) mkF va \(C_2=3\) mkF kondensatorlar ketma-ket ulanib, 10 V kuchlanishga ulangan. Umumiy sig‘im, zaryad, har biridagi kuchlanish va energiyani toping.",
           r"\(C=\frac{2\cdot3}{5}=1{,}2\) mkF. \(q=CU=12\) mkC (ikkalasida bir xil). \(U_1=q/C_1=6\) V, \(U_2=4\) V. \(W=CU^2/2=60\) mkJ.")],
 simtask=["Qarama-qarshi ishorali zaryadlar (dipol) maydon chiziqlarini kuzating va bir xil ishorali holat bilan solishtiring.", "d ni 2 marta kamaytiring — kuch necha marta ortadi? ε = 81 (suv) da kuch qanday o‘zgaradi?", "RC modelida C = 100 mkF, R = 10 kΩ uchun τ ni hisoblang va grafikdan 0,63ε nuqtasini toping."],
 mistakes=[("“Potensial nol bo‘lgan joyda maydon ham nol.”", "Dipol o‘rtasida φ = 0, ammo E ≠ 0. Maydon potensialning o‘zgarish tezligi (gradiyenti) bilan aniqlanadi."),
           ("“Kondensator zaryadi — ikki qoplama zaryadlari yig‘indisi.”", "Qoplamalarda +q va −q bor; kondensator zaryadi deb bitta qoplama zaryadi q tushuniladi."),
           ("“Ketma-ket ulanganda sig‘imlar qo‘shiladi.”", "Ketma-ket ulanganda teskari qiymatlar qo‘shiladi va umumiy sig‘im eng kichigidan ham kichik.")],
 ai=AI.format(t="elektrostatika va kondensatorlar", b="1) Gauss teoremasidan yassi kondensator maydoni va sig‘imini keltirib chiqarishga yordam ber.\n2) Python (numpy, matplotlib streamplot) yordamida ikki nuqtaviy zaryad maydon chiziqlarini chizadigan kod yoz."),
 quiz=[("Elementar zaryad qiymati:", ["1,6·10⁻¹⁹ C", "9,1·10⁻³¹ C", "6,02·10²³ C", "1 C"], 0, "Elektron zaryadining moduli."),
       ("Zaryadlar orasidagi masofa 2 marta kamaysa, Kulon kuchi:", ["4 marta ortadi", "2 marta ortadi", "4 marta kamayadi", "o‘zgarmaydi"], 0, "F ∝ 1/r²."),
       ("Kuchlanganlikning SI birligi:", ["V/m", "V", "C/m", "F"], 0, "N/C = V/m."),
       ("Yassi kondensator qoplamalari orasidagi masofa 2 marta oshirilsa, sig‘im:", ["2 marta kamayadi", "2 marta ortadi", "4 marta kamayadi", "o‘zgarmaydi"], 0, "C ∝ 1/d."),
       ("Uchta 3 mkF kondensator parallel ulangan. Umumiy sig‘im:", ["9 mkF", "1 mkF", "3 mkF", "6 mkF"], 0, "Parallelda qo‘shiladi."),
       ("2 mkF kondensator 100 V gacha zaryadlangan. Energiya:", ["10 mJ", "100 mJ", "1 mJ", "20 mJ"], 0, "CU²/2 = 2·10⁻⁶·10⁴/2."),
       ("Zaryad 1 nC, potensiallar farqi 1000 V. Maydon ishi:", ["1 mkJ", "1 mJ", "1 J", "1 nJ"], 0, "A = qU = 10⁻⁶ J."),
       ("O‘tkazgich ichida elektrostatik maydon kuchlanganligi:", ["nolga teng", "sirtdagidan katta", "markazda maksimal", "zaryadga proporsional"], 0, "Erkin zaryadlar maydonni kompensatsiya qiladi."),
       ("Suvda (ε = 81) ikki ion orasidagi kuch vakuumdagiga nisbatan:", ["81 marta kichik", "81 marta katta", "9 marta kichik", "o‘zgarmaydi"], 0, "F ∝ 1/ε."),
       ("Ekvipotensial sirt va kuch chizig‘i orasidagi burchak:", ["90°", "0°", "45°", "180°"], 0, "Ekvipotensial bo‘ylab ko‘chishda ish nol.")],
 blits=["Nima uchun sintetik kiyimni yechganda chirsillaydi?", "Momaqaldiroq paytida avtomobil ichida nima uchun xavfsiz?", "Kondensatorni zaryadlashda bajarilgan ish qayerga ketadi?", "Elektrometr va elektroskop farqi nimada?", "Nima uchun yuqori kuchlanishli qurilmalarda o‘tkir uchlardan qochiladi?"]
))

L.append(dict(
 n=13, short="O‘zgarmas elektr toki qonunlari", sim="circuit", refs=[1, 2, 3, 4, 5], intl=["openstax2", "halliday", "purcell"], tn=["TN6", "TN8"],
 phet=[("Circuit Construction Kit: DC", "circuit-construction-kit-dc"), ("Ohm's Law", "ohms-law"), ("Resistance in a Wire", "resistance-in-a-wire")],
 title="O‘zgarmas elektr toki qonunlari. Om qonuni. O‘tkazgichlarni ulash. Tokning ishi va quvvati. Joul–Lens qonuni",
 goal="Elektr toki, tok kuchi, kuchlanish va elektr qarshilik tushunchalarini, zanjir qismi va to‘la zanjir uchun Om qonunini, o‘tkazgichlarni ketma-ket va parallel ulashni, Kirxgof qoidalarini, tokning ishi va quvvatini hamda Joul–Lens qonunini o‘rganish.",
 outcomes=["tok kuchi, tok zichligi va dreyf tezligini bog‘laydi;", "Om qonunini zanjir qismi va to‘la zanjir uchun qo‘llaydi, EYuK va ichki qarshilikni tushuntiradi;", "aralash ulangan zanjirlarning umumiy qarshiligini va Kirxgof qoidalari yordamida toklarni hisoblaydi;", "tokning ishi, quvvati va ajraladigan issiqlikni hisoblaydi."],
 plan=["Elektr toki, tok kuchi va tok zichligi", "Kuchlanish, qarshilik, solishtirma qarshilik. Zanjir qismi uchun Om qonuni", "O‘tkazgichlarni ketma-ket va parallel ulash. Kirxgof qoidalari", "EYuK. To‘la zanjir uchun Om qonuni", "Tokning ishi va quvvati. Joul–Lens qonuni"],
 terms=["tok kuchi I", "tok zichligi j", "kuchlanish U", "qarshilik R", "solishtirma qarshilik \\(\\rho\\)", "EYuK \\(\\mathcal E\\)", "ichki qarshilik r"],
 theory=[
  ("Elektr toki", r"""<p>Elektr toki — zaryadlangan zarralarning tartibli harakati. Tok kuchi \(I=dq/dt\) (A), tok zichligi \(j=I/S=qnv_d\), bu yerda \(n\) — tashuvchilar konsentratsiyasi, \(v_d\) — dreyf tezligi. Metallarda tashuvchilar — erkin elektronlar (misda \(n\approx8{,}5\cdot10^{28}\) m⁻³); ularning dreyf tezligi juda kichik (mm/s tartibida), ammo elektr maydon zanjir bo‘ylab yorug‘lik tezligiga yaqin tezlikda tarqaladi. Tok yo‘nalishi deb musbat zaryadlarning harakat yo‘nalishi qabul qilingan.</p>"""),
  ("Om qonuni. Qarshilik", r"""<p>Zanjir qismi uchun Om qonuni: \(I=U/R\). O‘tkazgich qarshiligi \(R=\rho l/S\), \(\rho\) — solishtirma qarshilik (Ω·m; mis \(1{,}7\cdot10^{-8}\), nixrom \(1{,}1\cdot10^{-6}\)). Metallarda qarshilik temperatura bilan ortadi: \(R=R_0(1+\alpha t)\). Om qonunining differensial shakli \(\vec j=\sigma\vec E\), \(\sigma=1/\rho\) — solishtirma o‘tkazuvchanlik.</p>"""),
  ("Ulash usullari va Kirxgof qoidalari", r"""<p>Ketma-ket ulashda \(R=\sum R_i\), tok bir xil, kuchlanishlar qo‘shiladi; parallel ulashda \(1/R=\sum1/R_i\), kuchlanish bir xil, toklar qo‘shiladi. Murakkab zanjirlar uchun <b>Kirxgof qoidalari</b>:</p>
$$\sum_k I_k=0\ \text{(tugun)},\qquad \sum_k I_kR_k=\sum_k\mathcal E_k\ \text{(yopiq kontur)}$$
<p>Birinchisi zaryad saqlanishini, ikkinchisi energiya saqlanishini ifodalaydi (L22). Uitston ko‘prigining muvozanat sharti \(R_x/R_0=R_1/R_2\) qarshilikni aniq o‘lchash usulidir (L21).</p>"""),
  ("EYuK, to‘la zanjir va Joul–Lens qonuni", r"""<p>Manba EYuK i — chet kuchlarning birlik musbat zaryadni ko‘chirishda bajargan ishi: \(\mathcal E=A_\text{chet}/q\) (V). To‘la zanjir uchun Om qonuni:</p>
$$I=\frac{\mathcal E}{R+r},\qquad U=\mathcal E-Ir$$
<p>Tokning ishi \(A=UIt\), quvvati \(P=UI=I^2R=U^2/R\). <b>Joul–Lens qonuni:</b> tok o‘tganda ajraladigan issiqlik \(Q=I^2Rt\). Tashqi zanjirdagi quvvat \(R=r\) da maksimal (\(P_\text{max}=\mathcal E^2/4r\)), bunda FIK 50 %.</p>""")],
 chem=["Elektroliz Faradey qonunlari bo‘yicha: ajralgan modda massasi \\(m=\\frac{M}{zF}It\\), \\(F=eN_A=96\\,485\\) C/mol — Faradey doimiysi.",
       "Eritmalarning elektr o‘tkazuvchanligini o‘lchash (konduktometriya) ionlar konsentratsiyasi va dissotsiatsiya darajasini aniqlaydi.",
       "Galvanik element EYuK i reaksiyaning Gibbs energiyasi bilan bog‘langan: \\(\\Delta G=-zF\\mathcal E\\)."],
 example=[("Akkumulyator", r"EYuK 12 V, ichki qarshiligi 0,5 Ω bo‘lgan akkumulyatorga 5,5 Ω qarshilik ulandi. Tok kuchi, qisqichlardagi kuchlanish, tashqi quvvat va FIK ni toping.",
           r"\(I=12/6=2\) A. \(U=IR=11\) V. \(P=I^2R=22\) W. \(\eta=R/(R+r)=91{,}7\) %."),
          ("Elektroliz", r"Mis kuporosi eritmasidan 2 A tok 30 min o‘tkazildi. Katodda qancha mis ajraladi (M = 63,5 g/mol, z = 2)?",
           r"\(q=It=3600\) C. \(m=\frac{Mq}{zF}=\frac{63{,}5\cdot3600}{2\cdot96485}=1{,}18\) g.")],
 simtask=["1-misol qiymatlarini (ε = 12 V, r = 0,5 Ω, R = 5,5 Ω) kiriting va natijalarni tekshiring.", "R ni 0,1 Ω dan 30 Ω gacha o‘zgartirib, P(R) grafigining maksimumi R = r da ekanini tasdiqlang.", "Qisqa tutashuv tokini hisoblang va akkumulyatorni qisqa tutashtirish nima uchun xavfli ekanini tushuntiring."],
 mistakes=[("“Tok manbada hosil bo‘ladi va zanjirda sarflanadi.”", "Zaryad sarflanmaydi (tugun qoidasi); manbadan iste’molchiga energiya uzatiladi."),
           ("“Elektronlar simda yorug‘lik tezligida harakatlanadi.”", "Dreyf tezligi mm/s tartibida; yorug‘lik tezligiga yaqin tezlikda elektr maydon tarqaladi."),
           ("“Voltmetr va ampermetrni bir xil ulash mumkin.”", "Ampermetr ketma-ket (kichik qarshilik), voltmetr parallel (katta qarshilik) ulanadi.")],
 ai=AI.format(t="o‘zgarmas tok qonunlari", b="1) Ikki konturli zanjir uchun Kirxgof tenglamalarini tuzishga yordam ber (yo‘nalishlarni qanday tanlash kerak?).\n2) Python (numpy.linalg.solve) yordamida 3 tarmoqli zanjir toklarini hisoblaydigan kod yoz va quvvat balansini tekshir."),
 quiz=[("Qarshiligi 20 Ω o‘tkazgichdagi kuchlanish 4 V. Tok kuchi:", ["0,2 A", "5 A", "80 A", "0,5 A"], 0, "I = U/R."),
       ("Sim uzunligi 2 marta oshirilsa, qarshilik:", ["2 marta ortadi", "2 marta kamayadi", "4 marta ortadi", "o‘zgarmaydi"], 0, "R = ρl/S."),
       ("4 Ω va 6 Ω parallel ulangan. Umumiy qarshilik:", ["2,4 Ω", "10 Ω", "5 Ω", "1,5 Ω"], 0, "R = 24/10."),
       ("EYuK 6 V, r = 1 Ω, R = 5 Ω. Tok kuchi:", ["1 A", "6 A", "1,2 A", "0,5 A"], 0, "I = ε/(R + r)."),
       ("Kirxgofning birinchi qoidasi qaysi qonunga asoslangan?", ["zaryad saqlanishi", "energiya saqlanishi", "impuls saqlanishi", "Om qonuni"], 0, "Tugunda zaryad to‘planmaydi."),
       ("100 W lampa 220 V da ishlaydi. Tok kuchi:", ["≈0,45 A", "2,2 A", "22 A", "0,045 A"], 0, "I = P/U."),
       ("Joul–Lens qonuni:", [r"\(Q=I^2Rt\)", r"\(Q=IRt\)", r"\(Q=U/R\)", r"\(Q=IU/t\)"], 0, "Ajraladigan issiqlik."),
       ("Tashqi zanjirdagi quvvat qachon maksimal?", ["R = r", "R = 0", "R → ∞", "R = 2r"], 0, "Moslashtirilgan yuklama."),
       ("1 kVt·soat necha joul?", ["3,6·10⁶ J", "1000 J", "3600 J", "3,6·10³ J"], 0, "1000 W · 3600 s."),
       ("Ampermetr zanjirga qanday ulanadi?", ["ketma-ket", "parallel", "istalgancha", "manbaga parallel"], 0, "U orqali o‘lchanayotgan tok o‘tishi kerak.")],
 blits=["Nima uchun uydagi asboblar parallel ulanadi?", "Qisqa tutashuv nima uchun xavfli?", "Saqlagich (predoxranitel) qanday ishlaydi?", "Cho‘g‘lanma lampa qarshiligi yonganda nima uchun ortadi?", "Elektr energiyasi uchun to‘lov qaysi birlikda hisoblanadi?"]
))

L.append(dict(
 n=14, short="Turli muhitlarda elektr toki", sim="vacdiode", refs=[1, 2, 3, 4, 5], intl=["openstax2", "halliday", "atkins"], tn=["TN4", "TN8"],
 phet=[("Neon Lights & Other Discharge Lamps", "discharge-lamps"), ("Conductivity", "conductivity")],
 title="Turli muhitlarda elektr toki: vakuum, gazlar, plazma. Termoelektron emissiya. Gaz razryadi",
 goal="Termoelektron emissiya, elektronlarning metalldan chiqish ishi va vakuumdagi elektr toki, gazlarda ionlanish va rekombinatsiya, gaz razryadining volt-amper xarakteristikasi, mustaqil va nomustaqil razryad turlari hamda plazma tushunchasini o‘rganish.",
 outcomes=["chiqish ishi va termoelektron emissiyani (Richardson–Deshman formulasi) tushuntiradi;", "vakuum diod VAX ini (“3/2” qonuni va to‘yinish) tahlil qiladi;", "gazlarda ionlanish va rekombinatsiya jarayonlarini, nomustaqil va mustaqil razryadni farqlaydi;", "razryad turlari (tlovchi, uchqun, toj, yoy) va plazmaning qo‘llanilishiga misollar keltiradi."],
 plan=["Elektronlarning metalldan chiqish ishi. Termoelektron emissiya", "Vakuumda elektr toki. Vakuum diod va uning VAX i", "Gazlarda elektr toki. Ionlanish va rekombinatsiya", "Gaz razryadining to‘liq VAX i. Mustaqil va nomustaqil razryadlar, ularning turlari", "Plazma va uning qo‘llanilishi"],
 terms=["chiqish ishi A", "termoelektron emissiya", "to‘yinish toki", "“3/2” qonuni", "ionlanish energiyasi", "zarbiy ionlanish", "plazma"],
 theory=[
  ("Chiqish ishi va termoelektron emissiya", r"""<p>Metalldagi erkin elektronlarni sirtdagi potensial to‘siq ushlab turadi; elektronni metalldan chiqarish uchun kerak bo‘lgan eng kichik energiya — <b>chiqish ishi</b> \(A\) (volfram 4,5 eV, seziy 2,1 eV, oksid qoplamalar \(\sim1\) eV). Yuqori temperaturada ayrim elektronlar energiyasi \(A\) dan oshib, metalldan uchib chiqadi — <b>termoelektron emissiya</b>. To‘yinish toki zichligi Richardson–Deshman formulasi bilan beriladi:</p>
$$j_\text{to‘y}=BT^2e^{-A/kT}$$
<p>bu yerda volfram uchun tajribaviy \(B\approx6\cdot10^5\) A/(m²·K²). Temperatura 2000 K dan 2500 K ga oshsa, emissiya yuzlab marta ortadi.</p>"""),
  ("Vakuum diod", r"""<p>Vakuum diod — qizdiriladigan katod va anoddan iborat lampa; tok faqat anod potensiali musbat bo‘lganda o‘tadi (bir tomonlama o‘tkazuvchanlik — to‘g‘rilash). Kichik kuchlanishlarda katod yaqinida fazoviy zaryad buluti hosil bo‘ladi va tok Boguslavskiy–Lengmyur (“3/2”) qonuniga bo‘ysunadi:</p>
$$I_a=bU_a^{3/2}$$
<p>Katta kuchlanishda katoddan chiqqan barcha elektronlar anodga yetadi — tok to‘yinadi: \(I_\text{to‘y}=j_\text{to‘y}S_k\). VAX ni va to‘yinish tokining katod temperaturasiga bog‘liqligini o‘rganish — L23 laboratoriya ishi.</p>"""),
  ("Gazlarda elektr toki", r"""<p>Normal sharoitda gaz izolyator. Tashqi ionlovchi omil (alanga, ultrabinafsha, rentgen, radioaktiv nurlanish) neytral atomlardan elektron va musbat ionlar hosil qiladi — <b>ionlanish</b>; teskari jarayon — <b>rekombinatsiya</b>. Ionlovchi omil ta’sirida oqadigan tok — <b>nomustaqil razryad</b>: kichik kuchlanishda Om qonuniga bo‘ysunadi, kattaroq kuchlanishda to‘yinadi. Kuchlanish yanada ortganda elektronlar zarbiy ionlanish (elektron ko‘chkisi) hosil qiladi, katoddan ikkilamchi emissiya boshlanadi va razryad tashqi omilsiz davom etadi — <b>mustaqil razryad</b> (yonish kuchlanishi).</p>"""),
  ("Mustaqil razryad turlari va plazma", r"""<p><b>Tlovchi</b> razryad (past bosimda: neon reklama, lyuminessent lampalar), <b>uchqun</b> (chaqmoq, dvigatel shami), <b>toj</b> (yuqori kuchlanishli simlar, elektrofiltrlar), <b>yoy</b> (payvandlash, yoy pechlari, projektorlar). <b>Plazma</b> — ionlanish darajasi yuqori bo‘lgan, umuman olganda elektroneytral gaz; moddaning “to‘rtinchi holati”. Koinotdagi oddiy moddaning asosiy qismi plazma holatida (yulduzlar). Qo‘llanilishi: plazmali kesish, termoyadro qurilmalari (tokamak), spektral tahlilda induktiv bog‘langan plazma (ICP).</p>""")],
 chem=["Induktiv bog‘langan plazmali atom-emission va massa-spektrometriya (ICP-OES, ICP-MS) — elementlarning iz miqdorlarini aniqlashning eng sezgir usullaridan.",
       "Alangali ionlanish detektori (FID) gaz xromatografiyasida organik moddalarni aniqlaydi: yonishda hosil bo‘lgan ionlar toki o‘lchanadi.",
       "Elektrofiltrlar (toj razryadi) sanoat gazlarini changdan tozalaydi."],
 example=[("Termoemissiya", r"Volfram katod (A = 4,5 eV, B = 6·10⁵ A/(m²·K²), yuzasi 0,1 sm²) 2500 K gacha qizdirildi. To‘yinish tokini toping. 2000 K da tok necha marta kam?",
           r"\(kT=0{,}2154\) eV; \(e^{-A/kT}=e^{-20{,}89}=8{,}5\cdot10^{-10}\); \(j=6\cdot10^5\cdot6{,}25\cdot10^6\cdot8{,}5\cdot10^{-10}=3{,}2\cdot10^3\) A/m². \(I=jS=32\) mA. 2000 K da \(j\approx11\) A/m², \(I\approx0{,}11\) mA — taxminan 290 marta kam."),
          ("“3/2” qonuni", r"Diodda anod kuchlanishi 50 V bo‘lganda tok 7 mA (to‘yinishdan uzoq). 100 V da tok qancha bo‘ladi?",
           r"\(I_2=I_1(U_2/U_1)^{3/2}=7\cdot2^{1{,}5}=19{,}8\) mA (agar bu qiymat to‘yinish tokidan kichik bo‘lsa).")],
 simtask=["Katod temperaturasini 1900 K dan 2600 K gacha o‘zgartirib, to‘yinish toki qanday ortishini jadvalga yozing.", "To‘yinishdan uzoq sohada ikki nuqta tanlab, \\(I_2/I_1=(U_2/U_1)^{3/2}\\) bajarilishini tekshiring.", "Nima uchun to‘yinish toki anod kuchlanishiga bog‘liq emas? Tushuntiring."],
 mistakes=[("“Vakuumda tok o‘tishi mumkin emas, chunki u yerda zaryad yo‘q.”", "Zaryad tashuvchilarni katod beradi (termoemissiya); vakuumda elektronlar erkin harakatlanadi."),
           ("“Diod tokini cheksiz oshirish mumkin.”", "Tok katod emissiyasi bilan chegaralangan — to‘yinish toki."),
           ("“Plazma — shunchaki juda issiq gaz.”", "Plazmaning asosiy belgisi — ionlanish va kollektiv elektromagnit xossalar; past temperaturali plazma ham bor (lyuminessent lampa).")],
 ai=AI.format(t="turli muhitlarda elektr toki", b="1) Termoelektron emissiya va fotoemissiyani taqqoslab jadval tuzishga yordam ber.\n2) Python’da Richardson formulasi bo‘yicha j(T) ni 1800–2600 K oralig‘ida chizib, ln(j/T²) ning 1/T ga bog‘liqligidan chiqish ishini topadigan kod yoz."),
 quiz=[("Termoelektron emissiya nima?", ["qizdirilgan metalldan elektronlarning chiqishi", "yorug‘lik ta’sirida elektron chiqishi", "ionlarning rekombinatsiyasi", "elektrolitda ionlar harakati"], 0, "Energiya issiqlik harakatidan olinadi."),
       ("Vakuum diodning asosiy xossasi:", ["bir tomonlama o‘tkazuvchanlik", "signalni kuchaytirish", "katta sig‘im", "induktivlik"], 0, "To‘g‘rilash."),
       ("“3/2” qonuni:", [r"\(I=bU^{3/2}\)", r"\(I=U/R\)", r"\(I=bU^{2/3}\)", r"\(I=I_0e^{U}\)"], 0, "Fazoviy zaryad bilan cheklangan tok."),
       ("Katod temperaturasi oshsa, to‘yinish toki:", ["keskin ortadi", "kamayadi", "o‘zgarmaydi", "nolga tushadi"], 0, "Eksponensial bog‘lanish."),
       ("Mustaqil razryad uchun zarur jarayon:", ["zarbiy ionlanish va ikkilamchi emissiya", "tashqi ionlovchi omil", "faqat rekombinatsiya", "termoyadro sintezi"], 0, "Razryad o‘zini o‘zi ta’minlaydi."),
       ("Chaqmoq qaysi razryad turiga kiradi?", ["uchqun", "tlovchi", "toj", "yoy"], 0, "Qisqa muddatli kuchli razryad."),
       ("Elektr payvandlashda qaysi razryad ishlatiladi?", ["yoy", "toj", "tlovchi", "uchqun"], 0, "Katta tok, yuqori temperatura."),
       ("Plazma:", ["ionlangan, umuman elektroneytral gaz", "faqat musbat ionlardan iborat", "suyuq metall", "kristall"], 0, "Moddaning to‘rtinchi holati."),
       ("Chiqish ishi odatda qaysi birlikda beriladi?", ["eV", "V", "A", "W"], 0, "1 eV = 1,6·10⁻¹⁹ J."),
       ("Neon reklama lampalarida qaysi razryad?", ["tlovchi", "yoy", "uchqun", "toj"], 0, "Past bosimli gaz.")],
 blits=["Lyuminessent lampa qanday yonadi?", "Nima uchun yuqori kuchlanishli simlar atrofida tunda shu’la ko‘rinadi?", "Kineskopli televizorlarda elektronlar qayerdan olingan?", "Quyosh moddasi qaysi holatda?", "Elektr payvandlashda nima uchun ko‘zni himoya qilish kerak?"]
))

L.append(dict(
 n=15, short="Magnit maydon", sim="bfield", refs=[1, 2, 3, 4, 5], intl=["purcell", "openstax2", "halliday"], tn=["TN4", "TN6"],
 phet=[("Magnets and Electromagnets", "magnets-and-electromagnets"), ("Magnet and Compass", "magnet-and-compass")],
 title="Magnit maydon. Bio–Savar–Laplas qonuni. Amper kuchi. Lorens kuchi. Zaryadli zarralarning magnit maydondagi harakati",
 goal="Magnit maydon induksiyasi vektori, to‘g‘ri va aylanma tokning magnit maydonini hisoblash, Amper kuchi, parallel toklarning o‘zaro ta’siri, Lorens kuchi va zaryadli zarralarning bir jinsli magnit maydondagi harakatini o‘rganish.",
 outcomes=["to‘g‘ri tok, doiraviy o‘ram va solenoid maydonini hisoblaydi;", "Amper kuchining kattaligi va yo‘nalishini (chap qo‘l qoidasi) aniqlaydi;", "parallel toklarning o‘zaro ta’sir kuchini hisoblaydi;", "Lorens kuchi ta’sirida zaryadli zarra trayektoriyasi radiusi va aylanish davrini hisoblaydi."],
 plan=["Magnit maydon va uning induksiya vektori", "Bio–Savar–Laplas qonuni. To‘g‘ri va aylanma tok maydoni", "Amper kuchi. Parallel toklarning o‘zaro ta’siri", "Lorens kuchi", "Zaryadli zarralarning bir jinsli magnit maydondagi harakati. Massa-spektrometr"],
 terms=["magnit induksiya \\(\\vec B\\) (T)", "magnit doimiysi \\(\\mu_0\\)", "parma qoidasi", "Amper kuchi", "chap qo‘l qoidasi", "Lorens kuchi", "siklotron chastota"],
 theory=[
  ("Magnit maydon va induksiya vektori", r"""<p>Magnit maydon harakatlanayotgan zaryadlar (toklar) va doimiy magnitlar atrofida hosil bo‘ladi va faqat harakatlanayotgan zaryadlarga ta’sir qiladi. Uning kuch xarakteristikasi — <b>magnit induksiya</b> \(\vec B\) (tesla, T). Induksiya chiziqlari doim yopiq (magnit zaryadlar yo‘q): \(\oint\vec B\cdot d\vec S=0\). Yerning magnit maydoni \(\sim50\) mkT, uning gorizontal tashkil etuvchisi O‘zbekiston kengliklarida \(\approx25\)–28 mkT; kompas strelkasi aynan shu tashkil etuvchi bo‘ylab joylashadi.</p>"""),
  ("Bio–Savar–Laplas qonuni", r"""<p>Tok elementi \(I\,d\vec l\) hosil qiladigan maydon: \(d\vec B=\dfrac{\mu_0}{4\pi}\dfrac{I\,d\vec l\times\vec r}{r^3}\), \(\mu_0=4\pi\cdot10^{-7}\) H/m. Integrallash natijalari:</p>
$$B_\text{to‘g‘ri}=\frac{\mu_0I}{2\pi r},\qquad B_\text{o‘ram markazi}=\frac{\mu_0NI}{2R},\qquad B_\text{solenoid}=\mu_0nI$$
<p>Yo‘nalish parma (o‘ng vint) qoidasi bilan topiladi. Tangens-galvanometrda o‘ram maydoni Yer maydonining gorizontal tashkil etuvchisiga perpendikulyar bo‘ladi va strelka \(\tan\varphi=B_\text{o‘ram}/B_g\) burchakka buriladi — bundan \(B_g\) aniqlanadi (L24).</p>"""),
  ("Amper kuchi va parallel toklar", r"""<p>Magnit maydondagi tokli o‘tkazgichga ta’sir etuvchi kuch: \(d\vec F=I\,d\vec l\times\vec B\); to‘g‘ri o‘tkazgich uchun \(F=IBl\sin\alpha\), yo‘nalishi chap qo‘l qoidasi bilan aniqlanadi. Bir-biridan \(d\) masofadagi parallel toklar birlik uzunlikka \(F/l=\dfrac{\mu_0I_1I_2}{2\pi d}\) kuch bilan ta’sir qiladi: bir yo‘nalishli toklar tortishadi, qarama-qarshilari itarishadi. Elektr dvigatellari, karnaylar va magnitoelektrik o‘lchov asboblari Amper kuchiga asoslangan.</p>"""),
  ("Lorens kuchi va zarralar harakati", r"""<p>Magnit maydonda harakatlanayotgan zaryadga ta’sir etuvchi kuch:</p>
$$\vec F_L=q\vec v\times\vec B,\qquad F_L=qvB\sin\alpha$$
<p>Lorens kuchi tezlikka perpendikulyar, shuning uchun ish bajarmaydi va zarra energiyasini o‘zgartirmaydi. \(\vec v\perp\vec B\) bo‘lsa, zarra aylana bo‘ylab harakatlanadi: \(r=\dfrac{mv}{qB}\), aylanish davri \(T=\dfrac{2\pi m}{qB}\) tezlikka bog‘liq emas (siklotron prinsipi). Massa-spektrometrda bir xil energiyali ionlar trayektoriya radiusi bo‘yicha massasiga qarab ajratiladi.</p>""")],
 chem=["Massa-spektrometriya molekulyar massa va izotop tarkibini aniqlashning asosiy usuli; ionlar Lorens kuchi ta’sirida \\(m/q\\) nisbatiga qarab ajraladi.",
       "Yadro magnit rezonansi (YaMR) spektroskopiyasida kuchli magnit maydon (bir necha tesla) yadro spinlarini yo‘naltiradi — organik moddalar tuzilishini aniqlashning eng muhim usuli.",
       "Magnit aralashtirgichlar eritmani aylanuvchi magnit maydon yordamida aralashtiradi."],
 example=[("To‘g‘ri tok maydoni", r"Uzun to‘g‘ri o‘tkazgichdan 10 A tok o‘tmoqda. Undan 5 sm masofadagi magnit induksiyani toping va Yer maydoni (50 mkT) bilan solishtiring.",
           r"\(B=\frac{4\pi\cdot10^{-7}\cdot10}{2\pi\cdot0{,}05}=4\cdot10^{-5}\) T \(=40\) mkT — Yer maydoni bilan bir tartibda; shu sababli tok yaqinidagi kompas sezilarli og‘adi (Ersted tajribasi)."),
          ("Massa-spektrometr", r"Bir marta ionlangan ¹²C⁺ ioni 1000 V potensiallar farqida tezlatilib, 0,2 T maydonga perpendikulyar kirdi. Trayektoriya radiusini toping (m = 1,99·10⁻²⁶ kg).",
           r"\(v=\sqrt{2qU/m}=1{,}27\cdot10^5\) m/s. \(r=\frac{mv}{qB}=\frac{1{,}99\cdot10^{-26}\cdot1{,}27\cdot10^5}{1{,}6\cdot10^{-19}\cdot0{,}2}=7{,}9\) sm. ¹³C⁺ uchun \(r\approx8{,}2\) sm — izotoplar ajraladi.")],
 simtask=["“To‘g‘ri o‘tkazgich” rejimida I = 2 A, r = 1 sm o‘rnating va B = μ₀I/(2πr) ni tekshiring.", "Tangens-galvanometr rejimida tokni o‘zgartirib, φ ≈ 45° bo‘ladigan tokni toping va undan B_g ni hisoblang.", "O‘ramlar sonini ikki marta oshirsangiz, φ qanday o‘zgaradi? Nima uchun tg φ ∝ I?"],
 mistakes=[("“Magnit maydon tinch zaryadga ham ta’sir qiladi.”", "Magnit maydon faqat harakatlanayotgan zaryad va toklarga ta’sir qiladi."),
           ("“Lorens kuchi zarrani tezlashtiradi.”", "U tezlikka perpendikulyar, ish bajarmaydi; faqat harakat yo‘nalishini o‘zgartiradi."),
           ("“Yerning shimoliy geografik qutbi yaqinida shimoliy magnit qutb joylashgan.”", "U yerda janubiy magnit qutb joylashgan — shuning uchun kompasning shimoliy uchi o‘sha tomonga tortiladi.")],
 ai=AI.format(t="magnit maydon, Amper va Lorens kuchlari", b="1) Doiraviy o‘ram markazidagi maydonni Bio–Savar–Laplas qonunidan keltirib chiqarishga yordam ber.\n2) Python’da massa-spektrometrda ¹²C⁺, ¹³C⁺, ¹⁶O⁺ ionlarining trayektoriyalarini (yarim aylanalar) chizadigan kod yoz."),
 quiz=[("Magnit induksiyaning SI birligi:", ["tesla", "veber", "genri", "gauss"], 0, "1 T = 1 N/(A·m)."),
       ("To‘g‘ri tokdan masofa 2 marta oshsa, induksiya:", ["2 marta kamayadi", "4 marta kamayadi", "2 marta ortadi", "o‘zgarmaydi"], 0, "B ∝ 1/r."),
       ("Bir yo‘nalishdagi parallel toklar:", ["tortishadi", "itarishadi", "ta’sirlashmaydi", "aylanadi"], 0, "Amper tajribasi."),
       ("Lorens kuchining ishi:", ["nolga teng", "qvB ga teng", "mv²/2 ga teng", "qU ga teng"], 0, "Kuch tezlikka perpendikulyar."),
       ("Uzunligi 0,5 m, toki 2 A bo‘lgan o‘tkazgich 0,1 T maydonga perpendikulyar. Amper kuchi:", ["0,1 N", "1 N", "0,01 N", "10 N"], 0, "F = IBl."),
       ("Zaryadli zarraning magnit maydonda aylanish davri:", ["tezlikka bog‘liq emas", "tezlikka proporsional", "tezlikka teskari proporsional", "radiusga teng"], 0, "T = 2πm/(qB)."),
       ("Zarra tezligi 2 marta oshsa, trayektoriya radiusi:", ["2 marta ortadi", "4 marta ortadi", "o‘zgarmaydi", "2 marta kamayadi"], 0, "r = mv/(qB)."),
       ("Amper kuchining yo‘nalishi qaysi qoida bilan aniqlanadi?", ["chap qo‘l qoidasi", "parma qoidasi", "Lens qoidasi", "o‘ng qo‘l qoidasi"], 0, "Kuch, tok va maydon yo‘nalishlari bog‘lanishi."),
       ("Uzun solenoid ichidagi maydon:", [r"\(\mu_0nI\)", r"\(\mu_0I/(2\pi r)\)", r"\(\mu_0I/(2R)\)", "0"], 0, "n — birlik uzunlikdagi o‘ramlar soni."),
       ("Massa-spektrometr qaysi kuchga asoslangan?", ["Lorens kuchi", "Kulon kuchi", "Arximed kuchi", "ishqalanish kuchi"], 0, "Ionlar aylana bo‘ylab ajraladi.")],
 blits=["Ersted tajribasi nimani ko‘rsatdi?", "Qutb yog‘dusi (aurora) qanday paydo bo‘ladi?", "Elektr dvigatel qanday ishlaydi?", "Nima uchun kompas strelkasi tokli sim yaqinida buriladi?", "Magnit induksiya chiziqlari nima uchun yopiq?"]
))

L.append(dict(
 n=16, short="Elektromagnit induksiya", sim="induction", refs=[1, 2, 3, 4, 5], intl=["purcell", "openstax2", "halliday"], tn=["TN4", "TN8"],
 phet=[("Faraday's Law", "faradays-law"), ("Generator", "generator")],
 title="Elektromagnit induksiya hodisasi. Faradey qonuni. Lens qoidasi. O‘zinduksiya va o‘zaro induksiya. Magnit maydon energiyasi",
 goal="Magnit oqimi, Faradey tajribalari, elektromagnit induksiya qonuni, Lens qoidasi, induktivlik, o‘zinduksiya va o‘zaro induksiya hodisalari hamda magnit maydon energiyasini o‘rganish.",
 outcomes=["magnit oqimini hisoblaydi va uni o‘zgartirish usullarini ko‘rsatadi;", "Faradey qonuni bo‘yicha induksiya EYuK ini hisoblaydi va Lens qoidasi bilan induksion tok yo‘nalishini aniqlaydi;", "induktivlik, o‘zinduksiya EYuK i va magnit maydon energiyasini hisoblaydi;", "transformator va generator ishlashini tushuntiradi."],
 plan=["Magnit oqimi", "Faradey tajribalari. Elektromagnit induksiya qonuni", "Lens qoidasi", "Induktivlik. O‘zinduksiya hodisasi. O‘zaro induksiya", "Magnit maydon energiyasi"],
 terms=["magnit oqimi \\(\\Phi\\) (Wb)", "induksiya EYuK", "Lens qoidasi", "induktivlik L (H)", "o‘zinduksiya", "o‘zaro induksiya", "uyurmaviy (Fuko) toklar"],
 theory=[
  ("Magnit oqimi va Faradey qonuni", r"""<p>Sirt orqali magnit oqimi \(\Phi=\int\vec B\cdot d\vec S\), bir jinsli maydonda \(\Phi=BS\cos\alpha\) (veber, Wb = T·m²). Faradey (1831) yopiq kontur orqali o‘tuvchi magnit oqimi o‘zgarganda konturda tok paydo bo‘lishini aniqladi — <b>elektromagnit induksiya</b>. Induksiya EYuK i:</p>
$$\mathcal E_i=-N\frac{d\Phi}{dt}$$
<p>Oqim maydon \(B\), yuza \(S\) yoki burchak \(\alpha\) o‘zgarishi hisobiga o‘zgarishi mumkin. Maydonda \(v\) tezlik bilan harakatlanayotgan \(l\) uzunlikdagi o‘tkazgichda \(\mathcal E=Blv\).</p>"""),
  ("Lens qoidasi", r"""<p>Induksion tok shunday yo‘nalganki, uning magnit maydoni o‘zini vujudga keltirgan oqim o‘zgarishiga qarshilik qiladi (formuladagi minus ishorasi). Qoida energiya saqlanish qonunining natijasi: magnitni g‘altakka yaqinlashtirish uchun itarish kuchiga qarshi ish bajarish kerak va aynan shu ish induksion tokning elektr energiyasiga aylanadi. Massiv o‘tkazgichlarda uyurmaviy (Fuko) toklar hosil bo‘ladi — induksion pechlar va elektromagnit tormozlar shunga asoslangan.</p>"""),
  ("O‘zinduksiya va o‘zaro induksiya", r"""<p>Konturdagi tokning o‘zi hosil qilgan oqim \(\Phi=LI\); \(L\) — induktivlik (genri, H). Solenoid uchun \(L=\mu\mu_0n^2V\). Tok o‘zgarganda o‘zinduksiya EYuK i paydo bo‘ladi:</p>
$$\mathcal E_s=-L\frac{dI}{dt}$$
<p>U tok o‘zgarishiga qarshilik qiladi: zanjir ulanganda tok asta ortadi, uzilganda esa kuchli uchqun paydo bo‘lishi mumkin. Ikki kontur orasida o‘zaro induksiya: \(\mathcal E_2=-M\,dI_1/dt\) — transformatorning ishlash asosi (\(U_2/U_1\approx N_2/N_1\)).</p>"""),
  ("Magnit maydon energiyasi", r"""<p>Tokli g‘altakda energiya to‘planadi:</p>
$$W=\frac{LI^2}{2},\qquad w=\frac{B^2}{2\mu\mu_0}$$
<p>Bu energiya zanjir uzilganda o‘zinduksiya EYuK i orqali ajraladi. Masalan, MRT tomografining o‘ta o‘tkazuvchan magnitida (3 T) megajoullar tartibidagi energiya to‘plangan.</p>""")],
 chem=["Induksion qizdirish metallarni kontaktsiz, tez va toza eritish imkonini beradi.",
       "YaMR spektrometrida yadrolar presessiyasi qabul qiluvchi g‘altakda induksiya EYuK ini hosil qiladi — signal aynan Faradey qonuni bo‘yicha qayd qilinadi.",
       "Elektromagnit sarf o‘lchagichlarida o‘tkazuvchan suyuqlik magnit maydonda harakatlanib EYuK hosil qiladi: \\(\\mathcal E=Bdv\\)."],
 example=[("Aylanayotgan ramka", r"Yuzasi 100 sm², o‘ramlari 200 ta bo‘lgan ramka 0,5 T maydonda 50 ayl/s chastota bilan aylanmoqda. Maksimal EYuK ni toping.",
           r"\(\Phi=BS\cos\omega t\), \(\mathcal E=NBS\omega\sin\omega t\). \(\mathcal E_\text{max}=200\cdot0{,}5\cdot0{,}01\cdot2\pi\cdot50=314\) V — o‘zgaruvchan tok generatorining prinsipi."),
          ("O‘zinduksiya", r"Induktivligi 0,2 H bo‘lgan g‘altakdagi tok 0,01 s da 5 A dan 0 gacha tekis kamaydi. O‘zinduksiya EYuK i va g‘altakdagi boshlang‘ich energiyani toping.",
           r"\(\mathcal E_s=L\,\Delta I/\Delta t=0{,}2\cdot500=100\) V. \(W=LI^2/2=2{,}5\) J.")],
 simtask=["Magnit tezligini ikki marta oshiring: ε_max qanday o‘zgaradi? Faradey qonuni bilan tushuntiring.", "O‘ramlar sonini o‘zgartirib, ε_max ∝ N ekanini tekshiring.", "Magnit g‘altakka kirayotganda va chiqayotganda ε ishorasi nima uchun teskari? Lens qoidasi bilan izohlang."],
 mistakes=[("“Kuchli magnit g‘altak ichida tinch tursa ham tok hosil qiladi.”", "Induksiya uchun oqim o‘zgarishi kerak; o‘zgarmas oqim EYuK hosil qilmaydi."),
           ("“Induksion tok har doim magnitni tortadi.”", "Lens qoidasiga ko‘ra u harakatga qarshilik qiladi: yaqinlashayotgan magnitni itaradi, uzoqlashayotganini tortadi."),
           ("“Transformator o‘zgarmas tok kuchlanishini ham o‘zgartiradi.”", "O‘zgarmas tok o‘zgarmas oqim hosil qiladi — ikkilamchi chulg‘amda EYuK bo‘lmaydi.")],
 ai=AI.format(t="elektromagnit induksiya", b="1) Lens qoidasining energiya saqlanish qonunidan kelib chiqishini misol bilan tushuntirishga yordam ber.\n2) Python’da g‘altakdan o‘tayotgan magnit uchun Φ(t) va ε(t) ni sonli differensiallab chizadigan kod yoz va ∫ε dt = 0 ekanini tekshir."),
 quiz=[("Magnit oqimining birligi:", ["Wb", "T", "H", "A/m"], 0, "1 Wb = 1 T·m²."),
       ("Faradey qonuni:", [r"\(\mathcal E=-N\,d\Phi/dt\)", r"\(\mathcal E=IR\)", r"\(\mathcal E=-L\,I\)", r"\(F=qvB\)"], 0, "Induksiya EYuK i."),
       ("Oqim 0,1 s da 0,02 Wb ga tekis o‘zgardi, N = 100. EYuK:", ["20 V", "0,2 V", "2 V", "200 V"], 0, "100·0,02/0,1."),
       ("Lens qoidasi qaysi qonunning natijasi?", ["energiya saqlanishi", "zaryad saqlanishi", "impuls saqlanishi", "Kulon qonuni"], 0, "Induksion tok harakatga qarshilik qiladi."),
       ("Induktivlikning birligi:", ["genri", "farad", "tesla", "veber"], 0, "1 H = 1 Wb/A."),
       ("G‘altakdagi tok 2 marta oshsa, magnit maydon energiyasi:", ["4 marta ortadi", "2 marta ortadi", "o‘zgarmaydi", "2 marta kamayadi"], 0, "W = LI²/2."),
       ("Transformator birlamchi chulg‘amida 100, ikkilamchisida 1000 o‘ram, U₁ = 22 V. U₂:", ["220 V", "2,2 V", "22 V", "2200 V"], 0, "U₂/U₁ = N₂/N₁."),
       ("Maydonda harakatlanayotgan o‘tkazgichdagi EYuK:", [r"\(Blv\)", r"\(Bl/v\)", r"\(BIl\)", r"\(qvB\)"], 0, "Lorens kuchi natijasi."),
       ("Zanjir uzilganda uchqun chiqishiga sabab:", ["o‘zinduksiya", "o‘zaro induksiya", "termoemissiya", "Joul issiqligi"], 0, "Tok keskin kamayadi, dI/dt katta."),
       ("Ramkaning aylanish chastotasi 2 marta oshsa, maksimal EYuK:", ["2 marta ortadi", "4 marta ortadi", "o‘zgarmaydi", "2 marta kamayadi"], 0, "ℰ = NBSω.")],
 blits=["Velosiped dinamosi qanday ishlaydi?", "Induksion plita idishni qanday isitadi?", "Metall detektor qaysi hodisaga asoslangan?", "Nima uchun transformator o‘zagi yupqa plastinalardan yig‘iladi?", "Simsiz zaryadlash qanday ishlaydi?"]
))

L.append(dict(
 n=17, short="Elektromagnit tebranishlar va to‘lqinlar", sim="rlc", refs=[1, 2, 3, 4, 5], intl=["openstax2", "purcell", "feynman"], tn=["TN4"],
 phet=[("Circuit Construction Kit: AC", "circuit-construction-kit-ac"), ("Radio Waves & Electromagnetic Fields", "radio-waves")],
 title="Elektromagnit tebranishlar va to‘lqinlar. Tebranish konturi. Tomson formulasi. Elektromagnit to‘lqinlarning qo‘llanilishi",
 goal="Tebranish konturidagi fizik jarayonlar, erkin elektromagnit tebranishlar va Tomson formulasi, so‘nuvchi tebranishlar, elektromagnit to‘lqinlarning hosil bo‘lishi, xossalari, tarqalish tezligi va qo‘llanilishini o‘rganish.",
 outcomes=["tebranish konturida energiyaning elektr va magnit energiyalar orasida aylanishini tushuntiradi;", "Tomson formulasi bo‘yicha davr va chastotani hisoblaydi;", "so‘nish koeffitsiyenti va asllikni hisoblaydi, rezonans egri chizig‘ini tahlil qiladi;", "elektromagnit to‘lqin tezligi, to‘lqin uzunligi va shkala bo‘yicha qo‘llanilishini izohlaydi."],
 plan=["Tebranish konturidagi fizik jarayonlar", "Erkin elektromagnit tebranishlar. Tomson formulasi", "So‘nuvchi va majburiy tebranishlar. Rezonans", "Elektromagnit to‘lqinlar va ularning tarqalish tezligi", "Elektromagnit to‘lqinlar shkalasi va qo‘llanilishi"],
 terms=["tebranish konturi", "Tomson formulasi", "asllik Q", "so‘nish koeffitsiyenti \\(\\beta\\)", "elektromagnit to‘lqin", "yorug‘lik tezligi c", "to‘lqinlar shkalasi"],
 theory=[
  ("Tebranish konturi", r"""<p>Kondensator \(C\) va g‘altak \(L\) dan iborat zanjir — tebranish konturi. Zaryadlangan kondensator g‘altak orqali razryadlanadi: elektr maydon energiyasi \(q^2/2C\) magnit maydon energiyasi \(LI^2/2\) ga aylanadi, so‘ng aksincha. Qarshilik bo‘lmasa, to‘liq energiya saqlanadi: \(\dfrac{q^2}{2C}+\dfrac{LI^2}{2}=\text{const}\). Bu mexanik tebranishlarning to‘liq o‘xshashi: \(q\leftrightarrow x\), \(L\leftrightarrow m\), \(1/C\leftrightarrow k\).</p>"""),
  ("Tomson formulasi", r"""<p>Kirxgof qoidasidan \(L\ddot q+q/C=0\) — garmonik tebranish tenglamasi kelib chiqadi. Uning yechimi va davri:</p>
$$q=q_0\cos(\omega_0t+\varphi_0),\qquad \omega_0=\frac{1}{\sqrt{LC}},\qquad T=2\pi\sqrt{LC}$$
<p>Tok zaryaddan faza bo‘yicha \(\pi/2\) ga oldinda. Masalan, \(L=10\) mH, \(C=1\) mkF da \(T=0{,}63\) ms, \(f_0\approx1{,}6\) kHz.</p>"""),
  ("So‘nuvchi tebranishlar va rezonans", r"""<p>Aktiv qarshilik \(R\) energiyani issiqlikka aylantiradi: \(q=q_0e^{-\beta t}\cos\omega t\), \(\beta=R/2L\), \(\omega=\sqrt{\omega_0^2-\beta^2}\). Kontur sifati — asllik \(Q=\frac1R\sqrt{L/C}\). \(R\ge2\sqrt{L/C}\) bo‘lsa, tebranishlar yo‘qoladi (aperiodik rejim). Tashqi o‘zgaruvchan EYuK ta’sirida majburiy tebranishlar yuzaga keladi; \(\omega=\omega_0\) da tok amplitudasi maksimal — <b>rezonans</b>; rezonans egri chizig‘ining kengligi \(\Delta\omega\approx\omega_0/Q\). Radiopriyomnik konturi aynan shu tarzda kerakli stansiyani tanlaydi.</p>"""),
  ("Elektromagnit to‘lqinlar", r"""<p>Maksvell nazariyasiga ko‘ra o‘zgaruvchan elektr maydon magnit maydonni, o‘zgaruvchan magnit maydon esa elektr maydonni hosil qiladi — ular fazoda to‘lqin sifatida tarqaladi (Gers tajribasi, 1888). Elektromagnit to‘lqin ko‘ndalang: \(\vec E\perp\vec B\perp\vec v\), \(E=cB\). Vakuumda va muhitda tezligi:</p>
$$c=\frac{1}{\sqrt{\varepsilon_0\mu_0}}=2{,}998\cdot10^8\ \text{m/s},\qquad v=\frac{c}{\sqrt{\varepsilon\mu}},\qquad \lambda=\frac cf$$
<p>Shkala: radioto‘lqinlar (\(\lambda>1\) mm), infraqizil, ko‘rinadigan yorug‘lik (380–760 nm), ultrabinafsha, rentgen, gamma-nurlanish. Qo‘llanilishi: radio va televideniye, mobil aloqa (Wi-Fi 2,4 GHz, \(\lambda=12{,}5\) sm), mikroto‘lqinli pech, radiolokatsiya.</p>""")],
 chem=["Mikroto‘lqinli sintez: 2,45 GHz nurlanish qutbli molekulalarni (suv) tebratib, reaksiya aralashmasini tez va bir tekis isitadi.",
       "Spektroskopiyaning har bir turi EM shkalaning ma’lum sohasi bilan bog‘liq: radio — YaMR, mikroto‘lqin — aylanma, IQ — tebranma, UB va ko‘rinadigan — elektron o‘tishlar, rentgen — kristall tuzilishi.",
       "Tebranish konturi va rezonans dielektrometrik o‘lchash asboblarining asosi."],
 example=[("Radiopriyomnik konturi", r"Kontur induktivligi 0,25 mH. 1 MHz chastotali stansiyani qabul qilish uchun kondensator sig‘imi qancha bo‘lishi kerak? To‘lqin uzunligi qancha?",
           r"\(C=\frac{1}{4\pi^2f^2L}=\frac{1}{39{,}5\cdot10^{12}\cdot2{,}5\cdot10^{-4}}\approx101\) pF. \(\lambda=c/f=300\) m (o‘rta to‘lqinlar)."),
          ("Kontur energiyasi", r"Konturda \(C=2\) mkF kondensator 100 V gacha zaryadlangan, \(L=5\) mH. Maksimal tok va tebranish chastotasini toping.",
           r"Energiya saqlanishi: \(CU_0^2/2=LI_0^2/2\Rightarrow I_0=U_0\sqrt{C/L}=100\sqrt{4\cdot10^{-4}}=2\) A. \(f=\frac{1}{2\pi\sqrt{LC}}=\frac{1}{2\pi\cdot10^{-4}}\approx1{,}59\) kHz.")],
 simtask=["L = 10 mH, C = 1 mkF o‘rnating va davrni Tomson formulasi bilan tekshiring.", "R ni oshirib, tebranishlar qachon aperiodik bo‘lishini toping va \\(R=2\\sqrt{L/C}\\) bilan solishtiring.", "Rezonans egri chizig‘ining kengligi R ga qanday bog‘liq? Asllik Q ni o‘qing."],
 mistakes=[("“Kontur tebranish chastotasi kondensator zaryadiga bog‘liq.”", "Chastota faqat L va C ga bog‘liq: \\(\\omega_0=1/\\sqrt{LC}\\)."),
           ("“Elektromagnit to‘lqin tarqalishi uchun muhit kerak.”", "EM to‘lqinlar vakuumda ham tarqaladi (Quyosh nuri)."),
           ("“Radioto‘lqin va yorug‘lik — turli tabiatli.”", "Ikkalasi ham elektromagnit to‘lqin, faqat chastotasi farq qiladi.")],
 ai=AI.format(t="elektromagnit tebranishlar va to‘lqinlar", b="1) Mexanik va elektromagnit tebranishlar o‘xshashligi jadvalini (x↔q, m↔L, k↔1/C, ...) tuzishga yordam ber.\n2) Python’da RLC konturi tenglamasini scipy.integrate.solve_ivp bilan yechib, q(t) va energiyalar balansini chizadigan kod yoz."),
 quiz=[("Tomson formulasi:", [r"\(T=2\pi\sqrt{LC}\)", r"\(T=2\pi\sqrt{L/C}\)", r"\(T=2\pi LC\)", r"\(T=1/(LC)\)"], 0, "Erkin tebranishlar davri."),
       ("Kondensator sig‘imi 4 marta oshirilsa, kontur davri:", ["2 marta ortadi", "4 marta ortadi", "2 marta kamayadi", "o‘zgarmaydi"], 0, r"\(T\propto\sqrt C\)."),
       ("Vakuumda elektromagnit to‘lqin tezligi:", ["3·10⁸ m/s", "3·10⁵ m/s", "340 m/s", "cheksiz"], 0, r"\(c=1/\sqrt{\varepsilon_0\mu_0}\)."),
       ("100 MHz radioto‘lqin uzunligi:", ["3 m", "30 m", "0,3 m", "300 m"], 0, "λ = c/f."),
       ("Elektromagnit to‘lqinda \\(\\vec E\\) va \\(\\vec B\\) vektorlar:", ["o‘zaro va tarqalish yo‘nalishiga perpendikulyar", "parallel", "tarqalish yo‘nalishi bo‘ylab", "bir-biriga 45° burchak ostida"], 0, "Ko‘ndalang to‘lqin."),
       ("Ideal konturda energiya:", ["elektr va magnit energiya orasida aylanadi", "faqat kondensatorda saqlanadi", "issiqlikka aylanadi", "to‘liq nurlanadi"], 0, "R = 0."),
       ("Asllik Q oshganda rezonans egri chizig‘i:", ["torayadi", "kengayadi", "yo‘qoladi", "chapga siljiydi"], 0, "Δω ≈ ω₀/Q."),
       ("Qaysi nurlanishning to‘lqin uzunligi eng kichik?", ["gamma-nurlanish", "radioto‘lqin", "infraqizil", "ko‘rinadigan yorug‘lik"], 0, "Eng katta chastota."),
       ("Elektromagnit to‘lqinlarni tajribada birinchi bo‘lib kim hosil qilgan?", ["Gers", "Maksvell", "Faradey", "Ersted"], 0, "1888-yil."),
       ("Mikroto‘lqinli pech chastotasi 2,45 GHz. To‘lqin uzunligi:", ["≈12 sm", "≈1,2 m", "≈1,2 mm", "≈12 m"], 0, "λ = c/f.")],
 blits=["Nima uchun liftda mobil aloqa yomonlashadi?", "Radiopriyomnikni stansiyaga “sozlash” nimani anglatadi?", "Yorug‘lik tezligini birinchi kim va qanday o‘lchagan?", "Nima uchun mikroto‘lqinli pechga metall idish qo‘yilmaydi?", "Kontur tebranishlari nima uchun so‘nadi?"]
))

L.append(dict(
 n=18, short="O‘zgaruvchan tok qonunlari", sim="ac", refs=[1, 2, 3, 4, 5], intl=["openstax2", "halliday", "young"], tn=["TN4", "TN8"],
 phet=[("Circuit Construction Kit: AC", "circuit-construction-kit-ac"), ("Generator", "generator")],
 title="O‘zgaruvchan tok qonunlari. Aktiv, induktiv va sig‘im qarshiliklar. O‘zgaruvchan tok quvvati. Tok generatorlari",
 goal="O‘zgaruvchan tokning amplituda va ta’sir etuvchi qiymatlarini, aktiv, induktiv va sig‘im qarshiliklarni, to‘la qarshilikni, vektor diagrammalarni, kuchlanishlar rezonansini, o‘zgaruvchan tok quvvati va quvvat koeffitsiyentini hamda tok generatorlarining ishlash prinsipini o‘rganish.",
 outcomes=["o‘zgaruvchan tokning amplituda va ta’sir etuvchi qiymatlarini bog‘laydi;", "induktiv va sig‘im qarshiliklarni hisoblaydi, vektor diagramma quradi;", "ketma-ket RLC zanjirining to‘la qarshiligi, faza siljishi va rezonans chastotasini hisoblaydi;", "aktiv quvvat va quvvat koeffitsiyentini hisoblaydi, generator ishlashini tushuntiradi."],
 plan=["O‘zgaruvchan tok. Amplituda va ta’sir etuvchi qiymatlar", "Aktiv qarshilik, g‘altak va kondensator o‘zgaruvchan tok zanjirida", "Ketma-ket RLC zanjir. To‘la qarshilik. Vektor diagrammalar. Rezonans", "O‘zgaruvchan tok quvvati. Quvvat koeffitsiyenti", "Tok generatorlari. Uch fazali tok. Elektr energiyasini uzatish"],
 terms=["ta’sir etuvchi qiymat \\(U_m/\\sqrt2\\)", "induktiv qarshilik \\(X_L=\\omega L\\)", "sig‘im qarshilik \\(X_C=1/(\\omega C)\\)", "to‘la qarshilik Z", "faza siljishi \\(\\varphi\\)", "quvvat koeffitsiyenti \\(\\cos\\varphi\\)", "kuchlanishlar rezonansi"],
 theory=[
  ("Amplituda va ta’sir etuvchi qiymatlar", r"""<p>Sinusoidal o‘zgaruvchan tok: \(i=I_m\sin\omega t\), \(u=U_m\sin(\omega t+\varphi)\). Ta’sir etuvchi (effektiv) qiymat — aktiv qarshilikda bir xil issiqlik ajratadigan o‘zgarmas tok qiymati:</p>
$$I=\frac{I_m}{\sqrt2},\qquad U=\frac{U_m}{\sqrt2}$$
<p>Tarmoqdagi “220 V” — ta’sir etuvchi qiymat; amplituda \(U_m=311\) V, chastota 50 Hz. Ampermetr va voltmetrlar ta’sir etuvchi qiymatlarni ko‘rsatadi.</p>"""),
  ("R, L va C o‘zgaruvchan tok zanjirida", r"""<p>Aktiv qarshilikda tok va kuchlanish bir fazada. G‘altakda kuchlanish tokdan \(\pi/2\) oldinda, qarshiligi \(X_L=\omega L\) chastota bilan ortadi. Kondensatorda kuchlanish tokdan \(\pi/2\) orqada, qarshiligi \(X_C=1/(\omega C)\) chastota bilan kamayadi (o‘zgarmas tokni o‘tkazmaydi). Bu qarshiliklar reaktiv: o‘rtacha energiya iste’mol qilmaydi, faqat manba va maydon orasida energiya almashadi.</p>"""),
  ("Ketma-ket RLC zanjir va rezonans", r"""<p>Vektor (fazor) diagrammada \(U_R\) tok bo‘ylab, \(U_L\) yuqoriga, \(U_C\) pastga yo‘naladi. Natijada:</p>
$$Z=\sqrt{R^2+\left(\omega L-\frac{1}{\omega C}\right)^2},\qquad I=\frac UZ,\qquad \tan\varphi=\frac{\omega L-1/(\omega C)}{R}$$
<p>\(\omega L=1/(\omega C)\), ya’ni \(\omega_0=1/\sqrt{LC}\) da <b>kuchlanishlar rezonansi</b> kuzatiladi: \(Z=R\) minimal, tok maksimal, \(\varphi=0\), \(U_L\) va \(U_C\) esa alohida olinganda tarmoq kuchlanishidan ancha katta bo‘lishi mumkin.</p>"""),
  ("Quvvat. Generatorlar", r"""<p>O‘zgaruvchan tok zanjirida aktiv (o‘rtacha) quvvat \(P=UI\cos\varphi\); \(\cos\varphi\) — quvvat koeffitsiyenti. Kichik \(\cos\varphi\) da bir xil quvvat uchun katta tok kerak va simlardagi isrof ortadi; shuning uchun sanoatda kompensatsion kondensatorlar o‘rnatiladi. <b>Generator</b> — magnit maydonda aylanayotgan chulg‘am (yoki aylanuvchi magnit): \(\mathcal E=NBS\omega\sin\omega t\). Elektr stansiyalarida uch fazali tok ishlab chiqariladi; energiya yuqori kuchlanishda uzatiladi, chunki simlardagi isrof \(I^2R\) tok kvadratiga proporsional.</p>""")],
 chem=["Elektrokimyoviy impedans spektroskopiyasi (EIS) elektrod–eritma chegarasini R va C elementli ekvivalent sxema bilan tavsiflaydi.",
       "Konduktometriyada o‘zgaruvchan tok ishlatiladi: o‘zgarmas tok elektrodlarda elektroliz va qutblanishga olib kelardi.",
       "Elektroliz va galvanotexnikada o‘zgaruvchan tok to‘g‘rilagichlar (diodlar) orqali o‘zgarmas tokka aylantiriladi."],
 example=[("RLC zanjir", r"R = 40 Ω, L = 0,2 H, C = 100 mkF ketma-ket 220 V, 50 Hz tarmoqqa ulangan. \(X_L\), \(X_C\), Z, I, cos φ va aktiv quvvatni toping.",
           r"\(X_L=2\pi\cdot50\cdot0{,}2=62{,}8\) Ω; \(X_C=\frac{1}{2\pi\cdot50\cdot10^{-4}}=31{,}8\) Ω. \(Z=\sqrt{40^2+31^2}=50{,}6\) Ω. \(I=4{,}35\) A. \(\cos\varphi=40/50{,}6=0{,}79\). \(P=UI\cos\varphi=756\) W (\(=I^2R\))."),
          ("Rezonans chastotasi", r"Yuqoridagi zanjirda qaysi chastotada rezonans bo‘ladi va bunda tok qancha?",
           r"\(f_0=\frac{1}{2\pi\sqrt{0{,}2\cdot10^{-4}}}=35{,}6\) Hz. Rezonansda \(Z=R=40\) Ω, \(I=5{,}5\) A, \(U_L=U_C=I\cdot X_L(f_0)=5{,}5\cdot44{,}7\approx246\) V — tarmoq kuchlanishidan katta.")],
 simtask=["1-misol qiymatlarini kiriting va Z, I, cos φ ni tekshiring.", "Chastotani o‘zgartirib, rezonansni toping: faza siljishi qanday o‘zgaradi?", "C ni kamaytirib, tok kuchlanishdan oldinga o‘tadigan rejimni hosil qiling va vektor diagrammani tushuntiring."],
 mistakes=[("“Kondensator o‘zgaruvchan tokni o‘tkazmaydi.”", "Kondensator o‘zgarmas tokni o‘tkazmaydi; o‘zgaruvchan tok zaryadlanish-razryadlanish orqali o‘tadi."),
           ("“Quvvat har doim U·I ga teng.”", "Aktiv quvvat \\(UI\\cos\\varphi\\); UI — to‘la quvvat (V·A)."),
           ("“220 V — kuchlanishning maksimal qiymati.”", "Bu ta’sir etuvchi qiymat; amplituda 311 V.")],
 ai=AI.format(t="o‘zgaruvchan tok zanjirlari", b="1) Ketma-ket RLC zanjir uchun vektor diagramma qurishni bosqichma-bosqich tushuntirishga yordam ber.\n2) Python’da kompleks sonlar (j) yordamida Z(f) va φ(f) ni 10–200 Hz oralig‘ida hisoblab, rezonansni grafikda ko‘rsat."),
 quiz=[("Tarmoq kuchlanishining ta’sir etuvchi qiymati 220 V. Amplituda:", ["≈311 V", "220 V", "≈156 V", "440 V"], 0, "U√2."),
       ("Chastota oshganda induktiv qarshilik:", ["ortadi", "kamayadi", "o‘zgarmaydi", "nolga teng bo‘ladi"], 0, "X_L = ωL."),
       ("Chastota oshganda sig‘im qarshiligi:", ["kamayadi", "ortadi", "o‘zgarmaydi", "cheksiz bo‘ladi"], 0, "X_C = 1/(ωC)."),
       ("Kondensatorda kuchlanish tokdan:", ["π/2 ga orqada", "π/2 ga oldinda", "bir fazada", "π ga orqada"], 0, "Tok zaryad o‘zgarishi bilan belgilanadi."),
       ("R = 30 Ω, X_L − X_C = 40 Ω. To‘la qarshilik:", ["50 Ω", "70 Ω", "10 Ω", "35 Ω"], 0, "√(900 + 1600)."),
       ("Rezonansda ketma-ket RLC zanjirida:", ["Z = R, φ = 0", "Z = 0", "tok minimal", "φ = 90°"], 0, "Reaktiv qarshiliklar kompensatsiyalanadi."),
       ("U = 220 V, I = 5 A, cos φ = 0,8. Aktiv quvvat:", ["880 W", "1100 W", "176 W", "1375 W"], 0, "P = UIcos φ."),
       ("Elektr energiyasini uzoqqa yuqori kuchlanishda uzatish sababi:", ["simlardagi isrofni kamaytirish", "xavfsizlik", "chastotani oshirish", "sig‘imni kamaytirish"], 0, "P_isrof = I²R."),
       ("Sof induktivlik ulangan zanjirdagi o‘rtacha quvvat:", ["nolga teng", "UI ga teng", "I²X_L ga teng", "maksimal"], 0, "cos 90° = 0."),
       ("O‘zbekiston elektr tarmog‘i chastotasi:", ["50 Hz", "60 Hz", "100 Hz", "400 Hz"], 0, "Yevropa standarti.")],
 blits=["Nima uchun lampochka 50 Hz da miltillashi ko‘zga sezilmaydi?", "Uch fazali tok nima uchun qulay?", "Quvvat koeffitsiyentini oshirish nima uchun kerak?", "Kondensator o‘zgaruvchan tokni “o‘tkazishi” nimani anglatadi?", "Transformator nima uchun faqat o‘zgaruvchan tokda ishlaydi?"]
))
