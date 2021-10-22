from collections import defaultdict


def p1(input_string: str) -> str:
    visited = defaultdict(lambda: 0)

    x = 0
    y = 0
    visited[(x, y)] += 1
    for c in input_string:
        (x, y) = determine_new_coordinates(x, y, c)
        visited[(x, y)] += 1

    return len(visited)


def p2(input_string: str) -> str:
    visited = defaultdict(lambda: 0)
    
    x = [0, 0]
    y = [0, 0]

    visited[(x[0], y[0])] += 1
    visited[(x[1], y[1])] += 1

    index = 0

    for c in input_string:
        (x[index % 2], y[index % 2]) = determine_new_coordinates(x[index % 2], y[index % 2], c)
        visited[(x[index % 2], y[index % 2])] += 1
        index += 1

    return len(visited)


def determine_new_coordinates(x, y, character):
    if character == '^':
        y += 1
    elif character == 'v':
        y -= 1
    elif character == '<':
        x -= 1
    elif character == '>':
        x += 1
    else:
        raise Exception('Invalid character')
    return (x, y)


