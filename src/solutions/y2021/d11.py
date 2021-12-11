
from solutions.sharedlib import GenericMap2D, Point2D, get_points_in_square, input_map_2d


@input_map_2d(dict, int)
def p1(input_data: GenericMap2D) -> str:
    return sum(map(lambda _: step(input_data), range(100)))


@input_map_2d(dict, int)
def p2(input_data: GenericMap2D) -> str:
    i = 1
    while step(input_data) != 100:
        i += 1

    return i


def step(octopus_map: GenericMap2D):
    flashed = set()

    def increment_point(point: Point2D):
        if point in flashed:
            return

        octopus_map.map[point] += 1
        if octopus_map.map[point] > 9:
            flashed.add(point)

            octopus_map.map[point] = 0

            for adj in get_adjacent(point):
                increment_point(adj)

    for point in get_points_in_square(octopus_map.x_max, octopus_map.y_max):
        increment_point(point)

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
