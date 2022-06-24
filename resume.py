import pandas as pd

from utils import DataSets, Data, Say

say = Say()


def dataset_date(dataframe):
    try:
        dataframe.Fecha = pd.to_datetime(dataframe.Fecha, infer_datetime_format=True)
        dataframe.Fecha_Entrega = pd.to_datetime(
            dataframe["Fecha_Entrega"], infer_datetime_format=True
        )

        return dataframe
    except:
        dataframe.Fecha = pd.to_datetime(dataframe["Fecha"], infer_datetime_format=True)
        return dataframe


def dataset_date_iter(data_dict, labels):
    """Convierte a fecha"""
    for label in labels:
        try:
            dataset_date(data_dict[label])
            say.cow_says_good(f"Se cambio la columna Fecha en {label}")

        except:
            say.cow_says_error(f"{label} do not have [Fecha, Fecha_Entrega] columns")

    return data_dict


def resume_dataframe(data_dict, labels):
    """Da el resumen de los dataframes"""
    for label in labels:
        DataSets(data_set=data_dict[label], label=label).dataset_resume(
            data_set=data_dict[label], label=label
        )
