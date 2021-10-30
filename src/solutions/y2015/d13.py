from typing import Dict, List, Tuple
import re
from dataclasses import dataclass, field
from collections import defaultdict

from solutions.y2015.lib2015 import Graph, process_by_line_aggregate


@dataclass
class Line:
    name: str
    name_to: str
    action: str
    change: int

    def get_change(self):
        return self.change if self.action == 'gain' else -self.change

    def get_key_from_to(self):
        names = [self.name, self.name_to]
        names.sort()
        return f'{names[0]}&{names[1]}'


def p1(input_string: str) -> str:
    def extract(i: str) -> Line:
        matches = re.search(
            r'(?P<name>\w+) would (?P<action>\w+) (?P<change>\d+) happiness units by sitting next to (?P<namenextto>\w+).', i)

        return Line(matches.group('name'), matches.group('namenextto'), matches.group('action'), int(matches.group('change')))

    lines = process_by_line_aggregate(
        input_string, extract, list)

    x = defaultdict(lambda: 0)
    for y in lines:
        x[y.get_key_from_to()] += y.get_change()

    graph = Graph()
    edge: str
    for edge in x:
        graph.add_vertex(edge.split('&')[0], edge.split('&')[1], x[edge])
        graph.add_vertex(edge.split('&')[1], edge.split('&')[0], x[edge])

    # print(x)

    return graph.tsp_longest_path_round()


def p2(input_string: str) -> str:
    def extract(i: str) -> Line:
        matches = re.search(
            r'(?P<name>\w+) would (?P<action>\w+) (?P<change>\d+) happiness units by sitting next to (?P<namenextto>\w+).', i)

        return Line(matches.group('name'), matches.group('namenextto'), matches.group('action'), int(matches.group('change')))

    lines = process_by_line_aggregate(
        input_string, extract, list)

    x = defaultdict(lambda: 0)
    for y in lines:
        x[y.get_key_from_to()] += y.get_change()

    graph = Graph()
    edge: str
    for edge in x:
        graph.add_vertex(edge.split('&')[0], edge.split('&')[1], x[edge])
        graph.add_vertex(edge.split('&')[1], edge.split('&')[0], x[edge])

    # print(x)

    return graph.tsp_longest_path()
