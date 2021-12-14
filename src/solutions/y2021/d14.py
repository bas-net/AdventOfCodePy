
from collections import defaultdict
from typing import DefaultDict
import solutions.y2021.lib2021

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict


def p1(input_data) -> str:
    r = input_data.split('\n\n')

    polymer = r[0]

    rules = {}
    for rule_line in r[1].split('\n'):
        rule = get_dict_from_string(r'(\w+) -> (\w)', [
            ('pair', str),
            ('element', str)
        ], rule_line)
        rules[rule['pair']] = rule['element']

    for i in range(10):
        new_polymer = polymer[0]
        for pair in map(lambda j: polymer[j:j+2], range(len(polymer)-1)):
            # print(pair)
            if pair in rules:
                new_polymer += rules[pair] + pair[1]
            else:
                new_polymer += pair

        polymer = new_polymer

    # print(polymer)

    counts = defaultdict(lambda: 0)
    for c in polymer:
        counts[c] += 1
    # print(counts)
    counts = list(counts.values())
    counts.sort(reverse=True)

    return counts[0] - counts[-1]


def p2(input_data) -> str:
    r = input_data.split('\n\n')

    polymer = r[0]

    rules = {}
    for rule_line in r[1].split('\n'):
        rule = get_dict_from_string(r'(\w+) -> (\w)', [
            ('pair', str),
            ('element', str)
        ], rule_line)
        rules[rule['pair']] = rule['element']

    buckets = defaultdict(lambda: 0)
    for pair in map(lambda j: polymer[j:j+2], range(len(polymer)-1)):
        buckets[pair] += 1

    print(buckets)
    for i in range(40):
        new_buckets = defaultdict(lambda: 0)
        for pair in buckets:
            if pair in rules:
                new_buckets[pair[0] + rules[pair]] += buckets[pair]
                new_buckets[rules[pair] + pair[1]] += buckets[pair]
            else:
                new_buckets[pair] = buckets[pair]
        buckets = new_buckets


        # print(buckets)

    print(len(buckets))
    counts = defaultdict(lambda: 0)
    for pair in buckets:
        counts[pair[0]] += buckets[pair]
    counts[polymer[-1]] += 1

    print(counts)
    counts = list(counts.values())
    counts.sort()
    print(counts[-1] - counts[0])

    # exit()
    return counts[-1] - counts[0]
