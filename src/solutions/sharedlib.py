from typing import Any, Callable, List


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
