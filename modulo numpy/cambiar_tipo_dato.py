# astype: se utiliza para cambiar el tipo de datos de los elementos de un array NumPy. 
# Permite convertir un array a un tipo de datos diferente, lo que puede ser útil en diversas situaciones. 
# Este método crea una nueva copia del array con el nuevo tipo de datos, por lo que el array original no se modifica.

import numpy as np

num_enteros = np.array([1, 2, 3, 4, 5])
num_flotantes = num_enteros.astype(np.float64)

print(num_flotantes)  # [1. 2. 3. 4. 5.]

# -------------------------------------------------------------------------

# De flotante a entero
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')

print(newarr)        # [1 2 3]
print(newarr.dtype)  # int32

# -------------------------------------------------------------------------

# De entero a booleano:
arr_enteros = np.array([1, 0, 3])

arr_bol = arr_enteros.astype(bool)

print(arr_bol)        # [ True False True]
print(arr_bol.dtype)  # bool
