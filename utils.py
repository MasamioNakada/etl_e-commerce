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

    def get_delimiter(self, path, bytes=4096):
        sniffer = csv.Sniffer()
        data = open(path, "r").read(bytes)
        delimiter = sniffer.sniff(data).delimiter
        return delimiter

    def load_datasets_from_csv(self, path):
        labels = self.get_list_dir(path)
        dataset_dic = {}
        for name in labels:
            full_path = os.path.join(path, name)
            try:
                dataset_dic[name[:-4]] = pd.read_csv(
                    full_path, delimiter=self.get_delimiter(full_path), encoding="utf-8"
                )
            except:
                dataset_dic[name[:-4]] = pd.read_csv(
                    full_path,
                    delimiter=self.get_delimiter(full_path),
                    encoding="latin_1",
                )

        return dataset_dic


class Utils:

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
