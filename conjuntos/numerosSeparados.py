# Obtener un Conjunto de Números Seperados por Coma y Crear una Lista:

entrada = input('\nEscriba varios numeros separados por una coma: '.upper())
print(type(entrada))
print('-------------------------------------------------------------')

numeros = entrada.split(',')
print(type(numeros))
print(numeros)

# Split: convierte una cadena de texto en una lista.
