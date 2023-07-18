import numpy as np

# Crear un arreglo de NumPy con valores del 1 al 5
arreglo = np.array([1, 2, 3, 4, 5])

print("Arreglo:", arreglo)

# Operaciones básicas con el arreglo
suma = np.sum(arreglo)             # Suma de todos los elementos
promedio = np.mean(arreglo)        # Promedio de todos los elementos
maximo = np.max(arreglo)           # Valor máximo
minimo = np.min(arreglo)           # Valor mínimo
producto = np.prod(arreglo)        # Producto de todos los elementos
raiz_cuadrada = np.sqrt(arreglo)   # Raíz cuadrada de todos los elementos

# Imprimir los resultados
print(f'Suma: {suma}')                    # Suma: 15
print(f'Promedio: {int(promedio)}')       # Promedio: 3
print(f'Máximo: {maximo}')                # Máximo: 5
print(f'Mínimo: {minimo}')                # Mínimo: 1
print(f'Producto: {producto}')            # Producto: 120
print(f'Raíz cuadrada: {raiz_cuadrada}')  # Raíz cuadrada: [1. 1.41421356 1.73205081 2. 2.23606798]
