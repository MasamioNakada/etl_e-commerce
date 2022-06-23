from utils import Data, Say, id_to_int_iter
from load import Load
import pandas as pd

import resume 

say = Say()
load = Load(path="in")
data = Data(path="in")



if __name__ == "__main__":
    try:
        labels = data.get_labels(path="in")
        data_dict = load.load_datasets_from_csv(path="in")
    except ValueError:
        say.cow_says_error('Error al cargar base de datos')
    
    resume.dataset_date_iter(data_dict, labels)
    data_dict = id_to_int_iter(data_dict, labels)
    resume.resume_dataframe(data_dict, labels)




