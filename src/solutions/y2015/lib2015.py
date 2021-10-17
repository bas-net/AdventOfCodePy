from typing import Callable
from os import linesep


def process_by_line(input: str, function: Callable[[str], None]):
    for line in input.split('\n'):
        function(line)
