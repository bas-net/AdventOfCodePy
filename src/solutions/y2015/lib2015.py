from typing import Callable

def process_by_line_aggregate(input: str, function: Callable[[str], int], aggregation: Callable[[int], int]):
    return aggregation([function(line) for line in input.split('\n')])
