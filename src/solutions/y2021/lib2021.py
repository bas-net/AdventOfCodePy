from dataclasses import dataclass, field
from typing import Callable, Dict, List


def process_by_line_aggregate(
        input_str: str,
        function: Callable[[str], int],
        aggregation: Callable[[int], int]) -> int:
    return aggregation([function(line) for line in input_str.split('\n')])


def process_by_line(input_str: str, function: Callable[[str], None]) -> None:
    for line in input_str.split('\n'):
        function(line)


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
    nodes: Dict[str, Node]
    vertices: List[Vertex]

    def __init__(self) -> None:
        self.nodes = {}
        self.vertices = []

    def add_vertex(self, node_name_soure: str, node_name_to: str, weight: int):
        source_node = self.get_node_from_name(node_name_soure)
        to_node = self.get_node_from_name(node_name_to)

        source_node.vertices_to[node_name_to] = weight
        to_node.vertices_to[node_name_soure] = weight

        self.vertices.append(Vertex(source_node, to_node, weight))

    def get_node_from_name(self, node_name):
        if node_name in self.nodes:
            return self.nodes[node_name]

        node_source = Node(node_name)

        self.nodes[node_name] = node_source

        return node_source

    def tsp_shortest_path(self) -> int:
        """Traveling salesman problem"""
        shortest = None

        def get_potential_paths(node_name, visited):
            paths = []
            for to in self.nodes[node_name].vertices_to:
                if to not in visited:
                    this_path = list(visited)
                    this_path.append(to)
                    for x in get_potential_paths(to, this_path):
                        paths.append(x)
            if len(paths) > 0:
                return paths

            return [visited]

        paths = []
        for start_node in self.nodes:
            for x in get_potential_paths(start_node, [start_node]):
                paths.append(x)

        for path in paths:
            try:
                length = sum(self.nodes[path[i]].vertices_to[path[i + 1]]
                             for i in range(len(path) - 1))
                if shortest is None or shortest > length:
                    shortest = length
            except KeyError:
                pass

        return shortest

    def tsp_longest_path_round(self) -> int:
        """Traveling salesman problem"""
        # print('Calculating TSP')
        longest = None

        def get_potential_paths(node_name, visited):
            paths = []
            for to in self.nodes[node_name].vertices_to:
                if to not in visited:
                    this_path = list(visited)
                    this_path.append(to)
                    for x in get_potential_paths(to, this_path):
                        paths.append(x)
            if len(paths) > 0:
                return paths

            return [visited]

        paths = []
        for start_node in self.nodes:
            for x in get_potential_paths(start_node, [start_node]):
                x.append(start_node)
                paths.append(x)

        for path in paths:
            try:
                length = sum(self.nodes[path[i]].vertices_to[path[i + 1]]
                             for i in range(len(path) - 1))
                if longest is None or longest < length:
                    longest = length
            except KeyError:
                pass

        return longest

    def tsp_longest_path(self) -> int:
        """Traveling salesman problem"""
        longest = None

        def get_potential_paths(node_name, visited):
            paths = []
            for to in self.nodes[node_name].vertices_to:
                if to not in visited:
                    this_path = list(visited)
                    this_path.append(to)
                    for x in get_potential_paths(to, this_path):
                        paths.append(x)
            if len(paths) > 0:
                return paths

            return [visited]

        paths = []
        for start_node in self.nodes:
            for x in get_potential_paths(start_node, [start_node]):
                paths.append(x)

        for path in paths:
            try:
                length = sum(self.nodes[path[i]].vertices_to[path[i + 1]]
                             for i in range(len(path) - 1))
                if longest is None or longest < length:
                    longest = length
            except KeyError:
                pass

        return longest
