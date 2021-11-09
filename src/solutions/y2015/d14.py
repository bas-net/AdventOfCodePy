import re

import solutions.y2015.lib2015


def p1(input_string: str) -> str:
    reindeers = get_reindeers(input_string)

    return get_distance_of_fastest_at_time(reindeers, 1000 if len(reindeers) == 2 else 2503)


def p2(input_string: str) -> str:

    reindeers = get_reindeers(input_string)

    # Name: (distance, flying_for_resting_for, state)
    distances = {}
    for reindeer in reindeers:
        distances[reindeer[0]] = (0, 0, 'FLYING')
    
    points = {}
    for reindeer in reindeers:
        points[reindeer[0]] = 0

    for i in range(1000 if len(reindeers) == 2 else 2503):
        for reindeer in reindeers:
            current = distances[reindeer[0]]
            if current[2] == 'FLYING' and current[1] < reindeer[2]:
                distances[reindeer[0]] = (current[0] + reindeer[1], current[1] + 1, 'FLYING')
            elif current[2] == 'FLYING' and current[1] == reindeer[2]:
                distances[reindeer[0]] = (current[0], 1, 'RESTING')
            elif current[2] == 'RESTING' and current[1] < reindeer[3]:
                distances[reindeer[0]] = (current[0], current[1] + 1, 'RESTING')
            elif current[2] == 'RESTING' and current[1] == reindeer[3]:
                distances[reindeer[0]] = (current[0] + reindeer[1], 1, 'FLYING')
            else:
                raise Exception()
        
        max_dist = max([x[0] for x in distances.values()])
        for reindeer_name, information in distances.items():
            if information[0] == max_dist:
                points[reindeer_name] += 1

    return max(points.values())


def get_reindeers(input_string: str) -> str:
    def func(s):
        m = re.search(
            r'(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<flight_seconds>\d+) seconds, but then must rest for (?P<rest_seconds>\d+) seconds\.', s)
        g = m.groupdict()
        return (g['name'], int(g['speed']), int(g['flight_seconds']), int(g['rest_seconds']))

    return solutions.y2015.lib2015.process_by_line_aggregate(
        input_string, func, list)


def get_distance_of_fastest_at_time(reindeers, time):
    distances = {}
    for reindeer in reindeers:
        time_used = 0
        distance_flown = 0
        time_fly_rest_sequence = reindeer[2] + reindeer[3]
        distance_fly_rest_sequence = reindeer[1] * reindeer[2]

        while time_used <= time:
            time_left = time - time_used
            if time_left > time_fly_rest_sequence:
                time_used += time_fly_rest_sequence
                distance_flown += distance_fly_rest_sequence
            else:
                if time_left > reindeer[2]:
                    distance_flown += distance_fly_rest_sequence
                    break
                else:
                    distance_flown += time_left * reindeer[1]
                    break
        distances[reindeer[0]] = distance_flown
    return max(distances.values())
