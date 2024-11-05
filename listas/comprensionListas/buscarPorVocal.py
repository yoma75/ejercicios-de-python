# En una nueva lista agregar los animales que empiecen o tengan la vocal 'a'

animales = ['perro', 'araña', 'aguila', 'delfin', 'ardilla', 'gato']
nuevaLista = []

for x in animales:
  if 'a' in x:
    nuevaLista.append(x)
print(nuevaLista)  # ['araña', 'aguila', 'ardilla', 'gato']


# Con la COMPRENSION DE LISTAS seria asi:
otraNuevaLista = [x for x in animales if 'a' in x]
print(otraNuevaLista)  # ['araña', 'aguila', 'ardilla', 'gato']


# Imprime los valores que no sean 'araña'
newlist = [x for x in animales if x != "araña"]
print(newlist)  # ['perro', 'aguila', 'delfin', 'ardilla', 'gato']


'''
1. x for x in animales: significa que estamos iterando sobre cada elemento x en la lista animales.
2. if 'a' in x: es una condición que filtra los elementos. Solo se incluirán en la nueva lista aquellos elementos x que contengan la letra ‘a’.
'''