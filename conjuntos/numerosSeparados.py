# Obtener un Conjunto de Números Seperados por Coma y Crear una Lista:

entrada = input('\nEscriba varios numeros separados por una coma: '.upper())
print(type(entrada))  # <class 'str'>
print('-------------------------------------------------------------')


# Split: convierte una cadena de texto en una lista.
numeros = entrada.split(',')
print(type(numeros))  # <class 'list'>
print(numeros)

