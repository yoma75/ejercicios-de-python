# Ordenar una lista de cadenas por su longitud

frutas = ['manzana', 'pera', 'banano', 'cereza', 'guama']

ordenar = sorted(frutas, key = lambda x: len(x))
print(ordenar)  # ['pera', 'guama', 'banano', 'cereza', 'manzana']


''' se utiliza la función sorted para ordenar la lista de frutas en función de la longitud de cada cadena. La función lambda se pasa como el argumento key y se aplica a cada elemento de la lista para determinar el criterio de ordenamiento.'''
