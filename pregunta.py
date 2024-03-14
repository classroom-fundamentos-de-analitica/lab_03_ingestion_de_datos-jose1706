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
        #unir palabras por lineas
        primera = re.sub(r"\s{2,}", ",", lineas[0]).split(",")
        segunda = re.sub(r"\s{2,}", ",", lineas[1]).split(",")

        #limpiar las listas de encabezado
        primera.pop(), segunda.pop(0), segunda.pop(-1)

        #unir las palabras cortadas por el salto de linea y especificar el formato pedido
        encabezados = []
        for elm in primera:
            if "de" not in elm:
                encabezados.append(elm.lower().replace(" ", "_"))
            else:
                elm = elm + " " + segunda[0]
                encabezados.append(elm.lower().replace(" ", "_"))
        #definir las claves-columnas en los diccionarios
        texto = {
            encabezados[0] : [],
            encabezados[1] : [],
            encabezados[2] : [],
            encabezados[3] : [],
        }
        
        #ingreso de datos al diccionario
        for i in range(4, len(lineas)):
            ing = lineas[i].split() 
            if ing[0].isnumeric: #caso en el que se ingresa algun valor a las cuatro columnas
                texto[encabezados[0]].append(ing[0])
                texto[encabezados[1]].append(ing[1])
                texto[encabezados[2]].append(ing[2] + "%")
        print(encabezados)
        print(lineas[4][2], "si")
    return 


print(ingest_data())
