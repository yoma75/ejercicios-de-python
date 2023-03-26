# Escribir un programa que escriba los numeros del 1 al 100, pero 
# los múltiplos de 3 debe salir la palabra hola y en los
# múltiplos de 5 la palabra Mundo en lugar de los numeros 
# y si el numero es múltiplo de 3 y 5 debe de imprimir holaMundo en lugar del numero 

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("holaMundo")
  elif i % 3 == 0:
    print("hola")
  elif i % 5 == 0:
    print("Mundo")
  else:
    print(i)
