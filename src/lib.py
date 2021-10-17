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
