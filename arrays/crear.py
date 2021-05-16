import numpy as np

ejemplo = np.zeros(4)
print(ejemplo)  # [0. 0. 0. 0.]

ejemplo2 = np.ones(3)
print(ejemplo2)  # [1. 1. 1.]

ejemplo3 = np.arange(5)
print(ejemplo3)  # [0 1 2 3 4]

ejemplo4 = np.arange(2,20,3)  # Empieza en 2 hasta 20 y va de 3 en 3
print(ejemplo4)  # [ 2 5 8 11 14 17]

# Convertir una lista en un array
lista1 = [1,2,3,4]
array1  = np.array(lista1)
print(array1)  # [1 2 3 4]

# Listas dobles
lista1 = [1,2,3,4]
lista2 = [34,67,82,59]
lista_doble = (lista1,lista2)
print(lista_doble)  # ([1, 2, 3, 4], [34, 67, 82, 59])

# Convertir la lista anterior en un array
array_doble = np.array(lista_doble)
print(array_doble)  # [[ 1  2  3  4]
                    # [34 67 82 59]]

# Shape: que forma tiene
print(array_doble.shape)  # (2, 4), 2 filas y 4 columnas

# Tipo de dato del array
print(array_doble.dtype)  # int32
