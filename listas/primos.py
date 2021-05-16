# Crear una funcion generadora de números primos entre 0 y 100
# numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
# Utilizar la función generadora para mostrar los números primos menores de 50

numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def primos(maximo):
  for numero in range(maximo):  # genera los números del 0 al 50
    if (numero in numeros_primos):
      yield numero  # yield: función generadora, empieza nuevamente en el bucle
    if (numero > 100):
      break

maximo = 50
for numero in primos(maximo):  # si el número esta en la función 'primos' lo imprime
  print(numero, end=', ')  # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,


  