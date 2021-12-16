
import solutions.y2021.lib2021

from solutions.sharedlib import GenericMap2D, Point2D, get_points_in_square, get_points_in_square_y_first, input_map_2d, input_strings, get_dict_from_string, input_dict


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
            visited[p] = min(risk_map.map[p] + visited[point],
                             visited[p] if p in visited else 99999999999999999)

        if point.y > 0:
            add_to_queue(point.up())

        if point.y < max_y - 1:
            add_to_queue(point.down())

        if point.x > 0:
            add_to_queue(point.left())

        if point.x < max_x - 1:
            add_to_queue(point.right())

    raise Exception()


@input_map_2d(dict, int)
def p2(risk_map: GenericMap2D) -> str:
    return None
    new_map = {}
    for y_tile in range(5):
        for x_tile in range(5):
            for y in range(risk_map.y_max):
                for x in range(risk_map.x_max):
                    p = Point2D(x, y)
                    oint = Point2D(p.x + risk_map.x_max * x_tile,
                                   p.y + risk_map.y_max * y_tile)
                    # if oint.x > 50:
                    #     print(oint)
                    if y_tile == 0 and x_tile == 0:
                        new_map[oint] = risk_map.map[p]
                    else:
                        if y_tile == 0:
                            # print(f'{oint} = {oint.add(Point2D(-risk_map.x_max, 0))} + 1')
                            new_map[oint] = new_map[oint.add(
                                Point2D(-risk_map.x_max, 0))] + 1
                        else:
                            new_map[oint] = new_map[oint.add(
                                Point2D(0, -risk_map.y_max))] + 1
                    if new_map[oint] > 9:
                        new_map[oint] = 1

    print(len(risk_map.map))
    print(len(new_map))
    max_x = risk_map.x_max * 5
    max_y = risk_map.y_max * 5

    # for y in range(max_y):
    #     for x in range(max_x):
    #         print(new_map[Point2D(x, y)], end='')
    #     print()
    # for p in get_points_in_square_y_first(max_x, max_y):
    #     print()

    print(max_x, max_y)

    start_point = Point2D(0, 0)
    goal_point = Point2D(max_x - 1, max_y - 1)

    queue = [start_point]
    visited = {start_point: 0}
    i = 0
    global min_so_far
    min_so_far = 99999999999
    while len(queue) > 0:
        queue.sort(
            key=lambda p: visited[p] + (((abs(p.x - goal_point.x) + abs(p.y-goal_point.y))*1) if min_so_far == 99999999999 else 0))
        point = queue.pop(0)
        i += 1
        if i % 1000 == 0:
            print(f'{i} {len(queue)} {queue[:3]}')
        # if point[0] in visited and visited[point[0]] < point[1]:
        #     continue

        if point == goal_point:
            # exit()
            return visited[goal_point]

        # visited[point[0]] = point[1]

        def add_to_queue(p):
            global min_so_far
            if p not in visited and (new_map[p] + visited[point]) < min_so_far:
                queue.append(p)
            visited[p] = min(new_map[p] + visited[point],
                             visited[p] if p in visited else 99999999999999999)
            if p == goal_point:
                min_so_far = min(
                    new_map[p] + visited[point], visited[p] if p in visited else 99999999999999999)
                print(f'Set min_so_far = {min_so_far}')

        if point.y > 0:
            add_to_queue(point.up())

        if point.y < max_y - 1:
            add_to_queue(point.down())

        if point.x > 0:
            add_to_queue(point.left())

        if point.x < max_x - 1:
            add_to_queue(point.right())

    raise Exception()
