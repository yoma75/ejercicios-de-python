# encuesta:
# opciones: 5. Excelente, 4. Muy buena, 3. Buena, 2. Regular, 1. No satisfactoria
# Realice un programa que registre en un arreglo la evaluación de pacientes atendidos
# Mostrar las respuestas que cada uno de los pacientes


# encuesta:
# opciones: 5. Excelente, 4. Muy buena, 3. Buena, 2. Regular, 1. No satisfactoria
# Realice un programa que registre en un arreglo la evaluación de pacientes atendidos
# Mostrar las respuestas que cada uno de los pacientes

import numpy as np

valor_guardado = []
cont5, cont4, cont3, cont2, cont1 = 0,0,0,0,0
opc = 0

while (opc <= 6):
  opc = int(input(f'''\nDigite su opcion:
      5. Excelente
      4. Muy buena
      3. Buena
      2. Regular
      1. No satisfactoria
  '''))

  if (opc == 5):
    valor_guardado.append(opc)
    cont5 += 1
  elif (opc == 4):
    valor_guardado.append(opc)
    cont4 += 1
  elif (opc == 3):
    valor_guardado.append(opc)
    cont3 += 1
  elif (opc == 2):
    valor_guardado.append(opc)
    cont2 += 1
  elif (opc == 1):
    valor_guardado.append(opc)
    cont1 += 1
  else:
    print(f'No existe esta opcion\n')
  
convertir_a_array = np.array(valor_guardado)
print(f'{convertir_a_array}\n')

print(f'5. Excelentes: {cont5}')
print(f'4. Muy buena: {cont4}')
print(f'3. Buena: {cont3}')
print(f'2. Regular: {cont2}')
print(f'1. No satisfactoria: {cont1}')

