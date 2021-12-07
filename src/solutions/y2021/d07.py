
import solutions.y2021.lib2021

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict, input_ints_csv


@input_ints_csv
def p1(input_data) -> str:
    lower = min(input_data)
    higher = max(input_data)

    fuel_consumption = None
    for i in range(lower, higher + 1):
        # print(f'trying {i}')
        result = sum(map(lambda horizontal_position: abs(
            i - horizontal_position), input_data))
        # print(f'result: {result}')

        if fuel_consumption == None:
            fuel_consumption = result
        else:
            fuel_consumption = min(fuel_consumption, result)

    return fuel_consumption

@input_ints_csv
def p2(input_data) -> str:
    lower = min(input_data)
    higher = max(input_data)

    fuel_consumption = None
    for i in range(lower, higher + 1):
        # print(f'trying {i}')
        result = sum(map(lambda horizontal_position: sum_all_numbers_below(abs(
            i - horizontal_position)), input_data))
        # print(f'result: {result}')

        if fuel_consumption == None:
            fuel_consumption = result
        else:
            fuel_consumption = min(fuel_consumption, result)

    return fuel_consumption


def sum_all_numbers_below(i):
    return sum(range(1, i + 1))
