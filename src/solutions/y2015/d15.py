import enum
import re
from typing import Dict, List
from solutions.y2015.lib2015 import process_by_line
import itertools
from collections import defaultdict


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
    m = re.search(
        r'(?P<name>\w+): capacity (?P<capacity>[\-\d]+), durability (?P<durability>[\-\d]+), flavor (?P<flavor>[\-\d]+), texture (?P<texture>[\-\d]+), calories (?P<calories>[\-\d]+)', input_string)
    g = m.groupdict()
    return {
        'name': g['name'],
        'capacity': int(g['capacity']),
        'durability': int(g['durability']),
        'flavor': int(g['flavor']),
        'texture': int(g['texture']),
        'calories': int(g['calories']),
    }


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
