import pandas as pd
import numpy as np

np.arange(4)
serie = pd.Series(np.arange(4), index=['a','b','c','d'])
print(serie)  # a    0
              # b    1
              # c    2
              # d    3

borrar = serie.drop('c')
print(borrar)  # a    0
               # b    1
               # d    3

# Crear dataFrame a partir de una lista de valores de 9 elementos y de 3 filas x 3 columnas
lista_valores = np.arange(9).reshape(3,3)
print(lista_valores)  # [[0 1 2]
                      #  [3 4 5]
                      #  [6 7 8]]

lista_indices = ['a','b','c']
lista_columnas = ['c1','c2','c3']

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(f'\n{dataframe}')  #    c1  c2  c3
                         # a   0   1   2
                         # b   3   4   5
                         # c   6   7   8

# Borrar la fila b
borrar = dataframe.drop('b')
print(f'\n{borrar}')  #    c1  c2  c3
                      # a   0   1   2
                      # c   6   7   8                      

# Borrar columna c2, axis: es el eje
eliminar = dataframe.drop('c2', axis=1)
print(f'\n{eliminar}')  #    c1  c3
                        # a   0   2
                        # b   3   5
                        # c   6   8

# Cambios PERMANENTES
dataframe = dataframe.drop('b')
print(f'\n{dataframe}')
