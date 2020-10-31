# Almacena en una lista los numeros del 1 al 10 y mostralos en orden inverso separados por comas

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()

for x in numeros:
    print(x, end=", ")
