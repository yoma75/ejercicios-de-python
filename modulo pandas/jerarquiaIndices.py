# Jerarquía en los índices

import pandas as pd
import numpy as np

lista_valores = np.random.rand(6)
lista_indices = [[1,1,1,2,2,2], ['a','b','c','a','b','c']]

series = pd.Series(lista_valores, index=lista_indices)
print(series)  # 1  a    0.333178
               #    b    0.425789
               #    c    0.566837
               # 2  a    0.590968
               #    b    0.650997
               #    c    0.269547   


# Ubicar un valor
valor = series[1]['b']
print(valor)  # 0.425789

dataframe = series.unstack()
print(dataframe)  #          a         b         c
                  # 1  0.68526  0.646017  0.469513
                  # 2  0.95028  0.078800  0.663508


lista_valores = np.arange(16).reshape(4,4)
lista_indices = list('1234')
lista_columnas = list('abcd')
dataframe2 = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe2)  #     a   b   c   d
                   # 1   0   1   2   3
                   # 2   4   5   6   7
                   # 3   8   9  10  11
                   # 4  12  13  14  15

# Crear serie con doble índice a partir del dataframe2
serie2 = dataframe2.stack()
print(serie2)  # 1  a     0
               #    b     1
               #    c     2
               #    d     3
               # 2  a     4
               #    b     5
               #    c     6
               #    d     7
               # 3  a     8
               #    b     9
               #    c    10
               #    d    11
               # 4  a    12
               #    b    13
               #    c    14
               #    d    15

