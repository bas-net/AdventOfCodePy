def p1(input: str) -> str:
    return sum([1 if x == '(' else -1 if x == ')' else 0 for x in input])


def p2(input: str) -> str:
    pass
