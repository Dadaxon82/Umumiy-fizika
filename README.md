# Umumiy fizika — interaktiv ovozli elektron darslik

Qo‘qon davlat universiteti, Fizika va astronomiya kafedrasi · 60530100 — Kimyo (bakalavriat) · fan kodi **UMF11210** · 10 ECTS (300 soat: ma’ruza 54, laboratoriya 66, mustaqil ta’lim 180) · 2026/2027 o‘quv yili, 1–2-semestr.

Muallif: **Ergashev Dadaxon**. Sayt: https://dadaxon82.github.io/Umumiy-fizika/

Darslik fan dasturidagi besh bo‘limni qamrab oladi: mexanika, molekulyar fizika va termodinamika, elektr va magnetizm, optika, atom va yadro fizikasi.

## Tarkibi

| Bo‘lim | Fayllar |
|---|---|
| 27 ta ma’ruza (M1–M27): maqsad va TN, reja, tayanch tushunchalar, nazariya (KaTeX formulalar), «Kimyogar uchun» izohlari, 2 ta ishlangan misol, interaktiv model va topshiriqlar, PhET havolalari, SI bilan ishlash topshirig‘i, tipik xato tushunchalar, 10 savolli test, blits-so‘rov, adabiyotlar | `lecture1.html` … `lecture27.html` |
| Laboratoriyaga kirish: o‘lchash xatoliklari (GUM, Styudent koeffitsiyentlari), bilvosita o‘lchash, grafik va eng kichik kvadratlar usuli, Python bilan ishlash, hisobot tuzilishi, 8 savolli test | `laboratoriya.html` |
| 29 ta laboratoriya ishi (33 mashg‘ulot): maqsad, jihozlar, nazariya, bajarish tartibi, namunaviy o‘lchash jadvali, noaniqlik bilan hisoblash, ishlaydigan Python (NumPy) kodi, nazorat savollari | `lab1.html` … `lab33.html` |
| 45 ta mustaqil ta’lim mavzusi (180 soat), 12 ta kimyo yo‘nalishidagi keys-stadi, talablar va akademik halollik | `mustaqil.html` |
| Baholash: JN 30 / ON 20 / YaN 50, TN–nazorat matritsasi, rubrikalar, baho kalkulyatori | `baholash.html` |
| Annotatsiya (uz/ru/en), bibliografik ma’lumot, fan ma’lumotlari, ta’lim natijalari TN1–TN10, xalqaro talablarga muvofiqlik | `annotatsiya.html` |
| O‘qituvchi uchun qo‘llanma, 2 × 15 haftalik taqvim | `oqituvchi.html` |
| Atamalar lug‘ati (141 atama, UZ–RU–EN), dasturiy vositalar va onlayn resurslar | `glossariy.html`, `vositalar.html` |
| 36 ta interaktiv model (brauzerda, ovozli namoyish bilan) | `simulyatorlar.html`, `js/sims.js` |

Ko‘p mashg‘ulotli ishlarning ikkinchi sahifalari (`lab7`, `lab14`, `lab16`, `lab32`) va eski manzillar (`lectures/`, `labs/`, `yoriqnomalar/`) yangi sahifalarga avtomatik yo‘naltiriladi.

## Imkoniyatlar

- **O‘zbekcha ovozli o‘qish.** «Tinglash» tugmasi ma’ruza va laboratoriya matnlarini o‘qiydi: pauza, oldingi/keyingi xatboshi, tezlik, istalgan joydan boshlash. Formulalar so‘z bilan aytiladi. Ovoz oldindan tayyorlangan MP3 fayllardan (`audio/uz/`, Microsoft Edge neyron ovozi `uz-UZ-SardorNeural`) ijro etiladi; MP3 yo‘q joyda brauzer ovozi (Web Speech API) ishlatiladi.
- **Interaktiv modellar.** Har bir model parametrlarni surgich bilan o‘zgartirish, natijani SI birliklarida ko‘rish va «Ovozli namoyish» rejimida bosqichma-bosqich tushuntirishni beradi.
- **Yangi o‘zbek alifbosi** (Ö, Ğ, Ş, Ç): sahifalar yangi imloda ko‘rsatiladi, tarjima va ovoz uchun matn avtomatik 1995-yilgi lotin yozuviga qaytariladi; manba matnlar 1995-yilgi yozuvda saqlanadi (`gen/alifbo.py`, `js/alifbo.js`).
- **UZ / RU / EN** (Google Translate), kun/tun rejimi, chop etish uslubi, elektron doska va telefonlarga moslashuv.
- Shaxsiy ma’lumot to‘planmaydi: testlar brauzerning o‘zida tekshiriladi, hisob yaratilmaydi. Rasmiy topshiriqlar va baholash HEMIS’da.

## Mazmunni tahrirlash

Sahifalar `gen/` papkasidagi Python fayllaridan yaratiladi (HTML fayllarni qo‘lda tahrirlamang — keyingi qurishda ustidan yoziladi):

- `gen/lec_mex.py` (M1–M7), `gen/lec_mol.py` (M8–M11), `gen/lec_el.py` (M12–M18), `gen/lec_opt.py` (M19–M24), `gen/lec_atom.py` (M25–M27) — ma’ruzalar;
- `gen/lab_intro.py` — laboratoriyaga kirish; `gen/labs_a.py`, `gen/labs_b.py` — laboratoriya ishlari;
- `gen/other.py` — mustaqil ta’lim mavzulari, keys-stadilar, lug‘at, vositalar;
- `gen/tours.py` — modellarning ovozli namoyish bosqichlari;
- `gen/common.py` — sarlavha, menyu, adabiyotlar, xalqaro manbalar; `gen/build.py` — sahifa shablonlari va TN matritsasi.

O‘zgartirgandan so‘ng repozitoriya ildizida:

```bash
python gen/build.py .            # barcha sahifalarni qayta yaratish
python tools/check_pages.py .    # ichki havolalar, #ankorlar va fayl nomlari registrini tekshirish
```

## Ovoz fayllari

GitHub’ga (`main`) yuklangach `.github/workflows/ovoz.yml` faqat yangi yoki o‘zgargan xatboshilar uchun MP3 yaratadi. Ovozni almashtirish: Actions → «Ovoz (o‘zbekcha MP3)» → Run workflow → `uz-UZ-SardorNeural` (erkak) yoki `uz-UZ-MadinaNeural` (ayol).

Lokal (Python 3.10+, `pip install edge-tts playwright` va `python -m playwright install chromium`):

```bash
python tools/tts_extract.py . audio/uz/texts.json
TTS_PARALLEL=8 python tools/tts_generate.py audio/uz
```

## GitHub Pages

Settings → Pages → Source: **Deploy from a branch**, Branch: **main**, Folder: **/ (root)** → Save. Sayt statik (HTML/CSS/JS); formulalar uchun KaTeX `vendor/` papkasida — internetsiz ham ishlaydi.

KaTeX — MIT litsenziyasi (`vendor/katex/LICENSE`). PhET simulyatorlari Kolorado universiteti saytida ochiladi.
