# suma de dos matrices:

import numpy as np

# Definimos dos matrices
matriz1 = np.array([[1, 2],
                    [3, 4]])

matriz2 = np.array([[5, 6],
                    [7, 8]])

suma_matrices = matriz1 + matriz2

print("Matriz 1:")
print(matriz1)  # Matriz 1:
                # [[1 2]
                #  [3 4]]

print("\nMatriz 2:")  
print(matriz2)  # Matriz 2:
                # [[5 6]
                #  [7 8]]

print("\nResultado de la suma:")
print(suma_matrices)  # Resultado de la suma:
                      # [[ 6  8]
                      #  [10 12]]
