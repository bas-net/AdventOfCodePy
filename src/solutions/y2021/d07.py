
import solutions.y2021.lib2021

from solutions.sharedlib import input_ints_csv


@input_ints_csv
def p1(input_data) -> str:
    return allign_crabs(input_data,
                        lambda i, horizontal_position: abs(i - horizontal_position))


@input_ints_csv
def p2(input_data) -> str:
    return allign_crabs(input_data,
                        lambda i, horizontal_position: sum_all_numbers_below(abs(i - horizontal_position)))


def allign_crabs(input_data, function):
    lower = min(input_data)
    higher = max(input_data)

    fuel_consumption = None
    for i in range(lower, higher + 1):
        result = sum(map(lambda x: function(i, x), input_data))

        if fuel_consumption == None:
            fuel_consumption = result
        else:
            fuel_consumption = min(fuel_consumption, result)

    return fuel_consumption


def sum_all_numbers_below(i):
    return sum(range(1, i + 1))


def none_safe(func, a, b):
    if a == None:
        return b
    else:
        return func(a, b)
