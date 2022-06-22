from json import load
import os
from utils import Utils, Data
from load import Load
import pandas as pd


utils = Utils()

data = Data(path="in")

if __name__ == "__main__":
    pass
    # Con la función load_datasets_from csv cargamos todos los archivos csv de la carpeta 'in'
    # data_dict = load.load_datasets_from_csv(path="in")
    # utils.cow_says(f" {len(data_dict)} archivos subidos satisfactoriamente")
    # print(data_dict["Clientes"])
