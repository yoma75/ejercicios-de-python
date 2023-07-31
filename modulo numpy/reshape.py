# reshape: se utiliza para cambiar la forma (dimensiones) de un arreglo sin cambiar sus datos subyacentes. Permite reorganizar los elementos del arreglo en una nueva estructura, siempre y cuando el número total de elementos sea el mismo antes y después de la operación.

import numpy as np

arr_numeros = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

nuevo_arr = arr_numeros.reshape(4, 3)

# 4 matrices cada una con 4 elementos
print(nuevo_arr)  # [[ 1  2  3]
                  #  [ 4  5  6]
                  #  [ 7  8  9]
                  #  [10 11 12]]

# --------------------------------------------------------------------------------------------------------------

# Convierta la siguiente matriz 1D con 12 elementos en una matriz 3D.
# La dimensión más externa tendrá 2 matrices que contienen 3 matrices, cada una con 2 elementos:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


# 2 filas, 3 columnas y 2 elementos en cada "celda"
newarr = arr.reshape(2, 3, 2)

print(newarr)

'''
Capa 1:     Capa 2:
[[ 1  2]    [[ 7  8]
 [ 3  4]     [ 9 10]
 [ 5  6]]    [11 12]]

El nuevo arreglo newarr ahora es un arreglo tridimensional con las siguientes características:
Tiene 2 "capas" (o matrices) de tamaño 3x2 cada una.
La primera capa contiene los elementos del 1 al 6, mientras que la segunda capa contiene los elementos del 7 al 12.
'''
