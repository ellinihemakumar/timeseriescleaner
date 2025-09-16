import numpy as np
import pandas as pd


def clean_outofrange(data: pd.Series, min_val: int, max_val: int):
    '''Checking for values in range'''
    for t, value in data.items():
        # print("Checking value on", t, ":", value)
        if min_val <= value <= max_val:
            pass
            # print("Value ok:", value)
        else:
            data[t] = np.nan
            print("Value removed:", value)
    return data