import numpy as np


def zeros_insert(k, n):
    x = np.zeros((n + 1) * (len(k) - 1) + 1)
    x[::n+1] = k
    return x

