"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un Dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
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
        #de aqui ´para arriba todo esta bien 

        #ingreso de datos al diccionario
        for i in range(2, len(lineas)):

            lineas[i] = re.sub(r"\s{2,}", ".", lineas[i]).strip().split(".")
            lineas[i] = list(filter(lambda x: x, lineas[i]))

            if lineas[i] and lineas[i][0].isnumeric():
                texto["cluster"].append(int(lineas[i][0]))
                texto["cantidad_de_palabras_clave"].append(int(lineas[i][1]))
                texto["porcentaje_de_palabras_clave"].append(float(lineas[i][2][:-2].replace(",", ".")))
                texto["principales_palabras_clave"].append(" ".join(lineas[i][3:]))

            elif texto["principales_palabras_clave"]:
                line = texto["principales_palabras_clave"].pop() + " " + " ".join(lineas[i])                
                texto["principales_palabras_clave"].append(line.strip())

    df = pd.DataFrame(texto)
    return df 