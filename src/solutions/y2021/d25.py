
import solutions.y2021.lib2021

from solutions.sharedlib import GenericMap2D, Point2D, input_map_2d, input_strings, get_dict_from_string, input_dict
from collections import defaultdict

EMPTY_SPACE = '.'
SOUTH_MOVING = 'v'
EAST_MOVING = '>'


@input_map_2d(lambda: defaultdict(lambda: EMPTY_SPACE), str)
def p1(gmap: GenericMap2D) -> str:
    step = 0
    moved = True
    the_map = gmap.map

    # print_map(the_map)

    while moved :
        new_map = defaultdict(lambda: EMPTY_SPACE)
        moved = False
        for y in range(gmap.y_max + 1):
            for x in range(gmap.x_max + 1):
                p = Point2D(x, y)

                if the_map[p] == EAST_MOVING:
                    if the_map[p.east(loopback_at=gmap.x_max)] == EMPTY_SPACE:
                        new_map[
                            p.east(loopback_at=gmap.x_max)
                        ] = EAST_MOVING
                        moved = True
                    else:
                        new_map[p] = EAST_MOVING
        for y in range(gmap.y_max + 1):
            for x in range(gmap.x_max + 1):
                p = Point2D(x, y)

                if the_map[p] == SOUTH_MOVING:
                    if new_map[p.south(loopback_at=gmap.y_max)] == EMPTY_SPACE and (
                        the_map[p.south(loopback_at=gmap.y_max)] == EMPTY_SPACE or
                        the_map[p.south(loopback_at=gmap.y_max)
                                ] == EAST_MOVING
                    ):
                        new_map[
                            p.south(loopback_at=gmap.y_max)
                        ] = SOUTH_MOVING
                        moved = True
                    else:
                        new_map[p] = SOUTH_MOVING

        the_map = new_map
        step += 1
        print(step)
        # print_map(the_map)

    # expected = [
    #     '....>.>v.>',
    #     'v.v>.>v.v.',
    #     '>v>>..>v..',
    #     '>>v>v>.>.v',
    #     '.>v.v...v.',
    #     'v>>.>vvv..',
    #     '..v...>>..',
    #     'vv...>>vv.',
    #     '>.v.v..v.v',
    # ]

    # min_x = 0
    # max_x = 0
    # min_y = 0
    # max_y = 0
    # for point in the_map.keys():
    #     min_x = min(min_x, point.x)
    #     min_y = min(min_y, point.y)
    #     max_x = max(max_x, point.x)
    #     max_y = max(max_y, point.y)
    # print(max_x, gmap.x_max,  max_y, gmap.y_max)
    # print()
    # for y in range(min_y, max_y + 1):
    #     for x in range(min_x, max_x + 1):
    #         if expected[y][x] == the_map[Point2D(x, y)]:
    #             print('.', end='')
    #         else:
    #             print('!', end='')
    #     print()

    # exit()
    return step


def p2(input_data) -> str:
    pass


def print_map(map_dict):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for point in map_dict.keys():
        min_x = min(min_x, point.x)
        min_y = min(min_y, point.y)
        max_x = max(max_x, point.x)
        max_y = max(max_y, point.y)
    print()
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(map_dict[Point2D(x, y)], end='')
        print()
    print()
