'''
La función devuelve un identificador único para el objeto especificado.id()
Todos los objetos en Python tienen su propio identificador único.
El identificador se asigna al objeto cuando se crea.

El id es la dirección de memoria del objeto y será diferente para cada vez ejecutar el programa. (excepto para algún objeto que tenga un identificador único constante, como enteros de -5 a 256)
'''

animals = ('gato', 'delfin', 'tigre')
print(id(animals))  # 1893664948352 este numero sera diferente cada vez que se ejecuta el archivo
