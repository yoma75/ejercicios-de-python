# --------- Metodos booleanos para strings -------------

cadena = 'Estoy mostrando los metodos booleanos para los strings'

# startswith: verifica si la cadena empieza con el parametro que le especifico.
print(cadena.startswith('E'))  # True
print(cadena.startswith('k'))  # False


# endswith: verifica si la cadena finaliza con el parametro que le especifico.
print(cadena.endswith('s'))  # True
print(cadena.endswith('m'))  # False


# isupper: verifica si la cadena esta toda en mayuscula
print(cadena.isupper())  # False


# islower: verifica si la cadena esta toda en minuscula
print(cadena.islower())  # False
