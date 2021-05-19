# Crear una lista con los valores numéricos del 1 al 30
# Crear otra lista con los primeros 10 valores de la lista inicial
# Crear otra lista con los últimos 10 valores de la lista inicial
# Crear un bucle que recorra esta última lista de valores finales


import numpy as np

lista1 = np.arange(1,31)


# primeros 10 valores de la lista inicial
principio = lista1[0:10]  # [ 1  2  3  4  5  6  7  8  9 10]
print(principio)


# últimos 10 valores de la lista inicial
final = lista1[-10:]  # [21 22 23 24 25 26 27 28 29 30]
print(final)


# Recorrer lista final
for valor in final:
  print(valor, end=' ')  # 21 22 23 24 25 26 27 28 29 30
