'''zip: se utiliza para combinar dos o más iterables en una sola estructura de datos. La función toma como entrada dos o más iterables y devuelve un iterable que contiene TUPLAS de elementos correspondientes de los iterables originales
Sintaxis: zip(iterable1, iterable2, iterable3, ...) 
Donde "iterable1", "iterable2", "iterable3", etc. son los iterables que se quieren combinar.'''


# Por ejemplo, si tenemos dos listas "lista1" y "lista2" y queremos combinarlas en una lista de tuplas de elementos correspondientes, podemos usar la función "zip"
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista_combinada = list(zip(lista1, lista2))
print(lista_combinada)  # [(1, 'a'), (2, 'b'), (3, 'c')]


# También se puede utilizar con más de dos iterables. Por ejemplo, si tenemos tres listas "lista1", "lista2" y "lista3", podemos combinarlas en una lista de tuplas de tres elementos 
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = ['X', 'Y', 'Z']
lista_combinada = list(zip(lista1, lista2, lista3))
print(lista_combinada)  # [(1, 'a', 'X'), (2, 'b', 'Y'), (3, 'c', 'Z')]
