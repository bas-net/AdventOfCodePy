
from typing import Dict
from collections import defaultdict

from solutions.sharedlib import GenericMap2D, Point2D, get_points_in_square, input_map_2d

# default to highest so edges don't have to be treated special :D


@input_map_2d(lambda: defaultdict(lambda: 9), int)
def p1(height_map: GenericMap2D) -> str:
    total_risk_factor = 0
    for point in get_points_in_square(height_map.x_max + 1, height_map.y_max + 1):
        if is_point_low_point(height_map.map, point):
            total_risk_factor += 1 + height_map.map[point]

    return total_risk_factor

# default to highest so edges don't have to be treated special :D


@input_map_2d(lambda: defaultdict(lambda: 9), int)
def p2(height_map: GenericMap2D) -> str:
    low_points = []
    for point in get_points_in_square(height_map.x_max + 1, height_map.y_max + 1):
        if is_point_low_point(height_map.map, point):
            low_points.append(point)

    basin_sizes = []
    for low_point in low_points:
        basin_sizes.append(get_size_of_basin(height_map.map, low_point))

    basin_sizes.sort(reverse=True)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def is_point_low_point(height_map: Dict[Point2D, int], point: Point2D):
    return (height_map[point] < height_map[point.up()]
            and height_map[point] < height_map[point.down()]
            and height_map[point] < height_map[point.left()]
            and height_map[point] < height_map[point.right()])


def get_size_of_basin(height_map: Dict[Point2D, int], low_point: Point2D):
    queue = [low_point]
    handled = set()

    def add_to_queue(p: Point2D):
        if p in handled:
            return
        queue.append(p)

    while len(queue) > 0:
        point = queue.pop(0)
        if height_map[point] != 9:
            handled.add(point)

            add_to_queue(point.up())
            add_to_queue(point.down())
            add_to_queue(point.left())
            add_to_queue(point.right())

    return len(handled)
