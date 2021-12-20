
import solutions.y2021.lib2021

from solutions.sharedlib import Point2D, get_points_in_square, get_points_in_square_y_first, input_strings, get_dict_from_string, input_dict
from collections import defaultdict


def p1(input_data) -> str:
    # print('#..#.#######.##...##.##.#.#..#..#.....####...####.##.###...##.####......##.###.##...#..##..#.######...###..########.#.##.#.#..#..##.##..####.###.###..#...##.##.###.....###..###....#.####.#..##....#.##...##.#..#.....###.#..#.....##..##.#.#.....#....####.#.#.#....#.#...#.##...#.#.#....#.#.#....##.#.####.##..#####.####.#.####..#...###.###..##...#..###.####...#..#.####.###.##..##....#.####....#.#..##.#..#.##.##..#......###.#...#..#.#.#.##.######.##.##..####.##..#.###.##.....##...#.....#..#....###..####.#.##..#.'[319])
    # exit()
    r = input_data.split('\n\n')

    map_dict = defaultdict(lambda: 0)
    for y, line in enumerate(r[1].split('\n')):
        for x, char in enumerate(line):
            map_dict[Point2D(x, y)] = 1 if char == '#' else 0

    # print(*map_dict.keys(), sep='\n')
    # print_map(map_dict)
    for i in range(2):
        # new_map_dict = defaultdict(lambda: 0)
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0

        for point in map_dict.keys():
            min_x = min(min_x, point.x)
            min_y = min(min_y, point.y)
            max_x = max(max_x, point.x)
            max_y = max(max_y, point.y)

        min_x -= 1
        min_y -= 1
        max_x += 1
        max_y += 1

        new_map_dict = defaultdict(lambda: 1) if map_dict[Point2D(-1000,-1000)] == 0 and r[0][0] == '#' else defaultdict(lambda: 0)
        # print(new_map_dict)

        # print(f'{min_x}->{max_x}, {min_y}->{max_y}')
        # exit()
        c = 0
        for pixel_point in get_points_in_square(max_x + 1, max_y + 1, min_x, min_y):
            binary = ''
            
            for point in get_points_in_square_y_first(
                    pixel_point.x + 1 + 1,
                    pixel_point.y + 1 + 1,
                    pixel_point.x - 1,
                    pixel_point.y - 1):
                binary += str(map_dict[point])
            new_map_dict[pixel_point] = 1 if r[0][int(binary, 2)] == '#' else 0
            # print(f'pixel_point {pixel_point} gets {binary} which is {int(binary, 2)} and becomes {r[0][int(binary, 2)]}')
            
            # if max_y > 50 and c > 10:
            #     exit()
            c += 1
        map_dict = new_map_dict
        # print_map(map_dict)
    
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    for point in map_dict.keys():
        min_x = min(min_x, point.x)
        min_y = min(min_y, point.y)
        max_x = max(max_x, point.x)
        max_y = max(max_y, point.y)

    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1
    # print(f'{min_x}->{max_x}, {min_y}->{max_y}')

    # < 5698
    return str(len([v for v in map_dict.values() if v == 1]))


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
            print('#' if map_dict[Point2D(x, y)] == 1 else '.', end='')
        print()
    print()



def p2(input_data) -> str:
    # print('#..#.#######.##...##.##.#.#..#..#.....####...####.##.###...##.####......##.###.##...#..##..#.######...###..########.#.##.#.#..#..##.##..####.###.###..#...##.##.###.....###..###....#.####.#..##....#.##...##.#..#.....###.#..#.....##..##.#.#.....#....####.#.#.#....#.#...#.##...#.#.#....#.#.#....##.#.####.##..#####.####.#.####..#...###.###..##...#..###.####...#..#.####.###.##..##....#.####....#.#..##.#..#.##.##..#......###.#...#..#.#.#.##.######.##.##..####.##..#.###.##.....##...#.....#..#....###..####.#.##..#.'[319])
    # exit()
    r = input_data.split('\n\n')

    map_dict = defaultdict(lambda: 0)
    for y, line in enumerate(r[1].split('\n')):
        for x, char in enumerate(line):
            map_dict[Point2D(x, y)] = 1 if char == '#' else 0

    # print(*map_dict.keys(), sep='\n')
    # print_map(map_dict)
    for i in range(50):
        # new_map_dict = defaultdict(lambda: 0)
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0

        for point in map_dict.keys():
            min_x = min(min_x, point.x)
            min_y = min(min_y, point.y)
            max_x = max(max_x, point.x)
            max_y = max(max_y, point.y)

        min_x -= 1
        min_y -= 1
        max_x += 1
        max_y += 1

        new_map_dict = defaultdict(lambda: 1) if map_dict[Point2D(-1000,-1000)] == 0 and r[0][0] == '#' else defaultdict(lambda: 0)
        # print(new_map_dict)

        # print(f'{min_x}->{max_x}, {min_y}->{max_y}')
        # exit()
        c = 0
        for pixel_point in get_points_in_square(max_x + 1, max_y + 1, min_x, min_y):
            binary = ''
            
            for point in get_points_in_square_y_first(
                    pixel_point.x + 1 + 1,
                    pixel_point.y + 1 + 1,
                    pixel_point.x - 1,
                    pixel_point.y - 1):
                binary += str(map_dict[point])
            new_map_dict[pixel_point] = 1 if r[0][int(binary, 2)] == '#' else 0
            # print(f'pixel_point {pixel_point} gets {binary} which is {int(binary, 2)} and becomes {r[0][int(binary, 2)]}')
            
            # if max_y > 50 and c > 10:
            #     exit()
            c += 1
        map_dict = new_map_dict
        # print_map(map_dict)
    
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    for point in map_dict.keys():
        min_x = min(min_x, point.x)
        min_y = min(min_y, point.y)
        max_x = max(max_x, point.x)
        max_y = max(max_y, point.y)

    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1
    # print(f'{min_x}->{max_x}, {min_y}->{max_y}')

    # < 5698
    return str(len([v for v in map_dict.values() if v == 1]))
