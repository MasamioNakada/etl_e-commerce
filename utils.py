import pandas as pd


class Utils:
    def load_from_csv(self, path):
        data = pd.read_csv(path)
        return data.head(5)
