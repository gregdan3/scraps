#!/usr/bin/env python
import requests

data = requests.get("https://api.linku.la/v1/words").json()

categories = {"core", "common"}
startable = {"a", "k", "w", "n"}
numberable = {"a", "e", "i", "o"}
words = data.keys()

numbermap = {"a": "4", "e": "3", "i": "1", "o": "0"}


def sign(s):
    for i in range(1, 3):
        if s[i] in numbermap:
            return (s[:i] + numbermap[s[i]] + s[i + 1 :]).upper()


for word in words:
    if 4 <= len(word) <= 6 and data[word]["usage_category"] in categories:
        if word[0] in startable:
            if word[1] in numberable or word[2] in numberable:
                print(sign(word))
