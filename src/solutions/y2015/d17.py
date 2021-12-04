
from os import path, sep
from typing import List, Tuple
import solutions.y2015.lib2015

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict, input_ints

from itertools import permutations


@input_ints
def p1(input_data) -> str:
    if len(input_data) == 5:
        amount_to_store = 25
    else:
        amount_to_store = 150

    # working_options = set()
    # for option in permutations(input_data):
    #     total_option = 0
    #     for i, bucket in enumerate(option):
    #         total_option += bucket
    #         if total_option > amount_to_store:
    #             break
    #         if total_option == amount_to_store:
    #             opts = list(option[:i+1])
    #             opts.sort()
    #             working_options.add(tuple(opts))
    #             break

    options = list(enumerate(input_data))
    # print(options)

    options_found = recursive_find_options(amount_to_store, options)
    # print(*options_found, sep='\n')
    # exit()
    return len(options_found)


@input_ints
def p2(input_data) -> str:
    if len(input_data) == 5:
        amount_to_store = 25
    else:
        amount_to_store = 150
        
    options = list(enumerate(input_data))
    
    options_found = recursive_find_options(amount_to_store, options)

    min_length = min(len(x) for x in options_found)

    options_found = [x for x in options_found if len(x) == min_length]
    
    return len(options_found)


def recursive_find_options(
    amount_to_fill: int,
    options_left: List[Tuple[int, int]],
    total_so_far=0,
    path_so_far=()
) -> List[Tuple]:
    
    if total_so_far > amount_to_fill:
        # print(f'r {total_so_far} {path_so_far} options_left = {options_left} => bad!')
        return []
    if total_so_far == amount_to_fill:
        # print(f'r {total_so_far} {path_so_far} options_left = {options_left} => good!')
        l = list(path_so_far)
        l.sort()
        return [tuple(l)]

    # print(f'r {total_so_far} {path_so_far} options_left = {options_left}')

    results = []
    for i, option in enumerate(options_left):
        # Skip the path if the option we're looking at is bigger than the last.
        if len(path_so_far) > 0 and option[1] > path_so_far[-1][1]:
            continue

        results += recursive_find_options(amount_to_fill,
                                          options_left[:i] +
                                          options_left[i+1:],
                                          total_so_far + option[1],
                                          (*path_so_far, option))

    results = list(set(results))

    return results
