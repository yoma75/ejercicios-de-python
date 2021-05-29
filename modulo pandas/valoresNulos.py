# Valores nulos - NaN - dentro de las series y dataframes

import pandas as pd
import numpy as np

lista_valores = ['1','2',np.nan,'4']

serie = pd.Series(lista_valores, index=list('abcd'))
print(serie)  # a      1
              # b      2
              # c    NaN
              # d      4

valor_boleano = serie.isnull()
print(valor_boleano)  # a    False
                      # b    False
                      # c     True
                      # d    False

# Borrar valores nulos
borrar = serie.dropna()
print(borrar)  # a    1
               # b    2
               # d    4


# ------ con dataframes ----------

valorsitos = [[1,2,3], [4,np.nan,5], [6,7,np.nan]]
print(valorsitos)  # [[1, 2, 3], [4, nan, 5], [6, 7, nan]]

lista_indices = list('123')  # [1, 2, 3]
lista_columnas = list('abc')  # ['a', 'b', 'c']

dataframe = pd.DataFrame(valorsitos, index=lista_indices, columns=lista_columnas)
print(dataframe)  #    a    b    c
                  # 1  1  2.0  3.0
                  # 2  4  NaN  5.0
                  # 3  6  7.0  NaN

boleano = dataframe.isnull()
print(boleano)  #        a      b      c
                # 1  False  False  False
                # 2  False   True  False
                # 3  False  False   True

# Borrar valores nulos, borra las filas que contengan elementos nulos
borrar2 = dataframe.dropna()
print(borrar2)  #    a    b    c
                # 1  1  2.0  3.0

# Rellenar los NaN con el valor 0
asignar = dataframe.fillna(0)
print(asignar)  #    a    b    c
                # 1  1  2.0  3.0
                # 2  4  0.0  5.0
                # 3  6  7.0  0.0

