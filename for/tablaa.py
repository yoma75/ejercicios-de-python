# Pide al usuario un número entero (por ejemplo, 5) y muestra la tabla de multiplicar de ese número (desde "5 x 1 = 5" hasta "5 x 10 = 50").

numero = int(input('\nCuál tabla de multiplicar desea ver: '))

for n in range(1, 11):
  print(f'{numero} x {n} : {numero * n}')
