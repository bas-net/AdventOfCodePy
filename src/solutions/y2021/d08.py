
import solutions.y2021.lib2021

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict

@input_strings
def p1(input_data) -> str:
    count_1_4_7_8 = 0
    for string in input_data:
        ten_unique_signal_patterns, four_digit_output_value = tuple(map(str.strip, string.split('|')))

        for seven_segment_display in four_digit_output_value.split(' '):
            if len(seven_segment_display) in [2, 4, 3, 7]:
                count_1_4_7_8 += 1

    return count_1_4_7_8



def p2(input_data) -> str:
    pass
