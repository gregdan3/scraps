import time
from typing import Callable


def determine(s: str) -> bool:
    if len(s) < 5:
        return True
    return False


def for_loop_ver(tokens: list[str]):
    newlist: list[str] = []
    for item in tokens:
        if determine(item):
            newlist.append(item)
    return newlist


def list_comp_ver(tokens: list[str]):
    tokens = [token for token in tokens if determine(token)]
    return tokens


def generator_ver(tokens: list[str]):
    sample_list[:] = (tup for tup in sample_list if determine(tup))
    return sample_list


sample_list = ["bruh", "moment", "bruh", "moment", "holy", "fucking", "shit", "bitches"]


def timer(func: Callable[[list[str]], None]):
    start = time.time()
    for i in range(10000000):
        func(sample_list[:])
    end = time.time()

    return end - start


for func in [for_loop_ver, list_comp_ver, generator_ver]:
    print(timer(func))
