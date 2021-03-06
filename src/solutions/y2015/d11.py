from typing import Tuple


def p1(input_string: str) -> str:
    # Get next password
    # Increment
    # Validate
    return get_next_valid_password(input_string)


def p2(input_string: str) -> str:
    return get_next_valid_password(get_next_valid_password(input_string))


def get_next_valid_password(password):
    password = get_next_pwd(password)

    while not validate_password(password):
        password = get_next_pwd(password)

    return password


def validate_password(password: str) -> bool:
    has_any_increment = False
    for i in range(len(password) - 2):
        n0 = ord(password[i])
        n1 = ord(password[i + 1])
        n2 = ord(password[i + 2])
        if n0 + 1 == n1 and n1 + 1 == n2:
            has_any_increment = True

    if not has_any_increment:
        return False

    for c in password:
        if c in ['i', 'o', 'l']:
            return False

    pair_indices = set()
    for i in range(len(password) - 1):
        c0 = password[i]
        c1 = password[i + 1]
        if c0 == c1:
            if i - 1 not in pair_indices:
                pair_indices.add(i)

    if len(pair_indices) < 2:
        return False

    return True


def get_next_pwd(password: str) -> str:
    pwd = list(password)

    next_password = ''
    overflow = False
    for i in range(len(pwd) - 1, -1, -1):
        (next_char, overflow) = get_next_char(pwd[i])
        next_password = next_char + next_password
        if not overflow:
            break

    next_password = password[:-len(next_password)] + next_password

    # skip passwords
    skip_from = None
    for i, c in enumerate(next_password):
        if i < len(password) - 1:
            if c in ['i', 'o', 'l']:
                skip_from = i
                break
    if skip_from:
        next_password = next_password[:skip_from + 1] + \
            ''.rjust(len(password) - skip_from - 1, 'z')

    return next_password


def get_next_char(char: str) -> Tuple[str, bool]:
    # bool=overflow or not
    # str is next char
    i = ord(char)
    i += 1

    if i > ord('z'):
        return (chr(i - 26), True)

    return (chr(i), False)
