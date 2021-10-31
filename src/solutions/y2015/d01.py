from typing import Any, Callable, Dict, List, Union


def p1(input_string: str) -> str:
    return sum(convert_parentheses_to_ints(input_string))


def p2(input_string: str) -> str:
    return find_index_with_state(
        convert_parentheses_to_ints(input_string),
        state=lambda s, i: i if s is None else s + i,
        predicate=lambda s: s < 0
    ) + 1


def convert_parentheses_to_ints(input_string: str) -> List[int]:
    return map_dict_to_list({
        '(': 1,
        ')': -1
    }, input_string)


def map_dict_to_list(mapping: Dict[str, int], characters: Union[str, List]):
    return map(mapping.get, characters)


def find_index_with_state(
        data: List[Any],
        state: Callable[[Any, Any], Any],
        predicate: Callable[[Any], bool]
) -> int:
    state_data = None
    for i, e in enumerate(data):
        state_data = state(state_data, e)
        if predicate(state_data):
            return i
