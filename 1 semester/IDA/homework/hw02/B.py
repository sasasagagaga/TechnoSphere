def solution1(s):
    return [c * 4 for c in s]


def solution2(s):
    return [c * (i + 1) for i, c in enumerate(s)]


def solution3(r):
    return [x for x in r if x % 3 == 0 or x % 5 == 0]


def solution4(lst):
    return [x for sub_lst in lst for x in sub_lst ]


def solution5(n):
    return [(a, b, c) for a in range(1, n + 1) for b in range(a + 1, n + 1) for c in range(b + 1, n + 1) if a ** 2 + b ** 2 == c ** 2]


def solution6(a, b):
    return [[x + y for y in b] for x in a]


def solution7(lst):
    return [[lst[i][j] for i in range(len(lst))] for j in range(len(lst[0]))]


def solution8(a):
    return [[int(x) for x in s.split(' ')] for s in a]


def solution9(r):
    return {chr(ord('a') + i): i ** 2 for i in r}


def solution10(lst):
    return {s.title() for s in lst if len(s) > 3}


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
