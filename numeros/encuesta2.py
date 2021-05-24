# encuesta:
# opciones: 5. Excelente, 4. Muy buena, 3. Buena, 2. Regular, 1. No satisfactoria
# Realice un programa que registre en un arreglo la evaluación de pacientes atendidos
# Mostrar las respuestas que cada uno de los pacientes


import pandas as pd

valor_guardado = []
opc = 0

while (opc <= 6):
  opc = int(input(f'''\nDigite su opcion:
      5. Excelente
      4. Muy buena
      3. Buena
      2. Regular
      1. No satisfactoria
  '''))

  if ((opc == 5) or (opc == 4) or (opc == 3) or (opc == 2) or (opc == 1)):
    valor_guardado.append(opc)  
  else:
    print(f'No existe esta opcion\n')

print(f'\n {valor_guardado}')

serie = pd.Series(valor_guardado)
repetidos = serie.value_counts()
print(repetidos)


