import numpy as np

numeros = np.arange(5)
print(numeros)
print(f'raiz cuadrada: {np.sqrt(numeros)}\n')


# Crear numeros aleatorios
numeros1 = np.random.rand(5)
print(f'{numeros1}\n')


# sumar arrays
lista = [5,6,7,8,9]
numeros2 = np.array(lista)
print(numeros)  # [0 1 2 3 4]
print(lista)  # [5, 6, 7, 8, 9]
suma = np.add(numeros,numeros2)
print(f'Suma de los dos arrays: {suma}')  # [ 5  7  9 11 13]


