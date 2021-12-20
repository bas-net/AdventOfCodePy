
from typing import Callable, NamedTuple
import solutions.y2021.lib2021

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict


def p1(input_data) -> str:
    binary_stream = convert_to_binary(input_data)
    packet_tree = extract_packet_tree(binary_stream)


def p2(input_data) -> str:
    pass


class N(NamedTuple):
    type_id: int
    version: int


class Lit(N):
    value: int


def convert_to_binary(hex_stream):
    def turn_to_decimal(hex_char):
        for char in hex_char:
            # print(f'{char} => {int(char, 16)} => {"{0:b}".format(int(char, 16)).rjust(4, "0")}')
            yield "{0:b}".format(int(char, 16)).rjust(4, "0")
            # break
    return ''.join(turn_to_decimal(hex_stream))


def extract_packet_tree(binary_stream):
    version = int(binary_stream[:3], 2)
    binary_stream = binary_stream[3:]
    type_id = int(binary_stream[:3], 2)
    binary_stream = binary_stream[3:]

    
    result, consumed = get_handler(type_id, version)(
        type_id, version, binary_stream)
    binary_stream = binary_stream[:consumed]

    # print(binary_stream)
    # print(int(version, 2))
    # print(int(type_id, 2))


def get_handler(type_id, version) -> Callable:
    mapping = {
        4: handle_literal,
    }
    if type_id in mapping:
        return mapping
    else:
        return handle_operator


def handle_operator(type_id, version, binary_stream):
    length_type_id = binary_stream[:1]
    binary_stream = binary_stream[1:]

    if length_type_id == 0:
        length_of_subpackets = int(binary_stream[:15], 2)
        binary_stream = binary_stream[15:]
        
    else:
        number_of_subpackets = int(binary_stream[:11], 2)
        binary_stream = binary_stream[11:]


    return (N(type_id, version), 10)

def handle_literal(type_id, version, binary_stream):
    """Returns the literal value AND the number of bits consumed."""
    chunck = binary_stream[:5]
    binary_stream = binary_stream[5:]

    data_chunks = [chunck[1:]]

    while chunck[0] == '1':
        chunck = binary_stream[:5]
        binary_stream = binary_stream[5:]
        data_chunks.append(chunck[1:])

    return (Lit(type_id, version, int(''.join(data_chunks), 2)), len(data_chunks) * 5)
