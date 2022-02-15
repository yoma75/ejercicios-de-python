# Escribir una función que reciba una diccionario con las notas de los alumnos en curso en un examen y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.

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
print(estadistica_notas(notas))

# Min                  4.000000
# Max                  9.000000
# Media                6.600000
# Desviación típica    2.162175
# dtype: float64

