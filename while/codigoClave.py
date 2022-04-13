# Pide un código y una contraseña al usuario. No se le dejará proseguir hasta que el código sea 1234 y la clave sea 5000

codigo = int(input('Digite su código: '))
clave = int(input('Digite su clave: '))

while not ((codigo == 1234) and (clave == 5000)):
  print('Acceso denegado'.upper())
  codigo = int(input('\nDigite su código: '))
  clave = int(input('Digite su clave: '))

print('Acceso concedido')