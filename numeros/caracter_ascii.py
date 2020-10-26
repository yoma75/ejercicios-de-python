# Obtener el Valor Numérico de un Carácter Numérico ASCII

palabra = input('\nEscriba una palabra para obtener sus caracteres numericos: ')

for x in palabra:
    print('%s: %i' % (x, ord(x))) # ord: devuelve el codigo ASCII de un caracter

