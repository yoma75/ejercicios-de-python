# append: agrega el nuevo valor al final de la lista

gatos = ['Garfield', 'Michin', 'Silvestre']
print(gatos)  # ['Garfield', 'Michin', 'Silvestre']

gatos.append('Felix')
print(gatos)  # ['Garfield', 'Michin', 'Silvestre', 'Felix']


# insert: agregar un nuevo elemento en cualquier lugar de la lista
# list.insert(location, value)
gatos.insert(1, 'Cosmico')
print(gatos)  # ['Garfield', 'Cosmico', 'Michin', 'Silvestre', 'Felix']

