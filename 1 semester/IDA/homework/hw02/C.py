import re
from operator import setitem
from functools import reduce


def solution1(lst):
    return list(map(lambda x: int(''.join(re.findall(r'\d+', x))[::-1]), lst))


def solution2(lst):
    return list(map(lambda x: x[0] * x[1], lst))


def solution3(r):
    return list(filter(lambda x: x % 6 in [0, 2, 5], r))


def solution4(lst):
    return list(filter(lambda x: x, lst))


def solution5(rooms):
    list(map(lambda d: setitem(d, 'square', d['width'] * d['length']), rooms))


def solution6(rooms):
    return list(map(lambda d: setitem(d, 'square', d['width'] * d['length']) or d, rooms))


def solution7(rooms):
    return list(map(lambda d: dict(d, **{'square': d['width'] * d['length']}), rooms))


def solution8(lst):
    return reduce(lambda x, y: (x[0] + y['height'], x[1] + 1), lst, (0, 0))


def solution9(lst):
    return list(map(lambda x: x['name'], filter(lambda x: x['gpa'] > 4.5, lst)))


def solution10(lst):
    return list(filter(lambda x: sum(map(int, x[::2])) == sum(map(int, x[1::2])), lst))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
