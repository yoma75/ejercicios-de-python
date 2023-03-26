# Tabla de multiplicar

numero = int(input('\nCuál tabla de multiplicar desea ver: '))

for n in range(1, 11):
  print(f'{numero} x {n} : {numero * n}')
