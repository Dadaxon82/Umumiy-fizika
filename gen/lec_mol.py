"""II modul. Molekulyar fizika va termodinamika: M8–M11 ma'ruzalar mazmuni."""
from lec_mex import AI

L = []

L.append(dict(
 n=8, short="Molekulyar-kinetik nazariya asoslari", sim="maxwell", refs=[2, 3, 4, 5], intl=["schroeder", "atkins", "openstax2"], tn=["TN1", "TN7"],
 phet=[("Gas Properties", "gas-properties"), ("States of Matter", "states-of-matter")],
 title="Molekulyar-kinetik nazariya asoslari. Modda miqdori, temperatura. MKN ning asosiy tenglamasi",
 goal="Modda tuzilishining molekulyar-kinetik tasavvurlarini, modda miqdori, molyar massa, Avogadro doimiysi va temperatura tushunchalarini, molekulalarning o‘rtacha kvadratik tezligi va o‘rtacha kinetik energiyasini hamda MKN ning asosiy tenglamasini o‘rganish.",
 outcomes=["modda miqdori, molekulalar soni va massasini o‘zaro bog‘lab hisoblaydi;", "MKN asosiy tenglamasini keltirib chiqarish g‘oyasini tushuntiradi;", "temperaturaning molekulyar ma’nosini va uning o‘rtacha kinetik energiya bilan bog‘lanishini izohlaydi;", "gaz molekulalarining o‘rtacha kvadratik, o‘rtacha va eng ehtimolli tezliklarini hisoblaydi."],
 plan=["MKN ning asosiy qoidalari va tajribaviy asoslari (Broun harakati, diffuziya)", "Modda miqdori, molyar massa, Avogadro doimiysi", "Temperatura va termodinamik muvozanat", "Molekulalarning o‘rtacha kvadratik tezligi va o‘rtacha kinetik energiyasi", "MKN asosiy tenglamasi. Maksvell taqsimoti"],
 terms=["modda miqdori ν", "molyar massa M", "Avogadro doimiysi \\(N_A\\)", "Boltsman doimiysi k", "absolyut temperatura T", "o‘rtacha kvadratik tezlik", "Maksvell taqsimoti"],
 theory=[
  ("MKN ning asosiy qoidalari", r"""<p>Molekulyar-kinetik nazariya (MKN) uchta qoidaga tayanadi: 1) modda molekula va atomlardan iborat; 2) zarralar uzluksiz tartibsiz (issiqlik) harakatda; 3) zarralar o‘zaro ta’sirlashadi — kichik masofalarda itarishadi, kattaroq masofalarda tortishadi. Tajribaviy dalillar: Broun harakati (1827; nazariyasi Eynshteyn va Smoluxovskiy, 1905–1906; Perren tajribalari \(N_A\) ni aniqladi), diffuziya, gazlarning bosimi va issiqlikdan kengayishi.</p>"""),
  ("Modda miqdori va molyar massa", r"""<p>Modda miqdori \(\nu=N/N_A=m/M\) (mol), bu yerda \(N_A=6{,}022\,140\,76\cdot10^{23}\) mol⁻¹ — Avogadro doimiysi (2019-yildan aniq qiymat), \(M\) — molyar massa (kg/mol). Bitta molekula massasi \(m_0=M/N_A\). Masalan, suv uchun \(M=0{,}018\) kg/mol, \(m_0=3\cdot10^{-26}\) kg; 1 g suvda \(3{,}3\cdot10^{22}\) ta molekula bor.</p>"""),
  ("MKN asosiy tenglamasi va temperatura", r"""<p>Ideal gaz molekulalarining idish devoriga urilishlari natijasida bosim hosil bo‘ladi:</p>
$$p=\frac13n m_0\langle v^2\rangle=\frac23n\langle E_k\rangle,\qquad \langle E_k\rangle=\frac32kT$$
<p>bu yerda \(n=N/V\) — molekulalar konsentratsiyasi, \(k=1{,}380\,649\cdot10^{-23}\) J/K — Boltsman doimiysi. Demak <b>absolyut temperatura molekulalar ilgarilanma harakati o‘rtacha kinetik energiyasining o‘lchovidir</b>; bundan \(p=nkT\). Temperatura shkalalari bog‘lanishi: \(T=t+273{,}15\) K. Tenglamani keltirib chiqarish g‘oyasi: bitta molekula devorga urilganda uning impulsi \(2m_0v_x\) ga o‘zgaradi; \(\Delta t\) vaqtda devorga uriladigan molekulalar sonini hisoblab, to‘liq kuchni yuzaga bo‘lamiz.</p>"""),
  ("Molekulalar tezliklari. Maksvell taqsimoti", r"""<p>O‘rtacha kvadratik tezlik \(v_\text{kv}=\sqrt{3kT/m_0}=\sqrt{3RT/M}\) (\(R=kN_A=8{,}314\) J/(mol·K)). Molekulalar tezliklari bo‘yicha Maksvell taqsimotiga bo‘ysunadi; uning uchta xarakterli tezligi:</p>
$$v_\text{eh}=\sqrt{\frac{2RT}{M}},\qquad \langle v\rangle=\sqrt{\frac{8RT}{\pi M}},\qquad v_\text{kv}=\sqrt{\frac{3RT}{M}}$$
<p>Masalan, 0 °C da azot molekulalari uchun \(v_\text{kv}\approx493\) m/s, vodorod uchun \(\approx1840\) m/s. Temperatura ortishi bilan taqsimot kengayib, katta tezliklar tomon siljiydi. Molekulalar tezligini birinchi marta Shtern tajribasi (1920) bevosita o‘lchagan.</p>""")],
 chem=["Mol tushunchasi stexiometriyaning asosi: reaksiya tenglamasidagi koeffitsiyentlar moddalar miqdorlari nisbatini beradi.",
       "Arrenius tenglamasi \\(k=Ae^{-E_a/RT}\\) dagi eksponenta Maksvell–Boltsman taqsimotida energiyasi \\(E_a\\) dan katta molekulalar ulushini ifodalaydi.",
       "Graham qonuni (effuziya tezligi \\(\\propto1/\\sqrt M\\)) izotoplarni gaz diffuziyasi usulida ajratishda qo‘llanilgan."],
 example=[("Molekulalar soni va o‘lchami", r"1 L suvda nechta molekula bor? Bitta molekula massasi va o‘lchamini baholang (\(\rho=1000\) kg/m³).",
           r"\(m=1\) kg, \(\nu=m/M=55{,}6\) mol, \(N=\nu N_A=3{,}35\cdot10^{25}\). \(m_0=M/N_A=3\cdot10^{-26}\) kg. Bitta molekulaga to‘g‘ri keladigan hajm \(V/N=3\cdot10^{-29}\) m³, o‘lcham \(d\approx\sqrt[3]{3\cdot10^{-29}}\approx3\cdot10^{-10}\) m = 0,3 nm."),
          ("Gaz molekulalari energiyasi va bosim", r"27 °C da azot molekulalarining o‘rtacha kinetik energiyasi va o‘rtacha kvadratik tezligini toping. Konsentratsiya \(n=2{,}5\cdot10^{25}\) m⁻³ bo‘lsa, bosim qancha?",
           r"\(T=300\) K. \(\langle E_k\rangle=1{,}5kT=6{,}2\cdot10^{-21}\) J. \(v_\text{kv}=\sqrt{3\cdot8{,}314\cdot300/0{,}028}=517\) m/s. \(p=nkT=2{,}5\cdot10^{25}\cdot1{,}38\cdot10^{-23}\cdot300\approx1{,}04\cdot10^5\) Pa — atmosfera bosimiga yaqin.")],
 simtask=["Azot uchun T ni 300 K dan 1200 K gacha oshiring: tezliklar necha marta ortdi? Nazariy javob bilan solishtiring.", "Bir xil T da H₂ va CO₂ taqsimotlarini solishtiring va farqni molyar massa orqali izohlang.", "Egri chiziq ostidagi yuza nima uchun T ga bog‘liq emas? Taqsimotning normallanishini tushuntiring."],
 mistakes=[("“Temperatura — issiqlik miqdori.”", "Temperatura — o‘rtacha kinetik energiya o‘lchovi; issiqlik miqdori — energiya uzatish shakli."),
           ("“Gazning barcha molekulalari bir xil tezlikda harakatlanadi.”", "Tezliklar Maksvell taqsimotiga ega; bir xil T da ular keng oraliqda tarqalgan."),
           ("“0 °C da molekulalar harakati to‘xtaydi.”", "0 °C = 273 K; harakat mavjud. Hatto absolyut nolda ham kvant (nol nuqta) tebranishlari qoladi.")],
 ai=AI.format(t="molekulyar-kinetik nazariya", b="1) MKN asosiy tenglamasini devorga urilayotgan molekulalar impulsi orqali keltirib chiqarishga yordam ber.\n2) Python’da Maksvell taqsimotidan tasodifiy tezliklar generatsiya qilib (numpy), histogrammani nazariy egri bilan solishtir va ⟨v⟩, v_kv ni hisobla."),
 quiz=[("1 mol moddadagi zarralar soni:", ["6,02·10²³", "3,0·10²³", "1,38·10⁻²³", "8,31"], 0, "Avogadro doimiysi."),
       ("44 g CO₂ da modda miqdori:", ["1 mol", "2 mol", "0,5 mol", "44 mol"], 0, "M = 44 g/mol."),
       ("Absolyut temperatura 2 marta ortsa, molekulalarning o‘rtacha kinetik energiyasi:", ["2 marta ortadi", "4 marta ortadi", "√2 marta ortadi", "o‘zgarmaydi"], 0, "⟨E⟩ = 3kT/2."),
       ("Absolyut temperatura 4 marta ortsa, o‘rtacha kvadratik tezlik:", ["2 marta ortadi", "4 marta ortadi", "16 marta ortadi", "o‘zgarmaydi"], 0, r"\(v\propto\sqrt T\)."),
       ("27 °C ga mos absolyut temperatura:", ["300 K", "246 K", "27 K", "327 K"], 0, "T = t + 273."),
       ("MKN ning asosiy tenglamasi:", [r"\(p=\frac23n\langle E_k\rangle\)", r"\(p=nRT\)", r"\(pV=\text{const}\)", r"\(p=\rho gh\)"], 0, "Bosim — molekulalar zarbalarining natijasi."),
       ("Bir xil temperaturada qaysi gaz molekulalarining o‘rtacha tezligi eng katta?", ["H₂", "O₂", "CO₂", "N₂"], 0, "Eng kichik molyar massa."),
       ("Broun harakatining sababi:", ["suyuqlik molekulalarining zarraga tartibsiz urilishlari", "zarralarning o‘zaro tortishishi", "konveksiya oqimlari", "yorug‘lik bosimi"], 0, "Urilishlar muvozanatlashmaydi."),
       ("Boltsman doimiysi va gaz doimiysi orasidagi bog‘lanish:", [r"\(R=kN_A\)", r"\(k=RN_A\)", r"\(R=k/N_A\)", r"\(k=R+N_A\)"], 0, "R = 1,38·10⁻²³·6,02·10²³ ≈ 8,31."),
       ("Normal sharoitda gaz molekulalari konsentratsiyasi (Loshmidt soni) tartibi:", ["≈2,7·10²⁵ m⁻³", "≈6·10²³ m⁻³", "≈10³⁰ m⁻³", "≈10¹⁰ m⁻³"], 0, "n = p/(kT).")],
 blits=["Molekulalar tezligi yuzlab m/s bo‘lsa ham, hid xonaga nima uchun asta-sekin tarqaladi?", "Temperaturaning eng kichik qiymati bormi?", "Nima uchun yengil gazlar (H₂, He) Yer atmosferasini tark etadi?", "Ideal gaz modelida molekulalarning o‘zaro ta’siri hisobga olinadimi?", "Avogadro doimiysini qanday tajribalar orqali aniqlash mumkin?"]
))

L.append(dict(
 n=9, short="Ideal gaz qonunlari", sim="gas", refs=[2, 3, 4, 5], intl=["openstax2", "atkins", "schroeder"], tn=["TN6", "TN7"],
 phet=[("Gas Properties", "gas-properties")],
 title="Ideal gaz qonunlari. Mendeleyev–Klapeyron tenglamasi. Izojarayonlar. Dalton qonuni. Havo namligi",
 goal="Ideal gaz modeli, Mendeleyev–Klapeyron holat tenglamasi, izojarayonlar (Boyl–Mariott, Gey-Lyussak, Sharl qonunlari), Dalton qonuni, absolyut va nisbiy namlik hamda namlikni o‘lchash usullarini o‘rganish.",
 outcomes=["holat tenglamasidan gaz parametrlarini hisoblaydi;", "izojarayonlarni p–V, p–T, V–T diagrammalarda tasvirlaydi;", "gazlar aralashmasi uchun Dalton qonunini qo‘llaydi;", "absolyut va nisbiy namlikni, shudring nuqtasini hisoblaydi va psixrometr ishlash prinsipini tushuntiradi."],
 plan=["Ideal gaz modeli va holat parametrlari", "Mendeleyev–Klapeyron tenglamasi", "Izojarayonlar: izotermik, izobarik, izoxorik", "Gazlar aralashmasi. Dalton qonuni", "Absolyut va nisbiy namlik. Namlikni o‘lchash usullari"],
 terms=["ideal gaz", "holat tenglamasi \\(pV=\\nu RT\\)", "izoterma", "izobara", "izoxora", "parsial bosim", "nisbiy namlik \\(\\varphi\\)"],
 theory=[
  ("Ideal gaz va holat tenglamasi", r"""<p><b>Ideal gaz</b> — molekulalari moddiy nuqta deb qaraladigan va to‘qnashuvlardan tashqari o‘zaro ta’sirlashmaydigan gaz modeli. Siyrak real gazlar (normal sharoitdagi havo, N₂, O₂, He) unga yaxshi bo‘ysunadi. MKN tenglamasi \(p=nkT\) dan Mendeleyev–Klapeyron tenglamasi kelib chiqadi:</p>
$$pV=\nu RT=\frac mMRT,\qquad R=8{,}314\ \text{J/(mol·K)}$$
<p>Normal sharoitda (\(p_0=101\,325\) Pa, \(T_0=273{,}15\) K) 1 mol ideal gaz hajmi \(V_m=22{,}4\) L.</p>"""),
  ("Izojarayonlar", r"""<p>Gaz massasi o‘zgarmas va bitta parametr doimiy bo‘lgan jarayonlar:</p>
$$T=\text{const}:\ pV=\text{const};\qquad p=\text{const}:\ \frac VT=\text{const};\qquad V=\text{const}:\ \frac pT=\text{const}$$
<p>Mos ravishda Boyl–Mariott (izotermik), Gey-Lyussak (izobarik) va Sharl (izoxorik) qonunlari. p–V diagrammada izoterma — giperbola, izobara — gorizontal, izoxora — vertikal to‘g‘ri chiziq. Holat tenglamasining umumlashgan shakli: \(\dfrac{p_1V_1}{T_1}=\dfrac{p_2V_2}{T_2}\).</p>"""),
  ("Dalton qonuni", r"""<p>O‘zaro kimyoviy reaksiyaga kirishmaydigan gazlar aralashmasining bosimi komponentlarning parsial bosimlari yig‘indisiga teng: \(p=\sum p_i\), \(p_i=\nu_iRT/V\). Komponent ulushi: \(p_i/p=\nu_i/\nu=x_i\) (molyar ulush). Masalan, havoda kislorodning parsial bosimi \(\approx0{,}21\cdot101\) kPa \(\approx21\) kPa.</p>"""),
  ("Havo namligi va uni o‘lchash", r"""<p><b>Absolyut namlik</b> \(\rho\) — 1 m³ havodagi suv bug‘i massasi (g/m³). <b>Nisbiy namlik</b> — bug‘ parsial bosimining shu temperaturadagi to‘yingan bug‘ bosimiga nisbati:</p>
$$\varphi=\frac{p}{p_\text{t}}\cdot100\,\%=\frac{\rho}{\rho_\text{t}}\cdot100\,\%$$
<p>Havo soviganda bug‘ to‘yinadigan temperatura — <b>shudring nuqtasi</b>. O‘lchash usullari: kondensatsion gigrometr (shudring nuqtasi bo‘yicha), sochli gigrometr, <b>psixrometr</b> (quruq va ho‘l termometrlar ko‘rsatishlari farqi bo‘yicha jadvaldan), elektron sig‘im datchiklari. To‘yingan bug‘ bosimi temperaturaga kuchli bog‘liq: 20 °C da 2,34 kPa, 30 °C da 4,25 kPa, 100 °C da 101,3 kPa (L11).</p>""")],
 chem=["Gazlar bilan bog‘liq stexiometrik hisoblar holat tenglamasiga tayanadi: reaksiyada ajralgan gaz hajmidan modda miqdori topiladi.",
       "Gaz fazadagi muvozanat konstantasi \\(K_p\\) parsial bosimlar orqali ifodalanadi; bosimning muvozanatga ta’siri Le Shatelye prinsipi bilan tahlil qilinadi.",
       "Gigroskopik moddalarni saqlash va quritish (eksikator) nisbiy namlik tushunchasiga asoslanadi."],
 example=[("Ballondagi kislorod", r"Hajmi 40 L bo‘lgan ballonda 27 °C da 15 MPa bosim ostida kislorod bor. Kislorod massasini toping. Temperatura 7 °C gacha pasaysa, bosim qancha bo‘ladi?",
           r"\(m=\frac{pVM}{RT}=\frac{15\cdot10^6\cdot0{,}04\cdot0{,}032}{8{,}314\cdot300}=7{,}7\) kg. Izoxorik jarayon: \(p_2=p_1T_2/T_1=15\cdot280/300=14\) MPa."),
          ("Nisbiy namlik", r"Xonada temperatura 25 °C, shudring nuqtasi 15 °C. To‘yingan bug‘ bosimlari: 25 °C da 3,17 kPa, 15 °C da 1,71 kPa. Nisbiy namlikni toping.",
           r"Havodagi bug‘ bosimi shudring nuqtasidagi to‘yingan bug‘ bosimiga teng: \(p=1{,}71\) kPa. \(\varphi=1{,}71/3{,}17=0{,}54\), ya’ni 54 %.")],
 simtask=["Izotermik jarayonda V₂/V₁ = 2 bo‘lganda p₂ = p₁/2 ekanini tekshiring.", "Izobarik va izoxorik jarayonlarda bir xil x = 2 uchun gaz bajargan ishni solishtiring va izohlang.", "Bir atomli va ikki atomli gazlar uchun adiabata qiyaligini (γ) taqqoslang."],
 mistakes=[("“Holat tenglamasiga temperaturani °C da qo‘yish mumkin.”", "Faqat absolyut temperatura (K) ishlatiladi."),
           ("“Nisbiy namlik 100 % bo‘lsa, havo suvdan iborat.”", "Bu faqat bug‘ to‘yinganligini bildiradi; bug‘ ulushi baribir kichik (20 °C da taxminan 2 %)."),
           ("“Izotermik siqishda gaz isiydi.”", "Ideal gazda T o‘zgarmaydi; bajarilgan ish issiqlik sifatida atrofga uzatiladi.")],
 ai=AI.format(t="ideal gaz qonunlari va havo namligi", b="1) Uchta izojarayonni bitta holat tenglamasidan keltirib chiqarishga yordam ber.\n2) Python’da to‘yingan bug‘ bosimini Magnus formulasi bilan hisoblab, berilgan t va shudring nuqtasi bo‘yicha nisbiy namlikni topadigan funksiya yoz; formulaning aniqlik chegarasini ko‘rsat."),
 quiz=[("pV = νRT tenglamasi qanday nomlanadi?", ["Mendeleyev–Klapeyron", "Boyl–Mariott", "Van-der-Vaals", "Puasson"], 0, "Ideal gaz holat tenglamasi."),
       ("Izotermik jarayonda hajm 3 marta kamaysa, bosim:", ["3 marta ortadi", "3 marta kamayadi", "9 marta ortadi", "o‘zgarmaydi"], 0, "pV = const."),
       ("Normal sharoitda 1 mol ideal gaz hajmi:", ["22,4 L", "1 L", "24,5 L", "8,31 L"], 0, "V = RT/p."),
       ("Izobarik jarayonda T 2 marta ortsa, hajm:", ["2 marta ortadi", "2 marta kamayadi", "4 marta ortadi", "o‘zgarmaydi"], 0, "V/T = const."),
       ("Dalton qonuniga ko‘ra aralashma bosimi:", ["parsial bosimlar yig‘indisiga teng", "eng katta parsial bosimga teng", "parsial bosimlar ko‘paytmasiga teng", "o‘rtacha parsial bosimga teng"], 0, "p = Σpᵢ."),
       ("Sharl qonuni qaysi jarayonni tavsiflaydi?", ["izoxorik", "izobarik", "izotermik", "adiabatik"], 0, "p/T = const."),
       ("Shudring nuqtasi nima?", ["havodagi bug‘ to‘yinadigan temperatura", "suv qaynaydigan temperatura", "muz eriydigan temperatura", "nisbiy namlik 0 % bo‘ladigan temperatura"], 0, "Bug‘ kondensatsiyalana boshlaydi."),
       ("Psixrometrda ho‘l termometr quruqdan past ko‘rsatadi, chunki:", ["bug‘lanish issiqlik yutadi", "suv yaxshiroq isiydi", "u boshqa suyuqlik bilan to‘ldirilgan", "u quyosh nurida turadi"], 0, "Havo qanchalik quruq bo‘lsa, farq shunchalik katta."),
       ("Ballonda gaz 300 K da 10 MPa bosimda. 600 K da bosim (V = const):", ["20 MPa", "5 MPa", "10 MPa", "40 MPa"], 0, "p/T = const."),
       ("Havoda O₂ ning molyar ulushi 0,21. 100 kPa da uning parsial bosimi:", ["21 kPa", "79 kPa", "100 kPa", "2,1 kPa"], 0, "pᵢ = xᵢp.")],
 blits=["Nima uchun shinalardagi bosim qishda kamayadi?", "Tog‘ cho‘qqisida suv nima uchun pastroq temperaturada qaynaydi?", "Real gaz qachon ideal gazdan sezilarli farq qiladi?", "Ertalab o‘tlarda shudring nima uchun hosil bo‘ladi?", "Yopiq idishdagi gazga boshqa gaz qo‘shsak, Dalton qonuni qanday ishlaydi?"]
))

L.append(dict(
 n=10, short="Termodinamika asoslari", sim="calorimeter", refs=[2, 3, 4, 5], intl=["schroeder", "atkins", "openstax2"], tn=["TN3", "TN6", "TN7"],
 phet=[("Energy Forms and Changes", "energy-forms-and-changes"), ("Gas Properties", "gas-properties")],
 title="Termodinamika asoslari. Ichki energiya, issiqlik miqdori va ish. Termodinamikaning birinchi qonuni. Adiabatik jarayon",
 goal="Ichki energiya, issiqlik miqdori va gazning kengayishda bajargan ishi tushunchalarini, termodinamikaning birinchi qonunini, gazning issiqlik sig‘imi va uning jarayon turiga bog‘liqligini, birinchi qonunni izojarayonlarga qo‘llashni hamda adiabatik jarayon va Puasson tenglamasini o‘rganish.",
 outcomes=["ichki energiyani erkinlik darajalari soni orqali hisoblaydi;", "gaz ishini p–V diagrammadagi yuza sifatida topadi;", "birinchi qonunni izojarayonlarga qo‘llab Q, A va ΔU ni hisoblaydi;", "\\(C_p\\), \\(C_V\\) va γ ni gaz turiga qarab hisoblaydi, Puasson tenglamasini qo‘llaydi."],
 plan=["Ichki energiya. Energiyaning erkinlik darajalari bo‘yicha teng taqsimlanishi", "Issiqlik miqdori va issiqlik sig‘imi. Issiqlik balansi", "Gazning kengayishida bajarilgan ish", "Termodinamikaning birinchi qonuni va uni izojarayonlarga qo‘llash", "Adiabatik jarayon. Puasson tenglamasi"],
 terms=["ichki energiya U", "erkinlik darajalari soni i", "issiqlik miqdori Q", "solishtirma issiqlik sig‘imi c", "molyar issiqlik sig‘imlari \\(C_V\\), \\(C_p\\)", "Mayer tenglamasi", "adiabata ko‘rsatkichi \\(\\gamma\\)"],
 theory=[
  ("Ichki energiya", r"""<p>Ideal gazning ichki energiyasi molekulalar issiqlik harakati kinetik energiyalarining yig‘indisi. Energiya erkinlik darajalari bo‘yicha teng taqsimlanadi: har bir darajaga o‘rtacha \(kT/2\) to‘g‘ri keladi. Bir atomli gazda \(i=3\), ikki atomlida \(i=5\) (3 ilgarilanma + 2 aylanma), ko‘p atomlida \(i=6\):</p>
$$U=\frac i2\nu RT$$
<p>Ichki energiya — holat funksiyasi: uning o‘zgarishi faqat boshlang‘ich va oxirgi holatga bog‘liq.</p>"""),
  ("Issiqlik miqdori va issiqlik sig‘imi", r"""<p>Issiqlik miqdori — issiqlik almashinuvida uzatilgan energiya: \(Q=cm\Delta T\), bu yerda \(c\) — solishtirma issiqlik sig‘imi (suv uchun 4186 J/(kg·K), alyuminiy 900, mis 385). Fazaviy o‘tishlarda: erishda \(Q=\lambda m\), bug‘lanishda \(Q=rm\). Issiqlikdan izolyatsiyalangan sistemada <b>issiqlik balansi</b> bajariladi: \(\sum Q_i=0\) — kalorimetriyaning asosi (L12–L14).</p>"""),
  ("Gaz ishi va termodinamikaning birinchi qonuni", r"""<p>Gaz kengayganda bajargan ish \(\delta A=p\,dV\), \(A=\int_{V_1}^{V_2}p\,dV\) — p–V diagrammadagi egri chiziq ostidagi yuza; u jarayon yo‘liga bog‘liq. <b>Termodinamikaning birinchi qonuni</b> — energiya saqlanish qonuni:</p>
$$Q=\Delta U+A$$
<p>Izojarayonlarga qo‘llash: izoxorik \(A=0\), \(Q=\Delta U=\nu C_V\Delta T\); izobarik \(Q=\nu C_p\Delta T\), \(A=p\Delta V=\nu R\Delta T\); izotermik \(\Delta U=0\), \(Q=A=\nu RT\ln(V_2/V_1)\). Molyar issiqlik sig‘imlari: \(C_V=\frac i2R\), \(C_p=C_V+R\) (Mayer tenglamasi).</p>"""),
  ("Adiabatik jarayon. Puasson tenglamasi", r"""<p>Issiqlik almashinuvisiz (\(Q=0\)) jarayonda gaz ichki energiyasi hisobiga ish bajaradi: \(A=-\Delta U\). Ideal gaz uchun Puasson tenglamasi:</p>
$$pV^\gamma=\text{const},\qquad TV^{\gamma-1}=\text{const},\qquad \gamma=\frac{C_p}{C_V}=\frac{i+2}{i}$$
<p>Bir atomli gazda \(\gamma=5/3\), ikki atomlida 1,4. p–V diagrammada adiabata izotermadan tikroq. Tez jarayonlar (tovush to‘lqinidagi siqilish, dizel dvigatelida siqish, Kleman–Dezorm tajribasi — L15–L16) adiabatik deb qaraladi.</p>""")],
 chem=["Termokimyoda reaksiya issiqligi: o‘zgarmas hajmda \\(Q_V=\\Delta U\\), o‘zgarmas bosimda \\(Q_p=\\Delta H\\) (entalpiya); ideal gazlar uchun \\(\\Delta H=\\Delta U+\\Delta\\nu_\\text{gaz}RT\\).",
       "Kalorimetrik bomba bilan yonish issiqligini o‘lchash issiqlik balansiga asoslangan.",
       "Issiqlik sig‘imlari nisbati \\(\\gamma\\) molekuladagi atomlar soni (erkinlik darajalari) haqida ma’lumot beradi."],
 example=[("Izobarik isitish", r"0,5 mol azot (i = 5) o‘zgarmas bosimda 300 K dan 400 K gacha isitildi. Q, A va ΔU ni toping.",
           r"\(\Delta U=\nu\frac52R\Delta T=0{,}5\cdot2{,}5\cdot8{,}314\cdot100=1039\) J. \(A=\nu R\Delta T=416\) J. \(Q=\nu\frac72R\Delta T=1455\) J. Tekshiruv: \(Q=\Delta U+A\)."),
          ("Issiqlik balansi", r"200 g suvli (20 °C) kalorimetrga (\(C_k=40\) J/K) 100 °C gacha qizdirilgan 100 g alyuminiy tushirildi. Muvozanat temperaturasini toping.",
           r"\((4186\cdot0{,}2+40)(\theta-20)=900\cdot0{,}1\,(100-\theta)\Rightarrow877{,}2(\theta-20)=90(100-\theta)\Rightarrow\theta=\frac{17544+9000}{967{,}2}\approx27{,}4\) °C.")],
 simtask=["2-misol qiymatlarini modelga kiriting va θ ni qo‘lda hisob bilan solishtiring.", "Kalorimetr issiqlik sig‘imini 0 dan 200 J/K gacha o‘zgartiring: natijaga ta’siri qanchalik katta?", "Model ko‘rsatgan c qiymati jadval qiymatiga tengligini tekshiring va bu formula laboratoriyada nima uchun kerakligini tushuntiring."],
 mistakes=[("“Issiqlik miqdori — jismdagi energiya.”", "Jismda ichki energiya bor; issiqlik — uzatish jarayonida uzatilgan energiya."),
           ("“Adiabatik jarayonda temperatura o‘zgarmaydi.”", "Aksincha: Q = 0 bo‘lgani uchun kengayishda gaz soviydi, siqilishda isiydi."),
           ("“Gaz ishi faqat boshlang‘ich va oxirgi holatga bog‘liq.”", "Ish jarayon yo‘liga bog‘liq; holat funksiyasi faqat ichki energiya.")],
 ai=AI.format(t="termodinamikaning birinchi qonuni", b="1) Izobarik, izoxorik, izotermik va adiabatik jarayonlar uchun Q, A, ΔU jadvalini tuzishga yordam ber.\n2) Python’da bir xil V₁ → 2V₁ kengayish uchun izoterma va adiabatani p–V diagrammada chizib, ishlar farqini hisobla."),
 quiz=[("Termodinamikaning birinchi qonuni:", [r"\(Q=\Delta U+A\)", r"\(Q=\Delta U-A\)", r"\(A=Q+\Delta U\)", r"\(\Delta U=Q+pV\)"], 0, "A — gaz bajargan ish."),
       ("Izoxorik jarayonda gaz bajargan ish:", ["nolga teng", "pΔV", "νRT ln2", "Q ga teng"], 0, "V = const."),
       ("Bir atomli ideal gazning molyar issiqlik sig‘imi \\(C_V\\):", ["3R/2", "5R/2", "R", "3R"], 0, "i = 3."),
       ("Ikki atomli gaz uchun γ:", ["1,4", "1,67", "1,33", "2"], 0, "(i + 2)/i = 7/5."),
       ("Adiabatik kengayishda gaz:", ["soviydi", "isiydi", "temperaturasi o‘zgarmaydi", "issiqlik oladi"], 0, "A = −ΔU > 0."),
       ("Izotermik kengayishda gaz olgan issiqlik:", ["to‘liq ishga sarflanadi", "to‘liq ichki energiyaga aylanadi", "nolga teng", "yarmi ishga sarflanadi"], 0, "ΔU = 0."),
       ("2 kg suvni 10 °C dan 60 °C gacha isitish uchun kerakli issiqlik (c = 4200 J/(kg·K)):", ["420 kJ", "42 kJ", "84 kJ", "840 kJ"], 0, "Q = cmΔT."),
       ("Mayer tenglamasi:", [r"\(C_p-C_V=R\)", r"\(C_p+C_V=R\)", r"\(C_p/C_V=R\)", r"\(C_pC_V=R\)"], 0, "Izobarik isitishda qo‘shimcha ish bajariladi."),
       ("p–V diagrammada gaz bajargan ish:", ["egri chiziq ostidagi yuza", "egri chiziq qiyaligi", "nuqta koordinatasi", "izoterma uzunligi"], 0, r"\(A=\int p\,dV\)."),
       ("Puasson tenglamasi:", [r"\(pV^\gamma=\text{const}\)", r"\(pV=\text{const}\)", r"\(p/T=\text{const}\)", r"\(V/T=\text{const}\)"], 0, "Adiabatik jarayon uchun.")],
 blits=["Velosiped nasosi nima uchun qiziydi?", "Nima uchun \\(C_p>C_V\\)?", "Choynakdagi suvni qaynatish uchun ketgan issiqlikni qanday baholaysiz?", "Ideal gaz ichki energiyasi qaysi kattaliklarga bog‘liq?", "Dengiz shabadasi qanday paydo bo‘ladi (suv va qum issiqlik sig‘imi)?"]
))

L.append(dict(
 n=11, short="Suyuqlik va gazlarning xossalari", sim="capillary", refs=[1, 2, 3, 4], intl=["openstax1", "halliday", "atkins"], tn=["TN1", "TN7"],
 phet=[("Under Pressure", "under-pressure"), ("Buoyancy", "buoyancy"), ("Density", "density")],
 title="Suyuqlik va gazlarning umumiy xossalari: bosim, Paskal va Arximed qonunlari, Bernulli tenglamasi, qovushqoqlik, sirt taranglik va kapillyar hodisalar",
 goal="Modda fazalari, zichlik, suyuqlik va gazlardagi bosim, Paskal va Arximed qonunlari, bosimni o‘lchash, Bernulli tenglamasi, qovushqoqlik va laminar oqim, sirt taranglik, ho‘llash, Laplas formulasi va kapillyar hodisalarni o‘rganish.",
 outcomes=["gidrostatik bosimni hisoblaydi, Paskal va Arximed qonunlarini qo‘llaydi;", "uzluksizlik va Bernulli tenglamalaridan oqim tezligi va bosimni topadi;", "qovushqoqlik, laminar va turbulent oqimni, Stoks kuchini tushuntiradi;", "sirt taranglik koeffitsiyenti, Laplas bosimi va kapillyar ko‘tarilish balandligini hisoblaydi."],
 plan=["Modda fazalari. Zichlik. Suyuqlik va gazlardagi bosim", "Atmosfera va manometrik bosim. Paskal qonuni. Barometr va manometrlar", "Ko‘taruvchi kuch. Arximed qonuni", "Bernulli tenglamasi. Qovushqoqlik. Laminar oqim", "Sirt taranglik. Ho‘llash. Laplas formulasi. Kapillyar hodisalar"],
 terms=["zichlik \\(\\rho\\)", "gidrostatik bosim \\(\\rho gh\\)", "Arximed kuchi", "uzluksizlik tenglamasi", "dinamik qovushqoqlik \\(\\eta\\)", "sirt taranglik koeffitsiyenti \\(\\sigma\\)", "ho‘llash burchagi \\(\\theta\\)"],
 theory=[
  ("Bosim. Paskal va Arximed qonunlari", r"""<p>Bosim \(p=F/S\) (Pa). Tinch suyuqlikda \(h\) chuqurlikdagi bosim \(p=p_0+\rho gh\) (gidrostatik bosim). <b>Paskal qonuni:</b> suyuqlik yoki gazga berilgan tashqi bosim barcha yo‘nalishlarda o‘zgarishsiz uzatiladi — gidravlik press (\(F_2/F_1=S_2/S_1\)) shunga asoslangan. Atmosfera bosimi barometr bilan (Torrichelli: 760 mm simob ustuni = 101 325 Pa), ortiqcha (manometrik) bosim manometr bilan o‘lchanadi.</p>
<p><b>Arximed qonuni:</b> suyuqlikka botirilgan jismga yuqoriga yo‘nalgan ko‘taruvchi kuch ta’sir qiladi: \(F_A=\rho_\text{s}gV_\text{b}\). Jism \(\rho_\text{j}>\rho_\text{s}\) da cho‘kadi, \(\rho_\text{j}<\rho_\text{s}\) da suzadi. Gidrostatik tortish usulida jism zichligi \(\rho_\text{j}=\rho_\text{s}P_1/(P_1-P_2)\) (L4).</p>"""),
  ("Bernulli tenglamasi", r"""<p>Ideal (qovushqoqmas, siqilmas) suyuqlikning statsionar oqimi uchun uzluksizlik tenglamasi \(S_1v_1=S_2v_2\) va Bernulli tenglamasi o‘rinli:</p>
$$p+\frac{\rho v^2}{2}+\rho gh=\text{const}$$
<p>Oqim tezligi katta joyda statik bosim kichik. Bundan Torrichelli formulasi \(v=\sqrt{2gh}\), Venturi va Pito naychalari, purkagich hamda samolyot qanotining ko‘tarish kuchi tushuntiriladi.</p>"""),
  ("Qovushqoqlik va laminar oqim", r"""<p>Real suyuqlikda qatlamlar orasida ichki ishqalanish kuchi ta’sir qiladi: \(F=\eta S\,\dfrac{dv}{dz}\), \(\eta\) — dinamik qovushqoqlik (Pa·s; suv 20 °C da \(1{,}0\cdot10^{-3}\), glitserin \(\approx1{,}4\)). Kichik tezliklarda oqim <b>laminar</b> (qatlamli), Reynolds soni \(Re=\rho vd/\eta\gtrsim2300\) bo‘lganda <b>turbulent</b>. Quvurdagi laminar oqim sarfi — Puazeyl formulasi \(Q_V=\dfrac{\pi R^4\Delta p}{8\eta l}\). Sharchaga ta’sir etuvchi Stoks kuchi \(F=6\pi\eta rv\) qovushqoqlikni Stoks usulida o‘lchashning asosi.</p>"""),
  ("Sirt taranglik va kapillyar hodisalar", r"""<p>Suyuqlik sirtidagi molekulalar ichkariga tortiladi, shuning uchun sirt qo‘shimcha energiyaga ega: \(\sigma=F/l=E_\text{sirt}/S\) (N/m; suv 20 °C da 0,073). Egri sirt ostida qo‘shimcha (Laplas) bosim paydo bo‘ladi: \(\Delta p=\sigma\left(\frac1{R_1}+\frac1{R_2}\right)\), sfera uchun \(2\sigma/R\). Suyuqlik qattiq jismni ho‘llasa (\(\theta<90^\circ\)), kapillyarda ko‘tariladi, ho‘llamasa — pasayadi:</p>
$$h=\frac{2\sigma\cos\theta}{\rho gr}$$
<p>Tomchilar usuli (L17): tomizgichdan uzilayotgan tomchi og‘irligi sirt taranglik kuchiga teng, \(mg\approx\pi d\sigma\); suyuqliklarni taqqoslashda \(\sigma_x=\sigma_0\,m_x/m_0\).</p>""")],
 chem=["Sirt-faol moddalar (sovun, detergentlar) sirt tarangligini keskin kamaytiradi — yuvish, emulsiya va ko‘piklarning asosi.",
       "Qog‘oz va yupqa qatlam xromatografiyasida erituvchi kapillyar kuchlar ta’sirida ko‘tariladi.",
       "Viskozimetriya — polimerlarning molyar massasini aniqlash usullaridan biri (Mark–Kun–Xauvink tenglamasi)."],
 example=[("Gidrostatik tortish", r"Jism havoda 2,70 N, suvda 1,70 N og‘irlikka ega. Jism zichligi va hajmini toping (g = 9,8 m/s²).",
           r"\(F_A=1{,}00\) N \(=\rho_\text{s}gV\Rightarrow V=1{,}02\cdot10^{-4}\) m³ \(=102\) sm³. \(\rho=\rho_\text{s}\frac{P_1}{P_1-P_2}=1000\cdot2{,}70=2700\) kg/m³ — alyuminiy."),
          ("Kapillyar ko‘tarilish", r"Ichki diametri 0,8 mm bo‘lgan shisha naychada suv qancha balandlikka ko‘tariladi (σ = 0,073 N/m, to‘liq ho‘llash)?",
           r"\(r=0{,}4\) mm. \(h=\frac{2\cdot0{,}073}{1000\cdot9{,}8\cdot4\cdot10^{-4}}=0{,}037\) m \(=37\) mm.")],
 simtask=["2-misoldagi radius (0,4 mm) ni o‘rnating va h ni hisob bilan solishtiring.", "Suv, spirt va glitserin uchun bir xil r da h ni taqqoslang; σ va ρ ning ta’sirini ajrating.", "Simobni tanlang: nima uchun h manfiy? Menisk shaklini ho‘llash burchagi bilan bog‘lang."],
 mistakes=[("“Arximed kuchi jism og‘irligiga bog‘liq.”", "U siqib chiqarilgan suyuqlik og‘irligiga teng: \\(F_A=\\rho_s gV_b\\); jism materiali ahamiyatsiz."),
           ("“Oqim tezligi katta joyda bosim ham katta.”", "Bernulli tenglamasiga ko‘ra tezlik ortganda statik bosim kamayadi."),
           ("“Sirt taranglik faqat suvga xos.”", "Barcha suyuqliklar sirt tarangligiga ega; simobniki suvnikidan qariyb 6,5 marta katta.")],
 ai=AI.format(t="gidrostatika, gidrodinamika va sirt hodisalari", b="1) Bernulli tenglamasini energiya saqlanish qonunidan keltirib chiqarishga yordam ber.\n2) Python’da turli suyuqliklar (suv, spirt, glitserin) uchun h(r) kapillyar ko‘tarilish grafigini chiz va 0,1–2 mm oraliqda jadval tuz."),
 quiz=[("Suvda 10 m chuqurlikdagi gidrostatik bosim (ρ = 1000 kg/m³, g = 10 m/s²):", ["100 kPa", "10 kPa", "1 MPa", "1 kPa"], 0, "ρgh."),
       ("Gidravlik pressda kichik porshen yuzasi 10 sm², kattasi 500 sm². Kuchdan yutuq:", ["50 marta", "5 marta", "500 marta", "10 marta"], 0, "S₂/S₁."),
       ("Hajmi 0,002 m³ jism suvga to‘liq botirilgan. Arximed kuchi (g = 10 m/s²):", ["20 N", "2 N", "200 N", "0,2 N"], 0, "ρgV."),
       ("Quvur kesimi 2 marta kamaysa, ideal suyuqlik oqim tezligi:", ["2 marta ortadi", "2 marta kamayadi", "4 marta ortadi", "o‘zgarmaydi"], 0, "Sv = const."),
       ("Bernulli tenglamasi qaysi saqlanish qonunining natijasi?", ["energiya", "impuls", "zaryad", "impuls momenti"], 0, "Bosim ishi va energiya balansi."),
       ("Sirt taranglik koeffitsiyentining birligi:", ["N/m", "N/m²", "Pa", "J"], 0, "σ = F/l."),
       ("Kapillyar radiusi 2 marta kamaysa, ko‘tarilish balandligi:", ["2 marta ortadi", "2 marta kamayadi", "4 marta ortadi", "o‘zgarmaydi"], 0, "h ∝ 1/r."),
       ("Simob shisha naychada pasayadi, chunki:", ["shishani ho‘llamaydi", "zichligi katta", "sirt tarangligi kichik", "qovushqoqligi katta"], 0, "θ > 90°."),
       ("Stoks kuchi:", [r"\(6\pi\eta rv\)", r"\(\eta v/r\)", r"\(\rho gV\)", r"\(\sigma l\)"], 0, "Qovushqoq muhitda sekin harakatlanuvchi shar uchun."),
       ("Normal atmosfera bosimi taxminan:", ["101 kPa", "10 kPa", "1 MPa", "760 Pa"], 0, "760 mm simob ustuni.")],
 blits=["Nima uchun temir kema suzadi?", "Samolyot qanoti ko‘tarish kuchini qanday hosil qiladi?", "Daraxtlarda suv ildizdan barglarga qanday ko‘tariladi?", "Nima uchun sovunli suvdan katta pufak hosil qilish mumkin?", "Asal nima uchun sekin oqadi va qizdirilsa tezlashadi?"]
))
