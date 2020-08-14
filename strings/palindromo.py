# Decir si la palabra insertada es palindromo o no:

palabra = input('Escribe una palabra: ')

palabra_al_reves = palabra[::-1]
print(palabra_al_reves)

if palabra == palabra_al_reves:
    print('Es palindromo')
else:
    print('No es palindromo')