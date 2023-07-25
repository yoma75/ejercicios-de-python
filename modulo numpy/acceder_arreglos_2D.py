'''Para acceder a elementos de matrices 2-D, podemos usar números enteros separados por comas que representan la dimensión y el índice del elemento.

Piense en matrices 2D como una tabla con filas y columnas, donde la dimensión representa la fila y el índice representa la columna.'''

import numpy as np

arr_numeros = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr_numeros)  # [[ 1  2  3  4  5]
                    #  [ 6  7  8  9 10]]


# Acceda al elemento de la 1ª fila, 2ª columna
print(f'Segundo elemento de la primera fila: {arr_numeros[0, 1]}')  # 2


# Acceda al elemento de la 2ª fila, 5ª columna
print(f'Quinto elemento de la segunda fila: {arr_numeros[1, 4]}')  # 10


# Imprime el último elemento del 2º dim:
print(f'Ultimo elemento del segundo dim: {arr_numeros[1, -1]}')  # 10
