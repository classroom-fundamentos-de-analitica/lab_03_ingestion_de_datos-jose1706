"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.
"""

import pandas as pd
import re

def ingest_data():

    #
    # Inserte su código aquí
    #
    with open("clusters_report.txt", "r") as archivo:
        lineas = archivo.readlines()
        lineas[0] = re.sub(r"\s{2,}", "-", lineas[0])
        print(lineas[0], lineas[1])
    
    return 


print(ingest_data())
