# w: escribir (write)
# r: leer (read)
# a: añadir (append)

ficherito = open('ejemplo2.txt', 'w')

for x in range(1,16):
  if (x % 2 == 0):
    ficherito.write(f'Linea # {x} : par\n')
  else:
    ficherito.write(f'Linea # {x} : impar\n')

ficherito.close()