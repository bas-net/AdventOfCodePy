from typing import List


def p1(input: str) -> str:
    return sum(convert_parentheses_to_ints(input))


def p2(input: str) -> str:
    pointer = 0
    index = 1

    for i in convert_parentheses_to_ints(input):
        pointer += i
        if pointer < 0:
            return index
        index += 1
    
    raise 'Error'

def convert_parentheses_to_ints(input: str) -> List[int]:
    return [1 if x == '(' else -1 if x == ')' else 0 for x in input]