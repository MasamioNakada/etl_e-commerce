import matplotlib.pyplot as plt
import seaborn as sns

from load import Load
from utils import Data

data = Data(path="in")
load = Load(path="in")


labels = data.get_labels(path="in")
data_dict = load.load_datasets_from_csv(path="in")


class Visualization:
    def __init__(self, labels, data_dict) -> None:
        self.labels = labels
        self.data_dict = data_dict
