from numpy import column_stack
import pandas as pd
import os
from utils import Say, Data

utils = Say()

# esta clase
class Load:
    def __init__(self, path) -> None:
        self.path = path

    def load_datasets_from_csv(self, path):
        labels = Data(path=path).get_list_dir(path)
        dataset_dict = {}
        for name in labels:
            if name == "Localidades.csv":
                continue
            full_path = os.path.join(path, name)
            try:
                dataset_dict[name[:-4]] = pd.read_csv(
                    full_path,
                    delimiter=Data(path=path).get_delimiter(full_path),
                    encoding="latin_1",
                )

                if name == "Clientes.csv":
                    dataset_dict[name[:-4]] = dataset_dict[name[:-4]].drop(
                        columns="col10"
                    )
            except:
                dataset_dict[name[:-4]] = pd.read_csv(
                    full_path,
                    delimiter=Data(path=path).get_delimiter(full_path),
                    encoding="utf-8",
                )

                if name == "Clientes.csv":
                    dataset_dict[name[:-4]] = dataset_dict[name[:-4]].drop(
                        columns="col10"
                    )
        return dataset_dict
