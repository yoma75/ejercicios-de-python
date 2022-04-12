# w: escribir (write)
# r: leer (read)
# a: añadir (append)

fichero = open('ejemplo3.txt', 'w')
puestos = ['primero\n', 'segundo\n', 'tercero\n']
animales = ['perro ', 'caballo ', 'dinosaurio\n']

fichero.writelines(puestos)
fichero.writelines(animales)
fichero.close()