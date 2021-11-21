# sort: ordena automáticamente los ítems de una lista por su valor de menor a mayor:

numbers = [5, -10, 35, 0, -65, 100]
numbers.sort()
print(numbers)  # [-65, -10, 0, 5, 35, 100]


# Podemos utilizar el argumento reverse=True para indicar que la ordene al revés:
numbers.sort(reverse=True)
print(numbers)  # 100, 35, 5, 0, -10, -65]
