#  Este ejericio incluye los archivos poblacion.xlsx, poblacion2.csv y poblacion3.txt, los cuales están en la carpeta principal

# Dado el fichero excel que se adjunta en varios formatos:
# Copiar los datos al porta-papeles (abrir el archivo, seleccionar y dar ctrl + c)
# Crear un dataframe 'datos' con esos datos copiados.
# Mostrar por pantalla todos los datos del dataframe
# Mostrar todos los nombres de las columnas
# Mostrar la primera fila
# Mostrar la primera columna
# Mostrar todas las filas pero solo las columnas 'continente' y 'poblacion'
# Mostrar las 3 primeras filas
# Mostrar las ultimas 2 filas

# CADA VEZ QUE SE EJECUTA PRINT, SE DEBE SELECCIONAR Y COPIAR (numeral 4)

import pandas as pd
import numpy as np

# Lee lo que esta en el porta-papeles (ctrl + c)
datos = pd.read_clipboard()
print(datos)

#   Continente Densidad  Superficie      Población              País más poblado             Ciudad más poblada
# 0       Asia    86,88  43.810.000  4.677.291.000         China (1.392.240.000)             Tokio (35.682.000)
# 1     África     32,7  30.370.000  1.110.020.000         Nigeria (191.205.000)          El Cairo (16.794.000)
# 2     Europa       70  10.180.000    801.000.000           Rusia (112.000.000)             Moscú (18.940.000)
# 3    América     23,5  42.330.000  1.094.215.000  Estados Unidos (330.028.000)  Ciudad de México (22.577.000)
# 4    Oceanía     4,25   9.008.500     40.201.000        Australia (27.240.000)             Sídney (6.550.000)  


# nombres de las columnas
x = datos.columns
print(x)  # Index(['Continente', 'Densidad', 'Superficie', 'Población', 'País más poblado', 'Ciudad más poblada']


# primera FILA
primera = datos.loc[0]
print(primera)  # Continente                             Asia
                # Densidad                              86,88
                # Superficie                       43.810.000
                # Población                     4.677.291.000
                # País más poblado      China (1.392.240.000)
                # Ciudad más poblada       Tokio (35.682.000)


# primera COLUMNA
y = datos['Continente']
print(y)  # 0       Asia
          # 1     África
          # 2     Europa
          # 3    América
          # 4    Oceanía


# todas las filas pero solo las columnas 'continente' y 'poblacion'
m = datos.loc[::, ['Continente','Población']]
print(m)  #   Continente      Población
          # 0       Asia  4.677.291.000
          # 1     África  1.110.020.000
          # 2     Europa    801.000.000
          # 3    América  1.094.215.000
          # 4    Oceanía     40.201.000


# 3 primeras filas
h = datos.head(3)
print(h)

#   Continente Densidad  Superficie      Población       País más poblado     Ciudad más poblada
# 0       Asia    86,88  43.810.000  4.677.291.000  China (1.392.240.000)     Tokio (35.682.000)
# 1     África     32,7  30.370.000  1.110.020.000  Nigeria (191.205.000)  El Cairo (16.794.000)
# 2     Europa       70  10.180.000    801.000.000    Rusia (112.000.000)     Moscú (18.940.000)


# ultimas 2 filas
w = datos.tail(2)
print(w)

#   Continente Densidad  Superficie      Población              País más poblado             Ciudad más poblada
# 3    América     23,5  42.330.000  1.094.215.000  Estados Unidos (330.028.000)  Ciudad de México (22.577.000)
# 4    Oceanía     4,25   9.008.500     40.201.000        Australia (27.240.000)             Sídney (6.550.000)

