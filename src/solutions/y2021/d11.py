
import solutions.y2021.lib2021

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict


def input_square_map_ints(function):
    @input_strings
    def inner(input_lines):
        square_map = {}

        for y, line in enumerate(input_lines):
            for x, char in enumerate(line):
                square_map[(x, y)] = int(char)

        return function(square_map, len(input_lines[0]), len(input_lines))

    return inner


@input_square_map_ints
def p1(input_data, *_) -> str:
    return sum(map(lambda _: step(input_data), range(100)))


@input_square_map_ints
def p2(input_data, *_) -> str:
    i = 1
    while step(input_data) != 100:
        i += 1

    return i


def step(octopus_map):
    flashed = set()

    def increment_point(point):
        if point in flashed:
            return

        octopus_map[point] += 1
        if octopus_map[point] > 9:
            if point in flashed:
                raise Exception()

            flashed.add(point)

            octopus_map[point] = 0

            for adj in get_adjacent(point):
                increment_point(adj)

    for y in range(10):
        for x in range(10):
            increment_point((x, y))

    return len(flashed)


def get_adjacent(point):
    if point[0] > 0:
        yield (point[0]-1, point[1])
    if point[0] < 9:
        yield (point[0]+1, point[1])
    if point[1] > 0:
        yield (point[0], point[1]-1)
    if point[1] < 9:
        yield (point[0], point[1]+1)

    if point[0] > 0 and point[1] > 0:
        yield (point[0] - 1, point[1]-1)
    if point[0] < 9 and point[1] > 0:
        yield (point[0] + 1, point[1]-1)
    if point[0] > 0 and point[1] < 9:
        yield (point[0] - 1, point[1]+1)
    if point[0] < 9 and point[1] < 9:
        yield (point[0] + 1, point[1]+1)


def print_it(p):
    print()
    for y in range(10):
        line = ''
        for x in range(10):
            line += str(p[(x, y)])

        print(line)
