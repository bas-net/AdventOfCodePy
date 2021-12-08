from collections import namedtuple
import re
from typing import Any, Callable, Dict, List, NamedTuple, Pattern, Tuple, Union


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


def input_ints_csv(func: Callable[[List[int]], str]) -> Callable[[str], str]:
    def inner(*args, **kwargs) -> Any:
        if kwargs:
            print('Shouldn\'t have kwargs')
        if len(args) != 1:
            print('Should only have 1 arg')
        if not isinstance(args[0], str):
            print('Argument should be str')

        input_string = args[0]

        return func(list(map(int, input_string.split(','))))
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


def input_strings(func: Callable[[List[str]], str]) -> Callable[[str], str]:
    def inner(input_string: str) -> str:
        return func(input_string.split('\n'))
    return inner


RegexPattern = Union[str, Pattern]
Property = Tuple[str, Callable]


def input_named_tuple(
        regex: RegexPattern,
        properties: List[Property]):
    def decorator(func: Callable[[List[NamedTuple]], str]) -> Callable[[str], str]:
        def inner(input_string: str) -> str:
            Entity = namedtuple('Entity', [prop[0] for prop in properties])

            return func(
                list(
                    map(
                        lambda line: Entity(
                            **get_dict_from_string(regex, properties, line)),
                        input_string.split('\n')
                    )
                )
            )
        return inner
    return decorator
