import numpy as np

# Crear un array
array = np.arange(0,11)
print(array)  # [ 0  1  2  3  4  5  6  7  8  9 10]

# subconjunto, 0: posición inicial hasta 3: posición final
print(array[0:3])  # [0 1 2]

# copiar un array
array_copia = array.copy()
print(array_copia)  # [ 0  1  2  3  4  5  6  7  8  9 10]

array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(array2)  # [[1 2 3]
               # [4 5 6]
               # [7 8 9]]

print(array2[1])  # [4 5 6]


