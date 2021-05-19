# Crear una lista1 con los números del 10 al 19
# Crear una lista2 con los números del 50 al 59
# Crear una matriz de 2x10 (2 filas y 19 columnas) con las listas anteriores
# Crear otra matriz cuyos valores sean iguales a la matriz anterior multiplicados por 2

import numpy as np

lista1 = np.arange(10,20)
lista2 = np.arange(50,60)

# Para utilizar las 2 listas se deben de juntar
lista_doble = (lista1,lista2)


# crear matriz
matriz = np.array(lista_doble)
print(matriz)  # [[10 11 12 13 14 15 16 17 18 19]
               #  [50 51 52 53 54 55 56 57 58 59]

print(matriz.shape)  # (2, 10), 2 filas x 10 columnas


# Multiplicar x 2 la matriz 
multiplicar_matriz = matriz * 2
print(multiplicar_matriz)  # [[ 20  22  24  26  28  30  32  34  36  38]
                           #  [100 102 104 106 108 110 112 114 116 118]]
