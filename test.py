import numpy as np
import pandas as pd

from load import Load
from utils import DataSets, Data, Dataframe

data = Data(path="in")
load = Load(path="in")


labels = data.get_labels(path="in")
data_dict = load.load_datasets_from_csv(path="in")


def resume_dataframe(data_dict, labels):
    for label in labels:
        DataSets(data_set=data_dict[label], label=label).dataset_resume(
            data_set=data_dict[label], label=label
        )


if __name__ == "__main__":
    # resume_dataframe(data_dict, labels)
    Dataframe(data_dict["Venta"]).dataset_date(data_dict["Venta"])
