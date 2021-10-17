import os
import re
from typing import List, Tuple

NORMAL = '\033[00m'

RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
LIGHT_PURPLE = '\033[94m'


def print_colored(color: str, string: str) -> None:
    print(f'{color} {string}{NORMAL}')


def print_red(skk):
    print_colored(RED, skk)


def print_green(skk):
    print_colored(GREEN, skk)


def print_cyan(skk):
    print_colored(CYAN, skk)


def print_yellow(skk):
    print_colored(YELLOW, skk)


def print_light_purple(skk):
    print_colored(LIGHT_PURPLE, skk)


def get_solutions() -> List[Tuple[str, str, str, str]]:
    solutions = []

    solutions_path = './src/solutions'

    for year_dir in os.scandir(solutions_path):
        year = re.findall(r'y(\d\d\d\d)', year_dir.name)[0]
        for day_file in os.scandir(f'{solutions_path}/{year_dir.name}'):
            if not os.path.isfile(day_file.path):
                continue

            day_matches = re.findall(r'd(\d\d).py', day_file.name)

            # Skip if not a day file.
            if not day_matches:
                continue

            day = day_matches[0]

            solutions.append((year_dir.name, day_file.name, year, day))

    return solutions
