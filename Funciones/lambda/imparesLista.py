# Extraer los numeros impares de una lista

numeros = [1,2,3,4,5,6,7,8,9,10,11]
impares = list(filter(lambda x: x % 2 != 0, numeros))

print(impares)  # [1, 3, 5, 7, 9, 11]
