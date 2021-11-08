import re

import solutions.y2015.lib2015


def p1(input_string: str) -> str:
    def func(s):
        m = re.search(
            r'(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<flight_seconds>\d+) seconds, but then must rest for (?P<rest_seconds>\d+) seconds\.', s)
        g = m.groupdict()
        return (g['name'], int(g['speed']), int(g['flight_seconds']), int(g['rest_seconds']))

    reindeers = solutions.y2015.lib2015.process_by_line_aggregate(
        input_string, func, list)

    return get_distance_of_fastest_at_time(reindeers, 11 if len(reindeers) == 2 else 2503)


def p2(input_string: str) -> str:
    pass


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
