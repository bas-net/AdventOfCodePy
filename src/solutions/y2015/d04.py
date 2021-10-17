import hashlib


def p1(input_string: str) -> str:
    i = 0
    hash_string = hashlib.md5(f'{input_string}{i}'.encode('utf-8')).hexdigest()
    while hash_string[0:5] != '00000':
        i += 1
        hash_string = hashlib.md5(f'{input_string}{i}'.encode('utf-8')).hexdigest()
    return i


def p2(input_string: str) -> str:
    i = 0
    hash_string = hashlib.md5(f'{input_string}{i}'.encode('utf-8')).hexdigest()
    while hash_string[0:6] != ('0' * 6):
        i += 1
        hash_string = hashlib.md5(f'{input_string}{i}'.encode('utf-8')).hexdigest()
    return i
