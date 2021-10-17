import solutions.y2015.lib2015
from collections import defaultdict


def p1(input: str) -> str:
    visited = defaultdict(lambda: 0)
    x = 0
    y = 0
    visited[(x, y)] += 1
    for c in input:
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '<':
            x -= 1
        elif c == '>':
            x += 1
        else:
            raise 'Error'
        visited[(x, y)] += 1

    return len(visited)


def p2(input: str) -> str:
    visited = defaultdict(lambda: 0)
    xs = [0, 0]
    ys = [0, 0]

    visited[(xs[0], ys[0])] += 1
    visited[(xs[1], ys[1])] += 1

    index = 0

    for c in input:
        if c == '^':
            ys[index % 2] += 1
        elif c == 'v':
            ys[index % 2] -= 1
        elif c == '<':
            xs[index % 2] -= 1
        elif c == '>':
            xs[index % 2] += 1
        else:
            raise 'Error'
        visited[(xs[index % 2], ys[index % 2])] += 1
        index += 1

    return len(visited)
