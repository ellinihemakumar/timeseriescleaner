from matplotlib import pyplot as plt
import pandas as pd


def plot_timeseries(data_original: pd.Series, data: pd.Series, label: str = "Demo Data"):
    '''plot data showing outliers as red dots'''
    plt.figure(figsize=(10, 5))
    plt.plot(data_original, '.', color="red")
    plt.plot(data, '.', color="green")
    plt.title(label)
    plt.show()