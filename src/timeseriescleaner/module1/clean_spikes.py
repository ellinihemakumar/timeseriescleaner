'''Checking for jumps'''
import numpy as np
import pandas as pd


def clean_spikes(data: pd.Series, max_jump: int):
    '''Checking for jumps'''
    print("Checking for jumps in data")
    prev_value = data.iloc[0]
    for t, value in data.items():
        if abs(value - prev_value) <= max_jump:
            # "Value ok"
            data[t] = value
            prev_value = value
        else:
            data[t] = np.nan
            print("Jump detected and value removed on", t, ":", value)
    return data

    # print(f"Data removed: {data1_original[~data1_original.isin(data1)]}")