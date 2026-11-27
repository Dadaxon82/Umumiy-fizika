"""IV modul. Optika: M19–M24 ma'ruzalar mazmuni."""
from lec_mex import AI

L = []

L.append(dict(
 n=19, short="Yorug‘lik interferensiyasi", sim="young", refs=[1, 2, 3, 4, 5], intl=["hecht", "openstax3", "halliday"], tn=["TN9"],
 phet=[("Wave Interference", "wave-interference")],
 title="Yorug‘likning elektromagnit to‘lqin tabiati. Korpuskulyar-to‘lqin dualizm. Yorug‘lik interferensiyasi. Yupqa pardalar. Nyuton halqalari",
 goal="Yorug‘likning korpuskulyar-to‘lqin dualizmini, kogerentlik va interferensiya shartlarini, interferensiyani kuzatish usullarini (Yung tajribasi, Frenel ko‘zgulari), yupqa pardalardagi interferensiya va Nyuton halqalarini o‘rganish.",
 outcomes=["kogerent manbalar va optik yo‘llar farqi tushunchalarini qo‘llaydi;", "interferensiya maksimum va minimum shartlarini yozadi, Yung tajribasida polosalar kengligini hisoblaydi;", "yupqa parda va Nyuton halqalaridagi interferensiyani tushuntiradi va hisoblaydi;", "interferensiyaning texnikada qo‘llanilishiga (optikani ma’rifatlash, interferometrlar) misollar keltiradi."],
 plan=["Yorug‘likning tabiati. Korpuskulyar-to‘lqin dualizm", "Kogerentlik. Optik yo‘llar farqi. Interferensiya shartlari", "Interferensiyani kuzatish usullari: Yung tajribasi, Frenel ko‘zgulari va biprizmasi", "Yupqa pardalardagi interferensiya", "Nyuton halqalari. Interferensiyaning qo‘llanilishi"],
 terms=["kogerentlik", "optik yo‘l uzunligi nl", "optik yo‘llar farqi \\(\\Delta\\)", "interferensiya maksimumi", "polosalar kengligi", "yupqa parda", "Nyuton halqalari"],
 theory=[
  ("Yorug‘likning tabiati", r"""<p>Yorug‘lik — to‘lqin uzunligi 380–760 nm bo‘lgan elektromagnit to‘lqin; vakuumdagi tezligi \(c\), muhitda \(v=c/n\) (\(n\) — sindirish ko‘rsatkichi). Interferensiya, difraksiya va qutblanish yorug‘likning <b>to‘lqin</b> tabiatini, fotoeffekt va Kompton effekti esa <b>korpuskulyar</b> (foton) tabiatini ko‘rsatadi. Bu ikki xossa bir-birini to‘ldiradi — korpuskulyar-to‘lqin dualizm: foton energiyasi \(E=h\nu\), impulsi \(p=h/\lambda\) (M23).</p>"""),
  ("Kogerentlik va interferensiya shartlari", r"""<p>Interferensiya — kogerent to‘lqinlar qo‘shilganda intensivlikning fazoda qayta taqsimlanishi: ba’zi joylarda kuchayish (maksimum), boshqalarida susayish (minimum). <b>Kogerent</b> to‘lqinlarning chastotasi bir xil va fazalar farqi vaqt bo‘yicha o‘zgarmas. Optik yo‘l uzunligi \(L=nl\); optik yo‘llar farqi \(\Delta=n_2l_2-n_1l_1\). Shartlar:</p>
$$\Delta=m\lambda\ \text{(maksimum)},\qquad \Delta=\left(m+\tfrac12\right)\lambda\ \text{(minimum)},\qquad m=0,\pm1,\pm2,\dots$$
<p>Ikki to‘lqin qo‘shilganda \(I=I_1+I_2+2\sqrt{I_1I_2}\cos\delta\), bu yerda \(\delta=2\pi\Delta/\lambda\).</p>"""),
  ("Yung tajribasi", r"""<p>Oddiy manbalar kogerent emas, shuning uchun bitta manba yorug‘ligi ikkiga bo‘linadi: Yung tajribasida (1801) ikki tor tirqish, Frenel ko‘zgulari va biprizmasida esa manbaning ikki mavhum tasviri hosil qilinadi. Tirqishlar orasidagi masofa \(d\), ekrangacha masofa \(L\gg d\) bo‘lsa, ekrandagi \(y\) nuqta uchun \(\Delta=yd/L\). Bundan:</p>
$$y_m=m\frac{\lambda L}{d},\qquad \Delta y=\frac{\lambda L}{d}$$
<p>Masalan, \(\lambda=600\) nm, \(d=0{,}5\) mm, \(L=1\) m da polosalar kengligi 1,2 mm. Oq yorug‘likda markaziy polosa oq, qolganlari rangli bo‘ladi.</p>"""),
  ("Yupqa pardalar va Nyuton halqalari", r"""<p>Qalinligi \(d\), sindirish ko‘rsatkichi \(n\) bo‘lgan pardaning ikki sirtidan qaytgan nurlar interferensiyalanadi: \(\Delta=2d\sqrt{n^2-\sin^2i}\pm\lambda/2\) (optik zichroq muhitdan qaytishda yarim to‘lqin yo‘qotiladi). Sovun pufagi va suv ustidagi neft pardasining rangdorligi shu bilan izohlanadi. Yassi-qavariq linza shisha plastinkaga qo‘yilganda havo qatlami halqasimon teng qalinlik polosalarini beradi — <b>Nyuton halqalari</b>; qaytgan yorug‘likda qorong‘i halqalar radiusi \(r_m=\sqrt{mR\lambda}\).</p>
<p>Qo‘llanilishi: optikani ma’rifatlash (aks ettirishni kamaytiruvchi qoplamalar, qalinligi \(d=\lambda/(4n)\)), sirt sifatini nazorat qilish, interferometrlar (Maykelson, Fabri–Pero).</p>""")],
 chem=["Yupqa qatlamlar (oksid yoki polimer qoplama) qalinligini interferensiya ranglari va ellipsometriya orqali nanometr aniqlikda o‘lchash mumkin.",
       "IQ Furye-spektrometrlarining (FTIR) asosida Maykelson interferometri yotadi — zamonaviy kimyoviy tahlilning asosiy asbobi.",
       "Antirefleks qoplamalar kimyoviy usullarda (CVD, zol-gel) hosil qilinadi va qalinligi interferensiya shartiga ko‘ra tanlanadi."],
 example=[("Yung tajribasi", r"Tirqishlar orasi 0,4 mm, ekrangacha 1,5 m. Qo‘shni yorug‘ polosalar orasi 2,25 mm. Yorug‘lik to‘lqin uzunligini toping.",
           r"\(\lambda=\frac{\Delta y\,d}{L}=\frac{2{,}25\cdot10^{-3}\cdot0{,}4\cdot10^{-3}}{1{,}5}=6{,}0\cdot10^{-7}\) m \(=600\) nm (to‘q sariq)."),
          ("Ma’rifatlovchi qoplama", r"Shisha linza (n = 1,5) sirtiga sindirish ko‘rsatkichi 1,38 bo‘lgan MgF₂ qatlami qoplangan. 550 nm uchun aks ettirishni minimal qiladigan eng kichik qalinlikni toping.",
           r"Ikkala qaytish ham optik zichroq muhitdan, shuning uchun yarim to‘lqin yo‘qotishlar bir-birini kompensatsiyalaydi. Minimum sharti \(2nd=\lambda/2\Rightarrow d=\frac{\lambda}{4n}=\frac{550}{4\cdot1{,}38}\approx100\) nm.")],
 simtask=["λ = 600 nm, d = 0,5 mm, L = 1 m o‘rnating va polosalar kengligini Δy = λL/d bilan tekshiring.", "λ ni 450 nm dan 700 nm gacha o‘zgartiring: polosalar kengligi qanday o‘zgaradi? Oq yorug‘likda manzara qanday bo‘ladi?", "Tirqish kengligi b ni oshiring: difraksion o‘ram (kulrang punktir) qanday torayadi?"],
 mistakes=[("“Ikki lampa yorug‘ligi ham interferensiya beradi.”", "Mustaqil manbalar kogerent emas: manzara juda tez o‘zgarib, o‘rtachalashadi."),
           ("“Interferensiyada energiya yo‘qoladi.”", "Energiya faqat qayta taqsimlanadi: minimumlardagi kamayish maksimumlardagi ortish bilan qoplanadi."),
           ("“Polosalar kengligi tirqishlar orasidagi masofaga proporsional.”", "Aksincha, \\(\\Delta y=\\lambda L/d\\) — tirqishlar yaqinlashsa, polosalar kengayadi.")],
 ai=AI.format(t="yorug‘lik interferensiyasi", b="1) Yung tajribasida optik yo‘llar farqini geometrik chizma orqali keltirib chiqarishga yordam ber.\n2) Python’da ikki tirqish uchun intensivlik I(y) ni (tirqish kengligi hisobga olingan holda) hisoblab chiz va oq yorug‘lik uchun rangli manzarani taxminan modellashtir."),
 quiz=[("Interferensiya kuzatilishi uchun to‘lqinlar:", ["kogerent bo‘lishi kerak", "turli chastotali bo‘lishi kerak", "qutblanmagan bo‘lishi kerak", "juda intensiv bo‘lishi kerak"], 0, "Fazalar farqi o‘zgarmas bo‘lishi kerak."),
       ("Interferensiya maksimumining sharti:", [r"\(\Delta=m\lambda\)", r"\(\Delta=(m+\frac12)\lambda\)", r"\(\Delta=\lambda/4\)", r"faqat \(\Delta=0\)"], 0, "To‘lqinlar bir fazada qo‘shiladi."),
       ("Yung tajribasida tirqishlar orasidagi masofa 2 marta kamaysa, polosalar kengligi:", ["2 marta ortadi", "2 marta kamayadi", "o‘zgarmaydi", "4 marta ortadi"], 0, "Δy = λL/d."),
       ("λ = 500 nm, d = 1 mm, L = 2 m. Polosalar kengligi:", ["1 mm", "0,5 mm", "2 mm", "0,25 mm"], 0, "Δy = 500·10⁻⁹·2/10⁻³."),
       ("Sovun pufagining rangdorligi sababi:", ["yupqa pardadagi interferensiya", "dispersiya", "qutblanish", "fluoressensiya"], 0, "Qalinlikka bog‘liq yo‘l farqi."),
       ("Optik yo‘l uzunligi:", [r"\(nl\)", r"\(l/n\)", r"\(l\)", r"\(n/l\)"], 0, "Muhitda faza tezroq yig‘iladi."),
       ("Nyuton halqalarida (qaytgan yorug‘lik) qorong‘i halqa radiusi:", [r"\(\sqrt{mR\lambda}\)", r"\(mR\lambda\)", r"\(\sqrt{R/\lambda}\)", r"\(m\lambda/R\)"], 0, "Havo qatlami qalinligi r²/(2R)."),
       ("Ma’rifatlovchi qoplamaning optimal qalinligi:", [r"\(\lambda/(4n)\)", r"\(\lambda/2\)", r"\(\lambda\)", r"\(2\lambda n\)"], 0, "Yo‘l farqi λ/2."),
       ("Qizil yorug‘likni ko‘k bilan almashtirsak, Yung polosalari:", ["torayadi", "kengayadi", "o‘zgarmaydi", "yo‘qoladi"], 0, "λ kichik."),
       ("Interferensiyada energiya:", ["qayta taqsimlanadi", "yo‘qoladi", "ikki baravar ortadi", "issiqlikka aylanadi"], 0, "Saqlanish qonuni buzilmaydi.")],
 blits=["Nima uchun ko‘lmakdagi benzin dog‘i rangli ko‘rinadi?", "Kamera obyektivlari nima uchun binafsha tusda ko‘rinadi?", "Yung tajribasi yorug‘lik tabiati haqidagi qaysi bahsni hal qildi?", "Gravitatsion to‘lqinlar detektori LIGO qaysi asbobga asoslangan?", "Ikki alohida lazer nuri interferensiya beradimi?"]
))

L.append(dict(
 n=20, short="Yorug‘lik difraksiyasi", sim="grating", refs=[1, 2, 3, 4, 5], intl=["hecht", "openstax3", "young"], tn=["TN2", "TN9"],
 phet=[("Wave Interference", "wave-interference")],
 title="Yorug‘lik difraksiyasi. Gyuygens–Frenel prinsipi. Frenel va Fraungofer difraksiyasi. Difraksion panjara va uning ajrata olish qobiliyati",
 goal="Difraksiya hodisasini, Gyuygens–Frenel prinsipi va Frenel zonalari usulini, disk va doiraviy teshikdagi Frenel difraksiyasini, tirqish va difraksion panjaradagi Fraungofer difraksiyasini hamda panjaraning dispersiyasi va ajrata olish qobiliyatini o‘rganish.",
 outcomes=["Gyuygens–Frenel prinsipini va Frenel zonalari usulini tushuntiradi;", "doiraviy teshik va disk orqali Frenel difraksiyasini tahlil qiladi;", "tirqish va difraksion panjarada Fraungofer difraksiyasi maksimum va minimumlarini hisoblaydi;", "panjara davri, spektr tartibi va ajrata olish qobiliyatini hisoblaydi."],
 plan=["Difraksiya hodisasi. Gyuygens–Frenel prinsipi", "Frenel zonalari. Doiraviy teshik va diskdagi difraksiya", "Bitta tirqishdagi Fraungofer difraksiyasi", "Difraksion panjara. Panjara formulasi", "Panjaraning ajrata olish qobiliyati. Rentgen nurlarining difraksiyasi"],
 terms=["difraksiya", "Gyuygens–Frenel prinsipi", "Frenel zonalari", "panjara davri d", "spektr tartibi k", "ajrata olish qobiliyati R", "Vulf–Bregg formulasi"],
 theory=[
  ("Difraksiya va Gyuygens–Frenel prinsipi", r"""<p>Difraksiya — to‘lqinlarning to‘siqlarni aylanib o‘tishi, geometrik soya chegarasidan og‘ishi. U to‘siq o‘lchami to‘lqin uzunligi bilan taqqoslanadigan bo‘lganda yoki kuzatish masofasi katta bo‘lganda yaqqol namoyon bo‘ladi. <b>Gyuygens–Frenel prinsipi:</b> to‘lqin frontining har bir nuqtasi ikkilamchi kogerent to‘lqinlar manbai; kuzatish nuqtasidagi tebranish ularning interferensiyasi natijasidir.</p>"""),
  ("Frenel zonalari. Doiraviy teshik va disk", r"""<p>Frenel to‘lqin frontini zonalarga ajratdi: qo‘shni zonalardan kelayotgan tebranishlar qarama-qarshi fazada (yo‘l farqi \(\lambda/2\)). Teshik toq sonli zonalarni ochsa, markazda yorug‘ dog‘, juft sonli zonalarni ochsa — qorong‘i dog‘ kuzatiladi. Noshaffof disk soyasining markazida esa doim yorug‘ dog‘ bo‘ladi (Puasson dog‘i) — bu to‘lqin nazariyasining yorqin tasdig‘i. Zona plastinkasi linza kabi yorug‘likni fokuslaydi.</p>"""),
  ("Bitta tirqishda Fraungofer difraksiyasi", r"""<p>Parallel nurlar kengligi \(b\) bo‘lgan tirqishdan o‘tganda ekranda markaziy yorug‘ polosa va kuchsizroq yon maksimumlar hosil bo‘ladi. Minimumlar sharti:</p>
$$b\sin\varphi=k\lambda,\qquad k=\pm1,\pm2,\dots$$
<p>Markaziy maksimumning burchak kengligi \(2\lambda/b\): tirqish torayishi bilan manzara kengayadi. Shu sababli optik asboblarning ajrata olish qobiliyati difraksiya bilan cheklangan (Reley mezoni: doiraviy obyektiv uchun \(\theta_\text{min}=1{,}22\lambda/D\)).</p>"""),
  ("Difraksion panjara", r"""<p>Difraksion panjara — davri \(d\) bo‘lgan ko‘plab parallel tirqishlar (1 mm da 50–1200 shtrix). Bosh maksimumlar sharti — <b>panjara formulasi</b>:</p>
$$d\sin\varphi=k\lambda,\qquad k=0,\pm1,\pm2,\dots,\qquad k_\text{max}<\frac d\lambda$$
<p>Maksimumlar shtrixlar soni \(N\) ortishi bilan ingichkalashadi va yorqinlashadi. Oq yorug‘lik spektrga ajraladi (binafsha markazga yaqin, qizil uzoqroq). Ajrata olish qobiliyati \(R=\lambda/\delta\lambda=kN\); masalan, natriy dubleti (589,0 va 589,6 nm) uchun \(R\approx1000\) kerak. Kristallar rentgen nurlari uchun uch o‘lchamli panjara vazifasini bajaradi: Vulf–Bregg sharti \(2d\sin\theta=k\lambda\) — rentgen-struktura tahlilining asosi. Panjara yordamida to‘lqin uzunligini o‘lchash — L30 laboratoriya ishi.</p>""")],
 chem=["Rentgen-struktura tahlili (Vulf–Bregg formulasi) kristall va molekulalar tuzilishini aniqlashning asosiy usuli; DNK qo‘sh spirali ham shu usul ma’lumotlari asosida aniqlangan.",
       "Spektrofotometr va monoxromatorlarda difraksion panjara yorug‘likni to‘lqin uzunliklari bo‘yicha ajratadi.",
       "Elektronlar va neytronlar difraksiyasi sirt tuzilishini va kristallardagi atomlar joylashuvini o‘rganishda qo‘llaniladi."],
 example=[("Panjara bilan λ ni o‘lchash", r"1 mm da 300 shtrixli panjara. Yashil lazer nurining 1-tartib maksimumi 9,2° burchak ostida kuzatildi. To‘lqin uzunligini va eng katta tartibni toping.",
           r"\(d=1/300\) mm \(=3{,}33\) mkm. \(\lambda=d\sin\varphi=3{,}33\cdot0{,}1599=0{,}533\) mkm \(=533\) nm. \(d/\lambda=6{,}25\Rightarrow k_\text{max}=6\)."),
          ("Ajrata olish qobiliyati", r"Natriyning sariq dubleti (589,0 va 589,6 nm) 2-tartib spektrda ajralishi uchun panjaraning kamida nechta shtrixi yoritilishi kerak?",
           r"\(R=\lambda/\delta\lambda=589/0{,}6\approx982\). \(N=R/k=491\) — kamida \(\approx500\) shtrix.")],
 simtask=["λ = 532 nm, 300 shtrix/mm o‘rnating: 1-tartib burchagi 9,2° ga yaqinligini tekshiring.", "Yoritilgan shtrixlar sonini 2 dan 40 gacha oshiring: maksimumlar qanday o‘zgaradi?", "Shtrixlar zichligini 1000 /mm ga oshiring: nechta tartib kuzatiladi va nima uchun?"],
 mistakes=[("“Difraksiya faqat juda kichik teshiklarda bo‘ladi.”", "Difraksiya har doim bor; u to‘siq o‘lchami λ ga yaqin yoki kuzatish masofasi katta bo‘lganda sezilarli."),
           ("“Panjarada qizil nur ko‘kdan kamroq og‘adi.”", "\\(\\sin\\varphi=k\\lambda/d\\): qizil (katta λ) ko‘proq og‘adi — prizmadagi dispersiyaga teskari."),
           ("“Shtrixlar soni ko‘paysa, maksimumlar burchagi o‘zgaradi.”", "Burchak faqat d va λ ga bog‘liq; N maksimumlarning kengligi va yorqinligini o‘zgartiradi.")],
 ai=AI.format(t="yorug‘lik difraksiyasi va difraksion panjara", b="1) Panjara formulasini ikki qo‘shni tirqishdan kelayotgan nurlar yo‘l farqi orqali keltirib chiqarishga yordam ber.\n2) Python’da N tirqishli panjara intensivligini I(sinφ) hisoblab, N = 2, 5, 20 uchun bitta grafikda solishtir."),
 quiz=[("Difraksion panjara formulasi:", [r"\(d\sin\varphi=k\lambda\)", r"\(d\cos\varphi=k\lambda\)", r"\(b\sin\varphi=(k+\frac12)\lambda\)", r"\(d=k\lambda\sin\varphi\)"], 0, "Bosh maksimumlar sharti."),
       ("1 mm da 500 shtrix. Panjara davri:", ["2 mkm", "0,5 mkm", "500 nm", "5 mkm"], 0, "d = 1 mm/500."),
       ("Oq yorug‘lik panjara spektrida qaysi rang markazga eng yaqin?", ["binafsha", "qizil", "yashil", "sariq"], 0, "λ eng kichik."),
       ("Puasson dog‘i qayerda kuzatiladi?", ["noshaffof disk soyasining markazida", "teshik chetida", "panjara spektrida", "prizmada"], 0, "To‘lqin nazariyasining tasdig‘i."),
       ("Panjaraning ajrata olish qobiliyati:", [r"\(R=kN\)", r"\(R=d/\lambda\)", r"\(R=N/k\)", r"\(R=\lambda d\)"], 0, "N — yoritilgan shtrixlar soni."),
       ("Bitta tirqishda minimum sharti:", [r"\(b\sin\varphi=k\lambda\)", r"\(b\sin\varphi=(k+\frac12)\lambda\)", r"\(b=\lambda\)", r"\(\sin\varphi=b/\lambda\)"], 0, "Tirqish juft zonalarga bo‘linadi."),
       ("d = 2 mkm, λ = 0,5 mkm. Kuzatiladigan eng katta spektr tartibi:", ["3", "4", "2", "5"], 0, "d/λ = 4, ammo k = 4 ga φ = 90° to‘g‘ri keladi — u ekranga tushmaydi."),
       ("Rentgen-struktura tahlili qaysi formulaga asoslangan?", ["Vulf–Bregg", "Malyus", "Bryuster", "Vin"], 0, "2d sin θ = kλ."),
       ("Tirqish kengligi kamaysa, markaziy maksimum:", ["kengayadi", "torayadi", "o‘zgarmaydi", "yo‘qoladi"], 0, "Burchak kengligi 2λ/b."),
       ("Obyektiv diametri 2 marta oshsa, burchak ajrata olish chegarasi:", ["2 marta kichrayadi (yaxshilanadi)", "2 marta ortadi", "o‘zgarmaydi", "4 marta kichrayadi"], 0, "θ = 1,22λ/D.")],
 blits=["CD/DVD disk sirtida nima uchun kamalak ko‘rinadi?", "Nima uchun radioto‘lqinlar binolarni aylanib o‘tadi, yorug‘lik esa yo‘q?", "Teleskop diametri nima uchun katta qilinadi?", "Kristall panjara nima uchun rentgen nurlari uchun difraksion panjara bo‘la oladi?", "Ko‘zni qisib lampaga qaraganda nur “nayzalari” nima uchun ko‘rinadi?"]
))

L.append(dict(
 n=21, short="Dispersiya va qutblanish", sim="malus", refs=[1, 2, 3, 4, 5], intl=["hecht", "openstax3", "atkins"], tn=["TN1", "TN9"],
 phet=[("Bending Light", "bending-light")],
 title="Moddalarda elektromagnit to‘lqinlar. Yorug‘lik dispersiyasi va spektral tahlil. Yorug‘likning qutblanishi. Malyus va Bryuster qonunlari",
 goal="Yorug‘lik to‘lqinlarining modda bilan o‘zaro ta’sirini, dispersiya va spektral tahlil tushunchalarini, tabiiy va qutblangan yorug‘likni, Malyus qonunini hamda qaytish va sinishda yorug‘likning qutblanishi va Bryuster qonunini o‘rganish.",
 outcomes=["dispersiyani elektron nazariya asosida tushuntiradi va prizmada spektr hosil bo‘lishini izohlaydi;", "emission va yutilish spektrlarini, spektral tahlil asoslarini tushuntiradi;", "Malyus qonuni bo‘yicha qutblagich va analizatordan o‘tgan intensivlikni hisoblaydi;", "Bryuster burchagini hisoblaydi va qutblangan yorug‘lik olish usullarini sanab beradi."],
 plan=["Yorug‘likning modda bilan o‘zaro ta’siri. Yutilish va sochilish", "Yorug‘lik dispersiyasi. Prizmada spektr", "Spektral tahlil haqida tushuncha", "Tabiiy va qutblangan yorug‘lik. Malyus qonuni", "Qaytish va sinishda qutblanish. Bryuster qonuni"],
 terms=["dispersiya \\(n(\\lambda)\\)", "Buger–Lambert–Ber qonuni", "spektral tahlil", "qutblagich va analizator", "Malyus qonuni", "Bryuster burchagi", "optik faollik"],
 theory=[
  ("Yorug‘likning modda bilan o‘zaro ta’siri", r"""<p>Yorug‘lik to‘lqinining elektr maydoni modda atomlaridagi elektronlarni majburiy tebratadi; tebranayotgan elektronlar ikkilamchi to‘lqinlar chiqaradi. Ularning birlamchi to‘lqin bilan qo‘shilishi yorug‘likning muhitdagi tezligini kamaytiradi (\(v=c/n\)), yutilish (energiyaning issiqlikka o‘tishi) va sochilishni yuzaga keltiradi. Yutilish Buger–Lambert–Ber qonuniga bo‘ysunadi: \(I=I_0e^{-\alpha x}\), eritmalar uchun \(I=I_0\cdot10^{-\varepsilon cl}\). Kichik zarralarda Reley sochilishi \(I\propto1/\lambda^4\) — osmonning havorangligi va quyosh botishidagi qizillikning sababi.</p>"""),
  ("Dispersiya va prizma", r"""<p><b>Dispersiya</b> — sindirish ko‘rsatkichining to‘lqin uzunligiga bog‘liqligi \(n(\lambda)\). Shaffof moddalarda \(\lambda\) kamayishi bilan \(n\) ortadi (normal dispersiya; Koshi formulasi \(n\approx A+B/\lambda^2\)), yutilish chiziqlari yaqinida esa anomal dispersiya kuzatiladi. Prizmadan o‘tgan oq yorug‘lik spektrga ajraladi: binafsha nurlar ko‘proq, qizillari kamroq og‘adi (Nyuton, 1666). Kamalak ham yomg‘ir tomchilaridagi dispersiya natijasi.</p>"""),
  ("Spektral tahlil", r"""<p>Siyrak qizdirilgan gazlar <b>chiziqli emission</b> spektr beradi — har bir element uchun o‘ziga xos “barmoq izi”. Oq yorug‘lik sovuqroq gaz orqali o‘tganda xuddi shu to‘lqin uzunliklarida qorong‘i chiziqlar — <b>yutilish spektri</b> paydo bo‘ladi (Kirxgof va Bunzen, 1859; Quyosh spektridagi Fraungofer chiziqlari). Spektral tahlil moddaning kimyoviy tarkibini juda kichik miqdorlarda aniqlaydi; geliy avval Quyosh spektrida topilgan.</p>"""),
  ("Qutblanish. Malyus va Bryuster qonunlari", r"""<p>Yorug‘lik ko‘ndalang to‘lqin. Tabiiy yorug‘likda \(\vec E\) vektor tebranishlari barcha yo‘nalishlarda teng ehtimolli; tebranishlar bitta tekislikda bo‘lsa — <b>yassi qutblangan</b> yorug‘lik. Ideal qutblagich (polyaroid) tabiiy yorug‘lik intensivligini ikki marta kamaytiradi. Qutblagich va analizator o‘qlari orasidagi burchak \(\varphi\) bo‘lsa — <b>Malyus qonuni</b>:</p>
$$I=I_0\cos^2\varphi$$
<p>Dielektrik sirtidan qaytgan yorug‘lik qisman qutblanadi; tushish burchagi <b>Bryuster burchagi</b> \(\tan\theta_B=n_{21}\) bo‘lganda qaytgan nur to‘liq qutblanadi (tebranishlar tushish tekisligiga perpendikulyar), qaytgan va singan nurlar orasidagi burchak \(90^\circ\) bo‘ladi. Shisha uchun \(\theta_B\approx56^\circ\), suv uchun \(53^\circ\). Ba’zi kristallar (island shpati) ikki nur sindiradi; optik faol moddalar (shakar eritmasi) qutblanish tekisligini buradi.</p>""")],
 chem=["Spektrofotometriya Buger–Lambert–Ber qonuniga asoslangan: optik zichlik \\(D=\\varepsilon cl\\) orqali eritma konsentratsiyasi topiladi.",
       "Polyarimetriya: optik faol moddalar (shakar, aminokislotalar) qutblanish tekisligini buradi; burilish burchagi konsentratsiyaga proporsional, enantiomerlarni farqlashda qo‘llaniladi.",
       "Atom-emission va atom-absorbsion spektroskopiya — elementlar tahlilining standart usullari."],
 example=[("Ikki qutblagich", r"Tabiiy yorug‘lik (intensivligi I₀) qutblagich va analizator orqali o‘tdi, ularning o‘qlari orasidagi burchak 60°. Chiqishdagi intensivlikni toping.",
           r"Qutblagichdan keyin \(I_1=I_0/2\). Analizatordan keyin \(I_2=I_1\cos^260^\circ=\frac{I_0}{2}\cdot\frac14=\frac{I_0}{8}\)."),
          ("Bryuster burchagi", r"Suv (n = 1,33) sirtidan qaytgan quyosh nuri qaysi tushish burchagida to‘liq qutblanadi? Bunda nur qanday burchak ostida sinadi?",
           r"\(\theta_B=\arctan1{,}33=53{,}1^\circ\). Singan nur: \(90^\circ-53{,}1^\circ=36{,}9^\circ\) (Snellius qonuni bilan tekshiruv: \(\sin53{,}1^\circ/\sin36{,}9^\circ=1{,}33\)). Qutblovchi quyosh ko‘zoynaklari aynan shu yaltirashni so‘ndiradi.")],
 simtask=["φ ni 0° dan 90° gacha o‘zgartirib, I/I₀ = cos²φ ni 30°, 45°, 60° da tekshiring.", "n = 1,5 da tushish burchagini o‘zgartiring: R_p qaysi burchakda nolga teng? Uni arctg n bilan solishtiring.", "n = 1,33 (suv) uchun Bryuster burchagini toping va 2-misol bilan solishtiring."],
 mistakes=[("“Qutblagich yorug‘likni bo‘yaydi.”", "Qutblagich faqat ma’lum yo‘nalishdagi tebranishlarni o‘tkazadi; yorug‘lik rangi o‘zgarmaydi."),
           ("“Har qanday sirtdan qaytgan yorug‘lik to‘liq qutblanadi.”", "Dielektrik sirtidan qaytgan yorug‘lik odatda qisman qutblanadi; to‘liq qutblanish faqat Bryuster burchagida."),
           ("“Prizmada qizil nur eng ko‘p og‘adi.”", "Normal dispersiyada n binafsha uchun katta, shuning uchun binafsha nur ko‘proq og‘adi.")],
 ai=AI.format(t="dispersiya, spektral tahlil va qutblanish", b="1) Bryuster burchagida qaytgan va singan nurlar perpendikulyarligini Snellius qonunidan isbotlashga yordam ber.\n2) Python’da Frenel formulalari bo‘yicha R_s(θ) va R_p(θ) ni shisha (n = 1,5) uchun chizib, Bryuster burchagini sonli top."),
 quiz=[("Dispersiya nima?", ["sindirish ko‘rsatkichining to‘lqin uzunligiga bog‘liqligi", "yorug‘likning qaytishi", "yorug‘likning yutilishi", "qutblanish"], 0, "n(λ)."),
       ("Malyus qonuni:", [r"\(I=I_0\cos^2\varphi\)", r"\(I=I_0\cos\varphi\)", r"\(I=I_0\sin^2\varphi\)", r"\(I=I_0/\varphi\)"], 0, "Amplituda cos φ marta kamayadi."),
       ("Tabiiy yorug‘lik ideal qutblagichdan o‘tsa, intensivlik:", ["2 marta kamayadi", "o‘zgarmaydi", "4 marta kamayadi", "nolga teng bo‘ladi"], 0, "cos² ning o‘rtacha qiymati 1/2."),
       ("Bryuster qonuni:", [r"\(\tan\theta_B=n_{21}\)", r"\(\sin\theta_B=n\)", r"\(\cos\theta_B=1/n\)", r"\(\theta_B=n\)"], 0, "Qaytgan nur to‘liq qutblanadi."),
       ("Shisha (n = 1,5) uchun Bryuster burchagi:", ["≈56°", "≈42°", "≈34°", "≈90°"], 0, "arctg 1,5."),
       ("Osmonning havorangligiga sabab:", ["Reley sochilishi (∝ 1/λ⁴)", "dispersiya", "interferensiya", "qutblanish"], 0, "Ko‘k nur ko‘proq sochiladi."),
       ("Spektral tahlilda element nima orqali aniqlanadi?", ["o‘ziga xos chiziqli spektri orqali", "rangi orqali", "zichligi orqali", "massasi orqali"], 0, "Har bir elementning spektri noyob."),
       ("Prizmada qaysi nur eng ko‘p og‘adi?", ["binafsha", "qizil", "yashil", "sariq"], 0, "n eng katta."),
       ("Qutblagich va analizator o‘qlari perpendikulyar. O‘tgan yorug‘lik:", ["yo‘q", "I₀/2", "I₀/4", "I₀"], 0, "cos² 90° = 0."),
       ("Buger–Lambert–Ber qonuni nimani ifodalaydi?", ["yorug‘likning yutilishini", "yorug‘lik sinishini", "qutblanishni", "interferensiyani"], 0, "Intensivlikning eksponensial kamayishi.")],
 blits=["Quyosh botayotganda nima uchun qizil ko‘rinadi?", "Polyaroid ko‘zoynak bilan suv sirtiga qaraganda nima o‘zgaradi?", "Kamalak qanday hosil bo‘ladi?", "3D kinoda ko‘zoynaklar qanday ishlaydi?", "Geliy qanday kashf qilingan?"]
))

L.append(dict(
 n=22, short="Geometrik optika", sim=["lens", "snell"], refs=[1, 2, 3, 4, 5], intl=["hecht", "openstax3", "halliday"], tn=["TN6", "TN9"],
 phet=[("Geometric Optics", "geometric-optics"), ("Bending Light", "bending-light")],
 title="Geometrik optika. Yorug‘likning qaytish va sinish qonunlari. To‘la ichki qaytish. Linzalar va ularda tasvir yasash",
 goal="Yorug‘likning to‘g‘ri chiziq bo‘ylab tarqalishi, qaytish va sinish qonunlari, to‘la ichki qaytish, yupqa linzalar, linza formulasi va linzalarda tasvir yasash qoidalarini o‘rganish; lupa va mikroskop ishlashini tushunish.",
 outcomes=["qaytish va sinish qonunlarini qo‘llab nur yo‘lini quradi;", "to‘la ichki qaytishning kritik burchagini hisoblaydi va qo‘llanilishini (optik tola) tushuntiradi;", "yupqa linza formulasi bo‘yicha tasvir o‘rni, kattalashtirish va optik kuchni hisoblaydi;", "yig‘uvchi va sochuvchi linzalarda tasvir yasaydi, lupa va mikroskop kattalashtirishini baholaydi."],
 plan=["Yorug‘likning to‘g‘ri chiziq bo‘ylab tarqalishi. Ferma prinsipi", "Qaytish va sinish qonunlari. Sindirish ko‘rsatkichi", "To‘la ichki qaytish va uning qo‘llanilishi", "Yupqa linzalar. Linza formulasi. Optik kuch", "Linzalarda tasvir yasash. Lupa va mikroskop"],
 terms=["sindirish ko‘rsatkichi n", "Snellius qonuni", "kritik burchak", "fokus masofasi F", "optik kuch D (dptr)", "chiziqli kattalashtirish \\(\\Gamma\\)", "mavhum tasvir"],
 theory=[
  ("Geometrik optika qonunlari", r"""<p>To‘lqin uzunligi to‘siqlarga nisbatan juda kichik bo‘lsa, yorug‘lik tarqalishini nurlar bilan tavsiflash mumkin. Bir jinsli muhitda yorug‘lik to‘g‘ri chiziq bo‘ylab tarqaladi (soya va yarim soya, Quyosh va Oy tutilishlari). Geometrik optika qonunlari Ferma prinsipidan kelib chiqadi: yorug‘lik eng kam vaqt talab qiladigan yo‘l bo‘ylab tarqaladi.</p>"""),
  ("Qaytish va sinish qonunlari", r"""<p><b>Qaytish:</b> tushgan nur, qaytgan nur va normal bir tekislikda yotadi; qaytish burchagi tushish burchagiga teng. <b>Sinish (Snellius qonuni):</b></p>
$$n_1\sin\alpha=n_2\sin\beta,\qquad n=\frac cv$$
<p>Absolyut sindirish ko‘rsatkichlari: havo 1,0003, suv 1,33, shisha 1,5–1,9, olmos 2,42. Optik zichroq muhitga o‘tganda nur normalga yaqinlashadi. Yassi-parallel plastinkadan o‘tgan nur yo‘nalishini saqlaydi, faqat parallel siljiydi. Qatlamning ko‘rinma qalinligi \(h'\approx h/n\) — mikroskop bilan sindirish ko‘rsatkichini aniqlash (L28) shunga asoslangan.</p>"""),
  ("To‘la ichki qaytish", r"""<p>Optik zichroq muhitdan siyrakroq muhitga o‘tganda (\(n_1>n_2\)) tushish burchagi kritik burchakdan katta bo‘lsa, yorug‘lik to‘liq qaytadi:</p>
$$\sin\alpha_\text{kr}=\frac{n_2}{n_1}$$
<p>Shisha–havo uchun \(\alpha_\text{kr}\approx42^\circ\), olmos uchun \(24^\circ\) — olmos jilosining sababi. Qo‘llanilishi: optik tolali aloqa, endoskoplar, to‘la qaytaruvchi prizmalar (binokl, periskop), refraktometrlar (Abbe refraktometri suyuqliklar sindirish ko‘rsatkichini kritik burchak orqali o‘lchaydi).</p>"""),
  ("Yupqa linzalar va tasvir yasash", r"""<p>Yupqa linza formulasi, optik kuch va kattalashtirish:</p>
$$\frac1d+\frac1{d'}=\frac1F,\qquad D=\frac1F=(n-1)\left(\frac1{R_1}+\frac1{R_2}\right),\qquad \Gamma=\frac{h'}{h}=-\frac{d'}{d}$$
<p>Yig‘uvchi linza uchun \(F>0\), sochuvchi uchun \(F<0\); mavhum tasvir uchun \(d'<0\). Tasvir yasashda uchta qulay nurdan foydalaniladi: bosh optik o‘qqa parallel nur fokusdan o‘tadi; optik markazdan o‘tgan nur sinmaydi; fokusdan o‘tgan nur o‘qqa parallel chiqadi. Yig‘uvchi linzada: \(d>2F\) — haqiqiy, teskari, kichraygan (fotoapparat, ko‘z); \(F<d<2F\) — haqiqiy, teskari, kattalashgan (proyektor); \(d<F\) — mavhum, to‘g‘ri, kattalashgan (lupa, \(\Gamma\approx25\ \text{sm}/F\)). Mikroskop kattalashtirishi \(\Gamma\approx\dfrac{\delta\cdot25\ \text{sm}}{F_\text{ob}F_\text{ok}}\), \(\delta\) — tubus optik uzunligi (L27).</p>""")],
 chem=["Refraktometriya: suyuqliklar sindirish ko‘rsatkichi (Abbe refraktometri) bo‘yicha moddaning tozaligi va eritma konsentratsiyasi aniqlanadi (masalan, shakar miqdori).",
       "Optik tolali datchiklar kimyoviy reaktorlarda va spektroskopiyada masofadan o‘lchash imkonini beradi.",
       "Mikroskopiya — kristallar shakli, zarralar o‘lchami va biologik obyektlarni o‘rganishning asosiy usuli."],
 example=[("Linzada tasvir", r"Fokus masofasi 15 sm bo‘lgan yig‘uvchi linzadan 40 sm masofada balandligi 3 sm buyum turibdi. Tasvir o‘rni, kattalashtirish va turini toping.",
           r"\(\frac1{d'}=\frac1{15}-\frac1{40}=\frac{8-3}{120}\Rightarrow d'=24\) sm. \(\Gamma=-24/40=-0{,}6\), \(h'=-1{,}8\) sm: tasvir haqiqiy, teskari, kichraygan. Optik kuch \(D=1/0{,}15=6{,}7\) dptr."),
          ("Optik tola", r"Optik tola o‘zagining sindirish ko‘rsatkichi 1,48, qobig‘iniki 1,46. Kritik burchakni toping.",
           r"\(\sin\alpha_\text{kr}=1{,}46/1{,}48=0{,}9865\Rightarrow\alpha_\text{kr}=80{,}6^\circ\). Tola o‘qiga \(9{,}4^\circ\) dan kichik burchak ostida tarqalayotgan nurlar tola ichida qoladi.")],
 simtask=["Linza modelida 1-misol qiymatlarini kiriting va d′, Γ ni tekshiring.", "Buyumni 80 sm dan 5 sm gacha yaqinlashtirib, tasvir turi qaysi nuqtalarda (2F, F) o‘zgarishini kuzating.", "Sinish modelida n₁ = 1,5, n₂ = 1 o‘rnatib, to‘la ichki qaytish boshlanadigan burchakni toping va arcsin(n₂/n₁) bilan solishtiring."],
 mistakes=[("“Linzaning yarmini to‘sib qo‘ysak, tasvirning yarmi yo‘qoladi.”", "Tasvir to‘liq qoladi, faqat xiraroq bo‘ladi: har bir nuqta tasviri linzaning butun yuzasidan o‘tgan nurlar bilan hosil bo‘ladi."),
           ("“Mavhum tasvirni ko‘rib bo‘lmaydi.”", "Mavhum tasvirni ko‘z ko‘radi (lupa, ko‘zgu), faqat uni ekranda olib bo‘lmaydi."),
           ("“Suvdan havoga chiqayotgan nur doim siniladi.”", "Kritik burchakdan katta burchaklarda nur to‘liq qaytadi.")],
 ai=AI.format(t="geometrik optika va linzalar", b="1) Yupqa linza formulasini o‘xshash uchburchaklar orqali keltirib chiqarishga yordam ber.\n2) Python’da F = 15 sm linza uchun d′(d) va Γ(d) grafiklarini chizib, tasvir turlari sohalarini (d > 2F, F < d < 2F, d < F) belgilab ber."),
 quiz=[("Sinish qonuni:", [r"\(n_1\sin\alpha=n_2\sin\beta\)", r"\(n_1\cos\alpha=n_2\cos\beta\)", r"\(\alpha=\beta\)", r"\(n_1\alpha=n_2\)"], 0, "Snellius qonuni."),
       ("Yorug‘likning suvdagi tezligi (n = 1,33):", ["≈2,26·10⁸ m/s", "3·10⁸ m/s", "4·10⁸ m/s", "1,33·10⁸ m/s"], 0, "v = c/n."),
       ("Shisha (n = 1,5)–havo chegarasida kritik burchak:", ["≈42°", "≈56°", "≈30°", "≈90°"], 0, "arcsin(1/1,5)."),
       ("Fokus masofasi 0,25 m bo‘lgan linzaning optik kuchi:", ["4 dptr", "0,25 dptr", "25 dptr", "2 dptr"], 0, "D = 1/F."),
       ("Yig‘uvchi linzada d > 2F bo‘lsa, tasvir:", ["haqiqiy, teskari, kichraygan", "mavhum, to‘g‘ri, kattalashgan", "haqiqiy, to‘g‘ri, kattalashgan", "hosil bo‘lmaydi"], 0, "Fotoapparat rejimi."),
       ("Lupa qanday tasvir beradi?", ["mavhum, to‘g‘ri, kattalashgan", "haqiqiy, teskari", "haqiqiy, to‘g‘ri", "mavhum, teskari"], 0, "d < F."),
       ("Sochuvchi linzaning fokus masofasi:", ["manfiy", "musbat", "nol", "cheksiz"], 0, "Fokus mavhum."),
       ("d = 30 sm, F = 10 sm. Tasvirgacha masofa:", ["15 sm", "20 sm", "7,5 sm", "30 sm"], 0, "1/d′ = 1/10 − 1/30."),
       ("Optik tolada nur qaysi hodisa hisobiga tarqaladi?", ["to‘la ichki qaytish", "difraksiya", "interferensiya", "qutblanish"], 0, "Nur o‘zak ichida qoladi."),
       ("Yassi-parallel plastinkadan o‘tgan nur:", ["parallel siljiydi", "yo‘nalishini keskin o‘zgartiradi", "to‘liq qaytadi", "spektrga ajraladi"], 0, "Ikki sinish kompensatsiyalanadi.")],
 blits=["Nima uchun suvdagi qoshiq “singan” ko‘rinadi?", "Olmos nima uchun shunchalik yaltiraydi?", "Fotoapparatda tasvir qanday hosil bo‘ladi?", "Sahro sarobi (miraj) qanday paydo bo‘ladi?", "Ko‘zoynak linzasining optik kuchi qanday aniqlanadi?"]
))

L.append(dict(
 n=23, short="Nurlanishning kvant tabiati", sim=["planck", "photo"], refs=[1, 2, 3, 4, 5], intl=["krane", "openstax3", "halliday"], tn=["TN3", "TN5", "TN9"],
 phet=[("Blackbody Spectrum", "blackbody-spectrum"), ("Photoelectric Effect", "photoelectric")],
 title="Nurlanishning kvant tabiati. Issiqlik nurlanishi qonunlari. Plank gipotezasi. Tashqi fotoeffekt. Yorug‘lik bosimi. Kompton effekti",
 goal="Issiqlik nurlanishi va absolyut qora jism nurlanish qonunlarini (Kirxgof, Stefan–Bolsman, Vin), Plank gipotezasi va formulasini, foton energiyasi va impulsini, tashqi fotoeffekt qonunlari va Eynshteyn tenglamasini, yorug‘lik bosimi va Kompton effektini o‘rganish.",
 outcomes=["Stefan–Bolsman va Vin qonunlari bo‘yicha nurlanish quvvati va maksimum to‘lqin uzunligini hisoblaydi;", "Plank gipotezasi klassik fizika muammosini (“ultrabinafsha halokat”) qanday hal qilganini tushuntiradi;", "Eynshteyn tenglamasidan fotoelektronlar energiyasi, tormozlovchi kuchlanish va qizil chegarani hisoblaydi;", "foton impulsi, yorug‘lik bosimi va Kompton siljishini hisoblaydi."],
 plan=["Issiqlik nurlanishi. Kirxgof qonuni. Absolyut qora jism", "Stefan–Bolsman va Vinning siljish qonunlari", "Plank gipotezasi va formulasi. Foton energiyasi va impulsi", "Tashqi fotoeffekt qonunlari. Eynshteyn tenglamasi", "Yorug‘lik bosimi. Kompton effekti"],
 terms=["absolyut qora jism", "Stefan–Bolsman qonuni", "Vin qonuni", "Plank doimiysi h", "foton", "chiqish ishi A", "qizil chegara \\(\\lambda_0\\)"],
 theory=[
  ("Issiqlik nurlanishi va Kirxgof qonuni", r"""<p>Har qanday jism temperaturasi tufayli elektromagnit to‘lqinlar chiqaradi — <b>issiqlik nurlanishi</b>. Jismning chiqarish qobiliyati \(r_{\lambda T}\) va yutish qobiliyati \(a_{\lambda T}\) bog‘langan: <b>Kirxgof qonuniga</b> ko‘ra ularning nisbati barcha jismlar uchun bir xil universal funksiya, ya’ni yaxshi yutuvchi jism yaxshi nurlantiradi ham. Barcha nurlanishni yutadigan jism (\(a=1\)) — <b>absolyut qora jism</b>; uning modeli — kichik teshikli bo‘shliq.</p>"""),
  ("Stefan–Bolsman va Vin qonunlari", r"""<p>Absolyut qora jism birlik sirtidan nurlanish quvvati (energetik ravshanlik) va spektr maksimumi:</p>
$$R=\sigma T^4,\quad \sigma=5{,}67\cdot10^{-8}\ \frac{\text{W}}{\text{m}^2\text{K}^4};\qquad \lambda_\text{max}=\frac bT,\quad b=2{,}898\cdot10^{-3}\ \text{m·K}$$
<p>Quyosh sirti (\(T\approx5800\) K) uchun \(\lambda_\text{max}\approx500\) nm; inson tanasi (310 K) uchun \(\approx9{,}3\) mkm — infraqizil (teplovizorlar shu sohada ishlaydi). Real (kulrang) jismlar uchun \(R=\varepsilon\sigma T^4\), \(\varepsilon<1\).</p>"""),
  ("Plank gipotezasi. Foton", r"""<p>Klassik nazariya (Reley–Jins) qisqa to‘lqinlarda cheksiz energiya bashorat qilardi (“ultrabinafsha halokat”). Plank (1900) nurlanish faqat porsiyalar — kvantlar bilan chiqariladi deb faraz qildi: \(\varepsilon=h\nu\), \(h=6{,}626\cdot10^{-34}\) J·s. Plank formulasi tajribaga to‘liq mos keladi:</p>
$$r_{\lambda T}=\frac{2\pi hc^2}{\lambda^5}\,\frac{1}{e^{hc/\lambda kT}-1}$$
<p>Eynshteyn (1905) yorug‘lik kvantlar holida tarqaladi va yutiladi deb ko‘rsatdi; yorug‘lik kvanti — <b>foton</b>: energiyasi \(E=h\nu=hc/\lambda\), impulsi \(p=h/\lambda\), tinchlikdagi massasi nol. Amaliy ifoda: \(E[\text{eV}]\approx1240/\lambda[\text{nm}]\).</p>"""),
  ("Fotoeffekt, yorug‘lik bosimi va Kompton effekti", r"""<p><b>Tashqi fotoeffekt</b> — yorug‘lik ta’sirida moddadan elektronlar chiqishi (Gers, 1887; Stoletov qonunlari). Qonunlar: 1) to‘yinish fototoki yorug‘lik intensivligiga proporsional; 2) fotoelektronlarning maksimal kinetik energiyasi intensivlikka bog‘liq emas va chastota bilan chiziqli ortadi; 3) har bir modda uchun qizil chegara mavjud. Eynshteyn tenglamasi:</p>
$$h\nu=A+\frac{mv_\text{max}^2}{2},\qquad eU_z=h\nu-A,\qquad \lambda_0=\frac{hc}{A}$$
<p>\(U_z(\nu)\) grafigining qiyaligi \(h/e\) — Plank doimiysini aniqlash usuli (L31–L32). Foton impulsi yorug‘lik bosimini beradi: \(p=\frac{I}{c}(1+\rho)\) (P.N. Lebedev tajribalari, 1899–1901), \(\rho\) — qaytarish koeffitsiyenti. <b>Kompton effekti</b> — rentgen fotonlarining erkin elektronlarda sochilganda to‘lqin uzunligining ortishi: \(\Delta\lambda=\frac{h}{m_ec}(1-\cos\theta)\), \(h/(m_ec)=2{,}43\) pm — fotonning zarra xossasini bevosita tasdiqlaydi.</p>""")],
 chem=["Fotokimyo foton energiyasi bilan bog‘liq: bog‘ni uzish uchun \\(h\\nu\\ge E_\\text{bog‘}\\) bo‘lishi kerak (masalan, ozon qatlami 300 nm dan qisqa UB nurlarni yutadi).",
       "Fotoelektron spektroskopiya (XPS) Eynshteyn tenglamasiga asoslanib, elementlarning bog‘lanish energiyalari va kimyoviy holatini aniqlaydi.",
       "Pirometriya va termografiya (Vin va Stefan–Bolsman qonunlari) reaktor va pechlar temperaturasini kontaktsiz o‘lchaydi."],
 example=[("Quyosh nurlanishi", r"Quyosh sirti temperaturasi 5800 K. \(\lambda_\text{max}\) va 1 m² sirtdan nurlanish quvvatini toping.",
           r"\(\lambda_\text{max}=2{,}898\cdot10^{-3}/5800=500\) nm (yashil-ko‘k). \(R=5{,}67\cdot10^{-8}\cdot5800^4=6{,}4\cdot10^7\) W/m² = 64 MW/m²."),
          ("Fotoeffekt", r"Kaliy katodga (A = 2,3 eV) 400 nm li yorug‘lik tushmoqda. Foton energiyasi, fotoelektronlarning maksimal kinetik energiyasi, tormozlovchi kuchlanish va qizil chegarani toping.",
           r"\(E=1240/400=3{,}10\) eV. \(E_k=3{,}10-2{,}3=0{,}80\) eV, \(U_z=0{,}80\) V. \(\lambda_0=1240/2{,}3=539\) nm — bundan uzun to‘lqinli yorug‘lik kaliyda fotoeffekt bermaydi.")],
 simtask=["Plank modelida T = 5800 K da λ_max ni o‘qing va Vin qonuni bilan tekshiring; T ni ikki marta oshiring — R necha marta ortadi?", "Fotoeffekt modelida 2-misol qiymatlarini kiriting va U_z ni tekshiring.", "Intensivlikni o‘zgartiring: to‘yinish toki va U_z qanday o‘zgaradi? Klassik to‘lqin nazariyasi bilan qanday ziddiyat bor?"],
 mistakes=[("“Yorug‘lik qanchalik yorqin bo‘lsa, elektronlar shunchalik tez uchadi.”", "Elektronlar energiyasi faqat chastotaga bog‘liq; intensivlik ularning sonini belgilaydi."),
           ("“Qora jism doim qora ko‘rinadi.”", "Yetarlicha qizdirilgan absolyut qora jism (masalan, Quyosh) eng kuchli nurlantiruvchidir."),
           ("“Foton tinch holatda ham mavjud bo‘lishi mumkin.”", "Fotonning tinchlikdagi massasi nol, u faqat c tezlikda harakatlanadi.")],
 ai=AI.format(t="nurlanishning kvant tabiati va fotoeffekt", b="1) Plank formulasidan Vin qonunini (maksimum sharti) keltirib chiqarishga yordam ber.\n2) Python’da L31–L32 laboratoriya natijalari ko‘rinishidagi (ν, U_z) nuqtalarga chiziqli moslash qilib, h va A ni noaniqligi bilan topadigan kod yoz."),
 quiz=[("Stefan–Bolsman qonuni:", [r"\(R=\sigma T^4\)", r"\(R=\sigma T\)", r"\(\lambda T=b\)", r"\(E=h\nu\)"], 0, "To‘liq nurlanish quvvati."),
       ("Temperatura 2 marta oshsa, absolyut qora jism nurlanish quvvati:", ["16 marta ortadi", "2 marta ortadi", "4 marta ortadi", "8 marta ortadi"], 0, "2⁴ = 16."),
       ("T = 2898 K da λ_max:", ["1 mkm", "500 nm", "2,9 mkm", "100 nm"], 0, "b/T."),
       ("Foton energiyasi:", [r"\(h\nu\)", r"\(mc^2/2\)", r"\(h/\lambda\)", r"\(kT\)"], 0, "h/λ — foton impulsi."),
       ("500 nm foton energiyasi:", ["≈2,5 eV", "≈5 eV", "≈1 eV", "≈12 eV"], 0, "1240/500."),
       ("Fotoelektronlarning maksimal energiyasi nimaga bog‘liq?", ["yorug‘lik chastotasiga", "yorug‘lik intensivligiga", "yoritish vaqtiga", "katod yuzasiga"], 0, "Eynshteyn tenglamasi."),
       ("Chiqish ishi 4,5 eV. Qizil chegara:", ["≈276 nm", "≈500 nm", "≈700 nm", "≈125 nm"], 0, "1240/4,5."),
       ("To‘yinish fototoki nimaga proporsional?", ["yorug‘lik intensivligiga", "chastotaga", "chiqish ishiga", "tormozlovchi kuchlanishga"], 0, "Fotonlar soniga."),
       ("Kompton effekti nimani tasdiqlaydi?", ["fotonning impulsi borligini", "yorug‘likning to‘lqin tabiatini", "qutblanishni", "dispersiyani"], 0, "Foton–elektron to‘qnashuvi."),
       ("\\(U_z(\\nu)\\) grafigining qiyaligi:", [r"\(h/e\)", r"\(A/e\)", r"\(e/h\)", r"\(c/h\)"], 0, "\\(eU_z=h\\nu-A\\).")],
 blits=["Nima uchun qizdirilgan temir avval qizil, keyin oq rangda nurlanadi?", "Quyosh panellari qaysi hodisaga asoslangan?", "Teplovizor qanday ishlaydi?", "Nima uchun UB nurlar teri uchun xavfli, IQ esa unchalik emas?", "Quyosh yelkani bilan kosmik kema harakatlana oladimi?"]
))

L.append(dict(
 n=24, short="Fotometriya asoslari", sim="photometry", refs=[1, 2, 3, 4, 5], intl=["openstax3", "hecht", "young"], tn=["TN2", "TN9"],
 phet=[("Color Vision", "color-vision")],
 title="Fotometriya asoslari. Yorug‘lik oqimi, yorug‘lik kuchi, yoritilganlik va ravshanlik. Yoritilganlik qonuni",
 goal="Energetik va fotometrik kattaliklar orasidagi farqni, yorug‘lik oqimi, yorug‘lik kuchi, yoritilganlik va ravshanlik tushunchalarini, yoritilganlik qonunlarini hamda fotometrlarning ishlash prinsipini o‘rganish.",
 outcomes=["fotometrik kattaliklarni va ularning birliklarini (lm, kd, lk, kd/m²) farqlaydi;", "nuqtaviy manba hosil qilgan yoritilganlikni masofa va tushish burchagiga qarab hisoblaydi;", "fotometr yordamida ikki manba yorug‘lik kuchlarini taqqoslaydi;", "ish joyi yoritilganligi me’yorlari va manbalar samaradorligini (lm/W) baholaydi."],
 plan=["Energetik va fotometrik kattaliklar. Ko‘zning spektral sezgirligi", "Yorug‘lik oqimi va yorug‘lik kuchi", "Yoritilganlik. Yoritilganlik qonunlari", "Ravshanlik", "Fotometrlar va lyuksmetrlar. Yoritish me’yorlari"],
 terms=["yorug‘lik oqimi \\(\\Phi\\) (lm)", "yorug‘lik kuchi I (kd)", "fazoviy burchak \\(\\Omega\\) (sr)", "yoritilganlik E (lk)", "ravshanlik L (kd/m²)", "yorug‘lik samaradorligi (lm/W)", "fotometr"],
 theory=[
  ("Energetik va fotometrik kattaliklar", r"""<p>Energetik kattaliklar nurlanish energiyasini (W) ifodalaydi; fotometrik kattaliklar esa yorug‘likni ko‘z sezgirligiga qarab baholaydi. Kunduzgi ko‘z 555 nm (yashil) da eng sezgir; 555 nm dagi 1 W monoxromatik nurlanish 683 lm ga teng. Shu sababli bir xil quvvatli qizil va yashil manbalar ko‘zga turlicha yorug‘ ko‘rinadi. SI ning yorug‘likka oid asosiy birligi — <b>kandela</b> (kd).</p>"""),
  ("Yorug‘lik oqimi va yorug‘lik kuchi", r"""<p>Yorug‘lik oqimi \(\Phi\) — ko‘z sezgirligi bilan baholangan nurlanish quvvati (lyumen, lm). Yorug‘lik kuchi — birlik fazoviy burchakka to‘g‘ri keladigan oqim: \(I=d\Phi/d\Omega\) (kd); 1 lm = 1 kd·sr. Barcha yo‘nalishlarda bir tekis nurlanadigan nuqtaviy manba uchun \(\Phi=4\pi I\). Yorug‘lik samaradorligi: cho‘g‘lanma lampa \(\approx15\) lm/W, lyuminessent \(\approx60\) lm/W, LED \(100\)–\(200\) lm/W.</p>"""),
  ("Yoritilganlik qonunlari", r"""<p>Yoritilganlik — sirtga tushgan oqimning yuzaga nisbati: \(E=d\Phi/dS\) (lyuks, 1 lk = 1 lm/m²). Nuqtaviy manba uchun:</p>
$$E=\frac{I\cos\alpha}{r^2}$$
<p>Yoritilganlik masofa kvadratiga teskari proporsional (birinchi qonun) va nurlarning tushish burchagi kosinusiga proporsional (ikkinchi qonun). Taqqoslash uchun: quyoshli kun \(\sim10^5\) lk, xona 300–500 lk, laboratoriya stoli \(\ge500\) lk, to‘lin oy kechasi \(\sim0{,}2\) lk.</p>"""),
  ("Ravshanlik va fotometrlar", r"""<p>Ravshanlik — nurlantiruvchi sirtning birlik ko‘rinma yuzasidan berilgan yo‘nalishdagi yorug‘lik kuchi: \(L=\dfrac{I}{S\cos\theta}\) (kd/m²). Ravshanligi yo‘nalishga bog‘liq bo‘lmagan sirtlar Lambert sirtlari deyiladi. <b>Fotometr</b> ikki manbani taqqoslaydi: ekranning ikki tomoni bir xil yoritilganda \(\dfrac{I_1}{r_1^2}=\dfrac{I_2}{r_2^2}\) — bundan noma’lum manba yorug‘lik kuchi aniqlanadi (Bunzen fotometri). Zamonaviy lyuksmetrlarda fotodiod va ko‘z sezgirligiga moslovchi filtr ishlatiladi.</p>""")],
 chem=["Titrlashda rang o‘tishini aniq kuzatish uchun laboratoriya stoli yoritilganligi me’yorlari (≥ 500 lk) muhim.",
       "Kolorimetriyada eritmalar rangining intensivligini taqqoslash fotometrik prinsiplarga asoslangan.",
       "Lyuminofor va LED materiallarini sintez qilishda yorug‘lik samaradorligi (lm/W) asosiy ko‘rsatkich hisoblanadi."],
 example=[("Stol yoritilganligi", r"Yorug‘lik kuchi 200 kd bo‘lgan lampa stol ustidan 1,5 m balandlikda osilgan. Lampa ostidagi nuqtada va undan 2 m chetdagi nuqtada yoritilganlikni toping.",
           r"Lampa ostida: \(E_1=200/1{,}5^2=89\) lk. Chetdagi nuqta: \(r=\sqrt{1{,}5^2+2^2}=2{,}5\) m, \(\cos\alpha=1{,}5/2{,}5=0{,}6\), \(E_2=200\cdot0{,}6/6{,}25=19{,}2\) lk."),
          ("Fotometr", r"Ikki manba orasidagi masofa 2 m. Yorug‘lik kuchi 100 kd bo‘lgan manbadan 1,33 m masofada ekranning ikki tomoni bir xil yoritildi. Ikkinchi manba yorug‘lik kuchini toping.",
           r"\(\frac{I_1}{r_1^2}=\frac{I_2}{r_2^2}\Rightarrow I_2=100\cdot\frac{0{,}67^2}{1{,}33^2}\approx25\) kd.")],
 simtask=["I₁ = 100 kd, I₂ = 25 kd o‘rnating va ekranni muvozanat nuqtasiga suring; uni formula bilan tekshiring.", "Tushish burchagini 0° dan 60° gacha oshiring: E necha marta kamayadi?", "Bitta manbadan masofa 2 marta oshirilganda E ning 4 marta kamayishini grafikdan tekshiring."],
 mistakes=[("“Ko‘p vattli lampa doim yorug‘roq.”", "Yorug‘lik oqimi samaradorlikka bog‘liq: 10 W LED 60 W cho‘g‘lanma lampadan yorug‘roq bo‘lishi mumkin."),
           ("“Masofa 2 marta oshsa, yoritilganlik 2 marta kamayadi.”", "Nuqtaviy manba uchun 4 marta kamayadi (\\(E\\propto1/r^2\\))."),
           ("“Yoritilganlik va ravshanlik bir xil narsa.”", "Yoritilganlik sirtga tushayotgan, ravshanlik esa sirtdan chiqayotgan (ko‘zga ko‘rinadigan) yorug‘likni tavsiflaydi.")],
 ai=AI.format(t="fotometriya", b="1) Yorug‘lik oqimi, yorug‘lik kuchi, yoritilganlik va ravshanlik orasidagi bog‘lanishlarni chizma bilan tushuntirishga yordam ber.\n2) Python’da xona shiftidagi 4 ta lampa hosil qilgan stol yoritilganligi xaritasini (E(x, y)) hisoblab, rang shkalasida chiz."),
 quiz=[("Yorug‘lik kuchining birligi:", ["kandela", "lyumen", "lyuks", "vatt"], 0, "SI asosiy birligi."),
       ("Yoritilganlik birligi:", ["lyuks", "kandela", "lyumen", "nit"], 0, "1 lk = 1 lm/m²."),
       ("Masofa 3 marta oshsa, yoritilganlik:", ["9 marta kamayadi", "3 marta kamayadi", "9 marta ortadi", "o‘zgarmaydi"], 0, "E ∝ 1/r²."),
       ("100 kd manbadan 2 m masofada (nurlar perpendikulyar) yoritilganlik:", ["25 lk", "50 lk", "200 lk", "100 lk"], 0, "100/4."),
       ("Nuqtaviy izotrop manbaning to‘la yorug‘lik oqimi:", [r"\(4\pi I\)", r"\(2\pi I\)", r"\(I\)", r"\(\pi I\)"], 0, "To‘liq fazoviy burchak 4π sr."),
       ("Ko‘z eng sezgir bo‘lgan to‘lqin uzunligi:", ["≈555 nm", "≈400 nm", "≈700 nm", "≈1000 nm"], 0, "Yashil."),
       ("Nurlar 60° burchak ostida tushsa, yoritilganlik perpendikulyar tushishdagiga nisbatan:", ["2 marta kam", "o‘zgarmaydi", "4 marta kam", "√3 marta kam"], 0, "cos 60° = 0,5."),
       ("Qaysi manbaning yorug‘lik samaradorligi eng yuqori?", ["LED", "cho‘g‘lanma lampa", "sham", "galogen lampa"], 0, "100–200 lm/W."),
       ("Fotometrda muvozanat sharti:", [r"\(I_1/r_1^2=I_2/r_2^2\)", r"\(I_1r_1=I_2r_2\)", r"\(I_1=I_2\)", r"\(r_1=r_2\)"], 0, "Yoritilganliklar tengligi."),
       ("1 lk ga teng:", ["1 lm/m²", "1 kd/m²", "1 W/m²", "1 lm·sr"], 0, "Ta’rif bo‘yicha.")],
 blits=["Nima uchun qishda Quyosh kamroq isitadi (tushish burchagi)?", "LED lampaning “60 W ekvivalenti” nimani anglatadi?", "Telefon kamerasini lyuksmetr sifatida ishlatish mumkinmi?", "Kitob o‘qish uchun qancha yoritilganlik kerak?", "Ko‘z qorong‘ida ranglarni nima uchun yomon farqlaydi?"]
))
