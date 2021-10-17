from collections import defaultdict


def p1(input_string: str) -> str:
    visited = defaultdict(lambda: 0)
    santa_x = 0
    santa_y = 0
    visited[(santa_x, santa_y)] += 1
    for c in input_string:
        if c == '^':
            santa_y += 1
        elif c == 'v':
            santa_y -= 1
        elif c == '<':
            santa_x -= 1
        elif c == '>':
            santa_x += 1
        else:
            raise Exception('Invalid character')
        visited[(santa_x, santa_y)] += 1

    return len(visited)


def p2(input_string: str) -> str:
    visited = defaultdict(lambda: 0)
    x = [0, 0]
    y = [0, 0]

    visited[(x[0], y[0])] += 1
    visited[(x[1], y[1])] += 1

    index = 0

    for c in input_string:
        if c == '^':
            y[index % 2] += 1
        elif c == 'v':
            y[index % 2] -= 1
        elif c == '<':
            x[index % 2] -= 1
        elif c == '>':
            x[index % 2] += 1
        else:
            raise Exception('Invalid character')
        visited[(x[index % 2], y[index % 2])] += 1
        index += 1

    return len(visited)
