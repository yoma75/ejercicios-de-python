# Sumar numeros entrantes hasta digitar 0 para salir:

suma = 0

n = float(input('Digite numero: '))

while n != 0:
  suma += n
  n = float(input('Digite otro numero: '))
print(f'El total de la suma es: {suma}\n')


