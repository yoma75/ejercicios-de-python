import numpy as np

matriz_ejemplo = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

nueva_matriz = matriz_ejemplo[:, :-1]  # Seleccionar todas las filas y todas las columnas excepto la última

print(nueva_matriz)  # [[1 2]
                     # [4 5]
                     # [7 8]]

'''En este ejemplo, se ha utilizado la notación [:, :-1] para seleccionar todas las filas (representadas por :) y todas las columnas excepto la última (representada por :-1). Permitiendo eliminar la segunda columna y quedarnos con las dos primeras.'''
