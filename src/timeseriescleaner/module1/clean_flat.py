import numpy as np
import pandas as pd


def clean_flat(data: pd.Series, flat_period: int):
    '''Checking for flat periods in data'''
    i = 0
    while i < len(data) - flat_period:
        if len(set(data[i: i + flat_period + 1])) == 1:
            print("Removing flat period starting at index:", i)
            data[i: i + flat_period + 1] = np.nan
            i += flat_period
        else:
            i += 1
    return data