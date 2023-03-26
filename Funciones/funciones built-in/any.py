'''any: devuelve "True" si al menos uno de los elementos de un iterable es verdadero, y "False" si todos los elementos son falsos o si el iterable está vacío'''

# Por ejemplo, si tenemos una lista de números y queremos verificar si al menos uno de ellos es mayor que 10, podemos usar la función "any" 
numeros = [5, 8, 12, 3, 7]
alguno_mayor_que_diez = any(num > 10 for num in numeros)
print(alguno_mayor_que_diez)  # True


# devuelve "False" porque todos los elementos de la lista "valores" son falsos.
valores = [False, 0, '', None]
alguno_verdadero = any(valores)
print(alguno_verdadero)  # False
