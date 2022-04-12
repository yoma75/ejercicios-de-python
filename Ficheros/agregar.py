# w: escribir (write)
# r: leer (read)
# a: añadir (append)

fichero = open('ejemplo3.txt', 'a')  # 'a' añade al final y si fuera 'w' lo reescribe
paises = ['Colombia ', 'Brasil ', 'Ecuador\n']

fichero.writelines(paises)
fichero.close()