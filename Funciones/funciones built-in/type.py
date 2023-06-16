# type: retorna el tipo del objeto especificado

def tipoDato(valor):
    return type(valor)

print(tipoDato(45))  # <class 'int'>
print(tipoDato(98.5))  # <class 'float'>
print(tipoDato('Hola Python!'))  # <class 'str'>
print(tipoDato(['a', 'e', 'i', 'o', 'u']))  # <class 'list'>
print(tipoDato(('a', 'e', 'i', 'o', 'u')))  # <class 'tuple'>
print(tipoDato({'animal':'salvaje', 'edad': 3}))  # <class 'dict'>
