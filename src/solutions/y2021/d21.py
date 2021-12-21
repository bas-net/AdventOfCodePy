
import solutions.y2021.lib2021

from solutions.sharedlib import input_named_tuple, input_strings, get_dict_from_string, input_dict


class DeterministicDie():

    def __init__(self) -> None:
        self.i = 0
        self.number_of_times_cast = 0

    def roll(self):
        self.number_of_times_cast += 1
        self.i += 1
        if self.i > 100:
            self.i = 1
        return self.i


class Player():
    def __init__(self, player_number, starting_position) -> None:
        self.player_number = player_number
        self.starting_position = starting_position
        self.score = 0
        self.position = starting_position

    def move_once(self, die):
        self.position += get_number_to_move(die)
        self.position = (self.position - 1) % 10 + 1
        self.score += self.position


@input_named_tuple(r'Player (\d+) starting position: (\d+)', [
    ('player_number', int),
    ('starting_position', int)
])
def p1(input_data) -> str:
    die = DeterministicDie()
    players = [Player(*i) for i in input_data]
    pi = 0
    while max([p.score for p in players]) < 1000:

        players[pi].move_once(die)

        pi += 1
        if pi >= len(players):
            pi = 0

    losing_player = [p for p in players if p.score < 1000][0]

    return losing_player.score * die.number_of_times_cast


@input_named_tuple(r'Player (\d+) starting position: (\d+)', [
    ('player_number', int),
    ('starting_position', int)
])
def p2(input_data) -> str:
    pass


def get_number_to_move(die: DeterministicDie):
    return die.roll() + die.roll() + die.roll()
