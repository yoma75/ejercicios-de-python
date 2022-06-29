'''Escribir una función que reciba un diccionario con las notas de los alumnos en curso en un examen y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.'''


import pandas as pd 

def estadistica_notas(notas):
    notas = pd.Series(notas)
    return notas.describe()

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(round(estadistica_notas(notas),2))  # 2 digitos después del punto

# count    5.00
# mean     6.60
# std      2.16
# min      4.00
# 25%      5.00
# 50%      6.50
# 75%      8.50
# max      9.00
# dtype: float64