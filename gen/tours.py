"""Interaktiv modellar uchun ovozli avtomatik namoyish ssenariylari.
Har bir qadam: (parametrlar, izoh). Logarifmik parametrlar daraja ko'rsatkichida beriladi (masalan 2 → 10²).
Tanlov (select) uchun qiymat '#indeks' ko'rinishida."""

T = {
 "vernier": [
  ({"res": "#0", "L": 23.47}, "Bu shtangensirkul modeli. Yuqorida asosiy shkala, pastda nonius. Nonius nolidan chapdagi butun millimetrlar soni yigirma uch. Endi noniusning qaysi chizig‘i asosiy shkala chizig‘i bilan aniq ustma-ust tushishini qidiramiz."),
  ({"L": 23.47}, "Beshinchi chiziq mos tushdi. Demak, o‘qish yigirma uch butun o‘ndan besh millimetr. Nonius bo‘limining qiymati o‘ndan bir millimetr — bu asbobning aniqligi."),
  ({"res": "#1", "L": 41.85}, "Endi yigirma bo‘limli noniusni tanlaymiz. Uning aniqligi yuzdan besh millimetr. O‘qish qoidasi o‘zgarmaydi: butun millimetrlar va mos tushgan chiziq tartib raqami ko‘paytirilgan aniqlik."),
  ({"res": "#0", "L": 12.6}, "Endi o‘zingiz uzunlikni o‘zgartirib, avval o‘qishni daftarga yozing, keyin o‘ng tomondagi natija bilan solishtiring.")],
 "kinem": [
  ({"x0": 0, "v0": 8, "a": -2, "t": 2}, "Chapda koordinata grafigi, o‘ngda tezlik grafigi. Boshlang‘ich tezlik sakkiz metr sekund, tezlanish manfiy: jism sekinlashmoqda."),
  ({"t": 4}, "To‘rtinchi sekundda tezlik nolga teng — jism to‘xtadi va koordinata grafigi eng yuqori nuqtaga yetdi. Tezlik grafigi ostidagi yuza ko‘chishga teng."),
  ({"t": 8}, "Sakkizinchi sekundda jism boshlang‘ich nuqtaga qaytdi: ko‘chish nolga teng, ammo bosib o‘tilgan yo‘l o‘ttiz ikki metr. Ko‘chish va yo‘lni farqlang."),
  ({"a": 0, "t": 6}, "Tezlanishni nolga tenglasak, harakat tekis bo‘ladi: koordinata grafigi to‘g‘ri chiziq, tezlik grafigi gorizontal chiziq.")],
 "projectile": [
  ({"v0": 20, "al": 45, "h0": 0, "pl": "#0"}, "Jism yigirma metr sekund tezlik bilan qirq besh gradus burchak ostida otildi. Qizil strelka gorizontal tezlik, yashil strelka vertikal tezlik. Gorizontal tezlik butun parvoz davomida o‘zgarmaydi."),
  ({"al": 30}, "Burchakni o‘ttiz gradusga kamaytiramiz. Uchish uzoqligi biroz kamaydi, balandlik esa sezilarli pasaydi. O‘ttiz va oltmish gradusda uzoqlik bir xil bo‘ladi."),
  ({"al": 45, "pl": "#2"}, "Endi xuddi shu otishni Oyda bajaramiz. Erkin tushish tezlanishi olti marta kichik, shuning uchun uchish uzoqligi va balandlik qariyb olti marta ortadi."),
  ({"pl": "#0", "h0": 20, "al": 0}, "Yigirma metr balandlikdan gorizontal otish. Uchish vaqti faqat balandlikka bog‘liq va tezlikka bog‘liq emas.")],
 "newton": [
  ({"al": 10, "mu": .3, "m": 1}, "Qiyalik o‘n gradus, ishqalanish koeffitsiyenti nol butun o‘ndan uch. Qiya bo‘ylab tortuvchi kuch tinchlikdagi ishqalanish bilan muvozanatlashgan, jism tinch turibdi."),
  ({"al": 30}, "Burchakni o‘ttiz gradusga oshiramiz. Burchak tangensi ishqalanish koeffitsiyentidan oshdi, jism tezlanish bilan sirpana boshladi."),
  ({"mu": 0}, "Ishqalanishni yo‘qotsak, tezlanish g ko‘paytirilgan sinus alfaga teng bo‘ladi: taxminan to‘rt butun to‘qqiz o‘ndan metr sekund kvadrat."),
  ({"mu": .3, "m": 4}, "Massani to‘rt marta oshirdik, lekin tezlanish o‘zgarmadi: og‘irlik ham, ishqalanish ham massaga proporsional.")],
 "spring": [
  ({"F": 100, "L0": 1.5, "d": .5, "mat": "#0"}, "Po‘lat simga yuz nyuton kuch qo‘yildi. Grafikda uzayish kuchga to‘g‘ri proporsional — bu Guk qonuni."),
  ({"d": 1}, "Sim diametrini ikki marta oshirsak, kesim yuzasi to‘rt marta ortadi va uzayish to‘rt marta kamayadi."),
  ({"d": .5, "mat": "#2"}, "Alyuminiyning Yung moduli po‘latnikidan qariyb uch marta kichik, shuning uchun bir xil kuchda u uch marta ko‘p uzayadi.")],
 "beam": [
  ({"F": 10, "l": .6, "b": 15, "hh": 3, "mat": "#0"}, "Ikki tayanchga qo‘yilgan po‘lat sterjen o‘rtasiga o‘n nyuton yuk osildi. Egilish strelasi millimetrning bir necha o‘ndan bir qismiga teng."),
  ({"hh": 6}, "Qalinlikni ikki marta oshiramiz. Egilish sakkiz marta kamaydi, chunki inersiya momenti qalinlik kubiga proporsional."),
  ({"hh": 3, "l": 1}, "Tayanchlar orasini oshirsak, egilish masofaning kubiga proporsional ravishda keskin ortadi."),
  ({"l": .6, "mat": "#3"}, "Alyuminiy sterjen po‘latnikiga qaraganda qariyb uch marta ko‘p egiladi. Laboratoriyada aynan shu bog‘lanishdan Yung moduli topiladi.")],
 "collision": [
  ({"m1": 1, "m2": 1, "v1": 3, "v2": 0, "k": 1}, "Massalari teng ikki jismning elastik to‘qnashuvi. To‘qnashuvdan so‘ng ular tezliklarini almashadi: birinchi jism to‘xtaydi, ikkinchisi uch metr sekund tezlik bilan ketadi."),
  ({"k": 0}, "Endi to‘qnashuv mutlaq noelastik: jismlar birlashib, umumiy tezlik bilan harakatlanadi. Impuls saqlandi, ammo kinetik energiyaning yarmi ichki energiyaga aylandi."),
  ({"k": 1, "m2": 5}, "Yengil jism og‘ir jismga urilsa, orqaga qaytadi. Ustunlar diagrammasida impuls har doim saqlanishini ko‘ring.")],
 "rotation": [
  ({"hgt": 1, "al": 20, "sh": "#1"}, "Bir metr balandlikdan disk dumalab tushmoqda. Uning potensial energiyasi ilgarilanma va aylanma kinetik energiyaga taqsimlanadi."),
  ({"sh": "#0"}, "Halqaning inersiya momenti eng katta. Energiyaning yarmi aylanishga ketadi, shuning uchun halqa eng sekin tushadi."),
  ({"sh": "#2"}, "Shar eng tez tushadi: aylanma energiya ulushi atigi yettidan ikki. O‘ngdagi diagrammada barcha shakllarning tushish vaqtlari taqqoslangan.")],
 "oscill": [
  ({"type": "#0", "L": 1, "A0": 10, "b": 0}, "Bir metr uzunlikdagi matematik mayatnik. Kichik amplitudada uning davri taxminan ikki sekund va massaga bog‘liq emas."),
  ({"L": .25}, "Uzunlikni to‘rt marta kamaytirsak, davr ikki marta kamayadi, chunki davr uzunlikning kvadrat ildiziga proporsional."),
  ({"L": 1, "type": "#1"}, "Endi bir metrlik sterjen — fizik mayatnik. Uning keltirilgan uzunligi uchdan ikki metr, shuning uchun davri matematik mayatnikdan kichik."),
  ({"type": "#2", "m": .5, "kk": 20, "b": .15}, "Prujinali tebrangich: davr massa va bikrlikka bog‘liq. So‘nish koeffitsiyentini oshirsak, amplituda eksponensial kamayadi.")],
 "maxwell": [
  ({"T": 300, "gas": "#2"}, "Uch yuz kelvindagi azot molekulalarining tezliklar bo‘yicha taqsimoti. Eng ehtimolli tezlik taxminan to‘rt yuz yigirma metr sekund."),
  ({"T": 1200}, "Temperaturani to‘rt marta oshirdik: taqsimot o‘ngga siljidi va kengaydi, tezliklar ikki marta ortdi. Egri chiziq ostidagi yuza o‘zgarmaydi."),
  ({"T": 300, "gas": "#0"}, "Vodorod molekulasi azotdan o‘n to‘rt marta yengil, shuning uchun bir xil temperaturada uning tezliklari qariyb uch butun o‘ndan yetti marta katta.")],
 "gas": [
  ({"pr": "#0", "x": 2, "i": "#1", "n": .5, "T1": 300}, "Izotermik kengayish: hajm ikki marta ortdi, bosim ikki marta kamaydi. Ichki energiya o‘zgarmaydi, olingan barcha issiqlik ishga sarflanadi."),
  ({"pr": "#1"}, "Izobarik kengayish: bosim o‘zgarmas, temperatura ikki marta ortdi. Issiqlikning bir qismi ichki energiyani oshiradi, qolgani ish bajaradi."),
  ({"pr": "#2"}, "Izoxorik isitish: hajm o‘zgarmas, gaz ish bajarmaydi. Barcha issiqlik ichki energiyaga aylanadi."),
  ({"pr": "#3"}, "Adiabatik kengayish: issiqlik almashinuvi yo‘q. Gaz ichki energiyasi hisobiga ish bajaradi va soviydi; egri chiziq izotermaga qaraganda tikroq.")],
 "calorimeter": [
  ({"m1": 200, "t1": 20, "mat": "#0", "m2": 100, "t2": 100, "Ck": 40}, "Yigirma gradusli suvga yuz gradusgacha qizdirilgan yuz gramm alyuminiy tushirildi. Jism bergan issiqlik suv va kalorimetr olgan issiqlikka teng."),
  ({"mat": "#3"}, "Qo‘rg‘oshinning solishtirma issiqlik sig‘imi ancha kichik, shuning uchun suv deyarli isimaydi."),
  ({"mat": "#4", "m2": 200, "t2": 60}, "Ikki xil temperaturadagi suvni aralashtiramiz: muvozanat temperaturasi massalar bo‘yicha o‘rtacha qiymatga yaqin, kalorimetr uni biroz pasaytiradi.")],
 "capillary": [
  ({"liq": "#0", "r": .5}, "Suv shishani ho‘llaydi, shuning uchun kapillyarda yuqoriga ko‘tariladi. Yarim millimetrli naychada ko‘tarilish taxminan uch santimetr."),
  ({"r": .1}, "Radiusni besh marta kamaytirsak, ko‘tarilish balandligi besh marta ortadi: balandlik radiusga teskari proporsional."),
  ({"liq": "#3", "r": .5}, "Simob shishani ho‘llamaydi: menisk qavariq va simob naychada pastga tushadi.")],
 "archimedes": [
  ({"body": "#0", "V": 40, "liq": "#0", "dip": 0}, "Alyuminiy jism havoda tortilmoqda. Dinamometr uning og‘irligini ko‘rsatadi."),
  ({"dip": 100}, "Jismni suvga to‘liq botiramiz. Dinamometr ko‘rsatishi Arximed kuchi qadar kamaydi. Shu ikki o‘lchovdan jism zichligi topiladi."),
  ({"liq": "#3"}, "Glitserinda Arximed kuchi kattaroq, chunki suyuqlik zichroq. Hisoblangan jism zichligi esa o‘zgarmaydi.")],
 "coulomb": [
  ({"q1": 5, "q2": -5, "d": 10, "eps": 1}, "Qarama-qarshi ishorali ikki zaryad — elektr dipol. Maydon chiziqlari musbat zaryaddan chiqib, manfiy zaryadga kiradi."),
  ({"q2": 5}, "Ikkinchi zaryad ishorasini almashtirdik: zaryadlar endi itariladi, o‘rtada maydon nolga teng nuqta paydo bo‘ldi."),
  ({"d": 5}, "Masofani ikki marta kamaytirsak, o‘zaro ta’sir kuchi to‘rt marta ortadi — Kulon qonuni."),
  ({"d": 10, "eps": 81}, "Zaryadlarni suvga joylashtirsak, kuch sakson bir marta kamayadi. Shu sababli suv tuzlarni yaxshi eritadi.")],
 "capacitor": [
  ({"C": 2, "R": 1, "U0": 12, "mode": "#0"}, "Yuz mikrofaradli kondensator o‘n kiloomli rezistor orqali zaryadlanmoqda. Vaqt doimiysi bir sekund: shu vaqtda kuchlanish o‘z qiymatining oltmish uch foiziga yetadi."),
  ({"R": 2}, "Qarshilikni o‘n marta oshirsak, zaryadlanish o‘n marta sekinlashadi. Tok esa boshida eng katta va eksponensial kamayadi."),
  ({"R": 1, "mode": "#1"}, "Razryadlanishda kondensator kuchlanishi har bir vaqt doimiysida e marta kamayadi.")],
 "circuit": [
  ({"E": 12, "r": 1, "R": 5}, "O‘n ikki voltli manba, ichki qarshiligi bir om. Tashqi qarshilik besh om bo‘lganda tok ikki amper."),
  ({"R": 1}, "Tashqi qarshilik ichki qarshilikka teng bo‘lganda tashqi zanjirdagi quvvat maksimal, ammo foydali ish koeffitsiyenti atigi ellik foiz."),
  ({"R": .1}, "Qisqa tutashuvga yaqin holat: tok juda katta, deyarli butun quvvat manba ichida issiqlikka aylanadi.")],
 "kirchhoff": [
  ({"E1": 6, "E2": 6, "R1": 10, "R2": 20, "R3": 10}, "Ikki manbali ikki konturli zanjir. Tugun uchun birinchi qoida: tugunga kirgan toklar yig‘indisi chiqqan toklar yig‘indisiga teng."),
  ({"E2": 0}, "Ikkinchi manbani olib tashlasak, o‘ng tarmoqdagi tok yo‘nalishini o‘zgartiradi. Manfiy ishora tanlangan yo‘nalish noto‘g‘ri ekanini bildiradi, xolos."),
  ({"E2": 9, "R3": 30}, "Har qanday parametrlarda ham tugun qoidasi va kontur qoidasi bajariladi, quvvat balansi saqlanadi.")],
 "wheatstone": [
  ({"Rx": 120, "R0": 100, "l1": 30}, "Uitston ko‘prigi muvozanatda emas: galvanometrdan tok o‘tmoqda."),
  ({"l1": 54.5}, "Sirpang‘ichni ellik to‘rt butun o‘ndan besh santimetrga suramiz. Galvanometr toki nolga yaqin — ko‘prik muvozanatda. Endi noma’lum qarshilik reoxord yelkalari nisbatidan topiladi."),
  ({"Rx": 300}, "Noma’lum qarshilik o‘zgarsa, muvozanat buziladi. O‘lchash aniqligi eng yuqori bo‘lishi uchun muvozanat reoxord o‘rtasiga yaqin bo‘lgani ma’qul.")],
 "vacdiode": [
  ({"U": 40, "T": 2300}, "Vakuum diodning volt-amper xarakteristikasi. Kichik kuchlanishlarda tok kuchlanishning uch ikkinchi darajasiga proporsional ortadi."),
  ({"U": 180}, "Katta kuchlanishda tok to‘yinadi: katoddan chiqqan barcha elektronlar anodga yetib boradi."),
  ({"T": 2500}, "Katod temperaturasini oshirsak, termoelektron emissiya keskin kuchayadi va to‘yinish toki bir necha marta ortadi.")],
 "bfield": [
  ({"mode": "#0", "I": 1, "r": 5}, "To‘g‘ri tokning magnit induksiya chiziqlari konsentrik aylanalardan iborat. Induksiya masofaga teskari proporsional kamayadi."),
  ({"mode": "#2", "I": .1, "r": 10, "N": 20, "Bh": 26}, "Tangens-galvanometr: g‘altak maydoni Yer maydoniga perpendikulyar. Kompas strelkasi natijaviy maydon bo‘ylab buriladi."),
  ({"I": .21}, "Tokni oshirsak, og‘ish burchagi ortadi. Burchak qirq besh gradusga yaqin bo‘lganda o‘lchash xatoligi eng kichik bo‘ladi — hozir aynan shunday.")],
 "induction": [
  ({"v": 1, "N": 300, "B0": .2}, "Magnit g‘altak ichidan o‘tmoqda. Magnit yaqinlashganda oqim ortadi, uzoqlashganda kamayadi — EYuK ishorasi o‘zgaradi."),
  ({"v": 2}, "Tezlikni ikki marta oshirsak, EYuK ham ikki marta ortadi, chunki u oqimning o‘zgarish tezligiga proporsional."),
  ({"v": 1, "N": 900}, "O‘ramlar sonini uch marta oshirsak, EYuK uch marta ortadi. Bu Faradey qonuni.")],
 "rlc": [
  ({"L": 1, "C": 0, "R": 2}, "O‘n millihenri va bir mikrofaraddan iborat kontur. Tomson formulasi bo‘yicha davr taxminan nol butun yuzdan oltmish uch millisekund."),
  ({"R": 30}, "Qarshilikni oshirsak, tebranishlar tez so‘nadi va rezonans egri chizig‘i kengayadi — konturning asllik koeffitsiyenti kamayadi."),
  ({"R": 2, "C": 2}, "Sig‘imni yuz marta oshirsak, xususiy chastota o‘n marta kamayadi.")],
 "ac": [
  ({"f": 50, "R": 40, "L": 200, "C": 100, "U": 220}, "Ellik gersli tarmoqqa ulangan ketma-ket zanjir. Induktiv qarshilik sig‘im qarshiligidan katta, shuning uchun tok kuchlanishdan orqada qoladi."),
  ({"f": 36}, "Chastotani o‘ttiz olti gersga tushiramiz: induktiv va sig‘im qarshiliklar tenglashdi. Bu kuchlanishlar rezonansi — tok maksimal, faza siljishi nol."),
  ({"f": 50, "C": 20}, "Sig‘imni kamaytirsak, sig‘im qarshiligi ortadi va tok kuchlanishdan oldinga o‘tadi. Quvvat koeffitsiyenti kamayadi.")],
 "young": [
  ({"lam": 600, "d": .5, "L": 1, "b": .05}, "Ikki tirqishdan o‘tgan yorug‘lik ekranda yorug‘ va qorong‘i polosalar hosil qiladi. Polosalar kengligi bir butun o‘ndan ikki millimetr."),
  ({"lam": 450}, "Ko‘k yorug‘likda to‘lqin uzunligi kichik, polosalar zichlashadi."),
  ({"lam": 600, "d": .25}, "Tirqishlar orasini ikki marta kamaytirsak, polosalar ikki marta kengayadi.")],
 "grating": [
  ({"lam": 532, "n": 300, "N": 12, "L": .5}, "Bir millimetrida uch yuz shtrixli panjara. Bosh maksimumlar burchaklari panjara formulasidan aniqlanadi."),
  ({"N": 40}, "Yoritilgan shtrixlar sonini oshirsak, bosh maksimumlar ingichkalashadi — panjaraning ajrata olish qobiliyati ortadi."),
  ({"n": 1000, "lam": 650}, "Shtrixlar zichligi katta panjarada maksimumlar katta burchaklarga siljiydi va tartiblar soni kamayadi.")],
 "malus": [
  ({"phi": 0, "n": 1.5, "th": 30}, "Qutblagich va analizator parallel: yorug‘lik to‘liq o‘tadi."),
  ({"phi": 60}, "Oltmish gradusda intensivlik to‘rt marta kamaydi, chunki kosinus kvadrati to‘rtdan biriga teng. Bu Malyus qonuni."),
  ({"phi": 90, "th": 56.3}, "Analizator perpendikulyar — yorug‘lik o‘tmaydi. O‘ng grafikda tushish burchagi Bryuster burchagiga teng bo‘lganda parallel tashkil etuvchi qaytmaydi, qaytgan nur to‘liq qutblanadi.")],
 "lens": [
  ({"f": 15, "d": 40, "hb": 3}, "Yig‘uvchi linza, buyum ikki fokus masofasidan uzoqda. Tasvir haqiqiy, teskari va kichiklashgan."),
  ({"d": 22}, "Buyumni fokus va ikki fokus oralig‘iga keltirdik: tasvir kattalashdi va uzoqlashdi. Proyektor shu tamoyilda ishlaydi."),
  ({"d": 8}, "Buyum fokus ichida: tasvir mavhum, to‘g‘ri va kattalashgan. Lupa shunday ishlaydi."),
  ({"f": -15, "d": 30}, "Sochuvchi linza har doim mavhum, to‘g‘ri va kichiklashgan tasvir beradi.")],
 "snell": [
  ({"n1": 1, "n2": 1.5, "th": 40}, "Yorug‘lik havodan shishaga o‘tmoqda: sinish burchagi tushish burchagidan kichik, nur normalga yaqinlashadi."),
  ({"n1": 1.5, "n2": 1, "th": 30}, "Endi yorug‘lik shishadan havoga chiqmoqda: nur normaldan uzoqlashadi."),
  ({"th": 45}, "Tushish burchagi kritik burchakdan katta bo‘ldi — to‘la ichki qaytish. Optik tola shu hodisaga asoslangan.")],
 "planck": [
  ({"T": 5800}, "Quyosh sirti temperaturasidagi absolyut qora jism spektri. Maksimum ko‘rinadigan sohada, taxminan besh yuz nanometr atrofida."),
  ({"T": 3000}, "Cho‘g‘lanma lampa temperaturasida maksimum infraqizil sohaga siljidi va nurlanish quvvati qariyb o‘n to‘rt marta kamaydi."),
  ({"T": 9000}, "Issiq yulduzlarda maksimum ultrabinafsha tomonga siljiydi: Vin qonuni. To‘liq quvvat esa temperaturaning to‘rtinchi darajasiga proporsional.")],
 "photo": [
  ({"lam": 400, "met": "#1", "Ip": 70, "U": 1}, "Kaliy katodni binafsha yorug‘lik bilan yoritamiz. Foton energiyasi chiqish ishidan katta — fotoeffekt kuzatiladi."),
  ({"Ip": 30}, "Intensivlikni kamaytirsak, to‘yinish toki kamayadi, ammo tormozlovchi kuchlanish o‘zgarmaydi: elektronlar energiyasi yorug‘lik chastotasiga bog‘liq."),
  ({"Ip": 70, "lam": 650}, "Qizil yorug‘likda foton energiyasi chiqish ishidan kichik — intensivlik qanchalik katta bo‘lmasin, fotoeffekt yo‘q. Bu qizil chegara."),
  ({"lam": 300, "U": -1.5}, "Ultrabinafsha nurda fotoelektronlar energiyasi katta; tormozlovchi kuchlanish orqali uni o‘lchash mumkin.")],
 "photometry": [
  ({"I1": 100, "I2": 25, "x": 1, "al": 0}, "Fotometr ekrani ikki manba o‘rtasida. Birinchi manba to‘rt marta kuchli, shuning uchun ekranning chap tomoni yorug‘roq."),
  ({"x": 1.33}, "Ekranni muvozanat nuqtasiga suramiz: ikkala tomon bir xil yoritilgan. Yorug‘lik kuchlari masofalar kvadratlari nisbatiga teng."),
  ({"al": 60}, "Nurlar qiya tushsa, yoritilganlik tushish burchagi kosinusiga proporsional kamayadi.")],
 "bohr": [
  ({"nu": 3, "nl": 2}, "Elektron uchinchi sathdan ikkinchi sathga o‘tdi. Chiqarilgan foton to‘lqin uzunligi olti yuz ellik olti nanometr — Balmer seriyasining qizil chizig‘i."),
  ({"nu": 2, "nl": 1}, "Ikkinchi sathdan birinchiga o‘tishda Layman seriyasining ultrabinafsha chizig‘i chiqariladi."),
  ({"nu": 6, "nl": 3}, "Uchinchi sathga o‘tishlar Pashen seriyasini beradi — infraqizil soha.")],
 "franck": [
  ({"U": 8, "Ur": .5}, "Elektronlar simob bug‘i orqali tezlatilmoqda. Ularning energiyasi to‘rt butun o‘ndan to‘qqiz elektronvoltga yetguncha to‘qnashuvlar elastik bo‘ladi."),
  ({"U": 25}, "Anod toki har to‘rt butun o‘ndan to‘qqiz voltda keskin kamayadi: elektron atomni qo‘zg‘atib, energiyasini yo‘qotadi. Bu atom energiyasi kvantlanganligining bevosita isboti."),
  ({"Ur": 1.5}, "Tormozlovchi kuchlanishni oshirsak, minimumlar chuqurlashadi, ammo ular orasidagi masofa o‘zgarmaydi.")],
 "decay": [
  ({"iso": "#0", "N0": 400, "sp": .6}, "To‘rt yuzta radioaktiv yadro. Har bir yadro tasodifiy vaqtda yemiriladi, ammo yarim yemirilish davri o‘tganda ularning qariyb yarmi qoladi."),
  ({"N0": 900}, "Yadrolar soni ko‘p bo‘lsa, tasodifiy natija nazariy egri chiziqqa yaqinroq bo‘ladi."),
  ({"iso": "#5", "N0": 400}, "Uglerod o‘n to‘rtning yarim yemirilish davri besh ming yetti yuz o‘ttiz yil. Radiouglerod usulida arxeologik namunalar yoshi aniqlanadi.")],
 "binding": [
  ({"A": 56}, "Solishtirma bog‘lanish energiyasi temir atrofida maksimal — taxminan sakkiz butun o‘ndan sakkiz megaelektronvolt."),
  ({"A": 235}, "Og‘ir yadrolarda bog‘lanish energiyasi kichikroq. Uran yadrosi ikki bo‘lakka bo‘linganda taxminan ikki yuz megaelektronvolt energiya ajraladi."),
  ({"A": 4}, "Yengil yadrolar qo‘shilganda ham energiya ajraladi — bu termoyadro sintezi, Quyosh energiyasining manbai.")],
}
