# Estadísticas en dataFrame

import pandas as pd
import numpy as np

array = np.array([[1,8,3], [5,6,7]])
print(array)  # [[1 8 3]
              #  [5 6 7]]

dataframe = pd.DataFrame(array, index=['a','b'], columns=list('123'))
print(dataframe)  #    1  2  3
                  # a  1  8  3
                  # b  5  6  7

# sum: suma por columnas
sumita = dataframe.sum()
print(f'\n{sumita}')  # 1     6
                      # 2    14
                      # 3    10

# sumar por columnas, axis: eje x
sumita_col = dataframe.sum(axis=1)
print(sumita_col)  # a    12
                   # b    18

# mínimo valor por columnas
mini = dataframe.min()
print(mini)  # 1    1
             # 2    6
             # 3    3

# Máximo valor por columnas
max = dataframe.max()
print(max)  # 1    5
            # 2    8
            # 3    7

# máximo valor por filas
max2 = dataframe.max(axis=1)
print(max2)  # a    8
             # b    7

# descripción del dataframe
descrip = dataframe.describe()
print(descrip)  #               1         2         3
                # count  2.000000  2.000000  2.000000   cada columna tiene 2 elementos
                # mean   3.000000  7.000000  5.000000   suma los valores de cada columna y divide en 2 
                # std    2.828427  1.414214  2.828427   desviación típica
                # min    1.000000  6.000000  3.000000   mínimo
                # 25%    2.000000  6.500000  4.000000   suma los valores de cada columna y saca el 25% 
                # 50%    3.000000  7.000000  5.000000   suma los valores de cada columna y saca el 50% 
                # 75%    4.000000  7.500000  6.000000   suma los valores de cada columna y saca el 75% 
                # max    5.000000  8.000000  7.000000   máximo

