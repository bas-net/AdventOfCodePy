from typing import List


def p1(input_string: str) -> str:
    return sum(convert_parentheses_to_ints(input_string))


def p2(input_string: str) -> str:
    pointer = 0
    index = 1

    # TODO Possibly some kind of "run till sum/aggregation = or is less than more than/lambda expr"
    for i in convert_parentheses_to_ints(input_string):
        pointer += i
        if pointer < 0:
            return index
        index += 1

    raise Exception('Invalid state')


# TODO Possibly turn to a generic "character to int mapping"
def convert_parentheses_to_ints(input_string: str) -> List[int]:
    return [1 if x == '(' else -1 if x == ')' else 0 for x in input_string]
