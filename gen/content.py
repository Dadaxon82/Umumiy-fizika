# -*- coding: utf-8 -*-
"""Fan dasturi (UMF11210, 2026/2027) asosidagi mazmun. Manba: QDU "Umumiy fizika" fan dasturi (rus tilida), o'zbekchaga o'girilgan.
Matnlar joriy lotin imlosida yoziladi; yangi alifbo (Ö, Ğ, Ş, Ç) sahifada avtomatik qo'llanadi."""

FAN = {
    "nomi": "Umumiy fizika",
    "kod": "UMF11210",
    "yil": "2026/2027",
    "semestr": "1–2",
    "ects": "10",
    "turi": "Majburiy",
    "til": "Rus",
    "tartib": "60530100 – 1.11",
    "hafta_soat": "8",
    "jami": "300",
    "maruza": "54",
    "lab": "66",
    "mustaqil": "180",
    "auditoriya": "120",
    "yonalish": "60530100 – Kimyo (kunduzgi ta’lim)",
    "bilim_sohasi": "500 000 – Tabiiy fanlar, matematika va statistika",
    "talim_sohasi": "530 000 – Fizika va tabiiy fanlar",
    "fakultet": "Tabiiy fanlar va iqtisodiyot fakulteti",
    "kafedra": "Fizika va astronomiya kafedrasi",
}

MAQSAD = ("Talabalarni makro va mikrodunyodagi harakat va uning turlari, modda tuzilishi va xossalari, turli agregat "
          "holatlardagi makroskopik tizimlarning (alohida jismlar va maydonlar uchun) fizik xossalari, Koinot obyektlari va "
          "hodisalari haqidagi zarur ilmiy tasavvurlar, bilim va tushunchalar bilan qurollantirish hamda ularda fenomenologik "
          "bilim, ko‘nikma va malakalarni shakllantirish.")
VAZIFA = ("Talabalarda umumiy fizika kursi bo‘limlari bo‘yicha amaliy mashg‘ulotlarda o‘zlashtirilgan barcha mavzular bo‘yicha "
          "masala yechish ko‘nikma va malakalarini, laboratoriya ishlarini tushunish va ular bo‘yicha xulosa chiqara olishni, "
          "shuningdek fizik qonuniyatlar va munosabatlarni to‘g‘ri aniqlashni shakllantirish.")

PREREKV = [("Umumiy fizika", "UMF11210"), ("Umumiy psixologiya", "UMP1106"), ("Oliy matematika", "OMT11208")]

# Ta'lim natijalari (TN / PO)
TN = [
    ("TN1", "k", "Kelajakdagi mutaxassislik doirasida yuzaga keladigan masalalarda hodisalarning fizik mohiyatini ajrata olish."),
    ("TN2", "k", "Zamonaviy fizik eksperimental asboblar (mikroskop, spektrograf va boshqalar) bilan yaxshi tanish bo‘lish, turli fizik tajribalarni o‘tkazish bo‘yicha yetarli ko‘nikmalarga ega bo‘lish."),
    ("TN3", "k", "Fizik qonunlarning qo‘llanilish chegaralarini aniqlay olish va bunda fizikaning turli bo‘limlariga nazariy yondashuvlarning umumiyligini hisobga olish."),
    ("TN4", "k", "Elektr va magnit maydonlardagi hodisalar, elektromagnit induksiya xossalari, mexanik va elektromagnit tebranishlar hamda to‘lqinlar haqida bilimga ega bo‘lish."),
    ("TN5", "k", "Atomlar tuzilishi va mikrodunyo fizikasi, atom yadrosi va elementar zarralar fizikasi haqida bilimga ega bo‘lish."),
    ("TN6", "n", "Fizik qonuniyatlar bo‘yicha nazariy bilimlarni qo‘llab, tabiat qonunlariga oid asosiy masalalarni to‘g‘ri yecha oladi."),
    ("TN7", "n", "Jismlarning mexanik harakati, dinamika qonunlari, saqlanish qonunlari, molekulyar-kinetik nazariya va termodinamika asoslari haqida bilimga ega."),
    ("TN8", "n", "O‘zgarmas va o‘zgaruvchan tok qonunlarini o‘rganadi, ularni taqqoslaydi va o‘lchov asboblari bilan mustaqil ishlay oladi."),
    ("TN9", "n", "Geometrik, to‘lqin va kvant optikasi bilan yaqindan tanishadi va ularning aniq masalalarini farqlay oladi."),
    ("TN10", "n", "Atom tuzilishi va mikrodunyo haqida tasavvurga ega."),
]
# TN – nazorat matritsasi (JN, ON, YaN)
TN_MATRIX = {"TN1": "+++", "TN2": "+++", "TN3": "+++", "TN4": "+++", "TN5": "+++", "TN6": "+++",
             "TN7": "+--", "TN8": "+--", "TN9": "++-", "TN10": "+--"}

# Fan dasturidagi ma'ruzalar (54 soat): (sarlavha, mazmun, adabiyot)
MARUZA = [
    ("Moddiy nuqta kinematikasi", "Mexanik harakat. Fazo va vaqt. Sanoq sistemasi. Harakatning nisbiyligi. Moddiy nuqta, trayektoriya, yo‘l va ko‘chish. To‘g‘ri chiziqli harakatda tezlik va tezlanish. Fizik kattaliklar. O‘lchov birliklari.", "1, 2, 3"),
    ("Egri chiziqli harakat", "Egri chiziqli harakatda tezlik va tezlanish. Tangensial va normal tezlanish. Qattiq jismning aylanma harakati, burilish burchagi, burchak tezlik va burchak tezlanish.", "1, 2, 3"),
    ("Moddiy nuqta dinamikasi", "Nyutonning birinchi qonuni. Inersial sanoq sistemasi. Massa va kuch tushunchalari. Jism impulsi. Nyutonning ikkinchi qonuni. Ilgarilanma harakat dinamikasining asosiy tenglamasi. Nyutonning uchinchi qonuni. Galileyning nisbiylik prinsipi.", "1, 2, 3"),
    ("Tabiatdagi kuchlar va ularning xossalari", "Elastiklik kuchi. Guk qonuni. Yung moduli. Ishqalanish kuchlari va ularning turlari. Butun olam tortishish qonuni. Gravitatsiya kuchi. Og‘irlik kuchi va vazn.", "1, 2, 3"),
    ("Mexanikada saqlanish qonunlari", "Impulsning saqlanish qonuni. Ilgarilanma harakatda ish, energiya va quvvat. Kinetik energiya. Potensial energiya. Mexanik energiya va uning saqlanish qonuni. Energiyaning grafik tasviri. Markaziy absolyut elastik va noelastik to‘qnashuvlar.", "1, 2, 3"),
    ("Qattiq jism aylanma harakati dinamikasi", "Moddiy nuqta va jismning inersiya momenti. Shteyner teoremasi. Aylanma harakatda ish va kinetik energiya. Kuch momenti. Aylanma harakat dinamikasining asosiy tenglamasi. Impuls momenti va uning saqlanish qonuni.", "1, 2, 3"),
    ("Mexanik tebranishlar va to‘lqinlar", "Garmonik tebranishlar. Garmonik tebranishlarning amplitudasi, siklik chastotasi va fazasi. Prujinali, matematik va fizik mayatniklar. Mexanik to‘lqin jarayonlari. Ko‘ndalang va bo‘ylama to‘lqinlar. To‘lqinlarning muhitda tarqalishi. Tovush to‘lqinlari.", "1, 2, 3, 4"),
    ("Molekulyar-kinetik nazariya asoslari", "Modda miqdori, molyar massa, Avogadro doimiysi va temperatura tushunchasi. Molekulalar ilgarilanma harakatining o‘rtacha kvadratik tezligi. Molekulalar issiqlik harakatining o‘rtacha kinetik energiyasi. Molekulyar-kinetik nazariyaning asosiy tenglamasi.", "2, 3, 4, 5"),
    ("Ideal gaz qonunlari", "Ideal gaz. Mendeleyev–Klapeyron tenglamasi. Ideal gaz holat tenglamasi. Izojarayonlar. Dalton qonuni. Absolyut va nisbiy namlik. Nisbiy namlikni o‘lchash usullari.", "2, 3, 4, 5"),
    ("Termodinamika asoslari", "Ichki energiya. Issiqlik miqdori. Gazning kengayishida bajarilgan ish. Termodinamikaning birinchi qonuni. Gazning issiqlik sig‘imi va uning jarayon turiga bog‘liqligi. Termodinamikaning birinchi qonunini izojarayonlarga qo‘llash. Adiabatik jarayon. Puasson tenglamasi.", "2, 3, 4, 5"),
    ("Suyuqlik va gazlarning umumiy xossalari", "Modda fazalari. Zichlik. Suyuqlik va gazlardagi bosim. Atmosfera bosimi va manometrik bosim. Paskal qonuni. Bosimni o‘lchash va barometr. Ko‘taruvchi kuch va Arximed qonuni. Bernulli tenglamasi. Qovushqoqlik. Laminar oqim. Sirt taranglik. Ho‘llash hodisasi. Laplas formulasi. Kapillyar hodisalar.", "1, 2, 3, 4"),
    ("Elektrostatik maydon va uning xossalari", "Elektrostatika. Elektr zaryadi. Zaryadning diskretligi. Elektr zaryadining saqlanish qonuni. Kulon qonuni. Elektrostatik maydon kuchlanganligi. Elektrostatik maydon potensiali. Kondensatorlar va ularni ulash. Elektrostatik maydon energiyasi.", "1, 2, 3, 4"),
    ("O‘zgarmas elektr toki qonunlari", "O‘zgarmas elektr toki. Tok kuchi. Kuchlanish. Elektr qarshilik. O‘tkazgichlarni ketma-ket va parallel ulash. Zanjir qismi uchun Om qonuni. Tokning ishi va quvvati. Joul–Lens qonuni.", "1–5"),
    ("Turli muhitlarda elektr toki", "Termoelektron emissiya hodisasi. Vakuumda elektr toki. Elektronlarning metalldan chiqish ishi. Gazlarda elektr toki. Ionlanish va rekombinatsiya jarayonlari. Gaz razryadining to‘liq volt-amper xarakteristikasi. Mustaqil va nomustaqil gaz razryadlari, ularning turlari va qo‘llanilishi. Plazma haqida tushuncha.", "1–5"),
    ("Magnit maydon", "Magnit maydon induksiyasi vektori. To‘g‘ri va aylanma tokning magnit maydonini hisoblash. Amper kuchi. Parallel toklarning o‘zaro ta’siri. Magnit maydonning harakatlanayotgan zaryadga ta’siri. Lorens kuchi. Zaryadli zarralarning bir jinsli magnit maydondagi harakati.", "1–5"),
    ("Elektromagnit induksiya hodisasi", "Magnit oqimi. Faradey tajribalari. Faradeyning elektromagnit induksiya qonuni. Lens qoidasi. Induktivlik. O‘zinduksiya hodisasi. O‘zaro induksiya. Magnit maydon energiyasi.", "1–5"),
    ("Elektromagnit tebranishlar va to‘lqinlar", "Tebranish konturidagi fizik jarayonlar. Tomson formulasi. Erkin elektromagnit tebranishlar. Elektromagnit to‘lqinlar va ularning tarqalish tezligi. Elektromagnit to‘lqinlarning qo‘llanilishi.", "1–5"),
    ("O‘zgaruvchan tok qonunlari", "O‘zgaruvchan tokning amplituda va ta’sir etuvchi qiymatlari. O‘zgaruvchan tok zanjiridagi aktiv, induktiv va sig‘im qarshiliklar. O‘zgaruvchan tok quvvati. Quvvat koeffitsiyenti. Tok generatorlari.", "1–5"),
    ("Yorug‘likning elektromagnit to‘lqin tabiati. Yorug‘lik interferensiyasi", "Yorug‘likning korpuskulyar-to‘lqin dualizmi. Yorug‘lik interferensiyasi va uni kuzatish usullari. Yupqa pardalardagi interferensiya. Nyuton halqalari.", "1–5"),
    ("Yorug‘lik difraksiyasi", "Difraksiya hodisasi. Gyuygens–Frenel prinsipi. Disk va doiraviy teshikdagi Frenel difraksiyasi. Difraksion panjaradagi Fraungofer difraksiyasi. Difraksion panjara va uning ajrata olish qobiliyati.", "1–5"),
    ("Moddalarda elektromagnit to‘lqinlar. Yorug‘likning qutblanishi", "Yorug‘lik to‘lqinlarining muhit bilan o‘zaro ta’siri. Yorug‘lik dispersiyasi. Spektral tahlil haqida tushuncha. Tabiiy va qutblangan yorug‘lik. Malyus qonuni. Ikki muhit chegarasida qaytish va sinishda yorug‘likning qutblanishi. Bryuster qonuni.", "1–5"),
    ("Geometrik optika", "Yorug‘likning to‘g‘ri chiziq bo‘ylab tarqalish qonuni. Yorug‘likning qaytish va sinish qonunlari. To‘la ichki qaytish. Linzalar. Yupqa linza formulasi. Linzada tasvir yasash.", "1–5"),
    ("Nurlanishning kvant tabiati. Kvant optikasi elementlari", "Issiqlik nurlanishi. Absolyut qora jism nurlanish qonunlari. Kirxgof qonuni. Stefan–Bolsman qonuni. Vinning siljish qonuni. Plank gipotezasi va formulasi. Foton energiyasi va impulsi. Tashqi fotoeffekt qonunlari. Eynshteyn tenglamasi. Yorug‘lik bosimi. Kompton effekti.", "1–5"),
    ("Fotometriya asoslari", "Yorug‘lik oqimi. Yorug‘lik kuchi. Yoritilganlik. Yoritilganlik qonuni. Ravshanlik.", "1–5"),
    ("Atom tuzilishi", "Tomson modeli. Rezerford tajribasi. Atomning yadro modeli. Vodorod atomining nurlanish spektri. Bor postulatlari. Vodorod atomi uchun Bor nazariyasi.", "1–5"),
    ("Radioaktivlik", "Radioaktiv yemirilish qonuni. Siljish qoidasi. Alfa-yemirilish. Beta-yemirilish. Gamma-nurlanish va uning xossalari.", "1–5"),
    ("Atom yadrosining tuzilishi va xossalari", "Yadro kuchlari. Massa defekti va yadroning bog‘lanish energiyasi. Yadroning fenomenologik tomchi va qobiq modellari. Yadro reaksiyalari. Yadrolarning bo‘linish reaksiyalari. Zanjir reaksiya. Yadro reaktorlari. Yadro energetikasi muammolari. Termoyadro reaksiyalari.", "1–5"),
]

# Fan dasturidagi laboratoriya mashg'ulotlari (66 soat)
LAB = [
    "Shtangensirkul yordamida jismlarning chiziqli o‘lchamlarini aniqlash",
    "To‘g‘ri geometrik shakldagi jismlarning zichligini aniqlash",
    "Piknometr yordamida suyuqlik zichligini aniqlash",
    "Suyuqlikda cho‘kadigan jismlarning zichligini gidrostatik tortish usulida aniqlash",
    "Qattiq jismlarning sirpanish ishqalanish koeffitsiyentini aniqlash",
    "Qattiq jismlarning elastiklik modulini egilish usulida aniqlash",
    "Qattiq jismlarning elastiklik modulini egilish usulida aniqlash",
    "Matematik mayatnik yordamida erkin tushish tezlanishini aniqlash",
    "Fizik mayatnik yordamida erkin tushish tezlanishini aniqlash",
    "Suyuqliklarning hajmiy kengayish koeffitsiyentini aniqlash",
    "Havo namligini aniqlash",
    "Suv aralashmasining temperaturasini aniqlash",
    "Qattiq jismlarning solishtirma issiqlik sig‘imini aniqlash",
    "Qattiq jismlarning solishtirma issiqlik sig‘imini aniqlash",
    "Gazlar solishtirma issiqlik sig‘imlarining nisbatini aniqlash",
    "Gazlar solishtirma issiqlik sig‘imlarining nisbatini aniqlash",
    "Tomchilar usulida sirt taranglik koeffitsiyentini aniqlash",
    "Qattiq jismlarning issiqlikdan kengayish koeffitsiyentini aniqlash",
    "Kondensatorlarning elektr sig‘imini aniqlash",
    "Zanjir qismi uchun Om qonuni yordamida o‘tkazgich qarshiligini aniqlash",
    "Uitston ko‘prigi yordamida qarshiliklarni aniqlash",
    "Kirxgof qoidalarini o‘rganish",
    "Vakuum diodning volt-amper xarakteristikasini o‘rganish",
    "Yer magnit maydoni kuchlanganligining gorizontal tashkil etuvchisini aniqlash",
    "Faradeyning elektromagnit induksiya qonunini o‘rganish",
    "Ignalar yordamida shishaning sindirish ko‘rsatkichini aniqlash",
    "Mikroskopning ishlash prinsipini o‘rganish va uning kattalashtirishini aniqlash",
    "Mikroskop yordamida shishaning sindirish ko‘rsatkichini aniqlash",
    "Qavariq va botiq linzalarning bosh fokus masofasini aniqlash",
    "Difraksion panjara yordamida yorug‘lik to‘lqin uzunligini aniqlash",
    "Tashqi fotoeffekt hodisasini o‘rganish",
    "Tashqi fotoeffekt hodisasini o‘rganish",
    "Atomlar spektrlari bo‘yicha kompyuter tajribasi. Frank–Gers tajribasini o‘rganish",
]

# Mustaqil ta'lim (180 soat): har biri 4 soat, "mavzu bo'yicha taqdimot tayyorlash"
MUSTAQIL = [
    "Vektor kattaliklarni qo‘shish", "Butun olam tortishish qonuni", "Elastiklik kuchlari ta’sirida harakat",
    "O‘zgarmas kuchlar ta’sirida harakat", "Gorizontal otilgan jismlar harakati", "Qiya tekislikda jismlar harakati",
    "Ichki energiyani topishga doir masalalar yechish", "Issiqlik miqdorini topish",
    "Solishtirma issiqlik sig‘imini topishga doir masalalar yechish", "O‘zgaruvchan tok qonunlari",
    "Elektromagnit tebranishlar, to‘lqinlar", "Toklarning magnit maydoni",
    "Yorug‘lik dispersiyasi. Yorug‘likning yutilishi va sochilishi", "Yorug‘lik bosimi. Lebedev tajribalari",
    "Issiqlik nurlanishi",
    "O‘zgaruvchan tok qonunlari. O‘zgaruvchan tokning amplituda va ta’sir etuvchi qiymatlari. O‘zgaruvchan tok zanjirida quvvat",
    "O‘zgaruvchan tok zanjiridagi aktiv, induktiv va sig‘im qarshiliklar. O‘zgaruvchan tokning to‘la qarshiligi",
    "Kondensator va induktivlikdagi toklar. Vektor diagrammalar. Rezonans va uning turlari",
    "Linzalarning kamchiliklari. Aberratsiyalar (ko‘ndalang va bo‘ylama, sferik aberratsiyalar)",
    "Chiziqli va nochiziqli optika", "Fotometrlar va ularning qo‘llanilishi", "Yorug‘lik tezligini o‘lchash usullari",
    "Yupqa yassi-parallel plastinkada nurlar yo‘li", "Sinish qonunini Nyuton va Gyuygens nazariyalari bo‘yicha hisoblash",
    "Lupada nurlar yo‘li va uning qo‘llanilishi", "Mikroskopda nurlar yo‘li va uning qo‘llanilishi",
    "Ko‘zgu formulasi (fokus, fokal tekislik)", "Yassi, botiq va qavariq ko‘zgularda tasvir yasash",
    "Sferik sirtda yorug‘likning sinishi. Linza formulasini keltirib chiqarish (bosh optik o‘q, fokal tekislik, fokus, optik kuch)",
    "Qavariq va botiq linzalarda tasvir yasash. Yig‘uvchi va sochuvchi linzalarning xarakteristikalari",
    "Optik tizimlar aberratsiyalari va ularning turlari", "Ko‘z. Ko‘z optik asbob sifatida. Ko‘rish burchagi",
    "Yorug‘lik interferensiyasi va uni kuzatish usullari", "Difraksiya hodisasining fan va texnikada qo‘llanilishi",
    "Qutblangan yorug‘lik olish", "Tomsonning atom modeli", "Alfa-zarralarning sochilishi. Rezerford formulasi",
    "Bor postulatlari. Frank–Gers tajribalari", "Vodorod atomi uchun Bor nazariyasi", "Faza va guruh tezliklari",
    "Kvant sonlar. Shtern–Gerlax tajribasi", "Pauli prinsipi. Zeeman effekti", "Yadro massasi va uni o‘lchash usullari",
    "Sun’iy radioaktivlik. Yadroning gamma-nurlanishi", "Elementar zarralar. Kvarklar. Glyuonlar",
]

TEXNOLOGIYA = ["Ma’ruzalar", "Amaliy va laboratoriya ishlarini bajarish va tahlil qilish", "Interaktiv keys-stadilar",
               "Blits-so‘rov", "Guruhlarda ishlash", "Taqdimotlar o‘tkazish", "Jamoaviy ish va himoya uchun loyihalar"]

KREDIT = ["o‘quv mashg‘ulotlarida faol ishtirok etishi;", "mustaqil ta’lim topshiriqlarini o‘z vaqtida bajarishi;",
          "joriy va oraliq nazoratlardan muvaffaqiyatli o‘tishi;", "akademik halollik tamoyillariga rioya qilishi;",
          "yakuniy nazoratda ijobiy natija olishi shart."]

TUZUVCHI = [("Meliqo‘ziyev Dadaqo‘zi Jo‘raqo‘ziyevich", "QDU Fizika va astronomiya kafedrasi o‘qituvchisi, PhD"),
            ("Mirsultonov Ilhomjon Mirzaxakimovich", "QDU Fizika va astronomiya kafedrasi o‘qituvchisi, PhD")]
TAQRIZCHI = [("N.X. Yo‘ldoshev", "f.-m.f.d., professor, Farg‘ona davlat texnika universiteti “Fizika” kafedrasi"),
             ("F.O. Dadaboyeva", "p.f.f.d. (PhD), dotsent, QDU “Fizika va astronomiya” kafedrasi")]

ADABIYOT_ASOSIY = [
    "Gaibov A. Fizika. — 2022.",
    "Abduraxmonov Q. va boshq. Fizika. — 2018.",
    "Eshboltayev I. va boshq. Umumiy fizikadan laboratoriya mashg‘ulotlari. — 2023.",
    "Трофимова Т.И. Курс физики. — 1985.",
    "Tursunov I. Fizika. — 2020.",
]
ADABIYOT_QOSHIMCHA = [
    "Sultanov N. Fizika kursi. Darslik. — Classik, 2021. — 412 b.",
    "Nurmatov N.A., Raxmonov G‘.T., Alimov R., Sultonov O.Z., Xamidjonov I.X. “Elektr va magnetizm fanidan praktikum”. Uslubiy qo‘llanma. — Toshkent: Innovatsiya-Ziyo, 2021. — 176 b.",
    "Ульмасова М. и др. Практикум по физике. Механика и молекулярная физика. — Ташкент: Укитувчи, 1996.",
    "Giancoli D.C. Physics: Principles with Applications. 6th ed. — Prentice Hall, 2004.",
    "Serway R.A., Jewett J.W. Physics for Scientists and Engineers with Modern Physics. 9th ed. — Cengage Learning, 2013.",
]
RESURS = [("www.tdpu.uz", "https://www.tdpu.uz"), ("www.edu.uz", "https://www.edu.uz"), ("www.pedagog.uz", "https://www.pedagog.uz"),
          ("www.ziyonet.uz", "https://www.ziyonet.uz"), ("MIT OpenCourseWare", "https://ocw.mit.edu/courses/5-61-physical-chemistry-fall-2017/")]

# ---------------- Baholash ----------------
NAZORAT = [
    ("Joriy nazorat (JN)", 30, 18, "1-MT: mustaqil ta’lim taqdimoti (prezentatsiya) va uning himoyasi; DF: laboratoriya mashg‘ulotlaridagi faolligi; 2-MT: keys-stadi (case-study) tahlili va yechimi."),
    ("Oraliq nazorat (ON)", 20, 12, "Oraliq nazorat testi (HEMIS tizimida, 12-hafta, 20 ta savol)."),
    ("Yakuniy nazorat (YaN)", 50, 30, "1-kurslar uchun: yakuniy nazorat yozma ishi (3 ta nazariy savol + 1 ta keys). Yuqori kurslar uchun: Universitet Kengashi belgilagan shakl; topshiriqlar fanning ta’lim natijalarini baholashi shart."),
]
JN_RUBRIKA = [
    ("Mustaqil ta’lim taqdimoti va uning himoyasi (1-topshiriq)", 5,
     "Qo‘shimcha ilmiy-uslubiy adabiyotlardan foydalanib batafsil taqdimot tayyorlagan; fizik jarayonlar, formulalar va chizmalarni mantiqiy izchil bayon qiladi, himoyada fikrini mustaqil va erkin ifodalaydi.",
     "Mavzu asosan yoritilgan, taqdimot tushunarli, lekin faqat asosiy darsliklar bilan cheklangan; himoyada tayyor matnga tayanadi, ayrim atama yoki formulalarni tushuntirishda kichik noaniqliklarga yo‘l qo‘yadi.",
     "Taqdimot yuzaki tayyorlangan, materiallar to‘liq tahlil qilinmagan, ko‘chirmachilikka yo‘l qo‘yilgan; slaydlarda zarur vizual ma’lumot (chizma, diagramma) yo‘q, mavzuni tushuntira olmaydi.",
     "Taqdimot umuman tayyorlanmagan, mavzuni bilmaydi yoki belgilangan muddatda HEMIS tizimiga yuklanmagan."),
    ("Fizik qonunlar tahlili va masala yechish modelini qurish (qonunlarni amalda qo‘llash, sxemalar chizish)", 20,
     "Qonunlarning fizik mohiyatini to‘liq tushunadi, kerakli qonuniyatlarni aniq tanlaydi, chizma va zanjir sxemalarini xatosiz chizadi, yechimning mustaqil algoritmini tuzadi.",
     "Asosiy qonuniyatlarni yozadi, lekin murakkabroq sxemalar yoki yechim ketma-ketligini tuzishda o‘qituvchi yordamiga tayanadi.",
     "Faqat bitta formulaga to‘g‘ridan-to‘g‘ri qo‘yiladigan eng oddiy masalalar shartini yoza oladi; chizma va sxemalarni mustaqil tuza olmaydi, qonuniyatni tanlashda xatoga yo‘l qo‘yadi.",
     "Masala shartini umuman tushunmaydi, fizik qonuniyatlarni amaliyot bilan bog‘lay olmaydi, sxema va chizma chiza olmaydi."),
    ("Keys-stadi (case-study) tahlili va yechimi (2-topshiriq: fizik qonunlarni hayotiy/amaliy muammolarga qo‘llash)", 5,
     "Berilgan muammoli fizik vaziyatni chuqur tahlil qilgan, fizik qonuniyatlar asosida to‘liq va ijodiy yechim taklif etgan; barcha xulosalar mantiqan to‘g‘ri va ilmiy asoslangan.",
     "Keysni tahlil qilishga harakat qilgan, asosiy fizik qonunlarni qisman to‘g‘ri qo‘llagan, lekin yechimni asoslashda yoki formulalarni amaliyotga bog‘lashda kamchiliklar bor.",
     "Muammoli vaziyatning fizik mohiyatini to‘liq anglamagan, aniq yechim taklif eta olmagan; tahlil o‘rniga umumiy so‘zlar yozilgan yoki boshqa mavzuga chalg‘igan.",
     "Keys-stadi topshirig‘i bajarilmagan, muammoli vaziyat yechimi taqdim etilmagan yoki muddatida topshirilmagan."),
]
ON_RUBRIKA = [
    ("18–20 ball (90–100%)", "Testning 18–20 savoliga to‘g‘ri javob bergan. Fan mohiyatini to‘liq tushunadi, mustaqil va ijodiy fikrlaydi, olgan bilimini to‘g‘ri ifodalay oladi."),
    ("14–17 ball (70–89,9%)", "14–17 savolga to‘g‘ri javob bergan. Fan mohiyatini tushunadi, lekin ayrim murakkab nazariy savollar yoki hisob-kitoblarda xatoga yo‘l qo‘yadi."),
    ("12–13 ball (60–69,9%)", "12–13 savolga to‘g‘ri javob bergan. Bilimni amalda qo‘llashda qiynaladi, fan haqida umumiy tasavvurga ega, asosan oddiy savollarni yechadi."),
    ("0–11 ball (0–59,9%)", "0–11 savolga to‘g‘ri javob bergan. Fan dasturini o‘zlashtirmagan, mavzular mohiyatini tushunmaydi."),
]
YAN_RUBRIKA = [
    ("Nazariy savollar (1, 2, 3-savollar)", 30,
     ["27–30 ball: barcha savollarga to‘liq, aniq va mantiqan izchil javob berilgan; kalit so‘z va iboralar to‘g‘ri va o‘rinli ishlatilgan; fikrlar ilmiy asoslangan.",
      "21–26 ball: savollarning asosiy mazmuni yoritilgan, kalit iboralar yetarli ishlatilgan; ayrim nazariy tushunchalarni tushuntirishda kichik noaniqliklar bor.",
      "18–20 ball: savollarga qisman yoki yuzaki javob berilgan; kalit so‘zlar to‘liq ochilmagan, fikrlar tarqoq va umumiy tushunchalar bilan cheklangan.",
      "0–17 ball: savollar mohiyati umuman tushunilmagan, javoblar noto‘g‘ri yoki yozilmagan; kalit so‘zlar o‘z o‘rnida ishlatilmagan."],
     "Har bir savol 10 ball: 1-mezon — nazariy bilim mohiyatini ochish (4 ball); 2-mezon — kalit ibora va fizik atamalarni to‘g‘ri ishlatish (3 ball); 3-mezon — fikrni mantiqan izchil bayon qilish va mustaqil xulosa (3 ball)."),
    ("Keys-topshiriq (4-savol: muammoli vaziyat tahlili va masala yechimi)", 20,
     ["18–20 ball: vaziyat chuqur tahlil qilingan va to‘g‘ri baholangan; masala to‘liq yechilgan, fizik kattaliklar xatosiz hisoblangan, natijalar to‘g‘ri talqin qilingan va SI tizimida aniq ifodalangan.",
      "14–17 ball: vaziyat to‘g‘ri baholangan, kerakli formulalar (masalan, Om qonuni, Amper qonuni) to‘g‘ri tanlangan; lekin hisob-kitob yoki yakuniy xulosada kichik xatolar bor.",
      "12–13 ball: keys mohiyati qisman tushunilgan, faqat ayrim formulalar yozilgan; masala oxirigacha yechilmagan yoki hisoblashlar mantiqsiz va noto‘g‘ri.",
      "0–11 ball: keys bo‘yicha vaziyat umuman tushunilmagan, masala yechimi ko‘rsatilmagan, fizik qonunlarni muammoli amaliyotga qo‘llay olmagan."],
     ""),
]
BAHO = [("90–100", "A’lo", "Ta’lim natijalarini yuqori darajada o‘zlashtirgan; bilimlarni mustaqil tahlil qiladi va yangi vaziyatlarda qo‘llaydi."),
        ("70–89,9", "Yaxshi", "Asosiy ta’lim natijalarini barqaror o‘zlashtirgan; bilim va ko‘nikmalarni amaliy vaziyatlarda qo‘llaydi."),
        ("60–69,9", "Qoniqarli", "Talab qilinadigan minimal ta’lim natijalariga erishgan, biroq tahlil, asoslash yoki mustaqil qo‘llashda cheklovlar bor."),
        ("0–59,9", "Qoniqarsiz", "Minimal ta’lim natijalariga yetarli darajada erishmagan.")]

# ---------------- Atamalar lug'ati (o'zbekcha – ruscha – inglizcha) ----------------
GLOSSARIY = [
    ("Mexanik harakat", "Механическое движение", "Mechanical motion", "Jism vaziyatining boshqa jismlarga nisbatan vaqt o‘tishi bilan o‘zgarishi.", 1),
    ("Sanoq sistemasi", "Система отсчёта", "Frame of reference", "Sanoq jismi, unga bog‘langan koordinatalar sistemasi va vaqtni o‘lchash asbobi (soat) majmui.", 1),
    ("Moddiy nuqta", "Материальная точка", "Point particle", "Berilgan masala sharoitida o‘lchamlarini hisobga olmasa ham bo‘ladigan, massaga ega jism.", 1),
    ("Trayektoriya", "Траектория", "Trajectory", "Moddiy nuqtaning harakat davomida fazoda chizgan chizig‘i.", 1),
    ("Ko‘chish", "Перемещение", "Displacement", "Jismning boshlang‘ich vaziyatidan oxirgi vaziyatiga yo‘nalgan vektor.", 1),
    ("Tezlanish", "Ускорение", "Acceleration", "Tezlikning vaqt bo‘yicha o‘zgarish jadalligini ifodalovchi vektor kattalik: $a = dv/dt$.", 1),
    ("Normal tezlanish", "Нормальное ускорение", "Normal (centripetal) acceleration", "Egri chiziqli harakatda tezlik yo‘nalishining o‘zgarishini ifodalaydi: $a_n = v^2/R$.", 2),
    ("Burchak tezlik", "Угловая скорость", "Angular velocity", "Burilish burchagining vaqt bo‘yicha hosilasi: $\\omega = d\\varphi/dt$.", 2),
    ("Inersial sanoq sistemasi", "Инерциальная система отсчёта", "Inertial frame", "Nyutonning birinchi qonuni bajariladigan sanoq sistemasi.", 3),
    ("Impuls", "Импульс", "Momentum", "Jism massasining uning tezligiga ko‘paytmasi: $p = mv$.", 3),
    ("Kuch", "Сила", "Force", "Jismlarning o‘zaro ta’siri o‘lchovi; jismga tezlanish beradi yoki uni deformatsiyalaydi.", 3),
    ("Guk qonuni", "Закон Гука", "Hooke’s law", "Kichik deformatsiyalarda elastiklik kuchi deformatsiyaga proporsional: $F = -kx$.", 4),
    ("Yung moduli", "Модуль Юнга", "Young’s modulus", "Mexanik kuchlanishning nisbiy uzayishga nisbati; materialning cho‘zilishga qarshiligi.", 4),
    ("Ishqalanish koeffitsiyenti", "Коэффициент трения", "Coefficient of friction", "Ishqalanish kuchining normal bosim kuchiga nisbati.", 4),
    ("Kinetik energiya", "Кинетическая энергия", "Kinetic energy", "Harakatlanayotgan jismning energiyasi: $E_k = mv^2/2$.", 5),
    ("Potensial energiya", "Потенциальная энергия", "Potential energy", "Jismlarning o‘zaro joylashuviga bog‘liq energiya.", 5),
    ("Quvvat", "Мощность", "Power", "Vaqt birligida bajarilgan ish: $N = dA/dt$.", 5),
    ("Inersiya momenti", "Момент инерции", "Moment of inertia", "Aylanma harakatdagi inertlik o‘lchovi: $I = \\sum m_i r_i^2$.", 6),
    ("Kuch momenti", "Момент силы", "Torque", "Kuchning aylantiruvchi ta’siri: $M = Fl$.", 6),
    ("Garmonik tebranish", "Гармоническое колебание", "Harmonic oscillation", "Kattalik vaqt bo‘yicha sinus yoki kosinus qonuni bilan o‘zgaradigan tebranish.", 7),
    ("Matematik mayatnik", "Математический маятник", "Simple pendulum", "Cho‘zilmaydigan vaznsiz ipga osilgan moddiy nuqta; davri $T = 2\\pi\\sqrt{l/g}$.", 7),
    ("Bo‘ylama to‘lqin", "Продольная волна", "Longitudinal wave", "Muhit zarralari to‘lqin tarqalish yo‘nalishi bo‘ylab tebranadigan to‘lqin.", 7),
    ("Avogadro doimiysi", "Постоянная Авогадро", "Avogadro constant", "Bir mol moddadagi zarralar soni: $N_A \\approx 6{,}02\\cdot10^{23}$ mol⁻¹.", 8),
    ("Ideal gaz", "Идеальный газ", "Ideal gas", "Molekulalari orasidagi o‘zaro ta’sirni (to‘qnashuvdan tashqari) hisobga olmasa ham bo‘ladigan gaz modeli.", 9),
    ("Nisbiy namlik", "Относительная влажность", "Relative humidity", "Havodagi suv bug‘i bosimining shu temperaturadagi to‘yingan bug‘ bosimiga nisbati (%).", 9),
    ("Ichki energiya", "Внутренняя энергия", "Internal energy", "Jismni tashkil etgan zarralar harakati va o‘zaro ta’siri energiyalarining yig‘indisi.", 10),
    ("Adiabatik jarayon", "Адиабатический процесс", "Adiabatic process", "Tashqi muhit bilan issiqlik almashinuvisiz sodir bo‘ladigan jarayon.", 10),
    ("Solishtirma issiqlik sig‘imi", "Удельная теплоёмкость", "Specific heat capacity", "1 kg moddani 1 K ga isitish uchun zarur issiqlik miqdori.", 10),
    ("Paskal qonuni", "Закон Паскаля", "Pascal’s law", "Suyuqlik yoki gazga berilgan bosim barcha yo‘nalishlarda o‘zgarishsiz uzatiladi.", 11),
    ("Arximed kuchi", "Сила Архимеда", "Buoyant force", "Suyuqlik yoki gazga botirilgan jismga ta’sir etuvchi, siqib chiqarilgan muhit og‘irligiga teng ko‘taruvchi kuch.", 11),
    ("Sirt taranglik", "Поверхностное натяжение", "Surface tension", "Suyuqlik sirtini qisqartirishga intiluvchi kuchning sirt chegarasi uzunligiga nisbati.", 11),
    ("Elektr zaryadi", "Электрический заряд", "Electric charge", "Jismlarning elektromagnit o‘zaro ta’sirga kirishish xossasini ifodalovchi kattalik; birligi kulon (C).", 12),
    ("Kulon qonuni", "Закон Кулона", "Coulomb’s law", "Ikki nuqtaviy zaryadning o‘zaro ta’sir kuchi: $F = k\\,q_1q_2/r^2$.", 12),
    ("Elektr maydon kuchlanganligi", "Напряжённость электрического поля", "Electric field strength", "Maydonning birlik musbat zaryadga ta’sir kuchi: $E = F/q$.", 12),
    ("Elektr sig‘im", "Электроёмкость", "Capacitance", "Zaryadning potensiallar farqiga nisbati: $C = q/U$; birligi farad (F).", 12),
    ("Om qonuni", "Закон Ома", "Ohm’s law", "Zanjir qismidagi tok kuchlanishga to‘g‘ri, qarshilikka teskari proporsional: $I = U/R$.", 13),
    ("Joul–Lens qonuni", "Закон Джоуля–Ленца", "Joule’s law", "Tok o‘tganda ajralgan issiqlik miqdori: $Q = I^2Rt$.", 13),
    ("Termoelektron emissiya", "Термоэлектронная эмиссия", "Thermionic emission", "Qizdirilgan metall sirtidan elektronlarning chiqishi.", 14),
    ("Plazma", "Плазма", "Plasma", "Ionlashgan, umuman elektroneytral gaz holati.", 14),
    ("Magnit induksiya", "Магнитная индукция", "Magnetic flux density", "Magnit maydonning kuch xarakteristikasi; birligi tesla (T).", 15),
    ("Lorens kuchi", "Сила Лоренца", "Lorentz force", "Magnit maydonda harakatlanayotgan zaryadga ta’sir etuvchi kuch: $F = qvB\\sin\\alpha$.", 15),
    ("Elektromagnit induksiya", "Электромагнитная индукция", "Electromagnetic induction", "Magnit oqimi o‘zgarganda berk konturda EYuK hosil bo‘lishi: $\\varepsilon = -d\\Phi/dt$.", 16),
    ("Induktivlik", "Индуктивность", "Inductance", "Kontur orqali o‘tuvchi magnit oqimining tok kuchiga nisbati; birligi genri (H).", 16),
    ("Tomson formulasi", "Формула Томсона", "Thomson’s formula", "Tebranish konturining xususiy tebranish davri: $T = 2\\pi\\sqrt{LC}$.", 17),
    ("Ta’sir etuvchi qiymat", "Действующее значение", "RMS value", "Aktiv qarshilikda shuncha issiqlik ajratadigan o‘zgarmas tok qiymati: $I = I_0/\\sqrt{2}$.", 18),
    ("Interferensiya", "Интерференция", "Interference", "Kogerent to‘lqinlar qo‘shilganda intensivlikning fazoda qayta taqsimlanishi.", 19),
    ("Difraksiya", "Дифракция", "Diffraction", "To‘lqinlarning to‘siqlarni aylanib o‘tishi va geometrik soya sohasiga kirishi.", 20),
    ("Qutblanish", "Поляризация", "Polarization", "Ko‘ndalang to‘lqin tebranishlari yo‘nalishining tartiblanganligi.", 21),
    ("Dispersiya", "Дисперсия", "Dispersion", "Sindirish ko‘rsatkichining yorug‘lik to‘lqin uzunligiga bog‘liqligi.", 21),
    ("To‘la ichki qaytish", "Полное внутреннее отражение", "Total internal reflection", "Optik zichroq muhitdan siyrakroq muhitga o‘tishda tushish burchagi chegaraviy burchakdan katta bo‘lganda yorug‘likning to‘liq qaytishi.", 22),
    ("Optik kuch", "Оптическая сила", "Optical power", "Linza fokus masofasiga teskari kattalik: $D = 1/F$; birligi dioptriya.", 22),
    ("Absolyut qora jism", "Абсолютно чёрное тело", "Black body", "O‘ziga tushgan barcha nurlanishni yutadigan ideal jism.", 23),
    ("Fotoeffekt", "Фотоэффект", "Photoelectric effect", "Yorug‘lik ta’sirida moddadan elektronlarning chiqishi: $h\\nu = A + mv^2/2$.", 23),
    ("Foton", "Фотон", "Photon", "Elektromagnit nurlanish kvanti; energiyasi $E = h\\nu$.", 23),
    ("Yoritilganlik", "Освещённость", "Illuminance", "Sirtga tushayotgan yorug‘lik oqimining yuzaga nisbati; birligi lyuks (lx).", 24),
    ("Bor postulatlari", "Постулаты Бора", "Bohr’s postulates", "Atomdagi elektronning statsionar orbitalari va o‘tishlarda foton chiqarish/yutish haqidagi qoidalar.", 25),
    ("Yarim yemirilish davri", "Период полураспада", "Half-life", "Radioaktiv yadrolarning yarmi yemiriladigan vaqt.", 26),
    ("Massa defekti", "Дефект массы", "Mass defect", "Yadro tarkibidagi nuklonlar massalari yig‘indisi bilan yadro massasi orasidagi farq.", 27),
    ("Zanjir reaksiya", "Цепная реакция", "Chain reaction", "Bo‘linishda ajralgan neytronlar yangi bo‘linishlarni yuzaga keltiradigan o‘z-o‘zini davom ettiruvchi yadro reaksiyasi.", 27),
]

# ---------------- Dasturiy vositalar ----------------
VOSITALAR = [
    ("PhET Interactive Simulations", "Simulyatsiya", "Kolorado universitetining bepul interaktiv simulyatsiyalari: mexanika, elektr, optika, kvant fizikasi. Brauzerda ishlaydi, rus tilida ham mavjud.", "https://phet.colorado.edu/", "Bepul"),
    ("Tracker", "Video tahlil", "Tajriba videosi asosida jism harakatini kadrma-kadr tahlil qilish: yo‘l, tezlik, tezlanish grafiklari.", "https://physlets.org/tracker/", "Bepul, ochiq kodli"),
    ("GeoGebra", "Grafik va modellashtirish", "Vektorlar, grafiklar, nurlar yo‘lini yasash va oddiy fizik modellar uchun.", "https://www.geogebra.org/", "Bepul"),
    ("Desmos", "Grafik kalkulyator", "Formulalar grafigini tez chizish, parametrlarni slayder bilan o‘zgartirish.", "https://www.desmos.com/calculator", "Bepul"),
    ("Python (NumPy, Matplotlib, Jupyter)", "Hisoblash", "Laboratoriya natijalarini qayta ishlash, xatoliklarni hisoblash, grafik va approksimatsiya.", "https://www.python.org/", "Bepul, ochiq kodli"),
    ("LibreOffice Calc / MS Excel", "Elektron jadval", "O‘lchov jadvallari, o‘rtacha qiymat va xatolik, eng kichik kvadratlar usuli bilan grafik.", "https://www.libreoffice.org/", "Bepul / pullik"),
    ("Algodoo", "2D fizika muhiti", "Kuchlar, to‘qnashuvlar, ishqalanish va optikani sudrab-tashlab modellashtirish.", "https://www.algodoo.com/", "Bepul"),
    ("OpenStax University Physics", "Darslik", "Uch jildli bepul universitet fizika darsligi (ingliz tilida).", "https://openstax.org/subjects/science", "Bepul"),
    ("HyperPhysics", "Ma’lumotnoma", "Fizika tushunchalari xaritasi va formulalar ma’lumotnomasi (ingliz tilida).", "http://hyperphysics.phy-astr.gsu.edu/hbase/index.html", "Bepul"),
    ("MIT OpenCourseWare", "Ochiq kurslar", "MIT kurslari materiallari; fan dasturidagi axborot resurslaridan biri.", "https://ocw.mit.edu/", "Bepul"),
    ("ZiyoNET", "Ta’lim portali", "O‘zbekiston ta’lim axborot tarmog‘i; o‘zbek tilidagi darslik va qo‘llanmalar.", "https://www.ziyonet.uz/", "Bepul"),
]

# ---------------- PhET simulyatorlari (fan dasturi ma'ruzalariga moslab) ----------------
PHET = [
    (1, "Projectile Motion", "projectile-motion", "Otilgan jism trayektoriyasi, tezlik va tezlanish vektorlari"),
    (3, "Collision Lab", "collision-lab", "Impuls va to‘qnashuvlar (5-ma’ruza bilan ham bog‘liq)"),
    (4, "Hooke’s Law", "hookes-law", "Elastiklik kuchi va prujina bikirligi"),
    (4, "Gravity Force Lab", "gravity-force-lab", "Butun olam tortishish qonuni"),
    (5, "Energy Skate Park", "energy-skate-park", "Kinetik va potensial energiya, saqlanish qonuni"),
    (6, "Gravity and Orbits", "gravity-and-orbits", "Orbital harakat, tortishish va aylanma harakat"),
    (7, "Pendulum Lab", "pendulum-lab", "Matematik va fizik mayatnik davri"),
    (7, "Masses and Springs", "masses-and-springs", "Prujinali mayatnik, garmonik tebranish energiyasi"),
    (7, "Wave on a String", "wave-on-a-string", "Ko‘ndalang to‘lqin, amplituda, chastota, qaytish"),
    (8, "Gas Properties", "gas-properties", "Molekulalar harakati, bosim, temperatura, gaz qonunlari"),
    (11, "Fluid Pressure and Flow", "fluid-pressure-and-flow", "Suyuqlik bosimi va Bernulli tenglamasi"),
    (12, "Coulomb’s Law", "coulombs-law", "Nuqtaviy zaryadlar o‘zaro ta’siri"),
    (12, "Charges and Fields", "charges-and-fields", "Elektr maydon kuchlanganligi va potensial"),
    (12, "Capacitor Lab: Basics", "capacitor-lab-basics", "Yassi kondensator sig‘imi va energiyasi"),
    (13, "Circuit Construction Kit: DC", "circuit-construction-kit-dc", "O‘zgarmas tok zanjirlari, Om qonuni, Kirxgof qoidalari"),
    (16, "Faraday’s Electromagnetic Lab", "faradays-electromagnetic-lab", "Elektromagnit induksiya, generator, transformator"),
    (18, "Circuit Construction Kit: AC", "circuit-construction-kit-ac", "O‘zgaruvchan tok, RLC zanjir, rezonans"),
    (19, "Wave Interference", "wave-interference", "Ikki manbadan interferensiya, difraksiya (20-ma’ruza)"),
    (22, "Bending Light", "bending-light", "Qaytish, sinish, to‘la ichki qaytish, prizma"),
    (22, "Geometric Optics", "geometric-optics", "Linzalar va ko‘zgularda tasvir yasash"),
    (23, "Blackbody Spectrum", "blackbody-spectrum", "Issiqlik nurlanishi, Vin siljish qonuni"),
    (23, "Photoelectric Effect", "photoelectric", "Tashqi fotoeffekt qonunlari"),
    (25, "Rutherford Scattering", "rutherford-scattering", "Rezerford tajribasi va atomning yadro modeli"),
    (25, "Models of the Hydrogen Atom", "models-of-the-hydrogen-atom", "Tomson, Rezerford, Bor modellari"),
    (26, "Alpha Decay", "alpha-decay", "Alfa-yemirilish va yarim yemirilish davri"),
    (27, "Nuclear Fission", "nuclear-fission", "Yadro bo‘linishi va zanjir reaksiya"),
]
