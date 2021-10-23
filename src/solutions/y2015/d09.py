import re
from dataclasses import dataclass, field
from itertools import permutations
from typing import Dict, List

import solutions.y2015.lib2015


def p1(input_string: str) -> str:
    g = build_graph(input_string)
    # print([x for x in g.nodes])
    # print(g.nodes)
    return  g.tsp_shortest_path()


def p2(input_string: str) -> str:
    g = build_graph(input_string)
    # print([x for x in g.nodes])
    # print(g.nodes)
    return  g.tsp_longest_path()


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
                paths.append(x)

        for path in paths:
            # print(path)
            try:
                length = sum(self.nodes[path[i]].vertices_to[path[i + 1]]
                             for i in range(len(path) - 1))
                if longest is None or longest < length:
                    longest = length
            except KeyError:
                pass

        return longest


def build_graph(vertex_description_lines: str) -> Graph:
    graph = Graph()
    graph.nodes = {}
    graph.vertices = []
    # print([x for x in graph.nodes])

    def func(vertex_description: str) -> None:

        matches = re.search(
            r'(?P<source>\w+) to (?P<target>\w+) = (?P<distance>\d+)', vertex_description)
        graph.add_vertex(
            matches.group('source'),
            matches.group('target'),
            int(matches.group('distance')))

    solutions.y2015.lib2015.process_by_line(vertex_description_lines, func)

    return graph
