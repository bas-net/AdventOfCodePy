import re
from typing import Callable, Dict, List

from solutions.sharedlib import input_strings

BOARD_WIDTH = 5
BOARD_HEIGHT = 5


@input_strings
def p1(lines) -> str:
    return run_bingo(
        lines,
        lambda board, called_numbers, number, _: (True, get_score(board, called_numbers, number)))


@input_strings
def p2(lines: List[str]) -> str:
    def handler(board, called_numbers, number, boards: List[Dict]):
        if len(boards) == 1:
            return (True, get_score(board, called_numbers, number))
        boards.remove(board)
        return (False, 0)

    return run_bingo(lines, handler)


def get_callable_numbers(number_line):
    return map(int, number_line.split(','))


def run_bingo(lines, on_board_completion: Callable):
    number_line, board_lines = split_boards_and_numbers_lines(lines)

    numbers_to_call = get_callable_numbers(number_line)
    boards = get_boards(board_lines)

    pulled_numbers = set()
    for number in numbers_to_call:
        pulled_numbers.add(number)
        for board in boards:
            if check_if_board_won(board, pulled_numbers):
                should_stop, return_value = on_board_completion(
                    board, pulled_numbers, number, boards)
                if should_stop:
                    return return_value


def split_boards_and_numbers_lines(lines):
    return (lines[0], lines[2:])


def get_score(board, numbers, last_called):
    unmarked_sum = 0
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[(x, y)] not in numbers:
                unmarked_sum += board[(x, y)]
    return unmarked_sum * last_called


def get_boards(lines):
    boards = []
    while len(lines) > 0:
        boards.append(get_board(lines[:5]))
        lines = lines[6:]
    return boards


def get_board(lines):
    board = {}
    for y, line in enumerate(lines):
        # print(line)
        for x, number in enumerate(re.split(' +', line.strip())):
            # print(number)
            board[(x, y)] = int(number)
    return board


def check_if_board_won(board, numbers):
    col_counts = [0]*BOARD_WIDTH
    row_counts = [0]*BOARD_HEIGHT
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[(x, y)] in numbers:
                col_counts[x] += 1
                row_counts[y] += 1

    return (any(count == BOARD_WIDTH for count in col_counts) or
            any(count == BOARD_HEIGHT for count in row_counts))
