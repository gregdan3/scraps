import json
import urllib.request

CATEGORIES = ["core", "widespread", "common", "uncommon"]

HEADERS = {  # pretend to be Chrome 121 for Discord links
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3"
}


def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    resp = urllib.request.urlopen(req).read()
    return resp


LANG = "eng"
data = download(f"https://api.linku.la/v1/words?lang={LANG}")
data = json.loads(data)

data = {
    k: v["translations"][LANG]["definitions"]
    for k, v in data.items()
    if v["usage_category"] in CATEGORIES
}

print(json.dumps(data, sort_keys=True))
