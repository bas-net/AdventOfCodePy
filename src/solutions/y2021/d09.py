
from typing import DefaultDict, Dict, Tuple
import solutions.y2021.lib2021

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict
from collections import defaultdict

Point = Tuple[int, int]


@input_strings
def p1(input_data) -> str:
    # default to highest so edges don't have to be treated special :D
    height_map: Dict[Point, int] = defaultdict(lambda: 9)
    max_y = 0
    max_x = 0
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            height_map[(x, y)] = int(char)
            max_x = max(x, max_x)
        max_y = max(y, max_y)

    total_risk_factor = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if is_point_low_point(height_map, (x, y)):
                total_risk_factor += 1 + height_map[(x, y)]

    return total_risk_factor

@input_strings
def p2(input_data) -> str:
    # default to highest so edges don't have to be treated special :D
    height_map: Dict[Point, int] = defaultdict(lambda: 9)
    max_y = 0
    max_x = 0
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            height_map[(x, y)] = int(char)
            max_x = max(x, max_x)
        max_y = max(y, max_y)

    low_points = []
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if is_point_low_point(height_map, (x, y)):
                low_points.append((x, y))

    basin_sizes = []
    for low_point in low_points:
        basin_sizes.append(get_size_of_basin(height_map, low_point))

    basin_sizes.sort(reverse=True)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def is_point_low_point(height_map, point):
    if (1 == 1
                and height_map[point] < height_map[(point[0] - 1, point[1])]
                and height_map[point] < height_map[(point[0] + 1, point[1])]
                and height_map[point] < height_map[(point[0], point[1] - 1)]
                and height_map[point] < height_map[(point[0], point[1] + 1)]
            ):
        return True
    return False


def get_size_of_basin(height_map, low_point):
    queue = [low_point]
    handled = set()

    def add_to_queue(p):
        if p in handled:
            return
        queue.append(p)

    while len(queue) > 0:
        point = queue.pop(0)
        if height_map[point] != 9:
            handled.add(point)

            add_to_queue((point[0] - 1, point[1]))
            add_to_queue((point[0] + 1, point[1]))
            add_to_queue((point[0], point[1] - 1))
            add_to_queue((point[0], point[1] + 1))

    return len(handled)
