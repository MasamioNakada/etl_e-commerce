from utils import Data, Say, id_to_int_iter
from load import Load
import pandas as pd


import resume
import normalizar
import export
import data_quality as quality

say = Say()
load = Load(path="in")
data = Data(path="in")


if __name__ == "__main__":
    # cargamos del directorio in los dataframes
    try:
        labels = data.get_labels(path="in")
        data_dict = load.load_datasets_from_csv(path="in")
    except ValueError:
        say.cow_says_error("Error al cargar base de datos")

    # convertimos las columnas fechas a objeto -> datetime
    resume.dataset_date_iter(data_dict, labels)

    # todas las columnas tipo id se convierten en entero
    data_dict = id_to_int_iter(data_dict, labels)

    # normalizar los dataframes
    data_dict = normalizar.normalizar_all(data_dict)

    # imprimos el resumen de los dataframes
    resume.resume_dataframe(data_dict, labels)

    # Report de Calidad de los datos png
    quality.visual_report_iter(data_dict, labels)

    # Report autogenerado markdown
    quality.genarator_md_iter(labels)

    # export to csv
    export.export_to_csv(data_dict, labels)
