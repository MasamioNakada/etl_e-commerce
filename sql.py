from sqlalchemy import create_engine
import pandas as pd
from utils import Say

say = Say()

username = "root"
password = "root"
host = "localhost"
dbname = "ecommerce"
engine = create_engine(
    "mysql+mysqlconnector://{0}:{1}@{2}/{3}".format(username, password, host, dbname)
)


def insert_master(df):
    df.to_sql("Localidades", con=engine, if_exists="append", index="False")


def insert_database(data_dict, labels):
    for label in labels:
        data_dict[label].to_sql(label, con=engine, if_exists="append")


def load_sql(data_dict, labels):

    df = pd.read_csv("in/Localidades.csv")
    insert_master(df)
    insert_database(data_dict, labels)
