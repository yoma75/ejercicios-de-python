# Pedir al usuario que introduzca la suma de 135 y 768, deberá repetirse hasta que introduzca el resultado correcto:

suma =int(input('Cuanto es la suma entre 135 y 768: '))

while suma != 903:
  suma = int(input('Vuelve a intentarlo: '))

print(f'Correcto: la suma entre 135 y 768 es: {suma}')
