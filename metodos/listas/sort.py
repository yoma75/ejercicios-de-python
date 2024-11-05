# sort: ordena automáticamente los ítems de una lista por su valor de menor a mayor:
numbers = [5, -10, 35, 0, -65, 100]
numbers.sort()
print(numbers)  # [-65, -10, 0, 5, 35, 100]


# El argumento reverse=True ordena DESCENDENTEMENTE:
numbers.sort(reverse=True)
print(numbers)  # 100, 35, 5, 0, -10, -65]


# Tambien sirve para ordenar alfabeticamente una lista
frutas = ['naranja', 'mango', 'kiwi', 'sandia', 'banano']
frutas.sort()
print(frutas)  # ['banano', 'kiwi', 'mango', 'naranja', 'sandia']


# Ordenar alfabeticamente sin tener en cuenta si son mayusculas
frutas = ['naranja', 'Mango', 'kiwi', 'Sandia', 'Banano']
frutas.sort(key = str.lower)
print(frutas)  # ['Banano', 'kiwi', 'Mango', 'naranja', 'Sandia']
