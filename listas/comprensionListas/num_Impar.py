# lista los numeros impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numImpares = [x for x in numeros if x % 2 != 0]

print(numImpares)  # [1, 3, 5, 7, 9]
