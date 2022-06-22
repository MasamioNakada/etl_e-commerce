import os

import pandas as pd
import csv


class Data:
    def __init__(self, path):
        self.path = path

        # self.encoding = encoding

    def get_list_dir(self, path):
        self.__labels = os.listdir(path)
        return self.__labels

    def get_labels(self, path):
        labels = self.get_list_dir(path)
        labels_clean = []

        for label in labels:
            labels_clean.append(label[:-4])

        return labels_clean

    def get_delimiter(self, path, bytes=4096):
        sniffer = csv.Sniffer()
        data = open(path, "r").read(bytes)
        delimiter = sniffer.sniff(data).delimiter
        return delimiter


class DataSets:
    def __init__(self, data_set, label) -> None:
        self.dataset = data_set
        self.label = label

    def dataset_resume(self, data_set, label):
        parameters = {
            "Overview": data_set.head(5),
            "Shape": data_set.shape,
            "Type of data": data_set.dtypes,
            "Null Values": data_set.isnull().sum(),
        }
        print("=" * 20, f"Review {label}", "=" * 20)
        for name, func in parameters.items():
            print("-" * 20, name, "-" * 20)
            print(func)


class Dataframe:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def dataset_date(self, dataframe):
        try:
            dataframe.Fecha = pd.to_datetime(dataframe.Fecha, format="%Y-%m-%d")
            dataframe.Fecha_Entrega = pd.to_datetime(
                dataframe.Fecha_Entrega, format="%Y-%m-%d"
            )
            return dataframe.dytpes
        except:
            pass
            Say.bart_says("Dataframe do not have [Fecha, Fecha_Entrega] columns")


class Say:

    # -----------------------------------------------
    def cow_says(self, str):
        lenght = len(str)
        print(" _" + lenght * "_" + "_ ")
        print("< " + str + " > ")
        print(" -" + lenght * "-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print("            (__)\       )\/\ ")
        print("                ||----w | ")
        print("                ||     || ")

    def bart_says(self, str):
        print("⌈" + len(str) * "¯" + "⌉")
        print("⁞" + str + "⁞")
        print("⌊" + len(str) * "_" + "⌋")
        print("   |/")
        print("|\/\/\/|")
        print("|      |")
        print("|      |")
        print("| (o)(o)")
        print("C      _)")
        print("| ,___|")
        print("|   /")
        print("/____|")
        print("/     |")


# --------------------------------------------
