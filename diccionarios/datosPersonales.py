'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''

persona = {}
information = 's'

while information == 's':
    key = input('\nQue llave deseas introducir: ')

    value = input(key + ': ')
    persona[key] = value
    
    information = input('\n¿Quieres añadir más información (s/n)? ')

print(f'{persona}\n')

