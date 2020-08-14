# # Escribir una función que reciba una diccionario con las notas de los alumnos en curso en un examen y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.


import pandas as pd 

def estadistica_notas(notas):
    notas = pd.Series(notas)
    return notas.describe()

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(estadistica_notas(notas))

