from collections import defaultdict
from typing import Dict, List
from dataclasses import dataclass


def p1(input_string: str) -> str:
    return do_stuff(input_string, 1)


def p2(input_string: str) -> str:
    return do_stuff(input_string, 2)


def do_stuff(instructions: str, number_of_walkers: int) -> int:
    visited_count = init_visited_count_store()

    coords = init_point_list(number_of_walkers)

    set_all_points_to_visited(visited_count, coords)

    for index, instr in enumerate(instructions):
        coord_under_edit = index % number_of_walkers

        coords[coord_under_edit] = determine_instruction_result(
            coords[coord_under_edit],
            instr)
        
        visited_count[coords[coord_under_edit]] += 1

    return len(visited_count)


@dataclass(unsafe_hash=True, frozen=True)
class Point:
    x: int = 0
    y: int = 0


def determine_instruction_result(coords: Point, character) -> Point:
    (x, y) = (coords.x, coords.y)

    if character == '^':
        y += 1
    elif character == 'v':
        y -= 1
    elif character == '<':
        x -= 1
    elif character == '>':
        x += 1
    else:
        raise Exception('Invalid character')

    return Point(x, y)


def init_visited_count_store() -> Dict[Point, int]:
    return defaultdict(lambda: 0)


def init_point_list(number: int) -> List[Point]:
    return [Point() for _ in range(number)]


def set_all_points_to_visited(visited_count: Dict[Point, int], coords: List[Point]):
    for coord in coords:
        visited_count[coord] += 1
