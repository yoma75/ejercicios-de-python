# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

PASWORD = 'EnaNo'
clave = input('Write your password please: ')

if clave == PASWORD.lower():
    print('Correct password')
else:
    print('incorrect password')

