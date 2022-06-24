from cmath import exp
from email import header
import pandas as pd

from utils import Say

say = Say()


def export_to_csv(data_dict, labels):

    Localidades = pd.read_csv("in/Localidades.csv")
    Localidades.to_csv(
        "out/localidades.csv", sep=",", index=False, header=False, encoding="latin_1"
    )
    for label in labels:
        data_dict[label].to_csv(
            f"out/{label}.csv", sep=",", index=False, header=False, encoding="latin_1"
        )
    intt = len(labels)

    return say.cow_says_good(f"Se exporto correctamente {intt} data sets de {intt}")
