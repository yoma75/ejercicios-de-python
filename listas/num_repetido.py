# Programa que permita ingresar N números y determine cuantas veces aparece el mismo número, dicho número a buscar debe solicitarse al usuario al inicio del programa. 

lista = []
i, contador = 0, 0

while i < 7:
    numero = int(input('Ingrese un numero: '))
    lista.append(numero)
    i = i+1

print()
pedir = int(input('Cual numero desea buscar: '))

for x in lista:
    if x == pedir:
        contador = contador + 1

print(f'El numero {pedir} se repite {contador} veces')
