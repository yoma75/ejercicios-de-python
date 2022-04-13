#  Crea un programa que pida al usuario que introduzca su nombre y un número entero, y escriba su nombre en pantalla tantas veces como indique ese número entero

name = input('Digita tu nombre: ')
cantidad = int(input('Cuantas veces quieres que lo repita: '))

for x in range(0, cantidad):
  print(name)