import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
import numpy as np

def null_review(df):
    null_serie = df.isnull().sum()
    null_serie = null_serie[null_serie != 0]
    return null_serie

def null_percentage(df):
    null_serie = null_review(df)
    total = df.shape[0]
    null_dict = {}
    for i in range(null_serie.size):
        percent = round(null_serie.values[i]*100/total,2)
        null_dict[null_serie.index[i]] = percent
    return null_dict


def outlier_detect(df):
    ban_list = ['Telefono','X','Y','Latitud','Longitud']
    z_dict = {}
    outlier_dict={}
    for col in df.columns:
        if df[col].dtypes == np.float64:
            if col in ban_list:
                continue
            else:
                z = np.abs(stats.zscore(df[col].dropna()))
                z_dict[col] = z

                outlier_dict[col] = z_dict[col][z_dict[col] > 3]
    return outlier_dict

def outlier_percent(df):
    percent_outlier_dict={}
    outlier_dict = outlier_detect(df)
    total = df.shape[0]

    for i in range(len(outlier_dict.keys())):
        percent = len(list(outlier_dict.values())[i])*100/total
        percent_outlier_dict[list(outlier_dict.keys())[i]] = percent

    return percent_outlier_dict



def visual_report():
    pass




    



    



    