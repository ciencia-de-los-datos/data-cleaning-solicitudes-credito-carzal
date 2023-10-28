"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from unidecode import unidecode
import re


def clean_data():
    def format_date(str_date):
        d = re.search(r'(^\d+)\/(\d+)\/(\d+)', str_date, re.IGNORECASE)
        day = d.group(1)
        month = d.group(2)
        year = d.group(3)
        if len(day)>2:
            date = year + '/' + month + '/' + day
            return date
        else:
            date = day + '/' + month + '/' + year
            return date

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.rename(columns={'Unnamed: 0':'index'},inplace=True)
    df.set_index('index',inplace=True)


    df["sexo"] = df["sexo"].apply(lambda x : x.upper())
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].apply(lambda x : str(x).upper()).apply(lambda x: str(x).replace(" ","")).apply(lambda x: unidecode(x)) 
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x : str(x).upper()).apply(lambda x: str(x).replace(" ","")).apply(lambda x: unidecode(x)).apply(lambda x: str(x).replace("-","")).apply(lambda x: str(x).replace("_","")).apply(lambda x: str(x).replace("-","")).apply(lambda x: str(x).replace(".",""))
    #df["barrio"] = df["barrio"].apply(lambda x : str(x).upper()).apply(lambda x: str(x).replace(" ","")).apply(lambda x: unidecode(x)).apply(lambda x: str(x).replace("-","")).apply(lambda x: str(x).replace("_","")).apply(lambda x: str(x).replace("-","")).apply(lambda x: str(x).replace(".","")).apply(lambda x: str(x).replace("?","E"))
    df.barrio = df.barrio.apply(lambda x : str(x).upper()).map(lambda x: re.sub("-| ", "_", str(x)))
    df["línea_credito"] = df["línea_credito"].apply(lambda x : str(x).upper()).apply(lambda x: str(x).replace(" ","")).apply(lambda x: unidecode(x)).apply(lambda x: str(x).replace("-","")).apply(lambda x: str(x).replace("_","")).apply(lambda x: str(x).replace("-","")).apply(lambda x: str(x).replace(".",""))
    #df["línea_credito"] = ["SOLIDARIA" if i == "SOLIDIARIA" else i for i in df["línea_credito"] ]
    #df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format= "mixed")
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: x.replace("$","")).apply(lambda x: x.replace(" ","")).apply(lambda x: x.replace(",","")).astype(float).astype(int)

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    return df