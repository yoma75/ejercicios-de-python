# Programa que permita ingresar 5 números y calcular el promedio

lista=[]

for x in range(5):
    numeros = int(input('{}. Digite un numero: '.format(x+1)))
    lista.append(numeros)

# for i in notas:
#     suma = suma + i

suma = (lista[0]+lista[1]+lista[2]+lista[3]+lista[4])
promedio = suma // 5

print('')
print(f'La suma de los numeros: {lista[0]}, {lista[1]}, {lista[2]}, {lista[3]} y {lista[4]} es: {suma}'.upper())
print(f'y su promedio es de: {promedio}'.upper())

print(f'Otra forma mas rápida de hacer: {sum(lista)}')

