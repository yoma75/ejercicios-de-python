# Shape: es un atributo que se utiliza para obtener la dimensión o forma de un array. Un array en NumPy puede ser unidimensional (vector), bidimensional (matriz), o incluso de dimensiones superiores. El atributo shape devuelve una tupla que representa la longitud de cada dimensión del array.

import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Obtener las formas o dimensiones
shape_1d = array_1d.shape
shape_2d = array_2d.shape
shape_3d = array_3d.shape

print("Forma del array 1D:", shape_1d)  # Salida: (5,)

print("Forma del array 2D:", shape_2d)  # Salida: (2, 3) 2 filas y 3 columnas

print("Forma del array 3D:", shape_3d)  # Salida: (2, 2, 2)  
# tiene 2 bloques, cada bloque contiene 2 filas y 2 columnas.


'''El atributo shape es útil para entender las dimensiones y tamaños de los arrays, lo que facilita las operaciones matemáticas y manipulaciones de los mismos.'''
