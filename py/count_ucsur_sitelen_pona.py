"""
Expects a curdir full of json files exported by the discord chat exporter tool
"""

import json
from collections import Counter
from os import listdir
from typing import Callable, List

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

KNOWN_BOTS = [
    "466378653216014359",  # pk
    "204255221017214977",  # yag
    "946665197362360321",
]

COMMANDS = ["pk;", "pk!"]
EXACTS = ["Pinned a message.", "Joined the server."]


def get_dir_json(dir: str):
    return [f for f in listdir(dir) if f.endswith(".json")]


def load_channel(fname: str):
    with open(fname, "r") as f:
        contents = f.read()
    loaded = json.loads(contents)
    return loaded


def yield_msg_contents_from_channel(
    channel: dict, filters: List[Callable] = [lambda x: True]
):
    for message in channel["messages"]:
        if all([filter(message) for filter in filters]):
            yield message["content"]


def remove_exacts(message: dict):
    return message["content"] not in EXACTS


def remove_empty(message: dict):
    return len(message["content"]) > 0


def remove_known_bots(message: dict):
    return message["author"]["id"] not in KNOWN_BOTS


def remove_known_commands(message: dict):
    starts = ["pk;", "pk!"]
    return not any([message["content"].startswith(start) for start in starts])


def filter_ascii(msg: str):
    filtered = ""
    for c in msg:
        if ord(c) > 256:
            filtered += c
    return filtered


def filter_emoji(msg: str):
    filtered = ""

    range_min = ord("\U0001F300")  # 127744
    range_max = ord("\U0001FAF6")  # 129782
    range_min_2 = 126980
    range_max_2 = 127569
    range_min_3 = 169
    range_max_3 = 174
    range_min_4 = 8205
    range_max_4 = 12953
    for c in msg:
        char_code = ord(c)
        if range_min <= char_code <= range_max:
            continue
        elif range_min_2 <= char_code <= range_max_2:
            continue
        elif range_min_3 <= char_code <= range_max_3:
            continue
        elif range_min_4 <= char_code <= range_max_4:
            continue
        filtered += c
    return filtered


def main():
    character_counter = Counter()

    channels = get_dir_json(".")
    for channel in channels:
        json_channel = load_channel(channel)
        for message in yield_msg_contents_from_channel(
            json_channel,
            [remove_exacts, remove_empty, remove_known_bots, remove_known_commands],
        ):
            message = filter_ascii(message)
            message = filter_emoji(message)
            character_counter.update(message)

    cleaned = dict()
    for k, v in character_counter.items():
        if k in UCSUR_MAP:
            cleaned[UCSUR_MAP[k]] = v
    for k, v in UCSUR_MAP.items():
        if v not in cleaned:
            cleaned[v] = 0
    cleaned = {
        k: v for k, v in sorted(cleaned.items(), key=lambda x: x[1], reverse=True)
    }
    print(json.dumps(cleaned))


if __name__ == "__main__":
    main()
