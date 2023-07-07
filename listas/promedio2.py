# Dada una lista de números, escribe un programa que encuentre el promedio de todos los elementos de la lista.

listaNumeros = []

for x in range(5):
    numUsuario = int(input(f'{x+1}. numero: '))
    listaNumeros.append(numUsuario)

promedio = sum(listaNumeros) / len(listaNumeros)

print(f'La suma de los numeros es: {sum(listaNumeros)} y su promedio es: {promedio}\n')

    
# 1. numero: 986
# 2. numero: 123
# 3. numero: 593
# 4. numero: 716
# 5. numero: 111
# La suma de los numeros es: 2529 y su promedio es: 505.8
