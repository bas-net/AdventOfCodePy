from typing import Dict, List
from solutions.sharedlib import get_dict_from_string, input_dict
import solutions.y2021.lib2021


@input_dict(
    r'(\w+) (\d+)', [
        ('direction', str),
        ('amount', int),
    ]
)
def p1(instrs: List[Dict]) -> str:
    horizontal_position = 0
    depth = 0
    for instr in instrs:
        if instr['direction'] == 'forward':
            horizontal_position += instr['amount']
        elif instr['direction'] == 'down':
            depth += instr['amount']
        elif instr['direction'] == 'up':
            depth -= instr['amount']
        else:
            raise Exception()

    return horizontal_position * depth


@input_dict(
    r'(\w+) (\d+)', [
        ('direction', str),
        ('amount', int),
    ]
)
def p2(instrs: List[Dict]) -> str:
    horizontal_position = 0
    aim = 0
    depth = 0
    for instr in instrs:
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
