import solutions.y2015.lib2015
import hashlib


def p1(input: str) -> str:
    i = 0
    hash = hashlib.md5(f'{input}{i}'.encode('utf-8')).hexdigest()
    while hash[0:5] != '00000':
        i += 1
        hash = hashlib.md5(f'{input}{i}'.encode('utf-8')).hexdigest()
    return i


def p2(input: str) -> str:
    pass
