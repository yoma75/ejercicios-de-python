# Seleccionar datos en las series

import pandas as pd
import numpy as np

lista_valores = np.arange(3)
lista_indices = ['i1','i2','i3']

# Crear serie
serie = pd.Series(lista_valores, index=lista_indices)
print(serie)  # i1    0
              # i2    1
              # i3    2

# Acceder a un valor a partir del indice
acceder = serie['i2']
print(f'\n{acceder}')  # 1

# Acceder a la fila 2, las filas se cuentan a partir de 0
acceder1 = serie[2]
print(f'\n{acceder1}')  # 2

# Acceder a las filas a partir de un rango
acceder2 = serie[0:2]
print(f'\n{acceder2}')  # i1    0
                        # i2    1

# Acceder por los indices a partir de un rango
acceder3 = serie['i1':'i3']
print(f'\n{acceder3}')  # i1    0
                        # i2    1
                        # i3    2

# Acceder a valores mayores que 1
acceder4 = serie[serie > 1]
print(f'\n{acceder4}')  # i3    2 

# Asignar un valor a partir de una condicion
serie[serie > 1] = 7
print(f'\n{acceder3}')  # i1    0
                        # i2    1
                        # i3    7

