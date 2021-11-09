dividendo = int(input('Cual es el dividendo: '))
divisor = int(input('Cual es el divisor: '))

while divisor == 0:
  divisor = int(input('El divisor no puede ser cero: '))
print(f'La división es: {dividendo / divisor}\n')
