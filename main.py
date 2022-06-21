from utils import Utils

utils = Utils()


def load_data(path):
    return utils.load_from_csv(path)


if __name__ == "__main__":
    load_data("Datasets/Clientes.csv")
