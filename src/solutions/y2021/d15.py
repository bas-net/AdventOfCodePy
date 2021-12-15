
import solutions.y2021.lib2021

from solutions.sharedlib import GenericMap2D, Point2D, get_points_in_square, input_map_2d, input_strings, get_dict_from_string, input_dict


@input_map_2d(dict, int)
def p1(risk_map: GenericMap2D) -> str:
    max_x = risk_map.x_max
    max_y = risk_map.y_max

    start_point = Point2D(0, 0)
    goal_point = Point2D(max_x - 1, max_y - 1)

    queue = [start_point]
    visited = {start_point: 0}
    i = 0
    while len(queue) > 0:
        queue.sort(key=lambda p: visited[p])
        point = queue.pop(0)
        # i += 1
        # if i % 100 == 0:
        #     print(f'{i} {len(queue)} {queue[:3]}')
        # if point[0] in visited and visited[point[0]] < point[1]:
        #     continue

        if point == goal_point:
            return visited[goal_point]

        # visited[point[0]] = point[1]

        def add_to_queue(p):
            if p not in visited:
                queue.append(p)
            visited[p] = min(risk_map.map[p] + visited[point], visited[p] if p in visited else 99999999999999999)

        if point.y > 0:
            add_to_queue(point.up())

        if point.y < max_y - 1:
            add_to_queue(point.down())

        if point.x > 0:
            add_to_queue(point.left())

        if point.x < max_x - 1:
            add_to_queue(point.right())

    raise Exception()


def p2(input_data) -> str:
    pass
