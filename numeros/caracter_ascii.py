# Obtener el Valor Numérico de un Carácter Numérico ASCII

palabra = input('\nEscriba una palabra para obtener sus caracteres numéricos: ')

for x in palabra:
    print('%s: %i' % (x, ord(x))) # ord: devuelve el código ASCII de un carácter

