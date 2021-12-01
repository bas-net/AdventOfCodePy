import enum
import re
from typing import Any, Callable, Dict, List, Pattern, Tuple, Union
from solutions.y2015.lib2015 import process_by_line
import itertools
from collections import defaultdict
from solutions.sharedlib import get_dict_from_string


def p1(input_string: str) -> str:
    ingredients = [get_ingredient(line) for line in input_string.split('\n')]
    # x,y,z,a

    max_result = None

    for ingredient_counts in [
        list(x)
        for x
        in itertools.product(range(100 + 1), repeat=len(ingredients))
        if sum(x) == 100
    ]:
        result = apply_function(get_total_attributes(
            ingredients, ingredient_counts))
        if max_result:
            max_result = max(result, max_result)
        else:
            max_result = result

    return max_result


def p2(input_string: str) -> str:
    ingredients = [get_ingredient(line) for line in input_string.split('\n')]
    # x,y,z,a

    max_result = None

    for ingredient_counts in [
        list(x)
        for x
        in itertools.product(range(100 + 1), repeat=len(ingredients))
        if sum(x) == 100
    ]:
        total_attributes = get_total_attributes(
            ingredients, ingredient_counts, with_calories=True)

        if total_attributes['calories'] != 500:
            continue

        result = apply_function(get_total_attributes(
            ingredients, ingredient_counts))

        if max_result:
            max_result = max(result, max_result)
        else:
            max_result = result

    return max_result




def get_ingredient(input_string: str) -> Dict:
    return get_dict_from_string(
        r'(\w+): capacity ([\-\d]+), durability ([\-\d]+), flavor ([\-\d]+), texture ([\-\d]+), calories ([\-\d]+)',
        [
            ('name', str),
            ('capacity', int),
            ('durability', int),
            ('flavor', int),
            ('texture', int),
            ('calories', int),
        ], input_string)


def get_total_attributes(ingredients: List[Dict], multipliers: List[int], with_calories: bool = False) -> Dict:
    attribute_results = defaultdict(lambda: 0)
    for ingredient, multiplier in zip(ingredients, multipliers):
        attribute_results['capacity'] += ingredient['capacity'] * multiplier
        attribute_results['durability'] += ingredient['durability'] * multiplier
        attribute_results['flavor'] += ingredient['flavor'] * multiplier
        attribute_results['texture'] += ingredient['texture'] * multiplier
        if with_calories:
            attribute_results['calories'] += ingredient['calories'] * multiplier

    return dict(attribute_results)


def apply_function(attribute_results: Dict) -> int:
    result = 1
    for v in attribute_results.values():
        result *= max(v, 0)

    return result
