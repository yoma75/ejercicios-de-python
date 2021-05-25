# Operaciones sobre series y DataFrames

import pandas as pd
import numpy as np

serie1 = pd.Series([0,1,2], index=['a','b','c'])
print(serie1)  # a    0
               # b    1
               # c    2

serie2 = pd.Series([3,4,5,6], index=['a','b','c','d'])
print(serie2)  # a    3
               # b    4
               # c    5
               # d    6

suma = (serie1 + serie2)
print(f'\n{suma}')  # a    3.0
                    # b    5.0
                    # c    7.0
                    # d    NaN

lista_valores = np.arange(4).reshape(2,2)
print(f'\n{lista_valores}')  # [[0 1]
                             #  [2 3]]

# Crear una lista
lista_indices = list('ab')
print(f'\n{lista_indices}')  # ['a', 'b']

lista_columnas = list('12')
print(f'\n{lista_columnas}')  # ['1', '2']

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(f'\n{dataframe}')  #    1  2
                         # a  0  1
                         # b  2  3


lista_valores2 = np.arange(9).reshape(3,3)
print(f'\n{lista_valores2}')  # [[0 1 2]
                              #  [3 4 5]
                              #  [6 7 8]]

lista_indices2 = list('abc')  # ['a', 'b', 'c]
lista_columnas2 = list('123')  # # ['1', '2', '3']

dataframe2 = pd.DataFrame(lista_valores2, index=lista_indices2, columns=lista_columnas2)
print(f'\n{dataframe2}')  #    1  2  3
                          # a  0  1  2
                          # b  3  4  5
                          # c  6  7  8

sumita = dataframe + dataframe2
print(f'\n{sumita}')  #      1    2   3
                      # a  0.0  2.0 NaN
                      # b  5.0  7.0 NaN
                      # c  NaN  NaN NaN
