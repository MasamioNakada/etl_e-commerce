import os
from utils import Utils, Data
import pandas as pd


utils = Utils()
data = Data(path="in")

if __name__ == "__main__":
    dict1 = data.load_datasets_from_csv(path="in")
    print(dict1)
