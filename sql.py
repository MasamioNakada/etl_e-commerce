from genericpath import exists
from sqlite3 import dbapi2
from sqlalchemy import create_engine
import pandas as pd
from utils import Say

say = Say()

username = "root"
password = "root"
host = "181.65.113.94"
dbname = "ecommerce"
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{dbname}")


def insert_master(df):
    df.to_sql("Localidades", con=engine, if_exists="append", index="False")


def insert_database(data_dict, labels):
    for label in labels:
        data_dict[label].to_sql(label, con=engine, if_exists="append")


def load_sql(data_dict, labels):

    df = pd.read_csv("in/Localidades.csv")
    insert_master(df)
    insert_database(data_dict, labels)
