# ndmin: argumento que sirve para definir el numero de dimensiones de la matriz
# ndim: verifica el numero de dimensiones del array

'''Cree una matriz con 5 dimensiones y verifique que tenga 5 dimensiones:'''

import numpy as np

arr_numeros = np.array([1,45,87,23,55], ndmin=5)

print(arr_numeros)  # [[[[[ 1 45 87 23 55]]]]]
print(f'Numero de dimensiones: {arr_numeros.ndim}')  # Numero de dimensiones: 5


'''En esta matriz, la dimensión más interna (5.° dim) tiene 4 elementos, 
la 4.° dim tiene 1 elemento que es el vector, 
la 3.° dim tiene 1 elemento que es la matriz con el vector, 
la 2.° dim tiene 1 elemento que es una matriz 3D y 
la 1.° dim tiene 1 elemento que es una matriz 4D.'''
