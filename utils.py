
import encodings
from importlib.resources import path
import os
import pandas as pd
import csv

class Data:
    def __init__(self, path, encoding):
        self.path = path
        self.encoding = encoding

    def get_list_dir(self):
        labels = os.listdir(self.path)
        return labels

    def get_delimiter(self, bytes = 4096):
        sniffer = csv.Sniffer
        

    @property
    def load_from_csv(self):
        
        data = pd.read_csv(self.path,sep='\s+' ,encoding=self.encoding, dtype = str)

        return data.head()
    



class Utils:



#-----------------------------------------------
    def cow_says(self,str):
        lenght = len(str)
        print(" _" + lenght*"_" + "_ ")
        print("< " + str + " > ")
        print(" -" + lenght*"-" + "- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print("            (__)\       )\/\ ")
        print("                ||----w | ")
        print("                ||     || ")

    def bart_says(self,str):
        print("⌈" + len(str) * "¯" + "⌉")
        print("⁞" + str + "⁞")
        print("⌊" + len(str) * "_" + "⌋")        
        print('   |/')
        print("|\/\/\/|")  
        print("|      |")
        print("|      |")
        print("| (o)(o)")
        print("C      _)")
        print("| ,___|")
        print("|   /")
        print("/____|")
        print("/     |")

#--------------------------------------------
