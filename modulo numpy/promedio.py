import numpy as np

# Lista de números
numeros = [5, 10, 15, 20, 25]

# Convertir la lista en un arreglo de NumPy
arreglo_numeros = np.array(numeros)

# Calcular el promedio utilizando la función mean()
promedio = np.mean(arreglo_numeros)

print(f'El promedio es: {int(promedio)}')  # El promedio es: 15
