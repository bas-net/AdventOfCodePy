import solutions.y2015.lib2015


def p1(input_string: str) -> str:
    out = input_string
    for _ in range(40):
        out = iteration(out)
    return len(out)


def p2(input_string: str) -> str:
    out = input_string
    for _ in range(50):
        out = iteration(out)
    return len(out)


def iteration(input_str: str) -> str:
    out = ''
    handling = None
    count = 0
    for c in input_str:
        if handling and handling == c:
            count += 1
        elif not handling:
            handling = c
            count += 1
        elif handling and handling != c:
            out += f'{count}{handling}'
            handling = c
            count = 1

    out += f'{count}{handling}'

    return out
