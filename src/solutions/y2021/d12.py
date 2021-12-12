
from dataclasses import dataclass, field
from typing import List, NamedTuple, Tuple
import solutions.y2021.lib2021

from solutions.sharedlib import input_named_tuple, input_strings, get_dict_from_string, input_dict


class Node(NamedTuple):
    id: str

    def is_small_cave(self):
        return self.id.islower()

    def is_big_cave(self):
        return self.id.isupper()

    def is_start(self):
        return self.id == 'start'

    def is_end(self):
        return self.id == 'end'


class Vertex(NamedTuple):
    link: Tuple[Node, Node]


class Graph(NamedTuple):
    nodes: List[Node]
    vertices: List[Vertex]

    def add_vertex(self, vertex: Vertex):
        self.vertices.append(vertex)
        for node in vertex.link:
            self.add_node_if_not_known(node)

    def add_node_if_not_known(self, node: Node):
        if node not in self.nodes:
            self.nodes.append(node)

    def get_node(self, id):
        return [node for node in self.nodes if node.id == id][0]

    def get_connected_nodes(self, source_node: Node):
        vertices = [
            vertex for vertex in self.vertices if source_node in vertex.link]
        return [node for vertex in vertices for node in vertex.link if node != source_node]


@input_named_tuple(r'(\w+)-(\w+)', [
    ('source', str),
    ('destination', str)
])
def p1(input_data) -> str:
    g = Graph([], [])

    for connection in input_data:
        g.add_vertex(
            Vertex((Node(connection.source), Node(connection.destination))))

    # print(*g.nodes, sep='\n')

    start = g.get_node('start')
    queue = [(start.id,)]
    full_paths = []

    while len(queue) > 0:
        path = queue.pop(0)
        last_node = g.get_node(path[-1])
        for connected_node in g.get_connected_nodes(last_node):
            if connected_node.is_small_cave() and connected_node.id in path:
                continue

            if connected_node.is_end():
                full_paths.append((*path, connected_node.id))
            else:
                queue.append((*path, connected_node.id))

    return len(full_paths)


@dataclass
class P2Path:
    path: Tuple
    duplicate_visited_small_cave: str

    @property
    def can_visit_small_again(self):
        return self.path.count(self.duplicate_visited_small_cave) < 2


@input_named_tuple(r'(\w+)-(\w+)', [
    ('source', str),
    ('destination', str)
])
def p2(input_data) -> str:
    g = Graph([], [])

    for connection in input_data:
        g.add_vertex(
            Vertex((Node(connection.source), Node(connection.destination))))

    # print(*g.nodes, sep='\n')

    start = g.get_node('start')
    all_small_ids = [node.id for node in g.nodes if node.is_small_cave() and not node.is_start() and not node.is_end()]
    queue = [P2Path((start.id,), None)] + [P2Path((start.id,), small_id)
                                           for small_id in all_small_ids]
    full_paths = []

    while len(queue) > 0:
        path = queue.pop(0)
        last_node = g.get_node(path.path[-1])
        for connected_node in g.get_connected_nodes(last_node):
            if connected_node.is_small_cave() and connected_node.id in path.path and not (connected_node.id == path.duplicate_visited_small_cave and path.can_visit_small_again):
                continue

            if connected_node.is_end():
                full_paths.append(
                    P2Path((*path.path, connected_node.id), path.duplicate_visited_small_cave))
            else:
                queue.append(P2Path((*path.path, connected_node.id),
                             path.duplicate_visited_small_cave))

    # print(*full_paths, sep='\n')
    # exit()

    full_paths = set(p2path.path for p2path in full_paths)

    return len(full_paths)
