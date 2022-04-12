# w: escribir (write)
# r: leer (read)
# a: añadir (append)

fichero = open('ejemplo1.txt', 'r')
lineas = fichero.readlines()
fichero.close()

print(lineas)
# ['Este es el primer ejemplo de escritura\n', 'La casa es grande\n']
