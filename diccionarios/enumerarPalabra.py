'''Enumera cada una de las palabras y vocales, y las repetidas las va sumando'''

palabra = 'brontosaurio'

d = dict()
for c in palabra:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1

print(f'\n{d}')

# El bucle for recorre la cadena. Cada vez que entramos al bucle, si el caracter c no
# está en el diccionario, creamos un nuevo elemento con la clave c y el valor inicial
# 1 (debido a que hemos visto esta letra solo una vez). Si c ya está previamente en
# el diccionario incrementamos d[c].

# {'b': 1, 'r': 2, 'o': 3, 'n': 1, 't': 1, 's': 1, 'a': 1, 'u': 1, 'i': 1}
