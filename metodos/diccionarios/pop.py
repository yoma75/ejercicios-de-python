# pop: extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto:

colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }

print(colores.pop("amarillo", "no se ha encontrado"))  # yellow
print(colores.pop("negro","no se ha encontrado"))  # no se ha encontrado
