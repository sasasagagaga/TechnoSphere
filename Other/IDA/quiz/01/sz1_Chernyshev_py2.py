
import numpy as np


def first(n):
    a = np.zeros((n, n))
    a[::2, ::2] = 1
    a[1::2, 1::2] = 1
    return a


def second(n):
    a = np.random.randint(1, 10000, n)
    b = a.copy()
    a[np.argsort(a)[-3:]] = 0
    return b, a


def third(n):
    return np.diag(np.random.randint(1, 20, n) ** 2)


def fourth(n, m):
    return np.arange(1, n * m + 1).reshape(m, n).T.reshape(n, m)


def fifth(n, m):
    A = np.random.randint(1, 10, (n, m))
    a = np.random.randint(1, 10, m)
    return A, a, ((A - a) ** 2).sum(axis=1) ** 0.5


# Formula was found here: https://en.wikipedia.org/wiki/Vector_space_model
def sixth(n, m):
    A = np.random.randint(1, 10, (n, m))
    a = np.random.randint(1, 10, m)
    return A, a, (A * a).sum(axis=1) / ((A ** 2).sum(axis=1) ** 0.5) / ((a ** 2).sum() ** 0.5)


# There are tests for every task
if __name__ == '__main__':
    # a = range(1, 11)
    # print a[0:5:3]
    results = [first(5), second(10), third(10), fourth(5, 5), fifth(3, 3), sixth(3, 3)]
    for i, res in enumerate(results):
        print "--- {} ---\n{}\n".format(i + 1, res)
