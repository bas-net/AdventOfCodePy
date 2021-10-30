import re
import json


def p1(input_string: str) -> str:
    return sum([int(x) for x in re.findall(r'(\-?\d+)', input_string)])


def p2(input_string: str) -> str:
    return get_sum(json.loads(input_string))


def get_sum(json_dict):
    total = 0
    if isinstance(json_dict, list):
        for x in json_dict:
            if isinstance(x, int):
                total += x
            elif isinstance(x, (dict, list)):
                total += get_sum(x)
    elif isinstance(json_dict, dict):
        for key in json_dict:
            if json_dict[key] == 'red':
                return 0

            if isinstance(json_dict[key], int):
                total += json_dict[key]
            elif isinstance(json_dict[key], (list, dict)):
                total += get_sum(json_dict[key])

    return total
