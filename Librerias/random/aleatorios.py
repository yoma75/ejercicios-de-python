# Generar un conjunto de números aleatorios y determinar cuáles son impares

from random import randint

numeros_aleatorios = [randint(1, 100) for _ in range(10)] # 10 numeros en la lista

print(f'\n {numeros_aleatorios}')

for x in numeros_aleatorios:
    if x % 2 == 1:        
        print(x)

