# tests/test_cleaning.py

import pytest
import pandas as pd
from src.tscleaner.cleaning import SpikeCleaner, OutOfRangeCleaner





@pytest.fixture
def time_series():
    date_rng = pd.date_range(start="2020-01-01", end="2020-01-10", freq="D")
    return pd.Series([1, 2, 3, 100, 5, 6, 7, 8, 9, 10], index=date_rng)


def test_spike_cleaner_removes_large_jumps(time_series):
    cleaner = SpikeCleaner(max_jump=10)
    cleaned = cleaner.clean(time_series)

    # Check that the spike (value=100) was cleaned
    assert cleaned.iloc[3] != 100
    # Optional: check NaN or interpolation if that's the behavior
    assert pd.isna(cleaned.iloc[3]) or cleaned.iloc[3] < 100


def test_out_of_range_cleaner_clips_or_removes():
    date_rng = pd.date_range(start="2020-01-01", periods=5, freq="D")
    series = pd.Series([-5, 10, 20, 55, 30], index=date_rng)

    cleaner = OutOfRangeCleaner(min_val=0, max_val=50)
    cleaned = cleaner.clean(series)

    assert pd.isna(cleaned.iloc[0])  # -5 becomes NaN error
    assert pd.isna(cleaned.iloc[3])  # 55 becomes NaN error
    assert cleaned.iloc[1] == 10     # valid value
    assert cleaned.iloc[2] == 20    # valid value
    assert cleaned.iloc[4] == 30   # valid value



#plot timeseries function test




