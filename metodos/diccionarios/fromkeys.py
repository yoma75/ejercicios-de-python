# fromkeys: retorna un diccionario con las llaves y valores especificos

x = ('key1', 'key2', 'key3')
y = 0

nuevo = dict.fromkeys(x, y)
print(nuevo)  # {'key1': 0, 'key2': 0, 'key3': 0}


# ------------- ejemplo 2 ----------------------------
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)
print(thisdict)  # ['key1': None, 'key2': None, 'key3': None]
