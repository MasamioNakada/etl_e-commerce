from time import process_time_ns
import pandas as pd

from utils import DataSets, Data, Say
from load import Load
from random import choices, choice


say = Say()
load = Load(path="in")
data = Data(path="in")

labels = data.get_labels(path="in")
data_dict = load.load_datasets_from_csv(path="in")


def dataset_date(dataframe):
    try:
        dataframe.Fecha = pd.to_datetime(dataframe['Fecha'], infer_datetime_format=True)
        dataframe.Fecha_Entrega = pd.to_datetime(
            dataframe['Fecha_Entrega'], infer_datetime_format=True
            )
        
        return dataframe
    except:
        dataframe.Fecha = pd.to_datetime(dataframe['Fecha'], infer_datetime_format=True)
        return dataframe


        

def dataset_date_iter(data_dict, labels):
    for label in labels:
        try:
            dataset_date(data_dict[label])
            print(f'pass {label}')
            return data_dict
        except:
            print(f'{label} do not have [Fecha, Fecha_Entrega] columns')

def resume_dataframe(data_dict, labels):
    for label in labels:
        DataSets(data_set=data_dict[label], label=label).dataset_resume(
            data_set=data_dict[label], label=label
        )
    
    


if __name__ == "__main__":
    #print(choice(labels))
    dataset_date_iter(data_dict, labels)

