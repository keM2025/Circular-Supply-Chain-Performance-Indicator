import pandas as pd

def min_max_normalize(series):
    return (series - series.min()) / (series.max() - series.min())

def invert(series):
    return 1 - series

def safe_divide(std, mean):
    return std / mean if mean != 0 else 0