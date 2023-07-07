# Suma de elementos pares: Dada una lista de números enteros, crea un programa que calcule la suma de todos los números pares de la lista.

numerosEnteros = []
suma = 0

for x in range(5):
    numUsuario = int(input(f'{x+1}. Número: '))
    numerosEnteros.append(numUsuario)

for z in numerosEnteros:
    if z % 2 == 0:
        suma = suma + z

print(f'La suma total de los numeros pares es: {suma}\n')


# 1. Número: 46
# 2. Número: 13
# 3. Número: 4
# 4. Número: 97
# 5. Número: 22
# La suma total de los numeros pares es: 72
