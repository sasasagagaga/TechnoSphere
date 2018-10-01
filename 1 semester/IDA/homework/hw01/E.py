import numpy as np
import pandas as pd

def df_diag_ones(df):
    df.values[range(df.shape[0]), range(df.shape[0])] = 1
    df.values[range(df.shape[0]), range(df.shape[0] - 1, -1, -1)] = 1
    return df

