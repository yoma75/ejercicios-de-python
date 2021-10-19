# items: genera una lista en clave-valor de los registros del diccionario::
# clave:valor

colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
print(colores.items())  # dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])


for clave, valor in colores.items():
    print(clave, valor)   # amarillo yellow
                          # azul blue
                          # verde green

