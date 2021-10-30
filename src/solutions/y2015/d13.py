from typing import Dict, List, Tuple
import re
from dataclasses import dataclass, field
from collections import defaultdict

import solutions.y2015.lib2015


@dataclass(frozen=True)
class Node:
    name: str
    vertices_to: Dict[str, int] = field(default_factory=dict)


@dataclass(frozen=True)
class Vertex:
    from_node: Node
    to_node: Node
    weight: int


@dataclass
class PotentialPath:
    distance_total: int = 0
    visited_nodes: List[str] = field(default_factory=list)


class Graph:
    nodes: Dict[str, Node] = {}
    vertices = []

    def add_vertex(self, node_name_soure: str, node_name_to: str, weight: int):
        source_node = self.get_node_from_name(node_name_soure)
        to_node = self.get_node_from_name(node_name_to)

        source_node.vertices_to[node_name_to] = weight
        to_node.vertices_to[node_name_soure] = weight

        self.vertices.append(Vertex(source_node, to_node, weight))

    def get_node_from_name(self, node_name):
        if node_name in self.nodes:
            return self.nodes[node_name]
        else:
            node_source = Node(node_name)
            self.nodes[node_name] = node_source
            # print(f'Createing node {node_name}')
            return node_source

    def tsp_shortest_path(self) -> int:
        """Traveling salesman problem"""
        # print('Calculating TSP')
        shortest = None

        def get_potential_paths(node_name, visited):
            paths = []
            for to in self.nodes[node_name].vertices_to:
                if to not in visited:
                    this_path = [x for x in visited]
                    this_path.append(to)
                    for x in get_potential_paths(to, this_path):
                        paths.append(x)
            if len(paths) > 0:
                return paths
            else:
                return [visited]

        paths = []
        for start_node in self.nodes:
            for x in [x for x in get_potential_paths(start_node, [start_node])]:
                paths.append(x)

        for path in paths:
            # print(path)
            try:
                length = sum(self.nodes[path[i]].vertices_to[path[i + 1]]
                             for i in range(len(path) - 1))
                if shortest is None or shortest > length:
                    shortest = length
            except KeyError:
                pass

        return shortest

    def tsp_longest_path(self) -> int:
        """Traveling salesman problem"""
        # print('Calculating TSP')
        longest = None

        def get_potential_paths(node_name, visited):
            paths = []
            for to in self.nodes[node_name].vertices_to:
                if to not in visited:
                    this_path = [x for x in visited]
                    this_path.append(to)
                    for x in get_potential_paths(to, this_path):
                        paths.append(x)
            if len(paths) > 0:
                return paths
            else:
                return [visited]

        paths = []
        for start_node in self.nodes:
            for x in [x for x in get_potential_paths(start_node, [start_node])]:
                x.append(start_node)
                paths.append(x)

        for path in paths:
            # print(path)
            try:
                length = sum(self.nodes[path[i]].vertices_to[path[i + 1]]
                             for i in range(len(path) - 1))
                if longest is None or longest < length:
                    longest = length
                    # print(path)
            except KeyError:
                pass

        return longest


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

    lines = solutions.y2015.lib2015.process_by_line_aggregate(
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


def p2(input_string: str) -> str:
    pass
