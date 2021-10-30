import re

from solutions.y2015.lib2015 import Graph, process_by_line


def p1(input_string: str) -> str:
    g = build_graph(input_string)
    return g.tsp_shortest_path()


def p2(input_string: str) -> str:
    g = build_graph(input_string)
    return g.tsp_longest_path()


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

    process_by_line(vertex_description_lines, func)

    return graph
