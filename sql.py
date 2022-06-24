from genericpath import exists
from sqlalchemy import create_engine
import pandas as pd
from utils import Say

say = Say()

engine = create_engine(say.cow_says_good(input('Ingrese la Url de la base de datos: ')))

def insert_master(df):
    df.to_sql('Localidades', con=engine, if_exists="append", index='False')

def insert_database(data_dict,labels):
    for label in labels:
         data_dict[label].to_sql(label,con=engine,if_exists="append")

def load_sql(data_dict,labels):

    df = pd.read_csv('in/Localidades.csv')
    insert_master(df)
    insert_database(data_dict,labels)