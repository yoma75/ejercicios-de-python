'''all: devuelve "True" si todos los elementos de un iterable son verdaderos, y "False" si al menos uno de ellos es falso o si el iterable está vacío. "iterable" es cualquier objeto como una lista, una tupla, un conjunto, un diccionario'''

# Por ejemplo, si tenemos una lista de números y queremos verificar si todos los números son mayores que cero, podemos usar la función "all"
numeros = [1, 2, 3, 4, 5]
mayores_que_cero = all(num > 0 for num in numeros)
print(mayores_que_cero)  # True


# si tenemos una lista que contiene al menos un elemento falso, la función "all" devolverá "False"
valores = [True, False, True]
todos_verdaderos = all(valores)
print(todos_verdaderos)  # False
