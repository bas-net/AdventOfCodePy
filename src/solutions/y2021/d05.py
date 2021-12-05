from collections import defaultdict
from typing import Dict, Generator, List, Tuple
import solutions.y2021.lib2021

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict

Point = Tuple[int, int]
Line = Tuple[Point, Point]


@input_dict(r'(\d+),(\d+) -> (\d+),(\d+)', [
    ('x0', int),
    ('y0', int),
    ('x1', int),
    ('y1', int),
])
def p1(input_data) -> str:
    field = defaultdict(lambda: 0)
    for line in input_data:
        # print(line)
        x0, y0, x1, y1 = (line['x0'], line['y0'], line['x1'], line['y1'])
        # print(is_horizontal_line(x0, y0, x1, y1))
        if is_horizontal_line(x0, y0, x1, y1):
            min_x = min(x0, x1)
            max_x = max(x0, x1)
            min_y = min(y0, y1)
            may_y = max(y0, y1)
            for x in range(min_x, max_x + 1):
                for y in range(min_y, may_y + 1):
                    field[(x, y)] += 1
                    # print(f'Marking {x},{y}')
    # print_field(field)
    # exit()
    return str(len([x for x in field.values() if x >= 2]))


@input_dict(r'(\d+),(\d+) -> (\d+),(\d+)', [
    ('x0', int),
    ('y0', int),
    ('x1', int),
    ('y1', int),
])
def p2(input_data) -> str:
    field = defaultdict(lambda: 0)

    # print(get_points_line_crosses(((1, 1), (3, 1))))

    for line in input_data:
        x0, y0, x1, y1 = (line['x0'], line['y0'], line['x1'], line['y1'])
        # 6,4 -> 2,0

        for point in get_points_line_crosses(((x0, y0), (x1, y1))):
            field[point] += 1

    # print_field(field)
    # exit()
    return str(len([x for x in field.values() if x >= 2]))


def is_horizontal_line(x0, y0, x1, y1):
    return x0 == x1 or y0 == y1


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
