import solutions.y2021.lib2021
from solutions.sharedlib import get_dict_from_string, input_dict


def p1(input_string: str) -> str:
    bit_counts = []
    count = 0
    for line in input_string.split('\n'):
        count += 1
        for i, c in enumerate(line):

            if len(bit_counts) <= i:
                bit_counts.append(0)
            if c == '1':
                bit_counts[i] += 1

    # print(count/2)
    gamma = int(''.join(['0' if c < count / 2 else '1' for c in bit_counts]), 2)
    epsilon = int(''.join(['0' if c > count / 2 else '1' for c in bit_counts]), 2)
    # print(gamma)
    return gamma * epsilon


def p2(input_string: str) -> str:
    binary_lines_oxy = input_string.split('\n')
    binary_lines_co2 = input_string.split('\n')

    oxy_depth = 0
    while len(binary_lines_oxy) > 1:
        bit_count= 0
        for line in binary_lines_oxy:
            if line[oxy_depth] == '1':
                bit_count += 1
        if bit_count >= len(binary_lines_oxy)/2:
            binary_lines_oxy = [x for x in binary_lines_oxy if x[oxy_depth] == '1']
        else:
            binary_lines_oxy = [x for x in binary_lines_oxy if x[oxy_depth] == '0']
        oxy_depth += 1

    co2_depth = 0
    while len(binary_lines_co2) > 1:
        bit_count= 0
        for line in binary_lines_co2:
            if line[co2_depth] == '1':
                bit_count += 1
        if bit_count < len(binary_lines_co2)/2:
            binary_lines_co2 = [x for x in binary_lines_co2 if x[co2_depth] == '1']
        else:
            binary_lines_co2 = [x for x in binary_lines_co2 if x[co2_depth] == '0']
        co2_depth += 1

    oxy = int(binary_lines_oxy[0],2)
    co2 = int(binary_lines_co2[0],2)
    return oxy * co2
