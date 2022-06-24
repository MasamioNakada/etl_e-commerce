import os, sys
import pandas as pd
import matplotlib.pyplot as plt

from markdownmaker.document import Document
from markdownmaker.markdownmaker import *

from scipy import stats
import numpy as np

from utils import Say

say = Say()


def null_review(df):
    null_serie = df.isnull().sum()
    null_serie = null_serie[null_serie != 0]
    return null_serie


def null_percentage(df):
    null_serie = null_review(df)
    total = df.shape[0]
    null_dict = {}
    for i in range(null_serie.size):
        percent = round(null_serie.values[i] * 100 / total, 2)
        null_dict[null_serie.index[i]] = percent
    return null_dict


def null_all_percentage(df):
    null_serie = null_review(df)
    null_sum = null_serie.sum()
    total = df.shape[0]
    null_sum_percent = null_sum / total
    return null_sum_percent


def outlier_detect(df):
    ban_list = ["Telefono", "X", "Y", "Latitud", "Longitud"]
    z_dict = {}
    outlier_dict = {}
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
    percent_outlier_dict = {}
    outlier_dict = outlier_detect(df)
    total = df.shape[0]

    for i in range(len(outlier_dict.keys())):
        percent = len(list(outlier_dict.values())[i]) * 100 / total
        percent_outlier_dict[list(outlier_dict.keys())[i]] = percent

    return percent_outlier_dict


def outlier_all_percent(df):
    outlier_dict = outlier_detect(df)
    total = df.shape[0]
    percent = 0
    for i in range(len(outlier_dict.keys())):
        percent += len(list(outlier_dict.values())[i]) * 100 / total
    return percent


def visual_report(df, label):
    nulls = null_all_percentage(df)
    outliers = outlier_all_percent(df)

    sin_error = 100 - nulls - outliers

    height = np.array([nulls, sin_error, outliers])
    visual = ["no_error", "outlier", "null"]

    fig, ax = plt.subplots()
    bar = ax.bar(
        visual, height, align="center", color=["#19C5AF", "#FDF400", "#E455AD"]
    )

    ax.set_title(f"Tabla {label}")
    ax.set_ylabel("Porcentaje")

    ax.bar_label(bar, label_type="center", padding=8, fontsize=12)
    plt.savefig(f"out_plot/{label}.png")
    return plt.show()


def visual_report_iter(data_dict, labels):
    for label in labels:
        visual_report(data_dict[label], label)


def generator_md(label):

    doc = Document()

    doc.add(Header("Report Data Quality "))
    with HeaderSubLevel(doc):
        doc.add(Header(f"{label} DataSet"))
        doc.add(Image(url=f"../out_plot/{label}.png", alt_text=f"{label}"))

    return doc.write()


def genarator_md_iter(labels):

    fd = os.open("report/reporte_calidad_datos.md", os.O_RDWR)
    title = "# Reporte de ventas\n \n"
    doc = ""
    for label in labels:
        doc += generator_md(label)

    line = str.encode(title + doc)
    os.write(fd, line)
    os.close(fd)
    return say.cow_says_good("reporte escrito exitosamente en ./report")
