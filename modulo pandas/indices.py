import pandas as pd

lista_valores = [1,2,3]
lista_indices = ['a','b','c']
serie = pd.Series(lista_valores, index=lista_indices)
print(serie)  # a    1
              # b    2
              # c    3


# Crear dataFrame a partir de una lista
lista_valores2 = [[5,8,2],[9,6,1],[8,5,3]]
lista_indices2 = ['historia','dibujo','deporte']
lista_nombres = ['Antonio','Maria','Pedro']

dataframe = pd.DataFrame(lista_valores2, index=lista_indices2, columns=lista_nombres)
print(dataframe)  #              Antonio  Maria  Pedro
                  # historia        5      8      2
                  # dibujo          9      6      1
                  # deporte         8      5      3
 

# Cuales son los indices
print(dataframe.index)  # Index(['historia', 'dibujo', 'deporte'], dtype='object')
