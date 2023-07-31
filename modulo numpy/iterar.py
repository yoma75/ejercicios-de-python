# Iterar significa pasar por los elementos uno por uno.

import numpy as np

numeros = np.array([1, 2, 3, 4, 5])

for x in numeros:
    print(x)

'''
1
2
3
4
5
'''

# ----------------------------------------------------------------------------------------------------

# Iteración de matrices 2D

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)  # [1 2 3]
            # [4 5 6]


# ----------------------------------------------------------------------------------------------------

arr_num = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr_num:
  for y in x:
    print(y)

'''
1
2
3
4
5
6
'''


# ------------------------------------------------------------------------------------------------------

# Iteración de matrices 3D
# En una matriz 3D pasará por todas las matrices 2D.

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)  # [[1 2 3]
            #  [4 5 6]]
            # [[ 7  8  9]
            #  [10 11 12]]
 
# ------------------------------------------------------------------------------------------------------

# Para devolver los valores reales, los escalares, tenemos que iterar las matrices en cada dimensión

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

'''
1
2
3
4
5
6
7
8
9
10
11
12
'''

# ------------------------------------------------------------------------------------------------------

# nditer: es una función de ayuda que se puede utilizar desde iteraciones muy básicas hasta iteraciones muy avanzadas

arr_numeritos = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr_numeritos):
  print(x)

'''
1
2
3
4
5
6
7
8
'''
