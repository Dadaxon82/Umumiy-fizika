# Umumiy fizika — interaktiv elektron darslik

Qo‘qon davlat universiteti, Fizika va astronomiya kafedrasi · Fan kodi UMF11210 · 10 ECTS (300 soat) · 2026/2027.
Sayt: https://dadaxon82.github.io/Umumiy-fizika/

## Tarkibi

| Bo‘lim | Fayl |
|---|---|
| Ma’ruzalar | `lectures/lectureN.html` |
| Laboratoriya ishlari | `labs/labN.html` |
| Mustaqil ta’lim yo‘riqnomalari | `yoriqnomalar/MT-NN.html` |
| Darslik haqida (fan dasturi, TN1–TN10, mavzular, adabiyotlar) | `annotatsiya.html` |
| Baholash: JN 30 / ON 20 / YaN 50, rubrikalar, kalkulyator | `baholash.html` |
| Mustaqil ta’lim: 45 mavzu va talablar | `mustaqil.html` |
| O‘qituvchi uchun qo‘llanma | `oqituvchi.html` |
| Atamalar lug‘ati (UZ–RU–EN), dasturiy vositalar | `glossariy.html`, `vositalar.html` |
| Interaktiv modellar va PhET simulyatorlari | `simulyatorlar.html`, `js/sims.js` |

## Imkoniyatlar

- **UZ / RU / EN** — butun sayt Google Translate orqali tarjima qilinadi (yuqoridagi tugmalar).
- **Yangi o‘zbek alifbosi** (O‘→Ö, G‘→Ğ, Sh→Ş, Ch→Ç) — matnlar joriy imloda saqlanadi, sahifa ochilganda avtomatik o‘tkaziladi (`js/app.js`). Tarjima uchun eski imlo ishlatiladi.
- **Kun / tun rejimi**, mundarija, **Tinglash** (brauzer ovozi), formulalar uchun KaTeX (`$...$`).

## Mazmunni tahrirlash

Sahifalar generator orqali quriladi. Matnlarni o‘zgartirish uchun:

- `gen/src/lectures/lectureN.html`, `gen/src/labs/labN.html`, `gen/src/yoriqnomalar/MT-NN.html` — ma’ruza, laboratoriya va MT matnlari. Tuzilishi: `<h1>Sarlavha</h1>`, so‘ng har bir bo‘lim `<section><h2>Nomi</h2> ... </section>`.
- `gen/content.py` — fan dasturi ma’lumotlari, lug‘at, vositalar, PhET ro‘yxati.
- `gen/build.py` — shablon, menyu, bosh sahifa.

Yangi ma’ruza qo‘shish: `gen/src/lectures/lecture25.html` faylini yarating. Keyin repozitoriya ildizida quyidagi buyruqni ishga tushiring:

```
python gen/build.py
```

Bosh sahifa va menyudagi "tez orada" kartochkasi avtomatik faollashadi.
