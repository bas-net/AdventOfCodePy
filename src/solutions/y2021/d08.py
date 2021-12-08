
from typing import DefaultDict, Dict, List
from solutions.y2021.d07 import sum_all_numbers_below
import solutions.y2021.lib2021

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict
from collections import defaultdict
from dataclasses import dataclass, field


@input_strings
def p1(input_data) -> str:
    count_1_4_7_8 = 0
    for string in input_data:
        ten_unique_signal_patterns, four_digit_output_value = tuple(
            map(str.strip, string.split('|')))

        for seven_segment_display in four_digit_output_value.split(' '):
            if len(seven_segment_display) in [2, 4, 3, 7]:
                count_1_4_7_8 += 1

    return count_1_4_7_8


@input_strings
def p2(input_data) -> str:
    default_graph = get_default_graph()

    sum_all_numbers = 0
    for string in input_data:
        ten_unique_signal_patterns, four_digit_output_value = tuple(
            map(str.strip, string.split('|')))

        graph = get_graph(ten_unique_signal_patterns.split())

        overlay_graph(default_graph, graph)

        result = ''
        for digit in four_digit_output_value.split():
            nn = [num_node for num_node in graph.number_nodes if all(signal in num_node.segments for signal in digit) and len(digit) == len(num_node.segments)]
            nn = nn[0]
            result += str(nn.number)

        sum_all_numbers += int(result)

        # segment_signal_options: Dict[str, List[str]] = {}
        # for signal_line in get_a_g():
        #     segment_signal_options[signal_line] = list(get_a_g())

        # for pattern in ten_unique_signal_patterns.split():
        #     if len(pattern) == 2:
        #         # 1
        #         remove_signal_line_option(
        #             segment_signal_options, 'abdeg', pattern)
        #     if len(pattern) == 3:
        #         # 7
        #         remove_signal_line_option(
        #             segment_signal_options, 'bdeg', pattern)
        #     if len(pattern) == 4:
        #         # 4
        #         remove_signal_line_option(
        #             segment_signal_options, 'aeg', pattern)
        #     if len(pattern) == 7:
        #         # 8
        #         pass
        # print(segment_signal_options)
        # exit()
        # for seven_segment_display in four_digit_output_value.split(' '):
        #     if len(seven_segment_display) in [2, 4, 3, 7]:
        # count_1_4_7_8 += 1

    return sum_all_numbers


def get_a_g():
    return map(number_to_char_lowercase, range(0, 7))


def number_to_char_lowercase(number):
    return chr(number + 97)


def remove_if_exists(l, e):
    if e in l:
        l.remove(e)


def remove_signal_line_option(segment_signal_options, segments, pattern):
    for segment in segments:
        for signal_line in pattern:
            remove_if_exists(segment_signal_options[segment], signal_line)


@dataclass
class CharNode():
    char: str
    connections: List['NumberNode'] = field(default_factory=list)

    def __str__(self):
        return f'{{CharNode: {self.char} -> [{",".join(str(number_node.number) for number_node in self.connections)}]}}'


@dataclass
class NumberNode():
    number: int = -1
    connections: List[CharNode] = field(default_factory=list)

    def __str__(self):
        return f'{{NumberNode: {self.number} -> [{",".join(str(char_node.char) for char_node in self.connections)}]}}'

    @property
    def segments(self):
        return "".join(char_node.char for char_node in self.connections)


@dataclass
class Graph():
    number_nodes: List[NumberNode]
    char_nodes: List[CharNode]


def get_default_graph():
    lists = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg',
    }

    char_nodes: Dict[str, CharNode] = {}
    for char in get_a_g():
        char_nodes[char] = CharNode(char=char)

    number_nodes: List[NumberNode] = []

    for number, segments in lists.items():
        nn = NumberNode(number=number)
        number_nodes.append(nn)
        for segment in segments:
            char_nodes[segment].connections.append(nn)
            nn.connections.append(char_nodes[segment])

    # print(*char_nodes.values(), sep='\n')
    # print(*number_nodes, sep='\n')

    return Graph(number_nodes, char_nodes)


def get_graph(signal_lines: List[str]):
    char_nodes: Dict[str, CharNode] = {}
    for char in get_a_g():
        char_nodes[char] = CharNode(char=char)

    number_nodes: List[NumberNode] = []

    for segments in signal_lines:
        nn = NumberNode()
        number_nodes.append(nn)
        for segment in segments:
            char_nodes[segment].connections.append(nn)
            nn.connections.append(char_nodes[segment])

    # print(*char_nodes.values(), sep='\n')
    # print(*number_nodes, sep='\n')

    return Graph(number_nodes, char_nodes)


def overlay_graph(base_graph: Graph, graph: Graph):
    for number_node in graph.number_nodes:
        # print(f'Checking {number_node}')
        possible_matches = base_graph.number_nodes
        matches: List[NumberNode] = []
        for possible_match in possible_matches:
            # print(f'  Comparing to {possible_match}')
            # NumberNode connection_count vs connection_count
            if len(possible_match.connections) != len(number_node.connections):
                # Check if the lengths are the same, if not remove.
                # possible_matches.remove(possible_match)
                # print('    Ditched because counts are different')
                pass
            else:
                # NumberNode check if connections map
                possible_char_map_matches = [
                    len(char_node.connections) for char_node in possible_match.connections]
                for char_node in number_node.connections:
                    if len(char_node.connections) in possible_char_map_matches:
                        possible_char_map_matches.remove(
                            len(char_node.connections))
                    else:
                        break

                if len(possible_char_map_matches) > 0:
                    # possible_matches.remove(possible_match)
                    # print('    Ditched because no possible map on chars')
                    continue
                matches.append(possible_match)

            # print(*matches, sep='\n')

        # print(f'Matches for {number_node}')
        # print(*matches, sep='\n')
        if len(matches) != 1:
            raise Exception()
        number_node.number = matches[0].number
    # print(*graph.number_nodes, sep='\n')
