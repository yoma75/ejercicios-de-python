# Seleccionar entradas para Dataframes

import pandas as pd
import numpy as np

lista_valores = np.arange(25).reshape(5,5)
print(lista_valores)  # [[ 0  1  2  3  4]
                      #  [ 5  6  7  8  9]
                      #  [10 11 12 13 14]
                      #  [15 16 17 18 19]
                      #  [20 21 22 23 24]]

# Los indices son las filas
lista_indices = ['i1','i2','i3','i4','i5']
lista_columnas = ['col1','col2','col3','col4','col5']

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(f'\n{dataframe}')  #     col1  col2  col3  col4  col5
                         # i1     0     1     2     3     4
                         # i2     5     6     7     8     9
                         # i3    10    11    12    13    14
                         # i4    15    16    17    18    19
                         # i5    20    21    22    23    24

# Acceder a un valor del dataframe
acceder = dataframe['col2']['i2']
print(f'\n{acceder}')  # 6


# Acceder a las columnas col3 y col5
acceder1 = dataframe[['col3','col5']]
print(f'\n{acceder1}')  #     col3  col5
                        # i1     2     4
                        # i2     7     9
                        # i3    12    14
                        # i4    17    19
                        # i5    22    24

# Valores mayores a 20
mayor = dataframe > 20
print(f'\n{mayor}')  #      col1   col2   col3   col4   col5
                     # i1  False  False  False  False  False
                     # i2  False  False  False  False  False
                     # i3  False  False  False  False  False
                     # i4  False  False  False  False  False
                     # i5  False   True   True   True   True

# Seleccionar el indice i3
fila = dataframe.loc['i3']
print(f'\n{fila}')  # col1    10
                    # col2    11
                    # col3    12
                    # col4    13
                    # col5    14



