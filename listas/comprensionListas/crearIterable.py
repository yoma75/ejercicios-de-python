# Crear un iterable = un rango de numeros del 0 al 9
numeros = [x for x in range(10)]
print(numeros)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Con una condicion
newlist = [x for x in range(10) if x < 5]
print(newlist)  # [0, 1, 2, 3, 4]
