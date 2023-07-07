# Programa que permita ingresar 5 números y calcular el promedio

lista = []
suma = 0

for x in range(5):
    numeros = int(input('{}. Digite un numero: '.format(x+1)))
    lista.append(numeros)

for i in lista:
    suma = suma + i

print(f'La suma es: {suma} y su promedio es: {suma / len(lista)}\n')
