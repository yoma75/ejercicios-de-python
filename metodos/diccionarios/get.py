# get: busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto:
# clave:valor
# key:value

colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }

print(colores.get('negro','no se encuentra'))  # no se encuentra
print(colores.get('azul','no se encuentra'))  # blue
