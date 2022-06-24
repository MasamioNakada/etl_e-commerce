from thefuzz import process
import pandas as pd
from load import Load


def norm_sucursales(df: pd.DataFrame) -> pd.DataFrame:
    choices = [
        "Buenos Aires",
        "Catamarca",
        "Córdoba",
        "Corrientes",
        "Chaco",
        "Chubut",
        "Entre Ríos",
        "Formosa",
        "Jujuy",
        "La Pampa",
        "La Rioja",
        "Mendoza",
        "Misiones",
        "Neuquén",
        "Río Negro",
        "Salta",
        "San Juan",
        "San Luis",
        "Santa Cruz",
        "Santa Fe",
        "Santiago del Estero",
        "Tucumán",
        "Tierra del Fuego, Antártida e Islas del Atlántico Sur",
    ]
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
    df.Provincia = df.Provincia.apply(
        lambda x: "Buenos Aires" if x in buenos_aires else x
    )
    df.Provincia = df.Provincia.apply(
        lambda x: process.extractOne(x, choices)[0] if x in df.Provincia.unique() else x
    )
    return df


def norm_clientes(df: pd.DataFrame) -> pd.DataFrame:
    pass


def norm_proveedores(df: pd.DataFrame) -> pd.DataFrame:
    pass
