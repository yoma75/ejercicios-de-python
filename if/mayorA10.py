# Escribe un programa que le pida un número al usuario e imprima en la consola si el número es mayor o menor/igual a 10.
# Si es mayor debe imprimir "El número es mayor a 10".
# Si es menor debe imprimir "El número es menor o igual a 10".

numero = int(input('Digite número: '))

if numero > 10:
  print(f'El número {numero} es mayor a 10')
elif numero < 10:
  print(f'El número {numero} es menor a 10')
elif numero == 10:
  print(f'El número {numero} es igual a 10')
