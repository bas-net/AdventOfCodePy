import re
from typing import Any, Callable, Dict, List, Pattern, Tuple, Union


def input_ints(func: Callable[[List[int]], str]) -> Callable[[str], str]:
    def inner(*args, **kwargs) -> Any:
        if kwargs:
            print('Shouldn\'t have kwargs')
        if len(args) != 1:
            print('Should only have 1 arg')
        if not isinstance(args[0], str):
            print('Argument should be str')

        input_string = args[0]

        return func(list(map(int, input_string.split('\n'))))
    return inner


def get_dict_from_string(
    regex: Union[str, Pattern],
    properties: List[Tuple[str, Callable]],
    string: str
) -> Dict[str, Any]:
    match = re.search(regex, string)

    groups = list(match.groups())

    if len(groups) != len(properties):
        raise Exception('Invalid property vs group count.')

    result = {}
    for i, (name, func) in enumerate(properties):
        result[name] = func(groups[i])

    return result


def input_dict(
    regex: Union[str, Pattern],
    properties: List[Tuple[str, Callable]]
) -> Callable[[Callable[[List[int]], str]], str]:
    def decorator(func: Callable[[List[int]], str]) -> Callable[[str], str]:
        def inner(input_string: str) -> str:
            return func(
                list(
                    map(
                        lambda line: get_dict_from_string(
                            regex, properties, line),
                        input_string.split('\n')
                    )
                )
            )
        return inner
    return decorator
