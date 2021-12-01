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
    p = None
    c = 0
    data = list(map(int, input_string.split('\n')))
    for i in range(len(data) - 2):
        x = data[i] + data[i+1] + data[i+2]
        if not p:
            p = x
        else:
            if p < x:
                c += 1
            p = x
    return c
