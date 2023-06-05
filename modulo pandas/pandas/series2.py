'''Escribir una función que reciba un diccionario con las notas de los alumnos en curso en un examen y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.'''

import pandas as pd

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticos = pd.Series([notas.min(), 
                              notas.max(), 
                              notas.mean(), 
                              notas.std()], 
                              index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticos

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(round(estadistica_notas(notas),2))

# Min                  4.00
# Max                  9.00
# Media                6.60
# Desviación típica    2.16
# dtype: float64

