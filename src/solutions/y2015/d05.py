import solutions.y2015.lib2015
from collections import defaultdict

def p1(input: str) -> str:
    def func(string: str) -> int:
        vowel_count = 0
        has_double = False
        has_no_illegal = True
        for i, c in enumerate(string):
            if c in 'aeiou':
                vowel_count += 1
            if i > 0:
                if c == string[i-1]:
                    has_double = True
                if f'{string[i-1]}{c}' in ['ab', 'cd', 'pq', 'xy']:
                    has_no_illegal = False

        return 1 if vowel_count >= 3 and has_double and has_no_illegal else 0

    return solutions.y2015.lib2015.process_by_line_aggregate(input, func, sum)


def p2(input: str) -> str:
    def func(string: str) -> int:
        has_repeat_with_between = False
        has_duplicate_pair = False
        pairs_with_index = {}
        for i, c in enumerate(string):
            if i >= 1:
                pair = f'{string[i-1]}{c}'
                if pair in pairs_with_index:
                    if pairs_with_index[pair] < i - 1:
                        has_duplicate_pair = True
                else:
                    pairs_with_index[pair] = i
            if i >= 2:
                if c == string[i-2]:
                    has_repeat_with_between = True

        return 1 if has_repeat_with_between and has_duplicate_pair else 0

    return solutions.y2015.lib2015.process_by_line_aggregate(input, func, sum)
