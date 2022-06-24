from load import Load
import pandas as pd
from thefuzz import process
import numpy as np


load = Load(path="in")

df_localidades = pd.read_csv("in/Localidades.csv")

choices_provincia = df_localidades.provincia_nombre.unique()
choices_localidad = df_localidades.localidad_censal_nombre.unique()
choices_departamento = df_localidades.departamento_nombre.unique()


buenos_aires = [
    "Ciudad de Buenos Aires",
    "CABA",
    "C deBuenos Aires",
    "Bs As",
    "Bs.As. ",
    "Buenos Aires",
    "B. Aires",
    "B.Aires",
    "Provincia de Buenos Aires",
    "Prov de Bs As.",
    "Pcia Bs AS",
]
buenos_aires_filter = lambda x: "Buenos Aires" if x in buenos_aires else x

capital_faderal = [
    "Capital",
    "Capital Federal",
    "CapFed",
    "Cap. Fed.",
    "Cap.   Federal",
]
capital_faderal_filter = lambda x: "Capital Federal" if x in capital_faderal else x


def normalizacion_sucursales(df):
    cord_label = ["Latitud", "Longitud"]
    filter_provincia = (
        lambda x: process.extractOne(x, choices_provincia)[0]
        if x in df.Provincia.unique()
        else x
    )
    filter_localidad = (
        lambda x: process.extractOne(x, choices_localidad)[0]
        if x in df.Localidad.unique()
        else x
    )

    df.Provincia = df.Provincia.apply(buenos_aires_filter)
    df.Provincia = df.Provincia.apply(filter_provincia)

    df.Localidad = df.Localidad.apply(buenos_aires_filter)
    df.Localidad = df.Localidad.apply(capital_faderal_filter)
    df.Localidad = df.Localidad.apply(filter_localidad)

    for label in cord_label:
        df[label] = df[label].replace(",", ".", regex=True)
        df[label] = df[label].astype(float)
        df[label] = df[label].apply(lambda x: -x if x > 0 else x)

    return df


def normalizacion_clientes(df):
    cord_label = ["X", "Y"]

    filter_provincia = (
        lambda x: process.extractOne(x, choices_provincia)[0]
        if x in df.Provincia.unique()
        else x
    )
    filter_localidad = (
        lambda x: process.extractOne(x, choices_localidad)[0]
        if x in df.Localidad.unique()
        else x
    )

    df.Provincia = df.Provincia.apply(buenos_aires_filter)
    df.Provincia = df.Provincia.apply(filter_provincia)

    df.Localidad = df.Localidad.apply(buenos_aires_filter)
    df.Localidad = df.Localidad.apply(filter_localidad)

    for label in cord_label:
        df[label] = df[label].replace(",", ".", regex=True)
        df[label] = df[label].replace("", np.nan, regex=True)
        df[label] = pd.to_numeric(df[label], errors="coerce")
        df[label] = df[label].apply(lambda x: -x if x > 0 else x)

    return df


def normalizacion_proveedor(df):
    for i in df.columns[2:]:
        df[i] = df[i].str.title()

    return df


def normalizar_all(data_dict):
    data_dict["Sucursales"] = normalizacion_sucursales(data_dict["Sucursales"])
    data_dict["Clientes"] = normalizacion_clientes(data_dict["Clientes"])
    data_dict["Proveedores"] = normalizacion_proveedor(data_dict["Proveedores"])

    return data_dict
