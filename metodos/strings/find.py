# find: devuelve el índice en el que aparece la subcadena (-1 si no aparece):

frase = ("La casa es grande y comoda")
print(frase.find('grande'))  # 11


# Donde se encuentra la vocal 'e' desde el indice 5 al 10
print(frase.find('e', 5, 10))  # 8


# Si no encuentra el valor devuelve -1
print(frase.find('u', 5, 10))  # -1
