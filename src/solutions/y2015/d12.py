import solutions.y2015.lib2015

import re
import json


def p1(input_string: str) -> str:
    return sum([int(x) for x in re.findall(r'(\-?\d+)', input_string)])


def p2(input_string: str) -> str:
    return get_sum(json.loads(input_string))


def get_sum(json):
    total = 0
    if type(json) is list:
        for x in json:
            if type(x) is int:
                total += x
            elif type(x) is dict or type(x) is list:
                total += get_sum(x)
    if isinstance(json, dict):
        for key in json:
            if json[key] == 'red':
                return 0
            elif isinstance(json[key], int):
                total += json[key]
            elif isinstance(json[key], list) or isinstance(json[key], dict):
                total += get_sum(json[key])

    return total
