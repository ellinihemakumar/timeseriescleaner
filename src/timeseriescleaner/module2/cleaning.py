from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass
class SpikeCleaner:
    '''Checking for jumps'''
    max_jump: int

    def clean(self, data: pd.Series) -> pd.Series:
        '''Cleaning data from jumps'''
        print("Checking for jumps in data")
        prev_value = data.iloc[0]
        for t, value in data.items():
            if abs(value - prev_value) <= self.max_jump:
                # "Value ok"
                data[t] = value
                prev_value = value
            else:
                data[t] = np.nan
                print("Jump detected and value removed on", t, ":", value)
        return data


@dataclass
class OutOfRangeCleaner:
    '''Checking for values in range'''
    min_val: int
    max_val: int

    def clean(self, data: pd.Series) -> pd.Series:
        '''Checking for values in range'''
        for t, value in data.items():
            # print("Checking value on", t, ":", value)
            if self.min_val <= value <= self.max_val:
                pass
                # print("Value ok:", value)
            else:
                data[t] = np.nan
                print("Value removed:", value)
        return data


@dataclass
class FlatPeriodCleaner:
    '''Checking for flat periods in data'''
    flat_period: int

    def clean(self, data: pd.Series) -> pd.Series:
        '''Checking for flat periods in data'''
        i = 0
        while i < len(data) - self.flat_period:
            if len(set(data[i: i + self.flat_period + 1])) == 1:
                print("Removing flat period starting at index:", i)
                data[i: i + self.flat_period + 1] = np.nan
                i += self.flat_period
            else:
                i += 1
        return data