#!/usr/bin/env python3
"""Assemble fonts/, css/, licenses/ and SHA256SUMS from the official font packages.

Usage: python3 -I scripts/build.py --dl <dir with unpacked official packages> --notices <dir>

Font files are copied byte for byte. Nothing here subsets, converts or renames
fonts internally: several families declare a Reserved Font Name under the OFL, and
the S-Core licence forbids changing the distributed file at all.
"""
import argparse
import glob
import hashlib
import os
import re
import shutil
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSDELIVR_NPM = "https://cdn.jsdelivr.net/npm"
WEIGHT_BY_NAME = {
    "Thin": 100, "ExtraLight": 200, "Light": 300, "Regular": 400, "Medium": 500,
    "SemiBold": 600, "Bold": 700, "ExtraBold": 800, "Black": 900,
}
NINE = ["1Thin", "2ExtraLight", "3Light", "4Regular", "5Medium", "6SemiBold", "7Bold", "8ExtraBold", "9Black"]


def face(family, src, weight, fmt="woff2"):
    return (
        "@font-face {\n"
        f'  font-family: "{family}";\n'
        "  font-style: normal;\n"
        "  font-display: swap;\n"
        f"  font-weight: {weight};\n"
        f'  src: url("{src}") format("{fmt}");\n'
        "}\n"
    )


def write_css(slug, header, body):
    with open(os.path.join(ROOT, "css", f"{slug}.css"), "w", encoding="utf-8") as fh:
        fh.write(f"/* {header} */\n{body}")


def place(src, slug, name=None):
    dest_dir = os.path.join(ROOT, "fonts", slug)
    os.makedirs(dest_dir, exist_ok=True)
    name = name or os.path.basename(src)
    shutil.copyfile(src, os.path.join(dest_dir, name))
    return f"../fonts/{slug}/{name}"


def licence(src, slug):
    shutil.copyfile(src, os.path.join(ROOT, "licenses", f"{slug}.txt"))


def fontsource_css(pkg, version, css_files, family=None):
    """Pin Fontsource's sliced Korean CSS to absolute jsDelivr URLs, woff2 only."""
    base = f"{JSDELIVR_NPM}/{pkg}@{version}"
    out = []
    for css in css_files:
        text = subprocess.run(
            ["curl", "-fsSL", "-m", "60", f"{base}/{css}"], check=True, capture_output=True, text=True
        ).stdout
        text = re.sub(r"/\*.*?\*/\s*", "", text, flags=re.S)
        text = re.sub(r",\s*url\([^)]*\.woff\)\s*format\('woff'\)", "", text)
        text = text.replace("format('woff2-variations')", "format('woff2')")
        text = text.replace("url(./files/", f"url({base}/files/")
        if family:
            text = re.sub(r"font-family: '[^']+'", f"font-family: '{family}'", text)
        out.append(text.strip() + "\n")
    return "".join(out)


def build(dl, notices):
    for sub in ("css", "fonts", "licenses"):
        shutil.rmtree(os.path.join(ROOT, sub), ignore_errors=True)
        os.makedirs(os.path.join(ROOT, sub))

    # --- Google Fonts families: sliced by unicode-range, served from Fontsource's npm packages.
    write_css(
        "noto-sans-kr", "Noto Sans KR | SIL OFL 1.1 | via @fontsource-variable/noto-sans-kr",
        fontsource_css("@fontsource-variable/noto-sans-kr", "5.3.1", ["index.css"], family="Noto Sans KR"),
    )
    write_css(
        "gothic-a1", "Gothic A1 | SIL OFL 1.1 | via @fontsource/gothic-a1",
        fontsource_css("@fontsource/gothic-a1", "5.3.0", [f"{w}.css" for w in (300, 400, 500, 700)]),
    )
    write_css(
        "ibm-plex-sans-kr", "IBM Plex Sans KR | SIL OFL 1.1 | via @fontsource/ibm-plex-sans-kr",
        fontsource_css("@fontsource/ibm-plex-sans-kr", "5.3.0", [f"{w}.css" for w in (300, 400, 500, 700)]),
    )
    licence(f"{dl}/gf/noto/OFL.txt", "noto-sans-kr")
    licence(f"{dl}/gf/gothic/OFL.txt", "gothic-a1")
    licence(f"{dl}/gf/plex/OFL.txt", "ibm-plex-sans-kr")

    # --- SUIT: official variable web subset. Both family names resolve to the same file.
    url = place(f"{dl}/suit/SUIT-Variable-woff2/SUIT-Variable.woff2", "suit")
    write_css("suit", "SUIT | SIL OFL 1.1 | official file, unmodified",
              face("SUIT Variable", url, "100 900") + face("SUIT", url, "100 900"))
    licence(f"{dl}/suit/SUIT-Variable-woff2/LICENSE", "suit")

    # --- Wanted Sans: official variable, full Hangul. The axis starts at 400.
    url = place(f"{dl}/wanted/WantedSans/webfonts/variable/complete/woff2/WantedSansVariable.woff2", "wanted-sans")
    write_css("wanted-sans", "Wanted Sans | SIL OFL 1.1 | official file, unmodified",
              face("Wanted Sans Variable", url, "400 1000") + face("Wanted Sans", url, "400 1000"))
    licence(f"{dl}/wanted/WantedSans/OFL.txt", "wanted-sans")

    # --- Spoqa Han Sans Neo: official web subset.
    spoqa = f"{dl}/spoqa/Spoqa_all/SpoqaHanSansNeo_all/SpoqaHanSansNeo_OTF_subset"
    body = "".join(
        face("Spoqa Han Sans Neo", place(f"{spoqa}/SpoqaHanSansNeo-{n}.woff2", "spoqa-han-sans-neo"), WEIGHT_BY_NAME[n])
        for n in ("Thin", "Light", "Regular", "Medium", "Bold")
    )
    write_css("spoqa-han-sans-neo", "Spoqa Han Sans Neo | SIL OFL 1.1 | official file, unmodified", body)
    licence(f"{dl}/spoqa/Spoqa_all/SpoqaHanSansNeo_all/LICENSE", "spoqa-han-sans-neo")

    # --- Paperlogy, Freesentation: nine official statics each.
    for slug, family, pkg in (("paperlogy", "Paperlogy", "paperlogy"), ("freesentation", "Freesentation", "freesentation")):
        body = "".join(
            face(family, place(f"{dl}/{pkg}/woff2/{family}-{w}.woff2", slug), (i + 1) * 100)
            for i, w in enumerate(NINE)
        )
        write_css(slug, f"{family} | SIL OFL 1.1 | official file, unmodified", body)
        licence(f"{dl}/{pkg}/OFL.txt", slug)

    # --- A2Z: official statics. Only the Korean file names change, for clean URLs; the bytes do not.
    body = ""
    for i, w in enumerate(NINE):
        src = [p for p in glob.glob(f"{dl}/a2z/a2z-woff2/*.woff2") if p.endswith(f"-{w}.woff2")][0]
        body += face("A2Z", place(src, "a2z", f"A2Z-{w}.woff2"), (i + 1) * 100)
    write_css("a2z", "A2Z | SIL OFL 1.1 | official file, unmodified", body)
    # Upstream ships no licence file; the OFL statement is embedded in the font itself.
    with open(f"{dl}/paperlogy/OFL.txt", encoding="utf-8") as fh:
        ofl = fh.read().split("\n", 1)[1]
    with open(os.path.join(ROOT, "licenses", "a2z.txt"), "w", encoding="utf-8") as fh:
        fh.write("Copyright © 2026 PT& (https://freesentation.blog/a2z)\n" + ofl)

    # --- LINE Seed Sans KR: official web build, three weights exist for Korean.
    line = glob.glob(f"{dl}/linekr/unz/*/Web/woff2")[0]
    body = "".join(
        face("LINE Seed Sans KR", place(f"{line}/LINESeedKR-{n}.woff2", "line-seed-sans-kr"), w)
        for n, w in (("Th", 100), ("Rg", 400), ("Bd", 700))
    )
    write_css("line-seed-sans-kr", "LINE Seed Sans KR | SIL OFL 1.1 | official file, unmodified", body)
    licence(glob.glob(f"{dl}/line/seed/*/OFL.txt")[0], "line-seed-sans-kr")

    # --- NanumSquare Neo: official web statics.
    nanum = glob.glob(f"{dl}/nanum/NanumSquareNeo/NanumSquareNeo/*/woff2")[0]
    body = "".join(
        face("NanumSquare Neo", place(f"{nanum}/NanumSquareNeoTTF-{n}.woff2", "nanum-square-neo"), w)
        for n, w in (("aLt", 300), ("bRg", 400), ("cBd", 700), ("dEb", 800), ("eHv", 900))
    )
    write_css("nanum-square-neo", "NanumSquare Neo | SIL OFL 1.1 (NAVER) | official file, unmodified", body)
    licence(f"{notices}/naver-licence.txt", "nanum-square-neo")

    # --- S-Core Dream: original OTF only. Its licence forbids conversion, so no woff2.
    body = "".join(
        face("S-Core Dream", place(f"{dl}/score/S-Core_Dream_OTF/SCDream{i}.otf", "s-core-dream"), i * 100, "opentype")
        for i in range(1, 10)
    )
    write_css("s-core-dream", "S-Core Dream | S-Core licence, see licenses/s-core-dream.txt | original OTF, unmodified", body)
    licence(f"{notices}/score-licence.txt", "s-core-dream")

    # --- Checksums of everything served, so any copy can be compared with upstream.
    lines = []
    for path in sorted(glob.glob(os.path.join(ROOT, "fonts", "*", "*"))):
        with open(path, "rb") as fh:
            lines.append(f"{hashlib.sha256(fh.read()).hexdigest()}  {os.path.relpath(path, ROOT)}")
    with open(os.path.join(ROOT, "SHA256SUMS"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dl", required=True)
    ap.add_argument("--notices", required=True)
    args = ap.parse_args()
    build(os.path.abspath(args.dl), os.path.abspath(args.notices))
