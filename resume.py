from utils import DataSets, Data
from load import Load


load = Load(path="in")
data = Data(path="in")

labels = data.get_labels(path="in")
data_dict = load.load_datasets_from_csv(path="in")


def to_date_dataframe(data_dict, labels):
    for label in labels:
        DataSets(data_set=data_dict[label])
    return data_dict


def resume_dataframe(data_dict, labels):
    for label in labels:
        DataSets(data_set=data_dict[label], label=label).dataset_resume(
            data_set=data_dict[label], label=label
        )


if __name__ == "__main__":

    data = to_date_dataframe(data_dict, labels)
    print(data)
