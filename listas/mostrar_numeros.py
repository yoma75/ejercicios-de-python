"""Introduzca un número (0 para terminar): 3 
Introduzca un número (0 para terminar): 5 
Introduzca un número (0 para terminar): 9 
Introduzca un número (0 para terminar): -1 
Introduzca un número (0 para terminar): -5 
Introduzca un número (0 para terminar): 7 
Introduzca un número (0 para terminar): 8 
Introduzca un número (0 para terminar): 12 
Introduzca un número (0 para terminar): 17 
Introduzca un número (0 para terminar): 9 

Los números tecleados son: 9 17 12 8 7 -5 -1 9 5 3 

Introduzca un número entero (0 para terminar): 12
Introduzca un número entero (0 para terminar): -6
Introduzca un número entero (0 para terminar): 3
Introduzca un número entero (0 para terminar): 0

Los números tecleados son: 3 -6 12  """

lista_numeros=[]

print()
for x in range(7):    
        numero = int(input(f'{x+1}. Introduzca un numero (0 para terminar): '))
        lista_numeros.append(numero)
        if numero == 0:
            break;

print()

if numero == 0:
    lista_numeros.pop()

print(f'Los numeros digitados de atrás para delante son: {lista_numeros[::-1]}')




