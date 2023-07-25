# Para acceder a elementos de matrices 3-D, podemos usar números enteros separados por comas que representan las dimensiones y el índice del elemento.

import numpy as np

arr_numeros = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_numeros)

'''[[[ 1  2  3]
     [ 4  5  6]]

    [[ 7  8  9]
     [10 11 12]]]'''


# Acceda al 3er elemento de la 2ª matriz de la 1ª matriz
print(arr_numeros[0, 1, 2])  # 6


'''
Ejemplo explicado
arr[0, 1, 2] imprime el valor 6.

El primer número representa la primera dimensión, que contiene dos matrices:
[[1, 2, 3], [4, 5, 6]]
y:
[[7, 8, 9], [10, 11, 12]]

Como seleccionamos 0, nos queda la primera matriz:
[[1, 2, 3], [4, 5, 6]]

El segundo número representa la segunda dimensión, que también contiene dos matrices:
[1, 2, 3]
y:
[4, 5, 6]
Como seleccionamos 1, nos queda la segunda matriz:
[4, 5, 6]

El tercer número representa la tercera dimensión, que contiene tres valores:
4
5
6
Como seleccionamos 2, terminamos con el tercer valor:
6
'''

''' Las tres matrices son las siguientes:

La primera matriz es una matriz de 2x3. Esto significa que tiene 2 filas y 3 columnas. Los elementos de la matriz son 1, 2, 3, 4, 5, 6.
La segunda matriz es una matriz de 2x3. Esto significa que tiene 2 filas y 3 columnas. Los elementos de la matriz son 7, 8, 9, 10, 11, 12.
La tercera matriz es una matriz de 2x3. Esto significa que tiene 2 filas y 3 columnas. Los elementos de la matriz son 1, 2, 3, 4, 5, 6.
Las tres matrices se combinan para formar una matriz de 3x3x3. Esto significa que tiene 3 filas, 3 columnas y 3 capas

La primera y tercera matriz se repiten porque la matriz original es una matriz 3D. Esto significa que tiene 3 dimensiones: filas, columnas y capas.
'''
