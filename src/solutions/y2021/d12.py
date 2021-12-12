
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

    print(*g.nodes, sep='\n')

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

    # print(queue)
    # print(full_paths)
    # exit()
    return len(full_paths)


def p2(input_data) -> str:
    pass
