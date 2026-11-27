"""Sayt sahifalarini tekshirish: ichki havolalar, ankorlar (#id), resurslar va fayl nomlari harf registri.

Ishlatish:  python tools/check_pages.py .
GitHub Pages fayl nomlarida katta-kichik harfni farqlaydi, Windows esa farqlamaydi — shuning uchun
nomlar diskdagi aniq ro'yxat bilan solishtiriladi.
"""
import html
import os
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()


def exact_exists(path: Path) -> bool:
    """Fayl mavjudligini harf registrini hisobga olib tekshiradi."""
    try:
        rel = path.resolve().relative_to(ROOT)
    except ValueError:
        return False
    cur = ROOT
    for part in rel.parts:
        if not cur.is_dir() or part not in os.listdir(cur):
            return False
        cur = cur / part
    return True


ids_cache = {}


def ids_of(path: Path):
    if path not in ids_cache:
        txt = path.read_text(encoding="utf-8", errors="replace")
        ids_cache[path] = set(re.findall(r'\bid="([^"]+)"', txt))
    return ids_cache[path]


def main():
    pages = sorted(p for p in ROOT.rglob("*.html") if not p.name.startswith("_") and "vendor" not in p.parts and ".git" not in p.parts)
    bad, checked = [], 0
    for page in pages:
        txt = page.read_text(encoding="utf-8", errors="replace")
        for attr, url in re.findall(r'\b(href|src)="([^"]+)"', txt):
            url = html.unescape(url)
            if re.match(r"^(https?:|mailto:|tel:|data:|javascript:)", url):
                continue
            path_part, _, anchor = url.partition("#")
            path_part = path_part.split("?")[0]
            target = page if not path_part else (page.parent / path_part)
            checked += 1
            if not exact_exists(target):
                bad.append(f"{page.relative_to(ROOT)}: {attr}={url} — fayl topilmadi")
                continue
            if anchor and target.suffix == ".html" and anchor not in ids_of(target):
                bad.append(f"{page.relative_to(ROOT)}: {url} — #{anchor} ankori yo'q")
    print(f"Sahifalar: {len(pages)}, tekshirilgan havolalar: {checked}, xato: {len(bad)}")
    for b in bad[:200]:
        print("  ✗", b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
