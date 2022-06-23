from utils import Data, Say, id_to_int_iter
from load import Load
import pandas as pd

import resume 

say = Say()
load = Load(path="in")
data = Data(path="in")



if __name__ == "__main__":
    #cargamos del directorio in los dataframes
    try:
        labels = data.get_labels(path="in")
        data_dict = load.load_datasets_from_csv(path="in")
    except ValueError:
        say.cow_says_error('Error al cargar base de datos')
    
    #convertimos las columnas fechas a objeto -> datetime
    resume.dataset_date_iter(data_dict, labels)
    
    data_dict = id_to_int_iter(data_dict, labels)

    #normalizar los dataframes

    #imprimos el resumen de los dataframes
    resume.resume_dataframe(data_dict, labels)




