import numpy as np
import pandas as pd


def peak_finder(s):
    x = s.values
    mask = (x[:-1] > x[1:])[1:] * (x[:-1] < x[1:])[:-1]
    return np.where(mask)[0] + 1

