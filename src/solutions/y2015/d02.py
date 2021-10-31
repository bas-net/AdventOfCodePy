from typing import List
from dataclasses import dataclass
from math import prod

from solutions.y2015.lib2015 import process_by_line_aggregate


@dataclass
class Dimensions2:
    length: int
    width: int

    def get_surface_area(self):
        return self.length * self.width


@dataclass
class Dimensions3:
    length: int
    width: int
    height: int

    count: int = 3

    def __init__(self, length: int, width: int, height: int) -> None:
        self.length = length
        self.width = width
        self.height = height

    def __getitem__(self, key: int) -> int:
        if key == 0:
            return self.length
        if key == 1:
            return self.height
        if key == 2:
            return self.width
        raise IndexError(
            f'Index \'{key}\' is out of range. 0,1,2 are allowed.')

    def get_sides(self) -> List[Dimensions2]:
        return [Dimensions2(self[i % 3], self[(i + 1) % 3]) for i in range(self.count * 2)]

    def get_surface_area(self):
        return sum([side.get_surface_area() for side in self.get_sides()])

    def get_smallest_side_area(self):
        return min([side.get_surface_area() for side in self.get_sides()])

    def as_list(self) -> List[int]:
        return [self[i] for i in range(self.count)]

    def get_smallest_two(self):
        l = self.as_list()
        l.sort()
        return l[:2]


def p1(input_str: str) -> str:
    def get_packaging_for_package(package: str) -> int:
        dimensions = get_dimensions(package)
        return dimensions.get_surface_area() + dimensions.get_smallest_side_area()

    return process_by_line_aggregate(input_str, get_packaging_for_package, sum)


def p2(input_str: str) -> str:
    def get_ribbon_for_package(package: str) -> int:
        dimensions = get_dimensions(package)

        perimeter = sum([dim * 2 for dim in dimensions.get_smallest_two()])

        ribbon = prod(dimensions.as_list())

        return perimeter + ribbon

    return process_by_line_aggregate(input_str, get_ribbon_for_package, sum)



def get_dimensions(package: str) -> Dimensions3:
    return Dimensions3(*list(map(int, package.split('x'))))


def move_smallest_side_to_start(sides: List[int]) -> None:
    sides.sort()
