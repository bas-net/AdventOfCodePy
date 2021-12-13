
import solutions.y2021.lib2021

from solutions.sharedlib import Point2D, get_points_in_square, get_points_in_square_y_first, input_strings, get_dict_from_string, input_dict


def p1(input_data: str) -> str:
    r = input_data.split('\n\n')

    points = list()
    for line in r[0].split():
        points.append(Point2D(*map(int, line.split(','))))

    max_x = max(p.x for p in points)
    max_y = max(p.y for p in points)

    for foldinstr in r[1].split('\n'):
        # print(f'Fold instr: \'{foldinstr}\'')
        instr_dict = get_dict_from_string(r'fold along (\w)=(\d+)', [
            ('xy', str),
            ('line', int)
        ], foldinstr)

        new_points = set()

        for point in points:
            if instr_dict['xy'] == 'y':
                if point.y > instr_dict['line']:
                    new_points.add(Point2D(point.x, max_y - point.y))
                else:
                    new_points.add(point)
            if instr_dict['xy'] == 'x':
                if point.x > instr_dict['line']:
                    new_points.add(Point2D(max_x - point.x, point.y))
                else:
                    new_points.add(point)

        points = list(new_points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)

        points.sort()
        # print(*points, sep='\n')

        return len(points)


def p2(input_data) -> str:
    r = input_data.split('\n\n')

    points = list()
    for line in r[0].split():
        points.append(Point2D(*map(int, line.split(','))))

    max_x = max(p.x for p in points) + 1
    max_y = max(p.y for p in points) + 1

    for foldinstr in r[1].split('\n'):
        # print(f'Fold instr: \'{foldinstr}\'')
        instr_dict = get_dict_from_string(r'fold along (\w)=(\d+)', [
            ('xy', str),
            ('line', int)
        ], foldinstr)

        new_points = set()

        for point in points:
            if instr_dict['xy'] == 'y':
                if point.y > instr_dict['line']:
                    new_points.add(Point2D(point.x, max_y - point.y - 1))
                else:
                    new_points.add(point)
            if instr_dict['xy'] == 'x':
                if point.x > instr_dict['line']:
                    new_points.add(Point2D(max_x - point.x - 1, point.y))
                else:
                    new_points.add(point)

        if instr_dict['xy'] == 'y':
            max_y = max_y // 2
        if instr_dict['xy'] == 'x':
            max_x = max_x // 2
        # print(f'{max_x} {max_y}')
        points = list(new_points)

        # points.sort()
        # if max_y < 25:
        #     print()

    for y in range(0, max_y):
        for x in range(0, max_x):
            if Point2D(x, y) in points:
                print('#', end='', sep='')
            else:
                print('.', end='')
        print()

    return 'Check the printed answer!'
