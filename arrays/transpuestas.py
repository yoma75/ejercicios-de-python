# Arrays o matrices transpuestas: consiste en cambiar ordenadamente las filas por las columnas

import numpy as np

# Crea un array de 0 a 15, de 3 filas y 5 columnas
array = np.arange(15).reshape((3,5))
print(array)  # [[ 0  1  2  3  4]
              #  [ 5  6  7  8  9]
              #  [10 11 12 13 14]]

# Mostrar el numero 7 del array anterior
print(array[1][2])  # fila 1 y columna 2

# array transpuesto
array_transpuesto = array.T
print(array_transpuesto)  # [[ 0  5 10]
                          #  [ 1  6 11]
                          #  [ 2  7 12]
                          #  [ 3  8 13]
                          #  [ 4  9 14]]
