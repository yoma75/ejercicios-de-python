#  map: es útil cuando necesitas aplicar una operación a todos los elementos de una secuencia y quieres obtener los resultados en una nueva lista o iterador.

# map(función, secuencia)

def longitud(n):
  return len(n)

x = map(longitud, ('manzana', 'guama', 'cereza'))
print(list(x))  # [7, 5, 6]

# -------------------------------------------------------------------------------------------------------

def myfunc(a, b):
  return a + b

z = map(myfunc, ('Kever', 'melame', 'cepeda'), ('gotas', 'rico', 'suave'))
print(list(z))  # ['Kevergotas', 'melamerico', 'cepedasuave']

# -------------------------------------------------------------------------------------------------------

def cuadrado(n):
    return n ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = map(cuadrado, numeros)

print(list(cuadrados))  # [1, 4, 9, 16, 25]
