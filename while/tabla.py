# Tabla de multiplicar

multi = 0
i = 0

numero = int(input('Ingrese el número de la tabla: '))

while i <= 10:
  multi = numero * i
  print(f'{numero} x {i} = {multi}')
  i += 1

