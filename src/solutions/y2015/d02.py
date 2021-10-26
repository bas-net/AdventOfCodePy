from typing import List

import solutions.y2015.lib2015


# TODO Make some kind of class with sides and dimensions to represent a cube.

def p1(input_str: str) -> str:
    def get_packaging_for_package(package: str) -> int:
        dimensions = get_dimensions(package)

        sides = [dimensions[0] * dimensions[1],
                 dimensions[1] * dimensions[2],
                 dimensions[2] * dimensions[0]]

        move_smallest_side_to_start(sides)

        # Every side * 2, except the smallest, which has the slack, so * 3.
        return sides[0] * 3 + sides[1] * 2 + sides[2] * 2

    return solutions.y2015.lib2015.process_by_line_aggregate(input_str, get_packaging_for_package, sum)


def p2(input_str: str) -> str:
    def get_ribbon_for_package(package: str) -> int:
        dimensions = get_dimensions(package)

        dimensions.sort()

        # The smallest dimenisions are in 0 and 1, so use those for the perimeter.
        perimeter = dimensions[0] * 2 + dimensions[1] * 2

        ribbon = dimensions[0] * dimensions[1] * dimensions[2]

        return perimeter + ribbon

    return solutions.y2015.lib2015.process_by_line_aggregate(input_str, get_ribbon_for_package, sum)


# TODO Possibly split out into get width height length/xyz
def get_dimensions(package: str) -> List[int]:
    return list(map(int, package.split('x')))


def move_smallest_side_to_start(sides: List[int]) -> None:
    sides.sort()
