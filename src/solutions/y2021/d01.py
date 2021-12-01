from typing import List
import solutions.y2021.lib2021
from solutions.sharedlib import input_ints


@input_ints
def p1(ints: List[int]) -> str:
    p = None
    c = 0
    for x in ints:
        if not p:
            p = x
        else:
            if p < x:
                c += 1
            p = x
    return c


@input_ints
def p2(data: List[int]) -> str:
    p = None
    c = 0
    for i in range(len(data) - 2):
        x = data[i] + data[i+1] + data[i+2]
        if not p:
            p = x
        else:
            if p < x:
                c += 1
            p = x
    return c
