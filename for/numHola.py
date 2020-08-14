# Escribir un programa que escriba los numeros del 1 al 100, pero 
# los multiplos de 3 debe salir la palabra hola y en los
# multiplos de 5 la palabra Mundo en lugar de los numeros 
# y si el numero es multiplo de 3 y 5 debe de imprimir holaMundo en
# lugar del numero 

for x in range(100):
    
    if x % 3==0:
        print('hola')
    elif x % 5==0:
        print('Mundo')
    else:
        print('HolaMundo')

