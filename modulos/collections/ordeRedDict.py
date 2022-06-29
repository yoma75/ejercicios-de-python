'''Ordenar un diccionario'''

from collections import OrderedDict

articulos = {7: 'mesa', 3: 'sillas', 2: 'sofa', 6: 'alfombra', 5: 'cuadro'}

# Ordenado por la llave
# OrderedDict([(2, 'sofa'), (3, 'sillas'), (5, 'cuadro'), (6, 'alfombra'), (7, 'mesa')])
print(OrderedDict(sorted(articulos.items(), key=lambda p: p[0])))


# ordenado por el nombre del articulo
# OrderedDict([(6, 'alfombra'), (5, 'cuadro'), (7, 'mesa'), (3, 'sillas'), (2, 'sofa')])
print(OrderedDict(sorted(articulos.items(), key=lambda p: p[1])))
