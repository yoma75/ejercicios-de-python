# Tenemos una lista de números y queremos crear una nueva lista que contenga el cuadrado de cada número en la lista original:

# cuadrados = [expresion for elemento in lista_existente]

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros]

print(cuadrados)  # [1, 4, 9, 16, 25]
