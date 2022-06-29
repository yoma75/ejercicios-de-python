'''
Obtener los elementos mas frecuentes de una lista
.most_common(n) = enumera los n elementos más comunes y sus recuentos desde el más común hasta el menos común. Si n es ninguno, enumera todos los recuentos de los elementos.
'''

from collections import Counter

numeros = [4, 9, 7, 4, 63, 45, 9, 7, 7]

contador = Counter(numeros)
print(contador.most_common(3))
# [(7, 3), (4, 2), (9, 2)] el numero 7 esta 3 veces, el numero 4 esta 2 veces, etc


print(contador.most_common())
# [(7, 3), (4, 2), (9, 2), (63, 1), (45, 1)]

# ---------------------------------------------------------------------

frase = 'Python es un lenguaje de programacion fácil de aprender'
print(Counter(frase).most_common(3))

# [(' ', 8), ('e', 7), ('n', 5)]
# espacios = 8 veces
# vocal e = 7 veces
# letra n = 5 veces
