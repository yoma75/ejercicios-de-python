'''Encontrar los productos mas caros o mas baratos de un diccionario'''


import heapq

productos = [
  {'articulo': 'mesa', 'precio': 485},
  {'articulo': 'silla', 'precio': 123},
  {'articulo': 'mantel', 'precio': 956},
  {'articulo': 'vasos', 'precio': 647},
  {'articulo': 'cubiertos', 'precio': 254}
]


masBarato = heapq.nsmallest(2, productos, key=lambda pr: pr['precio'])
print(f'Articulos mas baratos: {masBarato}')
# Articulos mas baratos: [{'articulo': 'silla', 'precio': 123}, {'articulo': 'cubiertos', 'precio': 254}]


masCostoso = heapq.nlargest(2, productos, key=lambda pr: pr['precio'])
print(f'Articulos mas costosos: {masCostoso}')
# Articulos mas costosos: [{'articulo': 'mantel', 'precio': 956}, {'articulo': 'vasos', 'precio': 647}]
