from collections import defaultdict
from typing import Dict, Generator, List, Tuple
import solutions.y2021.lib2021

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict

Point = Tuple[int, int]
Line = Tuple[Point, Point]


def input_map(func):
    def inner(input_string):
        return func(map(lambda line: ((line['x0'], line['y0']), (line['x1'], line['y1'])),
                        map(lambda s: get_dict_from_string(r'(\d+),(\d+) -> (\d+),(\d+)', [
                            ('x0', int),
                            ('y0', int),
                            ('x1', int),
                            ('y1', int),
                        ], s), input_string.split('\n'))))

    return inner


@input_map
def p1(input_data) -> str:
    field = defaultdict(lambda: 0)

    for line in input_data:
        if not is_line_diagonal(line):
            for point in get_points_line_crosses(line):
                field[point] += 1

    return get_score_for_field(field)


@ input_map
def p2(input_data) -> str:
    field = defaultdict(lambda: 0)

    for line in input_data:
        for point in get_points_line_crosses(line):
            field[point] += 1

    return get_score_for_field(field)


def get_score_for_field(field):
    return str(len([x for x in field.values() if x >= 2]))


def print_field(field: Dict[Tuple, int]):
    min_x = 0
    min_y = 0
    max_x = max(x[0] for x in field.keys())
    max_y = max(x[1] for x in field.keys())

    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            line += str(field[(x, y)]) if field[(x, y)] != 0 else '.'
        print(line)


def is_line_diagonal(line: Line) -> bool:
    return not (line[0][0] == line[1][0] or line[0][1] == line[1][1])


def get_points_diagonal_line_crosses(line: Line) -> Generator[Point, None, None]:
    diff = abs(line[0][0] - line[1][0]) + 1
    delta_x = 1 if line[0][0] - line[1][0] < 0 else - 1
    delta_y = 1 if line[0][1] - line[1][1] < 0 else - 1
    for delta in range(diff):
        yield (line[0][0] + delta_x * delta, line[0][1] + delta_y * delta)


def get_points_straight_line_crosses(line: Line) -> Generator[Point, None, None]:
    for y in get_range(line[0][1], line[1][1]):
        for x in get_range(line[0][0], line[1][0]):
            yield (x, y)


def get_points_line_crosses(line: Line) -> List[Point]:
    if is_line_diagonal(line):
        return list(get_points_diagonal_line_crosses(line))
    else:
        return list(get_points_straight_line_crosses(line))


def get_range(start, end):
    if start > end:
        return range(start, end - 1, -1)
    else:
        return range(start, end + 1)
