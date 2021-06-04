# Tenemos 3 clases: 'clase1', 'clase2', 'clase3'
# Generar un número aleatorio de alumnos por clase
# Para obtener un número aleatorio utilizaremos:
# np.random.randint(minimo,maximo,numero)
# Crear una serie de clases y alumnos
# Utilizar el indice de la clase creada para saber el numero de alumnos de la clase2

import pandas as pd
import numpy as np

minimo = 10
maximo = 40
numero = 3  # numero de alumnos, 1 por cada clase
alumnos = np.random.randint(minimo,maximo,numero)

clases = ['clase1','clase2','clase3']
serie = pd.Series(alumnos, index=clases)
print(serie)  # clase1    21
              # clase2    10
              # clase3    15

# Numero de alumnos de la clase2
ubicar = serie['clase2']
print(ubicar)  # 10
