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
            if label == "Localidades.csv":
                continue
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
            "Overview": data_set.tail(),
            "Shape": data_set.shape,
            "Type of data": data_set.dtypes,
            "Null Values": data_set.isnull().sum(),
        }
        print("")
        print("")
        print("=" * 20, f"Review {label}", "=" * 20)
        for name, func in parameters.items():
            print("-" * 20, name, "-" * 20)
            print(func)


def find_id(columns_name: str) -> bool:
    return ("Id" in columns_name) or ("ID" in columns_name)


def id_to_int(dataframe):
    cols = list(dataframe.columns)
    for col in cols:
        if find_id(col):
            dataframe[col].apply(int)

    return dataframe


def id_to_int_iter(data_dict, labels):
    '''Vuelve a entero las columnas Id'''
    for label in labels:
        data_dict[label] = id_to_int(data_dict[label])
    return data_dict


class Say:

    # -----------------------------------------------
    def cow_says_good(self, str):
        """
        Aquí va un string , y la vaquita lo dirá :v
        """
        lenght = len(str)
        print(" _" + lenght * "_" + "_ ")
        print("< " + str + " > ")
        print(" -" + lenght * "-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print("            (__)\  good )\/\ ")
        print("                ||----w | ")
        print("                ||     || ")

    def cow_says_error(self, str):
        lenght = len(str)
        print(" _" + lenght * "_" + "_ ")
        print("< " + str + " > ")
        print(" -" + lenght * "-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print("            (__)\  error )\/\ ")
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
