from typing import List
from solutions.sharedlib import input_ints


@input_ints
def p1(data: List[int]) -> str:
    return get_count_of_increasing_depth_measurements(
        lambda: data[0],
        lambda i: data[i],
        range(1, len(data))
    )


@input_ints
def p2(data: List[int]) -> str:
    return get_count_of_increasing_depth_measurements(
        lambda: sum(data[0:2]),
        lambda i: sum(data[i:i+2]),
        range(1, len(data) - 2)
    )


def get_count_of_increasing_depth_measurements(init_func, adding_func, indices):
    prev = init_func()
    count = 0
    for x in map(adding_func, indices):
        if prev < x:
            count += 1
        prev = x

    return count
