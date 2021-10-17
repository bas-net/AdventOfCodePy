import re

import solutions.y2015.lib2015


def p1(input_string: str) -> str:
    light_array = [[0 for _ in range(1000)] for _ in range(1000)]

    def func(instruction: str) -> None:
        (instr, x1, y1, x2, y2) = re.findall(
            r'([\w\s]+)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)', instruction)[0]
        xs = [int(x1), int(x2)]
        ys = [int(y1), int(y2)]
        xs.sort()
        ys.sort()
        if instr == 'turn on':
            for x in range(xs[0], xs[1] + 1):
                for y in range(ys[0], ys[1] + 1):
                    light_array[y][x] = 1
        elif instr == 'toggle':
            for x in range(xs[0], xs[1] + 1):
                for y in range(ys[0], ys[1] + 1):
                    light_array[y][x] = 1 if light_array[y][x] == 0 else 0
        elif instr == 'turn off':
            for x in range(xs[0], xs[1] + 1):
                for y in range(ys[0], ys[1] + 1):
                    light_array[y][x] = 0

    solutions.y2015.lib2015.process_by_line(input_string, func)

    return sum([sum(x) for x in light_array])


def p2(input_string: str) -> str:
    pass
