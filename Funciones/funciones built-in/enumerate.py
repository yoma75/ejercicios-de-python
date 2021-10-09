# funcion enumerate()
# retorna una tupla que contiene un contador (desde start, cuyo valor por defecto es 0) y los valores obtenidos al iterar sobre iterable.

gatos = ['silvestre', 'felix', 'cosmico', 'garfield']

# [(0, 'silvestre'), (1, 'felix'), (2, 'cosmico'), (3, 'garfield')]
print(list(enumerate(gatos)))  


print(list(enumerate(gatos, start=1)))
# [(1, 'silvestre'), (2, 'felix'), (3, 'cosmico'), (4, 'garfield')]

