import solutions.y2021.lib2021
from solutions.sharedlib import get_dict_from_string, input_dict
import re
BOARD_WIDTH = 5
BOARD_HEIGHT = 5


def p1(input_string: str) -> str:
    lines = input_string.split('\n')
    numbers = lines[0]
    boards = lines[2:]

    board_dicts = get_boards(boards)

    pulled_numbers = set()
    for number in map(int, numbers.split(',')):
        pulled_numbers.add(number)
        for board in board_dicts:
            if check_if_board_won(board, pulled_numbers):
                # print(f'Board won at number {number}!')
                return get_score(board, pulled_numbers, number)


def p2(input_string: str) -> str:
    lines = input_string.split('\n')
    numbers = lines[0]
    boards = lines[2:]

    board_dicts = get_boards(boards)

    pulled_numbers = set()
    for number in map(int, numbers.split(',')):
        pulled_numbers.add(number)
        for board in board_dicts:
            if check_if_board_won(board, pulled_numbers):
                if len(board_dicts) == 1:
                    return get_score(board,pulled_numbers, number)
                board_dicts.remove(board)
                


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
