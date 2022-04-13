# Pide al usuario 3 frases y guárdalas en un fichero "frases.txt".

lineas = []

for x in range(0, 3):
  frase = input('Escribe una frase: ')
  lineas.append(f'{frase}\n')

fichero = open('ejemplo4.txt', 'w')
fichero.writelines(lineas)
fichero.close()