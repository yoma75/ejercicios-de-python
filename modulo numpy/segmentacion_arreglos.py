# Slicing (segmentacion): tomar elementos de un índice dado a otro indice dado
# [start:end]
# [start:end:step]
#  El resultado incluye el índice inicial, pero excluye el índice final.


import numpy as np

#  ARREGLOS UNIDIMENSIONALES:

# Indices:                0 1 2 3 4 5 6
array_numeros = np.array([1,2,3,4,5,6,7])


# Desde el índice 1 al índice 5
print(array_numeros[1:5])  # [2 3 4 5]


# Desde el índice 4 hasta el final de la matriz
print(array_numeros[4:])  # [5 6 7]


# Desde el principio hasta el índice 4
print(array_numeros[:4])  # [1 2 3 4]


# Desde el índice 3 del final hasta el índice 1 del final
print(array_numeros[-3:-1])  # [5 6]


# Devolver todos los elementos del índice 1 al índice 5, de dos en 2
print(array_numeros[1:5:2])  # [2 4]


# Devolver todos los elementos, de dos en 2
print(array_numeros[::2])  # [1 3 5 7]


# ------------------------------------------------------------------------------------------------------------

# SEGMENTACION DE MATRICES 2D

# Indices:           0  1  2  3  4    0  1  2  3  4
numeros = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


print(numeros)  #  [[ 1  2  3  4  5]   primera fila, posicion 0
                #   [ 6  7  8  9 10]]  segunda fila, posicion 1


# Desde el segundo elemento, divida los elementos del índice 1 al índice 4
print(numeros[1, 1:4])  # [7 8 9]


# De ambos elementos, índice de retorno 2
print(numeros[0:2, 2])  # [3 8]


''' 
1. `import numpy as np`: Esta línea importa la biblioteca Numpy y la asigna a un alias "np". Esto es una práctica común para ahorrar tiempo al escribir el nombre completo de la biblioteca y hacer que el código sea más legible.

2. `numeros = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])`: En esta línea, se crea un arreglo multidimensional (matriz) llamado "numeros" utilizando la función "np.array()" de Numpy. El arreglo contiene dos filas y cinco columnas. La primera fila contiene los elementos del 1 al 5, y la segunda fila contiene los elementos del 6 al 10.

3. `print(numeros[0:2, 2])`: Esta línea imprime un subconjunto del arreglo "numeros". El subconjunto se obtiene seleccionando todas las filas desde la posición 0 hasta la posición 2 (sin incluir la posición 2), y la columna en la posición 2.

Para entender mejor qué se imprime, vamos a analizar el subconjunto seleccionado:

- La notación `[0:2]` selecciona las filas desde la posición 0 hasta la posición 2, sin incluir la posición 2. En este caso, selecciona la primera fila (posición 0) y la segunda fila (posición 1).

- La notación `[:, 2]` selecciona la columna en la posición 2 para todas las filas del subconjunto seleccionado anteriormente. Es decir, selecciona el tercer elemento de cada una de las dos filas.

Entonces, el resultado impreso sería un arreglo unidimensional que contiene los elementos 3 y 8, que son los terceros elementos de las dos filas seleccionadas:  [3 8]
'''


# Indices:           0  1  2  3  4    0  1  2  3  4
numeros = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


print(numeros)  #  [[ 1  2  3  4  5]   primera fila, posicion 0
                #   [ 6  7  8  9 10]]  segunda fila, posicion 1


# De ambos elementos, el índice de división 1 al índice 4 (no incluido), esto devolverá una matriz 2D
print(numeros[0:2, 1:4])  # [[2 3 4]
                          #  [7 8 9]]
