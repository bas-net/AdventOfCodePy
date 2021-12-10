
import solutions.y2021.lib2021

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict


@input_strings
def p1(input_data) -> str:
    total = 0
    for line in input_data:
        total += get_score_for_line(line)
    return total


def get_score_for_line(line):
    stack = []
    for c in line:
        if is_c_open_char(c):
            stack.append(c)
        elif is_c_close_char(c):
            if stack[-1] == mapping()[c]:
                stack.pop()
            else:
                return get_score_for_error(c)
    return 0


def get_score_for_error(c):
    return {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }[c]


def mapping():
    return {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }


def is_c_open_char(c):
    return c in ['(', '[', '{', '<']


def is_c_close_char(c):
    return c in [')', ']', '}', '>']


@input_strings
def p2(input_data) -> str:
    scores = []
    for line in input_data:
        score = get_score_for_line_2(line)
        if score != 0:
            scores.append(score)

    scores.sort()
    return scores[len(scores)//2]


def get_score_for_line_2(line):
    stack = []
    for c in line:
        if is_c_open_char(c):
            stack.append(c)
        elif is_c_close_char(c):
            if stack[-1] == mapping()[c]:
                stack.pop()
            else:
                return 0

    score = 0
    while len(stack) > 0:
        score *= 5
        score += get_score_for_completion_char(mapping()[stack.pop()])

    return score


def get_score_for_completion_char(c):
    return {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }[c]
