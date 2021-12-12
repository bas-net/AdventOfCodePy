import re
from enum import Enum
from typing import Dict
from solutions.sharedlib import Point2D, get_dict_from_string


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    N = 1
    E = 2
    S = 3
    W = 4

    MIN = 1
    MAX = 4


def p1(input_string: str) -> str:
    position: Point2D = Point2D(0, 0)
    d = Direction.NORTH

    for x in map(str.strip, input_string.split(',')):
        instruction = get_dict_from_string(r'(\w)(\d+)', [
            ('direction_to_turn', str),
            ('amount_to_move', int)
        ], x)

        d = {'L': turn_left, 'R': turn_right}[
            instruction['direction_to_turn']](d)

        delta = get_delta_for_direction(d)

        position = Point2D(
            position.x + delta.x * instruction['amount_to_move'],
            position.y + delta.y * instruction['amount_to_move']
        )

    return abs(position.x) + abs(position.y)


def turn_left(facing: Direction) -> Direction:
    return Direction(facing.value - 1 if facing.value > Direction.MIN.value else Direction.MAX.value)


def turn_right(facing: Direction) -> Direction:
    return Direction(facing.value + 1 if facing.value < Direction.MAX.value else Direction.MIN.value)


def get_delta_for_direction(facing: Direction) -> Point2D:
    return {
        Direction.N: Point2D(0, -1),
        Direction.W: Point2D(-1, 0),
        Direction.S: Point2D(0, +1),
        Direction.E: Point2D(+1, 0),
    }[facing]


def p2(input_string: str) -> str:
    position: Point2D = Point2D(0, 0)
    d = Direction.NORTH

    visited = set()
    visited.add(position)

    for x in map(str.strip, input_string.split(',')):
        instruction = get_dict_from_string(r'(\w)(\d+)', [
            ('direction_to_turn', str),
            ('amount_to_move', int)
        ], x)

        d = {'L': turn_left, 'R': turn_right}[
            instruction['direction_to_turn']](d)

        delta = get_delta_for_direction(d)

        for i in range(instruction['amount_to_move']):
            position = Point2D(
                position.x + delta.x,
                position.y + delta.y
            )

            if position in visited:
                return abs(position.x) + abs(position.y)

            visited.add(position)
    return -1
