"""
Expects a curdir full of svg files named "uFnnnn.*.svg"
Renames the files after their corresponding word
Used to fill ijo Linku with ssk's glyphs before replacing this with fontforge approach
"""

import os

UCSUR_MAP = {
    "󱤀": "a",
    "󱤁": "akesi",
    "󱤂": "ala",
    "󱤃": "alasa",
    "󱤄": "ale",
    "󱤅": "anpa",
    "󱤆": "ante",
    "󱤇": "anu",
    "󱤈": "awen",
    "󱤉": "e",
    "󱤊": "en",
    "󱤋": "esun",
    "󱤌": "ijo",
    "󱤍": "ike",
    "󱤎": "ilo",
    "󱤏": "insa",
    "󱤐": "jaki",
    "󱤑": "jan",
    "󱤒": "jelo",
    "󱤓": "jo",
    "󱤔": "kala",
    "󱤕": "kalama",
    "󱤖": "kama",
    "󱤗": "kasi",
    "󱤘": "ken",
    "󱤙": "kepeken",
    "󱤚": "kili",
    "󱤛": "kiwen",
    "󱤜": "ko",
    "󱤝": "kon",
    "󱤞": "kule",
    "󱤟": "kulupu",
    "󱤠": "kute",
    "󱤡": "la",
    "󱤢": "lape",
    "󱤣": "laso",
    "󱤤": "lawa",
    "󱤥": "len",
    "󱤦": "lete",
    "󱤧": "li",
    "󱤨": "lili",
    "󱤩": "linja",
    "󱤪": "lipu",
    "󱤫": "loje",
    "󱤬": "lon",
    "󱤭": "luka",
    "󱤮": "lukin",
    "󱤯": "lupa",
    "󱤰": "ma",
    "󱤱": "mama",
    "󱤲": "mani",
    "󱤳": "meli",
    "󱤴": "mi",
    "󱤵": "mije",
    "󱤶": "moku",
    "󱤷": "moli",
    "󱤸": "monsi",
    "󱤹": "mu",
    "󱤺": "mun",
    "󱤻": "musi",
    "󱤼": "mute",
    "󱤽": "nanpa",
    "󱤾": "nasa",
    "󱤿": "nasin",
    "󱥀": "nena",
    "󱥁": "ni",
    "󱥂": "nimi",
    "󱥃": "noka",
    "󱥄": "o",
    "󱥅": "olin",
    "󱥆": "ona",
    "󱥇": "open",
    "󱥈": "pakala",
    "󱥉": "pali",
    "󱥊": "palisa",
    "󱥋": "pan",
    "󱥌": "pana",
    "󱥍": "pi",
    "󱥎": "pilin",
    "󱥏": "pimeja",
    "󱥐": "pini",
    "󱥑": "pipi",
    "󱥒": "poka",
    "󱥓": "poki",
    "󱥔": "pona",
    "󱥕": "pu",
    "󱥖": "sama",
    "󱥗": "seli",
    "󱥘": "selo",
    "󱥙": "seme",
    "󱥚": "sewi",
    "󱥛": "sijelo",
    "󱥜": "sike",
    "󱥝": "sin",
    "󱥞": "sina",
    "󱥟": "sinpin",
    "󱥠": "sitelen",
    "󱥡": "sona",
    "󱥢": "soweli",
    "󱥣": "suli",
    "󱥤": "suno",
    "󱥥": "supa",
    "󱥦": "suwi",
    "󱥧": "tan",
    "󱥨": "taso",
    "󱥩": "tawa",
    "󱥪": "telo",
    "󱥫": "tenpo",
    "󱥬": "toki",
    "󱥭": "tomo",
    "󱥮": "tu",
    "󱥯": "unpa",
    "󱥰": "uta",
    "󱥱": "utala",
    "󱥲": "walo",
    "󱥳": "wan",
    "󱥴": "waso",
    "󱥵": "wawa",
    "󱥶": "weka",
    "󱥷": "wile",
    "󱥸": "namako",
    "󱥹": "kin",
    "󱥺": "oko",
    "󱥻": "kipisi",
    "󱥼": "leko",
    "󱥽": "monsuta",
    "󱥾": "tonsi",
    "󱥿": "jasima",
    "󱦀": "kijetesantakalu",
    "󱦁": "soko",
    "󱦂": "meso",
    "󱦃": "epiku",
    "󱦄": "kokosila",
    "󱦅": "lanpan",
    "󱦆": "n",
    "󱦇": "misikeke",
    "󱦈": "ku",
    "󱦠": "pake",
    "󱦡": "apeja",
    "󱦢": "majuna",
    "󱦣": "powe",
}

ADAPTED_MAP = {ord(k): v for k, v in UCSUR_MAP.items()}


def create_new_name(word: str, dup_num: int = 0):
    dup = ""
    if dup_num > 0:
        dup = str(dup_num)

    return word + dup + ".svg"


def adapt_codepoint_name(fname: str):
    codepoint = fname.split("_")[0]
    assert codepoint.startswith("uF")
    codepoint = codepoint.replace("uF", "U+F")
    return codepoint


def get_codepoint_int(fname: str):
    assert fname.startswith("uF"), fname
    assert fname.endswith(".svg"), fname
    codepoint = fname[1:6]
    return int(codepoint, 16)


def main():
    svgs = [f for f in os.listdir(".") if f.startswith(r"uF") and f.endswith(r".svg")]
    for svg in svgs:
        codepoint = get_codepoint_int(svg)
        word = ADAPTED_MAP[codepoint]
        new_name = create_new_name(word)
        os.rename(svg, new_name)


if __name__ == "__main__":
    main()
