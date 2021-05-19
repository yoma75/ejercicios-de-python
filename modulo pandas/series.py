import pandas as pd

serie = pd.Series([3,5,7])
print(serie)  # 0    3
              # 1    5
              # 2    7

print(serie[1])  # 5


asignaturas = ['matematicas', 'fisica', 'historia', 'biologia']
notas = [8,5,7,9]
alumno_daniel = pd.Series(notas,index=asignaturas)
print(alumno_daniel)  # matematicas    8
                      # fisica         5
                      # historia       7
                      # biologia       9


print(alumno_daniel['historia'])  # 7
print(alumno_daniel[alumno_daniel >= 8])  # matematicas    8
                                          # biologia       9


alumno_daniel.name = 'Notas de Daniel'
print(alumno_daniel)  # matematicas    8
                      # fisica         5
                      # historia       7
                      # biologia       9
                      # Name: Notas de Daniel


# Colocar un nombre al index
alumno_daniel.index.name = 'Asignaturas del alumno Daniel'
print(alumno_daniel)  # Asignaturas del alumno Daniel
                      # matematicas    8
                      # fisica         5
                      # historia       7
                      # biologia       9
                      # Name: Notas de Daniel


# Convertir una serie en un diccionario
diccionario = alumno_daniel.to_dict()
print(diccionario)  # {'matematicas': 8, 'fisica': 5, 'historia': 7, 'biologia': 9}


# Convertir un diccionario a una serie
serie1 = pd.Series(diccionario)
print(serie1)  # matematicas    8
               # fisica         5
               # historia       7
               # biologia       9

