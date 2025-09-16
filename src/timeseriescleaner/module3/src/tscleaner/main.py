'''entrance'''

import pandas as pd
from cleaning import SpikeCleaner, OutOfRangeCleaner, FlatPeriodCleaner
from plotting import plot_timeseries

# Create date range
date_rng = pd.date_range(start="1/1/2020", end="1/31/2020", freq="D")

# Sample time series data with DateTimeIndex
data1 = pd.Series([1, 2, -1, 4, 5, 20, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                   21, 22, 24, 24, 24, 24, 24, 24, 29, 30, 31], index=date_rng)
data2 = pd.Series([5, 6, 200, 8, 9, 10, 11, 12, 300, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                   23, 24, 25, 26, 27, 27, 27, 30, 31, 32, 33, 34, 35], index=date_rng)
data3 = pd.Series([15, 16, 11, 18, 400, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                   32, 33, 34, 35, 36, 37, 38, 39, 45, 45, 45, 45, 45, 45], index=date_rng)


cleaners = [
    SpikeCleaner(max_jump=10),
    OutOfRangeCleaner(min_val=0, max_val=50),
    FlatPeriodCleaner(flat_period=5),
]

# use cleaners dataclass
data_index = 1
for data in [data1, data2, data3]:
    label = 'Data ' + str(data_index)
    data_original = data.copy()
    for cleaner in cleaners:
        data = cleaner.clean(data)
    plot_timeseries(data_original, data, label=label)
    data_index += 1