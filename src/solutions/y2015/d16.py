
import solutions.y2015.lib2015

from solutions.sharedlib import input_strings, get_dict_from_string, input_dict


def get_list_of_things_about_sue():
    return {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }


@input_dict(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', [
    ('sue_number', int),
    ('p0_name', str),
    ('p0_value', int),
    ('p1_name', str),
    ('p1_value', int),
    ('p2_name', str),
    ('p2_value', int),
])
def p1(input_data) -> str:
    sue_identifiers = get_list_of_things_about_sue()
    for sue in input_data:
        if all(sue_identifiers[sue[f'p{i}_name']] == sue[f'p{i}_value'] for i in range(3)):
            return sue['sue_number']
    raise Exception('No matching Sue was found!')


def p2(input_data) -> str:
    pass
