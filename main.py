import os
from utils import Utils, Data
import pandas as pd


utils = Utils()

if __name__ == "__main__":
    labels = utils.get_list_dir('in')
    
    data_1 = Data(os.path.join('in',labels[1]),'utf-8')

    print(data_1.load_from_csv)


    
  





