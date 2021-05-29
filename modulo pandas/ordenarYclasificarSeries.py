# Ordenar y clasificar series

import pandas as pd
import numpy as np

lista_valores = range(4)
lista_indices = list('CABD')

serie = pd.Series(lista_valores, index=lista_indices)
print(serie) # C    0
             # A    1
             # B    2
             # D    3

# Ordenar los indices por orden alfabético
ordenar = serie.sort_index()
print(ordenar)  # A    1
                # B    2
                # C    0
                # D    3

serie2 = pd.Series(np.random.rand(10))
print(serie2)  

# ordenar por rank
ranki = serie2.rank()
print(f'\n{ranki}')  # 0     5.0
                     # 1     6.0
                     # 2     2.0
                     # 3     9.0
                     # 4     7.0
                     # 5     4.0
                     # 6     1.0
                     # 7    10.0
                     # 8     3.0
                     # 9     8.0

# ordenar por valores, los ordena de menor a mayor
ordenar_valores = ranki.sort_values()
print(ordenar_valores)  # 6     1.0
                        # 2     2.0
                        # 8     3.0
                        # 5     4.0
                        # 0     5.0
                        # 1     6.0
                        # 4     7.0
                        # 9     8.0
                        # 3     9.0
                        # 7    10.0

