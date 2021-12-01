import solutions.y2021.lib2021


def p1(input_string: str) -> str:
    p = None
    c = 0
    for x in map(int, input_string.split('\n')):
        if not p:
            p = x
        else:
            if p < x:
                c += 1
            p = x
    return c


def p2(input_string: str) -> str:
    pass
