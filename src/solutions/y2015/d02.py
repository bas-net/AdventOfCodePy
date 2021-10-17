from typing import List
import solutions.y2015.lib2015


def get_dimensions(package: str) -> List[int]:
    return list(map(int, package.split('x')))


def move_smallest_side_to_start(sides: List[int]) -> None:
    sides.sort()


def p1(input: str) -> str:
    def func(package: str) -> int:
        dimensions = get_dimensions(package)

        sides = [dimensions[0] * dimensions[1],
                 dimensions[1] * dimensions[2],
                 dimensions[2] * dimensions[0]]

        move_smallest_side_to_start(sides)

        # Every side * 2, except the smallest, which has the slack, so * 3.
        return sides[0] * 3 + sides[1] * 2 + sides[2] * 2

    return solutions.y2015.lib2015.process_by_line_aggregate(input, func, sum)


def p2(input: str) -> str:
    def func(package: str) -> int:
        dimensions = get_dimensions(package)

        dimensions.sort()

        # The smallest dimenisions are in 0 and 1, so use those for the perimeter.
        perimeter = dimensions[0] * 2 + dimensions[1] * 2

        ribbon = dimensions[0] * dimensions[1] * dimensions[2]

        return perimeter + ribbon

    return solutions.y2015.lib2015.process_by_line_aggregate(input, func, sum)
