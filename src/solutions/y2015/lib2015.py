from typing import Callable


def process_by_line_aggregate(
        input_str: str,
        function: Callable[[str], int],
        aggregation: Callable[[int], int]) -> int:
    return aggregation([function(line) for line in input_str.split('\n')])


def process_by_line(input_str: str, function: Callable[[str], None]) -> None:
    for line in input_str.split('\n'):
        function(line)
