from solutions.sharedlib import get_dict_from_string
import solutions.y2021.lib2021


def p1(input_string: str) -> str:
    horizontal_position = 0
    depth = 0
    for line in input_string.split('\n'):
        instr = get_dict_from_string(
            r'(\w+) (\d+)', [('direction', str), ('amount', int)], line)
        if instr['direction'] == 'forward':
            horizontal_position += instr['amount']
        elif instr['direction'] == 'down':
            depth += instr['amount']
        elif instr['direction'] == 'up':
            depth -= instr['amount']
        else:
            raise Exception()

    return horizontal_position * depth


def p2(input_string: str) -> str:
    horizontal_position = 0
    aim = 0
    depth = 0
    for line in input_string.split('\n'):
        instr = get_dict_from_string(
            r'(\w+) (\d+)', [('direction', str), ('amount', int)], line)
        if instr['direction'] == 'forward':
            horizontal_position += instr['amount']
            depth += aim * instr['amount']
        elif instr['direction'] == 'down':
            aim += instr['amount']
        elif instr['direction'] == 'up':
            aim -= instr['amount']
        else:
            raise Exception()

    return horizontal_position * depth
