import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def null_review(dataframe):
    null_serie = dataframe.isnull().sum()
    null_serie = null_serie[null_serie != 0]
    return null_serie

def null_percentage(dataframe):
    null_serie = null_review(dataframe)
    total = dataframe.shape[0]
    null_dict = {}
    for i in range(null_serie.size):
        percent = round(null_serie.values[i]*100/total,2)
        null_dict[null_serie.index[i]] = percent

    return null_dict