def p1(input: str) -> str:
    total = 0
    for package in input.split():
        dimensions = list(map(int, package.split('x')))

        sides = [dimensions[0] * dimensions[1],
                 dimensions[1] * dimensions[2],
                 dimensions[2] * dimensions[0]]
        sides.sort()

        package_total = sides[0] * 3 + sides[1] * 2 + sides[2] * 2

        total += package_total

    return total


def p2(input: str) -> str:
    total = 0
    for package in input.split():
        dimensions = list(map(int, package.split('x')))

        dimensions.sort()
        
        perimeter = dimensions[0] * 2 + dimensions[1] * 2

        ribbon = dimensions[0] * dimensions[1] * dimensions[2]

        total += perimeter + ribbon

    return total
