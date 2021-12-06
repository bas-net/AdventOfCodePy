
import solutions.y2021.lib2021

from solutions.sharedlib import input_ints_csv, input_strings, get_dict_from_string, input_dict

from collections import defaultdict


@input_ints_csv
def p1(input_data) -> str:
    fishies = defaultdict(lambda: 0)
    for i in input_data:
        fishies[i] += 1

    for i in range(80):
        # print(fishies, sum(fishies.values()))
        f2 = defaultdict(lambda: 0)
        for j in range(1, 8 + 1):
            f2[j-1] = fishies[j]
        f2[6] += fishies[0]
        f2[8] += fishies[0]
        fishies = f2

    return sum(fishies.values())


@input_ints_csv
def p2(input_data) -> str:
    fishies = defaultdict(lambda: 0)
    for i in input_data:
        fishies[i] += 1

    for i in range(256):
        # print(fishies, sum(fishies.values()))
        f2 = defaultdict(lambda: 0)
        for j in range(1, 8 + 1):
            f2[j-1] = fishies[j]
        f2[6] += fishies[0]
        f2[8] += fishies[0]
        fishies = f2

    return sum(fishies.values())
