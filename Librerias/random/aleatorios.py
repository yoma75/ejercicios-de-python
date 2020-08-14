# Generar un Conjunto de Números Aleatorios y Determinar Cuáles son Impares

from random import randint

numeros_aleatorios = [randint(1, 100) for _ in range(10)] # 10 numeros en la lista
print()
print(numeros_aleatorios)
print()

for x in numeros_aleatorios:
    if x % 2 == 1:        
        print(x)

